from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.mt5_con_subscription_symbol import MT5ConSubscriptionSymbol





T = TypeVar("T", bound="MT5ConSubscription")



@_attrs_define
class MT5ConSubscription:
    """ A subscription configuration of the trade server.

        Attributes:
            id (int | None | Unset): Unique configuration identifier assigned by the server.
            parent_id (int | None | Unset): Identifier of the directory the configuration is placed in; zero means the root
                directory.
            depends_id (int | None | Unset): Identifier of the configuration this one depends on; zero means no dependency.
            name (None | str | Unset): Configuration name.
            type_ (int | None | Unset): Subscription type code.
            image (int | None | Unset): Logo identifier shown for the subscription.
            description (None | str | Unset): Description of the subscription.
            url_description (None | str | Unset): Link to an additional description of the subscription.
            url_agreement (None | str | Unset): Link to the subscription agreement.
            control_mode (int | None | Unset): Code of the actions the client terminals are allowed to perform with the
                subscription.
            period_mode (int | None | Unset): Subscription period code.
            period_custom (int | None | Unset): Custom subscription period in days, used when `periodMode` selects a custom
                period.
            period_free_mode (int | None | Unset): Trial (free) period code.
            period_free_custom (int | None | Unset): Custom trial period value, used when `periodFreeMode` selects a custom
                trial period.
            flags (int | None | Unset): Additional subscription property flags.
            price (float | None | Unset): Subscription price for non-professional traders.
            price_pro (float | None | Unset): Subscription price for professional traders.
            price_currency (None | str | Unset): Currency of the subscription price.
            countries (list[str] | None | Unset): Countries the subscription is available in.
            groups (list[str] | None | Unset): Account groups the subscription is available in.
            symbols (list[MT5ConSubscriptionSymbol] | None | Unset): Trading instruments the subscription covers.
     """

    id: int | None | Unset = UNSET
    parent_id: int | None | Unset = UNSET
    depends_id: int | None | Unset = UNSET
    name: None | str | Unset = UNSET
    type_: int | None | Unset = UNSET
    image: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    url_description: None | str | Unset = UNSET
    url_agreement: None | str | Unset = UNSET
    control_mode: int | None | Unset = UNSET
    period_mode: int | None | Unset = UNSET
    period_custom: int | None | Unset = UNSET
    period_free_mode: int | None | Unset = UNSET
    period_free_custom: int | None | Unset = UNSET
    flags: int | None | Unset = UNSET
    price: float | None | Unset = UNSET
    price_pro: float | None | Unset = UNSET
    price_currency: None | str | Unset = UNSET
    countries: list[str] | None | Unset = UNSET
    groups: list[str] | None | Unset = UNSET
    symbols: list[MT5ConSubscriptionSymbol] | None | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.mt5_con_subscription_symbol import MT5ConSubscriptionSymbol
        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        parent_id: int | None | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        else:
            parent_id = self.parent_id

        depends_id: int | None | Unset
        if isinstance(self.depends_id, Unset):
            depends_id = UNSET
        else:
            depends_id = self.depends_id

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        type_: int | None | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        image: int | None | Unset
        if isinstance(self.image, Unset):
            image = UNSET
        else:
            image = self.image

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        url_description: None | str | Unset
        if isinstance(self.url_description, Unset):
            url_description = UNSET
        else:
            url_description = self.url_description

        url_agreement: None | str | Unset
        if isinstance(self.url_agreement, Unset):
            url_agreement = UNSET
        else:
            url_agreement = self.url_agreement

        control_mode: int | None | Unset
        if isinstance(self.control_mode, Unset):
            control_mode = UNSET
        else:
            control_mode = self.control_mode

        period_mode: int | None | Unset
        if isinstance(self.period_mode, Unset):
            period_mode = UNSET
        else:
            period_mode = self.period_mode

        period_custom: int | None | Unset
        if isinstance(self.period_custom, Unset):
            period_custom = UNSET
        else:
            period_custom = self.period_custom

        period_free_mode: int | None | Unset
        if isinstance(self.period_free_mode, Unset):
            period_free_mode = UNSET
        else:
            period_free_mode = self.period_free_mode

        period_free_custom: int | None | Unset
        if isinstance(self.period_free_custom, Unset):
            period_free_custom = UNSET
        else:
            period_free_custom = self.period_free_custom

        flags: int | None | Unset
        if isinstance(self.flags, Unset):
            flags = UNSET
        else:
            flags = self.flags

        price: float | None | Unset
        if isinstance(self.price, Unset):
            price = UNSET
        else:
            price = self.price

        price_pro: float | None | Unset
        if isinstance(self.price_pro, Unset):
            price_pro = UNSET
        else:
            price_pro = self.price_pro

        price_currency: None | str | Unset
        if isinstance(self.price_currency, Unset):
            price_currency = UNSET
        else:
            price_currency = self.price_currency

        countries: list[str] | None | Unset
        if isinstance(self.countries, Unset):
            countries = UNSET
        elif isinstance(self.countries, list):
            countries = self.countries


        else:
            countries = self.countries

        groups: list[str] | None | Unset
        if isinstance(self.groups, Unset):
            groups = UNSET
        elif isinstance(self.groups, list):
            groups = self.groups


        else:
            groups = self.groups

        symbols: list[dict[str, Any]] | None | Unset
        if isinstance(self.symbols, Unset):
            symbols = UNSET
        elif isinstance(self.symbols, list):
            symbols = []
            for symbols_type_0_item_data in self.symbols:
                symbols_type_0_item = symbols_type_0_item_data.to_dict()
                symbols.append(symbols_type_0_item)


        else:
            symbols = self.symbols


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if depends_id is not UNSET:
            field_dict["dependsId"] = depends_id
        if name is not UNSET:
            field_dict["name"] = name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if image is not UNSET:
            field_dict["image"] = image
        if description is not UNSET:
            field_dict["description"] = description
        if url_description is not UNSET:
            field_dict["urlDescription"] = url_description
        if url_agreement is not UNSET:
            field_dict["urlAgreement"] = url_agreement
        if control_mode is not UNSET:
            field_dict["controlMode"] = control_mode
        if period_mode is not UNSET:
            field_dict["periodMode"] = period_mode
        if period_custom is not UNSET:
            field_dict["periodCustom"] = period_custom
        if period_free_mode is not UNSET:
            field_dict["periodFreeMode"] = period_free_mode
        if period_free_custom is not UNSET:
            field_dict["periodFreeCustom"] = period_free_custom
        if flags is not UNSET:
            field_dict["flags"] = flags
        if price is not UNSET:
            field_dict["price"] = price
        if price_pro is not UNSET:
            field_dict["pricePro"] = price_pro
        if price_currency is not UNSET:
            field_dict["priceCurrency"] = price_currency
        if countries is not UNSET:
            field_dict["countries"] = countries
        if groups is not UNSET:
            field_dict["groups"] = groups
        if symbols is not UNSET:
            field_dict["symbols"] = symbols

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mt5_con_subscription_symbol import MT5ConSubscriptionSymbol
        d = dict(src_dict)
        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))


        def _parse_parent_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        parent_id = _parse_parent_id(d.pop("parentId", UNSET))


        def _parse_depends_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        depends_id = _parse_depends_id(d.pop("dependsId", UNSET))


        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        def _parse_type_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))


        def _parse_image(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        image = _parse_image(d.pop("image", UNSET))


        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_url_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_description = _parse_url_description(d.pop("urlDescription", UNSET))


        def _parse_url_agreement(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url_agreement = _parse_url_agreement(d.pop("urlAgreement", UNSET))


        def _parse_control_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        control_mode = _parse_control_mode(d.pop("controlMode", UNSET))


        def _parse_period_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period_mode = _parse_period_mode(d.pop("periodMode", UNSET))


        def _parse_period_custom(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period_custom = _parse_period_custom(d.pop("periodCustom", UNSET))


        def _parse_period_free_mode(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period_free_mode = _parse_period_free_mode(d.pop("periodFreeMode", UNSET))


        def _parse_period_free_custom(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period_free_custom = _parse_period_free_custom(d.pop("periodFreeCustom", UNSET))


        def _parse_flags(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        flags = _parse_flags(d.pop("flags", UNSET))


        def _parse_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price = _parse_price(d.pop("price", UNSET))


        def _parse_price_pro(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        price_pro = _parse_price_pro(d.pop("pricePro", UNSET))


        def _parse_price_currency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        price_currency = _parse_price_currency(d.pop("priceCurrency", UNSET))


        def _parse_countries(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                countries_type_0 = cast(list[str], data)

                return countries_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        countries = _parse_countries(d.pop("countries", UNSET))


        def _parse_groups(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                groups_type_0 = cast(list[str], data)

                return groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        groups = _parse_groups(d.pop("groups", UNSET))


        def _parse_symbols(data: object) -> list[MT5ConSubscriptionSymbol] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                symbols_type_0 = []
                _symbols_type_0 = data
                for symbols_type_0_item_data in (_symbols_type_0):
                    symbols_type_0_item = MT5ConSubscriptionSymbol.from_dict(symbols_type_0_item_data)



                    symbols_type_0.append(symbols_type_0_item)

                return symbols_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[MT5ConSubscriptionSymbol] | None | Unset, data)

        symbols = _parse_symbols(d.pop("symbols", UNSET))


        mt5_con_subscription = cls(
            id=id,
            parent_id=parent_id,
            depends_id=depends_id,
            name=name,
            type_=type_,
            image=image,
            description=description,
            url_description=url_description,
            url_agreement=url_agreement,
            control_mode=control_mode,
            period_mode=period_mode,
            period_custom=period_custom,
            period_free_mode=period_free_mode,
            period_free_custom=period_free_custom,
            flags=flags,
            price=price,
            price_pro=price_pro,
            price_currency=price_currency,
            countries=countries,
            groups=groups,
            symbols=symbols,
        )

        return mt5_con_subscription

