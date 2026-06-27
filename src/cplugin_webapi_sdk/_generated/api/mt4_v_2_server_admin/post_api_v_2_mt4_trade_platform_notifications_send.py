from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_notifications_send_request import MT4NotificationsSendRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/NotificationsSend".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4NotificationsSendRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4NotificationsSendRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4NotificationsSendRequest):
        
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
    body:    MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ 
    Args:
        trade_platform (UUID):
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.

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
    body:    MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ 
    Args:
        trade_platform (UUID):
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.

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
    body:    MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ 
    Args:
        trade_platform (UUID):
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.

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
    body:    MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  |     MT4NotificationsSendRequest  | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ 
    Args:
        trade_platform (UUID):
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.
        body (MT4NotificationsSendRequest | Unset): Request body for the v2 `NotificationsSend`
            admin endpoint —
            pushes a single message to one or more MT4 clients identified by
            account login. Maps onto the wrapper's
            `NotificationsSend2(int[] logins, string message)`.

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
