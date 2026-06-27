from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.chart_period import ChartPeriod
from ...models.mt4_chart_bar_list_api_response import MT4ChartBarListApiResponse
from ...models.request_mode import RequestMode
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    period: ChartPeriod | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    mode: RequestMode | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: str | Unset = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    json_mode: str | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/ChartRequest/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4ChartBarListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4ChartBarListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4ChartBarListApiResponse]:
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
    period: ChartPeriod | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    mode: RequestMode | Unset = UNSET,

) -> Response[MT4ChartBarListApiResponse]:
    """ Get chart bars

     OHLC chart bars for a symbol over a date range.

    Manager (live) call. Resolves the symbol's `ConSymbol` first
    (needed by the wrapper to set scale/digits), then asks for bars of
    the given `period` in the date window. `mode` defaults to
    `RangeInExcludeOutOfRage` — bars whose time falls strictly
    inside the window.

    Args:
        trade_platform (UUID):
        symbol (str):
        period (ChartPeriod | Unset):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        mode (RequestMode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ChartBarListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
period=period,
start=start,
end=end,
mode=mode,

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
    period: ChartPeriod | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    mode: RequestMode | Unset = UNSET,

) -> MT4ChartBarListApiResponse | None:
    """ Get chart bars

     OHLC chart bars for a symbol over a date range.

    Manager (live) call. Resolves the symbol's `ConSymbol` first
    (needed by the wrapper to set scale/digits), then asks for bars of
    the given `period` in the date window. `mode` defaults to
    `RangeInExcludeOutOfRage` — bars whose time falls strictly
    inside the window.

    Args:
        trade_platform (UUID):
        symbol (str):
        period (ChartPeriod | Unset):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        mode (RequestMode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ChartBarListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
period=period,
start=start,
end=end,
mode=mode,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    period: ChartPeriod | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    mode: RequestMode | Unset = UNSET,

) -> Response[MT4ChartBarListApiResponse]:
    """ Get chart bars

     OHLC chart bars for a symbol over a date range.

    Manager (live) call. Resolves the symbol's `ConSymbol` first
    (needed by the wrapper to set scale/digits), then asks for bars of
    the given `period` in the date window. `mode` defaults to
    `RangeInExcludeOutOfRage` — bars whose time falls strictly
    inside the window.

    Args:
        trade_platform (UUID):
        symbol (str):
        period (ChartPeriod | Unset):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        mode (RequestMode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ChartBarListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
period=period,
start=start,
end=end,
mode=mode,

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
    period: ChartPeriod | Unset = UNSET,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    mode: RequestMode | Unset = UNSET,

) -> MT4ChartBarListApiResponse | None:
    """ Get chart bars

     OHLC chart bars for a symbol over a date range.

    Manager (live) call. Resolves the symbol's `ConSymbol` first
    (needed by the wrapper to set scale/digits), then asks for bars of
    the given `period` in the date window. `mode` defaults to
    `RangeInExcludeOutOfRage` — bars whose time falls strictly
    inside the window.

    Args:
        trade_platform (UUID):
        symbol (str):
        period (ChartPeriod | Unset):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        mode (RequestMode | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ChartBarListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
period=period,
start=start,
end=end,
mode=mode,

    )).parsed
