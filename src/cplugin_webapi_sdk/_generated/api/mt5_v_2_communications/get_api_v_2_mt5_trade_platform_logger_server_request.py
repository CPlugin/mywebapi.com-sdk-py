from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_log_record_list_api_response import MT5LogRecordListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    mode: int | Unset = UNSET,
    type_: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["mode"] = mode

    params["type"] = type_

    params["from"] = from_

    params["to"] = to

    params["filter"] = filter_


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/LoggerServerRequest".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5LogRecordListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5LogRecordListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5LogRecordListApiResponse]:
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
    mode: int | Unset = UNSET,
    type_: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5LogRecordListApiResponse]:
    """ Read the journal of the trade server

     Returns the entries of the chosen kind in the given time window, newest and oldest included.
    The window is given in seconds elapsed since 01.01.1970; the optional keyword narrows the
    entries the way the journal search of the platform does.

    <br>`mode` accepts 0 (standard entries), 1 (errors only) or 2 (full journal); `type`
    accepts 0 (all events), 1–8 (configuration, system, network, history, users, trades, API
    calls, notifications) or 16–17 (live update, outgoing mail). Any other value is refused.


    The whole window is returned in one answer, so a wide window over a busy server is a large
    response.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        mode (int | Unset):
        type_ (int | Unset):
        from_ (int | Unset):
        to (int | Unset):
        filter_ (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5LogRecordListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
mode=mode,
type_=type_,
from_=from_,
to=to,
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
    mode: int | Unset = UNSET,
    type_: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5LogRecordListApiResponse | None:
    """ Read the journal of the trade server

     Returns the entries of the chosen kind in the given time window, newest and oldest included.
    The window is given in seconds elapsed since 01.01.1970; the optional keyword narrows the
    entries the way the journal search of the platform does.

    <br>`mode` accepts 0 (standard entries), 1 (errors only) or 2 (full journal); `type`
    accepts 0 (all events), 1–8 (configuration, system, network, history, users, trades, API
    calls, notifications) or 16–17 (live update, outgoing mail). Any other value is refused.


    The whole window is returned in one answer, so a wide window over a busy server is a large
    response.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        mode (int | Unset):
        type_ (int | Unset):
        from_ (int | Unset):
        to (int | Unset):
        filter_ (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5LogRecordListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
mode=mode,
type_=type_,
from_=from_,
to=to,
filter_=filter_,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    mode: int | Unset = UNSET,
    type_: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5LogRecordListApiResponse]:
    """ Read the journal of the trade server

     Returns the entries of the chosen kind in the given time window, newest and oldest included.
    The window is given in seconds elapsed since 01.01.1970; the optional keyword narrows the
    entries the way the journal search of the platform does.

    <br>`mode` accepts 0 (standard entries), 1 (errors only) or 2 (full journal); `type`
    accepts 0 (all events), 1–8 (configuration, system, network, history, users, trades, API
    calls, notifications) or 16–17 (live update, outgoing mail). Any other value is refused.


    The whole window is returned in one answer, so a wide window over a busy server is a large
    response.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        mode (int | Unset):
        type_ (int | Unset):
        from_ (int | Unset):
        to (int | Unset):
        filter_ (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5LogRecordListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
mode=mode,
type_=type_,
from_=from_,
to=to,
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
    mode: int | Unset = UNSET,
    type_: int | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    filter_: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5LogRecordListApiResponse | None:
    """ Read the journal of the trade server

     Returns the entries of the chosen kind in the given time window, newest and oldest included.
    The window is given in seconds elapsed since 01.01.1970; the optional keyword narrows the
    entries the way the journal search of the platform does.

    <br>`mode` accepts 0 (standard entries), 1 (errors only) or 2 (full journal); `type`
    accepts 0 (all events), 1–8 (configuration, system, network, history, users, trades, API
    calls, notifications) or 16–17 (live update, outgoing mail). Any other value is refused.


    The whole window is returned in one answer, so a wide window over a busy server is a large
    response.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        mode (int | Unset):
        type_ (int | Unset):
        from_ (int | Unset):
        to (int | Unset):
        filter_ (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5LogRecordListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
mode=mode,
type_=type_,
from_=from_,
to=to,
filter_=filter_,
x_request_timeout=x_request_timeout,

    )).parsed
