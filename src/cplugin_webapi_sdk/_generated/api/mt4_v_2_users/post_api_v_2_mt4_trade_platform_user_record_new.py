from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_user_api_response import MT4UserApiResponse
from ...models.mt4_user_create import MT4UserCreate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4UserCreate  |     MT4UserCreate  |     MT4UserCreate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/UserRecordNew".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4UserCreate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4UserCreate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4UserCreate):
        
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
    *,
    client: AuthenticatedClient | Client,
    body:    MT4UserCreate  |     MT4UserCreate  |     MT4UserCreate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4UserApiResponse]:
    """ Create account

     Create a new account — Type 1 mutator.

    POST mutator. Pass the full `MT4UserCreate` DTO. Set
    `Login = 0` to let MT4 server assign the next free id, or
    request a specific id by setting `Login > 0` (the server
    rejects collisions with an MT4 error envelope).

    The platform accepts the account with empty password bytes; clients
    MUST follow up with `POST UserPasswordSet/{login}` before the
    account is usable.

    Idempotency-Key strongly recommended — a retried create without it
    can land twice when the original response was lost on the wire,
    burning a second login id from the broker's sequence.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserApiResponse]
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
    body:    MT4UserCreate  |     MT4UserCreate  |     MT4UserCreate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4UserApiResponse | None:
    """ Create account

     Create a new account — Type 1 mutator.

    POST mutator. Pass the full `MT4UserCreate` DTO. Set
    `Login = 0` to let MT4 server assign the next free id, or
    request a specific id by setting `Login > 0` (the server
    rejects collisions with an MT4 error envelope).

    The platform accepts the account with empty password bytes; clients
    MUST follow up with `POST UserPasswordSet/{login}` before the
    account is usable.

    Idempotency-Key strongly recommended — a retried create without it
    can land twice when the original response was lost on the wire,
    burning a second login id from the broker's sequence.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserApiResponse
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
    body:    MT4UserCreate  |     MT4UserCreate  |     MT4UserCreate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4UserApiResponse]:
    """ Create account

     Create a new account — Type 1 mutator.

    POST mutator. Pass the full `MT4UserCreate` DTO. Set
    `Login = 0` to let MT4 server assign the next free id, or
    request a specific id by setting `Login > 0` (the server
    rejects collisions with an MT4 error envelope).

    The platform accepts the account with empty password bytes; clients
    MUST follow up with `POST UserPasswordSet/{login}` before the
    account is usable.

    Idempotency-Key strongly recommended — a retried create without it
    can land twice when the original response was lost on the wire,
    burning a second login id from the broker's sequence.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4UserApiResponse]
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
    body:    MT4UserCreate  |     MT4UserCreate  |     MT4UserCreate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4UserApiResponse | None:
    """ Create account

     Create a new account — Type 1 mutator.

    POST mutator. Pass the full `MT4UserCreate` DTO. Set
    `Login = 0` to let MT4 server assign the next free id, or
    request a specific id by setting `Login > 0` (the server
    rejects collisions with an MT4 error envelope).

    The platform accepts the account with empty password bytes; clients
    MUST follow up with `POST UserPasswordSet/{login}` before the
    account is usable.

    Idempotency-Key strongly recommended — a retried create without it
    can land twice when the original response was lost on the wire,
    burning a second login id from the broker's sequence.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.
        body (MT4UserCreate | Unset): Type 1 mutator input — full create shape for
            `UserRecordNew`.
            Same writable fields as MT4UserUpdate minus the explicit
            `Balance`/`Credit` (those should come through dedicated balance
            operations after the account exists). The platform allocates the next free
            login id when `Login = 0`; clients may also request a specific id by
            setting `Login > 0` (the server rejects collisions).

            Password / OTP / API-data fields are NOT on this DTO. After successful
            creation, set the initial password via a separate
            `POST UserPasswordSet/{login}` call. The platform accepts the new
            account with empty password bytes; the password endpoint lifts it to
            usable credentials.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4UserApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
