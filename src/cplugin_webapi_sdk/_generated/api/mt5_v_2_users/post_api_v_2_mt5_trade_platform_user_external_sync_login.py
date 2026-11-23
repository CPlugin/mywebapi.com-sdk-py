from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_external_sync_request import MT5ExternalSyncRequest
from ...models.mt5_result_api_response import MT5ResultApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    login: int,
    *,
    body:    MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/UserExternalSync/{login}".format(trade_platform=quote(str(trade_platform), safe=""),login=quote(str(login), safe=""),),
    }

    if isinstance(body, MT5ExternalSyncRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5ExternalSyncRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5ExternalSyncRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5ResultApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5ResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5ResultApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultApiResponse]:
    """ Synchronize an account with an external trading system

     <br>
                Asks the gateway to bring the trading state of the account in line with the external
                trading system it is linked to, and creates the correcting operations that follow from
                the difference. Such operations appear in the trading history of the account.

    <br>
                The scope of the synchronization is chosen by the request: the whole state, the balance,
                the open positions or the pending orders. The call works only when the gateway in use
                provides trading-state synchronization and the account is linked to the external system;
                otherwise the platform error is returned and nothing changes.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultApiResponse | None:
    """ Synchronize an account with an external trading system

     <br>
                Asks the gateway to bring the trading state of the account in line with the external
                trading system it is linked to, and creates the correcting operations that follow from
                the difference. Such operations appear in the trading history of the account.

    <br>
                The scope of the synchronization is chosen by the request: the whole state, the balance,
                the open positions or the pending orders. The call works only when the gateway in use
                provides trading-state synchronization and the account is linked to the external system;
                otherwise the platform error is returned and nothing changes.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultApiResponse]:
    """ Synchronize an account with an external trading system

     <br>
                Asks the gateway to bring the trading state of the account in line with the external
                trading system it is linked to, and creates the correcting operations that follow from
                the difference. Such operations appear in the trading history of the account.

    <br>
                The scope of the synchronization is chosen by the request: the whole state, the balance,
                the open positions or the pending orders. The call works only when the gateway in use
                provides trading-state synchronization and the account is linked to the external system;
                otherwise the platform error is returned and nothing changes.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  |     MT5ExternalSyncRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultApiResponse | None:
    """ Synchronize an account with an external trading system

     <br>
                Asks the gateway to bring the trading state of the account in line with the external
                trading system it is linked to, and creates the correcting operations that follow from
                the difference. Such operations appear in the trading history of the account.

    <br>
                The scope of the synchronization is chosen by the request: the whole state, the balance,
                the open positions or the pending orders. The call works only when the gateway in use
                provides trading-state synchronization and the account is linked to the external system;
                otherwise the platform error is returned and nothing changes.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.
        body (MT5ExternalSyncRequest | Unset): Request to synchronize an account with an external
            trading system through a gateway.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
