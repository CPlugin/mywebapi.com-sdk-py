from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_common_api_response import MT4CommonApiResponse
from ...models.mt4_common_update import MT4CommonUpdate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4CommonUpdate  |     MT4CommonUpdate  |     MT4CommonUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateCommon".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4CommonUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4CommonUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4CommonUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4CommonApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4CommonApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4CommonApiResponse]:
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
    body:    MT4CommonUpdate  |     MT4CommonUpdate  |     MT4CommonUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4CommonApiResponse]:
    r""" Update common config

     Update server-wide common settings — Type 1 mutator.

    Manager (live) call. Reads the current `ConCommon` from the
    MT4 server, overlays the fields in `MT4CommonUpdate` onto it
    (secret-preservation: fields not in the DTO keep their server
    value), and writes the merged struct back via
    `CfgUpdateCommon`.

    Preserved fields the DTO does not touch:
    <list type=\"bullet\"><item>Runtime counters (LastOrder, LastLogin, LostLogin,
            optimization timestamps, overnight rollover state).</item><item>Protocol identity
    (ServerVersion, ServerBuild).</item><item>Bind / web address arrays (variable-length nested
            collections — own endpoints planned).</item><item>Demo-account subsystem, paths,
    rollover/statement modes
            (sensitive admin areas with separate endpoints).</item></list>

    Idempotency-Key strongly recommended — overwriting common settings
    affects every connected client.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4CommonApiResponse]
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
    body:    MT4CommonUpdate  |     MT4CommonUpdate  |     MT4CommonUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4CommonApiResponse | None:
    r""" Update common config

     Update server-wide common settings — Type 1 mutator.

    Manager (live) call. Reads the current `ConCommon` from the
    MT4 server, overlays the fields in `MT4CommonUpdate` onto it
    (secret-preservation: fields not in the DTO keep their server
    value), and writes the merged struct back via
    `CfgUpdateCommon`.

    Preserved fields the DTO does not touch:
    <list type=\"bullet\"><item>Runtime counters (LastOrder, LastLogin, LostLogin,
            optimization timestamps, overnight rollover state).</item><item>Protocol identity
    (ServerVersion, ServerBuild).</item><item>Bind / web address arrays (variable-length nested
            collections — own endpoints planned).</item><item>Demo-account subsystem, paths,
    rollover/statement modes
            (sensitive admin areas with separate endpoints).</item></list>

    Idempotency-Key strongly recommended — overwriting common settings
    affects every connected client.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4CommonApiResponse
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
    body:    MT4CommonUpdate  |     MT4CommonUpdate  |     MT4CommonUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4CommonApiResponse]:
    r""" Update common config

     Update server-wide common settings — Type 1 mutator.

    Manager (live) call. Reads the current `ConCommon` from the
    MT4 server, overlays the fields in `MT4CommonUpdate` onto it
    (secret-preservation: fields not in the DTO keep their server
    value), and writes the merged struct back via
    `CfgUpdateCommon`.

    Preserved fields the DTO does not touch:
    <list type=\"bullet\"><item>Runtime counters (LastOrder, LastLogin, LostLogin,
            optimization timestamps, overnight rollover state).</item><item>Protocol identity
    (ServerVersion, ServerBuild).</item><item>Bind / web address arrays (variable-length nested
            collections — own endpoints planned).</item><item>Demo-account subsystem, paths,
    rollover/statement modes
            (sensitive admin areas with separate endpoints).</item></list>

    Idempotency-Key strongly recommended — overwriting common settings
    affects every connected client.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4CommonApiResponse]
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
    body:    MT4CommonUpdate  |     MT4CommonUpdate  |     MT4CommonUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4CommonApiResponse | None:
    r""" Update common config

     Update server-wide common settings — Type 1 mutator.

    Manager (live) call. Reads the current `ConCommon` from the
    MT4 server, overlays the fields in `MT4CommonUpdate` onto it
    (secret-preservation: fields not in the DTO keep their server
    value), and writes the merged struct back via
    `CfgUpdateCommon`.

    Preserved fields the DTO does not touch:
    <list type=\"bullet\"><item>Runtime counters (LastOrder, LastLogin, LostLogin,
            optimization timestamps, overnight rollover state).</item><item>Protocol identity
    (ServerVersion, ServerBuild).</item><item>Bind / web address arrays (variable-length nested
            collections — own endpoints planned).</item><item>Demo-account subsystem, paths,
    rollover/statement modes
            (sensitive admin areas with separate endpoints).</item></list>

    Idempotency-Key strongly recommended — overwriting common settings
    affects every connected client.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.
        body (MT4CommonUpdate | Unset): v2 Type 1 mutator DTO for MT4 server-wide common settings.
            Curated
            subset of the platform's `ConCommon` struct — exposes the fields
            most likely to need adjustment from a SaaS surface while leaving
            runtime counters, derived state, and the platform's internal arrays
            to the secret-preservation overlay on the controller side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4CommonApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
