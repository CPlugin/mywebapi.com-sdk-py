"""Flag fields — user rights, group permissions, symbol flags, …

They travel as the names of the set bits joined by ", ": ``"Enabled, Password"``. No bit set is ``"None"``; a
set bit the API has no name for is ``"Bit<n>"`` — keep it when writing the value back, the trading platform may
rely on it. The names and bit values of every flag type are in the OpenAPI spec (``x-enum-varnames`` /
``x-enum-values``).
"""
from __future__ import annotations

from collections.abc import Iterable


def parse_flags(value: str | None) -> list[str]:
    """Names of the set bits; ``"None"``, an empty string and ``None`` give an empty list."""
    if not value:
        return []
    return [n for n in (part.strip() for part in value.split(",")) if n and n.lower() != "none"]


def format_flags(names: Iterable[str]) -> str:
    """The wire form of a set of bit names; no names give ``"None"``. Duplicates are dropped, order is kept."""
    unique = list(dict.fromkeys(n.strip() for n in names if n.strip() and n.strip().lower() != "none"))
    return ", ".join(unique) if unique else "None"


def has_flag(value: str | None, name: str) -> bool:
    """Whether the bit ``name`` is set (names compare case-insensitively, as the API reads them)."""
    wanted = name.lower()
    return any(n.lower() == wanted for n in parse_flags(value))


def with_flag(value: str | None, name: str, on: bool = True) -> str:
    """``value`` with the bit ``name`` set (``on=True``) or cleared; every other bit, unnamed ones included, is kept."""
    wanted = name.lower()
    rest = [n for n in parse_flags(value) if n.lower() != wanted]
    return format_flags([*rest, name] if on else rest)
