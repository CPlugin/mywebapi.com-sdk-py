from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_subscription_action_result_api_response import MT5SubscriptionActionResultApiResponse
from ...models.mt5_subscription_target import MT5SubscriptionTarget
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5SubscriptionTarget  |     MT5SubscriptionTarget  |     MT5SubscriptionTarget  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/SubscriptionCancel".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5SubscriptionTarget):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5SubscriptionTarget):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5SubscriptionTarget):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5SubscriptionActionResultApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5SubscriptionActionResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5SubscriptionActionResultApiResponse]:
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
    body:    MT5SubscriptionTarget  |     MT5SubscriptionTarget  |     MT5SubscriptionTarget  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SubscriptionActionResultApiResponse]:
    """ Cancel a subscription of an account

     <br>
                Cancels the subscription of the account the way the client terminal does: the management
                mode of the configuration is honoured, and when unsubscribing is paid the money is
                handled according to the configuration. The cancellation is written as an action and the
                subscription record is removed.

    <br>
                The response carries the cancelled subscription record and the action record with the
                payment, if there was one. The operation is not idempotent: a repeated request for an
                already cancelled subscription fails with the platform error.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SubscriptionActionResultApiResponse]
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
    body:    MT5SubscriptionTarget  |     MT5SubscriptionTarget  |     MT5SubscriptionTarget  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SubscriptionActionResultApiResponse | None:
    """ Cancel a subscription of an account

     <br>
                Cancels the subscription of the account the way the client terminal does: the management
                mode of the configuration is honoured, and when unsubscribing is paid the money is
                handled according to the configuration. The cancellation is written as an action and the
                subscription record is removed.

    <br>
                The response carries the cancelled subscription record and the action record with the
                payment, if there was one. The operation is not idempotent: a repeated request for an
                already cancelled subscription fails with the platform error.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SubscriptionActionResultApiResponse
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
    body:    MT5SubscriptionTarget  |     MT5SubscriptionTarget  |     MT5SubscriptionTarget  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SubscriptionActionResultApiResponse]:
    """ Cancel a subscription of an account

     <br>
                Cancels the subscription of the account the way the client terminal does: the management
                mode of the configuration is honoured, and when unsubscribing is paid the money is
                handled according to the configuration. The cancellation is written as an action and the
                subscription record is removed.

    <br>
                The response carries the cancelled subscription record and the action record with the
                payment, if there was one. The operation is not idempotent: a repeated request for an
                already cancelled subscription fails with the platform error.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SubscriptionActionResultApiResponse]
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
    body:    MT5SubscriptionTarget  |     MT5SubscriptionTarget  |     MT5SubscriptionTarget  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SubscriptionActionResultApiResponse | None:
    """ Cancel a subscription of an account

     <br>
                Cancels the subscription of the account the way the client terminal does: the management
                mode of the configuration is honoured, and when unsubscribing is paid the money is
                handled according to the configuration. The cancellation is written as an action and the
                subscription record is removed.

    <br>
                The response carries the cancelled subscription record and the action record with the
                payment, if there was one. The operation is not idempotent: a repeated request for an
                already cancelled subscription fails with the platform error.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.
        body (MT5SubscriptionTarget | Unset): An account and a subscription configuration to act
            on.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SubscriptionActionResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
