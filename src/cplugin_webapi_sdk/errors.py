"""ApiError — raised when a v2 envelope carries a non-null ``error``.

Public surface mirrors the TS SDK: {code, description, activity_id}.
``manager_code`` and ``status`` are retained as extras for diagnostics.

The actual raising happens in Task 4 (unwrap.py). This module only defines
the exception type so other modules can import it without a circular dependency.
"""
from __future__ import annotations

from .envelope import ApiErrorBody, ApiMeta, WebApiErrorCode


class ApiError(Exception):
    """Raised by the transport when an envelope's ``error`` field is non-null."""

    def __init__(self, body: ApiErrorBody, meta: ApiMeta | None, status: int) -> None:
        self.code: WebApiErrorCode = body.code
        self.description: str | None = body.message
        self.activity_id: str | None = meta.activity_id if meta is not None else None
        self.manager_code: str | int | None = body.manager_code
        self.status: int = status
        super().__init__(self.description or f"v2 error: {body.code}")
