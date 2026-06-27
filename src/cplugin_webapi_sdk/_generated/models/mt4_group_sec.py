from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4GroupSec")



@_attrs_define
class MT4GroupSec:
    """ v2 DTO for one entry in a group's `SecGroups` array (32 elements
    indexed by symbol-group). Curated from `ConGroupSec`; drops the
    `Reserved` int[3] padding. Enum fields are typed as string for
    the leaf-nested-generic STJ source-gen reason — see
    feedback-stj-enum-leaf-nested.

        Attributes:
            show (int | Unset): 0 = security group hidden from clients, non-zero = visible
            trade (int | Unset): 0 = trading disabled, non-zero = trading enabled
            dealing_mode (None | str | Unset): Dealing mode (Manual / Auto / Activity)
            standard_commission (float | Unset): Standard commission
            commission_type (None | str | Unset): Commission type (Money / Pips / Percent)
            commission_lots_mode (None | str | Unset): Commission lots mode (PerLot / PerDeal)
            agent_commission (float | Unset): Agent commission
            agent_commission_mode (None | str | Unset): Agent commission type (Money / Pips)
            spread_diff (int | Unset): Spread difference compared to default symbol spread
            lot_min (int | Unset): Minimum allowed lot size (in 1/100 lot units, e.g. 100 = 1 lot)
            lot_max (int | Unset): Maximum allowed lot size
            lot_step (int | Unset): Lot step (10 lot = 1000, 1 lot = 100, 0.1 lot = 10)
            ie_deviation (int | Unset): Max price deviation in Instant Execution mode
            confirmation (int | Unset): 0 = no confirmation, non-zero = request mode confirmation
            trade_rights (None | str | Unset): Clients trade rights bit mask (string-encoded)
            ie_quick_mode (int | Unset): 0 = normal, non-zero = don't resend on deviation in IE
            auto_close_out_mode (None | str | Unset): Auto close-out method (None / HiHi / LoLo / FIFO / LIFO / ...)
            commission_taxes (float | Unset): Commission taxes
            commission_agent_lots (None | str | Unset): Agent commission lots mode
            free_margin_mode (int | Unset): 0 = strict margin check, non-zero = soft check
     """

    show: int | Unset = UNSET
    trade: int | Unset = UNSET
    dealing_mode: None | str | Unset = UNSET
    standard_commission: float | Unset = UNSET
    commission_type: None | str | Unset = UNSET
    commission_lots_mode: None | str | Unset = UNSET
    agent_commission: float | Unset = UNSET
    agent_commission_mode: None | str | Unset = UNSET
    spread_diff: int | Unset = UNSET
    lot_min: int | Unset = UNSET
    lot_max: int | Unset = UNSET
    lot_step: int | Unset = UNSET
    ie_deviation: int | Unset = UNSET
    confirmation: int | Unset = UNSET
    trade_rights: None | str | Unset = UNSET
    ie_quick_mode: int | Unset = UNSET
    auto_close_out_mode: None | str | Unset = UNSET
    commission_taxes: float | Unset = UNSET
    commission_agent_lots: None | str | Unset = UNSET
    free_margin_mode: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        show = self.show

        trade = self.trade

        dealing_mode: None | str | Unset
        if isinstance(self.dealing_mode, Unset):
            dealing_mode = UNSET
        else:
            dealing_mode = self.dealing_mode

        standard_commission = self.standard_commission

        commission_type: None | str | Unset
        if isinstance(self.commission_type, Unset):
            commission_type = UNSET
        else:
            commission_type = self.commission_type

        commission_lots_mode: None | str | Unset
        if isinstance(self.commission_lots_mode, Unset):
            commission_lots_mode = UNSET
        else:
            commission_lots_mode = self.commission_lots_mode

        agent_commission = self.agent_commission

        agent_commission_mode: None | str | Unset
        if isinstance(self.agent_commission_mode, Unset):
            agent_commission_mode = UNSET
        else:
            agent_commission_mode = self.agent_commission_mode

        spread_diff = self.spread_diff

        lot_min = self.lot_min

        lot_max = self.lot_max

        lot_step = self.lot_step

        ie_deviation = self.ie_deviation

        confirmation = self.confirmation

        trade_rights: None | str | Unset
        if isinstance(self.trade_rights, Unset):
            trade_rights = UNSET
        else:
            trade_rights = self.trade_rights

        ie_quick_mode = self.ie_quick_mode

        auto_close_out_mode: None | str | Unset
        if isinstance(self.auto_close_out_mode, Unset):
            auto_close_out_mode = UNSET
        else:
            auto_close_out_mode = self.auto_close_out_mode

        commission_taxes = self.commission_taxes

        commission_agent_lots: None | str | Unset
        if isinstance(self.commission_agent_lots, Unset):
            commission_agent_lots = UNSET
        else:
            commission_agent_lots = self.commission_agent_lots

        free_margin_mode = self.free_margin_mode


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if show is not UNSET:
            field_dict["show"] = show
        if trade is not UNSET:
            field_dict["trade"] = trade
        if dealing_mode is not UNSET:
            field_dict["dealingMode"] = dealing_mode
        if standard_commission is not UNSET:
            field_dict["standardCommission"] = standard_commission
        if commission_type is not UNSET:
            field_dict["commissionType"] = commission_type
        if commission_lots_mode is not UNSET:
            field_dict["commissionLotsMode"] = commission_lots_mode
        if agent_commission is not UNSET:
            field_dict["agentCommission"] = agent_commission
        if agent_commission_mode is not UNSET:
            field_dict["agentCommissionMode"] = agent_commission_mode
        if spread_diff is not UNSET:
            field_dict["spreadDiff"] = spread_diff
        if lot_min is not UNSET:
            field_dict["lotMin"] = lot_min
        if lot_max is not UNSET:
            field_dict["lotMax"] = lot_max
        if lot_step is not UNSET:
            field_dict["lotStep"] = lot_step
        if ie_deviation is not UNSET:
            field_dict["ieDeviation"] = ie_deviation
        if confirmation is not UNSET:
            field_dict["confirmation"] = confirmation
        if trade_rights is not UNSET:
            field_dict["tradeRights"] = trade_rights
        if ie_quick_mode is not UNSET:
            field_dict["ieQuickMode"] = ie_quick_mode
        if auto_close_out_mode is not UNSET:
            field_dict["autoCloseOutMode"] = auto_close_out_mode
        if commission_taxes is not UNSET:
            field_dict["commissionTaxes"] = commission_taxes
        if commission_agent_lots is not UNSET:
            field_dict["commissionAgentLots"] = commission_agent_lots
        if free_margin_mode is not UNSET:
            field_dict["freeMarginMode"] = free_margin_mode

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        show = d.pop("show", UNSET)

        trade = d.pop("trade", UNSET)

        def _parse_dealing_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dealing_mode = _parse_dealing_mode(d.pop("dealingMode", UNSET))


        standard_commission = d.pop("standardCommission", UNSET)

        def _parse_commission_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commission_type = _parse_commission_type(d.pop("commissionType", UNSET))


        def _parse_commission_lots_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commission_lots_mode = _parse_commission_lots_mode(d.pop("commissionLotsMode", UNSET))


        agent_commission = d.pop("agentCommission", UNSET)

        def _parse_agent_commission_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        agent_commission_mode = _parse_agent_commission_mode(d.pop("agentCommissionMode", UNSET))


        spread_diff = d.pop("spreadDiff", UNSET)

        lot_min = d.pop("lotMin", UNSET)

        lot_max = d.pop("lotMax", UNSET)

        lot_step = d.pop("lotStep", UNSET)

        ie_deviation = d.pop("ieDeviation", UNSET)

        confirmation = d.pop("confirmation", UNSET)

        def _parse_trade_rights(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trade_rights = _parse_trade_rights(d.pop("tradeRights", UNSET))


        ie_quick_mode = d.pop("ieQuickMode", UNSET)

        def _parse_auto_close_out_mode(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        auto_close_out_mode = _parse_auto_close_out_mode(d.pop("autoCloseOutMode", UNSET))


        commission_taxes = d.pop("commissionTaxes", UNSET)

        def _parse_commission_agent_lots(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        commission_agent_lots = _parse_commission_agent_lots(d.pop("commissionAgentLots", UNSET))


        free_margin_mode = d.pop("freeMarginMode", UNSET)

        mt4_group_sec = cls(
            show=show,
            trade=trade,
            dealing_mode=dealing_mode,
            standard_commission=standard_commission,
            commission_type=commission_type,
            commission_lots_mode=commission_lots_mode,
            agent_commission=agent_commission,
            agent_commission_mode=agent_commission_mode,
            spread_diff=spread_diff,
            lot_min=lot_min,
            lot_max=lot_max,
            lot_step=lot_step,
            ie_deviation=ie_deviation,
            confirmation=confirmation,
            trade_rights=trade_rights,
            ie_quick_mode=ie_quick_mode,
            auto_close_out_mode=auto_close_out_mode,
            commission_taxes=commission_taxes,
            commission_agent_lots=commission_agent_lots,
            free_margin_mode=free_margin_mode,
        )

        return mt4_group_sec

