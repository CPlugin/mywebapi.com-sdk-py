from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_daily_report_list_api_response import MT4DailyReportListApiResponse
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

    json_logins: list[int] | Unset = UNSET
    if not isinstance(logins, Unset):
        json_logins = logins


    params["logins"] = json_logins

    params["name"] = name


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/DailyReportsRequest".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4DailyReportListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4DailyReportListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4DailyReportListApiResponse]:
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
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4DailyReportListApiResponse]:
    r""" Get daily reports

     End-of-day balance/equity/PnL snapshots for a batch of account logins within a date window — the
    broker daily-report data set, flat shape (one row per (login, day) pair).

    Manager-live read (round-trip to MT4 server). Pass logins as repeated
    query parameters: `?logins=1001&logins=1002&logins=1003`.
    Server-side billing counts this as one Manager request regardless of
    batch size — prefer one batched call over a per-login loop.

    Each row carries its own `Login` field, so the flat shape is
    joinable on the client side. The MT4 server returns dates in its
    local time zone, **not** UTC — clients should treat `Ctm` as
    \"broker day boundary\" and convert as appropriate.

    Note: the platform warns that asking for a window where the manager
    account lacks the `Automatic server reports` permission may
    cause MT4 to drop the manager connection. The API-side
    `ResourceAccess` check is an indirect guard; a broker that
    mis-configured the underlying manager rights can still observe
    transient connection bounces.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        logins (list[int] | Unset):
        name (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4DailyReportListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
to=to,
logins=logins,
name=name,
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    logins: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4DailyReportListApiResponse | None:
    r""" Get daily reports

     End-of-day balance/equity/PnL snapshots for a batch of account logins within a date window — the
    broker daily-report data set, flat shape (one row per (login, day) pair).

    Manager-live read (round-trip to MT4 server). Pass logins as repeated
    query parameters: `?logins=1001&logins=1002&logins=1003`.
    Server-side billing counts this as one Manager request regardless of
    batch size — prefer one batched call over a per-login loop.

    Each row carries its own `Login` field, so the flat shape is
    joinable on the client side. The MT4 server returns dates in its
    local time zone, **not** UTC — clients should treat `Ctm` as
    \"broker day boundary\" and convert as appropriate.

    Note: the platform warns that asking for a window where the manager
    account lacks the `Automatic server reports` permission may
    cause MT4 to drop the manager connection. The API-side
    `ResourceAccess` check is an indirect guard; a broker that
    mis-configured the underlying manager rights can still observe
    transient connection bounces.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        logins (list[int] | Unset):
        name (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4DailyReportListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
to=to,
logins=logins,
name=name,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    logins: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4DailyReportListApiResponse]:
    r""" Get daily reports

     End-of-day balance/equity/PnL snapshots for a batch of account logins within a date window — the
    broker daily-report data set, flat shape (one row per (login, day) pair).

    Manager-live read (round-trip to MT4 server). Pass logins as repeated
    query parameters: `?logins=1001&logins=1002&logins=1003`.
    Server-side billing counts this as one Manager request regardless of
    batch size — prefer one batched call over a per-login loop.

    Each row carries its own `Login` field, so the flat shape is
    joinable on the client side. The MT4 server returns dates in its
    local time zone, **not** UTC — clients should treat `Ctm` as
    \"broker day boundary\" and convert as appropriate.

    Note: the platform warns that asking for a window where the manager
    account lacks the `Automatic server reports` permission may
    cause MT4 to drop the manager connection. The API-side
    `ResourceAccess` check is an indirect guard; a broker that
    mis-configured the underlying manager rights can still observe
    transient connection bounces.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        logins (list[int] | Unset):
        name (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4DailyReportListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
to=to,
logins=logins,
name=name,
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
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    logins: list[int] | Unset = UNSET,
    name: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4DailyReportListApiResponse | None:
    r""" Get daily reports

     End-of-day balance/equity/PnL snapshots for a batch of account logins within a date window — the
    broker daily-report data set, flat shape (one row per (login, day) pair).

    Manager-live read (round-trip to MT4 server). Pass logins as repeated
    query parameters: `?logins=1001&logins=1002&logins=1003`.
    Server-side billing counts this as one Manager request regardless of
    batch size — prefer one batched call over a per-login loop.

    Each row carries its own `Login` field, so the flat shape is
    joinable on the client side. The MT4 server returns dates in its
    local time zone, **not** UTC — clients should treat `Ctm` as
    \"broker day boundary\" and convert as appropriate.

    Note: the platform warns that asking for a window where the manager
    account lacks the `Automatic server reports` permission may
    cause MT4 to drop the manager connection. The API-side
    `ResourceAccess` check is an indirect guard; a broker that
    mis-configured the underlying manager rights can still observe
    transient connection bounces.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        logins (list[int] | Unset):
        name (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4DailyReportListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
to=to,
logins=logins,
name=name,
x_request_timeout=x_request_timeout,

    )).parsed
