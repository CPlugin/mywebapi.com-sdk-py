from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_manager_rights import MT4ManagerRights
from ...models.mt4_manager_rights_api_response import MT4ManagerRightsApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4ManagerRights  |     MT4ManagerRights  |     MT4ManagerRights  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateManager".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4ManagerRights):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4ManagerRights):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4ManagerRights):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4ManagerRightsApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4ManagerRightsApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4ManagerRightsApiResponse]:
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
    body:    MT4ManagerRights  |     MT4ManagerRights  |     MT4ManagerRights  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ManagerRightsApiResponse]:
    """ Update manager config

     Update a manager-account configuration — Type 1 mutator.

    Manager (live) call. Manager-account entries are paged on the read
    side (see `CfgRequestManager`); the v2 contract identifies an
    entry by `Login`. Flow: read live list → match by Login →
    overlay (19 permission flags + IP filter + MailBox/Groups/InfoDepth)
    → write back. The wrapper's `Name` (read-only — server sets
    it), `SecGroups` (32-entry permission table), `ExpTime`,
    `Unused`, and `Reserved` are preserved.
    <br>`IpFrom`/`IpTo` in the body are `long` (DTO widens
    the wrapper's `uint` for safe JSON numerics) — values outside
    `[0, uint.MaxValue]` are rejected with
    `errorCode=Validation` before `ApplyTo`, to avoid a
    runtime `OverflowException` from Mapperly's checked cast.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ManagerRightsApiResponse]
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
    body:    MT4ManagerRights  |     MT4ManagerRights  |     MT4ManagerRights  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ManagerRightsApiResponse | None:
    """ Update manager config

     Update a manager-account configuration — Type 1 mutator.

    Manager (live) call. Manager-account entries are paged on the read
    side (see `CfgRequestManager`); the v2 contract identifies an
    entry by `Login`. Flow: read live list → match by Login →
    overlay (19 permission flags + IP filter + MailBox/Groups/InfoDepth)
    → write back. The wrapper's `Name` (read-only — server sets
    it), `SecGroups` (32-entry permission table), `ExpTime`,
    `Unused`, and `Reserved` are preserved.
    <br>`IpFrom`/`IpTo` in the body are `long` (DTO widens
    the wrapper's `uint` for safe JSON numerics) — values outside
    `[0, uint.MaxValue]` are rejected with
    `errorCode=Validation` before `ApplyTo`, to avoid a
    runtime `OverflowException` from Mapperly's checked cast.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ManagerRightsApiResponse
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
    body:    MT4ManagerRights  |     MT4ManagerRights  |     MT4ManagerRights  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ManagerRightsApiResponse]:
    """ Update manager config

     Update a manager-account configuration — Type 1 mutator.

    Manager (live) call. Manager-account entries are paged on the read
    side (see `CfgRequestManager`); the v2 contract identifies an
    entry by `Login`. Flow: read live list → match by Login →
    overlay (19 permission flags + IP filter + MailBox/Groups/InfoDepth)
    → write back. The wrapper's `Name` (read-only — server sets
    it), `SecGroups` (32-entry permission table), `ExpTime`,
    `Unused`, and `Reserved` are preserved.
    <br>`IpFrom`/`IpTo` in the body are `long` (DTO widens
    the wrapper's `uint` for safe JSON numerics) — values outside
    `[0, uint.MaxValue]` are rejected with
    `errorCode=Validation` before `ApplyTo`, to avoid a
    runtime `OverflowException` from Mapperly's checked cast.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ManagerRightsApiResponse]
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
    body:    MT4ManagerRights  |     MT4ManagerRights  |     MT4ManagerRights  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ManagerRightsApiResponse | None:
    """ Update manager config

     Update a manager-account configuration — Type 1 mutator.

    Manager (live) call. Manager-account entries are paged on the read
    side (see `CfgRequestManager`); the v2 contract identifies an
    entry by `Login`. Flow: read live list → match by Login →
    overlay (19 permission flags + IP filter + MailBox/Groups/InfoDepth)
    → write back. The wrapper's `Name` (read-only — server sets
    it), `SecGroups` (32-entry permission table), `ExpTime`,
    `Unused`, and `Reserved` are preserved.
    <br>`IpFrom`/`IpTo` in the body are `long` (DTO widens
    the wrapper's `uint` for safe JSON numerics) — values outside
    `[0, uint.MaxValue]` are rejected with
    `errorCode=Validation` before `ApplyTo`, to avoid a
    runtime `OverflowException` from Mapperly's checked cast.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).
        body (MT4ManagerRights | Unset): v2 DTO for an MT4 manager-account configuration entry.
            Curated subset
            of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
            the 19 boolean permission rights, IP-filter fields, and InfoDepth.
            Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
            IPFrom/IPTo are widened from uint to long so the JSON-serialized value
            fits inside JS Number safely (no precision loss).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ManagerRightsApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
