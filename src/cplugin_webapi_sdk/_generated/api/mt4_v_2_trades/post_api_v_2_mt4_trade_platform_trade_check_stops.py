from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_trade_transaction import MT4TradeTransaction
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4TradeTransaction  |     MT4TradeTransaction  |     MT4TradeTransaction  | Unset = UNSET,
    price: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["price"] = price


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/TradeCheckStops".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }

    if isinstance(body, MT4TradeTransaction):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4TradeTransaction):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4TradeTransaction):
        
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
    body:    MT4TradeTransaction  |     MT4TradeTransaction  |     MT4TradeTransaction  | Unset = UNSET,
    price: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Validate order stops

     Validate an order's SL/TP/pending-open levels against the symbol's administrator-set `stops_level`.

    Pump-cached call. The MT4 server verifies that the supplied SL/TP
    (and, for pending orders, the open price) sit at least
    `stops_level` away from the current market and that pending
    expiration is at least ten minutes in the future. Returns a bare
    boolean envelope: `true` when the wrapper's `ResultCode`
    is `Ok`.

    Useful for client-side pre-flight before submitting a real
    `TradeTransaction` — saves a server round-trip for invalid
    orders.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        price (float | Unset):
        x_request_timeout (float | Unset):
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
price=price,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeTransaction  |     MT4TradeTransaction  |     MT4TradeTransaction  | Unset = UNSET,
    price: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Validate order stops

     Validate an order's SL/TP/pending-open levels against the symbol's administrator-set `stops_level`.

    Pump-cached call. The MT4 server verifies that the supplied SL/TP
    (and, for pending orders, the open price) sit at least
    `stops_level` away from the current market and that pending
    expiration is at least ten minutes in the future. Returns a bare
    boolean envelope: `true` when the wrapper's `ResultCode`
    is `Ok`.

    Useful for client-side pre-flight before submitting a real
    `TradeTransaction` — saves a server round-trip for invalid
    orders.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        price (float | Unset):
        x_request_timeout (float | Unset):
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.

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
price=price,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeTransaction  |     MT4TradeTransaction  |     MT4TradeTransaction  | Unset = UNSET,
    price: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Validate order stops

     Validate an order's SL/TP/pending-open levels against the symbol's administrator-set `stops_level`.

    Pump-cached call. The MT4 server verifies that the supplied SL/TP
    (and, for pending orders, the open price) sit at least
    `stops_level` away from the current market and that pending
    expiration is at least ten minutes in the future. Returns a bare
    boolean envelope: `true` when the wrapper's `ResultCode`
    is `Ok`.

    Useful for client-side pre-flight before submitting a real
    `TradeTransaction` — saves a server round-trip for invalid
    orders.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        price (float | Unset):
        x_request_timeout (float | Unset):
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
price=price,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeTransaction  |     MT4TradeTransaction  |     MT4TradeTransaction  | Unset = UNSET,
    price: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Validate order stops

     Validate an order's SL/TP/pending-open levels against the symbol's administrator-set `stops_level`.

    Pump-cached call. The MT4 server verifies that the supplied SL/TP
    (and, for pending orders, the open price) sit at least
    `stops_level` away from the current market and that pending
    expiration is at least ten minutes in the future. Returns a bare
    boolean envelope: `true` when the wrapper's `ResultCode`
    is `Ok`.

    Useful for client-side pre-flight before submitting a real
    `TradeTransaction` — saves a server round-trip for invalid
    orders.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        price (float | Unset):
        x_request_timeout (float | Unset):
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The wrapper's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are exposed as plain strings. Clients submit
            the enum name (e.g. `"Buy"`, `"OpenPending"`); the response
            echoes the names back. This dodges the leaf-enum nested-generic STJ
            source-gen quirk documented in feedback-stj-enum-leaf-nested.

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
price=price,
x_request_timeout=x_request_timeout,

    )).parsed
