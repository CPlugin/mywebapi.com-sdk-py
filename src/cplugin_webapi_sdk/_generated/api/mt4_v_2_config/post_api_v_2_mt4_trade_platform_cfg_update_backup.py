from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_backup import MT4Backup
from ...models.mt4_backup_api_response import MT4BackupApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4Backup  |     MT4Backup  |     MT4Backup  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateBackup".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4Backup):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4Backup):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4Backup):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
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
    body:    MT4Backup  |     MT4Backup  |     MT4Backup  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4BackupApiResponse]:
    r""" Update backup config

     Update server backup configuration — Type 1 mutator.

    Manager (live) call. Reads the current `ConBackup`, overlays
    the fields in `MT4Backup` onto it, and writes back via
    `CfgUpdateBackup`. Two classes of preserved fields:
    <list type=\"bullet\"><item><b>Slave-server credential</b> — `WatchPassword` stays
            whatever the wrapper read live. It is unreachable from the
            v2 request body (DTO does not expose it).</item><item><b>Last-completion timestamps</b> —
    `FullBackupLastTime`,
            `ArchiveLastTime`, `ExportLastTime`, `WatchTimestamp`.
            Server-derived runtime state that clients must not overwrite.</item></list>
    Echoes the merged `MT4Backup` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BackupApiResponse]
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
    body:    MT4Backup  |     MT4Backup  |     MT4Backup  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4BackupApiResponse | None:
    r""" Update backup config

     Update server backup configuration — Type 1 mutator.

    Manager (live) call. Reads the current `ConBackup`, overlays
    the fields in `MT4Backup` onto it, and writes back via
    `CfgUpdateBackup`. Two classes of preserved fields:
    <list type=\"bullet\"><item><b>Slave-server credential</b> — `WatchPassword` stays
            whatever the wrapper read live. It is unreachable from the
            v2 request body (DTO does not expose it).</item><item><b>Last-completion timestamps</b> —
    `FullBackupLastTime`,
            `ArchiveLastTime`, `ExportLastTime`, `WatchTimestamp`.
            Server-derived runtime state that clients must not overwrite.</item></list>
    Echoes the merged `MT4Backup` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BackupApiResponse
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
    body:    MT4Backup  |     MT4Backup  |     MT4Backup  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4BackupApiResponse]:
    r""" Update backup config

     Update server backup configuration — Type 1 mutator.

    Manager (live) call. Reads the current `ConBackup`, overlays
    the fields in `MT4Backup` onto it, and writes back via
    `CfgUpdateBackup`. Two classes of preserved fields:
    <list type=\"bullet\"><item><b>Slave-server credential</b> — `WatchPassword` stays
            whatever the wrapper read live. It is unreachable from the
            v2 request body (DTO does not expose it).</item><item><b>Last-completion timestamps</b> —
    `FullBackupLastTime`,
            `ArchiveLastTime`, `ExportLastTime`, `WatchTimestamp`.
            Server-derived runtime state that clients must not overwrite.</item></list>
    Echoes the merged `MT4Backup` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4BackupApiResponse]
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
    body:    MT4Backup  |     MT4Backup  |     MT4Backup  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4BackupApiResponse | None:
    r""" Update backup config

     Update server backup configuration — Type 1 mutator.

    Manager (live) call. Reads the current `ConBackup`, overlays
    the fields in `MT4Backup` onto it, and writes back via
    `CfgUpdateBackup`. Two classes of preserved fields:
    <list type=\"bullet\"><item><b>Slave-server credential</b> — `WatchPassword` stays
            whatever the wrapper read live. It is unreachable from the
            v2 request body (DTO does not expose it).</item><item><b>Last-completion timestamps</b> —
    `FullBackupLastTime`,
            `ArchiveLastTime`, `ExportLastTime`, `WatchTimestamp`.
            Server-derived runtime state that clients must not overwrite.</item></list>
    Echoes the merged `MT4Backup` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).
        body (MT4Backup | Unset): v2 DTO for the MT4 server's backup configuration (wrapper's
            ConBackup).
            Curated subset — drops the WatchPassword field (slave-server credential)
            for security. All other wrapper public fields are preserved, enums are
            surfaced as enum types (V2JsonContext serializes them as strings via
            UseStringEnumConverter=true).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4BackupApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
