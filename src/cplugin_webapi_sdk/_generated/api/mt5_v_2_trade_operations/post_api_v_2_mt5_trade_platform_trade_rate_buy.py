from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.trade_rate_request import TradeRateRequest
from ...models.trade_rate_result_api_response import TradeRateResultApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    TradeRateRequest  |     TradeRateRequest  |     TradeRateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/TradeRateBuy".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, TradeRateRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, TradeRateRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, TradeRateRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TradeRateResultApiResponse | None:
    if response.status_code == 200:
        response_200 = TradeRateResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TradeRateResultApiResponse]:
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
    body:    TradeRateRequest  |     TradeRateRequest  |     TradeRateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[TradeRateResultApiResponse]:
    """ Calculate the rate of buying a currency for another one

     <br>
                Calculates how much of the calculation currency pays for one unit of the base currency
                when it is bought. With a group the spread adjustment of that group is applied; without
                it the market prices are used. A symbol and its price replace the market quote of that
                symbol in the calculation, unless the symbol is always converted at the market price.

    <br>
                Nothing is created or changed. The rate is built from current market data, so the
                connection must have the orders and positions of the platform loaded.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TradeRateResultApiResponse]
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
    body:    TradeRateRequest  |     TradeRateRequest  |     TradeRateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> TradeRateResultApiResponse | None:
    """ Calculate the rate of buying a currency for another one

     <br>
                Calculates how much of the calculation currency pays for one unit of the base currency
                when it is bought. With a group the spread adjustment of that group is applied; without
                it the market prices are used. A symbol and its price replace the market quote of that
                symbol in the calculation, unless the symbol is always converted at the market price.

    <br>
                Nothing is created or changed. The rate is built from current market data, so the
                connection must have the orders and positions of the platform loaded.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TradeRateResultApiResponse
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
    body:    TradeRateRequest  |     TradeRateRequest  |     TradeRateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[TradeRateResultApiResponse]:
    """ Calculate the rate of buying a currency for another one

     <br>
                Calculates how much of the calculation currency pays for one unit of the base currency
                when it is bought. With a group the spread adjustment of that group is applied; without
                it the market prices are used. A symbol and its price replace the market quote of that
                symbol in the calculation, unless the symbol is always converted at the market price.

    <br>
                Nothing is created or changed. The rate is built from current market data, so the
                connection must have the orders and positions of the platform loaded.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TradeRateResultApiResponse]
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
    body:    TradeRateRequest  |     TradeRateRequest  |     TradeRateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> TradeRateResultApiResponse | None:
    """ Calculate the rate of buying a currency for another one

     <br>
                Calculates how much of the calculation currency pays for one unit of the base currency
                when it is bought. With a group the spread adjustment of that group is applied; without
                it the market prices are used. A symbol and its price replace the market quote of that
                symbol in the calculation, unless the symbol is always converted at the market price.

    <br>
                Nothing is created or changed. The rate is built from current market data, so the
                connection must have the orders and positions of the platform loaded.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.
        body (TradeRateRequest | Unset): Conditions of a conversion rate calculation, v2 request
            DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TradeRateResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
