from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_batch_update_result_list_api_response import MT5BatchUpdateResultListApiResponse
from ...models.mt5_symbol_batch_update_item import MT5SymbolBatchUpdateItem
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/SymbolUpdateBatch".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, list[MT5SymbolBatchUpdateItem]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, list[MT5SymbolBatchUpdateItem]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/json"
    if isinstance(body, list[MT5SymbolBatchUpdateItem]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5BatchUpdateResultListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5BatchUpdateResultListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5BatchUpdateResultListApiResponse]:
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
    body:    list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5BatchUpdateResultListApiResponse]:
    """ Change several symbol configurations in one call

     <br>
                Each entry names a symbol and carries the fields to change; only the fields present in
    an
                entry are written, and a field left out keeps its current server value. Entries are read
    and
                prepared one by one and then sent to the trade server together; the answer lists the
    outcome
                of every entry in the order it was sent.

    <br>
                A symbol that cannot be read, or an entry that cannot be prepared, is reported with its
    own
                result code and does not block the others. When the platform refuses the whole batch,
    the
                error code of the call is returned instead of the list. Duplicate symbol names in one
    request
                are rejected. The call requires the right to change symbol settings and is accepted only
    by
                the main trade server.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5BatchUpdateResultListApiResponse]
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
    body:    list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5BatchUpdateResultListApiResponse | None:
    """ Change several symbol configurations in one call

     <br>
                Each entry names a symbol and carries the fields to change; only the fields present in
    an
                entry are written, and a field left out keeps its current server value. Entries are read
    and
                prepared one by one and then sent to the trade server together; the answer lists the
    outcome
                of every entry in the order it was sent.

    <br>
                A symbol that cannot be read, or an entry that cannot be prepared, is reported with its
    own
                result code and does not block the others. When the platform refuses the whole batch,
    the
                error code of the call is returned instead of the list. Duplicate symbol names in one
    request
                are rejected. The call requires the right to change symbol settings and is accepted only
    by
                the main trade server.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5BatchUpdateResultListApiResponse
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
    body:    list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5BatchUpdateResultListApiResponse]:
    """ Change several symbol configurations in one call

     <br>
                Each entry names a symbol and carries the fields to change; only the fields present in
    an
                entry are written, and a field left out keeps its current server value. Entries are read
    and
                prepared one by one and then sent to the trade server together; the answer lists the
    outcome
                of every entry in the order it was sent.

    <br>
                A symbol that cannot be read, or an entry that cannot be prepared, is reported with its
    own
                result code and does not block the others. When the platform refuses the whole batch,
    the
                error code of the call is returned instead of the list. Duplicate symbol names in one
    request
                are rejected. The call requires the right to change symbol settings and is accepted only
    by
                the main trade server.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5BatchUpdateResultListApiResponse]
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
    body:    list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  |     list[MT5SymbolBatchUpdateItem]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5BatchUpdateResultListApiResponse | None:
    """ Change several symbol configurations in one call

     <br>
                Each entry names a symbol and carries the fields to change; only the fields present in
    an
                entry are written, and a field left out keeps its current server value. Entries are read
    and
                prepared one by one and then sent to the trade server together; the answer lists the
    outcome
                of every entry in the order it was sent.

    <br>
                A symbol that cannot be read, or an entry that cannot be prepared, is reported with its
    own
                result code and does not block the others. When the platform refuses the whole batch,
    the
                error code of the call is returned instead of the list. Duplicate symbol names in one
    request
                are rejected. The call requires the right to change symbol settings and is accepted only
    by
                the main trade server.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):
        body (list[MT5SymbolBatchUpdateItem] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5BatchUpdateResultListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
