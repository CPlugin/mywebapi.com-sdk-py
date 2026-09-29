from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_symbol_config_api_response import MT4SymbolConfigApiResponse
from ...models.patch_api_v2mt4_trade_platform_symbol_config_symbol_json_body import PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    body: PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/MT4/{trade_platform}/SymbolConfig/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4SymbolConfigApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4SymbolConfigApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4SymbolConfigApiResponse]:
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
    body: PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4SymbolConfigApiResponse]:
    """ Patch symbol config

     Type 2 mutator — partial update of a symbol configuration. Same flow as `UserRecordPatch`; reads
    existing config live, overlays the patch, writes back.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody): Only the fields to change;
            the rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolConfigApiResponse]
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
    body: PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> MT4SymbolConfigApiResponse | None:
    """ Patch symbol config

     Type 2 mutator — partial update of a symbol configuration. Same flow as `UserRecordPatch`; reads
    existing config live, overlays the patch, writes back.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody): Only the fields to change;
            the rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolConfigApiResponse
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
    body: PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4SymbolConfigApiResponse]:
    """ Patch symbol config

     Type 2 mutator — partial update of a symbol configuration. Same flow as `UserRecordPatch`; reads
    existing config live, overlays the patch, writes back.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody): Only the fields to change;
            the rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SymbolConfigApiResponse]
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
    body: PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> MT4SymbolConfigApiResponse | None:
    """ Patch symbol config

     Type 2 mutator — partial update of a symbol configuration. Same flow as `UserRecordPatch`; reads
    existing config live, overlays the patch, writes back.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody): Only the fields to change;
            the rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SymbolConfigApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
