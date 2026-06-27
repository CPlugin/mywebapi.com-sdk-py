from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_feeder import MT4Feeder
from ...models.mt4_feeder_api_response import MT4FeederApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4Feeder  |     MT4Feeder  |     MT4Feeder  | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateFeeder".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4Feeder):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4Feeder):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4Feeder):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4FeederApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4FeederApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4FeederApiResponse]:
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
    body:    MT4Feeder  |     MT4Feeder  |     MT4Feeder  | Unset = UNSET,

) -> Response[MT4FeederApiResponse]:
    """ Update feeder config

     Update a quote/news feeder configuration — Type 1 mutator.

    Manager (live) call. Feeder configurations are paged on the read
    side (see `CfgRequestFeeder`); the v2 contract identifies a
    feeder by its `Name`. Same read-modify-write flow as
    `CfgUpdateSync`; the datafeed credential (`Password`)
    is preserved server-side.

    Args:
        trade_platform (UUID):
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4FeederApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4Feeder  |     MT4Feeder  |     MT4Feeder  | Unset = UNSET,

) -> MT4FeederApiResponse | None:
    """ Update feeder config

     Update a quote/news feeder configuration — Type 1 mutator.

    Manager (live) call. Feeder configurations are paged on the read
    side (see `CfgRequestFeeder`); the v2 contract identifies a
    feeder by its `Name`. Same read-modify-write flow as
    `CfgUpdateSync`; the datafeed credential (`Password`)
    is preserved server-side.

    Args:
        trade_platform (UUID):
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4FeederApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4Feeder  |     MT4Feeder  |     MT4Feeder  | Unset = UNSET,

) -> Response[MT4FeederApiResponse]:
    """ Update feeder config

     Update a quote/news feeder configuration — Type 1 mutator.

    Manager (live) call. Feeder configurations are paged on the read
    side (see `CfgRequestFeeder`); the v2 contract identifies a
    feeder by its `Name`. Same read-modify-write flow as
    `CfgUpdateSync`; the datafeed credential (`Password`)
    is preserved server-side.

    Args:
        trade_platform (UUID):
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4FeederApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4Feeder  |     MT4Feeder  |     MT4Feeder  | Unset = UNSET,

) -> MT4FeederApiResponse | None:
    """ Update feeder config

     Update a quote/news feeder configuration — Type 1 mutator.

    Manager (live) call. Feeder configurations are paged on the read
    side (see `CfgRequestFeeder`); the v2 contract identifies a
    feeder by its `Name`. Same read-modify-write flow as
    `CfgUpdateSync`; the datafeed credential (`Password`)
    is preserved server-side.

    Args:
        trade_platform (UUID):
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).
        body (MT4Feeder | Unset): v2 DTO for a single MT4 quote/news feeder configuration. Curated
            subset of the wrapper's ConFeeder — drops the wrapper's Unused
            reserved blob AND the `Password` field (datafeed credentials).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4FeederApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,

    )).parsed
