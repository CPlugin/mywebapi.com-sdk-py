from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_user_api_response import MT5UserApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    login: int,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/UserGet/{login}".format(trade_platform=quote(str(trade_platform), safe=""),login=quote(str(login), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5UserApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5UserApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5UserApiResponse]:
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

) -> Response[MT5UserApiResponse]:
    """ Get a user by login

    Args:
        trade_platform (UUID):
        login (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,

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

) -> MT5UserApiResponse | None:
    """ Get a user by login

    Args:
        trade_platform (UUID):
        login (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
login=login,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT5UserApiResponse]:
    """ Get a user by login

    Args:
        trade_platform (UUID):
        login (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,

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

) -> MT5UserApiResponse | None:
    """ Get a user by login

    Args:
        trade_platform (UUID):
        login (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
login=login,
client=client,

    )).parsed
