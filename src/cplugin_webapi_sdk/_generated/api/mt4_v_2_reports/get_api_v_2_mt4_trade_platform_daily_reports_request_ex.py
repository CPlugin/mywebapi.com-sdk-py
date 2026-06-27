from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.int_32mt4_daily_report_list_dictionary_api_response import Int32MT4DailyReportListDictionaryApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    logins: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_logins: list[int] | Unset = UNSET
    if not isinstance(logins, Unset):
        json_logins = logins


    params["logins"] = json_logins

    params["name"] = name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/DailyReportsRequestEx".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Int32MT4DailyReportListDictionaryApiResponse | None:
    if response.status_code == 200:
        response_200 = Int32MT4DailyReportListDictionaryApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Int32MT4DailyReportListDictionaryApiResponse]:
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    logins: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,

) -> Response[Int32MT4DailyReportListDictionaryApiResponse]:
    r""" Get daily reports (grouped)

     Same data set as `DailyReportsRequest`, but server-side grouped by login. Convenience shape for
    clients that pivot the data per-account (per-day rollups, account dashboards).

    Manager-live read — single round-trip to MT4 server, identical billing
    cost to `DailyReportsRequest`. The wrapper returns a sorted-list
    of sorted-lists (by login, then by date); the v2 envelope flattens
    the inner list to a chronologically-ordered `MT4DailyReport`
    array, leaving the outer keying by login.

    JSON shape: `{ \"817542\": [ ... ], \"1001\": [ ... ] }` — JSON
    object keys are strings, so int logins are stringified. Clients
    should parse keys back to int if needed.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        logins (list[int] | Unset):
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Int32MT4DailyReportListDictionaryApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
to=to,
logins=logins,
name=name,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    logins: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,

) -> Int32MT4DailyReportListDictionaryApiResponse | None:
    r""" Get daily reports (grouped)

     Same data set as `DailyReportsRequest`, but server-side grouped by login. Convenience shape for
    clients that pivot the data per-account (per-day rollups, account dashboards).

    Manager-live read — single round-trip to MT4 server, identical billing
    cost to `DailyReportsRequest`. The wrapper returns a sorted-list
    of sorted-lists (by login, then by date); the v2 envelope flattens
    the inner list to a chronologically-ordered `MT4DailyReport`
    array, leaving the outer keying by login.

    JSON shape: `{ \"817542\": [ ... ], \"1001\": [ ... ] }` — JSON
    object keys are strings, so int logins are stringified. Clients
    should parse keys back to int if needed.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        logins (list[int] | Unset):
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Int32MT4DailyReportListDictionaryApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
to=to,
logins=logins,
name=name,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    logins: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,

) -> Response[Int32MT4DailyReportListDictionaryApiResponse]:
    r""" Get daily reports (grouped)

     Same data set as `DailyReportsRequest`, but server-side grouped by login. Convenience shape for
    clients that pivot the data per-account (per-day rollups, account dashboards).

    Manager-live read — single round-trip to MT4 server, identical billing
    cost to `DailyReportsRequest`. The wrapper returns a sorted-list
    of sorted-lists (by login, then by date); the v2 envelope flattens
    the inner list to a chronologically-ordered `MT4DailyReport`
    array, leaving the outer keying by login.

    JSON shape: `{ \"817542\": [ ... ], \"1001\": [ ... ] }` — JSON
    object keys are strings, so int logins are stringified. Clients
    should parse keys back to int if needed.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        logins (list[int] | Unset):
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Int32MT4DailyReportListDictionaryApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
to=to,
logins=logins,
name=name,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    logins: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,

) -> Int32MT4DailyReportListDictionaryApiResponse | None:
    r""" Get daily reports (grouped)

     Same data set as `DailyReportsRequest`, but server-side grouped by login. Convenience shape for
    clients that pivot the data per-account (per-day rollups, account dashboards).

    Manager-live read — single round-trip to MT4 server, identical billing
    cost to `DailyReportsRequest`. The wrapper returns a sorted-list
    of sorted-lists (by login, then by date); the v2 envelope flattens
    the inner list to a chronologically-ordered `MT4DailyReport`
    array, leaving the outer keying by login.

    JSON shape: `{ \"817542\": [ ... ], \"1001\": [ ... ] }` — JSON
    object keys are strings, so int logins are stringified. Clients
    should parse keys back to int if needed.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        logins (list[int] | Unset):
        name (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Int32MT4DailyReportListDictionaryApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
to=to,
logins=logins,
name=name,

    )).parsed
