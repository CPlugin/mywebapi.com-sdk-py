"""CPlugin SaaS WebAPI Python SDK — v2.

Public surface for import::

    from cplugin_webapi_sdk import CPluginWebApiClient, ApiError
"""
from .client import CPluginWebApiClient, CPluginWebApiAsyncClient
from .errors import ApiError
from .envelope import ApiEnvelope, ApiMeta, ApiErrorBody, PagingMeta
from .environments import resolve_environment, ResolvedEnvironment, EnvironmentName
from .auth import ClientCredentialsAuth, BearerAuth, OAuth2TokenError
from .unwrap import unwrap, unwrap_async, unwrap_with_meta, unwrap_with_meta_async
from .pagination import (
    paginate_sync,
    collect_all_sync,
    paginate_async,
    collect_all_async,
    PageFetcherSync,
    PageFetcherAsync,
)
from .realtime import MT4RealtimeClient, MT5RealtimeClient, SignalRNotInstalledError
from .flags import parse_flags, format_flags, has_flag, with_flag
from .timeouts import (
    ErrorCode,
    RequestOutcome,
    is_outcome_unknown,
    is_safe_to_retry,
    MIN_REQUEST_TIMEOUT,
    MAX_REQUEST_TIMEOUT,
)

__all__ = [
    # * Primary client classes
    "CPluginWebApiClient",
    "CPluginWebApiAsyncClient",
    # * Error surface
    "ApiError",
    # * Timeouts and retries — error codes, X-Request-Outcome values, retry classification
    "ErrorCode",
    "RequestOutcome",
    "is_outcome_unknown",
    "is_safe_to_retry",
    "MIN_REQUEST_TIMEOUT",
    "MAX_REQUEST_TIMEOUT",
    # * Envelope types (for typed access to response metadata)
    "ApiEnvelope",
    "ApiMeta",
    "ApiErrorBody",
    "PagingMeta",
    # * Environment helpers
    "resolve_environment",
    "ResolvedEnvironment",
    "EnvironmentName",
    # * Auth classes (for custom httpx pipelines)
    "ClientCredentialsAuth",
    "BearerAuth",
    "OAuth2TokenError",
    # * Unwrap helpers (for use with raw() escape hatch)
    "unwrap",
    "unwrap_async",
    "unwrap_with_meta",
    "unwrap_with_meta_async",
    # * Pagination helpers — cursor-based iteration over meta.paging
    "paginate_sync",
    "collect_all_sync",
    "paginate_async",
    "collect_all_async",
    "PageFetcherSync",
    "PageFetcherAsync",
    # * Flag fields ("Enabled, Password") — user rights, group and symbol flags
    "parse_flags",
    "format_flags",
    "has_flag",
    "with_flag",
    # * Real-time SignalR clients (optional signalrcore extra)
    "MT4RealtimeClient",
    "MT5RealtimeClient",
    "SignalRNotInstalledError",
]
