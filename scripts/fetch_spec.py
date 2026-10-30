"""Fetch the v2 OpenAPI document from STAGING and write the vendored spec.

Staging is the reliable source. The main app and the x86 sidecar each expose a
swagger document; we union their `paths` and `components.schemas` into one
canonical file, matching the union the TS SDK performs.

Offline use: set ``WEBAPI_SPEC_FILE`` to a local x64 (main app) document and no
HTTP request is made. The sidecar routes are compiled out of that build, so the
previous vendored document is unioned in as the sidecar source — the same union
the online run performs against pre-x86.

Usage: python scripts/fetch_spec.py
       WEBAPI_SPEC_FILE=/path/to/swagger-v2.json python scripts/fetch_spec.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import httpx

MAIN_URL = "https://pre.mywebapi.com/swagger/v2/swagger.json"
SIDECAR_URL = "https://pre-x86.mywebapi.com/swagger/v2/swagger.json"
OUT = Path(__file__).resolve().parent.parent / "src" / "cplugin_webapi_sdk" / "spec" / "v2.json"
# * Local main-app document: skips the network entirely (CI-less rebuilds).
LOCAL_SPEC_ENV = "WEBAPI_SPEC_FILE"


def _merge(base: dict, extra: dict) -> dict:
    base.setdefault("paths", {})
    base.setdefault("components", {}).setdefault("schemas", {})
    for path, item in extra.get("paths", {}).items():
        base["paths"].setdefault(path, item)
    for name, schema in extra.get("components", {}).get("schemas", {}).items():
        base["components"]["schemas"].setdefault(name, schema)
    return base


def main() -> int:
    local_spec = os.environ.get(LOCAL_SPEC_ENV)
    if local_spec:
        main_doc = json.loads(Path(local_spec).read_text(encoding="utf-8"))
        # * The local build is x64-only and lacks the MT4 x86 sidecar routes;
        # *   keep them from the previous union rather than dropping operations.
        previous = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
        merged = _merge(main_doc, previous)
    else:
        with httpx.Client(timeout=30) as http:
            main_doc = http.get(MAIN_URL).raise_for_status().json()
            sidecar_doc = http.get(SIDECAR_URL).raise_for_status().json()
        merged = _merge(main_doc, sidecar_doc)
    path_count = len(merged["paths"])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(merged, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({path_count} paths)")
    if path_count < 174:
        print(f"! expected >= 174 paths, got {path_count}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
