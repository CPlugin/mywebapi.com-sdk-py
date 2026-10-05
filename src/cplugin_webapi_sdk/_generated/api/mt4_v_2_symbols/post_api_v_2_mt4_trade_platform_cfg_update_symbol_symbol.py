from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_symbol_config_api_response import MT4SymbolConfigApiResponse
from ...models.mt4_symbol_config_update import MT4SymbolConfigUpdate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    body:    MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateSymbol/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }

    if isinstance(body, MT4SymbolConfigUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4SymbolConfigUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4SymbolConfigUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
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
    body:    MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4SymbolConfigApiResponse]:
    """ Update symbol config

     Update a symbol's full configuration — Type 1 mutator with secret-preservation read.

    Completes the User/Group/Symbol Type 1 mutator triad. Same flow as
    `UserRecordUpdate` and `GroupRecordUpdate`: read the existing
    `ConSymbol` from MT4 server, overlay the
    `MT4SymbolConfigUpdate` DTO over it, write the merged structure
    back. Preserves the `Sessions` nested array, reserved/unused
    padding, and server-derived fields (`Count`, `CountOriginal`,
    `FilterCounter`, `Point`, `Multiply`, tick-value pair)
    — those are `[MapperIgnoreTarget]`'d on the mapper.

    Idempotency-Key strongly recommended.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolConfigApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
body=body,
x_request_timeout=x_request_timeout,

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
    body:    MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4SymbolConfigApiResponse | None:
    """ Update symbol config

     Update a symbol's full configuration — Type 1 mutator with secret-preservation read.

    Completes the User/Group/Symbol Type 1 mutator triad. Same flow as
    `UserRecordUpdate` and `GroupRecordUpdate`: read the existing
    `ConSymbol` from MT4 server, overlay the
    `MT4SymbolConfigUpdate` DTO over it, write the merged structure
    back. Preserves the `Sessions` nested array, reserved/unused
    padding, and server-derived fields (`Count`, `CountOriginal`,
    `FilterCounter`, `Point`, `Multiply`, tick-value pair)
    — those are `[MapperIgnoreTarget]`'d on the mapper.

    Idempotency-Key strongly recommended.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.

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
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4SymbolConfigApiResponse]:
    """ Update symbol config

     Update a symbol's full configuration — Type 1 mutator with secret-preservation read.

    Completes the User/Group/Symbol Type 1 mutator triad. Same flow as
    `UserRecordUpdate` and `GroupRecordUpdate`: read the existing
    `ConSymbol` from MT4 server, overlay the
    `MT4SymbolConfigUpdate` DTO over it, write the merged structure
    back. Preserves the `Sessions` nested array, reserved/unused
    padding, and server-derived fields (`Count`, `CountOriginal`,
    `FilterCounter`, `Point`, `Multiply`, tick-value pair)
    — those are `[MapperIgnoreTarget]`'d on the mapper.

    Idempotency-Key strongly recommended.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolConfigApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
body=body,
x_request_timeout=x_request_timeout,

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
    body:    MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  |     MT4SymbolConfigUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4SymbolConfigApiResponse | None:
    """ Update symbol config

     Update a symbol's full configuration — Type 1 mutator with secret-preservation read.

    Completes the User/Group/Symbol Type 1 mutator triad. Same flow as
    `UserRecordUpdate` and `GroupRecordUpdate`: read the existing
    `ConSymbol` from MT4 server, overlay the
    `MT4SymbolConfigUpdate` DTO over it, write the merged structure
    back. Preserves the `Sessions` nested array, reserved/unused
    padding, and server-derived fields (`Count`, `CountOriginal`,
    `FilterCounter`, `Point`, `Multiply`, tick-value pair)
    — those are `[MapperIgnoreTarget]`'d on the mapper.

    Idempotency-Key strongly recommended.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.
        body (MT4SymbolConfigUpdate | Unset): Type 1 mutator input for `CfgUpdateSymbol`. Same
            field set as the read
            DTO MT4SymbolConfig minus:
              * `Symbol` (path parameter, immutable identity);
              * `Count`, `CountOriginal`, `FilterCounter` — server-side
                counters, derived;
              * Enum fields are submitted as their names.

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Symbol` identity.
              * `Sessions` nested array (own endpoint planned).
              * `Unused`, `ExternalUnused`, `ProfitReserved`,
                `FilterReserved` reserved arrays.
              * `Count`, `CountOriginal`, `FilterCounter`,
                `BidTickValue`, `AskTickValue`, `Point`, `Multiply`
                — server-derived from other fields, writing them is a no-op or
                overwrite-with-stale.

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
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
