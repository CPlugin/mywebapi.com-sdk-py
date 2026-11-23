from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_order import MT5Order
  from ..models.mt5_position import MT5Position





T = TypeVar("T", bound="TradeAccountSetRequest")



@_attrs_define
class TradeAccountSetRequest:
    """ State of an account taken from an external trading system, v2 request DTO.

        Attributes:
            request_id (int | None | Unset): Caller-side identifier used to tie the call to its completion event; optional.
            login (int | Unset): Login of the account whose data is synchronised.
            balance (float | None | Unset): Balance the account must have after the synchronisation.
            orders (list[MT5Order] | None | Unset): Orders the account must have; omitted means the orders are not
                synchronised.
            positions (list[MT5Position] | None | Unset): Positions the account must have; omitted means the positions are
                not synchronised.
     """

    request_id: int | None | Unset = UNSET
    login: int | Unset = UNSET
    balance: float | None | Unset = UNSET
    orders: list[MT5Order] | None | Unset = UNSET
    positions: list[MT5Position] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_order import MT5Order
        from ..models.mt5_position import MT5Position
        request_id: int | None | Unset
        if isinstance(self.request_id, Unset):
            request_id = UNSET
        else:
            request_id = self.request_id

        login = self.login

        balance: float | None | Unset
        if isinstance(self.balance, Unset):
            balance = UNSET
        else:
            balance = self.balance

        orders: list[dict[str, Any]] | None | Unset
        if isinstance(self.orders, Unset):
            orders = UNSET
        elif isinstance(self.orders, list):
            orders = []
            for orders_type_0_item_data in self.orders:
                orders_type_0_item = orders_type_0_item_data.to_dict()
                orders.append(orders_type_0_item)


        else:
            orders = self.orders

        positions: list[dict[str, Any]] | None | Unset
        if isinstance(self.positions, Unset):
            positions = UNSET
        elif isinstance(self.positions, list):
            positions = []
            for positions_type_0_item_data in self.positions:
                positions_type_0_item = positions_type_0_item_data.to_dict()
                positions.append(positions_type_0_item)


        else:
            positions = self.positions


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if request_id is not UNSET:
            field_dict["requestId"] = request_id
        if login is not UNSET:
            field_dict["login"] = login
        if balance is not UNSET:
            field_dict["balance"] = balance
        if orders is not UNSET:
            field_dict["orders"] = orders
        if positions is not UNSET:
            field_dict["positions"] = positions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_order import MT5Order
        from ..models.mt5_position import MT5Position
        d = dict(src_dict)
        def _parse_request_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        request_id = _parse_request_id(d.pop("requestId", UNSET))


        login = d.pop("login", UNSET)

        def _parse_balance(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        balance = _parse_balance(d.pop("balance", UNSET))


        def _parse_orders(data: object) -> list[MT5Order] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                orders_type_0 = []
                _orders_type_0 = data
                for orders_type_0_item_data in (_orders_type_0):
                    orders_type_0_item = MT5Order.from_dict(orders_type_0_item_data)



                    orders_type_0.append(orders_type_0_item)

                return orders_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5Order] | None | Unset, data)

        orders = _parse_orders(d.pop("orders", UNSET))


        def _parse_positions(data: object) -> list[MT5Position] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                positions_type_0 = []
                _positions_type_0 = data
                for positions_type_0_item_data in (_positions_type_0):
                    positions_type_0_item = MT5Position.from_dict(positions_type_0_item_data)



                    positions_type_0.append(positions_type_0_item)

                return positions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5Position] | None | Unset, data)

        positions = _parse_positions(d.pop("positions", UNSET))


        trade_account_set_request = cls(
            request_id=request_id,
            login=login,
            balance=balance,
            orders=orders,
            positions=positions,
        )

        return trade_account_set_request

