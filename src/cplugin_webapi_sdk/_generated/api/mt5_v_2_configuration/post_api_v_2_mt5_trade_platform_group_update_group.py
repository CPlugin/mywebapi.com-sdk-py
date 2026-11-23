from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_con_group_api_response import MT5ConGroupApiResponse
from ...models.mt5_group_update_request import MT5GroupUpdateRequest
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    group: str,
    *,
    body:    MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/GroupUpdate/{group}".format(trade_platform=quote(str(trade_platform), safe=""),group=quote(str(group), safe=""),),
    }

    if isinstance(body, MT5GroupUpdateRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5GroupUpdateRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5GroupUpdateRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5ConGroupApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5ConGroupApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5ConGroupApiResponse]:
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
    body:    MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ConGroupApiResponse]:
    """ Change a group configuration

     <br>
                Writes the fields present in the body to the group with the given name. Only the fields
                the trading platform lets a manager change are accepted: the margin call level, the stop
                out level, the mode used to check them and the group trade options. A field left out of
                the body keeps its current value, and a body without any field is rejected.

    <br>
                The configuration is read from the trade server first, the body is applied over it and
    the
                result is written back, so a request never overwrites values it does not mention. The
                answer carries the configuration stored by the server after the write. Commission
    settings
                and per-symbol overrides are not part of this body.

    <br>
                The change is accepted only from the main trade server and only for a manager holding
    the
                rights to group margin and commission settings; any other case is answered with the
                platform error code. Repeat the request to retry after a failure that reported no
    result.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ConGroupApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
body=body,
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
    body:    MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ConGroupApiResponse | None:
    """ Change a group configuration

     <br>
                Writes the fields present in the body to the group with the given name. Only the fields
                the trading platform lets a manager change are accepted: the margin call level, the stop
                out level, the mode used to check them and the group trade options. A field left out of
                the body keeps its current value, and a body without any field is rejected.

    <br>
                The configuration is read from the trade server first, the body is applied over it and
    the
                result is written back, so a request never overwrites values it does not mention. The
                answer carries the configuration stored by the server after the write. Commission
    settings
                and per-symbol overrides are not part of this body.

    <br>
                The change is accepted only from the main trade server and only for a manager holding
    the
                rights to group margin and commission settings; any other case is answered with the
                platform error code. Repeat the request to retry after a failure that reported no
    result.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ConGroupApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    body:    MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ConGroupApiResponse]:
    """ Change a group configuration

     <br>
                Writes the fields present in the body to the group with the given name. Only the fields
                the trading platform lets a manager change are accepted: the margin call level, the stop
                out level, the mode used to check them and the group trade options. A field left out of
                the body keeps its current value, and a body without any field is rejected.

    <br>
                The configuration is read from the trade server first, the body is applied over it and
    the
                result is written back, so a request never overwrites values it does not mention. The
                answer carries the configuration stored by the server after the write. Commission
    settings
                and per-symbol overrides are not part of this body.

    <br>
                The change is accepted only from the main trade server and only for a manager holding
    the
                rights to group margin and commission settings; any other case is answered with the
                platform error code. Repeat the request to retry after a failure that reported no
    result.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ConGroupApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
body=body,
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
    body:    MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  |     MT5GroupUpdateRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ConGroupApiResponse | None:
    """ Change a group configuration

     <br>
                Writes the fields present in the body to the group with the given name. Only the fields
                the trading platform lets a manager change are accepted: the margin call level, the stop
                out level, the mode used to check them and the group trade options. A field left out of
                the body keeps its current value, and a body without any field is rejected.

    <br>
                The configuration is read from the trade server first, the body is applied over it and
    the
                result is written back, so a request never overwrites values it does not mention. The
                answer carries the configuration stored by the server after the write. Commission
    settings
                and per-symbol overrides are not part of this body.

    <br>
                The change is accepted only from the main trade server and only for a manager holding
    the
                rights to group margin and commission settings; any other case is answered with the
                platform error code. Repeat the request to retry after a failure that reported no
    result.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.
        body (MT5GroupUpdateRequest | Unset): Fields of a group configuration to change. Every
            field is optional: a field left out keeps
            its current server value, so the same body is safe to send repeatedly.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ConGroupApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
