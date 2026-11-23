from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.trade_margin_check_request import TradeMarginCheckRequest
from ...models.trade_margin_check_result_api_response import TradeMarginCheckResultApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    TradeMarginCheckRequest  |     TradeMarginCheckRequest  |     TradeMarginCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/TradeMarginCheck".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, TradeMarginCheckRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, TradeMarginCheckRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, TradeMarginCheckRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TradeMarginCheckResultApiResponse | None:
    if response.status_code == 200:
        response_200 = TradeMarginCheckResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[TradeMarginCheckResultApiResponse]:
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
    body:    TradeMarginCheckRequest  |     TradeMarginCheckRequest  |     TradeMarginCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[TradeMarginCheckResultApiResponse]:
    """ Check whether an account has the margin an order requires

     <br>
                Checks whether the given account can place the described order, and returns the state of
                the account before and after it. The margin of the hypothetical order is estimated from
                the current state of the account and the current prices of its group, so the after state
                is approximate.

    <br>
                Nothing is created or changed. An account without enough free margin is a normal answer
                (`allowed` is `false`) and not an error. The volume uses four decimal places of
                a lot; for the extended accuracy use the variant with the `Ext` suffix.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TradeMarginCheckResultApiResponse]
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
    body:    TradeMarginCheckRequest  |     TradeMarginCheckRequest  |     TradeMarginCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> TradeMarginCheckResultApiResponse | None:
    """ Check whether an account has the margin an order requires

     <br>
                Checks whether the given account can place the described order, and returns the state of
                the account before and after it. The margin of the hypothetical order is estimated from
                the current state of the account and the current prices of its group, so the after state
                is approximate.

    <br>
                Nothing is created or changed. An account without enough free margin is a normal answer
                (`allowed` is `false`) and not an error. The volume uses four decimal places of
                a lot; for the extended accuracy use the variant with the `Ext` suffix.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TradeMarginCheckResultApiResponse
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
    body:    TradeMarginCheckRequest  |     TradeMarginCheckRequest  |     TradeMarginCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[TradeMarginCheckResultApiResponse]:
    """ Check whether an account has the margin an order requires

     <br>
                Checks whether the given account can place the described order, and returns the state of
                the account before and after it. The margin of the hypothetical order is estimated from
                the current state of the account and the current prices of its group, so the after state
                is approximate.

    <br>
                Nothing is created or changed. An account without enough free margin is a normal answer
                (`allowed` is `false`) and not an error. The volume uses four decimal places of
                a lot; for the extended accuracy use the variant with the `Ext` suffix.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TradeMarginCheckResultApiResponse]
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
    body:    TradeMarginCheckRequest  |     TradeMarginCheckRequest  |     TradeMarginCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> TradeMarginCheckResultApiResponse | None:
    """ Check whether an account has the margin an order requires

     <br>
                Checks whether the given account can place the described order, and returns the state of
                the account before and after it. The margin of the hypothetical order is estimated from
                the current state of the account and the current prices of its group, so the after state
                is approximate.

    <br>
                Nothing is created or changed. An account without enough free margin is a normal answer
                (`allowed` is `false`) and not an error. The volume uses four decimal places of
                a lot; for the extended accuracy use the variant with the `Ext` suffix.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.
        body (TradeMarginCheckRequest | Unset): Order whose margin requirement is checked, v2
            request DTO.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TradeMarginCheckResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
