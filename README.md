# CPlugin SaaS WebAPI — Python SDK

Python client for the MyWebAPI.com trading platform management API (v2).

> **Develop-only.** This package is not published to PyPI. The distribution name `mywebapi-sdk` is a placeholder; do not rely on it. The package will be released to the private registry once the v2 API reaches production maturity.

## Install

For development, install the package in editable mode from the repo checkout:

```bash
# from clients/python/
pip install -e ".[test]"
```

This installs `cplugin_webapi_sdk` plus the test dependencies. Use `.[codegen]` to add the code-generation toolchain (see [Regenerate](#regenerate)).

## Environment presets

The client ships with two environment presets. Pass `env=` at construction time — no URL configuration needed:

| `env=`       | API base URL                        | Auth URL                            |
|--------------|-------------------------------------|-------------------------------------|
| `"prod"`     | `https://cloud.mywebapi.com`        | `https://auth.cplugin.net`          |
| `"staging"`  | `https://pre.mywebapi.com`          | `https://pre.auth.cplugin.net`      |
| `"custom"`   | supply `api_base_url=` + `authority=` | —                                 |

Credentials (client ID and secret) are managed through the **CPlugin Toolbox**:

- Staging: <https://pre.toolbox.cplugin.com>
- Production: <https://toolbox.cplugin.com>

## Quick start

```python
import os
from cplugin_webapi_sdk import CPluginWebApiClient, ApiError

# * The client manages OAuth2 token acquisition, caching, and refresh
# * transparently — pass credentials once, call methods on .mt4 / .mt5.
with CPluginWebApiClient(
    env="staging",
    client_id=os.environ["WEBAPI_CLIENT_ID"],
    client_secret=os.environ["WEBAPI_CLIENT_SECRET"],
) as client:
    # Discover configured trade platforms
    platforms = client.list_trade_platforms()
    tp = platforms[0]["id"]

    # server time (mt4 namespace)
    print("server time (mt4):", client.mt4.get_server_time(tp))

    # server time (mt5 namespace)
    print("server time (mt5):", client.mt5.get_server_time(tp))

    # Error handling
    try:
        client.mt4.get_user_record(tp, 99999999)
    except ApiError as e:
        print(f"Error [{e.code}]: {e.description}")
        if e.activity_id:
            print("  Activity ID:", e.activity_id)
```

### Static token (advanced / testing)

```python
from cplugin_webapi_sdk import CPluginWebApiClient

client = CPluginWebApiClient(env="staging", token="your-bearer-token")
```

### Async

An `async with`-compatible counterpart is available as `CPluginWebApiAsyncClient`:

```python
import asyncio, os
from cplugin_webapi_sdk import CPluginWebApiAsyncClient

async def main():
    async with CPluginWebApiAsyncClient(
        env="staging",
        client_id=os.environ["WEBAPI_CLIENT_ID"],
        client_secret=os.environ["WEBAPI_CLIENT_SECRET"],
    ) as client:
        t = await client.mt4.get_server_time(tp)
        print(t)

asyncio.run(main())
```

## Pagination

Paginated endpoints return `(items, meta)`. Use the built-in helpers to iterate:

```python
import os

from cplugin_webapi_sdk import CPluginWebApiClient, paginate_sync, collect_all_sync

with CPluginWebApiClient(
    env="staging",
    client_id=os.environ["WEBAPI_CLIENT_ID"],
    client_secret=os.environ["WEBAPI_CLIENT_SECRET"],
) as client:
    tp = client.list_trade_platforms()[0]["id"]

    # * Iterate page by page — no full dataset loaded into memory at once.
    for page in paginate_sync(
        lambda cur: client.mt4.users_request(tp, cursor=cur, limit=100)
    ):
        for user in page:
            print(user.get("login"), user.get("balance"))

    # * Or collect everything into a single flat list.
    all_trades = collect_all_sync(
        lambda cur: client.mt4.trades_request(tp, cursor=cur, limit=200)
    )
    print(f"Total open trades: {len(all_trades)}")
```

Async equivalents: `paginate_async` / `collect_all_async`.

## Real-time / SignalR

Real-time streaming is available via the optional `signalrcore` extra (install with `pip install -e ".[realtime]"`). The `.realtime` accessor is added in the next release and is currently **EXPERIMENTAL**:

```python
# * pip install -e ".[realtime]"
rt = client.realtime.mt4(trade_platform)   # or client.realtime.mt5(trade_platform)
rt.start()
for tick in rt.stream_ticks("EURUSD"):
    print(tick["symbol"], tick["bid"], tick["ask"])
rt.stop()
```

The `mt4` hubs stream ticks, trades, margin-call events, user updates, and symbol config changes; the `mt5` hubs stream connection status and margin-call updates.

> **Note:** The `realtime` namespace requires `signalrcore` to be installed. The REST surface (`mt4`, `mt5`, `list_trade_platforms`) works without it.

## Regenerate

To regenerate the generated client from a live or local WebAPI spec:

```bash
# Install codegen dependencies
pip install -e ".[codegen]"

# Fetch the OpenAPI spec from a running WebAPI instance
# (set WEBAPI_BASE_URL to the target server)
python scripts/fetch_spec.py

# Regenerate the generated client layer
python scripts/generate_client.py
```

The regenerated output lands in `src/cplugin_webapi_sdk/_generated/`.

## Develop

```bash
# Run the hermetic unit/contract suite (fast, no network)
cd clients/python
python -m pytest -q

# Run the gated staging E2E (requires live credentials)
WEBAPI_E2E=1 \
  WEBAPI_CLIENT_ID=your-id \
  WEBAPI_CLIENT_SECRET=your-secret \
  WEBAPI_TRADE_PLATFORM=your-tp-uuid \
  python -m pytest e2e -q
```

## Layout

```
clients/python/
├── src/cplugin_webapi_sdk/
│   ├── _generated/        # auto-generated endpoint modules and DTOs
│   ├── auth.py            # OAuth2 client credentials + static bearer auth
│   ├── client.py          # CPluginWebApiClient / CPluginWebApiAsyncClient
│   ├── envelope.py        # response envelope Pydantic models
│   ├── environments.py    # env presets (prod / staging / custom)
│   ├── errors.py          # ApiError exception type
│   ├── pagination.py      # paginate_sync/async, collect_all_sync/async
│   └── unwrap.py          # envelope unwrap helpers
├── examples/
│   └── 01_hello.py        # runnable quickstart
├── e2e/
│   └── test_e2e.py        # gated staging E2E test
├── tests/                 # hermetic unit and contract tests
└── scripts/               # fetch_spec.py, generate_client.py
```

---

MetaTrader, MT4, MT5, and MetaQuotes are trademarks or registered trademarks of MetaQuotes Ltd. This project is not affiliated with, endorsed by, or sponsored by MetaQuotes Ltd.
