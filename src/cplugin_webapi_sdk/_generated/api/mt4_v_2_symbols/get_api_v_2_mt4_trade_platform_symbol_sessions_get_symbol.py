from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_symbol_day_sessions_list_api_response import MT4SymbolDaySessionsListApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/SymbolSessionsGet/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4SymbolDaySessionsListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4SymbolDaySessionsListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4SymbolDaySessionsListApiResponse]:
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

) -> Response[MT4SymbolDaySessionsListApiResponse]:
    """ Get symbol sessions

     Trading session windows for a symbol, per weekday.

    Returns the wrapper's `ConSymbol.Sessions[7]` array (one entry
    per weekday, 0=Sunday). Each weekday entry carries up to three Quote
    (price) windows and up to three Trade (order acceptance) windows
    plus overnight flags. Closes the TODO documented in
    `MT4SymbolConfig`: the parent `CfgRequestSymbol` endpoint
    drops the nested Sessions array to keep the DTO manageable; this
    dedicated endpoint exposes it.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolDaySessionsListApiResponse]
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

) -> MT4SymbolDaySessionsListApiResponse | None:
    """ Get symbol sessions

     Trading session windows for a symbol, per weekday.

    Returns the wrapper's `ConSymbol.Sessions[7]` array (one entry
    per weekday, 0=Sunday). Each weekday entry carries up to three Quote
    (price) windows and up to three Trade (order acceptance) windows
    plus overnight flags. Closes the TODO documented in
    `MT4SymbolConfig`: the parent `CfgRequestSymbol` endpoint
    drops the nested Sessions array to keep the DTO manageable; this
    dedicated endpoint exposes it.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolDaySessionsListApiResponse
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

) -> Response[MT4SymbolDaySessionsListApiResponse]:
    """ Get symbol sessions

     Trading session windows for a symbol, per weekday.

    Returns the wrapper's `ConSymbol.Sessions[7]` array (one entry
    per weekday, 0=Sunday). Each weekday entry carries up to three Quote
    (price) windows and up to three Trade (order acceptance) windows
    plus overnight flags. Closes the TODO documented in
    `MT4SymbolConfig`: the parent `CfgRequestSymbol` endpoint
    drops the nested Sessions array to keep the DTO manageable; this
    dedicated endpoint exposes it.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolDaySessionsListApiResponse]
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

) -> MT4SymbolDaySessionsListApiResponse | None:
    """ Get symbol sessions

     Trading session windows for a symbol, per weekday.

    Returns the wrapper's `ConSymbol.Sessions[7]` array (one entry
    per weekday, 0=Sunday). Each weekday entry carries up to three Quote
    (price) windows and up to three Trade (order acceptance) windows
    plus overnight flags. Closes the TODO documented in
    `MT4SymbolConfig`: the parent `CfgRequestSymbol` endpoint
    drops the nested Sessions array to keep the DTO manageable; this
    dedicated endpoint exposes it.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolDaySessionsListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,

    )).parsed
