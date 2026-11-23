from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_symbol_api_response import MT5SymbolApiResponse
from ...models.mt5_symbol_update import MT5SymbolUpdate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    body:    MT5SymbolUpdate  |     MT5SymbolUpdate  |     MT5SymbolUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/SymbolUpdate/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }

    if isinstance(body, MT5SymbolUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5SymbolUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5SymbolUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5SymbolApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5SymbolApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5SymbolApiResponse]:
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
    body:    MT5SymbolUpdate  |     MT5SymbolUpdate  |     MT5SymbolUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SymbolApiResponse]:
    r""" Update a symbol

     <br>
                Changes the symbol record with the given name. Only the fields present in the body are
                written: the record is read from the trade server, the body is applied over it, and the
                merged record is written back. A field left out keeps its server value; for the
                description, omitting the key keeps the value while sending `\"\"` clears it. A body
                without any field is rejected, and an unknown value of an enum field is answered as a
                parameter error. The body must be the symbol update object — a full symbol record is not
                accepted.

    <br>
                The record is read from the trade server first, then written, then re-read, so the
                response carries the state actually stored by the server. An unknown symbol is
                answered with the trade server's error code instead of a record.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SymbolApiResponse]
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
    body:    MT5SymbolUpdate  |     MT5SymbolUpdate  |     MT5SymbolUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SymbolApiResponse | None:
    r""" Update a symbol

     <br>
                Changes the symbol record with the given name. Only the fields present in the body are
                written: the record is read from the trade server, the body is applied over it, and the
                merged record is written back. A field left out keeps its server value; for the
                description, omitting the key keeps the value while sending `\"\"` clears it. A body
                without any field is rejected, and an unknown value of an enum field is answered as a
                parameter error. The body must be the symbol update object — a full symbol record is not
                accepted.

    <br>
                The record is read from the trade server first, then written, then re-read, so the
                response carries the state actually stored by the server. An unknown symbol is
                answered with the trade server's error code instead of a record.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SymbolApiResponse
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
    body:    MT5SymbolUpdate  |     MT5SymbolUpdate  |     MT5SymbolUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SymbolApiResponse]:
    r""" Update a symbol

     <br>
                Changes the symbol record with the given name. Only the fields present in the body are
                written: the record is read from the trade server, the body is applied over it, and the
                merged record is written back. A field left out keeps its server value; for the
                description, omitting the key keeps the value while sending `\"\"` clears it. A body
                without any field is rejected, and an unknown value of an enum field is answered as a
                parameter error. The body must be the symbol update object — a full symbol record is not
                accepted.

    <br>
                The record is read from the trade server first, then written, then re-read, so the
                response carries the state actually stored by the server. An unknown symbol is
                answered with the trade server's error code instead of a record.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SymbolApiResponse]
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
    body:    MT5SymbolUpdate  |     MT5SymbolUpdate  |     MT5SymbolUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SymbolApiResponse | None:
    r""" Update a symbol

     <br>
                Changes the symbol record with the given name. Only the fields present in the body are
                written: the record is read from the trade server, the body is applied over it, and the
                merged record is written back. A field left out keeps its server value; for the
                description, omitting the key keeps the value while sending `\"\"` clears it. A body
                without any field is rejected, and an unknown value of an enum field is answered as a
                parameter error. The body must be the symbol update object — a full symbol record is not
                accepted.

    <br>
                The record is read from the trade server first, then written, then re-read, so the
                response carries the state actually stored by the server. An unknown symbol is
                answered with the trade server's error code instead of a record.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.
        body (MT5SymbolUpdate | Unset): Editable surface of a symbol record: 15 fields that are
            safely writable, every one optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SymbolApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
