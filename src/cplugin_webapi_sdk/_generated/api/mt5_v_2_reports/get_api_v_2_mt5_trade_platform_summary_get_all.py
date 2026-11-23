from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_summary_list_api_response import MT5SummaryListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/SummaryGetAll".format(trade_platform=quote(str(trade_platform), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5SummaryListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5SummaryListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5SummaryListApiResponse]:
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
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SummaryListApiResponse]:
    """ Summary of client and hedging positions for every symbol

     Returns the whole summary table: one record per symbol with the client open interest, the
    hedging position of the company and the profit of both. The table ends with the total
    record, which carries an empty symbol name. Profit figures of accounts whose deposit
    currency differs from the summary currency become available only after the trade server
    has received a quote of the symbol needed for the conversion.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SummaryListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
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
    x_request_timeout: float | Unset = UNSET,

) -> MT5SummaryListApiResponse | None:
    """ Summary of client and hedging positions for every symbol

     Returns the whole summary table: one record per symbol with the client open interest, the
    hedging position of the company and the profit of both. The table ends with the total
    record, which carries an empty symbol name. Profit figures of accounts whose deposit
    currency differs from the summary currency become available only after the trade server
    has received a quote of the symbol needed for the conversion.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SummaryListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SummaryListApiResponse]:
    """ Summary of client and hedging positions for every symbol

     Returns the whole summary table: one record per symbol with the client open interest, the
    hedging position of the company and the profit of both. The table ends with the total
    record, which carries an empty symbol name. Profit figures of accounts whose deposit
    currency differs from the summary currency become available only after the trade server
    has received a quote of the symbol needed for the conversion.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SummaryListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
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
    x_request_timeout: float | Unset = UNSET,

) -> MT5SummaryListApiResponse | None:
    """ Summary of client and hedging positions for every symbol

     Returns the whole summary table: one record per symbol with the client open interest, the
    hedging position of the company and the profit of both. The table ends with the total
    record, which carries an empty symbol name. Profit figures of accounts whose deposit
    currency differs from the summary currency become available only after the trade server
    has received a quote of the symbol needed for the conversion.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SummaryListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
