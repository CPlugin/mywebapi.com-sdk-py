from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.int_32_api_response import Int32ApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/HistoryCorrect/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }


    _kwargs["headers"] = headers
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
    x_request_timeout: float | Unset = UNSET,

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

    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Int32ApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
x_request_timeout=x_request_timeout,

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
    x_request_timeout: float | Unset = UNSET,

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

    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

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
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

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

    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Int32ApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
x_request_timeout=x_request_timeout,

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
    x_request_timeout: float | Unset = UNSET,

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

    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

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
x_request_timeout=x_request_timeout,

    )).parsed
