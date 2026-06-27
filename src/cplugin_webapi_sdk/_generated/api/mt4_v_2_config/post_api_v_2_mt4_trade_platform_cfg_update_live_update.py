from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_live_update import MT4LiveUpdate
from ...models.mt4_live_update_api_response import MT4LiveUpdateApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4LiveUpdate  |     MT4LiveUpdate  |     MT4LiveUpdate  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateLiveUpdate".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4LiveUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4LiveUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4LiveUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4LiveUpdateApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4LiveUpdateApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4LiveUpdateApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4LiveUpdate  |     MT4LiveUpdate  |     MT4LiveUpdate  | Unset = UNSET,

) -> Response[MT4LiveUpdateApiResponse]:
    """ Update LiveUpdate config

     Update a LiveUpdate service configuration — Type 1 mutator.

    Manager (live) call. LiveUpdate entries are paged on the read side
    (see `CfgRequestLiveUpdate`); the v2 contract identifies an
    entry by its `Company` field (same cursor key the read
    endpoint uses). Flow: read live list → match by `Company` →
    overlay → write back. The 128-element `Files` descriptor
    table and the runtime `Connections` counter are preserved
    server-side.

    Args:
        trade_platform (UUID):
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4LiveUpdateApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4LiveUpdate  |     MT4LiveUpdate  |     MT4LiveUpdate  | Unset = UNSET,

) -> MT4LiveUpdateApiResponse | None:
    """ Update LiveUpdate config

     Update a LiveUpdate service configuration — Type 1 mutator.

    Manager (live) call. LiveUpdate entries are paged on the read side
    (see `CfgRequestLiveUpdate`); the v2 contract identifies an
    entry by its `Company` field (same cursor key the read
    endpoint uses). Flow: read live list → match by `Company` →
    overlay → write back. The 128-element `Files` descriptor
    table and the runtime `Connections` counter are preserved
    server-side.

    Args:
        trade_platform (UUID):
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4LiveUpdateApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4LiveUpdate  |     MT4LiveUpdate  |     MT4LiveUpdate  | Unset = UNSET,

) -> Response[MT4LiveUpdateApiResponse]:
    """ Update LiveUpdate config

     Update a LiveUpdate service configuration — Type 1 mutator.

    Manager (live) call. LiveUpdate entries are paged on the read side
    (see `CfgRequestLiveUpdate`); the v2 contract identifies an
    entry by its `Company` field (same cursor key the read
    endpoint uses). Flow: read live list → match by `Company` →
    overlay → write back. The 128-element `Files` descriptor
    table and the runtime `Connections` counter are preserved
    server-side.

    Args:
        trade_platform (UUID):
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4LiveUpdateApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4LiveUpdate  |     MT4LiveUpdate  |     MT4LiveUpdate  | Unset = UNSET,

) -> MT4LiveUpdateApiResponse | None:
    """ Update LiveUpdate config

     Update a LiveUpdate service configuration — Type 1 mutator.

    Manager (live) call. LiveUpdate entries are paged on the read side
    (see `CfgRequestLiveUpdate`); the v2 contract identifies an
    entry by its `Company` field (same cursor key the read
    endpoint uses). Flow: read live list → match by `Company` →
    overlay → write back. The 128-element `Files` descriptor
    table and the runtime `Connections` counter are preserved
    server-side.

    Args:
        trade_platform (UUID):
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.
        body (MT4LiveUpdate | Unset): v2 DTO for a single MT4 LiveUpdate configuration entry.
            Curated
            subset of the wrapper's ConLiveUpdate — exposes the metadata
            (Company, Path, Version/Build, connection limits and counters,
            Type, Enable, TotalFiles). The wrapper's `Files` array
            (128-element LiveInfoFile descriptor table) is intentionally
            deferred to a future endpoint to keep this payload tractable; v2
            callers needing per-file detail will get a separate
            `CfgRequestLiveUpdateFiles` in a later slice.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4LiveUpdateApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,

    )).parsed
