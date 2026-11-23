from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.trade_account_set_request import TradeAccountSetRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    TradeAccountSetRequest  |     TradeAccountSetRequest  |     TradeAccountSetRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/TradeAccountSet".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, TradeAccountSetRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, TradeAccountSetRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, TradeAccountSetRequest):
        
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
    body:    TradeAccountSetRequest  |     TradeAccountSetRequest  |     TradeAccountSetRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Bring orders, positions and balance of an account in line with an external system

     <br>
                Makes the orders, positions and balance of the account match the passed state. The trade
                server compares the lists with its own data and performs the difference as deals with
    the
                `sync` reason: positions missing on one side are opened or closed, positions whose
                direction, price or contract size changed are reopened, a volume change is corrected,
    and
                a balance difference becomes a balance or correction deal. All of it stays in the
    trading
                history of the client.

    <br>
                The operation is heavy and changes money and positions: it must be used by the system
    that
                owns the account, not as a general-purpose edit. An omitted order or position list
    leaves
                that part untouched; an empty list states that the account has none and closes the
                existing ones. The call answers as soon as the trade server has accepted it, and the
                resulting state of the account is reported to the platform journal.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.

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
    body:    TradeAccountSetRequest  |     TradeAccountSetRequest  |     TradeAccountSetRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Bring orders, positions and balance of an account in line with an external system

     <br>
                Makes the orders, positions and balance of the account match the passed state. The trade
                server compares the lists with its own data and performs the difference as deals with
    the
                `sync` reason: positions missing on one side are opened or closed, positions whose
                direction, price or contract size changed are reopened, a volume change is corrected,
    and
                a balance difference becomes a balance or correction deal. All of it stays in the
    trading
                history of the client.

    <br>
                The operation is heavy and changes money and positions: it must be used by the system
    that
                owns the account, not as a general-purpose edit. An omitted order or position list
    leaves
                that part untouched; an empty list states that the account has none and closes the
                existing ones. The call answers as soon as the trade server has accepted it, and the
                resulting state of the account is reported to the platform journal.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.

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
    body:    TradeAccountSetRequest  |     TradeAccountSetRequest  |     TradeAccountSetRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Bring orders, positions and balance of an account in line with an external system

     <br>
                Makes the orders, positions and balance of the account match the passed state. The trade
                server compares the lists with its own data and performs the difference as deals with
    the
                `sync` reason: positions missing on one side are opened or closed, positions whose
                direction, price or contract size changed are reopened, a volume change is corrected,
    and
                a balance difference becomes a balance or correction deal. All of it stays in the
    trading
                history of the client.

    <br>
                The operation is heavy and changes money and positions: it must be used by the system
    that
                owns the account, not as a general-purpose edit. An omitted order or position list
    leaves
                that part untouched; an empty list states that the account has none and closes the
                existing ones. The call answers as soon as the trade server has accepted it, and the
                resulting state of the account is reported to the platform journal.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.

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
    body:    TradeAccountSetRequest  |     TradeAccountSetRequest  |     TradeAccountSetRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Bring orders, positions and balance of an account in line with an external system

     <br>
                Makes the orders, positions and balance of the account match the passed state. The trade
                server compares the lists with its own data and performs the difference as deals with
    the
                `sync` reason: positions missing on one side are opened or closed, positions whose
                direction, price or contract size changed are reopened, a volume change is corrected,
    and
                a balance difference becomes a balance or correction deal. All of it stays in the
    trading
                history of the client.

    <br>
                The operation is heavy and changes money and positions: it must be used by the system
    that
                owns the account, not as a general-purpose edit. An omitted order or position list
    leaves
                that part untouched; an empty list states that the account has none and closes the
                existing ones. The call answers as soon as the trade server has accepted it, and the
                resulting state of the account is reported to the platform journal.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.
        body (TradeAccountSetRequest | Unset): State of an account taken from an external trading
            system, v2 request DTO.

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
