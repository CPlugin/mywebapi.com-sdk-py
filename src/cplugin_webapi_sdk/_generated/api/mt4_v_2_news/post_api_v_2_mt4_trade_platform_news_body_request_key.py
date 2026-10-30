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
    key: int,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/NewsBodyRequest/{key}".format(trade_platform=quote(str(trade_platform), safe=""),key=quote(str(key), safe=""),),
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
    key: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Request news body fetch

     Ask the pump to fetch the body for the given news key (fire-and-forget).

    POST because this is a side-effect on the pump (it queues a fetch).
    The platform method returns `void` — there is no synchronous
    success/failure to surface. A subsequent `NewsBodyGet(key)` will
    see the body once the pump has retrieved it. The payload is a sentinel
    `true` meaning \"request dispatched\".

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        key (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
key=key,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    key: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Request news body fetch

     Ask the pump to fetch the body for the given news key (fire-and-forget).

    POST because this is a side-effect on the pump (it queues a fetch).
    The platform method returns `void` — there is no synchronous
    success/failure to surface. A subsequent `NewsBodyGet(key)` will
    see the body once the pump has retrieved it. The payload is a sentinel
    `true` meaning \"request dispatched\".

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        key (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
key=key,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    key: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Request news body fetch

     Ask the pump to fetch the body for the given news key (fire-and-forget).

    POST because this is a side-effect on the pump (it queues a fetch).
    The platform method returns `void` — there is no synchronous
    success/failure to surface. A subsequent `NewsBodyGet(key)` will
    see the body once the pump has retrieved it. The payload is a sentinel
    `true` meaning \"request dispatched\".

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        key (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
key=key,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    key: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Request news body fetch

     Ask the pump to fetch the body for the given news key (fire-and-forget).

    POST because this is a side-effect on the pump (it queues a fetch).
    The platform method returns `void` — there is no synchronous
    success/failure to surface. A subsequent `NewsBodyGet(key)` will
    see the body once the pump has retrieved it. The payload is a sentinel
    `true` meaning \"request dispatched\".

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        key (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
key=key,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
