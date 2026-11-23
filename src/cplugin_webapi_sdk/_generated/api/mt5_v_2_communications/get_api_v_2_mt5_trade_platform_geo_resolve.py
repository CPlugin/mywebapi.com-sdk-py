from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_geo_record_api_response import MT5GeoRecordApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    address: str | Unset = UNSET,
    flags: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["address"] = address

    params["flags"] = flags


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/GeoResolve".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5GeoRecordApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5GeoRecordApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5GeoRecordApiResponse]:
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
    address: str | Unset = UNSET,
    flags: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5GeoRecordApiResponse]:
    """ Describe an IP address

     Resolves the IPv4 or IPv6 address against the geo database of the platform and returns the
    description of the address range it belongs to: geography, network owner and the additional
    characteristics of the address.

    The flags choose which data is requested — the fields whose flag was not set are left empty,
    so asking for everything costs one answer of the widest kind but is the simplest way to fill
    the record. The record carries the IPv4 bounds of the range; the IPv6 bounds are not
    returned.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        address (str | Unset):
        flags (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5GeoRecordApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
address=address,
flags=flags,
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
    address: str | Unset = UNSET,
    flags: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5GeoRecordApiResponse | None:
    """ Describe an IP address

     Resolves the IPv4 or IPv6 address against the geo database of the platform and returns the
    description of the address range it belongs to: geography, network owner and the additional
    characteristics of the address.

    The flags choose which data is requested — the fields whose flag was not set are left empty,
    so asking for everything costs one answer of the widest kind but is the simplest way to fill
    the record. The record carries the IPv4 bounds of the range; the IPv6 bounds are not
    returned.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        address (str | Unset):
        flags (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5GeoRecordApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
address=address,
flags=flags,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    address: str | Unset = UNSET,
    flags: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5GeoRecordApiResponse]:
    """ Describe an IP address

     Resolves the IPv4 or IPv6 address against the geo database of the platform and returns the
    description of the address range it belongs to: geography, network owner and the additional
    characteristics of the address.

    The flags choose which data is requested — the fields whose flag was not set are left empty,
    so asking for everything costs one answer of the widest kind but is the simplest way to fill
    the record. The record carries the IPv4 bounds of the range; the IPv6 bounds are not
    returned.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        address (str | Unset):
        flags (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5GeoRecordApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
address=address,
flags=flags,
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
    address: str | Unset = UNSET,
    flags: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5GeoRecordApiResponse | None:
    """ Describe an IP address

     Resolves the IPv4 or IPv6 address against the geo database of the platform and returns the
    description of the address range it belongs to: geography, network owner and the additional
    characteristics of the address.

    The flags choose which data is requested — the fields whose flag was not set are left empty,
    so asking for everything costs one answer of the widest kind but is the simplest way to fill
    the record. The record carries the IPv4 bounds of the range; the IPv6 bounds are not
    returned.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        address (str | Unset):
        flags (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5GeoRecordApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
address=address,
flags=flags,
x_request_timeout=x_request_timeout,

    )).parsed
