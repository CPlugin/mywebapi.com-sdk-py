from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_user_restore_input import MT4UserRestoreInput
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  | Unset = UNSET,
    confirm: bool | Unset = False,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["confirm"] = confirm


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/BackupRestoreUsers".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }

    if isinstance(body, list[MT4UserRestoreInput]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, list[MT4UserRestoreInput]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/json"
    if isinstance(body, list[MT4UserRestoreInput]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



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
    body:    list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  | Unset = UNSET,
    confirm: bool | Unset = False,

) -> Response[BooleanApiResponse]:
    """ Restore users from backup

     Restore user records into the live MT4 database. Destructive — requires `?confirm=true`.

    Manager (live) call to the wrapper's
    `BackupRestoreUsers(UserRecord[] users)`. Each input
    `MT4UserRestoreInput` is mapped to a fresh `UserRecord`
    with the narrow restore field set — secrets, OTP, server-managed
    timestamps, and reserved blobs are NOT carried (see DTO docs).
    <br>
    Idempotency-Key header is <b>strongly recommended</b>: a network
    blip during a multi-user restore can leave the client uncertain
    whether the write happened. Without the key, retry will double-write.
    <br>
    Batch cap: 10000 records per call. Larger restores must be split.

    Args:
        trade_platform (UUID):
        confirm (bool | Unset):  Default: False.
        body (list[MT4UserRestoreInput] | Unset):
        body (list[MT4UserRestoreInput] | Unset):
        body (list[MT4UserRestoreInput] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
confirm=confirm,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  | Unset = UNSET,
    confirm: bool | Unset = False,

) -> BooleanApiResponse | None:
    """ Restore users from backup

     Restore user records into the live MT4 database. Destructive — requires `?confirm=true`.

    Manager (live) call to the wrapper's
    `BackupRestoreUsers(UserRecord[] users)`. Each input
    `MT4UserRestoreInput` is mapped to a fresh `UserRecord`
    with the narrow restore field set — secrets, OTP, server-managed
    timestamps, and reserved blobs are NOT carried (see DTO docs).
    <br>
    Idempotency-Key header is <b>strongly recommended</b>: a network
    blip during a multi-user restore can leave the client uncertain
    whether the write happened. Without the key, retry will double-write.
    <br>
    Batch cap: 10000 records per call. Larger restores must be split.

    Args:
        trade_platform (UUID):
        confirm (bool | Unset):  Default: False.
        body (list[MT4UserRestoreInput] | Unset):
        body (list[MT4UserRestoreInput] | Unset):
        body (list[MT4UserRestoreInput] | Unset):

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
confirm=confirm,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  | Unset = UNSET,
    confirm: bool | Unset = False,

) -> Response[BooleanApiResponse]:
    """ Restore users from backup

     Restore user records into the live MT4 database. Destructive — requires `?confirm=true`.

    Manager (live) call to the wrapper's
    `BackupRestoreUsers(UserRecord[] users)`. Each input
    `MT4UserRestoreInput` is mapped to a fresh `UserRecord`
    with the narrow restore field set — secrets, OTP, server-managed
    timestamps, and reserved blobs are NOT carried (see DTO docs).
    <br>
    Idempotency-Key header is <b>strongly recommended</b>: a network
    blip during a multi-user restore can leave the client uncertain
    whether the write happened. Without the key, retry will double-write.
    <br>
    Batch cap: 10000 records per call. Larger restores must be split.

    Args:
        trade_platform (UUID):
        confirm (bool | Unset):  Default: False.
        body (list[MT4UserRestoreInput] | Unset):
        body (list[MT4UserRestoreInput] | Unset):
        body (list[MT4UserRestoreInput] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
confirm=confirm,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  |     list[MT4UserRestoreInput]  | Unset = UNSET,
    confirm: bool | Unset = False,

) -> BooleanApiResponse | None:
    """ Restore users from backup

     Restore user records into the live MT4 database. Destructive — requires `?confirm=true`.

    Manager (live) call to the wrapper's
    `BackupRestoreUsers(UserRecord[] users)`. Each input
    `MT4UserRestoreInput` is mapped to a fresh `UserRecord`
    with the narrow restore field set — secrets, OTP, server-managed
    timestamps, and reserved blobs are NOT carried (see DTO docs).
    <br>
    Idempotency-Key header is <b>strongly recommended</b>: a network
    blip during a multi-user restore can leave the client uncertain
    whether the write happened. Without the key, retry will double-write.
    <br>
    Batch cap: 10000 records per call. Larger restores must be split.

    Args:
        trade_platform (UUID):
        confirm (bool | Unset):  Default: False.
        body (list[MT4UserRestoreInput] | Unset):
        body (list[MT4UserRestoreInput] | Unset):
        body (list[MT4UserRestoreInput] | Unset):

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
confirm=confirm,

    )).parsed
