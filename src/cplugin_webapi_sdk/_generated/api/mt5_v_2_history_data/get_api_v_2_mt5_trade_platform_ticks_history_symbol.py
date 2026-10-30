from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_tick_page_api_response import MT5TickPageApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/TicksHistory/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5TickPageApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5TickPageApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5TickPageApiResponse]:
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5TickPageApiResponse]:
    """ Get historical ticks

     <br>
                Historical ticks of a symbol for a time window, filtered by the symbol's tick
                filters, ordered by time ascending.

    <br>
                Times are the trading times of the trade server, not UTC: `timeMsc` and
                `time` repeat the millisecond and second values the platform uses,
                `dateTime` is the same moment without an offset. Prices are returned as the
                platform holds them, without rescaling. `flags` names the set bits of the
                tick kind, the same way the streaming events do.

    <br>
      `from` and `to` are optional: without `from` the window starts at
                the beginning of the history, without `to` it ends at the current server
                time. `limit` is 0 by default and returns the whole window; a positive value
                caps the returned ticks and sets `truncated`. There is no pagination: to read
                further, repeat the request with `from` moved past the last returned tick.

    <br>
                The call only reads and changes nothing. When the platform has not received the
                requested history yet, the call fails with the platform code `MT_RET_OK_NONE`
                and a message saying the history is not synchronized — such a request may be
                repeated later.


    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        limit (int | Unset):  Default: 0.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5TickPageApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
from_=from_,
to=to,
limit=limit,
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> MT5TickPageApiResponse | None:
    """ Get historical ticks

     <br>
                Historical ticks of a symbol for a time window, filtered by the symbol's tick
                filters, ordered by time ascending.

    <br>
                Times are the trading times of the trade server, not UTC: `timeMsc` and
                `time` repeat the millisecond and second values the platform uses,
                `dateTime` is the same moment without an offset. Prices are returned as the
                platform holds them, without rescaling. `flags` names the set bits of the
                tick kind, the same way the streaming events do.

    <br>
      `from` and `to` are optional: without `from` the window starts at
                the beginning of the history, without `to` it ends at the current server
                time. `limit` is 0 by default and returns the whole window; a positive value
                caps the returned ticks and sets `truncated`. There is no pagination: to read
                further, repeat the request with `from` moved past the last returned tick.

    <br>
                The call only reads and changes nothing. When the platform has not received the
                requested history yet, the call fails with the platform code `MT_RET_OK_NONE`
                and a message saying the history is not synchronized — such a request may be
                repeated later.


    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        limit (int | Unset):  Default: 0.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5TickPageApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
from_=from_,
to=to,
limit=limit,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5TickPageApiResponse]:
    """ Get historical ticks

     <br>
                Historical ticks of a symbol for a time window, filtered by the symbol's tick
                filters, ordered by time ascending.

    <br>
                Times are the trading times of the trade server, not UTC: `timeMsc` and
                `time` repeat the millisecond and second values the platform uses,
                `dateTime` is the same moment without an offset. Prices are returned as the
                platform holds them, without rescaling. `flags` names the set bits of the
                tick kind, the same way the streaming events do.

    <br>
      `from` and `to` are optional: without `from` the window starts at
                the beginning of the history, without `to` it ends at the current server
                time. `limit` is 0 by default and returns the whole window; a positive value
                caps the returned ticks and sets `truncated`. There is no pagination: to read
                further, repeat the request with `from` moved past the last returned tick.

    <br>
                The call only reads and changes nothing. When the platform has not received the
                requested history yet, the call fails with the platform code `MT_RET_OK_NONE`
                and a message saying the history is not synchronized — such a request may be
                repeated later.


    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        limit (int | Unset):  Default: 0.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5TickPageApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
from_=from_,
to=to,
limit=limit,
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    limit: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> MT5TickPageApiResponse | None:
    """ Get historical ticks

     <br>
                Historical ticks of a symbol for a time window, filtered by the symbol's tick
                filters, ordered by time ascending.

    <br>
                Times are the trading times of the trade server, not UTC: `timeMsc` and
                `time` repeat the millisecond and second values the platform uses,
                `dateTime` is the same moment without an offset. Prices are returned as the
                platform holds them, without rescaling. `flags` names the set bits of the
                tick kind, the same way the streaming events do.

    <br>
      `from` and `to` are optional: without `from` the window starts at
                the beginning of the history, without `to` it ends at the current server
                time. `limit` is 0 by default and returns the whole window; a positive value
                caps the returned ticks and sets `truncated`. There is no pagination: to read
                further, repeat the request with `from` moved past the last returned tick.

    <br>
                The call only reads and changes nothing. When the platform has not received the
                requested history yet, the call fails with the platform code `MT_RET_OK_NONE`
                and a message saying the history is not synchronized — such a request may be
                repeated later.


    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        limit (int | Unset):  Default: 0.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5TickPageApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
from_=from_,
to=to,
limit=limit,
x_request_timeout=x_request_timeout,

    )).parsed
