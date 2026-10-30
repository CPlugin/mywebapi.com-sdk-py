from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_trade_transaction import MT4TradeTransaction
from ...models.mt4_trade_transaction_api_response import MT4TradeTransactionApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4TradeTransaction  |     MT4TradeTransaction  |     MT4TradeTransaction  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/TradeTransaction".format(trade_platform=quote(str(trade_platform), safe=""),),
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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4TradeTransactionApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4TradeTransactionApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4TradeTransactionApiResponse]:
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
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4TradeTransactionApiResponse]:
    """ Submit trade transaction

     Submit a trade transaction — open / modify / close / balance op.

    <br>
    POST mutator covering every platform trade operation through the single
    `TradeTransaction` entry point. The request body's
    `tradeTransactionType` + `tradeCommand` combination selects
    the actual operation — `OpenMarket`+`Buy`, `PendingOpen`+`BuyLimit`,
    `CloseMarket`+`Sell`, and the manager-side `Br*` types:
    `BrModify` (open price, SL, TP of an order), `BrDelete`,
    `BrBalance`+`Balance` or `Credit` (balance/credit operation on
    `orderBy`). The schema of the request body lists every accepted value.
    <br>
    An unknown `tradeTransactionType`, `tradeCommand` or
    `tradeRequestFlags` value is refused with error code `Validation`
    and the list of valid values; nothing is sent to the trading platform.
    Names are case-insensitive; the numeric value of a member is accepted too.
    <br>
    On success the response echoes the platform's mutated structure — most
    importantly the `Order` field, which the server assigns on Open
    operations and clients use to track the ticket afterwards.
    <br><b>Idempotency-Key is essentially mandatory.</b> A retried trade
    transaction without the header can open a second position, double-
    close, or apply a balance op twice. With the header the second call
    returns the cached envelope from the first.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeTransactionApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
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
    x_request_timeout: float | Unset = UNSET,

) -> MT4TradeTransactionApiResponse | None:
    """ Submit trade transaction

     Submit a trade transaction — open / modify / close / balance op.

    <br>
    POST mutator covering every platform trade operation through the single
    `TradeTransaction` entry point. The request body's
    `tradeTransactionType` + `tradeCommand` combination selects
    the actual operation — `OpenMarket`+`Buy`, `PendingOpen`+`BuyLimit`,
    `CloseMarket`+`Sell`, and the manager-side `Br*` types:
    `BrModify` (open price, SL, TP of an order), `BrDelete`,
    `BrBalance`+`Balance` or `Credit` (balance/credit operation on
    `orderBy`). The schema of the request body lists every accepted value.
    <br>
    An unknown `tradeTransactionType`, `tradeCommand` or
    `tradeRequestFlags` value is refused with error code `Validation`
    and the list of valid values; nothing is sent to the trading platform.
    Names are case-insensitive; the numeric value of a member is accepted too.
    <br>
    On success the response echoes the platform's mutated structure — most
    importantly the `Order` field, which the server assigns on Open
    operations and clients use to track the ticket afterwards.
    <br><b>Idempotency-Key is essentially mandatory.</b> A retried trade
    transaction without the header can open a second position, double-
    close, or apply a balance op twice. With the header the second call
    returns the cached envelope from the first.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeTransactionApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeTransaction  |     MT4TradeTransaction  |     MT4TradeTransaction  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4TradeTransactionApiResponse]:
    """ Submit trade transaction

     Submit a trade transaction — open / modify / close / balance op.

    <br>
    POST mutator covering every platform trade operation through the single
    `TradeTransaction` entry point. The request body's
    `tradeTransactionType` + `tradeCommand` combination selects
    the actual operation — `OpenMarket`+`Buy`, `PendingOpen`+`BuyLimit`,
    `CloseMarket`+`Sell`, and the manager-side `Br*` types:
    `BrModify` (open price, SL, TP of an order), `BrDelete`,
    `BrBalance`+`Balance` or `Credit` (balance/credit operation on
    `orderBy`). The schema of the request body lists every accepted value.
    <br>
    An unknown `tradeTransactionType`, `tradeCommand` or
    `tradeRequestFlags` value is refused with error code `Validation`
    and the list of valid values; nothing is sent to the trading platform.
    Names are case-insensitive; the numeric value of a member is accepted too.
    <br>
    On success the response echoes the platform's mutated structure — most
    importantly the `Order` field, which the server assigns on Open
    operations and clients use to track the ticket afterwards.
    <br><b>Idempotency-Key is essentially mandatory.</b> A retried trade
    transaction without the header can open a second position, double-
    close, or apply a balance op twice. With the header the second call
    returns the cached envelope from the first.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeTransactionApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
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
    x_request_timeout: float | Unset = UNSET,

) -> MT4TradeTransactionApiResponse | None:
    """ Submit trade transaction

     Submit a trade transaction — open / modify / close / balance op.

    <br>
    POST mutator covering every platform trade operation through the single
    `TradeTransaction` entry point. The request body's
    `tradeTransactionType` + `tradeCommand` combination selects
    the actual operation — `OpenMarket`+`Buy`, `PendingOpen`+`BuyLimit`,
    `CloseMarket`+`Sell`, and the manager-side `Br*` types:
    `BrModify` (open price, SL, TP of an order), `BrDelete`,
    `BrBalance`+`Balance` or `Credit` (balance/credit operation on
    `orderBy`). The schema of the request body lists every accepted value.
    <br>
    An unknown `tradeTransactionType`, `tradeCommand` or
    `tradeRequestFlags` value is refused with error code `Validation`
    and the list of valid values; nothing is sent to the trading platform.
    Names are case-insensitive; the numeric value of a member is accepted too.
    <br>
    On success the response echoes the platform's mutated structure — most
    importantly the `Order` field, which the server assigns on Open
    operations and clients use to track the ticket afterwards.
    <br><b>Idempotency-Key is essentially mandatory.</b> A retried trade
    transaction without the header can open a second position, double-
    close, or apply a balance op twice. With the header the second call
    returns the cached envelope from the first.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.
        body (MT4TradeTransaction | Unset): v2 DTO for a trade transaction — input AND output of
            `TradeTransaction`.
            The platform's `TradeTransInfo` is in/out: the caller fills the request
            fields (operation type, command, symbol, volume, price), submits via POST,
            and the server populates the resulting `Order` id (for Open) or
            echoes the modified record (for Modify/Close).

            Enum fields (`TradeTransactionType`, `TradeCommand`,
            `TradeRequestFlags`) are plain strings. Clients submit the name
            (e.g. `"Buy"`, `"PendingOpen"`); the response echoes the names
            back. Each field lists its valid names.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeTransactionApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
