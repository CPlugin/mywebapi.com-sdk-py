from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt4_user_update import MT4UserUpdate
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/UserRecordUpdate".format(trade_platform=quote(str(trade_platform), safe=""),),
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
    *,
    client: AuthenticatedClient | Client,
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Update account

     Change an account. The `login` field of the body identifies the account and is never
    changed; the response is a boolean.

    Only the fields present in the body are written: the record is read live from the trade
    server, the body is applied over it, and the merged record is written back. A field that
    is left out keeps its server value; for the string fields, omitting the key keeps the
    value while sending `\"\"` clears it. Server-assigned and secret values (passwords, OTP
    secret, registration date, last login, previous-period balances) always keep their server
    values. A body with the login but no field to change is rejected.

    Idempotency-Key strongly recommended: a change to the account affects
    trading immediately, and a blind retry can overwrite concurrent edits.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Update account

     Change an account. The `login` field of the body identifies the account and is never
    changed; the response is a boolean.

    Only the fields present in the body are written: the record is read live from the trade
    server, the body is applied over it, and the merged record is written back. A field that
    is left out keeps its server value; for the string fields, omitting the key keeps the
    value while sending `\"\"` clears it. Server-assigned and secret values (passwords, OTP
    secret, registration date, last login, previous-period balances) always keep their server
    values. A body with the login but no field to change is rejected.

    Idempotency-Key strongly recommended: a change to the account affects
    trading immediately, and a blind retry can overwrite concurrent edits.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
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
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Update account

     Change an account. The `login` field of the body identifies the account and is never
    changed; the response is a boolean.

    Only the fields present in the body are written: the record is read live from the trade
    server, the body is applied over it, and the merged record is written back. A field that
    is left out keeps its server value; for the string fields, omitting the key keeps the
    value while sending `\"\"` clears it. Server-assigned and secret values (passwords, OTP
    secret, registration date, last login, previous-period balances) always keep their server
    values. A body with the login but no field to change is rejected.

    Idempotency-Key strongly recommended: a change to the account affects
    trading immediately, and a blind retry can overwrite concurrent edits.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
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
    body:    MT4UserUpdate  |     MT4UserUpdate  |     MT4UserUpdate  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Update account

     Change an account. The `login` field of the body identifies the account and is never
    changed; the response is a boolean.

    Only the fields present in the body are written: the record is read live from the trade
    server, the body is applied over it, and the merged record is written back. A field that
    is left out keeps its server value; for the string fields, omitting the key keeps the
    value while sending `\"\"` clears it. Server-assigned and secret values (passwords, OTP
    secret, registration date, last login, previous-period balances) always keep their server
    values. A body with the login but no field to change is rejected.

    Idempotency-Key strongly recommended: a change to the account affects
    trading immediately, and a blind retry can overwrite concurrent edits.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.
        body (MT4UserUpdate | Unset): Input shape for `UserRecordUpdate`: the editable part of an
            MT4 account record.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
