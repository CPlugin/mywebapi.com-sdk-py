from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.en_log_type import EnLogType
from ...models.mt4_server_log_list_api_response import MT4ServerLogListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    mode: EnLogType | Unset = UNSET,
    filter_: str | Unset = UNSET,
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

    json_mode: str | Unset = UNSET
    if not isinstance(mode, Unset):
        json_mode = mode.value

    params["mode"] = json_mode

    params["filter"] = filter_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/JournalRequest".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4ServerLogListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4ServerLogListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4ServerLogListApiResponse]:
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
    mode: EnLogType | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ServerLogListApiResponse]:
    """ Get server journal

     Server journal (log) entries for a date window.

    Manager (live) call — round-trips to MT4 server. Returns log entries
    in `[from, to]` range filtered by `mode` and an optional
    free-text `filter`. Defaults: `mode = Full`, `to = now`
    (server time).

    Heavier endpoint — large date windows return large arrays. Pair with
    reasonable `from`/`to` bounds; consider `Idempotency-Key`
    for retry safety on slow links.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        mode (EnLogType | Unset):
        filter_ (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ServerLogListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
to=to,
mode=mode,
filter_=filter_,
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
    mode: EnLogType | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ServerLogListApiResponse | None:
    """ Get server journal

     Server journal (log) entries for a date window.

    Manager (live) call — round-trips to MT4 server. Returns log entries
    in `[from, to]` range filtered by `mode` and an optional
    free-text `filter`. Defaults: `mode = Full`, `to = now`
    (server time).

    Heavier endpoint — large date windows return large arrays. Pair with
    reasonable `from`/`to` bounds; consider `Idempotency-Key`
    for retry safety on slow links.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        mode (EnLogType | Unset):
        filter_ (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ServerLogListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
to=to,
mode=mode,
filter_=filter_,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    mode: EnLogType | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ServerLogListApiResponse]:
    """ Get server journal

     Server journal (log) entries for a date window.

    Manager (live) call — round-trips to MT4 server. Returns log entries
    in `[from, to]` range filtered by `mode` and an optional
    free-text `filter`. Defaults: `mode = Full`, `to = now`
    (server time).

    Heavier endpoint — large date windows return large arrays. Pair with
    reasonable `from`/`to` bounds; consider `Idempotency-Key`
    for retry safety on slow links.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        mode (EnLogType | Unset):
        filter_ (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ServerLogListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
to=to,
mode=mode,
filter_=filter_,
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
    mode: EnLogType | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ServerLogListApiResponse | None:
    """ Get server journal

     Server journal (log) entries for a date window.

    Manager (live) call — round-trips to MT4 server. Returns log entries
    in `[from, to]` range filtered by `mode` and an optional
    free-text `filter`. Defaults: `mode = Full`, `to = now`
    (server time).

    Heavier endpoint — large date windows return large arrays. Pair with
    reasonable `from`/`to` bounds; consider `Idempotency-Key`
    for retry safety on slow links.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        mode (EnLogType | Unset):
        filter_ (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ServerLogListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
to=to,
mode=mode,
filter_=filter_,
x_request_timeout=x_request_timeout,

    )).parsed
