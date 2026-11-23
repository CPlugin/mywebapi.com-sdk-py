from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_user_api_response import MT5UserApiResponse
from ...models.mt5_user_update import MT5UserUpdate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5UserUpdate  |     MT5UserUpdate  |     MT5UserUpdate  | Unset = UNSET,
    login: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["login"] = login


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/UserUpdate".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }

    if isinstance(body, MT5UserUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5UserUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5UserUpdate):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5UserApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5UserApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5UserApiResponse]:
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
    body:    MT5UserUpdate  |     MT5UserUpdate  |     MT5UserUpdate  | Unset = UNSET,
    login: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserApiResponse]:
    r""" Update a user record

     <br>
                Changes the account named by the `login` query parameter. Only the fields present in
                the body are written: the record is read from the trade server, the body is applied over
                it, and the merged record is written back. A field left out keeps its server value; for
                the string fields, omitting the key keeps the value while sending `\"\"` clears it. A
                body without any field is rejected. The body must be the user update object — a full
    user
                record is not accepted.

    <br>
                The login identifies the record and is not part of the body; it is never changed by
                this call. An unknown login is answered with the trade server's error code. An unknown
                value of an enum field is answered as a validation error. The response is the updated
                record.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int | Unset):
        x_request_timeout (float | Unset):
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
login=login,
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
    body:    MT5UserUpdate  |     MT5UserUpdate  |     MT5UserUpdate  | Unset = UNSET,
    login: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserApiResponse | None:
    r""" Update a user record

     <br>
                Changes the account named by the `login` query parameter. Only the fields present in
                the body are written: the record is read from the trade server, the body is applied over
                it, and the merged record is written back. A field left out keeps its server value; for
                the string fields, omitting the key keeps the value while sending `\"\"` clears it. A
                body without any field is rejected. The body must be the user update object — a full
    user
                record is not accepted.

    <br>
                The login identifies the record and is not part of the body; it is never changed by
                this call. An unknown login is answered with the trade server's error code. An unknown
                value of an enum field is answered as a validation error. The response is the updated
                record.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int | Unset):
        x_request_timeout (float | Unset):
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
login=login,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT5UserUpdate  |     MT5UserUpdate  |     MT5UserUpdate  | Unset = UNSET,
    login: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserApiResponse]:
    r""" Update a user record

     <br>
                Changes the account named by the `login` query parameter. Only the fields present in
                the body are written: the record is read from the trade server, the body is applied over
                it, and the merged record is written back. A field left out keeps its server value; for
                the string fields, omitting the key keeps the value while sending `\"\"` clears it. A
                body without any field is rejected. The body must be the user update object — a full
    user
                record is not accepted.

    <br>
                The login identifies the record and is not part of the body; it is never changed by
                this call. An unknown login is answered with the trade server's error code. An unknown
                value of an enum field is answered as a validation error. The response is the updated
                record.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int | Unset):
        x_request_timeout (float | Unset):
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,
login=login,
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
    body:    MT5UserUpdate  |     MT5UserUpdate  |     MT5UserUpdate  | Unset = UNSET,
    login: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserApiResponse | None:
    r""" Update a user record

     <br>
                Changes the account named by the `login` query parameter. Only the fields present in
                the body are written: the record is read from the trade server, the body is applied over
                it, and the merged record is written back. A field left out keeps its server value; for
                the string fields, omitting the key keeps the value while sending `\"\"` clears it. A
                body without any field is rejected. The body must be the user update object — a full
    user
                record is not accepted.

    <br>
                The login identifies the record and is not part of the body; it is never changed by
                this call. An unknown login is answered with the trade server's error code. An unknown
                value of an enum field is answered as a validation error. The response is the updated
                record.


    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int | Unset):
        x_request_timeout (float | Unset):
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.
        body (MT5UserUpdate | Unset): MT5 user update DTO: the editable field set of an account,
            every field optional.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
login=login,
x_request_timeout=x_request_timeout,

    )).parsed
