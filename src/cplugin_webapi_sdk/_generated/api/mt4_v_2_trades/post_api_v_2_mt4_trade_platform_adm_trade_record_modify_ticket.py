from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_trade_api_response import MT4TradeApiResponse
from ...models.mt4_trade_update import MT4TradeUpdate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    ticket: int,
    *,
    body:    MT4TradeUpdate  |     MT4TradeUpdate  |     MT4TradeUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/AdmTradeRecordModify/{ticket}".format(trade_platform=quote(str(trade_platform), safe=""),ticket=quote(str(ticket), safe=""),),
    }

    if isinstance(body, MT4TradeUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4TradeUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4TradeUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4TradeApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4TradeApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4TradeApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    ticket: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeUpdate  |     MT4TradeUpdate  |     MT4TradeUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4TradeApiResponse]:
    """ Modify trade record (admin)

     Admin direct edit of a single trade record — Type 1 with read-first.

    <br>
    Low-level back-office override that writes directly to the trade
    record. For SL/TP edits prefer
    `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
    — that route goes through the wrapper's audited path. Use this
    endpoint for manual accounting corrections (commission/storage/taxes/
    profit, comment, magic) that the standard TradeTransaction path
    does not cover.
    <br>
    Flow: read existing trade via `TradeRecordsRequest`, patch the
    allow-listed fields in place, submit via `AdmTradeRecordModify`.
    Order/Login/Symbol/Volume/OpenPrice/OpenTime/CloseTime and gateway
    internals are preserved by virtue of not being on the input DTO.
    <br>
    Idempotency-Key strongly recommended. A retried edit without it can
    land twice — usually harmless, but generates audit log noise.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        ticket (int):
        x_request_timeout (float | Unset):
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
ticket=ticket,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    ticket: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeUpdate  |     MT4TradeUpdate  |     MT4TradeUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4TradeApiResponse | None:
    """ Modify trade record (admin)

     Admin direct edit of a single trade record — Type 1 with read-first.

    <br>
    Low-level back-office override that writes directly to the trade
    record. For SL/TP edits prefer
    `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
    — that route goes through the wrapper's audited path. Use this
    endpoint for manual accounting corrections (commission/storage/taxes/
    profit, comment, magic) that the standard TradeTransaction path
    does not cover.
    <br>
    Flow: read existing trade via `TradeRecordsRequest`, patch the
    allow-listed fields in place, submit via `AdmTradeRecordModify`.
    Order/Login/Symbol/Volume/OpenPrice/OpenTime/CloseTime and gateway
    internals are preserved by virtue of not being on the input DTO.
    <br>
    Idempotency-Key strongly recommended. A retried edit without it can
    land twice — usually harmless, but generates audit log noise.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        ticket (int):
        x_request_timeout (float | Unset):
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
ticket=ticket,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    ticket: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeUpdate  |     MT4TradeUpdate  |     MT4TradeUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4TradeApiResponse]:
    """ Modify trade record (admin)

     Admin direct edit of a single trade record — Type 1 with read-first.

    <br>
    Low-level back-office override that writes directly to the trade
    record. For SL/TP edits prefer
    `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
    — that route goes through the wrapper's audited path. Use this
    endpoint for manual accounting corrections (commission/storage/taxes/
    profit, comment, magic) that the standard TradeTransaction path
    does not cover.
    <br>
    Flow: read existing trade via `TradeRecordsRequest`, patch the
    allow-listed fields in place, submit via `AdmTradeRecordModify`.
    Order/Login/Symbol/Volume/OpenPrice/OpenTime/CloseTime and gateway
    internals are preserved by virtue of not being on the input DTO.
    <br>
    Idempotency-Key strongly recommended. A retried edit without it can
    land twice — usually harmless, but generates audit log noise.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        ticket (int):
        x_request_timeout (float | Unset):
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
ticket=ticket,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    ticket: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4TradeUpdate  |     MT4TradeUpdate  |     MT4TradeUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4TradeApiResponse | None:
    """ Modify trade record (admin)

     Admin direct edit of a single trade record — Type 1 with read-first.

    <br>
    Low-level back-office override that writes directly to the trade
    record. For SL/TP edits prefer
    `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
    — that route goes through the wrapper's audited path. Use this
    endpoint for manual accounting corrections (commission/storage/taxes/
    profit, comment, magic) that the standard TradeTransaction path
    does not cover.
    <br>
    Flow: read existing trade via `TradeRecordsRequest`, patch the
    allow-listed fields in place, submit via `AdmTradeRecordModify`.
    Order/Login/Symbol/Volume/OpenPrice/OpenTime/CloseTime and gateway
    internals are preserved by virtue of not being on the input DTO.
    <br>
    Idempotency-Key strongly recommended. A retried edit without it can
    land twice — usually harmless, but generates audit log noise.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        ticket (int):
        x_request_timeout (float | Unset):
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.
        body (MT4TradeUpdate | Unset): Type 1 mutator input for the admin direct-edit endpoint
            `AdmTradeRecordModify`. Only the fields a back-office tool would
            legitimately need to adjust are exposed; everything else (order id,
            login, symbol, volume, open/close times, gateway internals, conversion
            rates, API data blobs) is preserved from the server-side read.

            <br>
            For typical stop-loss / take-profit edits prefer
            `POST TradeTransaction` with `tradeTransactionType=ModifyTrade`
            — that goes through the wrapper's audited path. This endpoint is the
            low-level admin override for back-office corrections.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
ticket=ticket,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
