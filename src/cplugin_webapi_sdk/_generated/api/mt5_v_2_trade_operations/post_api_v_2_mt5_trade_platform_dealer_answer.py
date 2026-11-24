from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt5_confirm import MT5Confirm
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5Confirm  |     MT5Confirm  |     MT5Confirm  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/DealerAnswer".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5Confirm):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5Confirm):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5Confirm):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

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
    body:    MT5Confirm  |     MT5Confirm  |     MT5Confirm  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Answer the trade request taken for processing

     <br>
                Completes the request taken with `DealerGet` or `DealerLock`: the confirmation
                carries the answer code and, depending on the request, the confirmed volume, price and
                the identifiers of the order and the deal created in an external trading system. The
                request is processed by the trade server immediately and cannot be answered twice.

    <br>
                The identifier in the confirmation is the identifier of the original request, not the
                caller-side one. The queue must be opened with `DealerStart` first. A rejected
                answer is returned as the platform error that explains it, and the request then stays
                for the platform to expire.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Confirm | Unset):
        body (MT5Confirm | Unset):
        body (MT5Confirm | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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
    body:    MT5Confirm  |     MT5Confirm  |     MT5Confirm  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Answer the trade request taken for processing

     <br>
                Completes the request taken with `DealerGet` or `DealerLock`: the confirmation
                carries the answer code and, depending on the request, the confirmed volume, price and
                the identifiers of the order and the deal created in an external trading system. The
                request is processed by the trade server immediately and cannot be answered twice.

    <br>
                The identifier in the confirmation is the identifier of the original request, not the
                caller-side one. The queue must be opened with `DealerStart` first. A rejected
                answer is returned as the platform error that explains it, and the request then stays
                for the platform to expire.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Confirm | Unset):
        body (MT5Confirm | Unset):
        body (MT5Confirm | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
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
    body:    MT5Confirm  |     MT5Confirm  |     MT5Confirm  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Answer the trade request taken for processing

     <br>
                Completes the request taken with `DealerGet` or `DealerLock`: the confirmation
                carries the answer code and, depending on the request, the confirmed volume, price and
                the identifiers of the order and the deal created in an external trading system. The
                request is processed by the trade server immediately and cannot be answered twice.

    <br>
                The identifier in the confirmation is the identifier of the original request, not the
                caller-side one. The queue must be opened with `DealerStart` first. A rejected
                answer is returned as the platform error that explains it, and the request then stays
                for the platform to expire.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Confirm | Unset):
        body (MT5Confirm | Unset):
        body (MT5Confirm | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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
    body:    MT5Confirm  |     MT5Confirm  |     MT5Confirm  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Answer the trade request taken for processing

     <br>
                Completes the request taken with `DealerGet` or `DealerLock`: the confirmation
                carries the answer code and, depending on the request, the confirmed volume, price and
                the identifiers of the order and the deal created in an external trading system. The
                request is processed by the trade server immediately and cannot be answered twice.

    <br>
                The identifier in the confirmation is the identifier of the original request, not the
                caller-side one. The queue must be opened with `DealerStart` first. A rejected
                answer is returned as the platform error that explains it, and the request then stays
                for the platform to expire.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5Confirm | Unset):
        body (MT5Confirm | Unset):
        body (MT5Confirm | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
