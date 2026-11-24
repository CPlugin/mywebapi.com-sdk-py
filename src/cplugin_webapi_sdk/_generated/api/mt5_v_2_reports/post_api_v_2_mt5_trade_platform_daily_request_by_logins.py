from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_daily_list_api_response import MT5DailyListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["from"] = from_

    params["to"] = to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/DailyRequestByLogins".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }

    if isinstance(body, list[int]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body



        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, list[int]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body



        headers["Content-Type"] = "application/json"
    if isinstance(body, list[int]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body



        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5DailyListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5DailyListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5DailyListApiResponse]:
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
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5DailyListApiResponse]:
    """ Daily reports of several accounts

     Returns the daily reports of the listed accounts for the requested period, with the
    positions and pending orders open at the end of each day. The logins travel in the request
    body; a request without logins is rejected as invalid input. Times are seconds since
    01.01.1970 as the trade server counts them.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):
        to (int | Unset):
        x_request_timeout (float | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5DailyListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
from_=from_,
to=to,
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
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5DailyListApiResponse | None:
    """ Daily reports of several accounts

     Returns the daily reports of the listed accounts for the requested period, with the
    positions and pending orders open at the end of each day. The logins travel in the request
    body; a request without logins is rejected as invalid input. Times are seconds since
    01.01.1970 as the trade server counts them.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):
        to (int | Unset):
        x_request_timeout (float | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5DailyListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5DailyListApiResponse]:
    """ Daily reports of several accounts

     Returns the daily reports of the listed accounts for the requested period, with the
    positions and pending orders open at the end of each day. The logins travel in the request
    body; a request without logins is rejected as invalid input. Times are seconds since
    01.01.1970 as the trade server counts them.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):
        to (int | Unset):
        x_request_timeout (float | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5DailyListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
from_=from_,
to=to,
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
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5DailyListApiResponse | None:
    """ Daily reports of several accounts

     Returns the daily reports of the listed accounts for the requested period, with the
    positions and pending orders open at the end of each day. The logins travel in the request
    body; a request without logins is rejected as invalid input. Times are seconds since
    01.01.1970 as the trade server counts them.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):
        to (int | Unset):
        x_request_timeout (float | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5DailyListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )).parsed
