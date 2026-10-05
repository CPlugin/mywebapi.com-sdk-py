from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.string_api_response import StringApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    name: str,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT4/{trade_platform}/SrvFeederLog/{name}".format(trade_platform=quote(str(trade_platform), safe=""),name=quote(str(name), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StringApiResponse | None:
    if response.status_code == 200:
        response_200 = StringApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StringApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[StringApiResponse]:
    """ Get feeder log

     Server log for a single feeder by name (admin-only read).

    Manager (live) call to the platform's `SrvFeederLog(name)`. Returns
    the feeder's log buffer as a string (empty when the feeder is unknown
    or has no recent log activity). Payload is the raw log text — not an
    array of lines — to preserve formatting at the platform boundary.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        name (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StringApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
name=name,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> StringApiResponse | None:
    """ Get feeder log

     Server log for a single feeder by name (admin-only read).

    Manager (live) call to the platform's `SrvFeederLog(name)`. Returns
    the feeder's log buffer as a string (empty when the feeder is unknown
    or has no recent log activity). Payload is the raw log text — not an
    array of lines — to preserve formatting at the platform boundary.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        name (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StringApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
name=name,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[StringApiResponse]:
    """ Get feeder log

     Server log for a single feeder by name (admin-only read).

    Manager (live) call to the platform's `SrvFeederLog(name)`. Returns
    the feeder's log buffer as a string (empty when the feeder is unknown
    or has no recent log activity). Payload is the raw log text — not an
    array of lines — to preserve formatting at the platform boundary.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        name (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StringApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
name=name,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    name: str,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> StringApiResponse | None:
    """ Get feeder log

     Server log for a single feeder by name (admin-only read).

    Manager (live) call to the platform's `SrvFeederLog(name)`. Returns
    the feeder's log buffer as a string (empty when the feeder is unknown
    or has no recent log activity). Payload is the raw log text — not an
    array of lines — to preserve formatting at the platform boundary.

    **Timeout:** 30 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        name (str):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StringApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
name=name,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
