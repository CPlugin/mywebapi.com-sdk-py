from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_con_subscription_api_response import MT5ConSubscriptionApiResponse
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
        "url": "/api/v2/MT5/{trade_platform}/SubscriptionCfgGet/{name}".format(trade_platform=quote(str(trade_platform), safe=""),name=quote(str(name), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5ConSubscriptionApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5ConSubscriptionApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5ConSubscriptionApiResponse]:
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

) -> Response[MT5ConSubscriptionApiResponse]:
    """ Subscription configuration by name, from the streamed copy

     <br>
                Returns the subscription configuration with the given name from the configuration copy
                that the trade server streams to this connection. The call does not reach the server, so
                it answers immediately and may lag behind the server by the time of the last update.

    <br>
                The copy exists only when the configuration stream is enabled for the connection;
                otherwise the call fails with the platform error. Use the request form to read the
                configuration directly from the server.


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
        Response[MT5ConSubscriptionApiResponse]
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

) -> MT5ConSubscriptionApiResponse | None:
    """ Subscription configuration by name, from the streamed copy

     <br>
                Returns the subscription configuration with the given name from the configuration copy
                that the trade server streams to this connection. The call does not reach the server, so
                it answers immediately and may lag behind the server by the time of the last update.

    <br>
                The copy exists only when the configuration stream is enabled for the connection;
                otherwise the call fails with the platform error. Use the request form to read the
                configuration directly from the server.


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
        MT5ConSubscriptionApiResponse
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

) -> Response[MT5ConSubscriptionApiResponse]:
    """ Subscription configuration by name, from the streamed copy

     <br>
                Returns the subscription configuration with the given name from the configuration copy
                that the trade server streams to this connection. The call does not reach the server, so
                it answers immediately and may lag behind the server by the time of the last update.

    <br>
                The copy exists only when the configuration stream is enabled for the connection;
                otherwise the call fails with the platform error. Use the request form to read the
                configuration directly from the server.


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
        Response[MT5ConSubscriptionApiResponse]
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

) -> MT5ConSubscriptionApiResponse | None:
    """ Subscription configuration by name, from the streamed copy

     <br>
                Returns the subscription configuration with the given name from the configuration copy
                that the trade server streams to this connection. The call does not reach the server, so
                it answers immediately and may lag behind the server by the time of the last update.

    <br>
                The copy exists only when the configuration stream is enabled for the connection;
                otherwise the call fails with the platform error. Use the request form to read the
                configuration directly from the server.


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
        MT5ConSubscriptionApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
name=name,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
