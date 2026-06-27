from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_symbol_group import MT4SymbolGroup
from ...models.mt4_symbol_group_api_response import MT4SymbolGroupApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    pos: int,
    *,
    body:    MT4SymbolGroup  |     MT4SymbolGroup  |     MT4SymbolGroup  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateSymbolGroup/{pos}".format(trade_platform=quote(str(trade_platform), safe=""),pos=quote(str(pos), safe=""),),
    }

    if isinstance(body, MT4SymbolGroup):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4SymbolGroup):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4SymbolGroup):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4SymbolGroupApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4SymbolGroupApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4SymbolGroupApiResponse]:
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
    body:    MT4SymbolGroup  |     MT4SymbolGroup  |     MT4SymbolGroup  | Unset = UNSET,

) -> Response[MT4SymbolGroupApiResponse]:
    """ Update symbol group

     Update a symbol group at a given list position — Type 1 mutator.

    Position-based read-modify-write. `ConSymbolGroup` has no
    reserved padding or internal pointers, so the overlay is trivial.

    Args:
        trade_platform (UUID):
        pos (int):
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolGroupApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
body=body,

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
    body:    MT4SymbolGroup  |     MT4SymbolGroup  |     MT4SymbolGroup  | Unset = UNSET,

) -> MT4SymbolGroupApiResponse | None:
    """ Update symbol group

     Update a symbol group at a given list position — Type 1 mutator.

    Position-based read-modify-write. `ConSymbolGroup` has no
    reserved padding or internal pointers, so the overlay is trivial.

    Args:
        trade_platform (UUID):
        pos (int):
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolGroupApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4SymbolGroup  |     MT4SymbolGroup  |     MT4SymbolGroup  | Unset = UNSET,

) -> Response[MT4SymbolGroupApiResponse]:
    """ Update symbol group

     Update a symbol group at a given list position — Type 1 mutator.

    Position-based read-modify-write. `ConSymbolGroup` has no
    reserved padding or internal pointers, so the overlay is trivial.

    Args:
        trade_platform (UUID):
        pos (int):
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolGroupApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
body=body,

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
    body:    MT4SymbolGroup  |     MT4SymbolGroup  |     MT4SymbolGroup  | Unset = UNSET,

) -> MT4SymbolGroupApiResponse | None:
    """ Update symbol group

     Update a symbol group at a given list position — Type 1 mutator.

    Position-based read-modify-write. `ConSymbolGroup` has no
    reserved padding or internal pointers, so the overlay is trivial.

    Args:
        trade_platform (UUID):
        pos (int):
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.
        body (MT4SymbolGroup | Unset): v2 DTO describing a single MT4 symbol group (security
            category).
            Mirrors the wrapper's ConSymbolGroup — which only carries Name and
            Description as fixed-size ANSI fields. There is no ProfitCurrency on
            the MT4-side group struct (that lives on per-symbol settings, not on
            the group level), so the DTO faithfully exposes only what exists.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolGroupApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
body=body,

    )).parsed
