"""Regenerate the endpoint client + models from the vendored spec.

Replaces the old datamodel-code-generator flow. Output lands under
src/cplugin_webapi_sdk/_generated and is regenerated wholesale (never edited
by hand).

Requires the `codegen` extra:  pip install -e ".[codegen]"
Usage: python scripts/generate_client.py
"""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = ROOT / "src" / "cplugin_webapi_sdk" / "spec" / "v2.json"
CONFIG = ROOT / "openapi_python_client_config.yaml"
PKG = ROOT / "src" / "cplugin_webapi_sdk"
GENERATED = PKG / "_generated"


def main() -> int:
    if shutil.which("openapi-python-client") is None:
        print("openapi-python-client not on PATH — `pip install -e \".[codegen]\"`", file=sys.stderr)
        return 1
    if not SPEC.exists():
        print(f"spec missing at {SPEC} — run scripts/fetch_spec.py first", file=sys.stderr)
        return 1
    if GENERATED.exists():
        shutil.rmtree(GENERATED)
    # * generate into a temp project dir, then relocate the package tree into
    #   src/cplugin_webapi_sdk/_generated so imports are cplugin_webapi_sdk._generated.*
    cmd = [
        "openapi-python-client", "generate",
        "--path", str(SPEC),
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
