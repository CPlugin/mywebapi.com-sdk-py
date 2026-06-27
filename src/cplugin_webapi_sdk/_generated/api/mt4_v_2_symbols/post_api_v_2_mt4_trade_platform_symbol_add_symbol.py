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
    symbol: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/SymbolAdd/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
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
    symbol: str,
    *,
    client: AuthenticatedClient | Client,

) -> Response[BooleanApiResponse]:
    """ Add symbol

     Add a symbol to the platform's active set — Type 1 mutator.

    Promotes a configured symbol into the platform's currently-pumping
    set so it starts receiving ticks and accepting orders. Reversible via
    `SymbolHide`.

    v1 exposes this as `GET /api/MT4/{tp}/SymbolAdd/{symbol}` — that
    is a historical REST violation (GET should be safe/idempotent). v2
    corrects the verb to POST without changing the wrapper behaviour. The
    path stays the same to keep traceability with the underlying wrapper
    method name; only the HTTP verb changes.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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

) -> BooleanApiResponse | None:
    """ Add symbol

     Add a symbol to the platform's active set — Type 1 mutator.

    Promotes a configured symbol into the platform's currently-pumping
    set so it starts receiving ticks and accepting orders. Reversible via
    `SymbolHide`.

    v1 exposes this as `GET /api/MT4/{tp}/SymbolAdd/{symbol}` — that
    is a historical REST violation (GET should be safe/idempotent). v2
    corrects the verb to POST without changing the wrapper behaviour. The
    path stays the same to keep traceability with the underlying wrapper
    method name; only the HTTP verb changes.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
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

) -> Response[BooleanApiResponse]:
    """ Add symbol

     Add a symbol to the platform's active set — Type 1 mutator.

    Promotes a configured symbol into the platform's currently-pumping
    set so it starts receiving ticks and accepting orders. Reversible via
    `SymbolHide`.

    v1 exposes this as `GET /api/MT4/{tp}/SymbolAdd/{symbol}` — that
    is a historical REST violation (GET should be safe/idempotent). v2
    corrects the verb to POST without changing the wrapper behaviour. The
    path stays the same to keep traceability with the underlying wrapper
    method name; only the HTTP verb changes.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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

) -> BooleanApiResponse | None:
    """ Add symbol

     Add a symbol to the platform's active set — Type 1 mutator.

    Promotes a configured symbol into the platform's currently-pumping
    set so it starts receiving ticks and accepting orders. Reversible via
    `SymbolHide`.

    v1 exposes this as `GET /api/MT4/{tp}/SymbolAdd/{symbol}` — that
    is a historical REST violation (GET should be safe/idempotent). v2
    corrects the verb to POST without changing the wrapper behaviour. The
    path stays the same to keep traceability with the underlying wrapper
    method name; only the HTTP verb changes.

    Args:
        trade_platform (UUID):
        symbol (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,

    )).parsed
