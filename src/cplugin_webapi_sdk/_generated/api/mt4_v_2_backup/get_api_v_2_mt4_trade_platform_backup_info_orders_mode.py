from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_backup_info_list_api_response import MT4BackupInfoListApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    mode: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/BackupInfoOrders/{mode}".format(trade_platform=quote(str(trade_platform), safe=""),mode=quote(str(mode), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4BackupInfoListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4BackupInfoListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4BackupInfoListApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    mode: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4BackupInfoListApiResponse]:
    """ List order backup files

     List backup order files available on the MT4 server for a given mode.

    Manager (live) call to the wrapper's
    `BackupInfoOrders(int mode)`. Order-side counterpart of
    `BackupInfoUsers` — same shape, different catalog.
    Read-only operation.

    Args:
        trade_platform (UUID):
        mode (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BackupInfoListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
mode=mode,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    mode: int,
    *,
    client: AuthenticatedClient | Client,

) -> MT4BackupInfoListApiResponse | None:
    """ List order backup files

     List backup order files available on the MT4 server for a given mode.

    Manager (live) call to the wrapper's
    `BackupInfoOrders(int mode)`. Order-side counterpart of
    `BackupInfoUsers` — same shape, different catalog.
    Read-only operation.

    Args:
        trade_platform (UUID):
        mode (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BackupInfoListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
mode=mode,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    mode: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4BackupInfoListApiResponse]:
    """ List order backup files

     List backup order files available on the MT4 server for a given mode.

    Manager (live) call to the wrapper's
    `BackupInfoOrders(int mode)`. Order-side counterpart of
    `BackupInfoUsers` — same shape, different catalog.
    Read-only operation.

    Args:
        trade_platform (UUID):
        mode (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BackupInfoListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
mode=mode,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    mode: int,
    *,
    client: AuthenticatedClient | Client,

) -> MT4BackupInfoListApiResponse | None:
    """ List order backup files

     List backup order files available on the MT4 server for a given mode.

    Manager (live) call to the wrapper's
    `BackupInfoOrders(int mode)`. Order-side counterpart of
    `BackupInfoUsers` — same shape, different catalog.
    Read-only operation.

    Args:
        trade_platform (UUID):
        mode (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BackupInfoListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
mode=mode,
client=client,

    )).parsed
