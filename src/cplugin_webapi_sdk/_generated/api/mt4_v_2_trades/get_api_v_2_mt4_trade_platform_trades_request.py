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
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    group: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params["group"] = group


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/TradesRequest".format(trade_platform=quote(str(trade_platform), safe=""),),
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
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    group: str | Unset = UNSET,

) -> Response[MT4TradeListApiResponse]:
    r""" Query trades (live)

     Broad Manager-live trade query. Returns every trade visible to the authenticated manager, paged by
    ticket ascending.

    Manager (live) — each call hits the MT4 server. Designed as the
    \"scan from scratch\" counterpart to the pump variants
    (`TradesGetByMarket`, `TradesGetBySymbol`): pump reads are
    instant but limited to currently-open trades visible to the pump;
    this endpoint returns the full server-side set the manager can see.
    Heavy — paginate aggressively, prefer pump variants when freshness
    is not critical.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,
group=group,

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
    group: str | Unset = UNSET,

) -> MT4TradeListApiResponse | None:
    r""" Query trades (live)

     Broad Manager-live trade query. Returns every trade visible to the authenticated manager, paged by
    ticket ascending.

    Manager (live) — each call hits the MT4 server. Designed as the
    \"scan from scratch\" counterpart to the pump variants
    (`TradesGetByMarket`, `TradesGetBySymbol`): pump reads are
    instant but limited to currently-open trades visible to the pump;
    this endpoint returns the full server-side set the manager can see.
    Heavy — paginate aggressively, prefer pump variants when freshness
    is not critical.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,
group=group,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    group: str | Unset = UNSET,

) -> Response[MT4TradeListApiResponse]:
    r""" Query trades (live)

     Broad Manager-live trade query. Returns every trade visible to the authenticated manager, paged by
    ticket ascending.

    Manager (live) — each call hits the MT4 server. Designed as the
    \"scan from scratch\" counterpart to the pump variants
    (`TradesGetByMarket`, `TradesGetBySymbol`): pump reads are
    instant but limited to currently-open trades visible to the pump;
    this endpoint returns the full server-side set the manager can see.
    Heavy — paginate aggressively, prefer pump variants when freshness
    is not critical.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,
group=group,

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
    group: str | Unset = UNSET,

) -> MT4TradeListApiResponse | None:
    r""" Query trades (live)

     Broad Manager-live trade query. Returns every trade visible to the authenticated manager, paged by
    ticket ascending.

    Manager (live) — each call hits the MT4 server. Designed as the
    \"scan from scratch\" counterpart to the pump variants
    (`TradesGetByMarket`, `TradesGetBySymbol`): pump reads are
    instant but limited to currently-open trades visible to the pump;
    this endpoint returns the full server-side set the manager can see.
    Heavy — paginate aggressively, prefer pump variants when freshness
    is not critical.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        group (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,
group=group,

    )).parsed
