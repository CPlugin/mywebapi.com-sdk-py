from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_notifications_send_request import MT5NotificationsSendRequest
from ...models.mt5_result_api_response import MT5ResultApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/NotificationsSend".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5NotificationsSendRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5NotificationsSendRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5NotificationsSendRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5ResultApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5ResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5ResultApiResponse]:
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
    body:    MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultApiResponse]:
    """ Send a push notification to mobile terminals

     <br>
                Delivers a short message to the mobile terminals of the named accounts, either by their
                logins on the trade server or by the MetaQuotes identifiers their terminals are
    registered
                with. Exactly one of the two addressing lists must be sent.

    <br>
                Success means the notification was accepted for delivery, not that it reached a
    terminal;
                delivery needs the mobile terminal of the platform to be installed and registered. The
                message is limited by the platform to 1024 characters and is not stored or logged by the
                service.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultApiResponse]
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
    body:    MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultApiResponse | None:
    """ Send a push notification to mobile terminals

     <br>
                Delivers a short message to the mobile terminals of the named accounts, either by their
                logins on the trade server or by the MetaQuotes identifiers their terminals are
    registered
                with. Exactly one of the two addressing lists must be sent.

    <br>
                Success means the notification was accepted for delivery, not that it reached a
    terminal;
                delivery needs the mobile terminal of the platform to be installed and registered. The
                message is limited by the platform to 1024 characters and is not stored or logged by the
                service.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultApiResponse
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
    body:    MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultApiResponse]:
    """ Send a push notification to mobile terminals

     <br>
                Delivers a short message to the mobile terminals of the named accounts, either by their
                logins on the trade server or by the MetaQuotes identifiers their terminals are
    registered
                with. Exactly one of the two addressing lists must be sent.

    <br>
                Success means the notification was accepted for delivery, not that it reached a
    terminal;
                delivery needs the mobile terminal of the platform to be installed and registered. The
                message is limited by the platform to 1024 characters and is not stored or logged by the
                service.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultApiResponse]
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
    body:    MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  |     MT5NotificationsSendRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultApiResponse | None:
    """ Send a push notification to mobile terminals

     <br>
                Delivers a short message to the mobile terminals of the named accounts, either by their
                logins on the trade server or by the MetaQuotes identifiers their terminals are
    registered
                with. Exactly one of the two addressing lists must be sent.

    <br>
                Success means the notification was accepted for delivery, not that it reached a
    terminal;
                delivery needs the mobile terminal of the platform to be installed and registered. The
                message is limited by the platform to 1024 characters and is not stored or logged by the
                service.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.
        body (MT5NotificationsSendRequest | Unset): A push notification to send to the mobile
            terminals of a set of accounts.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
