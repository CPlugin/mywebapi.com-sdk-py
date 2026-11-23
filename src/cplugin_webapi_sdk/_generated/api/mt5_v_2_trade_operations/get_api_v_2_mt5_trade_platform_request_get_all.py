from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_request_list_api_response import MT5RequestListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    from_: int | Unset = 0,
    count: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["from"] = from_

    params["count"] = count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/RequestGetAll".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5RequestListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5RequestListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5RequestListApiResponse]:
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
    from_: int | Unset = 0,
    count: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5RequestListApiResponse]:
    """ List the trade requests waiting in the queue

     <br>
                Returns the requests waiting in the queue as one list, in the order the trade server
                keeps them. Reading does not take a request for processing and does not change the
                queue; requests already taken by a dealer are not part of the list.

    <br>
                The whole queue is read at once and then trimmed to the requested window: `from`
                skips that many requests from the head, `count` limits how many are returned, and
                the default of both returns everything. The queue is live, so a repeated call may see a
                different set. The queue must be opened with `DealerStart` first.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):  Default: 0.
        count (int | Unset):  Default: 0.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5RequestListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
count=count,
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
    from_: int | Unset = 0,
    count: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> MT5RequestListApiResponse | None:
    """ List the trade requests waiting in the queue

     <br>
                Returns the requests waiting in the queue as one list, in the order the trade server
                keeps them. Reading does not take a request for processing and does not change the
                queue; requests already taken by a dealer are not part of the list.

    <br>
                The whole queue is read at once and then trimmed to the requested window: `from`
                skips that many requests from the head, `count` limits how many are returned, and
                the default of both returns everything. The queue is live, so a repeated call may see a
                different set. The queue must be opened with `DealerStart` first.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):  Default: 0.
        count (int | Unset):  Default: 0.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5RequestListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
count=count,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: int | Unset = 0,
    count: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5RequestListApiResponse]:
    """ List the trade requests waiting in the queue

     <br>
                Returns the requests waiting in the queue as one list, in the order the trade server
                keeps them. Reading does not take a request for processing and does not change the
                queue; requests already taken by a dealer are not part of the list.

    <br>
                The whole queue is read at once and then trimmed to the requested window: `from`
                skips that many requests from the head, `count` limits how many are returned, and
                the default of both returns everything. The queue is live, so a repeated call may see a
                different set. The queue must be opened with `DealerStart` first.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):  Default: 0.
        count (int | Unset):  Default: 0.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5RequestListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
count=count,
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
    from_: int | Unset = 0,
    count: int | Unset = 0,
    x_request_timeout: float | Unset = UNSET,

) -> MT5RequestListApiResponse | None:
    """ List the trade requests waiting in the queue

     <br>
                Returns the requests waiting in the queue as one list, in the order the trade server
                keeps them. Reading does not take a request for processing and does not change the
                queue; requests already taken by a dealer are not part of the list.

    <br>
                The whole queue is read at once and then trimmed to the requested window: `from`
                skips that many requests from the head, `count` limits how many are returned, and
                the default of both returns everything. The queue is live, so a repeated call may see a
                different set. The queue must be opened with `DealerStart` first.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):  Default: 0.
        count (int | Unset):  Default: 0.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5RequestListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
count=count,
x_request_timeout=x_request_timeout,

    )).parsed
