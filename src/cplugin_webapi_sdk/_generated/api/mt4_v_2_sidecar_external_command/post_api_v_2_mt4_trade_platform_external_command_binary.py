from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_external_command_binary_request import MT4ExternalCommandBinaryRequest
from ...models.mt4_external_command_binary_response_api_response import MT4ExternalCommandBinaryResponseApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/ExternalCommandBinary".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4ExternalCommandBinaryRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4ExternalCommandBinaryRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4ExternalCommandBinaryRequest):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4ExternalCommandBinaryResponseApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4ExternalCommandBinaryResponseApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4ExternalCommandBinaryResponseApiResponse]:
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
    body:    MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ExternalCommandBinaryResponseApiResponse]:
    """ Send plugin command (binary)

     Pass arbitrary binary payload to the MT4 server's plugin pipeline.

    <br>
    Manager (live) call via the platform's
    `ExternalCommandCustom<byte[], byte[]>` overload with a
    pass-through byte-array marshaller. The first installed plugin
    that returns `RET_OK` wins; its response bytes become the
    payload's `Data` field.
    <br>
    Wire format: `byte[]` serializes as base64 in JSON. Clients
    agree with the plugin author on the binary layout.
    <br><b>Why sidecar-only:</b> the platform's binary variants rely on
    `Marshal.SizeOf` + native `ExternalCommand` dispatch.
    On `mtmanapi64.dll` the signed/unsigned marshalling
    diverges from `mtmanapi.dll` — same payload byte-for-byte
    can decode differently on x64. The x86 sidecar process loads the
    32-bit DLL where the marshalling is the original one.
    <br>
    The platform's third `ExternalCommandCustom` overload that
    takes an `ICustomSerializer` interface is genuinely not
    REST-translatable — it requires the caller to provide C#
    serialization logic in-process. Not exposed.


    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ExternalCommandBinaryResponseApiResponse]
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
    body:    MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ExternalCommandBinaryResponseApiResponse | None:
    """ Send plugin command (binary)

     Pass arbitrary binary payload to the MT4 server's plugin pipeline.

    <br>
    Manager (live) call via the platform's
    `ExternalCommandCustom<byte[], byte[]>` overload with a
    pass-through byte-array marshaller. The first installed plugin
    that returns `RET_OK` wins; its response bytes become the
    payload's `Data` field.
    <br>
    Wire format: `byte[]` serializes as base64 in JSON. Clients
    agree with the plugin author on the binary layout.
    <br><b>Why sidecar-only:</b> the platform's binary variants rely on
    `Marshal.SizeOf` + native `ExternalCommand` dispatch.
    On `mtmanapi64.dll` the signed/unsigned marshalling
    diverges from `mtmanapi.dll` — same payload byte-for-byte
    can decode differently on x64. The x86 sidecar process loads the
    32-bit DLL where the marshalling is the original one.
    <br>
    The platform's third `ExternalCommandCustom` overload that
    takes an `ICustomSerializer` interface is genuinely not
    REST-translatable — it requires the caller to provide C#
    serialization logic in-process. Not exposed.


    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ExternalCommandBinaryResponseApiResponse
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
    body:    MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ExternalCommandBinaryResponseApiResponse]:
    """ Send plugin command (binary)

     Pass arbitrary binary payload to the MT4 server's plugin pipeline.

    <br>
    Manager (live) call via the platform's
    `ExternalCommandCustom<byte[], byte[]>` overload with a
    pass-through byte-array marshaller. The first installed plugin
    that returns `RET_OK` wins; its response bytes become the
    payload's `Data` field.
    <br>
    Wire format: `byte[]` serializes as base64 in JSON. Clients
    agree with the plugin author on the binary layout.
    <br><b>Why sidecar-only:</b> the platform's binary variants rely on
    `Marshal.SizeOf` + native `ExternalCommand` dispatch.
    On `mtmanapi64.dll` the signed/unsigned marshalling
    diverges from `mtmanapi.dll` — same payload byte-for-byte
    can decode differently on x64. The x86 sidecar process loads the
    32-bit DLL where the marshalling is the original one.
    <br>
    The platform's third `ExternalCommandCustom` overload that
    takes an `ICustomSerializer` interface is genuinely not
    REST-translatable — it requires the caller to provide C#
    serialization logic in-process. Not exposed.


    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ExternalCommandBinaryResponseApiResponse]
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
    body:    MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  |     MT4ExternalCommandBinaryRequest  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ExternalCommandBinaryResponseApiResponse | None:
    """ Send plugin command (binary)

     Pass arbitrary binary payload to the MT4 server's plugin pipeline.

    <br>
    Manager (live) call via the platform's
    `ExternalCommandCustom<byte[], byte[]>` overload with a
    pass-through byte-array marshaller. The first installed plugin
    that returns `RET_OK` wins; its response bytes become the
    payload's `Data` field.
    <br>
    Wire format: `byte[]` serializes as base64 in JSON. Clients
    agree with the plugin author on the binary layout.
    <br><b>Why sidecar-only:</b> the platform's binary variants rely on
    `Marshal.SizeOf` + native `ExternalCommand` dispatch.
    On `mtmanapi64.dll` the signed/unsigned marshalling
    diverges from `mtmanapi.dll` — same payload byte-for-byte
    can decode differently on x64. The x86 sidecar process loads the
    32-bit DLL where the marshalling is the original one.
    <br>
    The platform's third `ExternalCommandCustom` overload that
    takes an `ICustomSerializer` interface is genuinely not
    REST-translatable — it requires the caller to provide C#
    serialization logic in-process. Not exposed.


    **Timeout:** 60 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.
        body (MT4ExternalCommandBinaryRequest | Unset): v2 DTO for binary `ExternalCommand`
            roundtrips (sidecar-only).
            The MT4 server's plugin API has no enforced wire-format — clients
            agree with their plugin on the binary layout and pass arbitrary
            bytes through this endpoint.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ExternalCommandBinaryResponseApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
