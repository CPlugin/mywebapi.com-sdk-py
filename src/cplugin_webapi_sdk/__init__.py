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

__all__ = [
    # * Primary client classes
    "CPluginWebApiClient",
    "CPluginWebApiAsyncClient",
    # * Error surface
    "ApiError",
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
    # * Real-time SignalR clients (optional signalrcore extra)
    "MT4RealtimeClient",
    "MT5RealtimeClient",
    "SignalRNotInstalledError",
]
