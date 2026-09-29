"""Request timeouts, retry classification and idempotency keys.

The server gives every call addressed to a trade platform a deadline. When the
trade server does not answer in time the API still answers (v2: HTTP 200 with an
error envelope), and the error code plus the ``X-Request-Outcome`` header say
whether the operation may still be applied:

- ``Timeout`` / ``timeout`` — a read did not finish; nothing changed. Safe to retry.
- ``Busy`` / ``not-started`` — refused before it was sent. Safe to retry.
- ``OutcomeUnknown`` / ``unknown`` — a trade or change did not finish and may still
  be applied. Check the result; never retry blindly.
- ``OutcomeUnknown`` / ``in-progress`` — a request with the same ``Idempotency-Key``
  is still running; this one was not executed.

Default deadlines per operation kind: trade 5 s, read 10 s, change 15 s,
history 30 s, maintenance 60 s. A caller chooses its own with ``X-Request-Timeout``
(seconds, 1–300); the applied value comes back in ``X-Request-Timeout-Applied``.
"""
from __future__ import annotations

import math
from typing import Any

# * Wire names.
REQUEST_TIMEOUT_HEADER = "X-Request-Timeout"
APPLIED_TIMEOUT_HEADER = "X-Request-Timeout-Applied"
OUTCOME_HEADER = "X-Request-Outcome"
IDEMPOTENCY_KEY_HEADER = "Idempotency-Key"

# * Bounds the server accepts for X-Request-Timeout; anything else answers Validation.
MIN_REQUEST_TIMEOUT = 1.0
MAX_REQUEST_TIMEOUT = 300.0

# * Longest Idempotency-Key the server accepts (draft-ietf-httpapi-idempotency-key-header).
MAX_IDEMPOTENCY_KEY_LENGTH = 255

# * How much longer than the requested server deadline the HTTP client waits.
# ! The server may extend its deadline by the time it spends opening the trade-platform
# !   connection for this request — up to 20 s — so it can answer as late as
# !   request_timeout + 20 s. 10 s more covers the network. A shorter margin makes the
# !   client give up first and lose the answer that says whether a trade was applied.
# ? Not a hard bound: the server's deadline starts after it has read the body and taken
# ?   the idempotency key, and those steps have no deadline of their own.
TRANSPORT_TIMEOUT_MARGIN = 30.0

# * Default HTTP client timeout: the longest server default (maintenance, 60 s)
#   plus the same margin, so no default-deadline call is cut off by the client.
DEFAULT_TRANSPORT_TIMEOUT = 90.0


class ErrorCode:
    """Values of ``error.code`` (``ApiError.code``) in a v2 envelope.

    The code is a plain string on the wire; unknown future codes arrive unchanged.
    """

    OK = "Ok"
    NO_CONNECT = "NoConnect"
    VALIDATION = "Validation"
    MT4_ERROR = "MT4Error"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    MT5_ERROR = "MT5Error"
    #: A read did not finish in time. Nothing changed; safe to retry.
    TIMEOUT = "Timeout"
    #: A trade or change did not finish in time and may still be applied, or a request
    #: with the same idempotency key is still running. Check the result before retrying.
    OUTCOME_UNKNOWN = "OutcomeUnknown"
    #: Too many requests wait for this trade platform; not sent. Safe to retry.
    BUSY = "Busy"
    INTERNAL = "Internal"
    #: Produced by the SDK, not the server: the body was not a v2 envelope
    #: (e.g. an HTML 502/504 page from a proxy).
    INVALID_RESPONSE = "InvalidResponse"


class RequestOutcome:
    """Values of the ``X-Request-Outcome`` response header (``ApiError.outcome``)."""

    #: The operation did not finish in time and changed nothing.
    TIMEOUT = "timeout"
    #: A trade or change did not finish in time and may still be applied.
    UNKNOWN = "unknown"
    #: The request was refused before it reached the trade server.
    NOT_STARTED = "not-started"
    #: A request with the same idempotency key is still being processed; this one was not executed.
    IN_PROGRESS = "in-progress"


_SAFE_CODES = frozenset({ErrorCode.TIMEOUT, ErrorCode.BUSY})
_SAFE_OUTCOMES = frozenset({RequestOutcome.TIMEOUT, RequestOutcome.NOT_STARTED})
_UNKNOWN_OUTCOMES = frozenset({RequestOutcome.UNKNOWN, RequestOutcome.IN_PROGRESS})


def validate_request_timeout(value: Any, *, name: str = "request_timeout") -> float | None:
    """Return ``value`` as seconds, ``None`` for ``None``; raise ``ValueError``/``TypeError`` otherwise.

    The server accepts 1 to 300 seconds, fractions included.
    """
    if value is None:
        return None
    # ! bool is an int subclass: True would silently mean one second.
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a number of seconds, got {type(value).__name__}")
    seconds = float(value)
    if math.isnan(seconds) or not MIN_REQUEST_TIMEOUT <= seconds <= MAX_REQUEST_TIMEOUT:
        raise ValueError(
            f"{name} must be from {MIN_REQUEST_TIMEOUT:g} to {MAX_REQUEST_TIMEOUT:g} seconds, got {value!r}"
        )
    return seconds


def validate_idempotency_key(value: Any) -> str | None:
    """Return the key unchanged, ``None`` for ``None``; reject empty, over-long or non-ASCII keys."""
    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError(f"idempotency_key must be a str, got {type(value).__name__}")
    if not value.strip():
        raise ValueError("idempotency_key must not be empty")
    if len(value) > MAX_IDEMPOTENCY_KEY_LENGTH:
        raise ValueError(f"idempotency_key must be at most {MAX_IDEMPOTENCY_KEY_LENGTH} characters")
    # ! An HTTP header value must be printable ASCII; httpx would otherwise fail
    # !   with an encoding error far from the caller's line.
    if not value.isascii() or not value.isprintable():
        raise ValueError("idempotency_key must be printable ASCII")
    return value


def format_seconds(seconds: float) -> str:
    """Seconds as the server writes them: invariant culture, up to three decimals (``10``, ``2.5``)."""
    return f"{seconds:.3f}".rstrip("0").rstrip(".")


def transport_timeout(base: float | None, request_timeout: float | None) -> float | None:
    """HTTP client timeout for one call: never shorter than ``request_timeout`` + margin.

    ``base`` is the client-wide timeout (``None`` = no limit, which already waits long enough).
    """
    if request_timeout is None or base is None:
        return base
    return max(base, request_timeout + TRANSPORT_TIMEOUT_MARGIN)


def _code_and_outcome(error: BaseException) -> tuple[str | None, str | None]:
    code = getattr(error, "code", None)
    outcome = getattr(error, "outcome", None)
    return (code if isinstance(code, str) else None, outcome if isinstance(outcome, str) else None)


def is_outcome_unknown(error: BaseException) -> bool:
    """Whether the failed operation may still be applied by the trade server.

    True for ``OutcomeUnknown`` (``X-Request-Outcome: unknown`` or ``in-progress``).
    Do not repeat such a request blindly — for a trade that means a second trade.
    Check the result (orders, positions, balance, the changed record), or repeat it
    with the **same** ``idempotency_key``: while the first one runs you get
    ``in-progress`` again, once it has finished you get its real result without it
    being executed twice.

    Anything that is not an ``ApiError`` returns False: the SDK cannot tell from a
    transport exception (``httpx.ReadTimeout``) whether the request was a write — for a
    trade or change treat those as unknown too.
    """
    code, outcome = _code_and_outcome(error)
    return code == ErrorCode.OUTCOME_UNKNOWN or outcome in _UNKNOWN_OUTCOMES


def is_safe_to_retry(error: BaseException) -> bool:
    """Whether repeating the request cannot apply the operation twice.

    True for ``Timeout`` (a read that changed nothing) and ``Busy`` (refused before
    it was sent), and for the matching ``X-Request-Outcome`` values ``timeout`` and
    ``not-started``. False for everything else, ``OutcomeUnknown`` above all — other
    codes (``Validation``, ``NotFound``, platform errors) will not succeed on a
    plain retry either.
    """
    if is_outcome_unknown(error):
        return False
    code, outcome = _code_and_outcome(error)
    return code in _SAFE_CODES or outcome in _SAFE_OUTCOMES
