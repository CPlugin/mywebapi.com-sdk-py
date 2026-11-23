from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...models.mt5_chart_rounding_rule import MT5ChartRoundingRule
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID
import datetime



def _get_kwargs(
    trade_platform: UUID,
    symbol: str,
    *,
    new_shares: int | Unset = UNSET,
    old_shares: int | Unset = UNSET,
    rounding_rule: MT5ChartRoundingRule | Unset = MT5ChartRoundingRule.STANDARD,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["newShares"] = new_shares

    params["oldShares"] = old_shares

    json_rounding_rule: str | Unset = UNSET
    if not isinstance(rounding_rule, Unset):
        json_rounding_rule = rounding_rule.value

    params["roundingRule"] = json_rounding_rule

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT5/{trade_platform}/ChartSplit/{symbol}".format(trade_platform=quote(str(trade_platform), safe=""),symbol=quote(str(symbol), safe=""),),
        "params": params,
    }


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
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    new_shares: int | Unset = UNSET,
    old_shares: int | Unset = UNSET,
    rounding_rule: MT5ChartRoundingRule | Unset = MT5ChartRoundingRule.STANDARD,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Split the price history of a symbol

     <br>
                Converts the stored bars and ticks of the symbol by the ratio of the new shares to the
    old
                ones — a split when there are more new shares, a consolidation when there are fewer —
    and
                rounds the converted prices by the chosen rule to the number of digits the symbol
    allows.
                The optional window limits the conversion to a period; without it the whole stored
    history
                of the symbol is converted.

    <br>
                The call changes both the bar history and the tick history of the trade server and is
    not
                reversible: the original prices are not kept anywhere, so keep a backup of the trade
    server
                before writing. The operation runs on the server in the background: the response
    confirms
                the command was accepted, not that the split has finished, and a split already running
    for
                the symbol is neither interrupted nor started again.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        new_shares (int | Unset):
        old_shares (int | Unset):
        rounding_rule (MT5ChartRoundingRule | Unset): Rounding rule applied to prices converted by
            a split. Default: MT5ChartRoundingRule.STANDARD.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
new_shares=new_shares,
old_shares=old_shares,
rounding_rule=rounding_rule,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    new_shares: int | Unset = UNSET,
    old_shares: int | Unset = UNSET,
    rounding_rule: MT5ChartRoundingRule | Unset = MT5ChartRoundingRule.STANDARD,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Split the price history of a symbol

     <br>
                Converts the stored bars and ticks of the symbol by the ratio of the new shares to the
    old
                ones — a split when there are more new shares, a consolidation when there are fewer —
    and
                rounds the converted prices by the chosen rule to the number of digits the symbol
    allows.
                The optional window limits the conversion to a period; without it the whole stored
    history
                of the symbol is converted.

    <br>
                The call changes both the bar history and the tick history of the trade server and is
    not
                reversible: the original prices are not kept anywhere, so keep a backup of the trade
    server
                before writing. The operation runs on the server in the background: the response
    confirms
                the command was accepted, not that the split has finished, and a split already running
    for
                the symbol is neither interrupted nor started again.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        new_shares (int | Unset):
        old_shares (int | Unset):
        rounding_rule (MT5ChartRoundingRule | Unset): Rounding rule applied to prices converted by
            a split. Default: MT5ChartRoundingRule.STANDARD.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
new_shares=new_shares,
old_shares=old_shares,
rounding_rule=rounding_rule,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    new_shares: int | Unset = UNSET,
    old_shares: int | Unset = UNSET,
    rounding_rule: MT5ChartRoundingRule | Unset = MT5ChartRoundingRule.STANDARD,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    """ Split the price history of a symbol

     <br>
                Converts the stored bars and ticks of the symbol by the ratio of the new shares to the
    old
                ones — a split when there are more new shares, a consolidation when there are fewer —
    and
                rounds the converted prices by the chosen rule to the number of digits the symbol
    allows.
                The optional window limits the conversion to a period; without it the whole stored
    history
                of the symbol is converted.

    <br>
                The call changes both the bar history and the tick history of the trade server and is
    not
                reversible: the original prices are not kept anywhere, so keep a backup of the trade
    server
                before writing. The operation runs on the server in the background: the response
    confirms
                the command was accepted, not that the split has finished, and a split already running
    for
                the symbol is neither interrupted nor started again.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        new_shares (int | Unset):
        old_shares (int | Unset):
        rounding_rule (MT5ChartRoundingRule | Unset): Rounding rule applied to prices converted by
            a split. Default: MT5ChartRoundingRule.STANDARD.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
symbol=symbol,
new_shares=new_shares,
old_shares=old_shares,
rounding_rule=rounding_rule,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    symbol: str,
    *,
    client: AuthenticatedClient | Client,
    new_shares: int | Unset = UNSET,
    old_shares: int | Unset = UNSET,
    rounding_rule: MT5ChartRoundingRule | Unset = MT5ChartRoundingRule.STANDARD,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> BooleanApiResponse | None:
    """ Split the price history of a symbol

     <br>
                Converts the stored bars and ticks of the symbol by the ratio of the new shares to the
    old
                ones — a split when there are more new shares, a consolidation when there are fewer —
    and
                rounds the converted prices by the chosen rule to the number of digits the symbol
    allows.
                The optional window limits the conversion to a period; without it the whole stored
    history
                of the symbol is converted.

    <br>
                The call changes both the bar history and the tick history of the trade server and is
    not
                reversible: the original prices are not kept anywhere, so keep a backup of the trade
    server
                before writing. The operation runs on the server in the background: the response
    confirms
                the command was accepted, not that the split has finished, and a split already running
    for
                the symbol is neither interrupted nor started again.


    **Timeout:** 5 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        symbol (str):
        new_shares (int | Unset):
        old_shares (int | Unset):
        rounding_rule (MT5ChartRoundingRule | Unset): Rounding rule applied to prices converted by
            a split. Default: MT5ChartRoundingRule.STANDARD.
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
symbol=symbol,
client=client,
new_shares=new_shares,
old_shares=old_shares,
rounding_rule=rounding_rule,
from_=from_,
to=to,
x_request_timeout=x_request_timeout,

    )).parsed
