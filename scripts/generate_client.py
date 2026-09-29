"""Regenerate the endpoint client + models from the vendored spec.

Replaces the old datamodel-code-generator flow. Output lands under
src/cplugin_webapi_sdk/_generated and is regenerated wholesale (never edited
by hand).

Requires the `codegen` extra:  pip install -e ".[codegen]"
Usage: python scripts/generate_client.py
"""
from __future__ import annotations

import json
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


def _prepare_spec(spec: dict) -> dict:
    """Adjust the vendored spec for code generation; the vendored file itself stays verbatim.

    - The server documents each operation's own default timeout as the schema
      ``default`` of the ``X-Request-Timeout`` header. openapi-python-client turns
      a parameter default into a keyword default and then always sends it, which
      would pin today's server defaults into every generated call. Dropping the
      default leaves the header out unless the caller sets it (the SDK sets it
      from ``request_timeout=``); the per-operation default stays in the docstring.
    - A ``servers: null`` (seen in hand-merged specs) is removed: the generator
      requires a list there.
    """
    if spec.get("servers") is None:
        spec.pop("servers", None)
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
    prepared = _prepare_spec(json.loads(SPEC.read_text(encoding="utf-8")))
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
    print(f"generated client at {GENERATED}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
