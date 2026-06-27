from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4ManagerRights")



@_attrs_define
class MT4ManagerRights:
    """ v2 DTO for an MT4 manager-account configuration entry. Curated subset
    of the wrapper's ConManager struct — exposes Login/Name/Groups/MailBox,
    the 19 boolean permission rights, IP-filter fields, and InfoDepth.
    Drops internal fields: SecGroups, ExpTime, Unused, Reserved blocks.
    IPFrom/IPTo are widened from uint to long so the JSON-serialized value
    fits inside JS Number safely (no precision loss).

        Attributes:
            login (int | Unset): Manager account login (read-only)
            name (None | str | Unset): Display name of the manager (read-only on the wrapper side)
            groups (None | str | Unset): Comma-separated list of managed group names (wildcard '*' allowed)
            mail_box (None | str | Unset): Internal mailbox name used for manager mail
            info_depth (int | Unset): Maximum reportable history depth, in days
            manager (bool | Unset):
            money (bool | Unset):
            online (bool | Unset):
            risk_man (bool | Unset):
            broker (bool | Unset):
            admin (bool | Unset):
            logs (bool | Unset):
            reports (bool | Unset):
            trades (bool | Unset):
            market_watch (bool | Unset):
            email (bool | Unset):
            user_details (bool | Unset):
            see_trades (bool | Unset):
            news (bool | Unset):
            plugins (bool | Unset):
            market (bool | Unset):
            notifications (bool | Unset):
            server_reports (bool | Unset):
            tech_support (bool | Unset):
            ip_filter (int | Unset): IP filtering mode (0 = disabled; non-zero = enabled — raw MT4 wrapper value, semantics
                preserved)
            ip_from (int | Unset): IP range start (uint widened to long for safe JSON numeric serialization)
            ip_to (int | Unset): IP range end (uint widened to long for safe JSON numeric serialization)
     """

    login: int | Unset = UNSET
    name: None | str | Unset = UNSET
    groups: None | str | Unset = UNSET
    mail_box: None | str | Unset = UNSET
    info_depth: int | Unset = UNSET
    manager: bool | Unset = UNSET
    money: bool | Unset = UNSET
    online: bool | Unset = UNSET
    risk_man: bool | Unset = UNSET
    broker: bool | Unset = UNSET
    admin: bool | Unset = UNSET
    logs: bool | Unset = UNSET
    reports: bool | Unset = UNSET
    trades: bool | Unset = UNSET
    market_watch: bool | Unset = UNSET
    email: bool | Unset = UNSET
    user_details: bool | Unset = UNSET
    see_trades: bool | Unset = UNSET
    news: bool | Unset = UNSET
    plugins: bool | Unset = UNSET
    market: bool | Unset = UNSET
    notifications: bool | Unset = UNSET
    server_reports: bool | Unset = UNSET
    tech_support: bool | Unset = UNSET
    ip_filter: int | Unset = UNSET
    ip_from: int | Unset = UNSET
    ip_to: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        login = self.login

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        groups: None | str | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        else:
            groups = self.groups

        mail_box: None | str | Unset
        if isinstance(self.mail_box, Unset):
            mail_box = UNSET
        else:
            mail_box = self.mail_box

        info_depth = self.info_depth

        manager = self.manager

        money = self.money

        online = self.online

        risk_man = self.risk_man

        broker = self.broker

        admin = self.admin

        logs = self.logs

        reports = self.reports

        trades = self.trades

        market_watch = self.market_watch

        email = self.email

        user_details = self.user_details

        see_trades = self.see_trades

        news = self.news

        plugins = self.plugins

        market = self.market

        notifications = self.notifications

        server_reports = self.server_reports

        tech_support = self.tech_support

        ip_filter = self.ip_filter

        ip_from = self.ip_from

        ip_to = self.ip_to


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if login is not UNSET:
            field_dict["login"] = login
        if name is not UNSET:
            field_dict["name"] = name
        if groups is not UNSET:
            field_dict["groups"] = groups
        if mail_box is not UNSET:
            field_dict["mailBox"] = mail_box
        if info_depth is not UNSET:
            field_dict["infoDepth"] = info_depth
        if manager is not UNSET:
            field_dict["manager"] = manager
        if money is not UNSET:
            field_dict["money"] = money
        if online is not UNSET:
            field_dict["online"] = online
        if risk_man is not UNSET:
            field_dict["riskMan"] = risk_man
        if broker is not UNSET:
            field_dict["broker"] = broker
        if admin is not UNSET:
            field_dict["admin"] = admin
        if logs is not UNSET:
            field_dict["logs"] = logs
        if reports is not UNSET:
            field_dict["reports"] = reports
        if trades is not UNSET:
            field_dict["trades"] = trades
        if market_watch is not UNSET:
            field_dict["marketWatch"] = market_watch
        if email is not UNSET:
            field_dict["email"] = email
        if user_details is not UNSET:
            field_dict["userDetails"] = user_details
        if see_trades is not UNSET:
            field_dict["seeTrades"] = see_trades
        if news is not UNSET:
            field_dict["news"] = news
        if plugins is not UNSET:
            field_dict["plugins"] = plugins
        if market is not UNSET:
            field_dict["market"] = market
        if notifications is not UNSET:
            field_dict["notifications"] = notifications
        if server_reports is not UNSET:
            field_dict["serverReports"] = server_reports
        if tech_support is not UNSET:
            field_dict["techSupport"] = tech_support
        if ip_filter is not UNSET:
            field_dict["ipFilter"] = ip_filter
        if ip_from is not UNSET:
            field_dict["ipFrom"] = ip_from
        if ip_to is not UNSET:
            field_dict["ipTo"] = ip_to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        login = d.pop("login", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_groups(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))


        def _parse_mail_box(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        mail_box = _parse_mail_box(d.pop("mailBox", UNSET))


        info_depth = d.pop("infoDepth", UNSET)

        manager = d.pop("manager", UNSET)

        money = d.pop("money", UNSET)

        online = d.pop("online", UNSET)

        risk_man = d.pop("riskMan", UNSET)

        broker = d.pop("broker", UNSET)

        admin = d.pop("admin", UNSET)

        logs = d.pop("logs", UNSET)

        reports = d.pop("reports", UNSET)

        trades = d.pop("trades", UNSET)

        market_watch = d.pop("marketWatch", UNSET)

        email = d.pop("email", UNSET)

        user_details = d.pop("userDetails", UNSET)

        see_trades = d.pop("seeTrades", UNSET)

        news = d.pop("news", UNSET)

        plugins = d.pop("plugins", UNSET)

        market = d.pop("market", UNSET)

        notifications = d.pop("notifications", UNSET)

        server_reports = d.pop("serverReports", UNSET)

        tech_support = d.pop("techSupport", UNSET)

        ip_filter = d.pop("ipFilter", UNSET)

        ip_from = d.pop("ipFrom", UNSET)

        ip_to = d.pop("ipTo", UNSET)

        mt4_manager_rights = cls(
            login=login,
            name=name,
            groups=groups,
            mail_box=mail_box,
            info_depth=info_depth,
            manager=manager,
            money=money,
            online=online,
            risk_man=risk_man,
            broker=broker,
            admin=admin,
            logs=logs,
            reports=reports,
            trades=trades,
            market_watch=market_watch,
            email=email,
            user_details=user_details,
            see_trades=see_trades,
            news=news,
            plugins=plugins,
            market=market,
            notifications=notifications,
            server_reports=server_reports,
            tech_support=tech_support,
            ip_filter=ip_filter,
            ip_from=ip_from,
            ip_to=ip_to,
        )

        return mt4_manager_rights

