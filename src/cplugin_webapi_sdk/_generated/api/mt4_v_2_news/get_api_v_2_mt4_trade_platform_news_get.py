from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_news_topic_list_api_response import MT4NewsTopicListApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/NewsGet".format(trade_platform=quote(str(trade_platform), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4NewsTopicListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4NewsTopicListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4NewsTopicListApiResponse]:
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

) -> Response[MT4NewsTopicListApiResponse]:
    """ List news headers

     All cached news topic headers (no body — fetch separately).

    Pump-cached read — returns the full news topic table held by the
    pumping connection. Each entry is a header (Key, Time, Topic,
    Category, Keywords, Priority, LangId). Body text is fetched via
    `NewsBodyGet(key)` after asking the pump to populate it via
    `NewsBodyRequest(key)`.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4NewsTopicListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> MT4NewsTopicListApiResponse | None:
    """ List news headers

     All cached news topic headers (no body — fetch separately).

    Pump-cached read — returns the full news topic table held by the
    pumping connection. Each entry is a header (Key, Time, Topic,
    Category, Keywords, Priority, LangId). Body text is fetched via
    `NewsBodyGet(key)` after asking the pump to populate it via
    `NewsBodyRequest(key)`.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4NewsTopicListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4NewsTopicListApiResponse]:
    """ List news headers

     All cached news topic headers (no body — fetch separately).

    Pump-cached read — returns the full news topic table held by the
    pumping connection. Each entry is a header (Key, Time, Topic,
    Category, Keywords, Priority, LangId). Body text is fetched via
    `NewsBodyGet(key)` after asking the pump to populate it via
    `NewsBodyRequest(key)`.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4NewsTopicListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,

) -> MT4NewsTopicListApiResponse | None:
    """ List news headers

     All cached news topic headers (no body — fetch separately).

    Pump-cached read — returns the full news topic table held by the
    pumping connection. Each entry is a header (Key, Time, Topic,
    Category, Keywords, Priority, LangId). Body text is fetched via
    `NewsBodyGet(key)` after asking the pump to populate it via
    `NewsBodyRequest(key)`.

    Args:
        trade_platform (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4NewsTopicListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,

    )).parsed
