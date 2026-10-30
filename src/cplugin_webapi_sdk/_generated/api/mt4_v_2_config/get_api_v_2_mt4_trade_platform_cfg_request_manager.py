from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_manager_rights_list_api_response import MT4ManagerRightsListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/CfgRequestManager".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4ManagerRightsListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4ManagerRightsListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4ManagerRightsListApiResponse]:
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
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ManagerRightsListApiResponse]:
    """ List manager configs

     All MT4 manager-account configurations on the connected server, paginated by Login.

    Manager-live read (round-trip). Each entry surfaces the manager's
    Login/Name/Groups/MailBox, the 19 boolean permission rights (Manager,
    Money, Broker, Admin, Reports, Trades, MarketWatch, etc.), IP-filter
    range, and InfoDepth. Internal platform fields (SecGroups, Unused,
    ExpTime, Reserved) are dropped from the v2 contract.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ManagerRightsListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,
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
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ManagerRightsListApiResponse | None:
    """ List manager configs

     All MT4 manager-account configurations on the connected server, paginated by Login.

    Manager-live read (round-trip). Each entry surfaces the manager's
    Login/Name/Groups/MailBox, the 19 boolean permission rights (Manager,
    Money, Broker, Admin, Reports, Trades, MarketWatch, etc.), IP-filter
    range, and InfoDepth. Internal platform fields (SecGroups, Unused,
    ExpTime, Reserved) are dropped from the v2 contract.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ManagerRightsListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ManagerRightsListApiResponse]:
    """ List manager configs

     All MT4 manager-account configurations on the connected server, paginated by Login.

    Manager-live read (round-trip). Each entry surfaces the manager's
    Login/Name/Groups/MailBox, the 19 boolean permission rights (Manager,
    Money, Broker, Admin, Reports, Trades, MarketWatch, etc.), IP-filter
    range, and InfoDepth. Internal platform fields (SecGroups, Unused,
    ExpTime, Reserved) are dropped from the v2 contract.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ManagerRightsListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,
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
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ManagerRightsListApiResponse | None:
    """ List manager configs

     All MT4 manager-account configurations on the connected server, paginated by Login.

    Manager-live read (round-trip). Each entry surfaces the manager's
    Login/Name/Groups/MailBox, the 19 boolean permission rights (Manager,
    Money, Broker, Admin, Reports, Trades, MarketWatch, etc.), IP-filter
    range, and InfoDepth. Internal platform fields (SecGroups, Unused,
    ExpTime, Reserved) are dropped from the v2 contract.

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ManagerRightsListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,
x_request_timeout=x_request_timeout,

    )).parsed
