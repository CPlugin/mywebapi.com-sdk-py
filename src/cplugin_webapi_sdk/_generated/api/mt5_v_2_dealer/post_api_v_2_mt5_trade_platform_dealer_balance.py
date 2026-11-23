from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.dealer_balance_request import DealerBalanceRequest
from ...models.u_int_64_api_response import UInt64ApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    DealerBalanceRequest  |     DealerBalanceRequest  |     DealerBalanceRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/DealerBalance".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, DealerBalanceRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, DealerBalanceRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, DealerBalanceRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> UInt64ApiResponse | None:
    if response.status_code == 200:
        response_200 = UInt64ApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[UInt64ApiResponse]:
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
    body:    DealerBalanceRequest  |     DealerBalanceRequest  |     DealerBalanceRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[UInt64ApiResponse]:
    """ Send a balance operation on behalf of the dealer

     <br>
                Credits or debits the balance of the account with the given login, creating a balance
                deal on the server. When the request type is omitted the balance operation is used;
                buy and sell types make no sense here. The comment is stored with the deal.

    <br>
                The operation is validated by the server against the standard credit and margin rules.
                On success the response carries the identifier of the created deal; a rejection is
                returned as the platform error that explains it.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (DealerBalanceRequest | Unset):
        body (DealerBalanceRequest | Unset):
        body (DealerBalanceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UInt64ApiResponse]
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
    body:    DealerBalanceRequest  |     DealerBalanceRequest  |     DealerBalanceRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> UInt64ApiResponse | None:
    """ Send a balance operation on behalf of the dealer

     <br>
                Credits or debits the balance of the account with the given login, creating a balance
                deal on the server. When the request type is omitted the balance operation is used;
                buy and sell types make no sense here. The comment is stored with the deal.

    <br>
                The operation is validated by the server against the standard credit and margin rules.
                On success the response carries the identifier of the created deal; a rejection is
                returned as the platform error that explains it.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (DealerBalanceRequest | Unset):
        body (DealerBalanceRequest | Unset):
        body (DealerBalanceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UInt64ApiResponse
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
    body:    DealerBalanceRequest  |     DealerBalanceRequest  |     DealerBalanceRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[UInt64ApiResponse]:
    """ Send a balance operation on behalf of the dealer

     <br>
                Credits or debits the balance of the account with the given login, creating a balance
                deal on the server. When the request type is omitted the balance operation is used;
                buy and sell types make no sense here. The comment is stored with the deal.

    <br>
                The operation is validated by the server against the standard credit and margin rules.
                On success the response carries the identifier of the created deal; a rejection is
                returned as the platform error that explains it.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (DealerBalanceRequest | Unset):
        body (DealerBalanceRequest | Unset):
        body (DealerBalanceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UInt64ApiResponse]
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
    body:    DealerBalanceRequest  |     DealerBalanceRequest  |     DealerBalanceRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> UInt64ApiResponse | None:
    """ Send a balance operation on behalf of the dealer

     <br>
                Credits or debits the balance of the account with the given login, creating a balance
                deal on the server. When the request type is omitted the balance operation is used;
                buy and sell types make no sense here. The comment is stored with the deal.

    <br>
                The operation is validated by the server against the standard credit and margin rules.
                On success the response carries the identifier of the created deal; a rejection is
                returned as the platform error that explains it.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (DealerBalanceRequest | Unset):
        body (DealerBalanceRequest | Unset):
        body (DealerBalanceRequest | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UInt64ApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
