from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_order_list_api_response import MT5OrderListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    mask: str,
    symbol: str,
    *,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/HistoryRequestByGroupSymbol/{mask}/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),mask=quote(str(mask), safe=""),symbol=quote(str(symbol), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5OrderListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5OrderListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5OrderListApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    mask: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5OrderListApiResponse]:
    """ Order history by group and symbol

     Returns the history orders of the given symbol for every login in the groups matching the
    mask, within a time window. Omitted bounds mean the whole history: from 01.01.1970 to the
    newest record. The result is not paginated: the whole window is returned at once.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        mask (str):
        symbol (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5OrderListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
mask=mask,
symbol=symbol,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    mask: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5OrderListApiResponse | None:
    """ Order history by group and symbol

     Returns the history orders of the given symbol for every login in the groups matching the
    mask, within a time window. Omitted bounds mean the whole history: from 01.01.1970 to the
    newest record. The result is not paginated: the whole window is returned at once.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        mask (str):
        symbol (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5OrderListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
mask=mask,
symbol=symbol,
client=client,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    mask: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5OrderListApiResponse]:
    """ Order history by group and symbol

     Returns the history orders of the given symbol for every login in the groups matching the
    mask, within a time window. Omitted bounds mean the whole history: from 01.01.1970 to the
    newest record. The result is not paginated: the whole window is returned at once.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        mask (str):
        symbol (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5OrderListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
mask=mask,
symbol=symbol,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    mask: str,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5OrderListApiResponse | None:
    """ Order history by group and symbol

     Returns the history orders of the given symbol for every login in the groups matching the
    mask, within a time window. Omitted bounds mean the whole history: from 01.01.1970 to the
    newest record. The result is not paginated: the whole window is returned at once.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        mask (str):
        symbol (str):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5OrderListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
mask=mask,
symbol=symbol,
client=client,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )).parsed
