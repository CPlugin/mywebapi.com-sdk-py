from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_access_list_api_response import MT4AccessListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/CfgRequestAccess".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4AccessListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4AccessListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4AccessListApiResponse]:
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
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[MT4AccessListApiResponse]:
    r""" List IP firewall rules

     All firewall (IP access) rules configured on the MT4 server, paginated.

    Manager-live read (round-trip). Each entry describes an IP range
    (IpFrom..IpTo, widened uint→long for JSON safety) with an Action
    flag and a free-form Comment. Ordering: by (IpFrom, IpTo) ascending.
    Cursor is an opaque base64 string holding the composite key
    \"{IpFrom:D10}|{IpTo:D10}\" — D10 width matches uint range (max
    4_294_967_295 = 10 digits) so lexicographic compare matches
    numeric compare, and the '|' delimiter cannot appear in IP values.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4AccessListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> MT4AccessListApiResponse | None:
    r""" List IP firewall rules

     All firewall (IP access) rules configured on the MT4 server, paginated.

    Manager-live read (round-trip). Each entry describes an IP range
    (IpFrom..IpTo, widened uint→long for JSON safety) with an Action
    flag and a free-form Comment. Ordering: by (IpFrom, IpTo) ascending.
    Cursor is an opaque base64 string holding the composite key
    \"{IpFrom:D10}|{IpTo:D10}\" — D10 width matches uint range (max
    4_294_967_295 = 10 digits) so lexicographic compare matches
    numeric compare, and the '|' delimiter cannot appear in IP values.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4AccessListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[MT4AccessListApiResponse]:
    r""" List IP firewall rules

     All firewall (IP access) rules configured on the MT4 server, paginated.

    Manager-live read (round-trip). Each entry describes an IP range
    (IpFrom..IpTo, widened uint→long for JSON safety) with an Action
    flag and a free-form Comment. Ordering: by (IpFrom, IpTo) ascending.
    Cursor is an opaque base64 string holding the composite key
    \"{IpFrom:D10}|{IpTo:D10}\" — D10 width matches uint range (max
    4_294_967_295 = 10 digits) so lexicographic compare matches
    numeric compare, and the '|' delimiter cannot appear in IP values.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4AccessListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> MT4AccessListApiResponse | None:
    r""" List IP firewall rules

     All firewall (IP access) rules configured on the MT4 server, paginated.

    Manager-live read (round-trip). Each entry describes an IP range
    (IpFrom..IpTo, widened uint→long for JSON safety) with an Action
    flag and a free-form Comment. Ordering: by (IpFrom, IpTo) ascending.
    Cursor is an opaque base64 string holding the composite key
    \"{IpFrom:D10}|{IpTo:D10}\" — D10 width matches uint range (max
    4_294_967_295 = 10 digits) so lexicographic compare matches
    numeric compare, and the '|' delimiter cannot appear in IP values.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4AccessListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,

    )).parsed
