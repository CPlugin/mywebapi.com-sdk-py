from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_mail_send_request import MT4MailSendRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4MailSendRequest  |     MT4MailSendRequest  |     MT4MailSendRequest  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/MailSend".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4MailSendRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4MailSendRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4MailSendRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

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
    body:    MT4MailSendRequest  |     MT4MailSendRequest  |     MT4MailSendRequest  | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Send mail to accounts

     Send an email to one or more client logins. Requires 'Email' admin right.

    Manager (live) call to the wrapper's
    `MailSend(MailBox mail, ICollection<int> logins)`.
    The wrapper itself refuses to run on x64 (
    `throw new WrapperException(\"MailSend cannot be called in x64 environment\")`),
    so this endpoint exists only in the sidecar build.

    Args:
        trade_platform (UUID):
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4MailSendRequest  |     MT4MailSendRequest  |     MT4MailSendRequest  | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Send mail to accounts

     Send an email to one or more client logins. Requires 'Email' admin right.

    Manager (live) call to the wrapper's
    `MailSend(MailBox mail, ICollection<int> logins)`.
    The wrapper itself refuses to run on x64 (
    `throw new WrapperException(\"MailSend cannot be called in x64 environment\")`),
    so this endpoint exists only in the sidecar build.

    Args:
        trade_platform (UUID):
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.

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

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4MailSendRequest  |     MT4MailSendRequest  |     MT4MailSendRequest  | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Send mail to accounts

     Send an email to one or more client logins. Requires 'Email' admin right.

    Manager (live) call to the wrapper's
    `MailSend(MailBox mail, ICollection<int> logins)`.
    The wrapper itself refuses to run on x64 (
    `throw new WrapperException(\"MailSend cannot be called in x64 environment\")`),
    so this endpoint exists only in the sidecar build.

    Args:
        trade_platform (UUID):
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4MailSendRequest  |     MT4MailSendRequest  |     MT4MailSendRequest  | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Send mail to accounts

     Send an email to one or more client logins. Requires 'Email' admin right.

    Manager (live) call to the wrapper's
    `MailSend(MailBox mail, ICollection<int> logins)`.
    The wrapper itself refuses to run on x64 (
    `throw new WrapperException(\"MailSend cannot be called in x64 environment\")`),
    so this endpoint exists only in the sidecar build.

    Args:
        trade_platform (UUID):
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.
        body (MT4MailSendRequest | Unset): v2 request DTO for `POST MailSend` (sidecar-only).
            Sends an
            email to one or more client logins. Wrapper signature:
            `ResultCode MailSend(MailBox mail, ICollection<int> logins)`.

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

    )).parsed
