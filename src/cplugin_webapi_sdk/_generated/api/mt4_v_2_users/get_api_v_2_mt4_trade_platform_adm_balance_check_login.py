from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_balance_diff_api_response import MT4BalanceDiffApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    login: int,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/AdmBalanceCheck/{login}".format(trade_platform=quote(str(trade_platform), safe=""),login=quote(str(login), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4BalanceDiffApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4BalanceDiffApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4BalanceDiffApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4BalanceDiffApiResponse]:
    r""" Check account balance

     Admin balance integrity check for a single account.

    Manager (live) call. Returns the difference between the recorded
    account balance and what the MT4 server recomputes from closed
    orders + balance operations. `diff = 0` → balance is intact;
    non-zero → admin tooling can run `AdmBalanceFix` to recompute
    (forthcoming Wave 3 endpoint).

    Read-only operation despite the wrapper's \"Adm\" prefix (the prefix
    signals the elevated authorization requirement, not a write side
    effect).

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BalanceDiffApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT4BalanceDiffApiResponse | None:
    r""" Check account balance

     Admin balance integrity check for a single account.

    Manager (live) call. Returns the difference between the recorded
    account balance and what the MT4 server recomputes from closed
    orders + balance operations. `diff = 0` → balance is intact;
    non-zero → admin tooling can run `AdmBalanceFix` to recompute
    (forthcoming Wave 3 endpoint).

    Read-only operation despite the wrapper's \"Adm\" prefix (the prefix
    signals the elevated authorization requirement, not a write side
    effect).

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BalanceDiffApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4BalanceDiffApiResponse]:
    r""" Check account balance

     Admin balance integrity check for a single account.

    Manager (live) call. Returns the difference between the recorded
    account balance and what the MT4 server recomputes from closed
    orders + balance operations. `diff = 0` → balance is intact;
    non-zero → admin tooling can run `AdmBalanceFix` to recompute
    (forthcoming Wave 3 endpoint).

    Read-only operation despite the wrapper's \"Adm\" prefix (the prefix
    signals the elevated authorization requirement, not a write side
    effect).

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BalanceDiffApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT4BalanceDiffApiResponse | None:
    r""" Check account balance

     Admin balance integrity check for a single account.

    Manager (live) call. Returns the difference between the recorded
    account balance and what the MT4 server recomputes from closed
    orders + balance operations. `diff = 0` → balance is intact;
    non-zero → admin tooling can run `AdmBalanceFix` to recompute
    (forthcoming Wave 3 endpoint).

    Read-only operation despite the wrapper's \"Adm\" prefix (the prefix
    signals the elevated authorization requirement, not a write side
    effect).

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BalanceDiffApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
