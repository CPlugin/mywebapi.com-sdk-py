from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_subscription_batch_result_api_response import MT5SubscriptionBatchResultApiResponse
from ...models.mt5_subscription_target import MT5SubscriptionTarget
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/SubscriptionCancelBatch".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, list[MT5SubscriptionTarget]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, list[MT5SubscriptionTarget]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/json"
    if isinstance(body, list[MT5SubscriptionTarget]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5SubscriptionBatchResultApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5SubscriptionBatchResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5SubscriptionBatchResultApiResponse]:
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
    body:    list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SubscriptionBatchResultApiResponse]:
    """ Cancel subscriptions of several accounts

     <br>
                Cancels every subscription of the batch with the same checks and the same payment
                handling as the single-account operation.

    <br>
                The response carries one result code per pair, in request order, together with the
                cancelled subscription records and their action records. `Ok` in the top-level
                envelope means every pair was cancelled, `ErrPartial` means only some were.
                The operation is not idempotent.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5SubscriptionTarget] | Unset):
        body (list[MT5SubscriptionTarget] | Unset):
        body (list[MT5SubscriptionTarget] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SubscriptionBatchResultApiResponse]
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
    body:    list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SubscriptionBatchResultApiResponse | None:
    """ Cancel subscriptions of several accounts

     <br>
                Cancels every subscription of the batch with the same checks and the same payment
                handling as the single-account operation.

    <br>
                The response carries one result code per pair, in request order, together with the
                cancelled subscription records and their action records. `Ok` in the top-level
                envelope means every pair was cancelled, `ErrPartial` means only some were.
                The operation is not idempotent.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5SubscriptionTarget] | Unset):
        body (list[MT5SubscriptionTarget] | Unset):
        body (list[MT5SubscriptionTarget] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SubscriptionBatchResultApiResponse
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
    body:    list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SubscriptionBatchResultApiResponse]:
    """ Cancel subscriptions of several accounts

     <br>
                Cancels every subscription of the batch with the same checks and the same payment
                handling as the single-account operation.

    <br>
                The response carries one result code per pair, in request order, together with the
                cancelled subscription records and their action records. `Ok` in the top-level
                envelope means every pair was cancelled, `ErrPartial` means only some were.
                The operation is not idempotent.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5SubscriptionTarget] | Unset):
        body (list[MT5SubscriptionTarget] | Unset):
        body (list[MT5SubscriptionTarget] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SubscriptionBatchResultApiResponse]
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
    body:    list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  |     list[MT5SubscriptionTarget]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SubscriptionBatchResultApiResponse | None:
    """ Cancel subscriptions of several accounts

     <br>
                Cancels every subscription of the batch with the same checks and the same payment
                handling as the single-account operation.

    <br>
                The response carries one result code per pair, in request order, together with the
                cancelled subscription records and their action records. `Ok` in the top-level
                envelope means every pair was cancelled, `ErrPartial` means only some were.
                The operation is not idempotent.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5SubscriptionTarget] | Unset):
        body (list[MT5SubscriptionTarget] | Unset):
        body (list[MT5SubscriptionTarget] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SubscriptionBatchResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
