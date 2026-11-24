from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_request_api_response import MT5RequestApiResponse
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
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/DealerGet".format(trade_platform=quote(str(trade_platform), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5RequestApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5RequestApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5RequestApiResponse]:
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

) -> Response[MT5RequestApiResponse]:
    """ Take the first request of the queue for processing

     <br>
                Takes the request at the head of the queue and reserves it for this connection: the
                trade server will not hand it to another dealer and waits for the answer. The request
                must be answered with `DealerAnswer`; an unanswered request is not returned to the
                queue and is lost.

    <br>
                The call is a write, not a read for all practical purposes: it changes the state of the
                queue and cannot be safely repeated — a repeated call takes the next request. When the
                queue is empty the platform answers `MT_RET_OK_NONE`. The queue must be opened with
                `DealerStart` first.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5RequestApiResponse]
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

) -> MT5RequestApiResponse | None:
    """ Take the first request of the queue for processing

     <br>
                Takes the request at the head of the queue and reserves it for this connection: the
                trade server will not hand it to another dealer and waits for the answer. The request
                must be answered with `DealerAnswer`; an unanswered request is not returned to the
                queue and is lost.

    <br>
                The call is a write, not a read for all practical purposes: it changes the state of the
                queue and cannot be safely repeated — a repeated call takes the next request. When the
                queue is empty the platform answers `MT_RET_OK_NONE`. The queue must be opened with
                `DealerStart` first.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5RequestApiResponse
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

) -> Response[MT5RequestApiResponse]:
    """ Take the first request of the queue for processing

     <br>
                Takes the request at the head of the queue and reserves it for this connection: the
                trade server will not hand it to another dealer and waits for the answer. The request
                must be answered with `DealerAnswer`; an unanswered request is not returned to the
                queue and is lost.

    <br>
                The call is a write, not a read for all practical purposes: it changes the state of the
                queue and cannot be safely repeated — a repeated call takes the next request. When the
                queue is empty the platform answers `MT_RET_OK_NONE`. The queue must be opened with
                `DealerStart` first.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5RequestApiResponse]
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

) -> MT5RequestApiResponse | None:
    """ Take the first request of the queue for processing

     <br>
                Takes the request at the head of the queue and reserves it for this connection: the
                trade server will not hand it to another dealer and waits for the answer. The request
                must be answered with `DealerAnswer`; an unanswered request is not returned to the
                queue and is lost.

    <br>
                The call is a write, not a read for all practical purposes: it changes the state of the
                queue and cannot be safely repeated — a repeated call takes the next request. When the
                queue is empty the platform answers `MT_RET_OK_NONE`. The queue must be opened with
                `DealerStart` first.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5RequestApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
