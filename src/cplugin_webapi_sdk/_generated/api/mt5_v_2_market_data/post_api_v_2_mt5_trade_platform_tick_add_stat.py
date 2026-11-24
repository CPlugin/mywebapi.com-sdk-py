from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt5_market_tick_add_stat_request import MT5MarketTickAddStatRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/TickAddStat".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5MarketTickAddStatRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5MarketTickAddStatRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5MarketTickAddStatRequest):
        
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
    *,
    client: AuthenticatedClient | Client,
    body:    MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Publish statistical information about the price

     <br>
                Publishes session statistics for the symbol of the given quote: the extremes of the bid,
                the ask and the last deal price, the extremes of the deal volume and the session totals.
                The figures replace the ones the trade server currently holds for the symbol, so send
    the
                complete set — a field left out is published as zero.

    <br>
                The call changes the figures terminals and subscribers display and is not reversible:
    the
                previous statistics are not kept anywhere and cannot be restored through the API.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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
    body:    MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Publish statistical information about the price

     <br>
                Publishes session statistics for the symbol of the given quote: the extremes of the bid,
                the ask and the last deal price, the extremes of the deal volume and the session totals.
                The figures replace the ones the trade server currently holds for the symbol, so send
    the
                complete set — a field left out is published as zero.

    <br>
                The call changes the figures terminals and subscribers display and is not reversible:
    the
                previous statistics are not kept anywhere and cannot be restored through the API.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
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
    body:    MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Publish statistical information about the price

     <br>
                Publishes session statistics for the symbol of the given quote: the extremes of the bid,
                the ask and the last deal price, the extremes of the deal volume and the session totals.
                The figures replace the ones the trade server currently holds for the symbol, so send
    the
                complete set — a field left out is published as zero.

    <br>
                The call changes the figures terminals and subscribers display and is not reversible:
    the
                previous statistics are not kept anywhere and cannot be restored through the API.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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
    body:    MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  |     MT5MarketTickAddStatRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Publish statistical information about the price

     <br>
                Publishes session statistics for the symbol of the given quote: the extremes of the bid,
                the ask and the last deal price, the extremes of the deal volume and the session totals.
                The figures replace the ones the trade server currently holds for the symbol, so send
    the
                complete set — a field left out is published as zero.

    <br>
                The call changes the figures terminals and subscribers display and is not reversible:
    the
                previous statistics are not kept anywhere and cannot be restored through the API.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.
        body (MT5MarketTickAddStatRequest | Unset): A quote together with the statistical
            information to publish with it.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
