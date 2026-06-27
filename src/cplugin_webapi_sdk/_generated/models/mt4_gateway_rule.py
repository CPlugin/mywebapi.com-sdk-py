from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4GatewayRule")



@_attrs_define
class MT4GatewayRule:
    """ v2 DTO for a single MT4 gateway-rule entry (STP execution routing
    policy). Curated subset of the wrapper's ConGatewayRule — drops the
    internal RequestRreserved/ExeReserved padding blocks.
    <br>
    Each rule selects orders by RequestSymbol and RequestGroup (each can
    be an exact name, a wildcard mask, or a group identifier), then
    routes them to ExeAccount (named externally), with execution limits
    expressed in pips and lots.

        Attributes:
            enable (bool | Unset): Whether the rule is active
            name (None | str | Unset): Public name of the rule (assumed unique within the rules table — used as cursor key)
            request_symbol (None | str | Unset): Order-matching symbol name, mask, or symbol-group identifier
            request_group (None | str | Unset): Order-matching account group name or group mask
            exe_account_name (None | str | Unset): Execution gateway-account name
            exe_account_id (int | Unset): Execution gateway-account internal id
            exe_max_deviation (int | Unset): Maximum allowed deviation (pips) between requested and executed price
            exe_max_profit_slippage (int | Unset): Maximum slippage in pips on profit-side execution
            exe_max_profit_slippage_lots (int | Unset): Maximum slippage volume in lots on profit-side execution
            exe_max_losing_slippage (int | Unset): Maximum slippage in pips on losing-side execution
            exe_max_losing_slippage_lots (int | Unset): Maximum slippage volume in lots on losing-side execution
            exe_account_pos (int | Unset): Current open position on the execution account
            exe_volume_percent (int | Unset): Coverage percentage (volume routed externally vs. internal book)
            exe_flags (int | Unset): Execution flags bitmap (raw wrapper int)
     """

    enable: bool | Unset = UNSET
    name: None | str | Unset = UNSET
    request_symbol: None | str | Unset = UNSET
    request_group: None | str | Unset = UNSET
    exe_account_name: None | str | Unset = UNSET
    exe_account_id: int | Unset = UNSET
    exe_max_deviation: int | Unset = UNSET
    exe_max_profit_slippage: int | Unset = UNSET
    exe_max_profit_slippage_lots: int | Unset = UNSET
    exe_max_losing_slippage: int | Unset = UNSET
    exe_max_losing_slippage_lots: int | Unset = UNSET
    exe_account_pos: int | Unset = UNSET
    exe_volume_percent: int | Unset = UNSET
    exe_flags: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        enable = self.enable

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        request_symbol: None | str | Unset
        if isinstance(self.request_symbol, Unset):
            request_symbol = UNSET
        else:
            request_symbol = self.request_symbol

        request_group: None | str | Unset
        if isinstance(self.request_group, Unset):
            request_group = UNSET
        else:
            request_group = self.request_group

        exe_account_name: None | str | Unset
        if isinstance(self.exe_account_name, Unset):
            exe_account_name = UNSET
        else:
            exe_account_name = self.exe_account_name

        exe_account_id = self.exe_account_id

        exe_max_deviation = self.exe_max_deviation

        exe_max_profit_slippage = self.exe_max_profit_slippage

        exe_max_profit_slippage_lots = self.exe_max_profit_slippage_lots

        exe_max_losing_slippage = self.exe_max_losing_slippage

        exe_max_losing_slippage_lots = self.exe_max_losing_slippage_lots

        exe_account_pos = self.exe_account_pos

        exe_volume_percent = self.exe_volume_percent

        exe_flags = self.exe_flags


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if enable is not UNSET:
            field_dict["enable"] = enable
        if name is not UNSET:
            field_dict["name"] = name
        if request_symbol is not UNSET:
            field_dict["requestSymbol"] = request_symbol
        if request_group is not UNSET:
            field_dict["requestGroup"] = request_group
        if exe_account_name is not UNSET:
            field_dict["exeAccountName"] = exe_account_name
        if exe_account_id is not UNSET:
            field_dict["exeAccountId"] = exe_account_id
        if exe_max_deviation is not UNSET:
            field_dict["exeMaxDeviation"] = exe_max_deviation
        if exe_max_profit_slippage is not UNSET:
            field_dict["exeMaxProfitSlippage"] = exe_max_profit_slippage
        if exe_max_profit_slippage_lots is not UNSET:
            field_dict["exeMaxProfitSlippageLots"] = exe_max_profit_slippage_lots
        if exe_max_losing_slippage is not UNSET:
            field_dict["exeMaxLosingSlippage"] = exe_max_losing_slippage
        if exe_max_losing_slippage_lots is not UNSET:
            field_dict["exeMaxLosingSlippageLots"] = exe_max_losing_slippage_lots
        if exe_account_pos is not UNSET:
            field_dict["exeAccountPos"] = exe_account_pos
        if exe_volume_percent is not UNSET:
            field_dict["exeVolumePercent"] = exe_volume_percent
        if exe_flags is not UNSET:
            field_dict["exeFlags"] = exe_flags

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable = d.pop("enable", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_request_symbol(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_symbol = _parse_request_symbol(d.pop("requestSymbol", UNSET))


        def _parse_request_group(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        request_group = _parse_request_group(d.pop("requestGroup", UNSET))


        def _parse_exe_account_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exe_account_name = _parse_exe_account_name(d.pop("exeAccountName", UNSET))


        exe_account_id = d.pop("exeAccountId", UNSET)

        exe_max_deviation = d.pop("exeMaxDeviation", UNSET)

        exe_max_profit_slippage = d.pop("exeMaxProfitSlippage", UNSET)

        exe_max_profit_slippage_lots = d.pop("exeMaxProfitSlippageLots", UNSET)

        exe_max_losing_slippage = d.pop("exeMaxLosingSlippage", UNSET)

        exe_max_losing_slippage_lots = d.pop("exeMaxLosingSlippageLots", UNSET)

        exe_account_pos = d.pop("exeAccountPos", UNSET)

        exe_volume_percent = d.pop("exeVolumePercent", UNSET)

        exe_flags = d.pop("exeFlags", UNSET)

        mt4_gateway_rule = cls(
            enable=enable,
            name=name,
            request_symbol=request_symbol,
            request_group=request_group,
            exe_account_name=exe_account_name,
            exe_account_id=exe_account_id,
            exe_max_deviation=exe_max_deviation,
            exe_max_profit_slippage=exe_max_profit_slippage,
            exe_max_profit_slippage_lots=exe_max_profit_slippage_lots,
            exe_max_losing_slippage=exe_max_losing_slippage,
            exe_max_losing_slippage_lots=exe_max_losing_slippage_lots,
            exe_account_pos=exe_account_pos,
            exe_volume_percent=exe_volume_percent,
            exe_flags=exe_flags,
        )

        return mt4_gateway_rule

