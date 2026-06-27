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
    orders: list[int] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_orders: list[int] | Unset = UNSET
    if not isinstance(orders, Unset):
        json_orders = orders


    params["orders"] = json_orders


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/TradeRecordsRequest".format(trade_platform=quote(str(trade_platform), safe=""),),
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
    orders: list[int] | Unset = UNSET,

) -> Response[MT4TradeListApiResponse]:
    """ Get trade records batch (live)

     Trade records for a batch of order tickets — live round-trip.

    Manager (live) call. Pass tickets as repeated query parameters:
    `?orders=12345&orders=67890`. Server-side billing counts this
    as one Manager request regardless of array length — prefer this over
    looping single `TradeRecordGet` calls.

    Returns the trade records the server has for the requested tickets.
    Order in the response is NOT guaranteed to match the request order;
    missing tickets are silently omitted (the envelope is not an error
    envelope in that case — match by `order` field on the client).

    Args:
        trade_platform (UUID):
        orders (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
orders=orders,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    orders: list[int] | Unset = UNSET,

) -> MT4TradeListApiResponse | None:
    """ Get trade records batch (live)

     Trade records for a batch of order tickets — live round-trip.

    Manager (live) call. Pass tickets as repeated query parameters:
    `?orders=12345&orders=67890`. Server-side billing counts this
    as one Manager request regardless of array length — prefer this over
    looping single `TradeRecordGet` calls.

    Returns the trade records the server has for the requested tickets.
    Order in the response is NOT guaranteed to match the request order;
    missing tickets are silently omitted (the envelope is not an error
    envelope in that case — match by `order` field on the client).

    Args:
        trade_platform (UUID):
        orders (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
orders=orders,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    orders: list[int] | Unset = UNSET,

) -> Response[MT4TradeListApiResponse]:
    """ Get trade records batch (live)

     Trade records for a batch of order tickets — live round-trip.

    Manager (live) call. Pass tickets as repeated query parameters:
    `?orders=12345&orders=67890`. Server-side billing counts this
    as one Manager request regardless of array length — prefer this over
    looping single `TradeRecordGet` calls.

    Returns the trade records the server has for the requested tickets.
    Order in the response is NOT guaranteed to match the request order;
    missing tickets are silently omitted (the envelope is not an error
    envelope in that case — match by `order` field on the client).

    Args:
        trade_platform (UUID):
        orders (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
orders=orders,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    orders: list[int] | Unset = UNSET,

) -> MT4TradeListApiResponse | None:
    """ Get trade records batch (live)

     Trade records for a batch of order tickets — live round-trip.

    Manager (live) call. Pass tickets as repeated query parameters:
    `?orders=12345&orders=67890`. Server-side billing counts this
    as one Manager request regardless of array length — prefer this over
    looping single `TradeRecordGet` calls.

    Returns the trade records the server has for the requested tickets.
    Order in the response is NOT guaranteed to match the request order;
    missing tickets are silently omitted (the envelope is not an error
    envelope in that case — match by `order` field on the client).

    Args:
        trade_platform (UUID):
        orders (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
orders=orders,

    )).parsed
