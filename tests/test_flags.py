"""Flag fields travel as names of the set bits ("Enabled, Password"); see flags.py."""
from __future__ import annotations

from cplugin_webapi_sdk import format_flags, has_flag, parse_flags, with_flag
from cplugin_webapi_sdk._generated.models.mt5_user import MT5User

# 4451 — what a real trading platform returns for a regular account: Default plus bit 12, which has no name
RIGHTS = "Enabled, Password, Trailing, Expert, Reports, Bit12"


def test_parse_flags_splits_the_names_of_the_set_bits() -> None:
    assert parse_flags(RIGHTS) == ["Enabled", "Password", "Trailing", "Expert", "Reports", "Bit12"]
    assert parse_flags("None") == []
    assert parse_flags("") == []
    assert parse_flags(None) == []


def test_format_flags_joins_names_and_nothing_is_none() -> None:
    assert format_flags(["Enabled", "Readonly", "Enabled"]) == "Enabled, Readonly"
    assert format_flags([]) == "None"


def test_has_flag_is_case_insensitive() -> None:
    assert has_flag(RIGHTS, "expert")
    assert not has_flag(RIGHTS, "Readonly")
    assert not has_flag("None", "Enabled")


def test_with_flag_sets_and_clears_one_bit_and_keeps_unnamed_ones() -> None:
    readonly = with_flag(RIGHTS, "Readonly")
    assert has_flag(readonly, "Readonly") and has_flag(readonly, "Bit12")
    assert with_flag(readonly, "Readonly", on=False) == RIGHTS
    assert with_flag("Enabled", "Enabled", on=False) == "None"


def test_generated_model_accepts_a_combination() -> None:
    # before: rights was a single-value enum — UsersRights("Enabled, Password") raised ValueError on every account
    # with more than one right
    user = MT5User.from_dict({"login": 2002, "rights": RIGHTS})
    assert has_flag(user.rights, "Expert")
    assert user.to_dict()["rights"] == RIGHTS
