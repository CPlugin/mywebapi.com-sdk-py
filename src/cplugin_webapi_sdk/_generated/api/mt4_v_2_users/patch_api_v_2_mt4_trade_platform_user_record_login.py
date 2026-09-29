from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_user_api_response import MT4UserApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    login: int,
    *,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/MT4/{trade_platform}/UserRecord/{login}".format(trade_platform=quote(str(trade_platform), safe=""),login=quote(str(login), safe=""),),
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4UserApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4UserApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4UserApiResponse]:
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
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4UserApiResponse]:
    """ Patch account

     Type 2 mutator — partial update of a user record. Client sends a JSON object containing only the
    fields to change; the server reads the current record live from MT4 (Manager, not pump), overlays
    the patch, and writes back. Echoes the merged record.

    Unknown keys in the patch body are silently ignored (forwards-compat).
    Field-level validation is delegated to MT4 server — invalid values
    surface as `MT4Error` envelopes. Secret-preservation and
    computed-field protection are handled by the existing Type 1 ApplyTo
    mapper's ignore list.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
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
    x_request_timeout: float | Unset = UNSET,

) -> MT4UserApiResponse | None:
    """ Patch account

     Type 2 mutator — partial update of a user record. Client sends a JSON object containing only the
    fields to change; the server reads the current record live from MT4 (Manager, not pump), overlays
    the patch, and writes back. Echoes the merged record.

    Unknown keys in the patch body are silently ignored (forwards-compat).
    Field-level validation is delegated to MT4 server — invalid values
    surface as `MT4Error` envelopes. Secret-preservation and
    computed-field protection are handled by the existing Type 1 ApplyTo
    mapper's ignore list.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4UserApiResponse]:
    """ Patch account

     Type 2 mutator — partial update of a user record. Client sends a JSON object containing only the
    fields to change; the server reads the current record live from MT4 (Manager, not pump), overlays
    the patch, and writes back. Echoes the merged record.

    Unknown keys in the patch body are silently ignored (forwards-compat).
    Field-level validation is delegated to MT4 server — invalid values
    surface as `MT4Error` envelopes. Secret-preservation and
    computed-field protection are handled by the existing Type 1 ApplyTo
    mapper's ignore list.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
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
    x_request_timeout: float | Unset = UNSET,

) -> MT4UserApiResponse | None:
    """ Patch account

     Type 2 mutator — partial update of a user record. Client sends a JSON object containing only the
    fields to change; the server reads the current record live from MT4 (Manager, not pump), overlays
    the patch, and writes back. Echoes the merged record.

    Unknown keys in the patch body are silently ignored (forwards-compat).
    Field-level validation is delegated to MT4 server — invalid values
    surface as `MT4Error` envelopes. Secret-preservation and
    computed-field protection are handled by the existing Type 1 ApplyTo
    mapper's ignore list.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
x_request_timeout=x_request_timeout,

    )).parsed
