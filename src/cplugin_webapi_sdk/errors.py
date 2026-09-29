"""ApiError — raised when a v2 envelope carries a non-null ``error``.

Public surface mirrors the TS SDK: {code, description, activity_id}.
``manager_code`` and ``status`` are retained as extras for diagnostics;
``outcome``, ``applied_timeout`` and ``headers`` come from the response headers
and say what a timeout means for the operation (see ``timeouts``).
"""
from __future__ import annotations

from collections.abc import Mapping

from .envelope import ApiErrorBody, ApiMeta, WebApiErrorCode
from .timeouts import (
    APPLIED_TIMEOUT_HEADER,
    OUTCOME_HEADER,
    is_outcome_unknown,
    is_safe_to_retry,
)


def _header(headers: Mapping[str, str], name: str) -> str | None:
    # * httpx.Headers is case-insensitive; a plain dict (tests, custom shims) may not be.
    value = headers.get(name)
    if value is None:
        lowered = name.lower()
        value = next((v for k, v in headers.items() if k.lower() == lowered), None)
    return value


class ApiError(Exception):
    """Raised by the transport when an envelope's ``error`` field is non-null.

    Attributes:
        code:            Stable error code (``ErrorCode``), e.g. ``"OutcomeUnknown"``.
        description:     Human-readable message from the server.
        activity_id:     Trace id to quote when reporting the problem.
        manager_code:    Raw trade-platform result code, when there is one.
        status:          HTTP status (v2 answers 200 even on errors).
        outcome:         ``X-Request-Outcome`` header (``RequestOutcome``): ``"timeout"``,
                         ``"unknown"``, ``"not-started"``, ``"in-progress"``, or ``None``.
        applied_timeout: ``X-Request-Timeout-Applied`` header — the deadline the server
                         used, in seconds — or ``None``.
        headers:         All response headers.
    """

    def __init__(
        self,
        body: ApiErrorBody,
        meta: ApiMeta | None,
        status: int,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        self.code: WebApiErrorCode = body.code
        self.description: str | None = body.message
        self.activity_id: str | None = meta.activity_id if meta is not None else None
        self.manager_code: str | int | None = body.manager_code
        self.status: int = status
        self.headers: Mapping[str, str] = headers if headers is not None else {}

        outcome = _header(self.headers, OUTCOME_HEADER)
        self.outcome: str | None = outcome.strip().lower() if outcome and outcome.strip() else None

        applied = _header(self.headers, APPLIED_TIMEOUT_HEADER)
        try:
            self.applied_timeout: float | None = float(applied) if applied else None
        except ValueError:
            self.applied_timeout = None

        super().__init__(self.description or f"v2 error: {body.code}")

    @property
    def outcome_unknown(self) -> bool:
        """The operation may still be applied — check before repeating (see ``is_outcome_unknown``)."""
        return is_outcome_unknown(self)

    @property
    def safe_to_retry(self) -> bool:
        """Repeating the request cannot apply the operation twice (see ``is_safe_to_retry``)."""
        return is_safe_to_retry(self)
