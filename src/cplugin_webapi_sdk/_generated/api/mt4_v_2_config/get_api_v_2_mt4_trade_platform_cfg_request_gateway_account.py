from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_gateway_account_list_api_response import MT4GatewayAccountListApiResponse
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
        "url": "/api/v2/MT4/{trade_platform}/CfgRequestGatewayAccount".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4GatewayAccountListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4GatewayAccountListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4GatewayAccountListApiResponse]:
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

) -> Response[MT4GatewayAccountListApiResponse]:
    """ List gateway accounts

     All STP gateway-account configuration entries on the MT4 server, paginated by stable internal Id.

    Manager-live read (round-trip). Each entry describes an external
    MT4 server connection used for STP order routing: public Name, an
    internal Id (stable identifier — used as the cursor key), the
    external server Login + Address, a NotifyLogins fixed-size array
    of 8 broker-side recipients, and a Flags bitmap. The wrapper's
    `Password` field (STP MT4 credential) is intentionally
    excluded from the v2 contract.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GatewayAccountListApiResponse]
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

) -> MT4GatewayAccountListApiResponse | None:
    """ List gateway accounts

     All STP gateway-account configuration entries on the MT4 server, paginated by stable internal Id.

    Manager-live read (round-trip). Each entry describes an external
    MT4 server connection used for STP order routing: public Name, an
    internal Id (stable identifier — used as the cursor key), the
    external server Login + Address, a NotifyLogins fixed-size array
    of 8 broker-side recipients, and a Flags bitmap. The wrapper's
    `Password` field (STP MT4 credential) is intentionally
    excluded from the v2 contract.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GatewayAccountListApiResponse
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

) -> Response[MT4GatewayAccountListApiResponse]:
    """ List gateway accounts

     All STP gateway-account configuration entries on the MT4 server, paginated by stable internal Id.

    Manager-live read (round-trip). Each entry describes an external
    MT4 server connection used for STP order routing: public Name, an
    internal Id (stable identifier — used as the cursor key), the
    external server Login + Address, a NotifyLogins fixed-size array
    of 8 broker-side recipients, and a Flags bitmap. The wrapper's
    `Password` field (STP MT4 credential) is intentionally
    excluded from the v2 contract.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GatewayAccountListApiResponse]
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

) -> MT4GatewayAccountListApiResponse | None:
    """ List gateway accounts

     All STP gateway-account configuration entries on the MT4 server, paginated by stable internal Id.

    Manager-live read (round-trip). Each entry describes an external
    MT4 server connection used for STP order routing: public Name, an
    internal Id (stable identifier — used as the cursor key), the
    external server Login + Address, a NotifyLogins fixed-size array
    of 8 broker-side recipients, and a Flags bitmap. The wrapper's
    `Password` field (STP MT4 credential) is intentionally
    excluded from the v2 contract.

    Args:
        trade_platform (UUID):
        limit (int | Unset):
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GatewayAccountListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
limit=limit,
cursor=cursor,

    )).parsed
