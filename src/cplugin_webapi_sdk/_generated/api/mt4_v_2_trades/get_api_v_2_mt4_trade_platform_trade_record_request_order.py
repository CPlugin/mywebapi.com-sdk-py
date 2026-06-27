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
    order: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/TradeRecordRequest/{order}".format(trade_platform=quote(str(trade_platform), safe=""),order=quote(str(order), safe=""),),
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
    order: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4TradeApiResponse]:
    """ Get trade record (live)

     Fresh-from-server fetch of a single trade record by ticket.

    Manager (live) counterpart to `TradeRecordGet`. Where the pump
    variant reads from local cache (may lag by milliseconds), this round-
    trips to the MT4 server every call — slower but authoritative.
    Useful for reconciliation, post-close ticket lookups (pump may have
    flushed), or any flow where the caller can tolerate the latency cost
    in exchange for guaranteed freshness. Returns NotFound envelope when
    the ticket does not exist on the server.

    Args:
        trade_platform (UUID):
        order (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
order=order,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    order: int,
    *,
    client: AuthenticatedClient | Client,

) -> MT4TradeApiResponse | None:
    """ Get trade record (live)

     Fresh-from-server fetch of a single trade record by ticket.

    Manager (live) counterpart to `TradeRecordGet`. Where the pump
    variant reads from local cache (may lag by milliseconds), this round-
    trips to the MT4 server every call — slower but authoritative.
    Useful for reconciliation, post-close ticket lookups (pump may have
    flushed), or any flow where the caller can tolerate the latency cost
    in exchange for guaranteed freshness. Returns NotFound envelope when
    the ticket does not exist on the server.

    Args:
        trade_platform (UUID):
        order (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
order=order,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    order: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4TradeApiResponse]:
    """ Get trade record (live)

     Fresh-from-server fetch of a single trade record by ticket.

    Manager (live) counterpart to `TradeRecordGet`. Where the pump
    variant reads from local cache (may lag by milliseconds), this round-
    trips to the MT4 server every call — slower but authoritative.
    Useful for reconciliation, post-close ticket lookups (pump may have
    flushed), or any flow where the caller can tolerate the latency cost
    in exchange for guaranteed freshness. Returns NotFound envelope when
    the ticket does not exist on the server.

    Args:
        trade_platform (UUID):
        order (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
order=order,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    order: int,
    *,
    client: AuthenticatedClient | Client,

) -> MT4TradeApiResponse | None:
    """ Get trade record (live)

     Fresh-from-server fetch of a single trade record by ticket.

    Manager (live) counterpart to `TradeRecordGet`. Where the pump
    variant reads from local cache (may lag by milliseconds), this round-
    trips to the MT4 server every call — slower but authoritative.
    Useful for reconciliation, post-close ticket lookups (pump may have
    flushed), or any flow where the caller can tolerate the latency cost
    in exchange for guaranteed freshness. Returns NotFound envelope when
    the ticket does not exist on the server.

    Args:
        trade_platform (UUID):
        order (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
order=order,
client=client,

    )).parsed
