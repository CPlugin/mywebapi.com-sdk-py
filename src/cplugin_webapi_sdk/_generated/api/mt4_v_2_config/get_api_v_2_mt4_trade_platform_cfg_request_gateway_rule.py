from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_gateway_rule_list_api_response import MT4GatewayRuleListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/CfgRequestGatewayRule".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4GatewayRuleListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4GatewayRuleListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4GatewayRuleListApiResponse]:
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

) -> Response[MT4GatewayRuleListApiResponse]:
    """ List gateway rules

     All MT4 gateway-rule entries (STP execution routing policies), paginated by Name.

    Manager-live read (round-trip). Each rule matches incoming orders
    by RequestSymbol + RequestGroup and routes them to a configured
    execution gateway-account (ExeAccountName/ExeAccountId) with
    per-rule slippage and volume limits. Name is assumed unique
    within the rules table and serves as the cursor key.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GatewayRuleListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,

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

) -> MT4GatewayRuleListApiResponse | None:
    """ List gateway rules

     All MT4 gateway-rule entries (STP execution routing policies), paginated by Name.

    Manager-live read (round-trip). Each rule matches incoming orders
    by RequestSymbol + RequestGroup and routes them to a configured
    execution gateway-account (ExeAccountName/ExeAccountId) with
    per-rule slippage and volume limits. Name is assumed unique
    within the rules table and serves as the cursor key.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GatewayRuleListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = UNSET,
    cursor: str | Unset = UNSET,

) -> Response[MT4GatewayRuleListApiResponse]:
    """ List gateway rules

     All MT4 gateway-rule entries (STP execution routing policies), paginated by Name.

    Manager-live read (round-trip). Each rule matches incoming orders
    by RequestSymbol + RequestGroup and routes them to a configured
    execution gateway-account (ExeAccountName/ExeAccountId) with
    per-rule slippage and volume limits. Name is assumed unique
    within the rules table and serves as the cursor key.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GatewayRuleListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
limit=limit,
cursor=cursor,

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

) -> MT4GatewayRuleListApiResponse | None:
    """ List gateway rules

     All MT4 gateway-rule entries (STP execution routing policies), paginated by Name.

    Manager-live read (round-trip). Each rule matches incoming orders
    by RequestSymbol + RequestGroup and routes them to a configured
    execution gateway-account (ExeAccountName/ExeAccountId) with
    per-rule slippage and volume limits. Name is assumed unique
    within the rules table and serves as the cursor key.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GatewayRuleListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,

    )).parsed
