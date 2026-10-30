from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.json_node_api_response import JsonNodeApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body: Any,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/ExternalCommandJSON".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> JsonNodeApiResponse | None:
    if response.status_code == 200:
        response_200 = JsonNodeApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[JsonNodeApiResponse]:
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
    body: Any,
    x_request_timeout: float | Unset = UNSET,

) -> Response[JsonNodeApiResponse]:
    """ Send plugin command (JSON)

     Plugin custom-command channel with JSON payload in both directions.

    Manager (live) call wrapping `ExternalCommandJSON`. The MT4
    server forwards the body to whichever installed plugin claims the
    command first; the first plugin returning `RET_OK` wins and its
    response becomes the v2 payload. The request body is sent verbatim
    (no field renaming, no schema enforcement) so the plugin author
    owns the over-the-wire contract on both ends.

    The platform trio (`ExternalCommand<TIn,TOut>` for binary
    marshal, `ExternalCommandCustom<T>` for caller-supplied
    serializer) is intentionally not exposed in v2 — those variants
    require compile-time struct layouts shared between client and
    plugin, which a REST surface cannot guarantee. Plugin developers
    who need binary transport should keep using the platform directly
    from the WebAPI process or build a dedicated binary endpoint.

    Idempotency-Key is strongly recommended — plugins may have side
    effects, and the channel itself gives no read-modify-write
    semantics.

    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (Any): Any JSON value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonNodeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
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
    body: Any,
    x_request_timeout: float | Unset = UNSET,

) -> JsonNodeApiResponse | None:
    """ Send plugin command (JSON)

     Plugin custom-command channel with JSON payload in both directions.

    Manager (live) call wrapping `ExternalCommandJSON`. The MT4
    server forwards the body to whichever installed plugin claims the
    command first; the first plugin returning `RET_OK` wins and its
    response becomes the v2 payload. The request body is sent verbatim
    (no field renaming, no schema enforcement) so the plugin author
    owns the over-the-wire contract on both ends.

    The platform trio (`ExternalCommand<TIn,TOut>` for binary
    marshal, `ExternalCommandCustom<T>` for caller-supplied
    serializer) is intentionally not exposed in v2 — those variants
    require compile-time struct layouts shared between client and
    plugin, which a REST surface cannot guarantee. Plugin developers
    who need binary transport should keep using the platform directly
    from the WebAPI process or build a dedicated binary endpoint.

    Idempotency-Key is strongly recommended — plugins may have side
    effects, and the channel itself gives no read-modify-write
    semantics.

    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (Any): Any JSON value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsonNodeApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: Any,
    x_request_timeout: float | Unset = UNSET,

) -> Response[JsonNodeApiResponse]:
    """ Send plugin command (JSON)

     Plugin custom-command channel with JSON payload in both directions.

    Manager (live) call wrapping `ExternalCommandJSON`. The MT4
    server forwards the body to whichever installed plugin claims the
    command first; the first plugin returning `RET_OK` wins and its
    response becomes the v2 payload. The request body is sent verbatim
    (no field renaming, no schema enforcement) so the plugin author
    owns the over-the-wire contract on both ends.

    The platform trio (`ExternalCommand<TIn,TOut>` for binary
    marshal, `ExternalCommandCustom<T>` for caller-supplied
    serializer) is intentionally not exposed in v2 — those variants
    require compile-time struct layouts shared between client and
    plugin, which a REST surface cannot guarantee. Plugin developers
    who need binary transport should keep using the platform directly
    from the WebAPI process or build a dedicated binary endpoint.

    Idempotency-Key is strongly recommended — plugins may have side
    effects, and the channel itself gives no read-modify-write
    semantics.

    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (Any): Any JSON value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[JsonNodeApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
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
    body: Any,
    x_request_timeout: float | Unset = UNSET,

) -> JsonNodeApiResponse | None:
    """ Send plugin command (JSON)

     Plugin custom-command channel with JSON payload in both directions.

    Manager (live) call wrapping `ExternalCommandJSON`. The MT4
    server forwards the body to whichever installed plugin claims the
    command first; the first plugin returning `RET_OK` wins and its
    response becomes the v2 payload. The request body is sent verbatim
    (no field renaming, no schema enforcement) so the plugin author
    owns the over-the-wire contract on both ends.

    The platform trio (`ExternalCommand<TIn,TOut>` for binary
    marshal, `ExternalCommandCustom<T>` for caller-supplied
    serializer) is intentionally not exposed in v2 — those variants
    require compile-time struct layouts shared between client and
    plugin, which a REST surface cannot guarantee. Plugin developers
    who need binary transport should keep using the platform directly
    from the WebAPI process or build a dedicated binary endpoint.

    Idempotency-Key is strongly recommended — plugins may have side
    effects, and the channel itself gives no read-modify-write
    semantics.

    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (Any): Any JSON value.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        JsonNodeApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
