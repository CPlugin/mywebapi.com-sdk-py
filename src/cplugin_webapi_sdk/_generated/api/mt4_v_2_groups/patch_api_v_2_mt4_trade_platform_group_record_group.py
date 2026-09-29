from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_group_api_response import MT4GroupApiResponse
from ...models.patch_api_v2mt4_trade_platform_group_record_group_json_body import PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    group: str,
    *,
    body: PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v2/MT4/{trade_platform}/GroupRecord/{group}".format(trade_platform=quote(str(trade_platform), safe=""),group=quote(str(group), safe=""),),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4GroupApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4GroupApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4GroupApiResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4GroupApiResponse]:
    """ Patch trading group

     Type 2 mutator — partial update of a trading group. Same semantics as `UserRecordPatch`; see that
    endpoint for the read-merge- write flow and forwards-compat behavior.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody): Only the fields to change; the
            rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GroupApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> MT4GroupApiResponse | None:
    """ Patch trading group

     Type 2 mutator — partial update of a trading group. Same semantics as `UserRecordPatch`; see that
    endpoint for the read-merge- write flow and forwards-compat behavior.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody): Only the fields to change; the
            rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GroupApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4GroupApiResponse]:
    """ Patch trading group

     Type 2 mutator — partial update of a trading group. Same semantics as `UserRecordPatch`; see that
    endpoint for the read-merge- write flow and forwards-compat behavior.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody): Only the fields to change; the
            rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GroupApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
group=group,
body=body,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    group: str,
    *,
    client: AuthenticatedClient | Client,
    body: PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody,
    x_request_timeout: float | Unset = UNSET,

) -> MT4GroupApiResponse | None:
    """ Patch trading group

     Type 2 mutator — partial update of a trading group. Same semantics as `UserRecordPatch`; see that
    endpoint for the read-merge- write flow and forwards-compat behavior.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        group (str):
        x_request_timeout (float | Unset):
        body (PatchApiV2MT4TradePlatformGroupRecordGroupJsonBody): Only the fields to change; the
            rest of the record stays as it is.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GroupApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
group=group,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
