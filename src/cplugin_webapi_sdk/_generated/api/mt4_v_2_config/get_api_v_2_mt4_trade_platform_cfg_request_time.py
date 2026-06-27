from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_server_time_api_response import MT4ServerTimeApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/CfgRequestTime".format(trade_platform=quote(str(trade_platform), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4ServerTimeApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4ServerTimeApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4ServerTimeApiResponse]:
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

) -> Response[MT4ServerTimeApiResponse]:
    """ Get access-hour matrix

     Server access-hour matrix (per-hour 7×24 allow/deny grid) from the MT4 server's `ConTime`
    configuration.

    Manager-live read (round-trip). Returns `MT4ServerTime` with
    a flat 168-element `AccessHours` array; each element is 0
    (denied) or 1 (allowed) for one hour of the week. Layout:
    `index = day*24 + hour`, day 0 = Sunday (MT4 convention).
    Internal `DaysControl` and `Reserved` wrapper fields
    are not surfaced.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ServerTimeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> MT4ServerTimeApiResponse | None:
    """ Get access-hour matrix

     Server access-hour matrix (per-hour 7×24 allow/deny grid) from the MT4 server's `ConTime`
    configuration.

    Manager-live read (round-trip). Returns `MT4ServerTime` with
    a flat 168-element `AccessHours` array; each element is 0
    (denied) or 1 (allowed) for one hour of the week. Layout:
    `index = day*24 + hour`, day 0 = Sunday (MT4 convention).
    Internal `DaysControl` and `Reserved` wrapper fields
    are not surfaced.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ServerTimeApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4ServerTimeApiResponse]:
    """ Get access-hour matrix

     Server access-hour matrix (per-hour 7×24 allow/deny grid) from the MT4 server's `ConTime`
    configuration.

    Manager-live read (round-trip). Returns `MT4ServerTime` with
    a flat 168-element `AccessHours` array; each element is 0
    (denied) or 1 (allowed) for one hour of the week. Layout:
    `index = day*24 + hour`, day 0 = Sunday (MT4 convention).
    Internal `DaysControl` and `Reserved` wrapper fields
    are not surfaced.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ServerTimeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> MT4ServerTimeApiResponse | None:
    """ Get access-hour matrix

     Server access-hour matrix (per-hour 7×24 allow/deny grid) from the MT4 server's `ConTime`
    configuration.

    Manager-live read (round-trip). Returns `MT4ServerTime` with
    a flat 168-element `AccessHours` array; each element is 0
    (denied) or 1 (allowed) for one hour of the week. Layout:
    `index = day*24 + hour`, day 0 = Sunday (MT4 convention).
    Internal `DaysControl` and `Reserved` wrapper fields
    are not surfaced.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ServerTimeApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,

    )).parsed
