from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_symbol_change_request import MT4SymbolChangeRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/SymbolChange".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4SymbolChangeRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4SymbolChangeRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4SymbolChangeRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

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
    *,
    client: AuthenticatedClient | Client,
    body:    MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Change symbol attributes

     Adjusts the per-symbol trading attributes that dealers manage from the MT4 Manager UI — spread,
    stops-level, smoothing, quote color, execution mode.

    Manager-live POST. Maps 1:1 to the wrapper's `SymbolChange`
    call which marshals an entire `SymbolProperties` struct down
    to the native server. Only the seven editable fields are exposed
    on the v2 contract — the wrapper's 8-int reserved padding is
    filled with zeros by Mapperly automatically.

    This is intentionally separate from the heavier `CfgUpdateSymbol`
    Type 1 mutator: `SymbolChange` is the dealer-tier adjustment
    path; `CfgUpdateSymbol` changes structural symbol configuration
    (currency, calc mode, margin, swap) that requires admin privileges
    and broker-side coordination.

    Args:
        trade_platform (UUID):
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Change symbol attributes

     Adjusts the per-symbol trading attributes that dealers manage from the MT4 Manager UI — spread,
    stops-level, smoothing, quote color, execution mode.

    Manager-live POST. Maps 1:1 to the wrapper's `SymbolChange`
    call which marshals an entire `SymbolProperties` struct down
    to the native server. Only the seven editable fields are exposed
    on the v2 contract — the wrapper's 8-int reserved padding is
    filled with zeros by Mapperly automatically.

    This is intentionally separate from the heavier `CfgUpdateSymbol`
    Type 1 mutator: `SymbolChange` is the dealer-tier adjustment
    path; `CfgUpdateSymbol` changes structural symbol configuration
    (currency, calc mode, margin, swap) that requires admin privileges
    and broker-side coordination.

    Args:
        trade_platform (UUID):
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Change symbol attributes

     Adjusts the per-symbol trading attributes that dealers manage from the MT4 Manager UI — spread,
    stops-level, smoothing, quote color, execution mode.

    Manager-live POST. Maps 1:1 to the wrapper's `SymbolChange`
    call which marshals an entire `SymbolProperties` struct down
    to the native server. Only the seven editable fields are exposed
    on the v2 contract — the wrapper's 8-int reserved padding is
    filled with zeros by Mapperly automatically.

    This is intentionally separate from the heavier `CfgUpdateSymbol`
    Type 1 mutator: `SymbolChange` is the dealer-tier adjustment
    path; `CfgUpdateSymbol` changes structural symbol configuration
    (currency, calc mode, margin, swap) that requires admin privileges
    and broker-side coordination.

    Args:
        trade_platform (UUID):
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  |     MT4SymbolChangeRequest  | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Change symbol attributes

     Adjusts the per-symbol trading attributes that dealers manage from the MT4 Manager UI — spread,
    stops-level, smoothing, quote color, execution mode.

    Manager-live POST. Maps 1:1 to the wrapper's `SymbolChange`
    call which marshals an entire `SymbolProperties` struct down
    to the native server. Only the seven editable fields are exposed
    on the v2 contract — the wrapper's 8-int reserved padding is
    filled with zeros by Mapperly automatically.

    This is intentionally separate from the heavier `CfgUpdateSymbol`
    Type 1 mutator: `SymbolChange` is the dealer-tier adjustment
    path; `CfgUpdateSymbol` changes structural symbol configuration
    (currency, calc mode, margin, swap) that requires admin privileges
    and broker-side coordination.

    Args:
        trade_platform (UUID):
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.
        body (MT4SymbolChangeRequest | Unset): POST body for the Manager-live `SymbolChange`
            endpoint. Maps 1:1 to the
            wrapper's `SymbolProperties` struct (the public properties, not the
            underscore-prefixed backing fields). The struct's 8-int `Reserved`
            padding is dropped from the v2 contract.

            <br>Use cases: dealers and exchange operators adjusting per-symbol spread,
            stops level, smoothing, or quote-color metadata without touching the broader
            symbol configuration. Heavier write operations (currency, calc mode,
            margin, swap) live on the separate `CfgUpdateSymbol` Type 1 mutator.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,

    )).parsed
