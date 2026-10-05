from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_trade_list_api_response import MT4TradeListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    file: str,
    *,
    request: str | Unset = UNSET,
    limit: int | Unset = 10000,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["request"] = request

    params["limit"] = limit


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/BackupRequestOrders/{file}".format(trade_platform=quote(str(trade_platform), safe=""),file=quote(str(file), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4TradeListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4TradeListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4TradeListApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    request: str | Unset = UNSET,
    limit: int | Unset = 10000,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4TradeListApiResponse]:
    """ Read orders from backup

     Read trade records out of a backup file (does NOT restore — read-only).

    Manager (live) call to the platform's
    `BackupRequestOrders(string file, string request)`. Order-side
    counterpart of `BackupRequestUsers`. Same caveats:
    read-only, full file loaded server-side regardless of `limit`,
    destructive restore is a separate (Wave 4b) operation.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        file (str):
        request (str | Unset):
        limit (int | Unset):  Default: 10000.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
file=file,
request=request,
limit=limit,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    request: str | Unset = UNSET,
    limit: int | Unset = 10000,
    x_request_timeout: float | Unset = UNSET,

) -> MT4TradeListApiResponse | None:
    """ Read orders from backup

     Read trade records out of a backup file (does NOT restore — read-only).

    Manager (live) call to the platform's
    `BackupRequestOrders(string file, string request)`. Order-side
    counterpart of `BackupRequestUsers`. Same caveats:
    read-only, full file loaded server-side regardless of `limit`,
    destructive restore is a separate (Wave 4b) operation.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        file (str):
        request (str | Unset):
        limit (int | Unset):  Default: 10000.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
file=file,
client=client,
request=request,
limit=limit,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    request: str | Unset = UNSET,
    limit: int | Unset = 10000,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4TradeListApiResponse]:
    """ Read orders from backup

     Read trade records out of a backup file (does NOT restore — read-only).

    Manager (live) call to the platform's
    `BackupRequestOrders(string file, string request)`. Order-side
    counterpart of `BackupRequestUsers`. Same caveats:
    read-only, full file loaded server-side regardless of `limit`,
    destructive restore is a separate (Wave 4b) operation.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        file (str):
        request (str | Unset):
        limit (int | Unset):  Default: 10000.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4TradeListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
file=file,
request=request,
limit=limit,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    file: str,
    *,
    client: AuthenticatedClient | Client,
    request: str | Unset = UNSET,
    limit: int | Unset = 10000,
    x_request_timeout: float | Unset = UNSET,

) -> MT4TradeListApiResponse | None:
    """ Read orders from backup

     Read trade records out of a backup file (does NOT restore — read-only).

    Manager (live) call to the platform's
    `BackupRequestOrders(string file, string request)`. Order-side
    counterpart of `BackupRequestUsers`. Same caveats:
    read-only, full file loaded server-side regardless of `limit`,
    destructive restore is a separate (Wave 4b) operation.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        file (str):
        request (str | Unset):
        limit (int | Unset):  Default: 10000.
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4TradeListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
file=file,
client=client,
request=request,
limit=limit,
x_request_timeout=x_request_timeout,

    )).parsed
