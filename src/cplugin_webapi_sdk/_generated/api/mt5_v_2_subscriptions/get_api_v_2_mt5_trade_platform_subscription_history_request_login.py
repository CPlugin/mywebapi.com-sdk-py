from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_subscription_history_list_api_response import MT5SubscriptionHistoryListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    login: int,
    *,
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
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/SubscriptionHistoryRequest/{login}".format(trade_platform=quote(str(trade_platform), safe=""),login=quote(str(login), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5SubscriptionHistoryListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5SubscriptionHistoryListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5SubscriptionHistoryListApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SubscriptionHistoryListApiResponse]:
    """ Subscription actions of an account for a period

     Returns every action performed with the subscriptions of the account inside the given
    time range: joins, renewals, cancellations and edits, each with the payment it carried.
    Both bounds are seconds since 1970-01-01 and are inclusive; the range is required.
    The result is not paginated.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        login (int):
        from_ (int | Unset):
        to (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SubscriptionHistoryListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
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
    login: int,
    *,
    client: AuthenticatedClient | Client,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SubscriptionHistoryListApiResponse | None:
    """ Subscription actions of an account for a period

     Returns every action performed with the subscriptions of the account inside the given
    time range: joins, renewals, cancellations and edits, each with the payment it carried.
    Both bounds are seconds since 1970-01-01 and are inclusive; the range is required.
    The result is not paginated.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        login (int):
        from_ (int | Unset):
        to (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SubscriptionHistoryListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SubscriptionHistoryListApiResponse]:
    """ Subscription actions of an account for a period

     Returns every action performed with the subscriptions of the account inside the given
    time range: joins, renewals, cancellations and edits, each with the payment it carried.
    Both bounds are seconds since 1970-01-01 and are inclusive; the range is required.
    The result is not paginated.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        login (int):
        from_ (int | Unset):
        to (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SubscriptionHistoryListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
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
    login: int,
    *,
    client: AuthenticatedClient | Client,
    from_: int | Unset = UNSET,
    to: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SubscriptionHistoryListApiResponse | None:
    """ Subscription actions of an account for a period

     Returns every action performed with the subscriptions of the account inside the given
    time range: joins, renewals, cancellations and edits, each with the payment it carried.
    Both bounds are seconds since 1970-01-01 and are inclusive; the range is required.
    The result is not paginated.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        login (int):
        from_ (int | Unset):
        to (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SubscriptionHistoryListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )).parsed
