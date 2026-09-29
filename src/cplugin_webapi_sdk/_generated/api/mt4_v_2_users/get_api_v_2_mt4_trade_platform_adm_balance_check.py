from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_balance_diff_list_api_response import MT4BalanceDiffListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    logins: list[int] | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    json_logins: list[int] | Unset = UNSET
    if not isinstance(logins, Unset):
        json_logins = logins


    params["logins"] = json_logins


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/AdmBalanceCheck".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4BalanceDiffListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4BalanceDiffListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4BalanceDiffListApiResponse]:
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
    logins: list[int] | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4BalanceDiffListApiResponse]:
    r""" Check account balances (batch)

     Admin balance integrity check for a batch of accounts.

    Same semantics as the single-login variant but takes a list of logins
    via repeated query parameters: `?logins=1001&logins=1002`.
    One billed Manager request regardless of the array length. The response
    list contains entries only for accounts the server flagged with a
    non-zero diff — clean accounts are silently omitted. Clients should
    treat \"missing from response\" as \"diff = 0\".

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BalanceDiffListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
logins=logins,
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
    logins: list[int] | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4BalanceDiffListApiResponse | None:
    r""" Check account balances (batch)

     Admin balance integrity check for a batch of accounts.

    Same semantics as the single-login variant but takes a list of logins
    via repeated query parameters: `?logins=1001&logins=1002`.
    One billed Manager request regardless of the array length. The response
    list contains entries only for accounts the server flagged with a
    non-zero diff — clean accounts are silently omitted. Clients should
    treat \"missing from response\" as \"diff = 0\".

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BalanceDiffListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
logins=logins,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    logins: list[int] | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4BalanceDiffListApiResponse]:
    r""" Check account balances (batch)

     Admin balance integrity check for a batch of accounts.

    Same semantics as the single-login variant but takes a list of logins
    via repeated query parameters: `?logins=1001&logins=1002`.
    One billed Manager request regardless of the array length. The response
    list contains entries only for accounts the server flagged with a
    non-zero diff — clean accounts are silently omitted. Clients should
    treat \"missing from response\" as \"diff = 0\".

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BalanceDiffListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
logins=logins,
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
    logins: list[int] | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4BalanceDiffListApiResponse | None:
    r""" Check account balances (batch)

     Admin balance integrity check for a batch of accounts.

    Same semantics as the single-login variant but takes a list of logins
    via repeated query parameters: `?logins=1001&logins=1002`.
    One billed Manager request regardless of the array length. The response
    list contains entries only for accounts the server flagged with a
    non-zero diff — clean accounts are silently omitted. Clients should
    treat \"missing from response\" as \"diff = 0\".

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BalanceDiffListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
logins=logins,
x_request_timeout=x_request_timeout,

    )).parsed
