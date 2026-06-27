from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_data_server import MT4DataServer
from ...models.mt4_data_server_api_response import MT4DataServerApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    pos: int,
    *,
    body:    MT4DataServer  |     MT4DataServer  |     MT4DataServer  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateDataServer/{pos}".format(trade_platform=quote(str(trade_platform), safe=""),pos=quote(str(pos), safe=""),),
    }

    if isinstance(body, MT4DataServer):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4DataServer):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4DataServer):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4DataServerApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4DataServerApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4DataServerApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4DataServer  |     MT4DataServer  |     MT4DataServer  | Unset = UNSET,

) -> Response[MT4DataServerApiResponse]:
    """ Update data-server entry

     Update a DataServer (access-server) entry at a given list position — Type 1 mutator.

    Same position-based read-modify-write pattern as
    `CfgUpdateAccess`. Preserves internal padding
    (`Reserved1`, `Reserved2`) and the `Next` pointer.
    `Loading`/`IpInternal` in the body must fit in
    `[0, uint.MaxValue]`.

    Args:
        trade_platform (UUID):
        pos (int):
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4DataServerApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4DataServer  |     MT4DataServer  |     MT4DataServer  | Unset = UNSET,

) -> MT4DataServerApiResponse | None:
    """ Update data-server entry

     Update a DataServer (access-server) entry at a given list position — Type 1 mutator.

    Same position-based read-modify-write pattern as
    `CfgUpdateAccess`. Preserves internal padding
    (`Reserved1`, `Reserved2`) and the `Next` pointer.
    `Loading`/`IpInternal` in the body must fit in
    `[0, uint.MaxValue]`.

    Args:
        trade_platform (UUID):
        pos (int):
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4DataServerApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4DataServer  |     MT4DataServer  |     MT4DataServer  | Unset = UNSET,

) -> Response[MT4DataServerApiResponse]:
    """ Update data-server entry

     Update a DataServer (access-server) entry at a given list position — Type 1 mutator.

    Same position-based read-modify-write pattern as
    `CfgUpdateAccess`. Preserves internal padding
    (`Reserved1`, `Reserved2`) and the `Next` pointer.
    `Loading`/`IpInternal` in the body must fit in
    `[0, uint.MaxValue]`.

    Args:
        trade_platform (UUID):
        pos (int):
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4DataServerApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4DataServer  |     MT4DataServer  |     MT4DataServer  | Unset = UNSET,

) -> MT4DataServerApiResponse | None:
    """ Update data-server entry

     Update a DataServer (access-server) entry at a given list position — Type 1 mutator.

    Same position-based read-modify-write pattern as
    `CfgUpdateAccess`. Preserves internal padding
    (`Reserved1`, `Reserved2`) and the `Next` pointer.
    `Loading`/`IpInternal` in the body must fit in
    `[0, uint.MaxValue]`.

    Args:
        trade_platform (UUID):
        pos (int):
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.
        body (MT4DataServer | Unset): v2 DTO for a single MT4 access-server (DataServer)
            configuration entry.
            Curated subset of the wrapper's ConDataServer — drops the internal
            Reserved1/Reserved2 padding and the Next pointer chain. Loading and
            IpInternal are widened from uint to long for JSON-safe numeric
            serialization.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4DataServerApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
body=body,

    )).parsed
