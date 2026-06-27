from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    license_name: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/LicenseCheck/{license_name}".format(trade_platform=quote(str(trade_platform), safe=""),license_name=quote(str(license_name), safe=""),),
    }


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
    license_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[BooleanApiResponse]:
    r""" Check license

     Check a license name against the MT4 server's license registry — admin-only read.

    Manager (live) call to the wrapper's `LicenseCheck(name)`.
    Returns a bare `bool` payload: `true` when the wrapper's
    result code is `Ok`, indicating the license is recognized;
    `false` on any non-Ok code (covers both \"license not found\"
    and \"manager lacks permission to query the license registry\").

    Args:
        trade_platform (UUID):
        license_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
license_name=license_name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    license_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> BooleanApiResponse | None:
    r""" Check license

     Check a license name against the MT4 server's license registry — admin-only read.

    Manager (live) call to the wrapper's `LicenseCheck(name)`.
    Returns a bare `bool` payload: `true` when the wrapper's
    result code is `Ok`, indicating the license is recognized;
    `false` on any non-Ok code (covers both \"license not found\"
    and \"manager lacks permission to query the license registry\").

    Args:
        trade_platform (UUID):
        license_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
license_name=license_name,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    license_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[BooleanApiResponse]:
    r""" Check license

     Check a license name against the MT4 server's license registry — admin-only read.

    Manager (live) call to the wrapper's `LicenseCheck(name)`.
    Returns a bare `bool` payload: `true` when the wrapper's
    result code is `Ok`, indicating the license is recognized;
    `false` on any non-Ok code (covers both \"license not found\"
    and \"manager lacks permission to query the license registry\").

    Args:
        trade_platform (UUID):
        license_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
license_name=license_name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    license_name: str,
    *,
    client: AuthenticatedClient | Client,

) -> BooleanApiResponse | None:
    r""" Check license

     Check a license name against the MT4 server's license registry — admin-only read.

    Manager (live) call to the wrapper's `LicenseCheck(name)`.
    Returns a bare `bool` payload: `true` when the wrapper's
    result code is `Ok`, indicating the license is recognized;
    `false` on any non-Ok code (covers both \"license not found\"
    and \"manager lacks permission to query the license registry\").

    Args:
        trade_platform (UUID):
        license_name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
license_name=license_name,
client=client,

    )).parsed
