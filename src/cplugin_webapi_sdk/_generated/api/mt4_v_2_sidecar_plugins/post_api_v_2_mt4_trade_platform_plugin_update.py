from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_plugin_param import MT4PluginParam
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4PluginParam  |     MT4PluginParam  |     MT4PluginParam  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/PluginUpdate".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4PluginParam):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4PluginParam):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4PluginParam):
        
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
    body:    MT4PluginParam  |     MT4PluginParam  |     MT4PluginParam  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Update plugin parameter

     Apply a plugin parameter update via the pump-side wrapper. Requires admin rights.

    Manager-live call to the wrapper's `PluginUpdate(ConPluginParam cpp)`.
    Body is `MT4PluginParam` (the same shape `PluginParamGet` returns).

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.

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
    body:    MT4PluginParam  |     MT4PluginParam  |     MT4PluginParam  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Update plugin parameter

     Apply a plugin parameter update via the pump-side wrapper. Requires admin rights.

    Manager-live call to the wrapper's `PluginUpdate(ConPluginParam cpp)`.
    Body is `MT4PluginParam` (the same shape `PluginParamGet` returns).

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.

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
    body:    MT4PluginParam  |     MT4PluginParam  |     MT4PluginParam  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Update plugin parameter

     Apply a plugin parameter update via the pump-side wrapper. Requires admin rights.

    Manager-live call to the wrapper's `PluginUpdate(ConPluginParam cpp)`.
    Body is `MT4PluginParam` (the same shape `PluginParamGet` returns).

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.

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
    body:    MT4PluginParam  |     MT4PluginParam  |     MT4PluginParam  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Update plugin parameter

     Apply a plugin parameter update via the pump-side wrapper. Requires admin rights.

    Manager-live call to the wrapper's `PluginUpdate(ConPluginParam cpp)`.
    Body is `MT4PluginParam` (the same shape `PluginParamGet` returns).

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.
        body (MT4PluginParam | Unset): v2 DTO for an MT4 plugin together with its parameter set
            (sidecar-only).
            Mirrors wrapper's `ConPluginParam`.

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
