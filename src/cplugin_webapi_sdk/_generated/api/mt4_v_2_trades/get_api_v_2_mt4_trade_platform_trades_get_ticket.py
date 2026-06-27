from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_trade_api_response import MT4TradeApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    ticket: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/TradesGet/{ticket}".format(trade_platform=quote(str(trade_platform), safe=""),ticket=quote(str(ticket), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4TradeApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4TradeApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4TradeApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    ticket: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4TradeApiResponse]:
    """ Get trade by ticket (cached)

     Open trade by ticket from the pump cache (dictionary lookup variant).

    Counterpart to `TradeRecordGet/{order}` — both are pump reads,
    but the wrapper exposes two distinct call paths: `TradeRecordGet`
    uses a dedicated single-record method, while this endpoint looks the
    trade up in the open-trades dictionary. Behaviourally equivalent for
    open trades; `TradeRecordGet` can also resolve recently closed
    trades that linger in cache.

    Args:
        trade_platform (UUID):
        ticket (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
ticket=ticket,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    ticket: int,
    *,
    client: AuthenticatedClient | Client,

) -> MT4TradeApiResponse | None:
    """ Get trade by ticket (cached)

     Open trade by ticket from the pump cache (dictionary lookup variant).

    Counterpart to `TradeRecordGet/{order}` — both are pump reads,
    but the wrapper exposes two distinct call paths: `TradeRecordGet`
    uses a dedicated single-record method, while this endpoint looks the
    trade up in the open-trades dictionary. Behaviourally equivalent for
    open trades; `TradeRecordGet` can also resolve recently closed
    trades that linger in cache.

    Args:
        trade_platform (UUID):
        ticket (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
ticket=ticket,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    ticket: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4TradeApiResponse]:
    """ Get trade by ticket (cached)

     Open trade by ticket from the pump cache (dictionary lookup variant).

    Counterpart to `TradeRecordGet/{order}` — both are pump reads,
    but the wrapper exposes two distinct call paths: `TradeRecordGet`
    uses a dedicated single-record method, while this endpoint looks the
    trade up in the open-trades dictionary. Behaviourally equivalent for
    open trades; `TradeRecordGet` can also resolve recently closed
    trades that linger in cache.

    Args:
        trade_platform (UUID):
        ticket (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
ticket=ticket,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    ticket: int,
    *,
    client: AuthenticatedClient | Client,

) -> MT4TradeApiResponse | None:
    """ Get trade by ticket (cached)

     Open trade by ticket from the pump cache (dictionary lookup variant).

    Counterpart to `TradeRecordGet/{order}` — both are pump reads,
    but the wrapper exposes two distinct call paths: `TradeRecordGet`
    uses a dedicated single-record method, while this endpoint looks the
    trade up in the open-trades dictionary. Behaviourally equivalent for
    open trades; `TradeRecordGet` can also resolve recently closed
    trades that linger in cache.

    Args:
        trade_platform (UUID):
        ticket (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
ticket=ticket,
client=client,

    )).parsed
