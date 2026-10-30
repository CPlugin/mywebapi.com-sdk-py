from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    order: int,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/TradeClearRollback/{order}".format(trade_platform=quote(str(trade_platform), safe=""),order=quote(str(order), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BooleanApiResponse | None:
    if response.status_code == 200:
        response_200 = BooleanApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BooleanApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    order: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Roll back trade transaction

     Roll back an in-flight trade transaction by ticket.

    Pump-cached call. Cancels a pending trade transaction that the
    MT4 server is still holding in the rollback buffer (e.g. an
    instant-execution requote that has not yet been confirmed). Has
    no effect once the transaction has been committed; returns the
    the platform's `ResultCode` as part of the envelope on failure.

    Idempotent on already-committed/already-rolled-back tickets.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        order (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
order=order,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    order: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Roll back trade transaction

     Roll back an in-flight trade transaction by ticket.

    Pump-cached call. Cancels a pending trade transaction that the
    MT4 server is still holding in the rollback buffer (e.g. an
    instant-execution requote that has not yet been confirmed). Has
    no effect once the transaction has been committed; returns the
    the platform's `ResultCode` as part of the envelope on failure.

    Idempotent on already-committed/already-rolled-back tickets.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        order (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
order=order,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    order: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Roll back trade transaction

     Roll back an in-flight trade transaction by ticket.

    Pump-cached call. Cancels a pending trade transaction that the
    MT4 server is still holding in the rollback buffer (e.g. an
    instant-execution requote that has not yet been confirmed). Has
    no effect once the transaction has been committed; returns the
    the platform's `ResultCode` as part of the envelope on failure.

    Idempotent on already-committed/already-rolled-back tickets.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        order (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
order=order,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    order: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Roll back trade transaction

     Roll back an in-flight trade transaction by ticket.

    Pump-cached call. Cancels a pending trade transaction that the
    MT4 server is still holding in the rollback buffer (e.g. an
    instant-execution requote that has not yet been confirmed). Has
    no effect once the transaction has been committed; returns the
    the platform's `ResultCode` as part of the envelope on failure.

    Idempotent on already-committed/already-rolled-back tickets.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        order (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
order=order,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
