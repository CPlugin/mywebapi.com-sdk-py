from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_user_api_response import MT5UserApiResponse
from ...models.patch_api_v2mt5_trade_platform_user_record_login_json_body import PatchApiV2MT5TradePlatformUserRecordLoginJsonBody
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    login: int,
    *,
    body: PatchApiV2MT5TradePlatformUserRecordLoginJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/MT5/{trade_platform}/UserRecord/{login}".format(trade_platform=quote(str(trade_platform), safe=""),login=quote(str(login), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

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
    login: int,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiV2MT5TradePlatformUserRecordLoginJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserApiResponse]:
    """ Partially update a user

     Send only the fields you want to change (JSON Merge Patch, RFC 7386);
    omitted fields keep their current values. Returns the updated record.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT5TradePlatformUserRecordLoginJsonBody): Only the fields to change; the
            rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserApiResponse]
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
    body: PatchApiV2MT5TradePlatformUserRecordLoginJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserApiResponse | None:
    """ Partially update a user

     Send only the fields you want to change (JSON Merge Patch, RFC 7386);
    omitted fields keep their current values. Returns the updated record.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT5TradePlatformUserRecordLoginJsonBody): Only the fields to change; the
            rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserApiResponse
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
    body: PatchApiV2MT5TradePlatformUserRecordLoginJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5UserApiResponse]:
    """ Partially update a user

     Send only the fields you want to change (JSON Merge Patch, RFC 7386);
    omitted fields keep their current values. Returns the updated record.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT5TradePlatformUserRecordLoginJsonBody): Only the fields to change; the
            rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5UserApiResponse]
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
    body: PatchApiV2MT5TradePlatformUserRecordLoginJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> MT5UserApiResponse | None:
    """ Partially update a user

     Send only the fields you want to change (JSON Merge Patch, RFC 7386);
    omitted fields keep their current values. Returns the updated record.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        login (int):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT5TradePlatformUserRecordLoginJsonBody): Only the fields to change; the
            rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5UserApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
login=login,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
