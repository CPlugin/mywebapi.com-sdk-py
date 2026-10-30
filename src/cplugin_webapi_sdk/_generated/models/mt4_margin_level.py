from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.margin_controlling_type import MarginControllingType
from ..models.margin_level_type import MarginLevelType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4MarginLevel")



@_attrs_define
class MT4MarginLevel:
    """ v2 DTO mirroring the platform's MarginLevel record. All fields are kept
    because clients monitoring margin call / stop-out conditions need the
    complete state. ControllingType and LevelType are returned as their names
    (e.g. "Percent" rather than 0).

        Attributes:
            login (int | Unset): Trading account number
            group (None | str | Unset): Group the account belongs to
            leverage (int | Unset): Account leverage (e.g. 100 means 1:100)
            updated (int | Unset): Last update timestamp (MT4 unix-time int)
            balance (float | Unset): Account balance (deposit minus losses)
            equity (float | Unset): Equity (balance + floating P&L)
            volume (int | Unset): Open volume across all positions
            margin (float | Unset): Used margin
            free (float | Unset): Free margin (equity − margin)
            level (float | Unset): Margin level in % (equity / margin × 100)
            controlling_type (MarginControllingType | Unset):
            level_type (MarginLevelType | Unset):
     """

    login: int | Unset = UNSET
    group: None | str | Unset = UNSET
    leverage: int | Unset = UNSET
    updated: int | Unset = UNSET
    balance: float | Unset = UNSET
    equity: float | Unset = UNSET
    volume: int | Unset = UNSET
    margin: float | Unset = UNSET
    free: float | Unset = UNSET
    level: float | Unset = UNSET
    controlling_type: MarginControllingType | Unset = UNSET
    level_type: MarginLevelType | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        group: None | str | Unset
        if isinstance(self.group, Unset):
            group = UNSET
        else:
            group = self.group

        leverage = self.leverage

        updated = self.updated

        balance = self.balance

        equity = self.equity

        volume = self.volume

        margin = self.margin

        free = self.free

        level = self.level

        controlling_type: str | Unset = UNSET
        if not isinstance(self.controlling_type, Unset):
            controlling_type = self.controlling_type.value


        level_type: str | Unset = UNSET
        if not isinstance(self.level_type, Unset):
            level_type = self.level_type.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if group is not UNSET:
            field_dict["group"] = group
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if updated is not UNSET:
            field_dict["updated"] = updated
        if balance is not UNSET:
            field_dict["balance"] = balance
        if equity is not UNSET:
            field_dict["equity"] = equity
        if volume is not UNSET:
            field_dict["volume"] = volume
        if margin is not UNSET:
            field_dict["margin"] = margin
        if free is not UNSET:
            field_dict["free"] = free
        if level is not UNSET:
            field_dict["level"] = level
        if controlling_type is not UNSET:
            field_dict["controllingType"] = controlling_type
        if level_type is not UNSET:
            field_dict["levelType"] = level_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        def _parse_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        group = _parse_group(d.pop("group", UNSET))


        leverage = d.pop("leverage", UNSET)

        updated = d.pop("updated", UNSET)

        balance = d.pop("balance", UNSET)

        equity = d.pop("equity", UNSET)

        volume = d.pop("volume", UNSET)

        margin = d.pop("margin", UNSET)

        free = d.pop("free", UNSET)

        level = d.pop("level", UNSET)

        _controlling_type = d.pop("controllingType", UNSET)
        controlling_type: MarginControllingType | Unset
        if isinstance(_controlling_type,  Unset):
            controlling_type = UNSET
        else:
            controlling_type = MarginControllingType(_controlling_type)




        _level_type = d.pop("levelType", UNSET)
        level_type: MarginLevelType | Unset
        if isinstance(_level_type,  Unset):
            level_type = UNSET
        else:
            level_type = MarginLevelType(_level_type)




        mt4_margin_level = cls(
            login=login,
            group=group,
            leverage=leverage,
            updated=updated,
            balance=balance,
            equity=equity,
            volume=volume,
            margin=margin,
            free=free,
            level=level,
            controlling_type=controlling_type,
            level_type=level_type,
        )

        return mt4_margin_level

