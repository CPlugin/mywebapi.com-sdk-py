from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_symbol_update import MT5SymbolUpdate





T = TypeVar("T", bound="MT5SymbolBatchUpdateItem")



@_attrs_define
class MT5SymbolBatchUpdateItem:
    """ One entry of a batch symbol update: the symbol to change and the fields to write.

        Attributes:
            symbol (None | str | Unset): Symbol name, e.g. `EURUSD`.
            update (MT5SymbolUpdate | None | Unset): Fields to change; fields left out keep their current server value.
     """

    symbol: None | str | Unset = UNSET
    update: MT5SymbolUpdate | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_symbol_update import MT5SymbolUpdate
        symbol: None | str | Unset
        if isinstance(self.symbol, Unset):
            symbol = UNSET
        else:
            symbol = self.symbol

        update: dict[str, Any] | None | Unset
        if isinstance(self.update, Unset):
            update = UNSET
        elif isinstance(self.update, MT5SymbolUpdate):
            update = self.update.to_dict()
        else:
            update = self.update


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if symbol is not UNSET:
            field_dict["symbol"] = symbol
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_symbol_update import MT5SymbolUpdate
        d = dict(src_dict)
        def _parse_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        symbol = _parse_symbol(d.pop("symbol", UNSET))


        def _parse_update(data: object) -> MT5SymbolUpdate | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                update_type_1 = MT5SymbolUpdate.from_dict(data)



                return update_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MT5SymbolUpdate | None | Unset, data)

        update = _parse_update(d.pop("update", UNSET))


        mt5_symbol_batch_update_item = cls(
            symbol=symbol,
            update=update,
        )

        return mt5_symbol_batch_update_item

