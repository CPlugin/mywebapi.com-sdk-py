from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_sync import MT4Sync
from ...models.mt4_sync_api_response import MT4SyncApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4Sync  |     MT4Sync  |     MT4Sync  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateSync".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4Sync):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4Sync):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4Sync):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4SyncApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4SyncApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4SyncApiResponse]:
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
    body:    MT4Sync  |     MT4Sync  |     MT4Sync  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4SyncApiResponse]:
    r""" Update sync rule

     Update a chart-history synchronization rule — Type 1 mutator.

    Manager (live) call. Sync configurations are paged on the read
    side (see `CfgRequestSync`); the v2 contract identifies a
    rule by the composite key `(Server, Login)`. Flow:
    <list type=\"number\"><item>Read the current list via `CfgRequestSync`.</item><item>Find the entry
    whose `(Server, Login)` matches the
            body. Missing entry → NotFound envelope.</item><item>Apply DTO overlay onto the matched
    entry — the
            replication credential (`Password`) carried by the
            live struct is preserved.</item><item>Write the merged struct back.</item></list>
    Echoes the merged `MT4Sync` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SyncApiResponse]
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
    body:    MT4Sync  |     MT4Sync  |     MT4Sync  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4SyncApiResponse | None:
    r""" Update sync rule

     Update a chart-history synchronization rule — Type 1 mutator.

    Manager (live) call. Sync configurations are paged on the read
    side (see `CfgRequestSync`); the v2 contract identifies a
    rule by the composite key `(Server, Login)`. Flow:
    <list type=\"number\"><item>Read the current list via `CfgRequestSync`.</item><item>Find the entry
    whose `(Server, Login)` matches the
            body. Missing entry → NotFound envelope.</item><item>Apply DTO overlay onto the matched
    entry — the
            replication credential (`Password`) carried by the
            live struct is preserved.</item><item>Write the merged struct back.</item></list>
    Echoes the merged `MT4Sync` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SyncApiResponse
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
    body:    MT4Sync  |     MT4Sync  |     MT4Sync  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4SyncApiResponse]:
    r""" Update sync rule

     Update a chart-history synchronization rule — Type 1 mutator.

    Manager (live) call. Sync configurations are paged on the read
    side (see `CfgRequestSync`); the v2 contract identifies a
    rule by the composite key `(Server, Login)`. Flow:
    <list type=\"number\"><item>Read the current list via `CfgRequestSync`.</item><item>Find the entry
    whose `(Server, Login)` matches the
            body. Missing entry → NotFound envelope.</item><item>Apply DTO overlay onto the matched
    entry — the
            replication credential (`Password`) carried by the
            live struct is preserved.</item><item>Write the merged struct back.</item></list>
    Echoes the merged `MT4Sync` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4SyncApiResponse]
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
    body:    MT4Sync  |     MT4Sync  |     MT4Sync  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4SyncApiResponse | None:
    r""" Update sync rule

     Update a chart-history synchronization rule — Type 1 mutator.

    Manager (live) call. Sync configurations are paged on the read
    side (see `CfgRequestSync`); the v2 contract identifies a
    rule by the composite key `(Server, Login)`. Flow:
    <list type=\"number\"><item>Read the current list via `CfgRequestSync`.</item><item>Find the entry
    whose `(Server, Login)` matches the
            body. Missing entry → NotFound envelope.</item><item>Apply DTO overlay onto the matched
    entry — the
            replication credential (`Password`) carried by the
            live struct is preserved.</item><item>Write the merged struct back.</item></list>
    Echoes the merged `MT4Sync` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).
        body (MT4Sync | Unset): v2 DTO for a single MT4 chart-history synchronization rule.
            Curated
            subset of the platform's ConSync — drops the Reserved padding, the
            Next pointer chain, the unused port slot, AND the `Password`
            field (replication credentials to the upstream sync source).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4SyncApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
