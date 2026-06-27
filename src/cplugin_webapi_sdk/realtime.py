"""Real-time SignalR clients for the MT4/MT5 v2 hubs.

! EXPERIMENTAL. There is no official Python SignalR client; this wraps the
  community library ``signalrcore``, which is an OPTIONAL dependency. Install with::

      pip install "mywebapi-sdk[signalr]"

  The REST surface of this SDK works without it — only these realtime clients
  require it, and they raise ``SignalRNotInstalledError`` with an install hint if
  it is missing.

! ``signalrcore`` is callback-first (synchronous observer model), unlike the
  TypeScript ``@microsoft/signalr`` async-iterable surface. Streams therefore
  take a callback via ``.subscribe()`` and return a subscription handle, rather
  than yielding via ``async for``.

Usage::

    from cplugin_webapi_sdk import CPluginWebApiClient

    with CPluginWebApiClient(env="staging", client_id=..., client_secret=...) as c:
        rt = c.realtime.mt4("my-trade-platform-id")
        rt.on_connection_status(lambda *args: print("status", args))
        rt.on_tick(lambda *args: print("tick", args))

        with rt:  # calls start() / stop()
            rt.subscribe_to_ticks("EURUSD")
            import time; time.sleep(5)
"""
from __future__ import annotations

from typing import Any, Callable, Optional
from urllib.parse import quote


# ---------------------------------------------------------------------------
# Error surface
# ---------------------------------------------------------------------------


class SignalRNotInstalledError(RuntimeError):
    """Raised when a realtime client is constructed but ``signalrcore`` is absent.

    The ``signalrcore`` package is an optional dependency of this SDK. Install it
    with the ``[signalr]`` extra::

        pip install "mywebapi-sdk[signalr]"
    """

    def __init__(self) -> None:
        super().__init__(
            "Real-time streaming requires the optional 'signalrcore' dependency. "
            'Install it with:  pip install "mywebapi-sdk[signalr]"'
        )


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _import_signalr():
    """Return ``HubConnectionBuilder`` from ``signalrcore``.

    * Lazy import isolated in a helper so tests can monkeypatch it and so the
    *   package imports cleanly when the extra is not installed.
    """
    try:
        from signalrcore.hub_connection_builder import HubConnectionBuilder  # type: ignore
    except ImportError as exc:  # ! callers convert this to SignalRNotInstalledError
        raise ImportError("signalrcore not installed") from exc
    return HubConnectionBuilder


def _build_hub_url(base_url: str, platform: str, trade_platform: str) -> str:
    """Build the fully-qualified hub WebSocket URL.

    * Mirror the TS hub-URL construction exactly: strip trailing slashes off
    *   the base, append ``/hubs/<platform>/v2``, then the URL-encoded
    *   ``tradePlatform`` query parameter.

    Args:
        base_url:       Resolved API base URL (trailing slash stripped here).
        platform:       Hub platform segment — ``"mt4"`` or ``"mt5"``.
        trade_platform: Trade platform identifier (URL-encoded in output).

    Returns:
        Fully-qualified URL string for the hub negotiate endpoint.
    """
    base = base_url.rstrip("/")
    return f"{base}/hubs/{platform}/v2?tradePlatform={quote(trade_platform, safe='')}"


# ---------------------------------------------------------------------------
# Base connection lifecycle
# ---------------------------------------------------------------------------


class _BaseRealtimeClient:
    """Shared connection lifecycle for the MT4/MT5 realtime clients.

    ! EXPERIMENTAL — see module docstring for caveats on ``signalrcore``.

    Subclasses set ``_PLATFORM`` to ``"mt4"`` or ``"mt5"`` and expose
    platform-specific callback and stream methods on top.
    """

    # * Overridden by MT4RealtimeClient / MT5RealtimeClient.
    _PLATFORM: str = ""

    def __init__(
        self,
        *,
        base_url: str,
        token_factory: Callable[[], str],
        trade_platform: str,
    ) -> None:
        """Construct and wire the hub connection.

        Args:
            base_url:       Resolved API base URL (e.g. ``https://pre.mywebapi.com``).
            token_factory:  Zero-arg callable returning the current bearer token
                            string. ``signalrcore`` calls this at negotiate time
                            and attaches the result as ``?access_token=…`` on the
                            WebSocket handshake.
            trade_platform: Platform identifier appended as ``?tradePlatform=…``
                            on the hub URL.

        Raises:
            ValueError:              If ``trade_platform`` is empty.
            SignalRNotInstalledError: If ``signalrcore`` is not installed.
        """
        if not trade_platform:
            raise ValueError("trade_platform is required")

        try:
            builder_cls = _import_signalr()
        except ImportError:
            raise SignalRNotInstalledError() from None

        self.hub_url: str = _build_hub_url(base_url, self._PLATFORM, trade_platform)
        self._token_factory: Callable[[], str] = token_factory

        # * access_token_factory lets signalrcore fetch a fresh token at negotiate
        # *   time and append it as ?access_token=… for the WebSocket handshake.
        self._conn = (
            builder_cls()
            .with_url(
                self.hub_url,
                options={"access_token_factory": token_factory},
            )
            .build()
        )
        self._started: bool = False

    # * --- lifecycle ---------------------------------------------------------

    def on_connection_status(self, handler: Callable[[Any], None]) -> None:
        """Register a callback for ``OnConnectionStatus`` events from the hub.

        ! Register all callbacks BEFORE ``start()`` — ``signalrcore`` may drop
        !   handlers registered after the connection is already open. Same race
        !   the TS client guards against with a pending-handler queue.

        Args:
            handler: Callable invoked with the raw event payload when the hub
                     broadcasts a connection status change.
        """
        # ! Register before start() — signalrcore may drop late handlers.
        self._conn.on("OnConnectionStatus", handler)

    def start(self) -> None:
        """Open the WebSocket connection to the hub.

        ! Register all callbacks BEFORE calling ``start()`` — see the class
        !   docstring for the handler-registration ordering requirement.
        """
        self._conn.start()
        self._started = True

    def stop(self) -> None:
        """Close the WebSocket connection to the hub."""
        if self._started:
            self._conn.stop()
            self._started = False

    def __enter__(self) -> "_BaseRealtimeClient":
        self.start()
        return self

    def __exit__(self, *exc: Any) -> None:
        self.stop()

    def _stream(self, method: str, args: Optional[list] = None):
        """Return a ``StreamHandler`` for the named server-streaming method.

        * ``signalrcore`` stream() returns an observable; call ``.subscribe(observer)``
        *   on the result to wire ``next`` / ``complete`` / ``error`` callbacks::
        *
        *     rt.stream_trades().subscribe({
        *         "next": lambda item: print(item),
        *         "complete": lambda: print("done"),
        *         "error": lambda err: print("err", err),
        *     })

        Args:
            method: Server-streaming method name (e.g. ``"StreamTrades"``).
            args:   Optional positional arguments passed to the server method.

        Returns:
            ``signalrcore.hub.handlers.StreamHandler`` — call ``.subscribe()`` on it.
        """
        return self._conn.stream(method, args or [])


# ---------------------------------------------------------------------------
# MT4 realtime client
# ---------------------------------------------------------------------------


class MT4RealtimeClient(_BaseRealtimeClient):
    """Real-time client for the MT4 v2 hub (``/hubs/mt4/v2``).

    ! EXPERIMENTAL — see module docstring.

    Obtain via ``client.realtime.mt4(trade_platform)``; do NOT instantiate
    directly unless you manage the ``base_url`` and ``token_factory`` yourself.

    Server method names mirror the TypeScript SDK verbatim::

        Callbacks:  OnTick, OnConnectionStatus
        Invokes:    SubscribeToTicks, UnsubscribeFromTicks
        Streams:    StreamTicks, StreamTrades, StreamUserUpdates,
                    StreamSymbolUpdates, StreamMarginCallUpdates
    """

    _PLATFORM = "mt4"

    # * --- callbacks --------------------------------------------------------

    def on_tick(self, handler: Callable[[Any], None]) -> None:
        """Register a callback for ``OnTick`` events broadcast by the hub.

        ! Register before ``start()`` — see lifecycle ordering note.

        Args:
            handler: Callable invoked with the raw tick payload per event.
        """
        # ! Register before start() — signalrcore may drop late handlers.
        self._conn.on("OnTick", handler)

    # * --- invocations ------------------------------------------------------

    def subscribe_to_ticks(self, symbol: str) -> None:
        """Ask the server to start pushing ``OnTick`` events for ``symbol``.

        Args:
            symbol: Instrument name (e.g. ``"EURUSD"``).
        """
        self._conn.send("SubscribeToTicks", [symbol])

    def unsubscribe_from_ticks(self, symbol: str) -> None:
        """Ask the server to stop pushing ``OnTick`` events for ``symbol``.

        Args:
            symbol: Instrument name (e.g. ``"EURUSD"``).
        """
        self._conn.send("UnsubscribeFromTicks", [symbol])

    # * --- server-streaming methods -----------------------------------------
    # * Call .subscribe({"next": cb, "complete": cb, "error": cb}) on each.

    def stream_ticks(self, symbol: str):
        """Stream server-side tick data for a single symbol.

        Args:
            symbol: Instrument name (e.g. ``"EURUSD"``).

        Returns:
            ``signalrcore.hub.handlers.StreamHandler`` — call ``.subscribe()``.
        """
        return self._stream("StreamTicks", [symbol])

    def stream_trades(self):
        """Stream open trade updates.

        Returns:
            ``signalrcore.hub.handlers.StreamHandler`` — call ``.subscribe()``.
        """
        return self._stream("StreamTrades")

    def stream_user_updates(self):
        """Stream user account change events.

        Returns:
            ``signalrcore.hub.handlers.StreamHandler`` — call ``.subscribe()``.
        """
        return self._stream("StreamUserUpdates")

    def stream_symbol_updates(self):
        """Stream symbol configuration change events.

        Returns:
            ``signalrcore.hub.handlers.StreamHandler`` — call ``.subscribe()``.
        """
        return self._stream("StreamSymbolUpdates")

    def stream_margin_call_updates(self):
        """Stream margin-call status events.

        Returns:
            ``signalrcore.hub.handlers.StreamHandler`` — call ``.subscribe()``.
        """
        return self._stream("StreamMarginCallUpdates")


# ---------------------------------------------------------------------------
# MT5 realtime client
# ---------------------------------------------------------------------------


class MT5RealtimeClient(_BaseRealtimeClient):
    """Real-time client for the MT5 v2 hub (``/hubs/mt5/v2``).

    ! EXPERIMENTAL — see module docstring.

    Obtain via ``client.realtime.mt5(trade_platform)``; do NOT instantiate
    directly unless you manage the ``base_url`` and ``token_factory`` yourself.

    Server method names mirror the TypeScript SDK verbatim::

        Callbacks:  OnConnectionStatus
        Streams:    StreamMarginCallUpdates
    """

    _PLATFORM = "mt5"

    # * --- server-streaming methods -----------------------------------------

    def stream_margin_call_updates(self):
        """Stream margin-call status events from the MT5 hub.

        Returns:
            ``signalrcore.hub.handlers.StreamHandler`` — call ``.subscribe()``.
        """
        return self._stream("StreamMarginCallUpdates")


# ---------------------------------------------------------------------------
# Namespace factory
# ---------------------------------------------------------------------------


class RealtimeNamespace:
    """Factory bound to a client's base URL and token provider.

    Exposed as ``client.realtime``; call ``.mt4(tp)`` / ``.mt5(tp)`` to create
    a hub client for a specific trade platform.

    ! Requires the optional ``signalrcore`` extra — see module docstring.
    """

    def __init__(
        self,
        *,
        base_url: str,
        token_factory: Callable[[], str],
    ) -> None:
        self._base_url = base_url
        self._token_factory = token_factory

    def mt4(self, trade_platform: str) -> MT4RealtimeClient:
        """Create an MT4 realtime hub client for the given trade platform.

        Args:
            trade_platform: Trade platform identifier (UUID string or slug).

        Returns:
            A new :class:`MT4RealtimeClient` — call ``start()`` / ``stop()``
            or use it as a context manager.

        Raises:
            SignalRNotInstalledError: If ``signalrcore`` is not installed.
        """
        return MT4RealtimeClient(
            base_url=self._base_url,
            token_factory=self._token_factory,
            trade_platform=trade_platform,
        )

    def mt5(self, trade_platform: str) -> MT5RealtimeClient:
        """Create an MT5 realtime hub client for the given trade platform.

        Args:
            trade_platform: Trade platform identifier (UUID string or slug).

        Returns:
            A new :class:`MT5RealtimeClient` — call ``start()`` / ``stop()``
            or use it as a context manager.

        Raises:
            SignalRNotInstalledError: If ``signalrcore`` is not installed.
        """
        return MT5RealtimeClient(
            base_url=self._base_url,
            token_factory=self._token_factory,
            trade_platform=trade_platform,
        )
