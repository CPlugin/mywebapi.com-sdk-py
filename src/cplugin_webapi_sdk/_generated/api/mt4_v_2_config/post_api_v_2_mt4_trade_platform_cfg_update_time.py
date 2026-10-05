from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt4_server_time import MT4ServerTime
from ...models.mt4_server_time_api_response import MT4ServerTimeApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    body:    MT4ServerTime  |     MT4ServerTime  |     MT4ServerTime  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/MT4/{trade_platform}/CfgUpdateTime".format(trade_platform=quote(str(trade_platform), safe=""),),
    }

    if isinstance(body, MT4ServerTime):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json-patch+json"
    if isinstance(body, MT4ServerTime):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, MT4ServerTime):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT4ServerTimeApiResponse | None:
    if response.status_code == 200:
        response_200 = MT4ServerTimeApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT4ServerTimeApiResponse]:
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
    body:    MT4ServerTime  |     MT4ServerTime  |     MT4ServerTime  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ServerTimeApiResponse]:
    """ Update access-hour matrix

     Update the 7×24 access-hour matrix — Type 1 mutator.

    Manager (live) call. Reads the current `ConTime`, replaces the
    168-hour access matrix with the supplied `AccessHours`, and
    writes back. The platform's internal `DaysControl` (server
    housekeeping) and `Reserved` (forward-compat padding) fields
    are preserved across the round-trip.

    `AccessHours` must be exactly 168 entries long; index =
    `day * 24 + hour` with day 0 = Sunday. Each value is
    `0` (denied) or `1` (allowed) — any other value is
    passed through verbatim (the platform does not validate, and
    MT4 may treat anything non-zero as allowed depending on build).

    Echoes the merged `MT4ServerTime` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ServerTimeApiResponse]
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
    body:    MT4ServerTime  |     MT4ServerTime  |     MT4ServerTime  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ServerTimeApiResponse | None:
    """ Update access-hour matrix

     Update the 7×24 access-hour matrix — Type 1 mutator.

    Manager (live) call. Reads the current `ConTime`, replaces the
    168-hour access matrix with the supplied `AccessHours`, and
    writes back. The platform's internal `DaysControl` (server
    housekeeping) and `Reserved` (forward-compat padding) fields
    are preserved across the round-trip.

    `AccessHours` must be exactly 168 entries long; index =
    `day * 24 + hour` with day 0 = Sunday. Each value is
    `0` (denied) or `1` (allowed) — any other value is
    passed through verbatim (the platform does not validate, and
    MT4 may treat anything non-zero as allowed depending on build).

    Echoes the merged `MT4ServerTime` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ServerTimeApiResponse
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
    body:    MT4ServerTime  |     MT4ServerTime  |     MT4ServerTime  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT4ServerTimeApiResponse]:
    """ Update access-hour matrix

     Update the 7×24 access-hour matrix — Type 1 mutator.

    Manager (live) call. Reads the current `ConTime`, replaces the
    168-hour access matrix with the supplied `AccessHours`, and
    writes back. The platform's internal `DaysControl` (server
    housekeeping) and `Reserved` (forward-compat padding) fields
    are preserved across the round-trip.

    `AccessHours` must be exactly 168 entries long; index =
    `day * 24 + hour` with day 0 = Sunday. Each value is
    `0` (denied) or `1` (allowed) — any other value is
    passed through verbatim (the platform does not validate, and
    MT4 may treat anything non-zero as allowed depending on build).

    Echoes the merged `MT4ServerTime` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT4ServerTimeApiResponse]
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
    body:    MT4ServerTime  |     MT4ServerTime  |     MT4ServerTime  | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT4ServerTimeApiResponse | None:
    """ Update access-hour matrix

     Update the 7×24 access-hour matrix — Type 1 mutator.

    Manager (live) call. Reads the current `ConTime`, replaces the
    168-hour access matrix with the supplied `AccessHours`, and
    writes back. The platform's internal `DaysControl` (server
    housekeeping) and `Reserved` (forward-compat padding) fields
    are preserved across the round-trip.

    `AccessHours` must be exactly 168 entries long; index =
    `day * 24 + hour` with day 0 = Sunday. Each value is
    `0` (denied) or `1` (allowed) — any other value is
    passed through verbatim (the platform does not validate, and
    MT4 may treat anything non-zero as allowed depending on build).

    Echoes the merged `MT4ServerTime` in the response.

    **Timeout:** 15 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: The operation may still be completed by the server
    (`X-Request-Outcome: unknown`): check its result before repeating it.

    Args:
        trade_platform (UUID):
        x_request_timeout (float | Unset):
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.
        body (MT4ServerTime | Unset): v2 DTO for the MT4 server's per-hour access matrix (the
            platform's
            `ConTime.Days` field). 168-element flat array; each element
            is `0` (denied) or `1` (allowed) for one hour of the
            week. Layout: `index = day * 24 + hour`, day-of-week 0..6
            matches MT4's native convention where day 0 = Sunday.
            <br>
            Example: `AccessHours[24..47]` covers Monday's 24 hours.
            Internal `DaysControl` and `Reserved` platform fields
            are not part of the v2 contract.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT4ServerTimeApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
body=body,
x_request_timeout=x_request_timeout,

    )).parsed
