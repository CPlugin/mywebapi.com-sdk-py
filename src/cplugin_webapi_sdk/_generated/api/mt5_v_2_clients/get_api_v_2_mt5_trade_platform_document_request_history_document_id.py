from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_document_list_api_response import MT5DocumentListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    document_id: int,
    *,
    author: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["author"] = author

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/DocumentRequestHistory/{document_id}".format(trade_platform=quote(str(trade_platform), safe=""),document_id=quote(str(document_id), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5DocumentListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5DocumentListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5DocumentListApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    document_id: int,
    *,
    client: AuthenticatedClient | Client,
    author: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5DocumentListApiResponse]:
    """ History of a document

     Returns the versions of the document for the requested time window — the record as it was after
    every change. Both bounds are optional: without them the whole history is read. When an author is
    given, only the changes made by that manager account are returned. Reading changes nothing.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        document_id (int):
        author (int | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5DocumentListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
document_id=document_id,
author=author,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    document_id: int,
    *,
    client: AuthenticatedClient | Client,
    author: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5DocumentListApiResponse | None:
    """ History of a document

     Returns the versions of the document for the requested time window — the record as it was after
    every change. Both bounds are optional: without them the whole history is read. When an author is
    given, only the changes made by that manager account are returned. Reading changes nothing.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        document_id (int):
        author (int | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5DocumentListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
document_id=document_id,
client=client,
author=author,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    document_id: int,
    *,
    client: AuthenticatedClient | Client,
    author: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5DocumentListApiResponse]:
    """ History of a document

     Returns the versions of the document for the requested time window — the record as it was after
    every change. Both bounds are optional: without them the whole history is read. When an author is
    given, only the changes made by that manager account are returned. Reading changes nothing.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        document_id (int):
        author (int | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5DocumentListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
document_id=document_id,
author=author,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    document_id: int,
    *,
    client: AuthenticatedClient | Client,
    author: int | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5DocumentListApiResponse | None:
    """ History of a document

     Returns the versions of the document for the requested time window — the record as it was after
    every change. Both bounds are optional: without them the whole history is read. When an author is
    given, only the changes made by that manager account are returned. Reading changes nothing.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        document_id (int):
        author (int | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5DocumentListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
document_id=document_id,
client=client,
author=author,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )).parsed
