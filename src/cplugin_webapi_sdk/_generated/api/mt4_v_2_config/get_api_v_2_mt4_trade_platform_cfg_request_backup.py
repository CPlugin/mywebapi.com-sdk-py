from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_backup_api_response import MT4BackupApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/CfgRequestBackup".format(trade_platform=quote(str(trade_platform), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4BackupApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4BackupApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4BackupApiResponse]:
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

) -> Response[MT4BackupApiResponse]:
    """ Get backup config

     MT4 server backup configuration (full + archive + export schedules, watchdog HA pair settings).

    Manager-live read (round-trip). Returns the wrapper's ConBackup as
    MT4Backup DTO — full/archive/export schedule enums and paths, last
    completion timestamps, and HA-watchdog fields. The wrapper's
    `WatchPassword` (slave-server credential) is intentionally
    dropped from the v2 contract for security and is NOT present in
    the response payload.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BackupApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> MT4BackupApiResponse | None:
    """ Get backup config

     MT4 server backup configuration (full + archive + export schedules, watchdog HA pair settings).

    Manager-live read (round-trip). Returns the wrapper's ConBackup as
    MT4Backup DTO — full/archive/export schedule enums and paths, last
    completion timestamps, and HA-watchdog fields. The wrapper's
    `WatchPassword` (slave-server credential) is intentionally
    dropped from the v2 contract for security and is NOT present in
    the response payload.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BackupApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4BackupApiResponse]:
    """ Get backup config

     MT4 server backup configuration (full + archive + export schedules, watchdog HA pair settings).

    Manager-live read (round-trip). Returns the wrapper's ConBackup as
    MT4Backup DTO — full/archive/export schedule enums and paths, last
    completion timestamps, and HA-watchdog fields. The wrapper's
    `WatchPassword` (slave-server credential) is intentionally
    dropped from the v2 contract for security and is NOT present in
    the response payload.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BackupApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> MT4BackupApiResponse | None:
    """ Get backup config

     MT4 server backup configuration (full + archive + export schedules, watchdog HA pair settings).

    Manager-live read (round-trip). Returns the wrapper's ConBackup as
    MT4Backup DTO — full/archive/export schedule enums and paths, last
    completion timestamps, and HA-watchdog fields. The wrapper's
    `WatchPassword` (slave-server credential) is intentionally
    dropped from the v2 contract for security and is NOT present in
    the response payload.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BackupApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,

    )).parsed
