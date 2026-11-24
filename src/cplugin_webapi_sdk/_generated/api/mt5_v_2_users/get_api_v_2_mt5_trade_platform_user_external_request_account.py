from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_user_api_response import MT5UserApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    account: str,
    *,
    gateway_id: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["gatewayId"] = gateway_id


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/UserExternalRequest/{account}".format(trade_platform=quote(str(trade_platform), safe=""),account=quote(str(account), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5UserApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5UserApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5UserApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    account: str,
    *,
    client: AuthenticatedClient | Client,
    gateway_id: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserApiResponse]:
    """ Read an account by its number in an external trading system, from the trade server

     <br>
                Same lookup as the cached read, but the record is requested from the trade server
    instead
                of the local cache, so it reflects changes made on the server immediately. When several
                accounts carry the same external number, the nearest record is returned.

    <br>
                The gateway identifier is optional: without it the number is matched against every
    gateway.
                The call only reads and changes nothing.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        account (str):
        gateway_id (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
account=account,
gateway_id=gateway_id,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    account: str,
    *,
    client: AuthenticatedClient | Client,
    gateway_id: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserApiResponse | None:
    """ Read an account by its number in an external trading system, from the trade server

     <br>
                Same lookup as the cached read, but the record is requested from the trade server
    instead
                of the local cache, so it reflects changes made on the server immediately. When several
                accounts carry the same external number, the nearest record is returned.

    <br>
                The gateway identifier is optional: without it the number is matched against every
    gateway.
                The call only reads and changes nothing.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        account (str):
        gateway_id (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
account=account,
client=client,
gateway_id=gateway_id,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    account: str,
    *,
    client: AuthenticatedClient | Client,
    gateway_id: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserApiResponse]:
    """ Read an account by its number in an external trading system, from the trade server

     <br>
                Same lookup as the cached read, but the record is requested from the trade server
    instead
                of the local cache, so it reflects changes made on the server immediately. When several
                accounts carry the same external number, the nearest record is returned.

    <br>
                The gateway identifier is optional: without it the number is matched against every
    gateway.
                The call only reads and changes nothing.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        account (str):
        gateway_id (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
account=account,
gateway_id=gateway_id,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    account: str,
    *,
    client: AuthenticatedClient | Client,
    gateway_id: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserApiResponse | None:
    """ Read an account by its number in an external trading system, from the trade server

     <br>
                Same lookup as the cached read, but the record is requested from the trade server
    instead
                of the local cache, so it reflects changes made on the server immediately. When several
                accounts carry the same external number, the nearest record is returned.

    <br>
                The gateway identifier is optional: without it the number is matched against every
    gateway.
                The call only reads and changes nothing.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        account (str):
        gateway_id (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
account=account,
client=client,
gateway_id=gateway_id,
x_request_timeout=x_request_timeout,

    )).parsed
