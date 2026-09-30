from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_gateway_rule import MT4GatewayRule
from ...models.mt4_gateway_rule_api_response import MT4GatewayRuleApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4GatewayRule  |     MT4GatewayRule  |     MT4GatewayRule  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateGatewayRule".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4GatewayRule):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4GatewayRule):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4GatewayRule):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4GatewayRuleApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4GatewayRuleApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4GatewayRuleApiResponse]:
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
    body:    MT4GatewayRule  |     MT4GatewayRule  |     MT4GatewayRule  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4GatewayRuleApiResponse]:
    """ Update gateway rule

     Update an STP gateway-rule entry — Type 1 mutator.

    Manager (live) call. Gateway rules are paged on the read side (see
    `CfgRequestGatewayRule`); the v2 contract identifies a rule
    by its public `Name`. Same read-modify-write flow; the two
    wrapper reserved padding blocks (`RequestRreserved` 32-int,
    `ExeReserved` 25-int) are preserved server-side.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GatewayRuleApiResponse]
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
    body:    MT4GatewayRule  |     MT4GatewayRule  |     MT4GatewayRule  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4GatewayRuleApiResponse | None:
    """ Update gateway rule

     Update an STP gateway-rule entry — Type 1 mutator.

    Manager (live) call. Gateway rules are paged on the read side (see
    `CfgRequestGatewayRule`); the v2 contract identifies a rule
    by its public `Name`. Same read-modify-write flow; the two
    wrapper reserved padding blocks (`RequestRreserved` 32-int,
    `ExeReserved` 25-int) are preserved server-side.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GatewayRuleApiResponse
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
    body:    MT4GatewayRule  |     MT4GatewayRule  |     MT4GatewayRule  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4GatewayRuleApiResponse]:
    """ Update gateway rule

     Update an STP gateway-rule entry — Type 1 mutator.

    Manager (live) call. Gateway rules are paged on the read side (see
    `CfgRequestGatewayRule`); the v2 contract identifies a rule
    by its public `Name`. Same read-modify-write flow; the two
    wrapper reserved padding blocks (`RequestRreserved` 32-int,
    `ExeReserved` 25-int) are preserved server-side.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4GatewayRuleApiResponse]
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
    body:    MT4GatewayRule  |     MT4GatewayRule  |     MT4GatewayRule  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4GatewayRuleApiResponse | None:
    """ Update gateway rule

     Update an STP gateway-rule entry — Type 1 mutator.

    Manager (live) call. Gateway rules are paged on the read side (see
    `CfgRequestGatewayRule`); the v2 contract identifies a rule
    by its public `Name`. Same read-modify-write flow; the two
    wrapper reserved padding blocks (`RequestRreserved` 32-int,
    `ExeReserved` 25-int) are preserved server-side.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.
        body (MT4GatewayRule | Unset): v2 DTO for a single MT4 gateway-rule entry (STP execution
            routing
            policy). Curated subset of the wrapper's ConGatewayRule — drops the
            internal RequestRreserved/ExeReserved padding blocks.
            <br>
            Each rule selects orders by RequestSymbol and RequestGroup (each can
            be an exact name, a wildcard mask, or a group identifier), then
            routes them to ExeAccount (named externally), with execution limits
            expressed in pips and lots.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4GatewayRuleApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
