from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_trade_list_api_response import MT4TradeListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    group: str,
    *,
    open_only: bool | Unset = True,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["openOnly"] = open_only


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/AdmTradesRequest/{group}".format(trade_platform=quote(str(trade_platform), safe=""),group=quote(str(group), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4TradeListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4TradeListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4TradeListApiResponse]:
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
    open_only: bool | Unset = True,

) -> Response[MT4TradeListApiResponse]:
    """ List group trades (admin)

     All trades belonging to accounts in a given group (admin scope).

    Manager (live) call. Returns trades for every account assigned to
    the given group. `openOnly=true` filters out closed trades on
    the server side. Pair with `Idempotency-Key` on retry — large
    groups can return substantial payloads.

    Args:
        trade_platform (UUID):
        group (str):
        open_only (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
open_only=open_only,

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
    open_only: bool | Unset = True,

) -> MT4TradeListApiResponse | None:
    """ List group trades (admin)

     All trades belonging to accounts in a given group (admin scope).

    Manager (live) call. Returns trades for every account assigned to
    the given group. `openOnly=true` filters out closed trades on
    the server side. Pair with `Idempotency-Key` on retry — large
    groups can return substantial payloads.

    Args:
        trade_platform (UUID):
        group (str):
        open_only (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
open_only=open_only,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    open_only: bool | Unset = True,

) -> Response[MT4TradeListApiResponse]:
    """ List group trades (admin)

     All trades belonging to accounts in a given group (admin scope).

    Manager (live) call. Returns trades for every account assigned to
    the given group. `openOnly=true` filters out closed trades on
    the server side. Pair with `Idempotency-Key` on retry — large
    groups can return substantial payloads.

    Args:
        trade_platform (UUID):
        group (str):
        open_only (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
open_only=open_only,

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
    open_only: bool | Unset = True,

) -> MT4TradeListApiResponse | None:
    """ List group trades (admin)

     All trades belonging to accounts in a given group (admin scope).

    Manager (live) call. Returns trades for every account assigned to
    the given group. `openOnly=true` filters out closed trades on
    the server side. Pair with `Idempotency-Key` on retry — large
    groups can return substantial payloads.

    Args:
        trade_platform (UUID):
        group (str):
        open_only (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
open_only=open_only,

    )).parsed
