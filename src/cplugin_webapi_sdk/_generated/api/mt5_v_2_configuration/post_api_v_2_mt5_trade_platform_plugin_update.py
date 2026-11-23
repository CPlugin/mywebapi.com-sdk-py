from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_plugin import MT5Plugin
from ...models.mt5_plugin_api_response import MT5PluginApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5Plugin  |     MT5Plugin  |     MT5Plugin  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/PluginUpdate".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5Plugin):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5Plugin):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5Plugin):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

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
    *,
    client: AuthenticatedClient | Client,
    body:    MT5Plugin  |     MT5Plugin  |     MT5Plugin  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5PluginApiResponse]:
    """ Store a plugin configuration

     <br>
                Writes the plugin configuration described by the body to the trade server. The record is
                identified by its name: an existing configuration with that name is replaced, and one
    that does
                not exist yet is added — the platform checks the record before storing it and refuses an
                incomplete or inconsistent one with the platform's parameter error.

    <br>
                The body is the complete configuration: parameters that are not listed are not stored,
    so read
                the configuration first and send it back with the fields you change. Parameters carry
    the
                module's own settings, and some modules keep credentials there — the whole request is
    treated
                as sensitive.

    <br>
                The trade server accepts the write only when the module is marked as editable through
    the
                manager interface, when plugin settings are pumped on the connection, and when the
    account of
                the API has the right to change plugin configurations; otherwise the platform error
    saying so is
                returned.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5PluginApiResponse]
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
    body:    MT5Plugin  |     MT5Plugin  |     MT5Plugin  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5PluginApiResponse | None:
    """ Store a plugin configuration

     <br>
                Writes the plugin configuration described by the body to the trade server. The record is
                identified by its name: an existing configuration with that name is replaced, and one
    that does
                not exist yet is added — the platform checks the record before storing it and refuses an
                incomplete or inconsistent one with the platform's parameter error.

    <br>
                The body is the complete configuration: parameters that are not listed are not stored,
    so read
                the configuration first and send it back with the fields you change. Parameters carry
    the
                module's own settings, and some modules keep credentials there — the whole request is
    treated
                as sensitive.

    <br>
                The trade server accepts the write only when the module is marked as editable through
    the
                manager interface, when plugin settings are pumped on the connection, and when the
    account of
                the API has the right to change plugin configurations; otherwise the platform error
    saying so is
                returned.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5PluginApiResponse
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
    body:    MT5Plugin  |     MT5Plugin  |     MT5Plugin  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5PluginApiResponse]:
    """ Store a plugin configuration

     <br>
                Writes the plugin configuration described by the body to the trade server. The record is
                identified by its name: an existing configuration with that name is replaced, and one
    that does
                not exist yet is added — the platform checks the record before storing it and refuses an
                incomplete or inconsistent one with the platform's parameter error.

    <br>
                The body is the complete configuration: parameters that are not listed are not stored,
    so read
                the configuration first and send it back with the fields you change. Parameters carry
    the
                module's own settings, and some modules keep credentials there — the whole request is
    treated
                as sensitive.

    <br>
                The trade server accepts the write only when the module is marked as editable through
    the
                manager interface, when plugin settings are pumped on the connection, and when the
    account of
                the API has the right to change plugin configurations; otherwise the platform error
    saying so is
                returned.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5PluginApiResponse]
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
    body:    MT5Plugin  |     MT5Plugin  |     MT5Plugin  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5PluginApiResponse | None:
    """ Store a plugin configuration

     <br>
                Writes the plugin configuration described by the body to the trade server. The record is
                identified by its name: an existing configuration with that name is replaced, and one
    that does
                not exist yet is added — the platform checks the record before storing it and refuses an
                incomplete or inconsistent one with the platform's parameter error.

    <br>
                The body is the complete configuration: parameters that are not listed are not stored,
    so read
                the configuration first and send it back with the fields you change. Parameters carry
    the
                module's own settings, and some modules keep credentials there — the whole request is
    treated
                as sensitive.

    <br>
                The trade server accepts the write only when the module is marked as editable through
    the
                manager interface, when plugin settings are pumped on the connection, and when the
    account of
                the API has the right to change plugin configurations; otherwise the platform error
    saying so is
                returned.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.
        body (MT5Plugin | Unset): Plugin configuration: the module loaded on a trade server
            together with the parameters it reads on
            start.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5PluginApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
