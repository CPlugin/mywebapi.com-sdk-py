from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_logs_out_request import MT4LogsOutRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4LogsOutRequest  |     MT4LogsOutRequest  |     MT4LogsOutRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/LogsOut".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4LogsOutRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4LogsOutRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4LogsOutRequest):
        
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
    body:    MT4LogsOutRequest  |     MT4LogsOutRequest  |     MT4LogsOutRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Write a record to the Manager API log

     Files one entry in the trade server's Manager API log under the
    connection that serves this request: the result code, the source and
    the message supplied in the body.

    The call has no return value of its own — the platform reports
    success by returning at all — so the answer is a bare `true` once
    the entry is filed. Logging must be enabled on the connection (see
    `LogsMode`) for the entry to be kept.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.

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
    body:    MT4LogsOutRequest  |     MT4LogsOutRequest  |     MT4LogsOutRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Write a record to the Manager API log

     Files one entry in the trade server's Manager API log under the
    connection that serves this request: the result code, the source and
    the message supplied in the body.

    The call has no return value of its own — the platform reports
    success by returning at all — so the answer is a bare `true` once
    the entry is filed. Logging must be enabled on the connection (see
    `LogsMode`) for the entry to be kept.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.

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
    body:    MT4LogsOutRequest  |     MT4LogsOutRequest  |     MT4LogsOutRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Write a record to the Manager API log

     Files one entry in the trade server's Manager API log under the
    connection that serves this request: the result code, the source and
    the message supplied in the body.

    The call has no return value of its own — the platform reports
    success by returning at all — so the answer is a bare `true` once
    the entry is filed. Logging must be enabled on the connection (see
    `LogsMode`) for the entry to be kept.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.

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
    body:    MT4LogsOutRequest  |     MT4LogsOutRequest  |     MT4LogsOutRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Write a record to the Manager API log

     Files one entry in the trade server's Manager API log under the
    connection that serves this request: the result code, the source and
    the message supplied in the body.

    The call has no return value of its own — the platform reports
    success by returning at all — so the answer is a bare `true` once
    the entry is filed. Logging must be enabled on the connection (see
    `LogsMode`) for the entry to be kept.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.
        body (MT4LogsOutRequest | Unset): One record written to the trade server's Manager API
            log. The entry is
            filed under the connection that serves the request, with the result code
            and source text supplied by the caller.

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
