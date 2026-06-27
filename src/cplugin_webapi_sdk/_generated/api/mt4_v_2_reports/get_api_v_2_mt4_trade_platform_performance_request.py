from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_performance_list_api_response import MT4PerformanceListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    *,
    from_: datetime.datetime | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/PerformanceRequest".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4PerformanceListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4PerformanceListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4PerformanceListApiResponse]:
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
    from_: datetime.datetime | Unset = UNSET,

) -> Response[MT4PerformanceListApiResponse]:
    """ Get server performance series

     Time series of MT4 server resource snapshots — CPU, memory, network, sockets, connected-users —
    captured at server-defined cadence.

    Manager-live read (round-trip to MT4 server). The MT4 server records
    these snapshots periodically (typically every five minutes, broker-
    configurable). Pass from as the earliest timestamp
    to include; the server returns every snapshot at or after that point
    up to the present, in ascending `Ctm` order. Useful for capacity
    dashboards, oncall incident timelines, and load investigations. Pump
    cache is NOT consulted — data reflects the authoritative server log.
    Returns an empty list (Ok envelope, not an error) when the window
    contains no snapshots.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4PerformanceListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,

) -> MT4PerformanceListApiResponse | None:
    """ Get server performance series

     Time series of MT4 server resource snapshots — CPU, memory, network, sockets, connected-users —
    captured at server-defined cadence.

    Manager-live read (round-trip to MT4 server). The MT4 server records
    these snapshots periodically (typically every five minutes, broker-
    configurable). Pass from as the earliest timestamp
    to include; the server returns every snapshot at or after that point
    up to the present, in ascending `Ctm` order. Useful for capacity
    dashboards, oncall incident timelines, and load investigations. Pump
    cache is NOT consulted — data reflects the authoritative server log.
    Returns an empty list (Ok envelope, not an error) when the window
    contains no snapshots.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4PerformanceListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,

) -> Response[MT4PerformanceListApiResponse]:
    """ Get server performance series

     Time series of MT4 server resource snapshots — CPU, memory, network, sockets, connected-users —
    captured at server-defined cadence.

    Manager-live read (round-trip to MT4 server). The MT4 server records
    these snapshots periodically (typically every five minutes, broker-
    configurable). Pass from as the earliest timestamp
    to include; the server returns every snapshot at or after that point
    up to the present, in ascending `Ctm` order. Useful for capacity
    dashboards, oncall incident timelines, and load investigations. Pump
    cache is NOT consulted — data reflects the authoritative server log.
    Returns an empty list (Ok envelope, not an error) when the window
    contains no snapshots.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4PerformanceListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,

) -> MT4PerformanceListApiResponse | None:
    """ Get server performance series

     Time series of MT4 server resource snapshots — CPU, memory, network, sockets, connected-users —
    captured at server-defined cadence.

    Manager-live read (round-trip to MT4 server). The MT4 server records
    these snapshots periodically (typically every five minutes, broker-
    configurable). Pass from as the earliest timestamp
    to include; the server returns every snapshot at or after that point
    up to the present, in ascending `Ctm` order. Useful for capacity
    dashboards, oncall incident timelines, and load investigations. Pump
    cache is NOT consulted — data reflects the authoritative server log.
    Returns an empty list (Ok envelope, not an error) when the window
    contains no snapshots.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4PerformanceListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,

    )).parsed
