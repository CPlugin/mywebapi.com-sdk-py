from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt5_subscription import MT5Subscription
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5Subscription  |     MT5Subscription  |     MT5Subscription  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/SubscriptionUpdate".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5Subscription):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5Subscription):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5Subscription):
        
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
    body:    MT5Subscription  |     MT5Subscription  |     MT5Subscription  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Update a subscription record

     <br>
                Changes a subscription record that already exists on the trade server. The record is
                addressed by `id`, which is mandatory: the subscription link itself is created and
                removed by the subscribe and cancel operations, never by this one.

    <br>
                Only the fields present in the body are written; a field left out keeps the value
                currently stored. The whole record must still satisfy the rules of the subscription
                configuration, so the usual order is: read the record, change the fields needed, send
                the result back.

    <br>
                The change is written straight to the subscription database and is not checked against
                the management mode of the configuration — the operation is meant for administrative
                corrections. The record can only be changed on the trade server that owns it; a request
                that reaches another server is refused with the platform error `MT_RET_ERR_NOTMAIN`.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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
    body:    MT5Subscription  |     MT5Subscription  |     MT5Subscription  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Update a subscription record

     <br>
                Changes a subscription record that already exists on the trade server. The record is
                addressed by `id`, which is mandatory: the subscription link itself is created and
                removed by the subscribe and cancel operations, never by this one.

    <br>
                Only the fields present in the body are written; a field left out keeps the value
                currently stored. The whole record must still satisfy the rules of the subscription
                configuration, so the usual order is: read the record, change the fields needed, send
                the result back.

    <br>
                The change is written straight to the subscription database and is not checked against
                the management mode of the configuration — the operation is meant for administrative
                corrections. The record can only be changed on the trade server that owns it; a request
                that reaches another server is refused with the platform error `MT_RET_ERR_NOTMAIN`.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.

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
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT5Subscription  |     MT5Subscription  |     MT5Subscription  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Update a subscription record

     <br>
                Changes a subscription record that already exists on the trade server. The record is
                addressed by `id`, which is mandatory: the subscription link itself is created and
                removed by the subscribe and cancel operations, never by this one.

    <br>
                Only the fields present in the body are written; a field left out keeps the value
                currently stored. The whole record must still satisfy the rules of the subscription
                configuration, so the usual order is: read the record, change the fields needed, send
                the result back.

    <br>
                The change is written straight to the subscription database and is not checked against
                the management mode of the configuration — the operation is meant for administrative
                corrections. The record can only be changed on the trade server that owns it; a request
                that reaches another server is refused with the platform error `MT_RET_ERR_NOTMAIN`.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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
    body:    MT5Subscription  |     MT5Subscription  |     MT5Subscription  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Update a subscription record

     <br>
                Changes a subscription record that already exists on the trade server. The record is
                addressed by `id`, which is mandatory: the subscription link itself is created and
                removed by the subscribe and cancel operations, never by this one.

    <br>
                Only the fields present in the body are written; a field left out keeps the value
                currently stored. The whole record must still satisfy the rules of the subscription
                configuration, so the usual order is: read the record, change the fields needed, send
                the result back.

    <br>
                The change is written straight to the subscription database and is not checked against
                the management mode of the configuration — the operation is meant for administrative
                corrections. The record can only be changed on the trade server that owns it; a request
                that reaches another server is refused with the platform error `MT_RET_ERR_NOTMAIN`.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.
        body (MT5Subscription | Unset): A subscription of a trading account, as stored by the
            trade server.

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
x_request_timeout=x_request_timeout,

    )).parsed
