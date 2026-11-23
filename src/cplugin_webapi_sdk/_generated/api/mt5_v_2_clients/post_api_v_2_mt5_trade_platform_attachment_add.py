from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_attachment import MT5Attachment
from ...models.mt5_attachment_api_response import MT5AttachmentApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5Attachment  |     MT5Attachment  |     MT5Attachment  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/AttachmentAdd".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5Attachment):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5Attachment):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5Attachment):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5AttachmentApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5AttachmentApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5AttachmentApiResponse]:
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
    body:    MT5Attachment  |     MT5Attachment  |     MT5Attachment  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5AttachmentApiResponse]:
    """ Store a file and link it to a document or a comment

     <br>
                Sends the file to the server, which stores it and assigns an identifier, and then links
    it to the
                document named by `documentID` or to the comment named by `commentID`. At most one of
    the
                two may be given; with neither, the file is stored on the client record without a link.
                The client must be identified, as the file belongs to it.

    <br>
                The file is stored before the link is written. When the link fails, the file stays on
    the server
                without an owner and cannot be removed through the API — check the document or comment
    identifier
                before sending large files.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5AttachmentApiResponse]
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
    body:    MT5Attachment  |     MT5Attachment  |     MT5Attachment  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5AttachmentApiResponse | None:
    """ Store a file and link it to a document or a comment

     <br>
                Sends the file to the server, which stores it and assigns an identifier, and then links
    it to the
                document named by `documentID` or to the comment named by `commentID`. At most one of
    the
                two may be given; with neither, the file is stored on the client record without a link.
                The client must be identified, as the file belongs to it.

    <br>
                The file is stored before the link is written. When the link fails, the file stays on
    the server
                without an owner and cannot be removed through the API — check the document or comment
    identifier
                before sending large files.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5AttachmentApiResponse
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
    body:    MT5Attachment  |     MT5Attachment  |     MT5Attachment  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5AttachmentApiResponse]:
    """ Store a file and link it to a document or a comment

     <br>
                Sends the file to the server, which stores it and assigns an identifier, and then links
    it to the
                document named by `documentID` or to the comment named by `commentID`. At most one of
    the
                two may be given; with neither, the file is stored on the client record without a link.
                The client must be identified, as the file belongs to it.

    <br>
                The file is stored before the link is written. When the link fails, the file stays on
    the server
                without an owner and cannot be removed through the API — check the document or comment
    identifier
                before sending large files.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5AttachmentApiResponse]
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
    body:    MT5Attachment  |     MT5Attachment  |     MT5Attachment  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5AttachmentApiResponse | None:
    """ Store a file and link it to a document or a comment

     <br>
                Sends the file to the server, which stores it and assigns an identifier, and then links
    it to the
                document named by `documentID` or to the comment named by `commentID`. At most one of
    the
                two may be given; with neither, the file is stored on the client record without a link.
                The client must be identified, as the file belongs to it.

    <br>
                The file is stored before the link is written. When the link fails, the file stays on
    the server
                without an owner and cannot be removed through the API — check the document or comment
    identifier
                before sending large files.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.
        body (MT5Attachment | Unset): File attached to a client, a document or a comment.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5AttachmentApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
