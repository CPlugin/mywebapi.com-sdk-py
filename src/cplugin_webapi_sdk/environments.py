"""Environment presets for the v2 SDK. Presets carry only customer-facing
base URLs — no internal hosts, tokens, or credentials.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

EnvironmentName = Literal["prod", "staging", "custom"]


@dataclass(frozen=True)
class ResolvedEnvironment:
    api_base_url: str
    authority: str


_PRESETS: dict[str, ResolvedEnvironment] = {
    "prod": ResolvedEnvironment("https://cloud.mywebapi.com", "https://auth.cplugin.net"),
    "staging": ResolvedEnvironment("https://pre.mywebapi.com", "https://pre.auth.cplugin.net"),
}


def _strip(u: str) -> str:
    # * Strip trailing slashes from URLs to normalize custom environment inputs.
    return u.rstrip("/")


def resolve_environment(
    env: EnvironmentName,
    *,
    api_base_url: str | None = None,
    authority: str | None = None,
) -> ResolvedEnvironment:
    # * Resolve environment configuration by name (preset) or custom URLs.
    # * For custom env, both api_base_url and authority are required and trailing slashes
    # * are stripped to normalize the URLs.
    if env == "custom":
        if not api_base_url or not authority:
            raise ValueError("custom environment requires both api_base_url and authority")
        return ResolvedEnvironment(_strip(api_base_url), _strip(authority))
    preset = _PRESETS.get(env)
    if preset is None:
        raise ValueError(f"unknown environment: {env!r}")
    return preset
