from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_user_api_response import MT4UserApiResponse
from ...models.mt4_user_update import MT4UserUpdate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    login: int,
    *,
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/UserRecordUpdate/{login}".format(trade_platform=quote(str(trade_platform), safe=""),login=quote(str(login), safe=""),),
    }

    if isinstance(body, MT4UserUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4UserUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4UserUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

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
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4UserApiResponse]:
    r""" Update account

     Update an account record — Type 1 mutator with secret-preservation read.

    <br>
    Surface-level Type 1 semantics: client submits the full `MT4UserUpdate`
    DTO and the server writes it back. Implementation requires an extra
    read step because the wrapper `UserRecord` struct contains
    secret/computed/read-only fields the v2 input DTO deliberately omits
    (Password, OTPSecret, LastDate, etc.). Without the read step those
    would be zeroed out by the write.
    <br>
    Flow:
    <list type=\"number\"><item>Fetch the existing record via `UserRecordsRequest` (live, not pump
    cache).</item><item>Apply the DTO over the in-memory record using `ApplyTo`. Secrets and read-only
    fields are `[MapperIgnoreTarget]`'d so they survive.</item><item>Write the modified record back via
    `UserRecordUpdate`.</item></list><br><b>This is NOT Type 2.</b> Type 2 mutators (single-field) are
    deferred
    to a later release and will accept just the field name + value, doing
    the read-modify-write entirely server-side. Both flows happen to use
    the same read-modify-write structure on the implementation side — the
    difference is what the client submits.
    <br>
    Idempotency-Key is strongly recommended; without it a retried update
    risks silently overwriting concurrent edits that happened between
    the original send and the retry.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
body=body,
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
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4UserApiResponse | None:
    r""" Update account

     Update an account record — Type 1 mutator with secret-preservation read.

    <br>
    Surface-level Type 1 semantics: client submits the full `MT4UserUpdate`
    DTO and the server writes it back. Implementation requires an extra
    read step because the wrapper `UserRecord` struct contains
    secret/computed/read-only fields the v2 input DTO deliberately omits
    (Password, OTPSecret, LastDate, etc.). Without the read step those
    would be zeroed out by the write.
    <br>
    Flow:
    <list type=\"number\"><item>Fetch the existing record via `UserRecordsRequest` (live, not pump
    cache).</item><item>Apply the DTO over the in-memory record using `ApplyTo`. Secrets and read-only
    fields are `[MapperIgnoreTarget]`'d so they survive.</item><item>Write the modified record back via
    `UserRecordUpdate`.</item></list><br><b>This is NOT Type 2.</b> Type 2 mutators (single-field) are
    deferred
    to a later release and will accept just the field name + value, doing
    the read-modify-write entirely server-side. Both flows happen to use
    the same read-modify-write structure on the implementation side — the
    difference is what the client submits.
    <br>
    Idempotency-Key is strongly recommended; without it a retried update
    risks silently overwriting concurrent edits that happened between
    the original send and the retry.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.

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
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4UserApiResponse]:
    r""" Update account

     Update an account record — Type 1 mutator with secret-preservation read.

    <br>
    Surface-level Type 1 semantics: client submits the full `MT4UserUpdate`
    DTO and the server writes it back. Implementation requires an extra
    read step because the wrapper `UserRecord` struct contains
    secret/computed/read-only fields the v2 input DTO deliberately omits
    (Password, OTPSecret, LastDate, etc.). Without the read step those
    would be zeroed out by the write.
    <br>
    Flow:
    <list type=\"number\"><item>Fetch the existing record via `UserRecordsRequest` (live, not pump
    cache).</item><item>Apply the DTO over the in-memory record using `ApplyTo`. Secrets and read-only
    fields are `[MapperIgnoreTarget]`'d so they survive.</item><item>Write the modified record back via
    `UserRecordUpdate`.</item></list><br><b>This is NOT Type 2.</b> Type 2 mutators (single-field) are
    deferred
    to a later release and will accept just the field name + value, doing
    the read-modify-write entirely server-side. Both flows happen to use
    the same read-modify-write structure on the implementation side — the
    difference is what the client submits.
    <br>
    Idempotency-Key is strongly recommended; without it a retried update
    risks silently overwriting concurrent edits that happened between
    the original send and the retry.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
body=body,
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
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4UserApiResponse | None:
    r""" Update account

     Update an account record — Type 1 mutator with secret-preservation read.

    <br>
    Surface-level Type 1 semantics: client submits the full `MT4UserUpdate`
    DTO and the server writes it back. Implementation requires an extra
    read step because the wrapper `UserRecord` struct contains
    secret/computed/read-only fields the v2 input DTO deliberately omits
    (Password, OTPSecret, LastDate, etc.). Without the read step those
    would be zeroed out by the write.
    <br>
    Flow:
    <list type=\"number\"><item>Fetch the existing record via `UserRecordsRequest` (live, not pump
    cache).</item><item>Apply the DTO over the in-memory record using `ApplyTo`. Secrets and read-only
    fields are `[MapperIgnoreTarget]`'d so they survive.</item><item>Write the modified record back via
    `UserRecordUpdate`.</item></list><br><b>This is NOT Type 2.</b> Type 2 mutators (single-field) are
    deferred
    to a later release and will accept just the field name + value, doing
    the read-modify-write entirely server-side. Both flows happen to use
    the same read-modify-write structure on the implementation side — the
    difference is what the client submits.
    <br>
    Idempotency-Key is strongly recommended; without it a retried update
    risks silently overwriting concurrent edits that happened between
    the original send and the retry.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.
        body (MT4UserUpdate | Unset): Type 1 mutator input — full-replace shape for
            `UserRecordUpdate`.
            Client submits every non-secret, non-read-only, non-computed field; the
            handler reads the current record from MT4 server, copies the secrets and
            read-only fields off it, applies this DTO over the rest, and writes the
            modified structure back.

            Read-only fields that do NOT appear here (preserved by the server-side
            read step):
              * `Login` — passed as a path parameter, immutable identity.
              * `RegistrationDate` — set once on creation, never updated.
              * `LastDate`, `LastIP` — assigned by MT4 server during login.
              * `PrevMonthBalance`, `PrevBalance`, `PrevMonthEquity`,
                `PrevEquity` — derived server-side at reporting close.

            Secret fields that do NOT appear here (preserved by the server-side
            read step; use dedicated endpoints to change them):
              * `Password`, `PasswordInvestor`, `PasswordPhone` —
                change via `POST UserPasswordSet`.
              * `OTPSecret` — provisioned via separate admin flow.
              * `APIData` — wrapper-internal blob, never client-controlled.

            <br><b>Note on Balance/Credit:</b> these fields ARE accepted here because the
            wrapper `UserRecordUpdate` writes them directly. However, the audit-
            trail-preserving way to move money is the dedicated balance operation
            endpoints (forthcoming) — submitting Balance via this DTO bypasses the
            audit log on MT4 server side.

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
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
