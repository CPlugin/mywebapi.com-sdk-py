from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_user_batch_result_list_api_response import MT5UserBatchResultListApiResponse
from ...models.mt5_user_delete_batch_request import MT5UserDeleteBatchRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/UserDeleteBatch".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5UserDeleteBatchRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5UserDeleteBatchRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5UserDeleteBatchRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5UserBatchResultListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5UserBatchResultListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5UserBatchResultListApiResponse]:
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
    body:    MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserBatchResultListApiResponse]:
    """ Remove several accounts

     <br>
                Removes every submitted account from the trade server database in one call. The
    operation
                is not reversible: the records are gone.

    <br>
                The per-account outcome is available only when every account was removed; a partly
                completed batch is answered with the platform error naming the partial failure, because
    the
                platform does not hand the individual results back to the caller in that case. Accounts
                that do not exist make the call fail as a whole.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserBatchResultListApiResponse]
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
    body:    MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserBatchResultListApiResponse | None:
    """ Remove several accounts

     <br>
                Removes every submitted account from the trade server database in one call. The
    operation
                is not reversible: the records are gone.

    <br>
                The per-account outcome is available only when every account was removed; a partly
                completed batch is answered with the platform error naming the partial failure, because
    the
                platform does not hand the individual results back to the caller in that case. Accounts
                that do not exist make the call fail as a whole.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserBatchResultListApiResponse
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
    body:    MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserBatchResultListApiResponse]:
    """ Remove several accounts

     <br>
                Removes every submitted account from the trade server database in one call. The
    operation
                is not reversible: the records are gone.

    <br>
                The per-account outcome is available only when every account was removed; a partly
                completed batch is answered with the platform error naming the partial failure, because
    the
                platform does not hand the individual results back to the caller in that case. Accounts
                that do not exist make the call fail as a whole.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserBatchResultListApiResponse]
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
    body:    MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  |     MT5UserDeleteBatchRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserBatchResultListApiResponse | None:
    """ Remove several accounts

     <br>
                Removes every submitted account from the trade server database in one call. The
    operation
                is not reversible: the records are gone.

    <br>
                The per-account outcome is available only when every account was removed; a partly
                completed batch is answered with the platform error naming the partial failure, because
    the
                platform does not hand the individual results back to the caller in that case. Accounts
                that do not exist make the call fail as a whole.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.
        body (MT5UserDeleteBatchRequest | Unset): Request to remove several trading accounts in
            one call.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserBatchResultListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
