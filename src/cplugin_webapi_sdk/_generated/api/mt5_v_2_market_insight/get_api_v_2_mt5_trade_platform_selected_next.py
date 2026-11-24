from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.mt5_selected_page_api_response import MT5SelectedPageApiResponse
from ...types import UNSET, Unset
from typing import cast
from uuid import UUID



def _get_kwargs(
    trade_platform: UUID,
    *,
    from_: int | Unset = UNSET,
    count: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_request_timeout, Unset):
        headers["X-Request-Timeout"] = str(x_request_timeout)




    

    params: dict[str, Any] = {}

    params["from"] = from_

    params["count"] = count


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/MT5/{trade_platform}/SelectedNext".format(trade_platform=quote(str(trade_platform), safe=""),),
        "params": params,
    }


    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> MT5SelectedPageApiResponse | None:
    if response.status_code == 200:
        response_200 = MT5SelectedPageApiResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[MT5SelectedPageApiResponse]:
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
    from_: int | Unset = UNSET,
    count: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SelectedPageApiResponse]:
    """ Read the selected-symbol list

     <br>
                Returns the names in the list in list order, together with the list length at the moment
                of the request. The window is positional: `from` is the position it starts at and
                `count` its size.

    <br>
                This is the list whose prices the manager application receives. When the application is
                connected with order or position updates, the symbols that have open orders or open
                positions are in the list automatically.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):
        count (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SelectedPageApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
count=count,
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
    from_: int | Unset = UNSET,
    count: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SelectedPageApiResponse | None:
    """ Read the selected-symbol list

     <br>
                Returns the names in the list in list order, together with the list length at the moment
                of the request. The window is positional: `from` is the position it starts at and
                `count` its size.

    <br>
                This is the list whose prices the manager application receives. When the application is
                connected with order or position updates, the symbols that have open orders or open
                positions are in the list automatically.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):
        count (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SelectedPageApiResponse
     """


    return sync_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
count=count,
x_request_timeout=x_request_timeout,

    ).parsed

async def asyncio_detailed(
    trade_platform: UUID,
    *,
    client: AuthenticatedClient | Client,
    from_: int | Unset = UNSET,
    count: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> Response[MT5SelectedPageApiResponse]:
    """ Read the selected-symbol list

     <br>
                Returns the names in the list in list order, together with the list length at the moment
                of the request. The window is positional: `from` is the position it starts at and
                `count` its size.

    <br>
                This is the list whose prices the manager application receives. When the application is
                connected with order or position updates, the symbols that have open orders or open
                positions are in the list automatically.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):
        count (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MT5SelectedPageApiResponse]
     """


    kwargs = _get_kwargs(
        trade_platform=trade_platform,
from_=from_,
count=count,
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
    from_: int | Unset = UNSET,
    count: int | Unset = UNSET,
    x_request_timeout: float | Unset = UNSET,

) -> MT5SelectedPageApiResponse | None:
    """ Read the selected-symbol list

     <br>
                Returns the names in the list in list order, together with the list length at the moment
                of the request. The window is positional: `from` is the position it starts at and
                `count` its size.

    <br>
                This is the list whose prices the manager application receives. When the application is
                connected with order or position updates, the symbols that have open orders or open
                positions are in the list automatically.


    **Timeout:** 10 s by default, adjustable per request with the `X-Request-Timeout` header. When the
    trade server does not answer in time: Nothing was changed; the request is safe to repeat.

    Args:
        trade_platform (UUID):
        from_ (int | Unset):
        count (int | Unset):
        x_request_timeout (float | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MT5SelectedPageApiResponse
     """


    return (await asyncio_detailed(
        trade_platform=trade_platform,
client=client,
from_=from_,
count=count,
x_request_timeout=x_request_timeout,

    )).parsed
