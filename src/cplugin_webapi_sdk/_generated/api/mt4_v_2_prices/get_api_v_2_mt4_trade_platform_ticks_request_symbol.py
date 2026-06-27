from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_tick_record_list_api_response import MT4TickRecordListApiResponse
from ...models.tick_request_flags import TickRequestFlags
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    flags: TickRequestFlags | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_start: str | Unset = UNSET
    if not isinstance(start, Unset):
        json_start = start.isoformat()
    params["start"] = json_start

    json_end: str | Unset = UNSET
    if not isinstance(end, Unset):
        json_end = end.isoformat()
    params["end"] = json_end

    json_flags: str | Unset = UNSET
    if not isinstance(flags, Unset):
        json_flags = flags.value

    params["flags"] = json_flags


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/TicksRequest/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4TickRecordListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4TickRecordListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4TickRecordListApiResponse]:
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
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    flags: TickRequestFlags | Unset = UNSET,

) -> Response[MT4TickRecordListApiResponse]:
    """ Get historical ticks

     Historical ticks for a symbol over a date range.

    Manager (live) call returning a list of `MT4TickRecord` DTOs.
    `flags` controls whether raw and/or normalised ticks are
    included (defaults to `All`). Heavy endpoint — pair with
    `Idempotency-Key` for retry safety.

    Args:
        trade_platform (UUID):
        symbol (str):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        flags (TickRequestFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TickRecordListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
start=start,
end=end,
flags=flags,

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
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    flags: TickRequestFlags | Unset = UNSET,

) -> MT4TickRecordListApiResponse | None:
    """ Get historical ticks

     Historical ticks for a symbol over a date range.

    Manager (live) call returning a list of `MT4TickRecord` DTOs.
    `flags` controls whether raw and/or normalised ticks are
    included (defaults to `All`). Heavy endpoint — pair with
    `Idempotency-Key` for retry safety.

    Args:
        trade_platform (UUID):
        symbol (str):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        flags (TickRequestFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TickRecordListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
start=start,
end=end,
flags=flags,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    flags: TickRequestFlags | Unset = UNSET,

) -> Response[MT4TickRecordListApiResponse]:
    """ Get historical ticks

     Historical ticks for a symbol over a date range.

    Manager (live) call returning a list of `MT4TickRecord` DTOs.
    `flags` controls whether raw and/or normalised ticks are
    included (defaults to `All`). Heavy endpoint — pair with
    `Idempotency-Key` for retry safety.

    Args:
        trade_platform (UUID):
        symbol (str):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        flags (TickRequestFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TickRecordListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
start=start,
end=end,
flags=flags,

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
    start: datetime.datetime | Unset = UNSET,
    end: datetime.datetime | Unset = UNSET,
    flags: TickRequestFlags | Unset = UNSET,

) -> MT4TickRecordListApiResponse | None:
    """ Get historical ticks

     Historical ticks for a symbol over a date range.

    Manager (live) call returning a list of `MT4TickRecord` DTOs.
    `flags` controls whether raw and/or normalised ticks are
    included (defaults to `All`). Heavy endpoint — pair with
    `Idempotency-Key` for retry safety.

    Args:
        trade_platform (UUID):
        symbol (str):
        start (datetime.datetime | Unset):
        end (datetime.datetime | Unset):
        flags (TickRequestFlags | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TickRecordListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
start=start,
end=end,
flags=flags,

    )).parsed
