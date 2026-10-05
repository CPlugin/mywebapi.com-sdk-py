from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_feed_mode import DataFeedMode
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MT4Feeder")



@_attrs_define
class MT4Feeder:
    """ v2 DTO for a single MT4 quote/news feeder configuration. Curated
    subset of the platform's ConFeeder — drops the platform's Unused
    reserved blob AND the `Password` field (datafeed credentials).

        Attributes:
            name (None | str | Unset): Feeder name (used as cursor key — assumed unique)
            file (None | str | Unset): Datafeed loader filename (DLL or script path)
            server (None | str | Unset): Upstream feeder server address
            login (None | str | Unset): Datafeed login (upstream credential identifier)
            keywords (None | str | Unset): Keywords for news filtering
            enable (int | Unset): Enable flag (0 = disabled, 1 = enabled — raw platform int)
            data_feed_mode (DataFeedMode | Unset):
            timeout (int | Unset): Maximum freeze time in seconds before considered stalled (default ~120)
            timeout_reconnect (int | Unset): Reconnect delay before "sleep" attempts threshold (default ~5s)
            timeout_sleep (int | Unset): Reconnect delay after "sleep" attempts threshold (default ~60s)
            attemps_sleep (int | Unset): Reconnect count before switching to sleep timeout
            news_lang_id (int | Unset): News language id
     """

    name: None | str | Unset = UNSET
    file: None | str | Unset = UNSET
    server: None | str | Unset = UNSET
    login: None | str | Unset = UNSET
    keywords: None | str | Unset = UNSET
    enable: int | Unset = UNSET
    data_feed_mode: DataFeedMode | Unset = UNSET
    timeout: int | Unset = UNSET
    timeout_reconnect: int | Unset = UNSET
    timeout_sleep: int | Unset = UNSET
    attemps_sleep: int | Unset = UNSET
    news_lang_id: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        file: None | str | Unset
        if isinstance(self.file, Unset):
            file = UNSET
        else:
            file = self.file

        server: None | str | Unset
        if isinstance(self.server, Unset):
            server = UNSET
        else:
            server = self.server

        login: None | str | Unset
        if isinstance(self.login, Unset):
            login = UNSET
        else:
            login = self.login

        keywords: None | str | Unset
        if isinstance(self.keywords, Unset):
            keywords = UNSET
        else:
            keywords = self.keywords

        enable = self.enable

        data_feed_mode: str | Unset = UNSET
        if not isinstance(self.data_feed_mode, Unset):
            data_feed_mode = self.data_feed_mode.value


        timeout = self.timeout

        timeout_reconnect = self.timeout_reconnect

        timeout_sleep = self.timeout_sleep

        attemps_sleep = self.attemps_sleep

        news_lang_id = self.news_lang_id


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if file is not UNSET:
            field_dict["file"] = file
        if server is not UNSET:
            field_dict["server"] = server
        if login is not UNSET:
            field_dict["login"] = login
        if keywords is not UNSET:
            field_dict["keywords"] = keywords
        if enable is not UNSET:
            field_dict["enable"] = enable
        if data_feed_mode is not UNSET:
            field_dict["dataFeedMode"] = data_feed_mode
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if timeout_reconnect is not UNSET:
            field_dict["timeoutReconnect"] = timeout_reconnect
        if timeout_sleep is not UNSET:
            field_dict["timeoutSleep"] = timeout_sleep
        if attemps_sleep is not UNSET:
            field_dict["attempsSleep"] = attemps_sleep
        if news_lang_id is not UNSET:
            field_dict["newsLangId"] = news_lang_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_file(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        file = _parse_file(d.pop("file", UNSET))


        def _parse_server(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        server = _parse_server(d.pop("server", UNSET))


        def _parse_login(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        login = _parse_login(d.pop("login", UNSET))


        def _parse_keywords(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        keywords = _parse_keywords(d.pop("keywords", UNSET))


        enable = d.pop("enable", UNSET)

        _data_feed_mode = d.pop("dataFeedMode", UNSET)
        data_feed_mode: DataFeedMode | Unset
        if isinstance(_data_feed_mode,  Unset):
            data_feed_mode = UNSET
        else:
            data_feed_mode = DataFeedMode(_data_feed_mode)




        timeout = d.pop("timeout", UNSET)

        timeout_reconnect = d.pop("timeoutReconnect", UNSET)

        timeout_sleep = d.pop("timeoutSleep", UNSET)

        attemps_sleep = d.pop("attempsSleep", UNSET)

        news_lang_id = d.pop("newsLangId", UNSET)

        mt4_feeder = cls(
            name=name,
            file=file,
            server=server,
            login=login,
            keywords=keywords,
            enable=enable,
            data_feed_mode=data_feed_mode,
            timeout=timeout,
            timeout_reconnect=timeout_reconnect,
            timeout_sleep=timeout_sleep,
            attemps_sleep=attemps_sleep,
            news_lang_id=news_lang_id,
        )

        return mt4_feeder

