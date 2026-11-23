from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.double_api_response import DoubleApiResponse
from ...models.mt4_trade_calc_profit_request import MT4TradeCalcProfitRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/TradeCalcProfit".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4TradeCalcProfitRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4TradeCalcProfitRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4TradeCalcProfitRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DoubleApiResponse | None:
    if response.status_code == 200:
        response_200 = DoubleApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DoubleApiResponse]:
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
    body:    MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[DoubleApiResponse]:
    """ Recalculate the profit of a trade

     Calculates the profit the supplied trade would carry at the prices
    given in the body, using the symbol's current conversion rates.

    Nothing is written anywhere: this is a calculation over a trade that
    exists only in the request, and it is safe to repeat. The result is the
    profit in the server's summary currency. An unknown symbol or an
    unknown direction answers with a validation or platform error in the
    error envelope.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DoubleApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
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
    body:    MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> DoubleApiResponse | None:
    """ Recalculate the profit of a trade

     Calculates the profit the supplied trade would carry at the prices
    given in the body, using the symbol's current conversion rates.

    Nothing is written anywhere: this is a calculation over a trade that
    exists only in the request, and it is safe to repeat. The result is the
    profit in the server's summary currency. An unknown symbol or an
    unknown direction answers with a validation or platform error in the
    error envelope.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DoubleApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[DoubleApiResponse]:
    """ Recalculate the profit of a trade

     Calculates the profit the supplied trade would carry at the prices
    given in the body, using the symbol's current conversion rates.

    Nothing is written anywhere: this is a calculation over a trade that
    exists only in the request, and it is safe to repeat. The result is the
    profit in the server's summary currency. An unknown symbol or an
    unknown direction answers with a validation or platform error in the
    error envelope.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DoubleApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
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
    body:    MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  |     MT4TradeCalcProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> DoubleApiResponse | None:
    """ Recalculate the profit of a trade

     Calculates the profit the supplied trade would carry at the prices
    given in the body, using the symbol's current conversion rates.

    Nothing is written anywhere: this is a calculation over a trade that
    exists only in the request, and it is safe to repeat. The result is the
    profit in the server's summary currency. An unknown symbol or an
    unknown direction answers with a validation or platform error in the
    error envelope.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.
        body (MT4TradeCalcProfitRequest | Unset): Input of the profit calculation: the trade
            fields the calculation reads.
            Only these fields take part in the result — stops, magic number, comment
            and timestamps do not change it.
            <br>
            Nothing is written anywhere: the trade record is assembled in memory,
            priced against the symbol's current conversion rates, and only the
            resulting profit is returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DoubleApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
