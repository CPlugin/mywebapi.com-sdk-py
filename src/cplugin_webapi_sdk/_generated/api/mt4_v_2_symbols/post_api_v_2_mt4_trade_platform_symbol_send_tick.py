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
    symbol: str | Unset = UNSET,
    bid: float | Unset = UNSET,
    ask: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["symbol"] = symbol

    params["bid"] = bid

    params["ask"] = ask


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/SymbolSendTick".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


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
    symbol: str | Unset = UNSET,
    bid: float | Unset = UNSET,
    ask: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Send synthetic tick

     Injects a synthetic tick into the MT4 server for the given symbol — used to keep the feed alive on
    instruments where the upstream datafeed is paused, or to drive simulator tooling.

    Manager-live POST. The platform requires the manager account to hold
    the `Market Watch` permission; without it the server typically
    drops the connection rather than returning an error. The API-side
    `ResourceAccessAuthorize` on this endpoint guards against API
    callers without the appropriate platform-level permission, but
    broker-side mis-configuration of the underlying manager rights
    remains the consumer's responsibility.

    `bid` and `ask` are absolute prices, not deltas. Pass
    the symbol's last-known bid/ask if you only need to refresh the
    timestamp; pass adjusted prices to actually move the quote.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str | Unset):
        bid (float | Unset):
        ask (float | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
bid=bid,
ask=ask,
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
    symbol: str | Unset = UNSET,
    bid: float | Unset = UNSET,
    ask: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Send synthetic tick

     Injects a synthetic tick into the MT4 server for the given symbol — used to keep the feed alive on
    instruments where the upstream datafeed is paused, or to drive simulator tooling.

    Manager-live POST. The platform requires the manager account to hold
    the `Market Watch` permission; without it the server typically
    drops the connection rather than returning an error. The API-side
    `ResourceAccessAuthorize` on this endpoint guards against API
    callers without the appropriate platform-level permission, but
    broker-side mis-configuration of the underlying manager rights
    remains the consumer's responsibility.

    `bid` and `ask` are absolute prices, not deltas. Pass
    the symbol's last-known bid/ask if you only need to refresh the
    timestamp; pass adjusted prices to actually move the quote.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str | Unset):
        bid (float | Unset):
        ask (float | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
symbol=symbol,
bid=bid,
ask=ask,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    symbol: str | Unset = UNSET,
    bid: float | Unset = UNSET,
    ask: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Send synthetic tick

     Injects a synthetic tick into the MT4 server for the given symbol — used to keep the feed alive on
    instruments where the upstream datafeed is paused, or to drive simulator tooling.

    Manager-live POST. The platform requires the manager account to hold
    the `Market Watch` permission; without it the server typically
    drops the connection rather than returning an error. The API-side
    `ResourceAccessAuthorize` on this endpoint guards against API
    callers without the appropriate platform-level permission, but
    broker-side mis-configuration of the underlying manager rights
    remains the consumer's responsibility.

    `bid` and `ask` are absolute prices, not deltas. Pass
    the symbol's last-known bid/ask if you only need to refresh the
    timestamp; pass adjusted prices to actually move the quote.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str | Unset):
        bid (float | Unset):
        ask (float | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
bid=bid,
ask=ask,
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
    symbol: str | Unset = UNSET,
    bid: float | Unset = UNSET,
    ask: float | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Send synthetic tick

     Injects a synthetic tick into the MT4 server for the given symbol — used to keep the feed alive on
    instruments where the upstream datafeed is paused, or to drive simulator tooling.

    Manager-live POST. The platform requires the manager account to hold
    the `Market Watch` permission; without it the server typically
    drops the connection rather than returning an error. The API-side
    `ResourceAccessAuthorize` on this endpoint guards against API
    callers without the appropriate platform-level permission, but
    broker-side mis-configuration of the underlying manager rights
    remains the consumer's responsibility.

    `bid` and `ask` are absolute prices, not deltas. Pass
    the symbol's last-known bid/ask if you only need to refresh the
    timestamp; pass adjusted prices to actually move the quote.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str | Unset):
        bid (float | Unset):
        ask (float | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
symbol=symbol,
bid=bid,
ask=ask,
x_request_timeout=x_request_timeout,

    )).parsed
