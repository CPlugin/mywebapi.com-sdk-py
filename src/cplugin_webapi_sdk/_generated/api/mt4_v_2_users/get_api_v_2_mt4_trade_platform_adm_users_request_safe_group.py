from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_user_list_api_response import MT4UserListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    group: str,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/AdmUsersRequestSafe/{group}".format(trade_platform=quote(str(trade_platform), safe=""),group=quote(str(group), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4UserListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4UserListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4UserListApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4UserListApiResponse]:
    r""" List group accounts (admin)

     All user accounts in a given group (admin scope) — the safe variant that honors permission checks
    server-side.

    Manager (live) call. Returns the curated `MT4User` projection
    for every account in the specified group. The platform's \"Safe\" suffix
    indicates it runs through `RunSafe` with the `Admin` rights
    guard — a manager lacking that permission receives a sensible error
    rather than a connection drop.

    Comma-separated group lists are accepted by the platform (it strips
    commas and trims whitespace internally); the simplest call pattern
    is a single group name. Large groups may return substantial
    payloads — pair with `Idempotency-Key` on retry.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT4UserListApiResponse | None:
    r""" List group accounts (admin)

     All user accounts in a given group (admin scope) — the safe variant that honors permission checks
    server-side.

    Manager (live) call. Returns the curated `MT4User` projection
    for every account in the specified group. The platform's \"Safe\" suffix
    indicates it runs through `RunSafe` with the `Admin` rights
    guard — a manager lacking that permission receives a sensible error
    rather than a connection drop.

    Comma-separated group lists are accepted by the platform (it strips
    commas and trims whitespace internally); the simplest call pattern
    is a single group name. Large groups may return substantial
    payloads — pair with `Idempotency-Key` on retry.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4UserListApiResponse]:
    r""" List group accounts (admin)

     All user accounts in a given group (admin scope) — the safe variant that honors permission checks
    server-side.

    Manager (live) call. Returns the curated `MT4User` projection
    for every account in the specified group. The platform's \"Safe\" suffix
    indicates it runs through `RunSafe` with the `Admin` rights
    guard — a manager lacking that permission receives a sensible error
    rather than a connection drop.

    Comma-separated group lists are accepted by the platform (it strips
    commas and trims whitespace internally); the simplest call pattern
    is a single group name. Large groups may return substantial
    payloads — pair with `Idempotency-Key` on retry.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT4UserListApiResponse | None:
    r""" List group accounts (admin)

     All user accounts in a given group (admin scope) — the safe variant that honors permission checks
    server-side.

    Manager (live) call. Returns the curated `MT4User` projection
    for every account in the specified group. The platform's \"Safe\" suffix
    indicates it runs through `RunSafe` with the `Admin` rights
    guard — a manager lacking that permission receives a sensible error
    rather than a connection drop.

    Comma-separated group lists are accepted by the platform (it strips
    commas and trims whitespace internally); the simplest call pattern
    is a single group name. Large groups may return substantial
    payloads — pair with `Idempotency-Key` on retry.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
