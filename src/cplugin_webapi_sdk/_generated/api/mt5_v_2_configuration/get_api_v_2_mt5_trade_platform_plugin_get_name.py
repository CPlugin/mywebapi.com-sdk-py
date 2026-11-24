from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_plugin_api_response import MT5PluginApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    name: str,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/PluginGet/{name}".format(trade_platform=quote(str(trade_platform), safe=""),name=quote(str(name), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5PluginApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5PluginApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5PluginApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5PluginApiResponse]:
    """ Plugin configuration by name

     <br>
                Returns the plugin configuration with the given name: the module it belongs to, the
    trade server
                identifier, whether the platform keeps it loaded, its flags and every parameter. The
    name is the
                configuration name shown in the platform administration — it is the identity of the
    record, so a
                different spelling answers the platform's not-found error.

    <br>
                Parameters carry the module's own settings, and some modules keep credentials there —
    treat the
                whole answer as sensitive. Values are returned in their text form; the parameter type
    says how
                the module reads them.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        name (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5PluginApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
name=name,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT5PluginApiResponse | None:
    """ Plugin configuration by name

     <br>
                Returns the plugin configuration with the given name: the module it belongs to, the
    trade server
                identifier, whether the platform keeps it loaded, its flags and every parameter. The
    name is the
                configuration name shown in the platform administration — it is the identity of the
    record, so a
                different spelling answers the platform's not-found error.

    <br>
                Parameters carry the module's own settings, and some modules keep credentials there —
    treat the
                whole answer as sensitive. Values are returned in their text form; the parameter type
    says how
                the module reads them.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        name (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5PluginApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
name=name,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5PluginApiResponse]:
    """ Plugin configuration by name

     <br>
                Returns the plugin configuration with the given name: the module it belongs to, the
    trade server
                identifier, whether the platform keeps it loaded, its flags and every parameter. The
    name is the
                configuration name shown in the platform administration — it is the identity of the
    record, so a
                different spelling answers the platform's not-found error.

    <br>
                Parameters carry the module's own settings, and some modules keep credentials there —
    treat the
                whole answer as sensitive. Values are returned in their text form; the parameter type
    says how
                the module reads them.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        name (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5PluginApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
name=name,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT5PluginApiResponse | None:
    """ Plugin configuration by name

     <br>
                Returns the plugin configuration with the given name: the module it belongs to, the
    trade server
                identifier, whether the platform keeps it loaded, its flags and every parameter. The
    name is the
                configuration name shown in the platform administration — it is the identity of the
    record, so a
                different spelling answers the platform's not-found error.

    <br>
                Parameters carry the module's own settings, and some modules keep credentials there —
    treat the
                whole answer as sensitive. Values are returned in their text form; the parameter type
    says how
                the module reads them.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        name (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5PluginApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
name=name,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
