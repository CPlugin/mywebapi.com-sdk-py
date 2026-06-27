from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    key: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/NewsBodyRequest/{key}".format(trade_platform=quote(str(trade_platform), safe=""),key=quote(str(key), safe=""),),
    }


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

) -> Response[BooleanApiResponse]:
    r""" Request news body fetch

     Ask the pump to fetch the body for the given news key (fire-and-forget).

    POST because this is a side-effect on the pump (it queues a fetch).
    The wrapper method returns `void` — there is no synchronous
    success/failure to surface. A subsequent `NewsBodyGet(key)` will
    see the body once the pump has retrieved it. The payload is a sentinel
    `true` meaning \"request dispatched\".

    Args:
        trade_platform (UUID):
        key (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
key=key,

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

) -> BooleanApiResponse | None:
    r""" Request news body fetch

     Ask the pump to fetch the body for the given news key (fire-and-forget).

    POST because this is a side-effect on the pump (it queues a fetch).
    The wrapper method returns `void` — there is no synchronous
    success/failure to surface. A subsequent `NewsBodyGet(key)` will
    see the body once the pump has retrieved it. The payload is a sentinel
    `true` meaning \"request dispatched\".

    Args:
        trade_platform (UUID):
        key (int):

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

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    key: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[BooleanApiResponse]:
    r""" Request news body fetch

     Ask the pump to fetch the body for the given news key (fire-and-forget).

    POST because this is a side-effect on the pump (it queues a fetch).
    The wrapper method returns `void` — there is no synchronous
    success/failure to surface. A subsequent `NewsBodyGet(key)` will
    see the body once the pump has retrieved it. The payload is a sentinel
    `true` meaning \"request dispatched\".

    Args:
        trade_platform (UUID):
        key (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
key=key,

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

) -> BooleanApiResponse | None:
    r""" Request news body fetch

     Ask the pump to fetch the body for the given news key (fire-and-forget).

    POST because this is a side-effect on the pump (it queues a fetch).
    The wrapper method returns `void` — there is no synchronous
    success/failure to surface. A subsequent `NewsBodyGet(key)` will
    see the body once the pump has retrieved it. The payload is a sentinel
    `true` meaning \"request dispatched\".

    Args:
        trade_platform (UUID):
        key (int):

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

    )).parsed
