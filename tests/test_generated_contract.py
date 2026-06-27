"""I-2: Guard test — fails loudly if _get_kwargs disappears from generated modules.

The facade client.py bypasses the generated _build_response/_parse_response pipeline
by calling _get_kwargs directly. This is a private symbol of openapi-python-client;
if a generator upgrade renames it, every namespace method will raise AttributeError
at call time rather than import time.

This test surfaces that breakage immediately after regeneration.
"""
from __future__ import annotations


def test_generated_ops_expose_get_kwargs():
    """I-2: _get_kwargs must be present on the server-time module after any regeneration."""
    from cplugin_webapi_sdk._generated.api.mt4_v_2_common import (
        get_api_v_2_mt4_trade_platform_server_time as m,
    )
    assert callable(getattr(m, "_get_kwargs", None)), (
        "_get_kwargs removed from generated module — client.py bypass is broken. "
        "Re-verify after every regeneration: "
        "grep -r '_get_kwargs' src/cplugin_webapi_sdk/_generated/api/"
    )


def test_symbol_info_module_exposes_get_kwargs():
    """I-2: _get_kwargs must be present on the symbol-info module (has an optional param)."""
    from cplugin_webapi_sdk._generated.api.mt4_v_2_symbols import (
        get_api_v_2_mt4_trade_platform_symbol_info_get as m,
    )
    assert callable(getattr(m, "_get_kwargs", None)), (
        "_get_kwargs removed from symbol_info generated module — client.py bypass is broken."
    )


def test_q3_bad_op_module_raises_type_error():
    """Q-3: _call_sync/_call_async must raise TypeError for a module without _get_kwargs."""
    import httpx
    import pytest
    from cplugin_webapi_sdk.client import _call_sync

    class _NotAnOpModule:
        pass

    fake_http = httpx.Client()
    with pytest.raises(TypeError, match="_get_kwargs"):
        _call_sync(fake_http, _NotAnOpModule())
    fake_http.close()
