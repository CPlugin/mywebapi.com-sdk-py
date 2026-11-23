from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_user_add_request import MT5UserAddRequest
from ...models.mt5_user_add_result_api_response import MT5UserAddResultApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5UserAddRequest  |     MT5UserAddRequest  |     MT5UserAddRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/UserAdd".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5UserAddRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5UserAddRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5UserAddRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5UserAddResultApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5UserAddResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5UserAddResultApiResponse]:
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
    body:    MT5UserAddRequest  |     MT5UserAddRequest  |     MT5UserAddRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserAddResultApiResponse]:
    """ Create a user account

     <br>
                 Creates a trading account on the trade server. Every field of the record is optional:
                 a field left out is not written to the new account, so it keeps the value the platform
                 starts it with — and that value is `None` for rights, so an account created without
                 `rights` cannot log in until the flag is granted. Send `rights` (at least
                 `Enabled`) to make the account usable.

                 A real trade server also refuses creation without a leverage (`MT_RET_ERR_PARAMS`):
                 send `leverage` together with the group.

    <br>
                 When the login field is absent or zero the server allocates one from the available
                 range; when no logins are left the call fails with the platform error
                 `MT_RET_USR_LOGIN_EXHAUSTED`. The group must be set, as well as the first or the
                 last name of the account holder; otherwise the call fails with `MT_RET_ERR_PARAMS`.
                 Adding an account whose login already exists fails with `MT_RET_USR_LOGIN_EXIST`.

    <br>
                 Passwords are checked against the group policy. When either the master or the investor
                 password is absent, both are regenerated to the group minimum length; a password the
                 policy refuses is replaced with a fresh pair and the creation is repeated up to ten
                 times. A failure of any other kind ends the call at once — a retry after a timeout
    could
                 create a second account, since the first attempt may have succeeded unseen.
                 The response carries the record as stored by the server, including the allocated login.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserAddResultApiResponse]
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
    body:    MT5UserAddRequest  |     MT5UserAddRequest  |     MT5UserAddRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserAddResultApiResponse | None:
    """ Create a user account

     <br>
                 Creates a trading account on the trade server. Every field of the record is optional:
                 a field left out is not written to the new account, so it keeps the value the platform
                 starts it with — and that value is `None` for rights, so an account created without
                 `rights` cannot log in until the flag is granted. Send `rights` (at least
                 `Enabled`) to make the account usable.

                 A real trade server also refuses creation without a leverage (`MT_RET_ERR_PARAMS`):
                 send `leverage` together with the group.

    <br>
                 When the login field is absent or zero the server allocates one from the available
                 range; when no logins are left the call fails with the platform error
                 `MT_RET_USR_LOGIN_EXHAUSTED`. The group must be set, as well as the first or the
                 last name of the account holder; otherwise the call fails with `MT_RET_ERR_PARAMS`.
                 Adding an account whose login already exists fails with `MT_RET_USR_LOGIN_EXIST`.

    <br>
                 Passwords are checked against the group policy. When either the master or the investor
                 password is absent, both are regenerated to the group minimum length; a password the
                 policy refuses is replaced with a fresh pair and the creation is repeated up to ten
                 times. A failure of any other kind ends the call at once — a retry after a timeout
    could
                 create a second account, since the first attempt may have succeeded unseen.
                 The response carries the record as stored by the server, including the allocated login.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserAddResultApiResponse
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
    body:    MT5UserAddRequest  |     MT5UserAddRequest  |     MT5UserAddRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserAddResultApiResponse]:
    """ Create a user account

     <br>
                 Creates a trading account on the trade server. Every field of the record is optional:
                 a field left out is not written to the new account, so it keeps the value the platform
                 starts it with — and that value is `None` for rights, so an account created without
                 `rights` cannot log in until the flag is granted. Send `rights` (at least
                 `Enabled`) to make the account usable.

                 A real trade server also refuses creation without a leverage (`MT_RET_ERR_PARAMS`):
                 send `leverage` together with the group.

    <br>
                 When the login field is absent or zero the server allocates one from the available
                 range; when no logins are left the call fails with the platform error
                 `MT_RET_USR_LOGIN_EXHAUSTED`. The group must be set, as well as the first or the
                 last name of the account holder; otherwise the call fails with `MT_RET_ERR_PARAMS`.
                 Adding an account whose login already exists fails with `MT_RET_USR_LOGIN_EXIST`.

    <br>
                 Passwords are checked against the group policy. When either the master or the investor
                 password is absent, both are regenerated to the group minimum length; a password the
                 policy refuses is replaced with a fresh pair and the creation is repeated up to ten
                 times. A failure of any other kind ends the call at once — a retry after a timeout
    could
                 create a second account, since the first attempt may have succeeded unseen.
                 The response carries the record as stored by the server, including the allocated login.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserAddResultApiResponse]
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
    body:    MT5UserAddRequest  |     MT5UserAddRequest  |     MT5UserAddRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserAddResultApiResponse | None:
    """ Create a user account

     <br>
                 Creates a trading account on the trade server. Every field of the record is optional:
                 a field left out is not written to the new account, so it keeps the value the platform
                 starts it with — and that value is `None` for rights, so an account created without
                 `rights` cannot log in until the flag is granted. Send `rights` (at least
                 `Enabled`) to make the account usable.

                 A real trade server also refuses creation without a leverage (`MT_RET_ERR_PARAMS`):
                 send `leverage` together with the group.

    <br>
                 When the login field is absent or zero the server allocates one from the available
                 range; when no logins are left the call fails with the platform error
                 `MT_RET_USR_LOGIN_EXHAUSTED`. The group must be set, as well as the first or the
                 last name of the account holder; otherwise the call fails with `MT_RET_ERR_PARAMS`.
                 Adding an account whose login already exists fails with `MT_RET_USR_LOGIN_EXIST`.

    <br>
                 Passwords are checked against the group policy. When either the master or the investor
                 password is absent, both are regenerated to the group minimum length; a password the
                 policy refuses is replaced with a fresh pair and the creation is repeated up to ten
                 times. A failure of any other kind ends the call at once — a retry after a timeout
    could
                 create a second account, since the first attempt may have succeeded unseen.
                 The response carries the record as stored by the server, including the allocated login.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.
        body (MT5UserAddRequest | Unset): Request body of the account-creation operation: the
            editable record plus the
                        optional login and the two passwords.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserAddResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
