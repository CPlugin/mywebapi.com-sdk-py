from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_license_check_request import MT5LicenseCheckRequest
from ...models.mt5_license_check_result_api_response import MT5LicenseCheckResultApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/LicenseCheck".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT5LicenseCheckRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT5LicenseCheckRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT5LicenseCheckRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5LicenseCheckResultApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5LicenseCheckResultApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5LicenseCheckResultApiResponse]:
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
    body:    MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5LicenseCheckResultApiResponse]:
    """ Check the application license on the trade server

     Asks the trade server whether the use of the named application is authorized in its platform
    license and receives the signed answer. The signature covers the result code, the application
    name and the random sequence, so the caller verifies the authenticity of the answer with the
    public key of the platform.

    The name is limited to 128 characters and the random sequence to 256 bytes; a longer value
    is refused as invalid. This check answers the licensing question alone — it changes nothing
    on the server.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5LicenseCheckResultApiResponse]
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
    body:    MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5LicenseCheckResultApiResponse | None:
    """ Check the application license on the trade server

     Asks the trade server whether the use of the named application is authorized in its platform
    license and receives the signed answer. The signature covers the result code, the application
    name and the random sequence, so the caller verifies the authenticity of the answer with the
    public key of the platform.

    The name is limited to 128 characters and the random sequence to 256 bytes; a longer value
    is refused as invalid. This check answers the licensing question alone — it changes nothing
    on the server.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5LicenseCheckResultApiResponse
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
    body:    MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5LicenseCheckResultApiResponse]:
    """ Check the application license on the trade server

     Asks the trade server whether the use of the named application is authorized in its platform
    license and receives the signed answer. The signature covers the result code, the application
    name and the random sequence, so the caller verifies the authenticity of the answer with the
    public key of the platform.

    The name is limited to 128 characters and the random sequence to 256 bytes; a longer value
    is refused as invalid. This check answers the licensing question alone — it changes nothing
    on the server.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5LicenseCheckResultApiResponse]
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
    body:    MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  |     MT5LicenseCheckRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5LicenseCheckResultApiResponse | None:
    """ Check the application license on the trade server

     Asks the trade server whether the use of the named application is authorized in its platform
    license and receives the signed answer. The signature covers the result code, the application
    name and the random sequence, so the caller verifies the authenticity of the answer with the
    public key of the platform.

    The name is limited to 128 characters and the random sequence to 256 bytes; a longer value
    is refused as invalid. This check answers the licensing question alone — it changes nothing
    on the server.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.
        body (MT5LicenseCheckRequest | Unset): Application license to verify against the license
            of the trade server.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5LicenseCheckResultApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
