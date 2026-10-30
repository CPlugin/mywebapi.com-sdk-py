from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_news_topic_api_response import MT4NewsTopicApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    pos: int,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/NewsTopicGet/{pos}".format(trade_platform=quote(str(trade_platform), safe=""),pos=quote(str(pos), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4NewsTopicApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4NewsTopicApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4NewsTopicApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4NewsTopicApiResponse]:
    """ Get news header by index

     Single cached news topic header by zero-based index.

    Pump-cached read — useful for paginating news without re-marshalling
    the whole array. Pair with `NewsTotal` to bound the index.
    Returns a platform-failure envelope when pos is
    out of range.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4NewsTopicApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT4NewsTopicApiResponse | None:
    """ Get news header by index

     Single cached news topic header by zero-based index.

    Pump-cached read — useful for paginating news without re-marshalling
    the whole array. Pair with `NewsTotal` to bound the index.
    Returns a platform-failure envelope when pos is
    out of range.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4NewsTopicApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4NewsTopicApiResponse]:
    """ Get news header by index

     Single cached news topic header by zero-based index.

    Pump-cached read — useful for paginating news without re-marshalling
    the whole array. Pair with `NewsTotal` to bound the index.
    Returns a platform-failure envelope when pos is
    out of range.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4NewsTopicApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT4NewsTopicApiResponse | None:
    """ Get news header by index

     Single cached news topic header by zero-based index.

    Pump-cached read — useful for paginating news without re-marshalling
    the whole array. Pair with `NewsTotal` to bound the index.
    Returns a platform-failure envelope when pos is
    out of range.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4NewsTopicApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
