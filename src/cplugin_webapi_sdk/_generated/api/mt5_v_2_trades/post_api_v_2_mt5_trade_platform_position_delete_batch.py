from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_result_list_api_response import MT5ResultListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/PositionDeleteBatch".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, list[int]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body



        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, list[int]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body



        headers["Content-Type"] = "application/json"
    if isinstance(body, list[int]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body



        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5ResultListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5ResultListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5ResultListApiResponse]:
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
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultListApiResponse]:
    """ Delete positions in bulk

     Deletes the listed positions and returns one result code per ticket, in the same order.
    `MT_RET_OK` means all were deleted, `MT_RET_ERR_PARTIAL` means only some —
    inspect each entry. On partial success the array carries a result for every ticket and
    the caller inspects them itself; on a complete failure no array is returned.
    Deleting positions does not touch the deal history, so the account may
    afterwards fail consistency checks.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultListApiResponse]
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
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultListApiResponse | None:
    """ Delete positions in bulk

     Deletes the listed positions and returns one result code per ticket, in the same order.
    `MT_RET_OK` means all were deleted, `MT_RET_ERR_PARTIAL` means only some —
    inspect each entry. On partial success the array carries a result for every ticket and
    the caller inspects them itself; on a complete failure no array is returned.
    Deleting positions does not touch the deal history, so the account may
    afterwards fail consistency checks.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultListApiResponse
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
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultListApiResponse]:
    """ Delete positions in bulk

     Deletes the listed positions and returns one result code per ticket, in the same order.
    `MT_RET_OK` means all were deleted, `MT_RET_ERR_PARTIAL` means only some —
    inspect each entry. On partial success the array carries a result for every ticket and
    the caller inspects them itself; on a complete failure no array is returned.
    Deleting positions does not touch the deal history, so the account may
    afterwards fail consistency checks.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultListApiResponse]
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
    body:    list[int]  |     list[int]  |     list[int]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultListApiResponse | None:
    """ Delete positions in bulk

     Deletes the listed positions and returns one result code per ticket, in the same order.
    `MT_RET_OK` means all were deleted, `MT_RET_ERR_PARTIAL` means only some —
    inspect each entry. On partial success the array carries a result for every ticket and
    the caller inspects them itself; on a complete failure no array is returned.
    Deleting positions does not touch the deal history, so the account may
    afterwards fail consistency checks.

    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):
        body (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
