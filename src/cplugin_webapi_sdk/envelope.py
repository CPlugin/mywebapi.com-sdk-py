"""v2 response envelope: {data, error, meta}.

Mirrors the TS SDK's ApiEnvelope[T] / ApiErrorBody / ApiMeta / PagingMeta.
The server always returns HTTP 200 and signals failure in-envelope via a
non-null ``error``. Field aliases map the server's camelCase JSON to
snake_case Python attributes.

Schema reference: spec/v2.json components.schemas.{ApiError,ApiMeta,PagingMeta}.
"""
from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")

# * Stable transport-level error codes (WebApiErrorCode). Kept as a plain str
#   so unknown future codes never raise on parse. The spec defines a fixed enum
#   (Unauthorized, Forbidden, NotFound, Internal, …) but the wire type is a
#   string — new codes would otherwise be rejected by a Literal union.
WebApiErrorCode = str


class PagingMeta(BaseModel):
    """Pagination cursor returned on list endpoints."""

    model_config = ConfigDict(populate_by_name=True)

    # * nextCursor is the opaque page token; pass it back as ?cursor=.
    next_cursor: str | None = Field(default=None, alias="nextCursor")
    # * hasMore is the explicit boolean sentinel so callers avoid null-string checks.
    has_more: bool = Field(default=False, alias="hasMore")


class ApiMeta(BaseModel):
    """Response metadata present on every v2 response."""

    model_config = ConfigDict(populate_by_name=True)

    # * W3C trace id — correlate this response in Seq/SigNoz logs.
    activity_id: str | None = Field(default=None, alias="activityId")
    # * Pagination info; null for non-list endpoints.
    paging: PagingMeta | None = None


class ApiErrorBody(BaseModel):
    """Parsed representation of the ``error`` field in a v2 envelope.

    ``code`` is the stable transport-level error code (WebApiErrorCode).
    ``manager_code`` is the raw MT4/MT5 ResultCode: a string for named enum
    members, an integer for unrecognised numeric codes.
    ``message`` is the human-readable description.
    """

    model_config = ConfigDict(populate_by_name=True)

    code: WebApiErrorCode
    # ! Raw MT4/MT5 ResultCode: a string for a named member, a number otherwise.
    manager_code: str | int | None = Field(default=None, alias="managerCode")
    message: str | None = None


class ApiEnvelope(BaseModel, Generic[T]):
    """Top-level v2 envelope: {data, error, meta}.

    ``data`` carries the typed payload on success (non-null).
    ``error`` is non-null on failure; the transport raises ApiError in that case.
    ``meta`` carries correlation and pagination metadata.
    """

    model_config = ConfigDict(populate_by_name=True)

    data: T | None = None
    error: ApiErrorBody | None = None
    meta: ApiMeta | None = None
