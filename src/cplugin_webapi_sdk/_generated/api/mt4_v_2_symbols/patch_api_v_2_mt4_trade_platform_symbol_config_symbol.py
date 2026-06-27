from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_symbol_config_api_response import MT4SymbolConfigApiResponse
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/MT4/{trade_platform}/SymbolConfig/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4SymbolConfigApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4SymbolConfigApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4SymbolConfigApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4SymbolConfigApiResponse]:
    """ Patch symbol config

     Type 2 mutator — partial update of a symbol configuration. Same flow as `UserRecordPatch`; reads
    existing config live, overlays the patch, writes back.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolConfigApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> MT4SymbolConfigApiResponse | None:
    """ Patch symbol config

     Type 2 mutator — partial update of a symbol configuration. Same flow as `UserRecordPatch`; reads
    existing config live, overlays the patch, writes back.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolConfigApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[MT4SymbolConfigApiResponse]:
    """ Patch symbol config

     Type 2 mutator — partial update of a symbol configuration. Same flow as `UserRecordPatch`; reads
    existing config live, overlays the patch, writes back.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolConfigApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> MT4SymbolConfigApiResponse | None:
    """ Patch symbol config

     Type 2 mutator — partial update of a symbol configuration. Same flow as `UserRecordPatch`; reads
    existing config live, overlays the patch, writes back.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolConfigApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,

    )).parsed
