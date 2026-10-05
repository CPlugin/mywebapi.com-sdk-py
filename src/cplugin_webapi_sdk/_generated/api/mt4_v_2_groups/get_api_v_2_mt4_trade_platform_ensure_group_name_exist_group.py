from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    group: str,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/EnsureGroupNameExist/{group}".format(trade_platform=quote(str(trade_platform), safe=""),group=quote(str(group), safe=""),),
    }


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
    group: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Check group exists

     Checks whether a trading group exists on the connected MT4 server. Useful as a validation pre-flight
    before creating users, moving users between groups, or wiring up automated provisioning.

    Manager-live read. The platform's `EnsureGroupNameExist` helper
    is internal/private, so this v2 endpoint re-implements the check
    directly: enumerate the full group catalog via
    `GroupsRequest` and look up the key. The same Manager request
    is incurred either way; there is no cheaper \"exists\" call in the
    MT4 trade-server surface.

    Returns `true` if the group is configured on the server,
    `false` otherwise. Group lookup is case-sensitive (MT4 group
    names are case-sensitive in the underlying API).

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Check group exists

     Checks whether a trading group exists on the connected MT4 server. Useful as a validation pre-flight
    before creating users, moving users between groups, or wiring up automated provisioning.

    Manager-live read. The platform's `EnsureGroupNameExist` helper
    is internal/private, so this v2 endpoint re-implements the check
    directly: enumerate the full group catalog via
    `GroupsRequest` and look up the key. The same Manager request
    is incurred either way; there is no cheaper \"exists\" call in the
    MT4 trade-server surface.

    Returns `true` if the group is configured on the server,
    `false` otherwise. Group lookup is case-sensitive (MT4 group
    names are case-sensitive in the underlying API).

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Check group exists

     Checks whether a trading group exists on the connected MT4 server. Useful as a validation pre-flight
    before creating users, moving users between groups, or wiring up automated provisioning.

    Manager-live read. The platform's `EnsureGroupNameExist` helper
    is internal/private, so this v2 endpoint re-implements the check
    directly: enumerate the full group catalog via
    `GroupsRequest` and look up the key. The same Manager request
    is incurred either way; there is no cheaper \"exists\" call in the
    MT4 trade-server surface.

    Returns `true` if the group is configured on the server,
    `false` otherwise. Group lookup is case-sensitive (MT4 group
    names are case-sensitive in the underlying API).

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Check group exists

     Checks whether a trading group exists on the connected MT4 server. Useful as a validation pre-flight
    before creating users, moving users between groups, or wiring up automated provisioning.

    Manager-live read. The platform's `EnsureGroupNameExist` helper
    is internal/private, so this v2 endpoint re-implements the check
    directly: enumerate the full group catalog via
    `GroupsRequest` and look up the key. The same Manager request
    is incurred either way; there is no cheaper \"exists\" call in the
    MT4 trade-server surface.

    Returns `true` if the group is configured on the server,
    `false` otherwise. Group lookup is case-sensitive (MT4 group
    names are case-sensitive in the underlying API).

    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
