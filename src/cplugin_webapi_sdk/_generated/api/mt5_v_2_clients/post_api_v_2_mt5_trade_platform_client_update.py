from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_client import MT5Client
from ...models.mt5_client_api_response import MT5ClientApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5Client  |     MT5Client  |     MT5Client  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/ClientUpdate".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5Client):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5Client):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5Client):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5ClientApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5ClientApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5ClientApiResponse]:
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
    body:    MT5Client  |     MT5Client  |     MT5Client  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ClientApiResponse]:
    """ Update a client

     Writes the changed client record back to the server database. Send the whole record, not only
    the fields that changed: a field left out is written as empty, so read the client first, change
    what is needed and send the result. The person name must be filled in, otherwise the record is
    refused. A client can only be changed from the server that created it; a record that does not
    exist is answered with a platform error. The response carries the record as stored by the server.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Client | Unset): Client record interface
        body (MT5Client | Unset): Client record interface
        body (MT5Client | Unset): Client record interface

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ClientApiResponse]
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
    body:    MT5Client  |     MT5Client  |     MT5Client  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ClientApiResponse | None:
    """ Update a client

     Writes the changed client record back to the server database. Send the whole record, not only
    the fields that changed: a field left out is written as empty, so read the client first, change
    what is needed and send the result. The person name must be filled in, otherwise the record is
    refused. A client can only be changed from the server that created it; a record that does not
    exist is answered with a platform error. The response carries the record as stored by the server.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Client | Unset): Client record interface
        body (MT5Client | Unset): Client record interface
        body (MT5Client | Unset): Client record interface

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ClientApiResponse
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
    body:    MT5Client  |     MT5Client  |     MT5Client  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ClientApiResponse]:
    """ Update a client

     Writes the changed client record back to the server database. Send the whole record, not only
    the fields that changed: a field left out is written as empty, so read the client first, change
    what is needed and send the result. The person name must be filled in, otherwise the record is
    refused. A client can only be changed from the server that created it; a record that does not
    exist is answered with a platform error. The response carries the record as stored by the server.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Client | Unset): Client record interface
        body (MT5Client | Unset): Client record interface
        body (MT5Client | Unset): Client record interface

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ClientApiResponse]
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
    body:    MT5Client  |     MT5Client  |     MT5Client  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ClientApiResponse | None:
    """ Update a client

     Writes the changed client record back to the server database. Send the whole record, not only
    the fields that changed: a field left out is written as empty, so read the client first, change
    what is needed and send the result. The person name must be filled in, otherwise the record is
    refused. A client can only be changed from the server that created it; a record that does not
    exist is answered with a platform error. The response carries the record as stored by the server.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Client | Unset): Client record interface
        body (MT5Client | Unset): Client record interface
        body (MT5Client | Unset): Client record interface

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ClientApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
