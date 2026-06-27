from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_user_list_api_response import MT4UserListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    logins: list[int] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_logins: list[int] | Unset = UNSET
    if not isinstance(logins, Unset):
        json_logins = logins


    params["logins"] = json_logins


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/UserRecordsRequest".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4UserListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4UserListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4UserListApiResponse]:
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
    logins: list[int] | Unset = UNSET,

) -> Response[MT4UserListApiResponse]:
    """ Get accounts batch (live)

     Account records for a list of logins — live round-trip to MT4 server.

    Manager batch variant. Pass logins as repeated query parameters:
    `?logins=1001&logins=1002&logins=1003`. Server-side billing
    counts this as one Manager request regardless of the array length —
    prefer batch over a loop of single-login calls.

    Order in the response is **not** guaranteed to match the request — the
    wrapper returns a dictionary. Missing logins are silently omitted; the
    envelope is not an error envelope in that case.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
logins=logins,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    logins: list[int] | Unset = UNSET,

) -> MT4UserListApiResponse | None:
    """ Get accounts batch (live)

     Account records for a list of logins — live round-trip to MT4 server.

    Manager batch variant. Pass logins as repeated query parameters:
    `?logins=1001&logins=1002&logins=1003`. Server-side billing
    counts this as one Manager request regardless of the array length —
    prefer batch over a loop of single-login calls.

    Order in the response is **not** guaranteed to match the request — the
    wrapper returns a dictionary. Missing logins are silently omitted; the
    envelope is not an error envelope in that case.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
logins=logins,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    logins: list[int] | Unset = UNSET,

) -> Response[MT4UserListApiResponse]:
    """ Get accounts batch (live)

     Account records for a list of logins — live round-trip to MT4 server.

    Manager batch variant. Pass logins as repeated query parameters:
    `?logins=1001&logins=1002&logins=1003`. Server-side billing
    counts this as one Manager request regardless of the array length —
    prefer batch over a loop of single-login calls.

    Order in the response is **not** guaranteed to match the request — the
    wrapper returns a dictionary. Missing logins are silently omitted; the
    envelope is not an error envelope in that case.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
logins=logins,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    logins: list[int] | Unset = UNSET,

) -> MT4UserListApiResponse | None:
    """ Get accounts batch (live)

     Account records for a list of logins — live round-trip to MT4 server.

    Manager batch variant. Pass logins as repeated query parameters:
    `?logins=1001&logins=1002&logins=1003`. Server-side billing
    counts this as one Manager request regardless of the array length —
    prefer batch over a loop of single-login calls.

    Order in the response is **not** guaranteed to match the request — the
    wrapper returns a dictionary. Missing logins are silently omitted; the
    envelope is not an error envelope in that case.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
logins=logins,

    )).parsed
