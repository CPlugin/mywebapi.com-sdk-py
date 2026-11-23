from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_result_api_response import MT5ResultApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    client_id: int,
    login: int,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/ClientUserAdd/{client_id}/{login}".format(trade_platform=quote(str(trade_platform), safe=""),client_id=quote(str(client_id), safe=""),login=quote(str(login), safe=""),),
    }


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
    client_id: int,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultApiResponse]:
    """ Attach a trading account to a client

     Binds the account with the given login to the client record, so the account is shown
    under that client. An account can belong to one client at a time; attaching it again
    to another client may fail with a platform error. The response carries the platform
    result code of the operation.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        client_id (int):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
client_id=client_id,
login=login,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    client_id: int,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultApiResponse | None:
    """ Attach a trading account to a client

     Binds the account with the given login to the client record, so the account is shown
    under that client. An account can belong to one client at a time; attaching it again
    to another client may fail with a platform error. The response carries the platform
    result code of the operation.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        client_id (int):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client_id=client_id,
login=login,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    client_id: int,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultApiResponse]:
    """ Attach a trading account to a client

     Binds the account with the given login to the client record, so the account is shown
    under that client. An account can belong to one client at a time; attaching it again
    to another client may fail with a platform error. The response carries the platform
    result code of the operation.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        client_id (int):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
client_id=client_id,
login=login,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    client_id: int,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultApiResponse | None:
    """ Attach a trading account to a client

     Binds the account with the given login to the client record, so the account is shown
    under that client. An account can belong to one client at a time; attaching it again
    to another client may fail with a platform error. The response carries the platform
    result code of the operation.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        client_id (int):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client_id=client_id,
login=login,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
