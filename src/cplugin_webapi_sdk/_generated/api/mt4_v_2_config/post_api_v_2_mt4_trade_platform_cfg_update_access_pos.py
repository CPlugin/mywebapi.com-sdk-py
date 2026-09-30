from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_access import MT4Access
from ...models.mt4_access_api_response import MT4AccessApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    pos: int,
    *,
    body:    MT4Access  |     MT4Access  |     MT4Access  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateAccess/{pos}".format(trade_platform=quote(str(trade_platform), safe=""),pos=quote(str(pos), safe=""),),
    }

    if isinstance(body, MT4Access):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4Access):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4Access):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4AccessApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4AccessApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4AccessApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4Access  |     MT4Access  |     MT4Access  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4AccessApiResponse]:
    r""" Update IP firewall rule

     Update an IP firewall rule at a given list position — Type 1 mutator.

    Manager (live) call. The wrapper's `CfgUpdateAccess(cfg, pos)`
    signature requires a position rather than a unique-key lookup (the
    rule table has no stable identifiers — multiple rules can carry the
    same range/action/comment). The v2 endpoint exposes the position as
    a route parameter; callers must read the current list via
    `CfgRequestAccess` first and pass the index of the row to
    update. Flow:
    <list type=\"number\"><item>Read the live list via `CfgRequestAccess`.</item><item>Bounds-check
    `pos` against the list length — out of
            range yields a NotFound envelope.</item><item>Apply DTO overlay onto
    `list[pos]`.</item><item>Write back with `CfgUpdateAccess(merged,
    pos)`.</item></list>`IpFrom`/`IpTo` in the body must fit in `[0, uint.MaxValue]`
    — out-of-range values are rejected with `errorCode=Validation`
    before the Mapperly checked-narrowing cast can throw.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4AccessApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4Access  |     MT4Access  |     MT4Access  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4AccessApiResponse | None:
    r""" Update IP firewall rule

     Update an IP firewall rule at a given list position — Type 1 mutator.

    Manager (live) call. The wrapper's `CfgUpdateAccess(cfg, pos)`
    signature requires a position rather than a unique-key lookup (the
    rule table has no stable identifiers — multiple rules can carry the
    same range/action/comment). The v2 endpoint exposes the position as
    a route parameter; callers must read the current list via
    `CfgRequestAccess` first and pass the index of the row to
    update. Flow:
    <list type=\"number\"><item>Read the live list via `CfgRequestAccess`.</item><item>Bounds-check
    `pos` against the list length — out of
            range yields a NotFound envelope.</item><item>Apply DTO overlay onto
    `list[pos]`.</item><item>Write back with `CfgUpdateAccess(merged,
    pos)`.</item></list>`IpFrom`/`IpTo` in the body must fit in `[0, uint.MaxValue]`
    — out-of-range values are rejected with `errorCode=Validation`
    before the Mapperly checked-narrowing cast can throw.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4AccessApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4Access  |     MT4Access  |     MT4Access  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4AccessApiResponse]:
    r""" Update IP firewall rule

     Update an IP firewall rule at a given list position — Type 1 mutator.

    Manager (live) call. The wrapper's `CfgUpdateAccess(cfg, pos)`
    signature requires a position rather than a unique-key lookup (the
    rule table has no stable identifiers — multiple rules can carry the
    same range/action/comment). The v2 endpoint exposes the position as
    a route parameter; callers must read the current list via
    `CfgRequestAccess` first and pass the index of the row to
    update. Flow:
    <list type=\"number\"><item>Read the live list via `CfgRequestAccess`.</item><item>Bounds-check
    `pos` against the list length — out of
            range yields a NotFound envelope.</item><item>Apply DTO overlay onto
    `list[pos]`.</item><item>Write back with `CfgUpdateAccess(merged,
    pos)`.</item></list>`IpFrom`/`IpTo` in the body must fit in `[0, uint.MaxValue]`
    — out-of-range values are rejected with `errorCode=Validation`
    before the Mapperly checked-narrowing cast can throw.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4AccessApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4Access  |     MT4Access  |     MT4Access  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4AccessApiResponse | None:
    r""" Update IP firewall rule

     Update an IP firewall rule at a given list position — Type 1 mutator.

    Manager (live) call. The wrapper's `CfgUpdateAccess(cfg, pos)`
    signature requires a position rather than a unique-key lookup (the
    rule table has no stable identifiers — multiple rules can carry the
    same range/action/comment). The v2 endpoint exposes the position as
    a route parameter; callers must read the current list via
    `CfgRequestAccess` first and pass the index of the row to
    update. Flow:
    <list type=\"number\"><item>Read the live list via `CfgRequestAccess`.</item><item>Bounds-check
    `pos` against the list length — out of
            range yields a NotFound envelope.</item><item>Apply DTO overlay onto
    `list[pos]`.</item><item>Write back with `CfgUpdateAccess(merged,
    pos)`.</item></list>`IpFrom`/`IpTo` in the body must fit in `[0, uint.MaxValue]`
    — out-of-range values are rejected with `errorCode=Validation`
    before the Mapperly checked-narrowing cast can throw.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).
        body (MT4Access | Unset): v2 DTO for a single MT4 firewall (access) rule. Curated subset
            of
            the wrapper's ConAccess struct — drops the 17-int Reserved padding.
            IpFrom/IpTo are widened from uint to long so the JSON-serialized
            numeric value fits inside JS Number safely (no precision loss).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4AccessApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
