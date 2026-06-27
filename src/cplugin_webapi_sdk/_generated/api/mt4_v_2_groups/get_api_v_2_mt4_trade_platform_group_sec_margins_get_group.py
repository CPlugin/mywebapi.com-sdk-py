from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_group_margin_list_api_response import MT4GroupMarginListApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    group: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/GroupSecMarginsGet/{group}".format(trade_platform=quote(str(trade_platform), safe=""),group=quote(str(group), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4GroupMarginListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4GroupMarginListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4GroupMarginListApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4GroupMarginListApiResponse]:
    """ Get group margin overrides

     Special-securities margin overrides (`SecMargins`) for one group.

    Pump-cached read. Returns the first `SecMarginsTotal` entries of
    the wrapper's 128-element `SecMargins` array — the trailing
    slots are always uninitialised padding. `SecMarginsTotal` itself
    is part of the parent `MT4Group` DTO.

    Args:
        trade_platform (UUID):
        group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GroupMarginListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,

) -> MT4GroupMarginListApiResponse | None:
    """ Get group margin overrides

     Special-securities margin overrides (`SecMargins`) for one group.

    Pump-cached read. Returns the first `SecMarginsTotal` entries of
    the wrapper's 128-element `SecMargins` array — the trailing
    slots are always uninitialised padding. `SecMarginsTotal` itself
    is part of the parent `MT4Group` DTO.

    Args:
        trade_platform (UUID):
        group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GroupMarginListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
group=group,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4GroupMarginListApiResponse]:
    """ Get group margin overrides

     Special-securities margin overrides (`SecMargins`) for one group.

    Pump-cached read. Returns the first `SecMarginsTotal` entries of
    the wrapper's 128-element `SecMargins` array — the trailing
    slots are always uninitialised padding. `SecMarginsTotal` itself
    is part of the parent `MT4Group` DTO.

    Args:
        trade_platform (UUID):
        group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GroupMarginListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,

) -> MT4GroupMarginListApiResponse | None:
    """ Get group margin overrides

     Special-securities margin overrides (`SecMargins`) for one group.

    Pump-cached read. Returns the first `SecMarginsTotal` entries of
    the wrapper's 128-element `SecMargins` array — the trailing
    slots are always uninitialised padding. `SecMarginsTotal` itself
    is part of the parent `MT4Group` DTO.

    Args:
        trade_platform (UUID):
        group (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GroupMarginListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
group=group,
client=client,

    )).parsed
