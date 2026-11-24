from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_logs_mode_request import MT4LogsModeRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4LogsModeRequest  |     MT4LogsModeRequest  |     MT4LogsModeRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/LogsMode".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4LogsModeRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4LogsModeRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4LogsModeRequest):
        
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
    body:    MT4LogsModeRequest  |     MT4LogsModeRequest  |     MT4LogsModeRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Set the logging mode of the Manager API connection

     Switches the Manager API log of the connection that serves this request
    on or off.

    The setting belongs to the connection, not to the trade server: it
    affects only the traffic of the connection pool that answered this
    call, it is not persisted, and it returns to the enabled default when
    that connection is re-established. Other connections of the same trade
    platform, and other trade platforms, are not affected.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.

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
    body:    MT4LogsModeRequest  |     MT4LogsModeRequest  |     MT4LogsModeRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Set the logging mode of the Manager API connection

     Switches the Manager API log of the connection that serves this request
    on or off.

    The setting belongs to the connection, not to the trade server: it
    affects only the traffic of the connection pool that answered this
    call, it is not persisted, and it returns to the enabled default when
    that connection is re-established. Other connections of the same trade
    platform, and other trade platforms, are not affected.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.

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
    body:    MT4LogsModeRequest  |     MT4LogsModeRequest  |     MT4LogsModeRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Set the logging mode of the Manager API connection

     Switches the Manager API log of the connection that serves this request
    on or off.

    The setting belongs to the connection, not to the trade server: it
    affects only the traffic of the connection pool that answered this
    call, it is not persisted, and it returns to the enabled default when
    that connection is re-established. Other connections of the same trade
    platform, and other trade platforms, are not affected.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.

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
    body:    MT4LogsModeRequest  |     MT4LogsModeRequest  |     MT4LogsModeRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Set the logging mode of the Manager API connection

     Switches the Manager API log of the connection that serves this request
    on or off.

    The setting belongs to the connection, not to the trade server: it
    affects only the traffic of the connection pool that answered this
    call, it is not persisted, and it returns to the enabled default when
    that connection is re-established. Other connections of the same trade
    platform, and other trade platforms, are not affected.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.
        body (MT4LogsModeRequest | Unset): Logging mode of the connection that serves the request.

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
