from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_symbol_info_api_response import MT4SymbolInfoApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    symbol: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["symbol"] = symbol


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/SymbolInfoGet".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4SymbolInfoApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4SymbolInfoApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4SymbolInfoApiResponse]:
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
    symbol: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4SymbolInfoApiResponse]:
    """ Get symbol market data (cached)

     Current cached market data for a single symbol.

    Pump-cached read — Bid/Ask/High/Low/Spread/Digits and last-tick time
    for the requested instrument. Returns NotFound-shaped envelope (the
    platform-level result code surfaces in ManagerAPICode / ErrorCode)
    when the symbol is not loaded on the connected server.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolInfoApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    symbol: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4SymbolInfoApiResponse | None:
    """ Get symbol market data (cached)

     Current cached market data for a single symbol.

    Pump-cached read — Bid/Ask/High/Low/Spread/Digits and last-tick time
    for the requested instrument. Returns NotFound-shaped envelope (the
    platform-level result code surfaces in ManagerAPICode / ErrorCode)
    when the symbol is not loaded on the connected server.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolInfoApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
symbol=symbol,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    symbol: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4SymbolInfoApiResponse]:
    """ Get symbol market data (cached)

     Current cached market data for a single symbol.

    Pump-cached read — Bid/Ask/High/Low/Spread/Digits and last-tick time
    for the requested instrument. Returns NotFound-shaped envelope (the
    platform-level result code surfaces in ManagerAPICode / ErrorCode)
    when the symbol is not loaded on the connected server.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolInfoApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    symbol: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4SymbolInfoApiResponse | None:
    """ Get symbol market data (cached)

     Current cached market data for a single symbol.

    Pump-cached read — Bid/Ask/High/Low/Spread/Digits and last-tick time
    for the requested instrument. Returns NotFound-shaped envelope (the
    platform-level result code surfaces in ManagerAPICode / ErrorCode)
    when the symbol is not loaded on the connected server.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolInfoApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
symbol=symbol,
x_request_timeout=x_request_timeout,

    )).parsed
