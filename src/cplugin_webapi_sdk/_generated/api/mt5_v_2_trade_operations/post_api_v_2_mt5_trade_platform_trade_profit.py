from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.trade_profit_request import TradeProfitRequest
from ...models.trade_profit_result_api_response import TradeProfitResultApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    TradeProfitRequest  |     TradeProfitRequest  |     TradeProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/TradeProfit".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, TradeProfitRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, TradeProfitRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, TradeProfitRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TradeProfitResultApiResponse | None:
    if response.status_code == 200:
        response_200 = TradeProfitResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TradeProfitResultApiResponse]:
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
    body:    TradeProfitRequest  |     TradeProfitRequest  |     TradeProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[TradeProfitResultApiResponse]:
    """ Calculate the profit of a position

     <br>
                Calculates the profit a position with the given direction, volume and prices would
    bring,
                in the deposit currency of the group, together with the rate that converts the profit
                currency of the symbol into that currency. The calculation uses the current market
    prices
                of the group, so the symbol must be available to that group.

    <br>
                Nothing is created or changed: the result describes a hypothetical position only. The
                volume uses four decimal places of a lot; for the extended accuracy use the variant with
                the `Ext` suffix.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TradeProfitResultApiResponse]
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
    body:    TradeProfitRequest  |     TradeProfitRequest  |     TradeProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> TradeProfitResultApiResponse | None:
    """ Calculate the profit of a position

     <br>
                Calculates the profit a position with the given direction, volume and prices would
    bring,
                in the deposit currency of the group, together with the rate that converts the profit
                currency of the symbol into that currency. The calculation uses the current market
    prices
                of the group, so the symbol must be available to that group.

    <br>
                Nothing is created or changed: the result describes a hypothetical position only. The
                volume uses four decimal places of a lot; for the extended accuracy use the variant with
                the `Ext` suffix.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TradeProfitResultApiResponse
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
    body:    TradeProfitRequest  |     TradeProfitRequest  |     TradeProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[TradeProfitResultApiResponse]:
    """ Calculate the profit of a position

     <br>
                Calculates the profit a position with the given direction, volume and prices would
    bring,
                in the deposit currency of the group, together with the rate that converts the profit
                currency of the symbol into that currency. The calculation uses the current market
    prices
                of the group, so the symbol must be available to that group.

    <br>
                Nothing is created or changed: the result describes a hypothetical position only. The
                volume uses four decimal places of a lot; for the extended accuracy use the variant with
                the `Ext` suffix.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TradeProfitResultApiResponse]
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
    body:    TradeProfitRequest  |     TradeProfitRequest  |     TradeProfitRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> TradeProfitResultApiResponse | None:
    """ Calculate the profit of a position

     <br>
                Calculates the profit a position with the given direction, volume and prices would
    bring,
                in the deposit currency of the group, together with the rate that converts the profit
                currency of the symbol into that currency. The calculation uses the current market
    prices
                of the group, so the symbol must be available to that group.

    <br>
                Nothing is created or changed: the result describes a hypothetical position only. The
                volume uses four decimal places of a lot; for the extended accuracy use the variant with
                the `Ext` suffix.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.
        body (TradeProfitRequest | Unset): Conditions of a profit calculation, v2 request DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TradeProfitResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
