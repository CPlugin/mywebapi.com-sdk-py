from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_tick_info_api_response import MT4TickInfoApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/TickInfoLast/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4TickInfoApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4TickInfoApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4TickInfoApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4TickInfoApiResponse]:
    """ Get last tick (cached)

     Last known bid/ask tick for a single symbol from the pump cache.

    Pump-cached read of the last tick. For sub-second updates prefer the
    SignalR tick stream over polling. Returns NotFound envelope when the
    pump cache has no tick for the requested symbol (symbol not in the
    active subscription set, or the platform has never received a tick
    since startup).

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TickInfoApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> MT4TickInfoApiResponse | None:
    """ Get last tick (cached)

     Last known bid/ask tick for a single symbol from the pump cache.

    Pump-cached read of the last tick. For sub-second updates prefer the
    SignalR tick stream over polling. Returns NotFound envelope when the
    pump cache has no tick for the requested symbol (symbol not in the
    active subscription set, or the platform has never received a tick
    since startup).

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TickInfoApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4TickInfoApiResponse]:
    """ Get last tick (cached)

     Last known bid/ask tick for a single symbol from the pump cache.

    Pump-cached read of the last tick. For sub-second updates prefer the
    SignalR tick stream over polling. Returns NotFound envelope when the
    pump cache has no tick for the requested symbol (symbol not in the
    active subscription set, or the platform has never received a tick
    since startup).

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TickInfoApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> MT4TickInfoApiResponse | None:
    """ Get last tick (cached)

     Last known bid/ask tick for a single symbol from the pump cache.

    Pump-cached read of the last tick. For sub-second updates prefer the
    SignalR tick stream over polling. Returns NotFound envelope when the
    pump cache has no tick for the requested symbol (symbol not in the
    active subscription set, or the platform has never received a tick
    since startup).

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TickInfoApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,

    )).parsed
