from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.int_32_api_response import Int32ApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/HistoryCorrect/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Int32ApiResponse | None:
    if response.status_code == 200:
        response_200 = Int32ApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Int32ApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Int32ApiResponse]:
    """ Repair chart history

     Recompute and patch internal consistency of a symbol's chart history.

    Manager (live) call. The MT4 server walks the symbol's full bar
    history for every period and fixes inconsistencies (gaps, broken
    OHLC relationships, mismatched aggregates). Returns the count of
    bars that the server corrected — zero is a valid result (history
    was already consistent).

    Requires Administrator rights on the manager account. The operation
    can take many seconds on long histories; pair with
    `Idempotency-Key` for retry safety so a TCP retry doesn't
    kick off a second full sweep.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Int32ApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Int32ApiResponse | None:
    """ Repair chart history

     Recompute and patch internal consistency of a symbol's chart history.

    Manager (live) call. The MT4 server walks the symbol's full bar
    history for every period and fixes inconsistencies (gaps, broken
    OHLC relationships, mismatched aggregates). Returns the count of
    bars that the server corrected — zero is a valid result (history
    was already consistent).

    Requires Administrator rights on the manager account. The operation
    can take many seconds on long histories; pair with
    `Idempotency-Key` for retry safety so a TCP retry doesn't
    kick off a second full sweep.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Int32ApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[Int32ApiResponse]:
    """ Repair chart history

     Recompute and patch internal consistency of a symbol's chart history.

    Manager (live) call. The MT4 server walks the symbol's full bar
    history for every period and fixes inconsistencies (gaps, broken
    OHLC relationships, mismatched aggregates). Returns the count of
    bars that the server corrected — zero is a valid result (history
    was already consistent).

    Requires Administrator rights on the manager account. The operation
    can take many seconds on long histories; pair with
    `Idempotency-Key` for retry safety so a TCP retry doesn't
    kick off a second full sweep.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Int32ApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Int32ApiResponse | None:
    """ Repair chart history

     Recompute and patch internal consistency of a symbol's chart history.

    Manager (live) call. The MT4 server walks the symbol's full bar
    history for every period and fixes inconsistencies (gaps, broken
    OHLC relationships, mismatched aggregates). Returns the count of
    bars that the server corrected — zero is a valid result (history
    was already consistent).

    Requires Administrator rights on the manager account. The operation
    can take many seconds on long histories; pair with
    `Idempotency-Key` for retry safety so a TCP retry doesn't
    kick off a second full sweep.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Int32ApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,

    )).parsed
