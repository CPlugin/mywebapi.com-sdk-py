from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.chart_period import ChartPeriod
from ...models.mt4_chart_write_request import MT4ChartWriteRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    body:    MT4ChartWriteRequest  |     MT4ChartWriteRequest  |     MT4ChartWriteRequest  | Unset = UNSET,
    period: ChartPeriod | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    json_period: str | Unset = UNSET
    if not isinstance(period, Unset):
        json_period = period.value

    params["period"] = json_period


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/ChartDelete/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
        "params": params,
    }

    if isinstance(body, MT4ChartWriteRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4ChartWriteRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4ChartWriteRequest):
        
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
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4ChartWriteRequest  |     MT4ChartWriteRequest  |     MT4ChartWriteRequest  | Unset = UNSET,
    period: ChartPeriod | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Delete chart bars

     Delete OHLC bars from a symbol's chart history — POST destructive.

    Manager (live) call. Removes bars whose `Time` matches the
    entries in `Rates` for the given `period`. Only the bar
    timestamp is consulted server-side; OHLC values can be zero.

    Idempotency-Key strongly recommended — silently repeating a delete on
    already-removed bars is harmless, but accidental double-submit could
    nudge audit logs with extra \"operation requested\" entries.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        period (ChartPeriod | Unset):
        x_request_timeout (float | Unset):
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
body=body,
period=period,
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
    body:    MT4ChartWriteRequest  |     MT4ChartWriteRequest  |     MT4ChartWriteRequest  | Unset = UNSET,
    period: ChartPeriod | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Delete chart bars

     Delete OHLC bars from a symbol's chart history — POST destructive.

    Manager (live) call. Removes bars whose `Time` matches the
    entries in `Rates` for the given `period`. Only the bar
    timestamp is consulted server-side; OHLC values can be zero.

    Idempotency-Key strongly recommended — silently repeating a delete on
    already-removed bars is harmless, but accidental double-submit could
    nudge audit logs with extra \"operation requested\" entries.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        period (ChartPeriod | Unset):
        x_request_timeout (float | Unset):
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.

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
body=body,
period=period,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4ChartWriteRequest  |     MT4ChartWriteRequest  |     MT4ChartWriteRequest  | Unset = UNSET,
    period: ChartPeriod | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Delete chart bars

     Delete OHLC bars from a symbol's chart history — POST destructive.

    Manager (live) call. Removes bars whose `Time` matches the
    entries in `Rates` for the given `period`. Only the bar
    timestamp is consulted server-side; OHLC values can be zero.

    Idempotency-Key strongly recommended — silently repeating a delete on
    already-removed bars is harmless, but accidental double-submit could
    nudge audit logs with extra \"operation requested\" entries.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        period (ChartPeriod | Unset):
        x_request_timeout (float | Unset):
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
body=body,
period=period,
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
    body:    MT4ChartWriteRequest  |     MT4ChartWriteRequest  |     MT4ChartWriteRequest  | Unset = UNSET,
    period: ChartPeriod | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Delete chart bars

     Delete OHLC bars from a symbol's chart history — POST destructive.

    Manager (live) call. Removes bars whose `Time` matches the
    entries in `Rates` for the given `period`. Only the bar
    timestamp is consulted server-side; OHLC values can be zero.

    Idempotency-Key strongly recommended — silently repeating a delete on
    already-removed bars is harmless, but accidental double-submit could
    nudge audit logs with extra \"operation requested\" entries.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        period (ChartPeriod | Unset):
        x_request_timeout (float | Unset):
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.
        body (MT4ChartWriteRequest | Unset): v2 request body for the `ChartAdd` / `ChartUpdate` /
            `ChartDelete`
            trio. Wraps the bars list so the request shape stays extensible — future
            metadata (e.g. `SkipIntegrityCheck`) can be added without a breaking
            change to clients that only sent `Rates`.

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
body=body,
period=period,
x_request_timeout=x_request_timeout,

    )).parsed
