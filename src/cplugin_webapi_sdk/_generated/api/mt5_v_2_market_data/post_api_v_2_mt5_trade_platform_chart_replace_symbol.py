from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt5_market_chart_write_request import MT5MarketChartWriteRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    body:    MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  | Unset = UNSET,
    from_: datetime.datetime,
    to: datetime.datetime,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/ChartReplace/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
        "params": params,
    }

    if isinstance(body, MT5MarketChartWriteRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5MarketChartWriteRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5MarketChartWriteRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BooleanApiResponse | None:
    if response.status_code == 200:
        response_200 = BooleanApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BooleanApiResponse]:
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
    body:    MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  | Unset = UNSET,
    from_: datetime.datetime,
    to: datetime.datetime,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Replace the stored minute bars of a period

     <br>
                Replaces the whole chart history of the symbol inside the given window with the bars
    sent:
                every stored bar whose time falls into the window is removed, and the sent ones are
    written
                instead. A bar of the window left out is therefore lost, which is what makes the call
                different from `ChartUpdate`.

    <br>
                The window is given in the trading time of the trade server and is inclusive of its
    bounds.
                Both bounds and at least one bar are required: without a window the call would erase the
                whole chart history of the symbol, and an empty list would only erase the period. Use
                `ChartDelete` to remove bars without sending replacements.

    <br>
                The call changes the history of the trade server and is not reversible: removed bars are
                not kept anywhere, so keep a backup of the trade server before writing. The response
                confirms the trade server accepted the call, not that terminals have already reloaded
    the
                history.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        from_ (datetime.datetime):
        to (datetime.datetime):
        x_request_timeout (float | Unset):
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
body=body,
from_=from_,
to=to,
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
    body:    MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  | Unset = UNSET,
    from_: datetime.datetime,
    to: datetime.datetime,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Replace the stored minute bars of a period

     <br>
                Replaces the whole chart history of the symbol inside the given window with the bars
    sent:
                every stored bar whose time falls into the window is removed, and the sent ones are
    written
                instead. A bar of the window left out is therefore lost, which is what makes the call
                different from `ChartUpdate`.

    <br>
                The window is given in the trading time of the trade server and is inclusive of its
    bounds.
                Both bounds and at least one bar are required: without a window the call would erase the
                whole chart history of the symbol, and an empty list would only erase the period. Use
                `ChartDelete` to remove bars without sending replacements.

    <br>
                The call changes the history of the trade server and is not reversible: removed bars are
                not kept anywhere, so keep a backup of the trade server before writing. The response
                confirms the trade server accepted the call, not that terminals have already reloaded
    the
                history.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        from_ (datetime.datetime):
        to (datetime.datetime):
        x_request_timeout (float | Unset):
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
body=body,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    body:    MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  | Unset = UNSET,
    from_: datetime.datetime,
    to: datetime.datetime,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Replace the stored minute bars of a period

     <br>
                Replaces the whole chart history of the symbol inside the given window with the bars
    sent:
                every stored bar whose time falls into the window is removed, and the sent ones are
    written
                instead. A bar of the window left out is therefore lost, which is what makes the call
                different from `ChartUpdate`.

    <br>
                The window is given in the trading time of the trade server and is inclusive of its
    bounds.
                Both bounds and at least one bar are required: without a window the call would erase the
                whole chart history of the symbol, and an empty list would only erase the period. Use
                `ChartDelete` to remove bars without sending replacements.

    <br>
                The call changes the history of the trade server and is not reversible: removed bars are
                not kept anywhere, so keep a backup of the trade server before writing. The response
                confirms the trade server accepted the call, not that terminals have already reloaded
    the
                history.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        from_ (datetime.datetime):
        to (datetime.datetime):
        x_request_timeout (float | Unset):
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
body=body,
from_=from_,
to=to,
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
    body:    MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  |     MT5MarketChartWriteRequest  | Unset = UNSET,
    from_: datetime.datetime,
    to: datetime.datetime,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Replace the stored minute bars of a period

     <br>
                Replaces the whole chart history of the symbol inside the given window with the bars
    sent:
                every stored bar whose time falls into the window is removed, and the sent ones are
    written
                instead. A bar of the window left out is therefore lost, which is what makes the call
                different from `ChartUpdate`.

    <br>
                The window is given in the trading time of the trade server and is inclusive of its
    bounds.
                Both bounds and at least one bar are required: without a window the call would erase the
                whole chart history of the symbol, and an empty list would only erase the period. Use
                `ChartDelete` to remove bars without sending replacements.

    <br>
                The call changes the history of the trade server and is not reversible: removed bars are
                not kept anywhere, so keep a backup of the trade server before writing. The response
                confirms the trade server accepted the call, not that terminals have already reloaded
    the
                history.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        from_ (datetime.datetime):
        to (datetime.datetime):
        x_request_timeout (float | Unset):
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.
        body (MT5MarketChartWriteRequest | Unset): Minute bars to write into the chart history of
            a symbol.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
body=body,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )).parsed
