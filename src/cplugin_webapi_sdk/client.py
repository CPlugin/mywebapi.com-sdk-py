"""Ergonomic facade over the generated WebAPI v2 layer.

Both ``CPluginWebApiClient`` (sync) and ``CPluginWebApiAsyncClient`` (async)
expose ``.mt4`` / ``.mt5`` namespaces of clean snake_case methods, share one
authenticated httpx client, and surface ``list_trade_platforms()`` (v1 raw
endpoint) plus a ``paged()`` seam for cursor-based iteration.

Both expose ``.mt4`` and ``.mt5`` namespaces of clean snake_case methods over the
generated endpoint functions, sharing one authenticated httpx client. Auth is
lazy: tokens are fetched on first request, cached, refreshed before expiry, and
re-fetched on a 401 (see auth.ClientCredentialsAuth). Real-time SignalR is
available via the ``.realtime`` namespace (optional ``signalrcore`` extra; Task 9).

Usage::

    client = CPluginWebApiClient(env="staging", client_id=..., client_secret=...)
    t = client.mt4.get_server_time("my-tp")
    for page in client.paged(lambda cur: client.mt4.users_request("my-tp", cursor=cur)):
        ...
"""
from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Callable, Generator, AsyncGenerator
from uuid import UUID

import httpx

from .auth import BearerAuth, ClientCredentialsAuth
from .environments import EnvironmentName, resolve_environment
from .realtime import RealtimeNamespace
from .timeouts import (
    DEFAULT_TRANSPORT_TIMEOUT,
    IDEMPOTENCY_KEY_HEADER,
    REQUEST_TIMEOUT_HEADER,
    format_seconds,
    operation_default_timeout,
    transport_timeout,
    validate_idempotency_key,
    validate_request_timeout,
)
from .unwrap import unwrap, unwrap_async, unwrap_with_meta, unwrap_with_meta_async
from ._generated.types import Unset

# * Generated op modules — paths verified against ls _generated/api/.
# * Tag slugs use _v_2_ (with underscores around the digit), e.g. mt4_v_2_common.
from ._generated.api.mt4_v_2_common import (
    get_api_v_2_mt4_trade_platform_server_time as _mt4_server_time,
    get_api_v_2_mt4_trade_platform_manager_common as _mt4_manager_common,
)
from ._generated.api.mt4_v_2_users import (
    get_api_v_2_mt4_trade_platform_users_request as _mt4_users_request,
    get_api_v_2_mt4_trade_platform_user_record_get_login as _mt4_user_record_get,
    patch_api_v_2_mt4_trade_platform_user_record_login as _mt4_user_record_patch,
)
from ._generated.models.patch_api_v2mt4_trade_platform_user_record_login_json_body import (
    PatchApiV2MT4TradePlatformUserRecordLoginJsonBody as _MT4UserRecordPatchBody,
)
from ._generated.api.mt4_v_2_symbols import (
    get_api_v_2_mt4_trade_platform_cfg_request_symbol as _mt4_symbols_list,
    get_api_v_2_mt4_trade_platform_symbol_info_get as _mt4_symbol_info,
)
from ._generated.api.mt4_v_2_groups import (
    get_api_v_2_mt4_trade_platform_ensure_group_name_exist_group as _mt4_group_exists,
)
from ._generated.api.mt4_v_2_trades import (
    get_api_v_2_mt4_trade_platform_trades_request as _mt4_trades_request,
)
from ._generated.api.mt4_v_2_dealer import (
    get_api_v_2_mt4_trade_platform_summary_get_all as _mt4_summary_get_all,
    get_api_v_2_mt4_trade_platform_summary_get_symbol as _mt4_summary_get,
    get_api_v_2_mt4_trade_platform_summary_currency as _mt4_summary_currency,
    get_api_v_2_mt4_trade_platform_exposure_get as _mt4_exposure_get,
    get_api_v_2_mt4_trade_platform_exposure_value_get_currency as _mt4_exposure_value,
    post_api_v_2_mt4_trade_platform_trade_calc_profit as _mt4_trade_calc_profit,
)
from ._generated.models.mt4_trade_calc_profit_request import (
    MT4TradeCalcProfitRequest as _MT4TradeCalcProfitBody,
)
from ._generated.api.mt5_v_2_common import (
    get_api_v_2_mt5_trade_platform_time_server as _mt5_server_time,
    get_api_v_2_mt5_trade_platform_time_get as _mt5_time_get,
)
from ._generated.api.mt5_v_2_managers import (
    get_api_v_2_mt5_trade_platform_manager_current as _mt5_manager_current,
)
from ._generated.api.mt5_v_2_users import (
    get_api_v_2_mt5_trade_platform_user_get_login as _mt5_user_get,
    get_api_v_2_mt5_trade_platform_user_cert_get_login as _mt5_user_cert_get,
    get_api_v_2_mt5_trade_platform_user_account_get_login as _mt5_user_account_get,
    get_api_v_2_mt5_trade_platform_user_get_by_logins as _mt5_user_get_by_logins,
    get_api_v_2_mt5_trade_platform_user_group_login as _mt5_user_group,
    get_api_v_2_mt5_trade_platform_user_logins_group as _mt5_user_logins,
    post_api_v_2_mt5_trade_platform_user_cert_confirm_login as _mt5_user_cert_confirm,
)
from ._generated.api.mt5_v_2_groups import (
    get_api_v_2_mt5_trade_platform_group_get_group as _mt5_group_get,
)
from ._generated.api.mt5_v_2_symbols import (
    get_api_v_2_mt5_trade_platform_symbol_get_symbol as _mt5_symbol_get,
)
from ._generated.api.mt5_v_2_trades import (
    get_api_v_2_mt5_trade_platform_position_request_by_group_mask as _mt5_positions_by_group,
    get_api_v_2_mt5_trade_platform_order_get_ticket as _mt5_order_get,
    get_api_v_2_mt5_trade_platform_deal_request_login as _mt5_deal_request,
    get_api_v_2_mt5_trade_platform_history_request_login as _mt5_history_request,
)
from ._generated.api.mt5_v_2_trading import (
    post_api_v_2_mt5_trade_platform_order_add as _mt5_order_add,
    post_api_v_2_mt5_trade_platform_order_cancel_ticket as _mt5_order_cancel,
)
from ._generated.api.mt5_v_2_trade_operations import (
    get_api_v_2_mt5_trade_platform_request_get_all as _mt5_request_get_all,
    get_api_v_2_mt5_trade_platform_request_get_id as _mt5_request_get,
    post_api_v_2_mt5_trade_platform_trade_profit as _mt5_trade_profit,
)
from ._generated.api.mt5_v_2_reports import (
    get_api_v_2_mt5_trade_platform_summary_get_all as _mt5_summary_get_all,
    get_api_v_2_mt5_trade_platform_summary_get_symbol as _mt5_summary_get,
    get_api_v_2_mt5_trade_platform_summary_currency as _mt5_summary_currency,
    get_api_v_2_mt5_trade_platform_exposure_get_all as _mt5_exposure_get_all,
    get_api_v_2_mt5_trade_platform_exposure_get_symbol as _mt5_exposure_get,
    get_api_v_2_mt5_trade_platform_daily_request_login as _mt5_daily_request,
    get_api_v_2_mt5_trade_platform_daily_request_light_login as _mt5_daily_request_light,
)
from ._generated.api.mt5_v_2_subscriptions import (
    get_api_v_2_mt5_trade_platform_subscription_cfg_request_name as _mt5_subscription_cfg_request,
    get_api_v_2_mt5_trade_platform_subscription_cfg_get_name as _mt5_subscription_cfg_get,
    get_api_v_2_mt5_trade_platform_subscription_request_login as _mt5_subscription_request,
    get_api_v_2_mt5_trade_platform_subscription_history_request_login as _mt5_subscription_history_request,
)
from ._generated.api.mt5_v_2_market_data import (
    get_api_v_2_mt5_trade_platform_tick_last_symbol as _mt5_tick_last,
    get_api_v_2_mt5_trade_platform_tick_stat_symbol as _mt5_tick_stat,
)
from ._generated.api.mt5_v_2_market_insight import (
    get_api_v_2_mt5_trade_platform_book_get_symbol as _mt5_book_get,
    get_api_v_2_mt5_trade_platform_online_request as _mt5_online_request,
)
from ._generated.api.mt5_v_2_configuration import (
    get_api_v_2_mt5_trade_platform_symbol_request_symbol as _mt5_symbol_request,
    get_api_v_2_mt5_trade_platform_symbol_exist_symbol as _mt5_symbol_exist,
    get_api_v_2_mt5_trade_platform_leverage_get_name as _mt5_leverage_get,
)
from ._generated.api.mt5_v_2_communications import (
    get_api_v_2_mt5_trade_platform_mail_request as _mt5_mail_request,
    get_api_v_2_mt5_trade_platform_news_request as _mt5_news_request,
    get_api_v_2_mt5_trade_platform_setting_get as _mt5_setting_get,
    post_api_v_2_mt5_trade_platform_mail_send as _mt5_mail_send,
)
from ._generated.api.mt5_v_2_clients import (
    get_api_v_2_mt5_trade_platform_client_user_request_client_id as _mt5_client_user_request,
    get_api_v_2_mt5_trade_platform_document_request_document_id as _mt5_document_request,
    post_api_v_2_mt5_trade_platform_client_update as _mt5_client_update,
)
from ._generated.models.mt5_order import MT5Order as _MT5OrderBody
from ._generated.models.mt5_mail_send_request import MT5MailSendRequest as _MT5MailSendBody
from ._generated.models.mt5_client import MT5Client as _MT5ClientBody
from ._generated.models.trade_profit_request import TradeProfitRequest as _MT5TradeProfitBody


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

class _RawResponse:
    """Minimal duck-typed response object for ``unwrap`` / ``unwrap_with_meta``.

    The generated ``_parse_response`` tries to deserialise ``data`` even on
    error envelopes (where ``data`` is ``null``), and crashes on a type error.
    Since ``unwrap`` reads only ``.content`` (raw bytes), ``.status_code`` and
    ``.headers``, we bypass ``_build_response`` entirely: call ``_get_kwargs`` +
    httpx.Client directly, and wrap the raw ``httpx.Response`` in this shim.
    """

    def __init__(self, raw: httpx.Response) -> None:
        self.content = raw.content
        self.status_code = raw.status_code
        # * Carried so ApiError can report X-Request-Outcome / X-Request-Timeout-Applied.
        self.headers = raw.headers


def _request_kwargs(
    owner: Any,
    op_module: Any,
    request_timeout: float | None,
    idempotency_key: str | None,
    kwargs: dict[str, Any],
) -> dict[str, Any]:
    """Build the httpx request for a generated op, with timeout and idempotency headers.

    ``request_timeout`` (seconds, 1–300) falls back to the client-wide default; when
    one applies, ``X-Request-Timeout`` is sent. The HTTP timeout of the call is
    stretched past the server's deadline — the one requested, else the operation's
    default from the spec — so the client does not give up before the server has
    said whether the operation was applied.
    """
    # Q-3: Guard against op_module that is not a generated endpoint module.
    if not callable(getattr(op_module, "_get_kwargs", None)):
        raise TypeError(
            "op_module must be a generated endpoint module exposing _get_kwargs"
        )
    # * raw() callers may use the generated parameter name; it means the same thing.
    generated = kwargs.pop("x_request_timeout", None)
    if generated is not None and not isinstance(generated, Unset):
        generated = validate_request_timeout(generated, name="x_request_timeout")
        if request_timeout is not None and validate_request_timeout(request_timeout) != generated:
            raise ValueError("request_timeout and x_request_timeout disagree; pass only one")
        request_timeout = generated
    seconds = validate_request_timeout(request_timeout)
    if seconds is None:
        seconds = owner._request_timeout
    key = validate_idempotency_key(idempotency_key)

    # ! _get_kwargs is a PRIVATE symbol of openapi-python-client. If a generator
    # ! upgrade renames it, this raises AttributeError at call time. Re-verify after
    # ! every regeneration: grep -r '_get_kwargs' src/cplugin_webapi_sdk/_generated/api/
    req_kwargs = op_module._get_kwargs(**kwargs)

    headers = {
        k: v for k, v in (req_kwargs.get("headers") or {}).items()
        if k.lower() != REQUEST_TIMEOUT_HEADER.lower()
    }
    if seconds is not None:
        headers[REQUEST_TIMEOUT_HEADER] = format_seconds(seconds)
    server_timeout = seconds if seconds is not None else operation_default_timeout(op_module)
    req_kwargs["timeout"] = transport_timeout(owner._timeout, server_timeout)
    if key is not None:
        headers[IDEMPOTENCY_KEY_HEADER] = key
    req_kwargs["headers"] = headers
    return req_kwargs


def _call_sync(
    owner: Any,
    op_module: Any,
    *,
    request_timeout: float | None = None,
    idempotency_key: str | None = None,
    **kwargs: Any,
) -> _RawResponse:
    """Invoke a generated op by calling its ``_get_kwargs`` + the owner's shared httpx client.

    This bypasses the generated ``_build_response`` / ``_parse_response`` pipeline,
    which crashes on error envelopes for typed response models (e.g. datetime fields).
    ``unwrap`` / ``unwrap_with_meta`` only need ``.content``, ``.status_code`` and ``.headers``.

    ! Never retried here: a repeated trade or change can be applied twice. The
    !   transport's ``retries`` only re-attempt opening the connection, before any
    !   byte of the request is sent; the auth flow re-sends only after a 401, which
    !   the server answers before running the action.
    """
    req_kwargs = _request_kwargs(owner, op_module, request_timeout, idempotency_key, kwargs)
    raw = owner._http.request(**req_kwargs)
    return _RawResponse(raw)


async def _call_async(
    owner: Any,
    op_module: Any,
    *,
    request_timeout: float | None = None,
    idempotency_key: str | None = None,
    **kwargs: Any,
) -> _RawResponse:
    """Async variant of ``_call_sync``."""
    req_kwargs = _request_kwargs(owner, op_module, request_timeout, idempotency_key, kwargs)
    raw = await owner._http.request(**req_kwargs)
    return _RawResponse(raw)


def _build_auth(
    client_id: str | None,
    client_secret: str | None,
    token: str | None,
    authority: str,
    scopes: list[str] | None,
) -> httpx.Auth:
    """Construct the appropriate auth handler from the provided credentials."""
    if token:
        return BearerAuth(token)
    if not (client_id and client_secret):
        raise ValueError(
            "provide either token= for static-JWT auth, "
            "or client_id= + client_secret= for OAuth2 client_credentials"
        )
    return ClientCredentialsAuth(
        client_id=client_id,
        client_secret=client_secret,
        identity_url=authority,
        scopes=scopes,
    )


def _patch_body(changes: Mapping[str, Any]) -> _MT4UserRecordPatchBody:
    """Wrap a mapping of changed fields into the generated merge-patch body."""
    if not isinstance(changes, Mapping):
        raise TypeError(f"changes must be a mapping of field names to values, got {type(changes).__name__}")
    # ! An empty patch would still be a write round-trip to the trade server for nothing.
    if not changes:
        raise ValueError("changes must contain at least one field")
    return _MT4UserRecordPatchBody.from_dict(dict(changes))


def _body(model: Any, payload: Mapping[str, Any] | Any) -> Any:
    """Wrap a mapping into a generated request model; an already-built model passes through."""
    if isinstance(payload, Mapping):
        return model.from_dict(dict(payload))
    return payload


def _to_uuid(trade_platform: str | UUID) -> UUID:
    """Accept a trade-platform identifier as str or UUID, always return UUID."""
    if isinstance(trade_platform, UUID):
        return trade_platform
    return UUID(trade_platform)


# ---------------------------------------------------------------------------
# Sync namespace objects
# ---------------------------------------------------------------------------

class _MT4Namespace:
    """Clean snake_case facade over the generated MT4 v2 endpoint modules.

    All methods accept ``trade_platform`` as a ``str`` (UUID string) or
    ``uuid.UUID`` — both are normalised internally, and a keyword-only
    ``request_timeout`` (seconds, 1–300) that overrides the server deadline for
    that call (default: the client's ``request_timeout``, else the server's
    default for the operation). Write methods also take ``idempotency_key``.

    Implementation note: we call ``_get_kwargs`` + the shared ``httpx.Client``
    directly (via ``_call_sync``), bypassing the generated ``_build_response`` /
    ``_parse_response`` pipeline. The generated ``_parse_response`` always tries
    to deserialise the ``data`` field even on error envelopes (where ``data`` is
    ``null``), which causes a crash on typed fields like ``datetime``. Since
    ``unwrap`` reads only ``.content`` (raw bytes) and ``.status_code``, the
    generated parsing layer is not needed here.
    """

    def __init__(self, owner: "CPluginWebApiClient") -> None:
        self._o = owner

    # * ----- common -----

    def get_server_time(self, trade_platform: str | UUID, *, request_timeout: float | None = None) -> Any:
        """Return current MT4 server time (ISO 8601 string)."""
        return unwrap(
            _call_sync(
                self._o, _mt4_server_time,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def get_manager_common(self, trade_platform: str | UUID, *, request_timeout: float | None = None) -> Any:
        """Return server-wide MT4 common settings (name, broker, version, tz)."""
        return unwrap(
            _call_sync(
                self._o, _mt4_manager_common,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    # * ----- users -----

    def users_request(
        self,
        trade_platform: str | UUID,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_timeout: float | None = None,
    ) -> tuple[Any, Any]:
        """Return ``(data, meta)`` for a paged list of MT4 user accounts.

        Pass ``cursor`` from ``meta.paging.next_cursor`` to advance pages.
        ``meta.paging.has_more`` signals that further pages exist.
        """
        from ._generated.types import UNSET

        return unwrap_with_meta(
            _call_sync(
                self._o, _mt4_users_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                limit=limit if limit is not None else UNSET,
                cursor=cursor if cursor is not None else UNSET,
            )
        )

    def get_user_record(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a single MT4 user account record from the pump cache."""
        return unwrap(
            _call_sync(
                self._o, _mt4_user_record_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    def patch_user_record(
        self,
        trade_platform: str | UUID,
        login: int,
        changes: Mapping[str, Any],
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Change the given fields of a user record (JSON Merge Patch) and return the merged record.

        ``changes`` holds only the fields to change, with their wire (camelCase)
        names, e.g. ``{"leverage": 200, "comment": "vip"}``. The server reads the
        current record from the trade server, overlays the changes and writes it
        back; unknown keys are ignored. A change that timed out answers
        ``OutcomeUnknown`` — pass ``idempotency_key`` to repeat it safely.
        """
        return unwrap(
            _call_sync(
                self._o, _mt4_user_record_patch,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                login=login,
                body=_patch_body(changes),
            )
        )

    # * ----- groups -----

    def group_exists(
        self,
        trade_platform: str | UUID,
        group: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return ``True`` if ``group`` is configured on the MT4 server."""
        return unwrap(
            _call_sync(
                self._o, _mt4_group_exists,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                group=group,
            )
        )

    # * ----- symbols -----

    def list_symbol_configs(self, trade_platform: str | UUID, *, request_timeout: float | None = None) -> Any:
        """Return all symbol configuration records from the MT4 server."""
        return unwrap(
            _call_sync(
                self._o, _mt4_symbols_list,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def get_symbol_info(
        self,
        trade_platform: str | UUID,
        *,
        symbol: str | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return live symbol info snapshot (spread, digits, sessions).

        Pass ``symbol`` to filter to a single instrument. Without it, all
        loaded symbols are returned.
        """
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt4_symbol_info,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol if symbol is not None else UNSET,
            )
        )

    # * ----- trades -----

    def trades_request(
        self,
        trade_platform: str | UUID,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        group: str | None = None,
        request_timeout: float | None = None,
    ) -> tuple[Any, Any]:
        """Return ``(data, meta)`` for a paged list of open trades.

        Optional ``group`` filter restricts results to accounts in that group.
        Pass ``cursor`` from the previous page's ``meta.paging.next_cursor``.
        """
        from ._generated.types import UNSET

        return unwrap_with_meta(
            _call_sync(
                self._o, _mt4_trades_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                limit=limit if limit is not None else UNSET,
                cursor=cursor if cursor is not None else UNSET,
                group=group if group is not None else UNSET,
            )
        )

    # * ----- dealer (summary and exposure) -----

    def summary_get_all(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's open-interest summary for every symbol."""
        return unwrap(
            _call_sync(
                self._o, _mt4_summary_get_all,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def summary_get(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's open-interest summary for one symbol."""
        return unwrap(
            _call_sync(
                self._o, _mt4_summary_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    def summary_currency(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's summary expressed in the server base currency."""
        return unwrap(
            _call_sync(
                self._o, _mt4_summary_currency,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def exposure_get(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the broker's currency exposure over all open client positions."""
        return unwrap(
            _call_sync(
                self._o, _mt4_exposure_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def exposure_value(
        self,
        trade_platform: str | UUID,
        currency: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the exposure of one currency."""
        return unwrap(
            _call_sync(
                self._o, _mt4_exposure_value,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                currency=currency,
            )
        )

    def trade_calc_profit(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Calculate profit for a hypothetical trade without executing it.

        ``body`` holds the trade description with its wire (camelCase) names, or a
        ready request model.
        """
        return unwrap(
            _call_sync(
                self._o, _mt4_trade_calc_profit,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                body=_body(_MT4TradeCalcProfitBody, body),
            )
        )

    # * ----- escape hatch -----

    def raw(
        self,
        op_module: Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
        **kwargs: Any,
    ) -> Any:
        """Call any generated MT4 op module via ``_get_kwargs`` + the shared httpx client.

        Injects the shared authenticated httpx client automatically.
        Returns a ``_RawResponse`` — call ``unwrap()`` / ``unwrap_with_meta()`` on it.

        ``request_timeout`` (seconds, 1–300) sets the server deadline for this call;
        ``idempotency_key`` sends ``Idempotency-Key`` so a repeat after
        ``OutcomeUnknown`` returns the original result instead of executing again.

        Example::

            from cplugin_webapi_sdk._generated.api.mt4_v_2_history import (
                get_api_v_2_mt4_trade_platform_trades_user_history_login as history_op,
            )
            from cplugin_webapi_sdk import unwrap
            resp = client.mt4.raw(history_op, trade_platform=tp_id, login=1001, from_time=..., to_time=...)
            data = unwrap(resp)
        """
        return _call_sync(
            self._o, op_module,
            request_timeout=request_timeout, idempotency_key=idempotency_key, **kwargs,
        )


class _MT5Namespace:
    """Clean snake_case facade over the generated MT5 v2 endpoint modules.

    See ``_MT4Namespace`` for the implementation note on bypassing
    ``_build_response`` / ``_parse_response``.
    """

    def __init__(self, owner: "CPluginWebApiClient") -> None:
        self._o = owner

    # * ----- common -----

    def get_server_time(self, trade_platform: str | UUID, *, request_timeout: float | None = None) -> Any:
        """Return current MT5 server time (ISO 8601 string)."""
        return unwrap(
            _call_sync(
                self._o, _mt5_server_time,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def get_manager_current(self, trade_platform: str | UUID, *, request_timeout: float | None = None) -> Any:
        """Return the currently-connected MT5 manager record."""
        return unwrap(
            _call_sync(
                self._o, _mt5_manager_current,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    # * ----- users -----

    def get_user(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a single MT5 user record by login."""
        return unwrap(
            _call_sync(
                self._o, _mt5_user_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    # * ----- groups -----

    def get_group(
        self,
        trade_platform: str | UUID,
        group: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return MT5 group configuration by exact name."""
        return unwrap(
            _call_sync(
                self._o, _mt5_group_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                group=group,
            )
        )

    # * ----- symbols -----

    def get_symbol(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return MT5 symbol settings by exact symbol name."""
        return unwrap(
            _call_sync(
                self._o, _mt5_symbol_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    # * ----- trades -----

    def positions_by_group(
        self,
        trade_platform: str | UUID,
        mask: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return open positions for all logins in groups matching ``mask``."""
        return unwrap(
            _call_sync(
                self._o, _mt5_positions_by_group,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                mask=mask,
            )
        )

    # * ----- common (extended) -----

    def time_get(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the trade server's current time record."""
        return unwrap(
            _call_sync(
                self._o, _mt5_time_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    # * ----- reports (summary, exposure, daily) -----

    def summary_get_all(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's open-interest summary for every symbol."""
        return unwrap(
            _call_sync(
                self._o, _mt5_summary_get_all,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def summary_get(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's open-interest summary for one symbol."""
        return unwrap(
            _call_sync(
                self._o, _mt5_summary_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    def summary_currency(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's summary expressed in the server base currency."""
        return unwrap(
            _call_sync(
                self._o, _mt5_summary_currency,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def exposure_get_all(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the broker's currency exposure over all open client positions."""
        return unwrap(
            _call_sync(
                self._o, _mt5_exposure_get_all,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    def exposure_get(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the broker's exposure for one symbol."""
        return unwrap(
            _call_sync(
                self._o, _mt5_exposure_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    def daily_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the full daily report of one account."""
        return unwrap(
            _call_sync(
                self._o, _mt5_daily_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    def daily_request_light(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the compact daily report of one account."""
        return unwrap(
            _call_sync(
                self._o, _mt5_daily_request_light,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    # * ----- subscriptions -----

    def subscription_cfg_request(
        self,
        trade_platform: str | UUID,
        name: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a subscription configuration by name, read from the trade server."""
        return unwrap(
            _call_sync(
                self._o, _mt5_subscription_cfg_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                name=name,
            )
        )

    def subscription_cfg_get(
        self,
        trade_platform: str | UUID,
        name: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a cached subscription configuration by name."""
        return unwrap(
            _call_sync(
                self._o, _mt5_subscription_cfg_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                name=name,
            )
        )

    def subscription_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the active subscriptions of one account."""
        return unwrap(
            _call_sync(
                self._o, _mt5_subscription_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    def subscription_history_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the subscription history of one account."""
        return unwrap(
            _call_sync(
                self._o, _mt5_subscription_history_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    # * ----- users (extended) -----

    def user_cert_get(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the certificate record of one account."""
        return unwrap(
            _call_sync(
                self._o, _mt5_user_cert_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    def user_account_get(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the trading account of one user (balances, credit, leverage)."""
        return unwrap(
            _call_sync(
                self._o, _mt5_user_account_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    def user_get_by_logins(
        self,
        trade_platform: str | UUID,
        logins: list[int],
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return user records for several logins in one call."""
        return unwrap(
            _call_sync(
                self._o, _mt5_user_get_by_logins,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                logins=logins,
            )
        )

    def user_group(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the group name of one account."""
        return unwrap(
            _call_sync(
                self._o, _mt5_user_group,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    def user_logins(
        self,
        trade_platform: str | UUID,
        group: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the logins that belong to one group."""
        return unwrap(
            _call_sync(
                self._o, _mt5_user_logins,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                group=group,
            )
        )

    def user_cert_confirm(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Confirm the pending certificate of one account."""
        return unwrap(
            _call_sync(
                self._o, _mt5_user_cert_confirm,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                login=login,
            )
        )

    # * ----- trade operations -----

    def request_get_all(
        self,
        trade_platform: str | UUID,
        *,
        from_: int | None = None,
        count: int | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the trade requests waiting for a dealer answer."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_request_get_all,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                from_=from_ if from_ is not None else UNSET,
                count=count if count is not None else UNSET,
            )
        )

    def request_get(
        self,
        trade_platform: str | UUID,
        id: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return one trade request by its identifier."""
        return unwrap(
            _call_sync(
                self._o, _mt5_request_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                id=id,
            )
        )

    def trade_profit(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Calculate profit for a hypothetical trade without executing it."""
        return unwrap(
            _call_sync(
                self._o, _mt5_trade_profit,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                body=_body(_MT5TradeProfitBody, body),
            )
        )

    # * ----- trading -----

    def order_get(
        self,
        trade_platform: str | UUID,
        ticket: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return one order by ticket."""
        return unwrap(
            _call_sync(
                self._o, _mt5_order_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                ticket=ticket,
            )
        )

    def order_add(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Place a new order on the trade server."""
        return unwrap(
            _call_sync(
                self._o, _mt5_order_add,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                body=_body(_MT5OrderBody, body),
            )
        )

    def order_cancel(
        self,
        trade_platform: str | UUID,
        ticket: int,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Cancel a pending order by ticket."""
        return unwrap(
            _call_sync(
                self._o, _mt5_order_cancel,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                ticket=ticket,
            )
        )

    def deal_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        from_: Any = None,
        to: Any = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the deals of one account, optionally limited to a time window."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_deal_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
                from_=from_ if from_ is not None else UNSET,
                to=to if to is not None else UNSET,
            )
        )

    def history_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        from_: Any = None,
        to: Any = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the closed-order history of one account."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_history_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
                from_=from_ if from_ is not None else UNSET,
                to=to if to is not None else UNSET,
            )
        )

    # * ----- market data and insight -----

    def tick_last(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the last tick of a symbol."""
        return unwrap(
            _call_sync(
                self._o, _mt5_tick_last,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    def tick_stat(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return tick statistics of a symbol."""
        return unwrap(
            _call_sync(
                self._o, _mt5_tick_stat,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    def book_get(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the current depth-of-market book of a symbol."""
        return unwrap(
            _call_sync(
                self._o, _mt5_book_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    def online_request(
        self,
        trade_platform: str | UUID,
        *,
        from_: int | None = None,
        count: int | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the accounts currently connected to the trade server."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_online_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                from_=from_ if from_ is not None else UNSET,
                count=count if count is not None else UNSET,
            )
        )

    # * ----- configuration -----

    def symbol_request(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        group: str | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a symbol configuration, read from the trade server."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_symbol_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
                group=group if group is not None else UNSET,
            )
        )

    def symbol_exist(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        group: str | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return whether a symbol exists, optionally inside one group."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_symbol_exist,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
                group=group if group is not None else UNSET,
            )
        )

    def leverage_get(
        self,
        trade_platform: str | UUID,
        name: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a leverage configuration by name."""
        return unwrap(
            _call_sync(
                self._o, _mt5_leverage_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                name=name,
            )
        )

    # * ----- communications -----

    def mail_request(
        self,
        trade_platform: str | UUID,
        *,
        from_: int | None = None,
        count: int | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the internal mail queue of the trade server."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_mail_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                from_=from_ if from_ is not None else UNSET,
                count=count if count is not None else UNSET,
            )
        )

    def news_request(
        self,
        trade_platform: str | UUID,
        *,
        from_: int | None = None,
        count: int | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the news topics of the trade server."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_news_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                from_=from_ if from_ is not None else UNSET,
                count=count if count is not None else UNSET,
            )
        )

    def setting_get(
        self,
        trade_platform: str | UUID,
        *,
        section: str | None = None,
        key: str | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return server settings, optionally narrowed to one section and key."""
        from ._generated.types import UNSET

        return unwrap(
            _call_sync(
                self._o, _mt5_setting_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                section=section if section is not None else UNSET,
                key=key if key is not None else UNSET,
            )
        )

    def mail_send(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Send an internal mail message to accounts."""
        return unwrap(
            _call_sync(
                self._o, _mt5_mail_send,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                body=_body(_MT5MailSendBody, body),
            )
        )

    # * ----- clients -----

    def client_user_request(
        self,
        trade_platform: str | UUID,
        client_id: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the users attached to one client record."""
        return unwrap(
            _call_sync(
                self._o, _mt5_client_user_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                client_id=client_id,
            )
        )

    def document_request(
        self,
        trade_platform: str | UUID,
        document_id: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return one KYC document record by its identifier."""
        return unwrap(
            _call_sync(
                self._o, _mt5_document_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                document_id=document_id,
            )
        )

    def client_update(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Create or update a client record."""
        return unwrap(
            _call_sync(
                self._o, _mt5_client_update,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                body=_body(_MT5ClientBody, body),
            )
        )

    # * ----- escape hatch -----

    def raw(
        self,
        op_module: Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
        **kwargs: Any,
    ) -> Any:
        """Call any generated MT5 op module via ``_get_kwargs`` + the shared httpx client.

        Injects the shared authenticated httpx client automatically.
        Returns a ``_RawResponse`` — call ``unwrap()`` / ``unwrap_with_meta()`` on it.
        ``request_timeout`` / ``idempotency_key`` as in ``_MT4Namespace.raw``.
        """
        return _call_sync(
            self._o, op_module,
            request_timeout=request_timeout, idempotency_key=idempotency_key, **kwargs,
        )


# ---------------------------------------------------------------------------
# Async namespace objects
# ---------------------------------------------------------------------------

class _MT4AsyncNamespace:
    """Async facade over the generated MT4 v2 endpoint modules."""

    def __init__(self, owner: "CPluginWebApiAsyncClient") -> None:
        self._o = owner

    async def get_server_time(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return current MT4 server time (ISO 8601 string)."""
        return unwrap(
            await _call_async(
                self._o, _mt4_server_time,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def get_manager_common(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return server-wide MT4 common settings."""
        return unwrap(
            await _call_async(
                self._o, _mt4_manager_common,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def users_request(
        self,
        trade_platform: str | UUID,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_timeout: float | None = None,
    ) -> tuple[Any, Any]:
        """Return ``(data, meta)`` for a paged list of MT4 user accounts."""
        from ._generated.types import UNSET

        return unwrap_with_meta(
            await _call_async(
                self._o, _mt4_users_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                limit=limit if limit is not None else UNSET,
                cursor=cursor if cursor is not None else UNSET,
            )
        )

    async def get_user_record(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a single MT4 user account record from the pump cache."""
        return unwrap(
            await _call_async(
                self._o, _mt4_user_record_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    async def patch_user_record(
        self,
        trade_platform: str | UUID,
        login: int,
        changes: Mapping[str, Any],
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Change the given fields of a user record; see the sync ``patch_user_record``."""
        return unwrap(
            await _call_async(
                self._o, _mt4_user_record_patch,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                login=login,
                body=_patch_body(changes),
            )
        )

    async def group_exists(
        self,
        trade_platform: str | UUID,
        group: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return ``True`` if ``group`` is configured on the MT4 server."""
        return unwrap(
            await _call_async(
                self._o, _mt4_group_exists,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                group=group,
            )
        )

    async def list_symbol_configs(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return all symbol configuration records from the MT4 server."""
        return unwrap(
            await _call_async(
                self._o, _mt4_symbols_list,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def get_symbol_info(
        self,
        trade_platform: str | UUID,
        *,
        symbol: str | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return live symbol info snapshot (spread, digits, sessions).

        Pass ``symbol`` to filter to a single instrument. Without it, all
        loaded symbols are returned.
        """
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt4_symbol_info,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol if symbol is not None else UNSET,
            )
        )

    async def trades_request(
        self,
        trade_platform: str | UUID,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        group: str | None = None,
        request_timeout: float | None = None,
    ) -> tuple[Any, Any]:
        """Return ``(data, meta)`` for a paged list of open trades."""
        from ._generated.types import UNSET

        return unwrap_with_meta(
            await _call_async(
                self._o, _mt4_trades_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                limit=limit if limit is not None else UNSET,
                cursor=cursor if cursor is not None else UNSET,
                group=group if group is not None else UNSET,
            )
        )

    # * ----- dealer (summary and exposure) -----

    async def summary_get_all(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's open-interest summary for every symbol."""
        return unwrap(
            await _call_async(
                self._o, _mt4_summary_get_all,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def summary_get(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's open-interest summary for one symbol."""
        return unwrap(
            await _call_async(
                self._o, _mt4_summary_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    async def summary_currency(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's summary expressed in the server base currency."""
        return unwrap(
            await _call_async(
                self._o, _mt4_summary_currency,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def exposure_get(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the broker's currency exposure over all open client positions."""
        return unwrap(
            await _call_async(
                self._o, _mt4_exposure_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def exposure_value(
        self,
        trade_platform: str | UUID,
        currency: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the exposure of one currency."""
        return unwrap(
            await _call_async(
                self._o, _mt4_exposure_value,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                currency=currency,
            )
        )

    async def trade_calc_profit(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Calculate profit for a hypothetical trade; see the sync method."""
        return unwrap(
            await _call_async(
                self._o, _mt4_trade_calc_profit,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                body=_body(_MT4TradeCalcProfitBody, body),
            )
        )

    async def raw(
        self,
        op_module: Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
        **kwargs: Any,
    ) -> Any:
        """Call any generated MT4 op module via ``_get_kwargs`` + the shared async httpx client.

        Returns a ``_RawResponse`` — call ``unwrap()`` / ``unwrap_with_meta()`` on it.
        ``request_timeout`` / ``idempotency_key`` as in ``_MT4Namespace.raw``.
        """
        return await _call_async(
            self._o, op_module,
            request_timeout=request_timeout, idempotency_key=idempotency_key, **kwargs,
        )


class _MT5AsyncNamespace:
    """Async facade over the generated MT5 v2 endpoint modules."""

    def __init__(self, owner: "CPluginWebApiAsyncClient") -> None:
        self._o = owner

    async def get_server_time(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return current MT5 server time (ISO 8601 string)."""
        return unwrap(
            await _call_async(
                self._o, _mt5_server_time,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def get_manager_current(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the currently-connected MT5 manager record."""
        return unwrap(
            await _call_async(
                self._o, _mt5_manager_current,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def get_user(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a single MT5 user record by login."""
        return unwrap(
            await _call_async(
                self._o, _mt5_user_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    async def get_group(
        self,
        trade_platform: str | UUID,
        group: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return MT5 group configuration by exact name."""
        return unwrap(
            await _call_async(
                self._o, _mt5_group_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                group=group,
            )
        )

    async def get_symbol(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return MT5 symbol settings by exact symbol name."""
        return unwrap(
            await _call_async(
                self._o, _mt5_symbol_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    async def positions_by_group(
        self,
        trade_platform: str | UUID,
        mask: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return open positions for all logins in groups matching ``mask``."""
        return unwrap(
            await _call_async(
                self._o, _mt5_positions_by_group,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                mask=mask,
            )
        )

    # * ----- common (extended) -----

    async def time_get(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the trade server's current time record."""
        return unwrap(
            await _call_async(
                self._o, _mt5_time_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    # * ----- reports (summary, exposure, daily) -----

    async def summary_get_all(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's open-interest summary for every symbol."""
        return unwrap(
            await _call_async(
                self._o, _mt5_summary_get_all,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def summary_get(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's open-interest summary for one symbol."""
        return unwrap(
            await _call_async(
                self._o, _mt5_summary_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    async def summary_currency(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the dealer's summary expressed in the server base currency."""
        return unwrap(
            await _call_async(
                self._o, _mt5_summary_currency,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def exposure_get_all(
        self,
        trade_platform: str | UUID,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the broker's currency exposure over all open client positions."""
        return unwrap(
            await _call_async(
                self._o, _mt5_exposure_get_all,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
            )
        )

    async def exposure_get(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the broker's exposure for one symbol."""
        return unwrap(
            await _call_async(
                self._o, _mt5_exposure_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    async def daily_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the full daily report of one account."""
        return unwrap(
            await _call_async(
                self._o, _mt5_daily_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    async def daily_request_light(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the compact daily report of one account."""
        return unwrap(
            await _call_async(
                self._o, _mt5_daily_request_light,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    # * ----- subscriptions -----

    async def subscription_cfg_request(
        self,
        trade_platform: str | UUID,
        name: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a subscription configuration by name, read from the trade server."""
        return unwrap(
            await _call_async(
                self._o, _mt5_subscription_cfg_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                name=name,
            )
        )

    async def subscription_cfg_get(
        self,
        trade_platform: str | UUID,
        name: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a cached subscription configuration by name."""
        return unwrap(
            await _call_async(
                self._o, _mt5_subscription_cfg_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                name=name,
            )
        )

    async def subscription_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the active subscriptions of one account."""
        return unwrap(
            await _call_async(
                self._o, _mt5_subscription_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    async def subscription_history_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the subscription history of one account."""
        return unwrap(
            await _call_async(
                self._o, _mt5_subscription_history_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    # * ----- users (extended) -----

    async def user_cert_get(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the certificate record of one account."""
        return unwrap(
            await _call_async(
                self._o, _mt5_user_cert_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    async def user_account_get(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the trading account of one user (balances, credit, leverage)."""
        return unwrap(
            await _call_async(
                self._o, _mt5_user_account_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    async def user_get_by_logins(
        self,
        trade_platform: str | UUID,
        logins: list[int],
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return user records for several logins in one call."""
        return unwrap(
            await _call_async(
                self._o, _mt5_user_get_by_logins,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                logins=logins,
            )
        )

    async def user_group(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the group name of one account."""
        return unwrap(
            await _call_async(
                self._o, _mt5_user_group,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
            )
        )

    async def user_logins(
        self,
        trade_platform: str | UUID,
        group: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the logins that belong to one group."""
        return unwrap(
            await _call_async(
                self._o, _mt5_user_logins,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                group=group,
            )
        )

    async def user_cert_confirm(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Confirm the pending certificate of one account."""
        return unwrap(
            await _call_async(
                self._o, _mt5_user_cert_confirm,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                login=login,
            )
        )

    # * ----- trade operations -----

    async def request_get_all(
        self,
        trade_platform: str | UUID,
        *,
        from_: int | None = None,
        count: int | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the trade requests waiting for a dealer answer."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_request_get_all,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                from_=from_ if from_ is not None else UNSET,
                count=count if count is not None else UNSET,
            )
        )

    async def request_get(
        self,
        trade_platform: str | UUID,
        id: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return one trade request by its identifier."""
        return unwrap(
            await _call_async(
                self._o, _mt5_request_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                id=id,
            )
        )

    async def trade_profit(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Calculate profit for a hypothetical trade without executing it."""
        return unwrap(
            await _call_async(
                self._o, _mt5_trade_profit,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                body=_body(_MT5TradeProfitBody, body),
            )
        )

    # * ----- trading -----

    async def order_get(
        self,
        trade_platform: str | UUID,
        ticket: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return one order by ticket."""
        return unwrap(
            await _call_async(
                self._o, _mt5_order_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                ticket=ticket,
            )
        )

    async def order_add(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Place a new order on the trade server."""
        return unwrap(
            await _call_async(
                self._o, _mt5_order_add,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                body=_body(_MT5OrderBody, body),
            )
        )

    async def order_cancel(
        self,
        trade_platform: str | UUID,
        ticket: int,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Cancel a pending order by ticket."""
        return unwrap(
            await _call_async(
                self._o, _mt5_order_cancel,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                ticket=ticket,
            )
        )

    async def deal_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        from_: Any = None,
        to: Any = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the deals of one account, optionally limited to a time window."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_deal_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
                from_=from_ if from_ is not None else UNSET,
                to=to if to is not None else UNSET,
            )
        )

    async def history_request(
        self,
        trade_platform: str | UUID,
        login: int,
        *,
        from_: Any = None,
        to: Any = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the closed-order history of one account."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_history_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                login=login,
                from_=from_ if from_ is not None else UNSET,
                to=to if to is not None else UNSET,
            )
        )

    # * ----- market data and insight -----

    async def tick_last(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the last tick of a symbol."""
        return unwrap(
            await _call_async(
                self._o, _mt5_tick_last,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    async def tick_stat(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return tick statistics of a symbol."""
        return unwrap(
            await _call_async(
                self._o, _mt5_tick_stat,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    async def book_get(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the current depth-of-market book of a symbol."""
        return unwrap(
            await _call_async(
                self._o, _mt5_book_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
            )
        )

    async def online_request(
        self,
        trade_platform: str | UUID,
        *,
        from_: int | None = None,
        count: int | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the accounts currently connected to the trade server."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_online_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                from_=from_ if from_ is not None else UNSET,
                count=count if count is not None else UNSET,
            )
        )

    # * ----- configuration -----

    async def symbol_request(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        group: str | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a symbol configuration, read from the trade server."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_symbol_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
                group=group if group is not None else UNSET,
            )
        )

    async def symbol_exist(
        self,
        trade_platform: str | UUID,
        symbol: str,
        *,
        group: str | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return whether a symbol exists, optionally inside one group."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_symbol_exist,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                symbol=symbol,
                group=group if group is not None else UNSET,
            )
        )

    async def leverage_get(
        self,
        trade_platform: str | UUID,
        name: str,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return a leverage configuration by name."""
        return unwrap(
            await _call_async(
                self._o, _mt5_leverage_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                name=name,
            )
        )

    # * ----- communications -----

    async def mail_request(
        self,
        trade_platform: str | UUID,
        *,
        from_: int | None = None,
        count: int | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the internal mail queue of the trade server."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_mail_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                from_=from_ if from_ is not None else UNSET,
                count=count if count is not None else UNSET,
            )
        )

    async def news_request(
        self,
        trade_platform: str | UUID,
        *,
        from_: int | None = None,
        count: int | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the news topics of the trade server."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_news_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                from_=from_ if from_ is not None else UNSET,
                count=count if count is not None else UNSET,
            )
        )

    async def setting_get(
        self,
        trade_platform: str | UUID,
        *,
        section: str | None = None,
        key: str | None = None,
        request_timeout: float | None = None,
    ) -> Any:
        """Return server settings, optionally narrowed to one section and key."""
        from ._generated.types import UNSET

        return unwrap(
            await _call_async(
                self._o, _mt5_setting_get,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                section=section if section is not None else UNSET,
                key=key if key is not None else UNSET,
            )
        )

    async def mail_send(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Send an internal mail message to accounts."""
        return unwrap(
            await _call_async(
                self._o, _mt5_mail_send,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                body=_body(_MT5MailSendBody, body),
            )
        )

    # * ----- clients -----

    async def client_user_request(
        self,
        trade_platform: str | UUID,
        client_id: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return the users attached to one client record."""
        return unwrap(
            await _call_async(
                self._o, _mt5_client_user_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                client_id=client_id,
            )
        )

    async def document_request(
        self,
        trade_platform: str | UUID,
        document_id: int,
        *,
        request_timeout: float | None = None,
    ) -> Any:
        """Return one KYC document record by its identifier."""
        return unwrap(
            await _call_async(
                self._o, _mt5_document_request,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                document_id=document_id,
            )
        )

    async def client_update(
        self,
        trade_platform: str | UUID,
        body: Mapping[str, Any] | Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Create or update a client record."""
        return unwrap(
            await _call_async(
                self._o, _mt5_client_update,
                trade_platform=_to_uuid(trade_platform),
                request_timeout=request_timeout,
                idempotency_key=idempotency_key,
                body=_body(_MT5ClientBody, body),
            )
        )

    async def raw(
        self,
        op_module: Any,
        *,
        request_timeout: float | None = None,
        idempotency_key: str | None = None,
        **kwargs: Any,
    ) -> Any:
        """Call any generated MT5 op module via ``_get_kwargs`` + the shared async httpx client.

        Returns a ``_RawResponse`` — call ``unwrap()`` / ``unwrap_with_meta()`` on it.
        ``request_timeout`` / ``idempotency_key`` as in ``_MT4Namespace.raw``.
        """
        return await _call_async(
            self._o, op_module,
            request_timeout=request_timeout, idempotency_key=idempotency_key, **kwargs,
        )


# ---------------------------------------------------------------------------
# Public sync client
# ---------------------------------------------------------------------------

class CPluginWebApiClient:
    """Synchronous WebAPI v2 client.

    Constructs one shared authenticated ``httpx.Client``. Auth is lazy:
    tokens are fetched on first request, cached until near-expiry, and
    force-refreshed on a 401 response.

    Args:
        env:          Named environment preset — ``"prod"``, ``"staging"``, or
                      ``"custom"``.
        client_id:    OAuth2 client ID (required unless ``token=`` is supplied).
        client_secret: OAuth2 client secret (required unless ``token=`` is supplied).
        token:        Static bearer token. Mutually exclusive with
                      ``client_id`` / ``client_secret``.
        api_base_url: Override API base URL (required when ``env="custom"``).
        authority:    Override OIDC authority URL (required when ``env="custom"``).
        scopes:       OAuth2 scopes to request (default: server-defined).
        timeout:      HTTP client timeout in seconds (default: 30.0). A trade-platform
                      call waits at least its server deadline + 30 s — the requested
                      ``request_timeout``, else the operation's default from the spec
                      (60 s where it documents none) — so it is never cut off before
                      the server answers; this value is the floor.
        request_timeout: Default server deadline in seconds (1–300) for every call,
                      sent as ``X-Request-Timeout``. ``None`` (default): the server's
                      own per-operation default (trade 5 s, read 10 s, change 15 s,
                      history 30 s, maintenance 60 s).
        retries:      Transport-level retry count for opening a connection (default: 2).
                      Only connection attempts are repeated, never a sent request:
                      a repeated trade could be applied twice.
        transport:    Custom ``httpx.BaseTransport`` (e.g. ``respx.MockTransport``
                      for tests). Overrides ``retries``.

    Attributes for Task 9 (realtime SignalR wiring):
        _api_base (str):      Resolved API base URL without trailing slash.
        _token_getter (callable → str): Zero-arg callable returning the current
                              bearer token; calls the auth flow's token-fetch if
                              the cached token has expired.
    """

    def __init__(
        self,
        *,
        env: EnvironmentName = "prod",
        client_id: str | None = None,
        client_secret: str | None = None,
        token: str | None = None,
        api_base_url: str | None = None,
        authority: str | None = None,
        scopes: list[str] | None = None,
        timeout: float | None = DEFAULT_TRANSPORT_TIMEOUT,
        request_timeout: float | None = None,
        retries: int = 2,
        transport: httpx.BaseTransport | None = None,
    ) -> None:
        resolved = resolve_environment(env, api_base_url=api_base_url, authority=authority)

        # * Validated up front: a bad client-wide default fails here, not on the first call.
        self._request_timeout: float | None = validate_request_timeout(request_timeout)
        self._timeout: float | None = timeout

        # * Resolved base URL — stored for Task 9 realtime wiring.
        self._api_base: str = resolved.api_base_url

        auth = _build_auth(client_id, client_secret, token, resolved.authority, scopes)
        self._auth = auth

        self._http = httpx.Client(
            base_url=self._api_base,
            timeout=timeout,
            auth=auth,
            transport=transport or httpx.HTTPTransport(retries=retries),
        )

        # * Zero-arg token getter for Task 9 realtime wiring.
        # * Uses the public current_token() accessor on both auth types.
        self._token_getter: Callable[[], str] = auth.current_token

        self.mt4 = _MT4Namespace(self)
        self.mt5 = _MT5Namespace(self)
        self._realtime: RealtimeNamespace | None = None

    @property
    def realtime(self) -> RealtimeNamespace:
        """Real-time SignalR namespace. Requires the optional ``signalrcore`` extra.

        Returns a :class:`~cplugin_webapi_sdk.realtime.RealtimeNamespace` bound to
        this client's base URL and token provider. Constructing a hub client from
        the namespace will raise :class:`~cplugin_webapi_sdk.realtime.SignalRNotInstalledError`
        if ``signalrcore`` is not installed.

        Example::

            rt = client.realtime.mt4("my-trade-platform-id")
            rt.on_tick(lambda *args: print(args))
            with rt:
                rt.subscribe_to_ticks("EURUSD")
                import time; time.sleep(5)
        """
        # * Lazily create so the client itself is usable without signalrcore.
        if self._realtime is None:
            self._realtime = RealtimeNamespace(
                base_url=self._api_base,
                token_factory=self._token_getter,
            )
        return self._realtime

    def list_trade_platforms(self) -> list[dict]:
        """Return the raw v1 list of configured trade platforms.

        This endpoint pre-dates the v2 envelope — it returns a plain JSON array,
        not the ``{data, error, meta}`` structure. Mirror the TS SDK's behaviour:
        raise directly on HTTP errors via ``raise_for_status()``.
        """
        # ! v1, unversioned path — NOT covered by the v2 spec / generated layer.
        r = self._http.get("/api/TradePlatforms")
        r.raise_for_status()
        return r.json()

    def paged(
        self,
        fetch_page: Callable[[str | None], tuple[Any, Any]],
    ) -> Generator[Any, None, None]:
        """Iterate pages by calling ``fetch_page(cursor)`` until exhausted.

        ``fetch_page`` must be a callable that accepts an opaque cursor string
        (``None`` on the first call) and returns ``(data, meta)`` — the same
        shape that namespace paged methods like ``mt4.users_request`` return.
        Each call yields the ``data`` portion of that page.

        Example::

            for page_data in client.paged(
                lambda cur: client.mt4.users_request("tp-id", cursor=cur)
            ):
                process(page_data)
        """
        cursor: str | None = None
        while True:
            data, meta = fetch_page(cursor)
            yield data
            paging = meta.paging if meta else None
            if not paging or not paging.has_more:
                break
            cursor = paging.next_cursor

    def close(self) -> None:
        """Close the underlying httpx client and free connection pool resources."""
        self._http.close()

    def __enter__(self) -> "CPluginWebApiClient":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()


# ---------------------------------------------------------------------------
# Public async client
# ---------------------------------------------------------------------------

class CPluginWebApiAsyncClient:
    """Asynchronous WebAPI v2 client — mirrors ``CPluginWebApiClient`` exactly.

    All namespace methods are ``async``; use ``async with`` / ``await aclose()``.
    Constructor arguments, ``timeout`` / ``request_timeout`` / ``retries`` included,
    are the same as for ``CPluginWebApiClient``.

    Attributes for Task 9 (realtime SignalR wiring):
        _api_base (str):      Resolved API base URL without trailing slash.
        _token_getter (callable → str): Zero-arg callable returning the current
                              bearer token synchronously (same public accessor
                              as the sync client).
    """

    def __init__(
        self,
        *,
        env: EnvironmentName = "prod",
        client_id: str | None = None,
        client_secret: str | None = None,
        token: str | None = None,
        api_base_url: str | None = None,
        authority: str | None = None,
        scopes: list[str] | None = None,
        timeout: float | None = DEFAULT_TRANSPORT_TIMEOUT,
        request_timeout: float | None = None,
        retries: int = 2,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        resolved = resolve_environment(env, api_base_url=api_base_url, authority=authority)

        # * Validated up front: a bad client-wide default fails here, not on the first call.
        self._request_timeout: float | None = validate_request_timeout(request_timeout)
        self._timeout: float | None = timeout

        # * Resolved base URL — stored for Task 9 realtime wiring.
        self._api_base: str = resolved.api_base_url

        auth = _build_auth(client_id, client_secret, token, resolved.authority, scopes)
        self._auth = auth

        self._http = httpx.AsyncClient(
            base_url=self._api_base,
            timeout=timeout,
            auth=auth,
            transport=transport or httpx.AsyncHTTPTransport(retries=retries),
        )

        # * Zero-arg sync token getter for Task 9 realtime wiring.
        # * Uses the public current_token() accessor on both auth types.
        # * Async callers should use the underlying auth's _get_token_async directly;
        # * this sync getter is kept for interop with realtime wiring that bootstraps
        # * synchronously.
        self._token_getter: Callable[[], str] = auth.current_token

        self.mt4 = _MT4AsyncNamespace(self)
        self.mt5 = _MT5AsyncNamespace(self)
        self._realtime: RealtimeNamespace | None = None

    @property
    def realtime(self) -> RealtimeNamespace:
        """Real-time SignalR namespace. Requires the optional ``signalrcore`` extra.

        Returns a :class:`~cplugin_webapi_sdk.realtime.RealtimeNamespace` bound to
        this client's base URL and token provider. The realtime layer is always
        synchronous (``signalrcore`` manages its own thread); it is safe to use
        from an async context.

        Example::

            rt = client.realtime.mt5("my-trade-platform-id")
            rt.on_mt5_connection_status(lambda *args: print(args))
            with rt:
                import asyncio; await asyncio.sleep(5)
        """
        # * Lazily create so the client itself is usable without signalrcore.
        if self._realtime is None:
            self._realtime = RealtimeNamespace(
                base_url=self._api_base,
                token_factory=self._token_getter,
            )
        return self._realtime

    async def list_trade_platforms(self) -> list[dict]:
        """Return the raw v1 list of configured trade platforms.

        This endpoint pre-dates the v2 envelope — it returns a plain JSON array.
        Raises ``httpx.HTTPStatusError`` on non-2xx responses.
        """
        # ! v1, unversioned path — NOT covered by the v2 spec / generated layer.
        r = await self._http.get("/api/TradePlatforms")
        r.raise_for_status()
        return r.json()

    async def paged(
        self,
        fetch_page: Callable[[str | None], Any],
    ) -> AsyncGenerator[Any, None]:
        """Async page iterator — mirrors the sync ``paged()`` seam.

        ``fetch_page`` must be an async callable (or coroutine function) that
        accepts a cursor and returns ``(data, meta)``.

        Example::

            async for page_data in client.paged(
                lambda cur: client.mt4.users_request("tp-id", cursor=cur)
            ):
                await process(page_data)
        """
        cursor: str | None = None
        while True:
            data, meta = await fetch_page(cursor)
            yield data
            paging = meta.paging if meta else None
            if not paging or not paging.has_more:
                break
            cursor = paging.next_cursor

    async def aclose(self) -> None:
        """Close the underlying async httpx client."""
        await self._http.aclose()

    async def __aenter__(self) -> "CPluginWebApiAsyncClient":
        return self

    async def __aexit__(self, *exc: Any) -> None:
        await self.aclose()
