from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_leverage_list_api_response import MT5LeverageListApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    groups: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["groups"] = groups


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/LeverageRequestArray".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5LeverageListApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5LeverageListApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5LeverageListApiResponse]:
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
    groups: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5LeverageListApiResponse]:
    r""" Floating margin configurations that apply to groups

     <br>
                Returns every floating margin configuration the trade server applies to at least one of
    the
                groups selected by the mask. The mask takes group names including the subgroup
                (`demo\demoforex`), several names separated by commas, and the wildcards `*` (any
                value) and `!` (exclude), for example `demo*,!demoforex` — every group whose name
                starts with `demo` except `demoforex`. An omitted mask selects every group.

    <br>
                The call blocks until the server answers. Every configuration is returned with its rules
    and
                tiers.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        groups (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5LeverageListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
groups=groups,
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
    groups: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5LeverageListApiResponse | None:
    r""" Floating margin configurations that apply to groups

     <br>
                Returns every floating margin configuration the trade server applies to at least one of
    the
                groups selected by the mask. The mask takes group names including the subgroup
                (`demo\demoforex`), several names separated by commas, and the wildcards `*` (any
                value) and `!` (exclude), for example `demo*,!demoforex` — every group whose name
                starts with `demo` except `demoforex`. An omitted mask selects every group.

    <br>
                The call blocks until the server answers. Every configuration is returned with its rules
    and
                tiers.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        groups (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5LeverageListApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
groups=groups,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    groups: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5LeverageListApiResponse]:
    r""" Floating margin configurations that apply to groups

     <br>
                Returns every floating margin configuration the trade server applies to at least one of
    the
                groups selected by the mask. The mask takes group names including the subgroup
                (`demo\demoforex`), several names separated by commas, and the wildcards `*` (any
                value) and `!` (exclude), for example `demo*,!demoforex` — every group whose name
                starts with `demo` except `demoforex`. An omitted mask selects every group.

    <br>
                The call blocks until the server answers. Every configuration is returned with its rules
    and
                tiers.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        groups (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5LeverageListApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
groups=groups,
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
    groups: str | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5LeverageListApiResponse | None:
    r""" Floating margin configurations that apply to groups

     <br>
                Returns every floating margin configuration the trade server applies to at least one of
    the
                groups selected by the mask. The mask takes group names including the subgroup
                (`demo\demoforex`), several names separated by commas, and the wildcards `*` (any
                value) and `!` (exclude), for example `demo*,!demoforex` — every group whose name
                starts with `demo` except `demoforex`. An omitted mask selects every group.

    <br>
                The call blocks until the server answers. Every configuration is returned with its rules
    and
                tiers.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        groups (str | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5LeverageListApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
groups=groups,
x_request_timeout=x_request_timeout,

    )).parsed
