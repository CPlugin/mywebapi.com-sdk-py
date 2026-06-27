from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.boolean_api_response import BooleanApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    logins: list[int] | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_logins: list[int] | Unset = UNSET
    if not isinstance(logins, Unset):
        json_logins = logins


    params["logins"] = json_logins


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/AdmBalanceFix".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


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
    logins: list[int] | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Fix account balances

     Admin balance fix — recompute balances for the given logins.

    POST mutator. Asks MT4 server to take the diffs reported by
    `AdmBalanceCheck` and write them onto the accounts. Empty body —
    the logins are submitted as repeated query parameters
    (`?logins=1001&logins=1002`) to keep the URL shape parallel
    with the read variant and avoid the awkward \"POST with int[] body\"
    pattern.

    This DOES modify account balances. Pair every retry with an
    `Idempotency-Key` header; otherwise a retried fix can double-
    apply on an account whose original fix happened to land but whose
    response was lost on the wire.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
logins=logins,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    logins: list[int] | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Fix account balances

     Admin balance fix — recompute balances for the given logins.

    POST mutator. Asks MT4 server to take the diffs reported by
    `AdmBalanceCheck` and write them onto the accounts. Empty body —
    the logins are submitted as repeated query parameters
    (`?logins=1001&logins=1002`) to keep the URL shape parallel
    with the read variant and avoid the awkward \"POST with int[] body\"
    pattern.

    This DOES modify account balances. Pair every retry with an
    `Idempotency-Key` header; otherwise a retried fix can double-
    apply on an account whose original fix happened to land but whose
    response was lost on the wire.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
logins=logins,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    logins: list[int] | Unset = UNSET,

) -> Response[BooleanApiResponse]:
    r""" Fix account balances

     Admin balance fix — recompute balances for the given logins.

    POST mutator. Asks MT4 server to take the diffs reported by
    `AdmBalanceCheck` and write them onto the accounts. Empty body —
    the logins are submitted as repeated query parameters
    (`?logins=1001&logins=1002`) to keep the URL shape parallel
    with the read variant and avoid the awkward \"POST with int[] body\"
    pattern.

    This DOES modify account balances. Pair every retry with an
    `Idempotency-Key` header; otherwise a retried fix can double-
    apply on an account whose original fix happened to land but whose
    response was lost on the wire.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BooleanApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
logins=logins,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    logins: list[int] | Unset = UNSET,

) -> BooleanApiResponse | None:
    r""" Fix account balances

     Admin balance fix — recompute balances for the given logins.

    POST mutator. Asks MT4 server to take the diffs reported by
    `AdmBalanceCheck` and write them onto the accounts. Empty body —
    the logins are submitted as repeated query parameters
    (`?logins=1001&logins=1002`) to keep the URL shape parallel
    with the read variant and avoid the awkward \"POST with int[] body\"
    pattern.

    This DOES modify account balances. Pair every retry with an
    `Idempotency-Key` header; otherwise a retried fix can double-
    apply on an account whose original fix happened to land but whose
    response was lost on the wire.

    Args:
        trade_platform (UUID):
        logins (list[int] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BooleanApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
logins=logins,

    )).parsed
