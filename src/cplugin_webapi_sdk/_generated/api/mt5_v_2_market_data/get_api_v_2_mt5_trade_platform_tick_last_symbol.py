from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_market_tick_short_api_response import MT5MarketTickShortApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/TickLast/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5MarketTickShortApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5MarketTickShortApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5MarketTickShortApiResponse]:
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
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5MarketTickShortApiResponse]:
    r""" Get the last quote of a symbol

     <br>
                Returns the latest quote of the symbol as the trade server currently holds it, with the
                spread difference of the manager's group already applied — the same figure the terminals
                of that group see. Use `TickLastRaw` for the quote exactly as the data provider sent it.

    <br>
                The call only reads and changes nothing. It requires a connection to the trade platform;
                without one the call is answered with a \"not connected\" error. The symbol must be part
    of
                the quotes the connection receives, otherwise the trade server answers with an error.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5MarketTickShortApiResponse]
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
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT5MarketTickShortApiResponse | None:
    r""" Get the last quote of a symbol

     <br>
                Returns the latest quote of the symbol as the trade server currently holds it, with the
                spread difference of the manager's group already applied — the same figure the terminals
                of that group see. Use `TickLastRaw` for the quote exactly as the data provider sent it.

    <br>
                The call only reads and changes nothing. It requires a connection to the trade platform;
                without one the call is answered with a \"not connected\" error. The symbol must be part
    of
                the quotes the connection receives, otherwise the trade server answers with an error.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5MarketTickShortApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5MarketTickShortApiResponse]:
    r""" Get the last quote of a symbol

     <br>
                Returns the latest quote of the symbol as the trade server currently holds it, with the
                spread difference of the manager's group already applied — the same figure the terminals
                of that group see. Use `TickLastRaw` for the quote exactly as the data provider sent it.

    <br>
                The call only reads and changes nothing. It requires a connection to the trade platform;
                without one the call is answered with a \"not connected\" error. The symbol must be part
    of
                the quotes the connection receives, otherwise the trade server answers with an error.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5MarketTickShortApiResponse]
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
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT5MarketTickShortApiResponse | None:
    r""" Get the last quote of a symbol

     <br>
                Returns the latest quote of the symbol as the trade server currently holds it, with the
                spread difference of the manager's group already applied — the same figure the terminals
                of that group see. Use `TickLastRaw` for the quote exactly as the data provider sent it.

    <br>
                The call only reads and changes nothing. It requires a connection to the trade platform;
                without one the call is answered with a \"not connected\" error. The symbol must be part
    of
                the quotes the connection receives, otherwise the trade server answers with an error.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5MarketTickShortApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
