from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_holiday import MT4Holiday
from ...models.mt4_holiday_api_response import MT4HolidayApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    pos: int,
    *,
    body:    MT4Holiday  |     MT4Holiday  |     MT4Holiday  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateHoliday/{pos}".format(trade_platform=quote(str(trade_platform), safe=""),pos=quote(str(pos), safe=""),),
    }

    if isinstance(body, MT4Holiday):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4Holiday):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4Holiday):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4HolidayApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4HolidayApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4HolidayApiResponse]:
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
    body:    MT4Holiday  |     MT4Holiday  |     MT4Holiday  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4HolidayApiResponse]:
    """ Update holiday entry

     Update a holiday-calendar entry at a given list position — Type 1 mutator.

    Position-based read-modify-write. The wrapper stores `Enable`
    as `int` (0/1) — the DTO surfaces it as `bool`; the
    mapper bridges with a `BoolToInt` helper. The 13-int
    `Reserved` padding and `Next` pointer are preserved.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4HolidayApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
body=body,
x_request_timeout=x_request_timeout,

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
    body:    MT4Holiday  |     MT4Holiday  |     MT4Holiday  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4HolidayApiResponse | None:
    """ Update holiday entry

     Update a holiday-calendar entry at a given list position — Type 1 mutator.

    Position-based read-modify-write. The wrapper stores `Enable`
    as `int` (0/1) — the DTO surfaces it as `bool`; the
    mapper bridges with a `BoolToInt` helper. The 13-int
    `Reserved` padding and `Next` pointer are preserved.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4HolidayApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    pos: int,
    *,
    client: AuthenticatedClient | Client,
    body:    MT4Holiday  |     MT4Holiday  |     MT4Holiday  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4HolidayApiResponse]:
    """ Update holiday entry

     Update a holiday-calendar entry at a given list position — Type 1 mutator.

    Position-based read-modify-write. The wrapper stores `Enable`
    as `int` (0/1) — the DTO surfaces it as `bool`; the
    mapper bridges with a `BoolToInt` helper. The 13-int
    `Reserved` padding and `Next` pointer are preserved.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4HolidayApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
pos=pos,
body=body,
x_request_timeout=x_request_timeout,

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
    body:    MT4Holiday  |     MT4Holiday  |     MT4Holiday  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4HolidayApiResponse | None:
    """ Update holiday entry

     Update a holiday-calendar entry at a given list position — Type 1 mutator.

    Position-based read-modify-write. The wrapper stores `Enable`
    as `int` (0/1) — the DTO surfaces it as `bool`; the
    mapper bridges with a `BoolToInt` helper. The 13-int
    `Reserved` padding and `Next` pointer are preserved.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        pos (int):
        x_request_timeout (float | Unset):
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).
        body (MT4Holiday | Unset): v2 DTO for a single MT4 holiday-calendar entry. Curated subset
            of the
            wrapper's ConHoliday struct — exposes the broker-facing fields and
            drops the internal Reserved/Next pointer block. Date is split into
            Year/Month/Day ints (wire-compatible with the wrapper, no DateTime
            conversion to avoid timezone ambiguity for date-only entries).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4HolidayApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
pos=pos,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
