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
    *,
    limit: int | Unset = 100000,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/UsersSyncRead".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


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
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100000,

) -> Response[MT4UserListApiResponse]:
    """ Read user-records sync

     Read user records buffered by a prior `UsersSyncStart` call.

    Manager (live) call to the wrapper's `UsersSyncRead()`.
    Must be preceded by `POST UsersSyncStart` on the main x64
    API to seed the server-side snapshot. Same UnpackObject hazard
    as `UsersSnapshot` — sidecar-only.

    Args:
        trade_platform (UUID):
        limit (int | Unset):  Default: 100000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100000,

) -> MT4UserListApiResponse | None:
    """ Read user-records sync

     Read user records buffered by a prior `UsersSyncStart` call.

    Manager (live) call to the wrapper's `UsersSyncRead()`.
    Must be preceded by `POST UsersSyncStart` on the main x64
    API to seed the server-side snapshot. Same UnpackObject hazard
    as `UsersSnapshot` — sidecar-only.

    Args:
        trade_platform (UUID):
        limit (int | Unset):  Default: 100000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100000,

) -> Response[MT4UserListApiResponse]:
    """ Read user-records sync

     Read user records buffered by a prior `UsersSyncStart` call.

    Manager (live) call to the wrapper's `UsersSyncRead()`.
    Must be preceded by `POST UsersSyncStart` on the main x64
    API to seed the server-side snapshot. Same UnpackObject hazard
    as `UsersSnapshot` — sidecar-only.

    Args:
        trade_platform (UUID):
        limit (int | Unset):  Default: 100000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 100000,

) -> MT4UserListApiResponse | None:
    """ Read user-records sync

     Read user records buffered by a prior `UsersSyncStart` call.

    Manager (live) call to the wrapper's `UsersSyncRead()`.
    Must be preceded by `POST UsersSyncStart` on the main x64
    API to seed the server-side snapshot. Same UnpackObject hazard
    as `UsersSnapshot` — sidecar-only.

    Args:
        trade_platform (UUID):
        limit (int | Unset):  Default: 100000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,

    )).parsed
