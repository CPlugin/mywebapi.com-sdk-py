from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_batch_result_list_api_response import MT5BatchResultListApiResponse
from ...models.mt5_client import MT5Client
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    list[MT5Client]  |     list[MT5Client]  |     list[MT5Client]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/ClientAddBatch".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, list[MT5Client]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, list[MT5Client]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/json"
    if isinstance(body, list[MT5Client]):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = []
            for body_item_data in body:
                body_item = body_item_data.to_dict()
                _kwargs["json"].append(body_item)



        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5BatchResultListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5BatchResultListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5BatchResultListApiResponse]:
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
    body:    list[MT5Client]  |     list[MT5Client]  |     list[MT5Client]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5BatchResultListApiResponse]:
    """ Add clients in bulk

     Adds the listed clients to the server database in one call — the same rules and the same
    validation as the single add. Every record receives the identifier the server assigned to it,
    which is returned per entry together with its result code. A partial failure answers one entry
    per client, so inspect each result instead of trusting the batch as a whole.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5Client] | Unset):
        body (list[MT5Client] | Unset):
        body (list[MT5Client] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5BatchResultListApiResponse]
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
    body:    list[MT5Client]  |     list[MT5Client]  |     list[MT5Client]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5BatchResultListApiResponse | None:
    """ Add clients in bulk

     Adds the listed clients to the server database in one call — the same rules and the same
    validation as the single add. Every record receives the identifier the server assigned to it,
    which is returned per entry together with its result code. A partial failure answers one entry
    per client, so inspect each result instead of trusting the batch as a whole.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5Client] | Unset):
        body (list[MT5Client] | Unset):
        body (list[MT5Client] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5BatchResultListApiResponse
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
    body:    list[MT5Client]  |     list[MT5Client]  |     list[MT5Client]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5BatchResultListApiResponse]:
    """ Add clients in bulk

     Adds the listed clients to the server database in one call — the same rules and the same
    validation as the single add. Every record receives the identifier the server assigned to it,
    which is returned per entry together with its result code. A partial failure answers one entry
    per client, so inspect each result instead of trusting the batch as a whole.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5Client] | Unset):
        body (list[MT5Client] | Unset):
        body (list[MT5Client] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5BatchResultListApiResponse]
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
    body:    list[MT5Client]  |     list[MT5Client]  |     list[MT5Client]  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5BatchResultListApiResponse | None:
    """ Add clients in bulk

     Adds the listed clients to the server database in one call — the same rules and the same
    validation as the single add. Every record receives the identifier the server assigned to it,
    which is returned per entry together with its result code. A partial failure answers one entry
    per client, so inspect each result instead of trusting the batch as a whole.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (list[MT5Client] | Unset):
        body (list[MT5Client] | Unset):
        body (list[MT5Client] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5BatchResultListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
