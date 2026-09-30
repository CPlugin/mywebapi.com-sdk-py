"""Regenerate the endpoint client + models from the vendored spec.

Replaces the old datamodel-code-generator flow. Output lands under
src/cplugin_webapi_sdk/_generated and is regenerated wholesale (never edited
by hand).

Requires the `codegen` extra:  pip install -e ".[codegen]"
Usage: python scripts/generate_client.py
"""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "src" / "cplugin_webapi_sdk" / "spec" / "v2.json"
CONFIG = ROOT / "openapi_python_client_config.yaml"
PKG = ROOT / "src" / "cplugin_webapi_sdk"
GENERATED = PKG / "_generated"

# * Request-timeout header the server documents on every trade-platform operation.
TIMEOUT_HEADER = "x-request-timeout"
# * Machine-owned table of per-operation server defaults, read by client.py.
TIMEOUTS_MODULE = GENERATED / "operation_timeouts.py"

_METHOD_RE = re.compile(r'"method":\s*"([a-z]+)"')
_URL_RE = re.compile(r'"url":\s*"([^"]+)"')
_PARAM_RE = re.compile(r"\{[^}]*\}")


def _route_key(method: str, path: str) -> tuple[str, str]:
    # * Path parameters are renamed by the generator (tradePlatform -> trade_platform);
    #   compare templates with the parameter names blanked out.
    return method.lower(), _PARAM_RE.sub("{}", path).lower()


def _timeout_defaults(spec: dict) -> dict[tuple[str, str], float]:
    """Per-operation default of the X-Request-Timeout header, keyed by (method, path template)."""
    defaults: dict[tuple[str, str], float] = {}
    for path, item in spec.get("paths", {}).items():
        for method, op in item.items():
            if not isinstance(op, dict):
                continue
            for param in op.get("parameters", []):
                if param.get("in") == "header" and str(param.get("name", "")).lower() == TIMEOUT_HEADER:
                    default = param.get("schema", {}).get("default")
                    if isinstance(default, (int, float)):
                        defaults[_route_key(method, path)] = float(default)
    return defaults


def _write_timeouts_module(defaults: dict[tuple[str, str], float]) -> int:
    """Map every generated op module to its server default; return how many have one."""
    table: dict[str, float] = {}
    for module in sorted((GENERATED / "api").glob("*/*.py")):
        if module.name == "__init__.py":
            continue
        source = module.read_text(encoding="utf-8")
        method, url = _METHOD_RE.search(source), _URL_RE.search(source)
        if not (method and url):
            raise SystemExit(f"cannot read method/url of {module}")
        seconds = defaults.get(_route_key(method.group(1), url.group(1)))
        if seconds is not None:
            table[f"{module.parent.name}.{module.stem}"] = seconds
    lines = [
        '"""Server default of X-Request-Timeout per generated operation, in seconds.',
        "",
        "Written by scripts/generate_client.py from the spec; never edit by hand.",
        "Keys are ``<tag package>.<operation module>``. Operations without a",
        "documented default are absent.",
        '"""',
        "",
        "DEFAULTS: dict[str, float] = {",
        *(f'    "{key}": {value!r},' for key, value in table.items()),
        "}",
        "",
    ]
    TIMEOUTS_MODULE.write_text("\n".join(lines), encoding="utf-8")
    return len(table)


def _prepare_spec(spec: dict) -> dict:
    """Adjust the vendored spec for code generation; the vendored file itself stays verbatim.

    - The server documents each operation's own default timeout as the schema
      ``default`` of the ``X-Request-Timeout`` header. openapi-python-client turns
      a parameter default into a keyword default and then always sends it, which
      would pin today's server defaults into every generated call. Dropping the
      default leaves the header out unless the caller sets it (the SDK sets it
      from ``request_timeout=``); the per-operation default stays in the docstring
      and in ``_generated/operation_timeouts.py``.
    """
    for item in spec.get("paths", {}).values():
        for op in item.values():
            if not isinstance(op, dict):
                continue
            for param in op.get("parameters", []):
                if param.get("in") == "header" and str(param.get("name", "")).lower() == TIMEOUT_HEADER:
                    param.get("schema", {}).pop("default", None)
    return spec


def main() -> int:
    if shutil.which("openapi-python-client") is None:
        print("openapi-python-client not on PATH — `pip install -e \".[codegen]\"`", file=sys.stderr)
        return 1
    if not SPEC.exists():
        print(f"spec missing at {SPEC} — run scripts/fetch_spec.py first", file=sys.stderr)
        return 1
    if GENERATED.exists():
        shutil.rmtree(GENERATED)
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    defaults = _timeout_defaults(spec)
    prepared = _prepare_spec(spec)
    with tempfile.TemporaryDirectory() as tmp:
        prepared_path = Path(tmp) / "v2.json"
        prepared_path.write_text(json.dumps(prepared), encoding="utf-8")
        # * generate into a temp project dir, then relocate the package tree into
        #   src/cplugin_webapi_sdk/_generated so imports are cplugin_webapi_sdk._generated.*
        cmd = [
            "openapi-python-client", "generate",
            "--path", str(prepared_path),
            "--config", str(CONFIG),
            "--output-path", str(PKG / "_gen_tmp"),
            "--overwrite",
            "--meta", "none",
        ]
        result = subprocess.run(cmd, cwd=ROOT)
    if result.returncode != 0:
        return result.returncode
    produced = PKG / "_gen_tmp"
    shutil.move(str(produced), str(GENERATED))
    mapped = _write_timeouts_module(defaults)
    if mapped != len(defaults):
        print(f"! {len(defaults)} operations document a timeout, {mapped} generated modules matched", file=sys.stderr)
        return 1
    print(f"generated client at {GENERATED} ({mapped} operations with a default timeout)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
