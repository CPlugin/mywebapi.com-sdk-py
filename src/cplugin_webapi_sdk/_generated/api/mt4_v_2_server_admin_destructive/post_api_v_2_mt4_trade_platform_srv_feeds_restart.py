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
    *,
    confirm: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["confirm"] = confirm


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/SrvFeedsRestart".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
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
    *,
    client: AuthenticatedClient | Client,
    confirm: bool | Unset = False,

) -> Response[BooleanApiResponse]:
    """ Restart data feeders

     Restart all running data feeders. Destructive — requires `?confirm=true`.

    Manager (live) call to the wrapper's `SrvFeedsRestart()`.
    Cycles all running quote/news feeders. May cause a brief gap in
    the tick stream — typically a second or two. Idempotent.

    Args:
        trade_platform (UUID):
        confirm (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
confirm=confirm,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    confirm: bool | Unset = False,

) -> BooleanApiResponse | None:
    """ Restart data feeders

     Restart all running data feeders. Destructive — requires `?confirm=true`.

    Manager (live) call to the wrapper's `SrvFeedsRestart()`.
    Cycles all running quote/news feeders. May cause a brief gap in
    the tick stream — typically a second or two. Idempotent.

    Args:
        trade_platform (UUID):
        confirm (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
confirm=confirm,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    confirm: bool | Unset = False,

) -> Response[BooleanApiResponse]:
    """ Restart data feeders

     Restart all running data feeders. Destructive — requires `?confirm=true`.

    Manager (live) call to the wrapper's `SrvFeedsRestart()`.
    Cycles all running quote/news feeders. May cause a brief gap in
    the tick stream — typically a second or two. Idempotent.

    Args:
        trade_platform (UUID):
        confirm (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
confirm=confirm,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    confirm: bool | Unset = False,

) -> BooleanApiResponse | None:
    """ Restart data feeders

     Restart all running data feeders. Destructive — requires `?confirm=true`.

    Manager (live) call to the wrapper's `SrvFeedsRestart()`.
    Cycles all running quote/news feeders. May cause a brief gap in
    the tick stream — typically a second or two. Idempotent.

    Args:
        trade_platform (UUID):
        confirm (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
confirm=confirm,

    )).parsed
