import pytest
from cplugin_webapi_sdk.environments import resolve_environment, ResolvedEnvironment


def test_prod_preset():
    r = resolve_environment("prod")
    assert r == ResolvedEnvironment("https://cloud.mywebapi.com", "https://auth.cplugin.net")


def test_staging_preset():
    r = resolve_environment("staging")
    assert r == ResolvedEnvironment("https://pre.mywebapi.com", "https://pre.auth.cplugin.net")


def test_custom_strips_trailing_slashes():
    r = resolve_environment("custom", api_base_url="http://localhost:5002/",
                            authority="http://localhost:5001/")
    assert r == ResolvedEnvironment("http://localhost:5002", "http://localhost:5001")


def test_custom_requires_both_urls():
    with pytest.raises(ValueError):
        resolve_environment("custom", api_base_url="http://x")
