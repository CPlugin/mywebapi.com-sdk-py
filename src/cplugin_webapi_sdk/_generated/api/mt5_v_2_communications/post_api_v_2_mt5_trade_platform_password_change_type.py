from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_result_api_response import MT5ResultApiResponse
from ...models.users_passwords import UsersPasswords
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    type_: UsersPasswords,
    *,
    body:    str  |     str  |     str  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/PasswordChange/{type_}".format(trade_platform=quote(str(trade_platform), safe=""),type_=quote(str(type_), safe=""),),
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



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5ResultApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5ResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5ResultApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    type_: UsersPasswords,
    *,
    client: AuthenticatedClient | Client,
    body:    str  |     str  |     str  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultApiResponse]:
    """ Change the password of the manager account used by the connection

     Replaces the stored password of the account the API uses to connect to the trade server. The
    change is made by the account itself and applies to the password type given in the route:
    `Main`, `Investor`, `API` or `Trader`. Any other value is refused.

    <br>
    The connection settings kept by this API are not updated by this call: the next connection
    attempt still presents the old password and the platform refuses it until the settings are
    brought in line. Change the password here only together with the stored settings.


    The new password must contain at least two of the three character kinds — lower case, upper
    case, digits — and meet the minimum length of the group of the account; a password the
    policy refuses is answered with the platform error that explains it.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        type_ (UsersPasswords):
        x_request_timeout (float | Unset):
        body (str | Unset):
        body (str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
type_=type_,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    type_: UsersPasswords,
    *,
    client: AuthenticatedClient | Client,
    body:    str  |     str  |     str  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultApiResponse | None:
    """ Change the password of the manager account used by the connection

     Replaces the stored password of the account the API uses to connect to the trade server. The
    change is made by the account itself and applies to the password type given in the route:
    `Main`, `Investor`, `API` or `Trader`. Any other value is refused.

    <br>
    The connection settings kept by this API are not updated by this call: the next connection
    attempt still presents the old password and the platform refuses it until the settings are
    brought in line. Change the password here only together with the stored settings.


    The new password must contain at least two of the three character kinds — lower case, upper
    case, digits — and meet the minimum length of the group of the account; a password the
    policy refuses is answered with the platform error that explains it.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        type_ (UsersPasswords):
        x_request_timeout (float | Unset):
        body (str | Unset):
        body (str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
type_=type_,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    type_: UsersPasswords,
    *,
    client: AuthenticatedClient | Client,
    body:    str  |     str  |     str  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5ResultApiResponse]:
    """ Change the password of the manager account used by the connection

     Replaces the stored password of the account the API uses to connect to the trade server. The
    change is made by the account itself and applies to the password type given in the route:
    `Main`, `Investor`, `API` or `Trader`. Any other value is refused.

    <br>
    The connection settings kept by this API are not updated by this call: the next connection
    attempt still presents the old password and the platform refuses it until the settings are
    brought in line. Change the password here only together with the stored settings.


    The new password must contain at least two of the three character kinds — lower case, upper
    case, digits — and meet the minimum length of the group of the account; a password the
    policy refuses is answered with the platform error that explains it.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        type_ (UsersPasswords):
        x_request_timeout (float | Unset):
        body (str | Unset):
        body (str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5ResultApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
type_=type_,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    type_: UsersPasswords,
    *,
    client: AuthenticatedClient | Client,
    body:    str  |     str  |     str  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5ResultApiResponse | None:
    """ Change the password of the manager account used by the connection

     Replaces the stored password of the account the API uses to connect to the trade server. The
    change is made by the account itself and applies to the password type given in the route:
    `Main`, `Investor`, `API` or `Trader`. Any other value is refused.

    <br>
    The connection settings kept by this API are not updated by this call: the next connection
    attempt still presents the old password and the platform refuses it until the settings are
    brought in line. Change the password here only together with the stored settings.


    The new password must contain at least two of the three character kinds — lower case, upper
    case, digits — and meet the minimum length of the group of the account; a password the
    policy refuses is answered with the platform error that explains it.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        type_ (UsersPasswords):
        x_request_timeout (float | Unset):
        body (str | Unset):
        body (str | Unset):
        body (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5ResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
type_=type_,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
