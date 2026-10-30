from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_group_api_response import MT4GroupApiResponse
from ...models.mt4_group_update import MT4GroupUpdate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    group: str,
    *,
    body:    MT4GroupUpdate  |     MT4GroupUpdate  |     MT4GroupUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/GroupRecordUpdate/{group}".format(trade_platform=quote(str(trade_platform), safe=""),group=quote(str(group), safe=""),),
    }

    if isinstance(body, MT4GroupUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4GroupUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4GroupUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4GroupApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4GroupApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4GroupApiResponse]:
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
    body:    MT4GroupUpdate  |     MT4GroupUpdate  |     MT4GroupUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4GroupApiResponse]:
    """ Update trading group

     Update a group configuration — Type 1 mutator with secret-preservation read.

    <br>
    Same flow as `UserRecordUpdate`: read the existing
    `ConGroup` from the MT4 server, overlay the
    `MT4GroupUpdate` DTO over the in-memory record, write the
    merged structure back. Preserves SMTP credentials, template paths,
    SecuritiesHash, reserved arrays, the nested SecGroups/SecMargins
    arrays, and NewsLanguages — none of those are on the input DTO so
    they survive untouched.
    <br>
    Wraps the platform's `CfgUpdateGroup` — v2 renames to
    `GroupRecordUpdate` for consistency with
    `UserRecordUpdate`; the underlying platform call is the same as
    v1's `POST CfgUpdateGroup` endpoint.
    <br>
    Idempotency-Key strongly recommended for safe retries.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GroupApiResponse]
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
    body:    MT4GroupUpdate  |     MT4GroupUpdate  |     MT4GroupUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4GroupApiResponse | None:
    """ Update trading group

     Update a group configuration — Type 1 mutator with secret-preservation read.

    <br>
    Same flow as `UserRecordUpdate`: read the existing
    `ConGroup` from the MT4 server, overlay the
    `MT4GroupUpdate` DTO over the in-memory record, write the
    merged structure back. Preserves SMTP credentials, template paths,
    SecuritiesHash, reserved arrays, the nested SecGroups/SecMargins
    arrays, and NewsLanguages — none of those are on the input DTO so
    they survive untouched.
    <br>
    Wraps the platform's `CfgUpdateGroup` — v2 renames to
    `GroupRecordUpdate` for consistency with
    `UserRecordUpdate`; the underlying platform call is the same as
    v1's `POST CfgUpdateGroup` endpoint.
    <br>
    Idempotency-Key strongly recommended for safe retries.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GroupApiResponse
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
    body:    MT4GroupUpdate  |     MT4GroupUpdate  |     MT4GroupUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4GroupApiResponse]:
    """ Update trading group

     Update a group configuration — Type 1 mutator with secret-preservation read.

    <br>
    Same flow as `UserRecordUpdate`: read the existing
    `ConGroup` from the MT4 server, overlay the
    `MT4GroupUpdate` DTO over the in-memory record, write the
    merged structure back. Preserves SMTP credentials, template paths,
    SecuritiesHash, reserved arrays, the nested SecGroups/SecMargins
    arrays, and NewsLanguages — none of those are on the input DTO so
    they survive untouched.
    <br>
    Wraps the platform's `CfgUpdateGroup` — v2 renames to
    `GroupRecordUpdate` for consistency with
    `UserRecordUpdate`; the underlying platform call is the same as
    v1's `POST CfgUpdateGroup` endpoint.
    <br>
    Idempotency-Key strongly recommended for safe retries.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GroupApiResponse]
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
    body:    MT4GroupUpdate  |     MT4GroupUpdate  |     MT4GroupUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4GroupApiResponse | None:
    """ Update trading group

     Update a group configuration — Type 1 mutator with secret-preservation read.

    <br>
    Same flow as `UserRecordUpdate`: read the existing
    `ConGroup` from the MT4 server, overlay the
    `MT4GroupUpdate` DTO over the in-memory record, write the
    merged structure back. Preserves SMTP credentials, template paths,
    SecuritiesHash, reserved arrays, the nested SecGroups/SecMargins
    arrays, and NewsLanguages — none of those are on the input DTO so
    they survive untouched.
    <br>
    Wraps the platform's `CfgUpdateGroup` — v2 renames to
    `GroupRecordUpdate` for consistency with
    `UserRecordUpdate`; the underlying platform call is the same as
    v1's `POST CfgUpdateGroup` endpoint.
    <br>
    Idempotency-Key strongly recommended for safe retries.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.
        body (MT4GroupUpdate | Unset): Type 1 mutator input — full-replace shape for
            `GroupRecordUpdate`.
            Same field set as the read DTO MT4Group minus the immutable
            group name (path parameter) and the derived `SecMarginsTotal`
            (computed from SecMargins length).

            Fields preserved by the server-side read step (NOT on this DTO):
              * `Group` — path param, immutable identity.
              * `SmtpServer`, `SmtpLogin`, `SmtpPassword` — SMTP creds,
                never client-controlled.
              * `Templates` — server-side filesystem path.
              * `SecuritiesHash` — opaque platform bookkeeping.
              * `Reserved`, `UnusedRights` — reserved arrays.
              * `SecGroups[32]`, `SecMargins[128]` — nested arrays, planned
                as dedicated v2 endpoints.
              * `NewsLanguages`, `NewsLanguagesTotal` — separate management.
              * `SecMarginsTotal` — derived from SecMargins length.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GroupApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
