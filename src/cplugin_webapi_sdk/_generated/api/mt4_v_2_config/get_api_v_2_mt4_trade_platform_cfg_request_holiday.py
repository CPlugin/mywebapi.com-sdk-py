from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_holiday_list_api_response import MT4HolidayListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/CfgRequestHoliday".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4HolidayListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4HolidayListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4HolidayListApiResponse]:
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
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4HolidayListApiResponse]:
    r""" List holiday config

     All holiday-calendar entries configured on the MT4 server, paginated.

    Manager-live read (round-trip). Holidays describe trading-suspension
    dates per symbol or symbol-group. Each entry carries date components
    (Year/Month/Day), a work-time window (From/To, minutes from midnight,
    both 0 for full closure), the affected Symbol (or \"All\"), a free-form
    Description, and an Enable flag. Ordering: by (Year, Month, Day, From,
    Symbol) ascending so cursors are stable and unique. The cursor is an
    opaque base64 string produced by CursorCodec from the composite
    \"{YYYYMMDD * 10000 + From:D14}|{Symbol}\" key — the Symbol tiebreaker
    covers the case where multiple holidays share date and From minute
    (per-symbol partial-day closures), guaranteeing pagination never drops
    rows even inside same-(date,From) clusters.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4HolidayListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,
x_request_timeout=x_request_timeout,

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
    x_request_timeout: float | Unset = UNSET,

) -> MT4HolidayListApiResponse | None:
    r""" List holiday config

     All holiday-calendar entries configured on the MT4 server, paginated.

    Manager-live read (round-trip). Holidays describe trading-suspension
    dates per symbol or symbol-group. Each entry carries date components
    (Year/Month/Day), a work-time window (From/To, minutes from midnight,
    both 0 for full closure), the affected Symbol (or \"All\"), a free-form
    Description, and an Enable flag. Ordering: by (Year, Month, Day, From,
    Symbol) ascending so cursors are stable and unique. The cursor is an
    opaque base64 string produced by CursorCodec from the composite
    \"{YYYYMMDD * 10000 + From:D14}|{Symbol}\" key — the Symbol tiebreaker
    covers the case where multiple holidays share date and From minute
    (per-symbol partial-day closures), guaranteeing pagination never drops
    rows even inside same-(date,From) clusters.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4HolidayListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4HolidayListApiResponse]:
    r""" List holiday config

     All holiday-calendar entries configured on the MT4 server, paginated.

    Manager-live read (round-trip). Holidays describe trading-suspension
    dates per symbol or symbol-group. Each entry carries date components
    (Year/Month/Day), a work-time window (From/To, minutes from midnight,
    both 0 for full closure), the affected Symbol (or \"All\"), a free-form
    Description, and an Enable flag. Ordering: by (Year, Month, Day, From,
    Symbol) ascending so cursors are stable and unique. The cursor is an
    opaque base64 string produced by CursorCodec from the composite
    \"{YYYYMMDD * 10000 + From:D14}|{Symbol}\" key — the Symbol tiebreaker
    covers the case where multiple holidays share date and From minute
    (per-symbol partial-day closures), guaranteeing pagination never drops
    rows even inside same-(date,From) clusters.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4HolidayListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,
x_request_timeout=x_request_timeout,

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
    x_request_timeout: float | Unset = UNSET,

) -> MT4HolidayListApiResponse | None:
    r""" List holiday config

     All holiday-calendar entries configured on the MT4 server, paginated.

    Manager-live read (round-trip). Holidays describe trading-suspension
    dates per symbol or symbol-group. Each entry carries date components
    (Year/Month/Day), a work-time window (From/To, minutes from midnight,
    both 0 for full closure), the affected Symbol (or \"All\"), a free-form
    Description, and an Enable flag. Ordering: by (Year, Month, Day, From,
    Symbol) ascending so cursors are stable and unique. The cursor is an
    opaque base64 string produced by CursorCodec from the composite
    \"{YYYYMMDD * 10000 + From:D14}|{Symbol}\" key — the Symbol tiebreaker
    covers the case where multiple holidays share date and From minute
    (per-symbol partial-day closures), guaranteeing pagination never drops
    rows even inside same-(date,From) clusters.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4HolidayListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,
x_request_timeout=x_request_timeout,

    )).parsed
