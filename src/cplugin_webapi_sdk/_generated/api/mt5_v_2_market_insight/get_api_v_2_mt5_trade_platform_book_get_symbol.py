from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_book_api_response import MT5BookApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/BookGet/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5BookApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5BookApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5BookApiResponse]:
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
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5BookApiResponse]:
    """ Read the Depth of Market of a symbol

     <br>
                Returns the whole Depth of Market of the symbol — every entry, not the difference from
    the
                previous state — ordered by price from the highest to the lowest. Volumes are given as
    the
                data provider supplies them, together with the extended-precision value.

    <br>
                The trade server delivers the Depth of Market only after the manager application has
                subscribed to the symbol, so the first call for a symbol subscribes to it and the
                subscription is kept for later calls. A symbol with the Depth of Market disabled on the
                server answers a platform error instead of an empty book.


    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5BookApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
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
    x_request_timeout: float | Unset = UNSET,

) -> MT5BookApiResponse | None:
    """ Read the Depth of Market of a symbol

     <br>
                Returns the whole Depth of Market of the symbol — every entry, not the difference from
    the
                previous state — ordered by price from the highest to the lowest. Volumes are given as
    the
                data provider supplies them, together with the extended-precision value.

    <br>
                The trade server delivers the Depth of Market only after the manager application has
                subscribed to the symbol, so the first call for a symbol subscribes to it and the
                subscription is kept for later calls. A symbol with the Depth of Market disabled on the
                server answers a platform error instead of an empty book.


    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5BookApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5BookApiResponse]:
    """ Read the Depth of Market of a symbol

     <br>
                Returns the whole Depth of Market of the symbol — every entry, not the difference from
    the
                previous state — ordered by price from the highest to the lowest. Volumes are given as
    the
                data provider supplies them, together with the extended-precision value.

    <br>
                The trade server delivers the Depth of Market only after the manager application has
                subscribed to the symbol, so the first call for a symbol subscribes to it and the
                subscription is kept for later calls. A symbol with the Depth of Market disabled on the
                server answers a platform error instead of an empty book.


    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5BookApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
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
    x_request_timeout: float | Unset = UNSET,

) -> MT5BookApiResponse | None:
    """ Read the Depth of Market of a symbol

     <br>
                Returns the whole Depth of Market of the symbol — every entry, not the difference from
    the
                previous state — ordered by price from the highest to the lowest. Volumes are given as
    the
                data provider supplies them, together with the extended-precision value.

    <br>
                The trade server delivers the Depth of Market only after the manager application has
                subscribed to the symbol, so the first call for a symbol subscribes to it and the
                subscription is kept for later calls. A symbol with the Depth of Market disabled on the
                server answers a platform error instead of an empty book.


    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5BookApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
