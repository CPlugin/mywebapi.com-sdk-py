from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    login: int,
    *,
    body:    str  |     str  |     str  | Unset = UNSET,
    change_investor: bool | Unset = False,
    clean_pubkey: bool | Unset = False,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["changeInvestor"] = change_investor

    params["cleanPubkey"] = clean_pubkey


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/UserPasswordSet/{login}".format(trade_platform=quote(str(trade_platform), safe=""),login=quote(str(login), safe=""),),
        "params": params,
    }

    if isinstance(body, str):
        if not isinstance(body, Unset):
            _kwargs["json"] = body

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, str):
        if not isinstance(body, Unset):
            _kwargs["json"] = body

        headers["Content-Type"] = "application/json"
    if isinstance(body, str):
        if not isinstance(body, Unset):
            _kwargs["json"] = body

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BooleanApiResponse | None:
    if response.status_code == 200:
        response_200 = BooleanApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BooleanApiResponse]:
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
    body:    str  |     str  |     str  | Unset = UNSET,
    change_investor: bool | Unset = False,
    clean_pubkey: bool | Unset = False,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Set account password

     Set the account password — Type 1 mutator (direct overwrite).

    POST body: the new password as a JSON string. Optional query params:
    `changeInvestor=true` sets the read-only investor password instead
    of the primary one; `cleanPubkey=true` resets the public key alongside
    the password (caller's RSA-protected secondary auth).

    <br>
    This is a Type 1 mutator — full-replace semantics. The platform accepts
    the new password directly without a read-modify-write loop. There is no
    Type 2 (\"set only this field, leave the rest alone\") variant of password
    change because the password is itself a single field — the read step
    would be tautological.
    <br>
    Idempotency-Key is strongly recommended. A retried password change without
    the header risks setting it twice (the second call returns success even
    though the password is the same), which is harmless but generates audit
    noise. With the header, the second call short-circuits to the cached
    response.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        change_investor (bool | Unset):  Default: False.
        clean_pubkey (bool | Unset):  Default: False.
        x_request_timeout (float | Unset):
        body (str | Unset):
        body (str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
body=body,
change_investor=change_investor,
clean_pubkey=clean_pubkey,
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
    body:    str  |     str  |     str  | Unset = UNSET,
    change_investor: bool | Unset = False,
    clean_pubkey: bool | Unset = False,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Set account password

     Set the account password — Type 1 mutator (direct overwrite).

    POST body: the new password as a JSON string. Optional query params:
    `changeInvestor=true` sets the read-only investor password instead
    of the primary one; `cleanPubkey=true` resets the public key alongside
    the password (caller's RSA-protected secondary auth).

    <br>
    This is a Type 1 mutator — full-replace semantics. The platform accepts
    the new password directly without a read-modify-write loop. There is no
    Type 2 (\"set only this field, leave the rest alone\") variant of password
    change because the password is itself a single field — the read step
    would be tautological.
    <br>
    Idempotency-Key is strongly recommended. A retried password change without
    the header risks setting it twice (the second call returns success even
    though the password is the same), which is harmless but generates audit
    noise. With the header, the second call short-circuits to the cached
    response.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        change_investor (bool | Unset):  Default: False.
        clean_pubkey (bool | Unset):  Default: False.
        x_request_timeout (float | Unset):
        body (str | Unset):
        body (str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
body=body,
change_investor=change_investor,
clean_pubkey=clean_pubkey,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    login: int,
    *,
    client: AuthenticatedClient | Client,
    body:    str  |     str  |     str  | Unset = UNSET,
    change_investor: bool | Unset = False,
    clean_pubkey: bool | Unset = False,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Set account password

     Set the account password — Type 1 mutator (direct overwrite).

    POST body: the new password as a JSON string. Optional query params:
    `changeInvestor=true` sets the read-only investor password instead
    of the primary one; `cleanPubkey=true` resets the public key alongside
    the password (caller's RSA-protected secondary auth).

    <br>
    This is a Type 1 mutator — full-replace semantics. The platform accepts
    the new password directly without a read-modify-write loop. There is no
    Type 2 (\"set only this field, leave the rest alone\") variant of password
    change because the password is itself a single field — the read step
    would be tautological.
    <br>
    Idempotency-Key is strongly recommended. A retried password change without
    the header risks setting it twice (the second call returns success even
    though the password is the same), which is harmless but generates audit
    noise. With the header, the second call short-circuits to the cached
    response.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        change_investor (bool | Unset):  Default: False.
        clean_pubkey (bool | Unset):  Default: False.
        x_request_timeout (float | Unset):
        body (str | Unset):
        body (str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
login=login,
body=body,
change_investor=change_investor,
clean_pubkey=clean_pubkey,
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
    body:    str  |     str  |     str  | Unset = UNSET,
    change_investor: bool | Unset = False,
    clean_pubkey: bool | Unset = False,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Set account password

     Set the account password — Type 1 mutator (direct overwrite).

    POST body: the new password as a JSON string. Optional query params:
    `changeInvestor=true` sets the read-only investor password instead
    of the primary one; `cleanPubkey=true` resets the public key alongside
    the password (caller's RSA-protected secondary auth).

    <br>
    This is a Type 1 mutator — full-replace semantics. The platform accepts
    the new password directly without a read-modify-write loop. There is no
    Type 2 (\"set only this field, leave the rest alone\") variant of password
    change because the password is itself a single field — the read step
    would be tautological.
    <br>
    Idempotency-Key is strongly recommended. A retried password change without
    the header risks setting it twice (the second call returns success even
    though the password is the same), which is harmless but generates audit
    noise. With the header, the second call short-circuits to the cached
    response.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        change_investor (bool | Unset):  Default: False.
        clean_pubkey (bool | Unset):  Default: False.
        x_request_timeout (float | Unset):
        body (str | Unset):
        body (str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
body=body,
change_investor=change_investor,
clean_pubkey=clean_pubkey,
x_request_timeout=x_request_timeout,

    )).parsed
