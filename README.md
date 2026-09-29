# CPlugin SaaS WebAPI — Python SDK

Python client for the MyWebAPI.com trading platform management API (v2).

## Install

```bash
pip install mywebapi-sdk            # REST client
pip install "mywebapi-sdk[signalr]" # plus the experimental real-time client
```

The distribution is `mywebapi-sdk`; the import name is `cplugin_webapi_sdk`. Until the first release is on PyPI, install from a checkout of this repository:

```bash
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

## Timeouts and retries

Every call addressed to a trade platform has a deadline on the server. When the trading platform does not answer in time, the API still answers — with an error that says whether the operation can have been applied. Default deadlines per operation: trade 5 s, read 10 s, change 15 s, history and reports 30 s, server maintenance 60 s. The API reference lists the default of each operation.

Set your own deadline, in seconds from 1 to 300, for the whole client or for one call:

```python
from cplugin_webapi_sdk import CPluginWebApiClient

client = CPluginWebApiClient(env="staging", client_id=..., client_secret=..., request_timeout=20)

client.mt4.get_server_time(tp, request_timeout=3)  # one call
resp = client.mt4.raw(op_module, trade_platform=tp, request_timeout=120)  # any generated operation
```

The value is sent as the `X-Request-Timeout` header; a value outside 1–300 raises `ValueError` before anything is sent. The HTTP client waits at least 30 s longer than the deadline you set: the server may add up to 20 s for connecting to the trading platform, and the rest covers the network. The server's deadline starts after it has read the request and taken the idempotency key, so on a very slow network or database the client can still give up first — raise `timeout=` for such an environment. The client-wide HTTP timeout (`timeout=`, default 90 s) is never shortened.

When the deadline passes, `ApiError` carries the code and the `X-Request-Outcome` header:

| `e.code` | `e.outcome` | What happened | Retry? |
|---|---|---|---|
| `Timeout` | `timeout` | A read did not finish. Nothing was changed. | Safe |
| `Busy` | `not-started` | Too many requests wait for this trading platform; this one was not sent. | Safe |
| `OutcomeUnknown` | `unknown` | A trade or change did not finish and **may still be applied**. | Check first |
| `OutcomeUnknown` | `in-progress` | A request with the same `Idempotency-Key` is still running; this one was not executed. | Same key |

`e.applied_timeout` is the deadline the server used (`X-Request-Timeout-Applied`), `e.headers` all response headers. `is_safe_to_retry(e)` and `is_outcome_unknown(e)` (also `e.safe_to_retry` / `e.outcome_unknown`) classify an error; `ErrorCode` and `RequestOutcome` hold the values:

```python
import uuid
from cplugin_webapi_sdk import ApiError, is_outcome_unknown, is_safe_to_retry

key = str(uuid.uuid4())  # one key per logical operation, kept across repeats
try:
    client.mt4.patch_user_record(tp, login, idempotency_key=key)
except ApiError as e:
    if is_outcome_unknown(e):
        # * Never repeat blindly — for a trade that means a second trade.
        #   Repeat with the SAME key: while the first request still runs you get
        #   OutcomeUnknown / in-progress again; once it has finished you get its
        #   real result, and it is not executed a second time.
        ...
    elif is_safe_to_retry(e):
        ...  # Timeout or Busy: nothing was applied, repeat when you like
    else:
        raise
```

The finished result is kept for the key for a limited time only — by default one minute, counted from the first request — so repeat promptly. A repeat after the stored result has expired is executed again. Without an idempotency key, or when in doubt, check the result yourself (orders, positions, balance, the changed record) before repeating an `OutcomeUnknown` request. If the outcome of a timed-out operation cannot be determined, the server keeps the key taken for one hour; after that, check the outcome and use a new key.

The SDK does not repeat a request because of a timeout or an error code. `retries=` (default 2) only repeats opening the connection, before any byte of the request is sent. With client-credentials auth, a request answered `401` is sent once more with a fresh token; the server refuses an unauthenticated request before running it. An `httpx` transport error (`httpx.ReadTimeout`, a dropped connection) or an `InvalidResponse` error from a proxy page leaves a trade or change just as unknown as `OutcomeUnknown` does — treat it the same way.

Real-time: hub calls addressed to a trading platform, and connecting to a hub, fail after 60 s; streams are not affected.

## Flag fields

User rights, group permissions and symbol flags are strings with the names of the set bits: `"Enabled, Password"`, `"None"` when no bit is set. A bit the API has no name for arrives as `"Bit<n>"` — keep it when you write the value back. The helpers work on that form:

```python
from cplugin_webapi_sdk import has_flag, with_flag

if not has_flag(user.rights, "Readonly"):
    user.rights = with_flag(user.rights, "Readonly")  # other bits are kept
```

`parse_flags` / `format_flags` convert to and from a list of names. The bit values of every flag type are in the OpenAPI spec (`x-enum-varnames`, `x-enum-values`).

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

Real-time streaming is available via the optional `signalr` extra, which installs the community `signalrcore` library (`pip install "mywebapi-sdk[signalr]"`). The `.realtime` accessor is **EXPERIMENTAL**:

```python
rt = client.realtime.mt4(trade_platform)   # or client.realtime.mt5(trade_platform)
rt.start()
rt.stream_ticks("EURUSD").subscribe({
    "next": lambda tick: print(tick),
    "complete": lambda: print("done"),
    "error": lambda err: print("error:", err),
})
...
rt.stop()
```

The `mt4` hubs stream ticks, trades, margin-call events, user updates, and symbol config changes; the `mt5` hubs stream connection status and margin-call updates.

> **Note:** The `realtime` namespace requires `signalrcore` to be installed. The REST surface (`mt4`, `mt5`, `list_trade_platforms`) works without it.

## Regenerate

The endpoint layer is generated from the vendored OpenAPI spec `src/cplugin_webapi_sdk/spec/v2.json`:

```bash
# Install codegen dependencies
pip install -e ".[codegen]"

# Refresh the vendored spec from staging (main service and x86 sidecar, merged)
python scripts/fetch_spec.py

# Regenerate the generated client layer
python scripts/generate_client.py
```

The regenerated output lands in `src/cplugin_webapi_sdk/_generated/` and is never edited by hand. `generate_client.py` drops the documented default of the `X-Request-Timeout` header before generating, so a generated call sends the header only when a timeout is set.

## Develop

```bash
# Run the hermetic unit/contract suite (fast, no network)
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
.
├── src/cplugin_webapi_sdk/
│   ├── _generated/        # auto-generated endpoint modules and DTOs
│   ├── spec/v2.json       # vendored OpenAPI spec the generated layer is built from
│   ├── auth.py            # OAuth2 client credentials + static bearer auth
│   ├── client.py          # CPluginWebApiClient / CPluginWebApiAsyncClient
│   ├── discovery.py       # OIDC discovery for the token endpoint
│   ├── envelope.py        # response envelope Pydantic models
│   ├── environments.py    # env presets (prod / staging / custom)
│   ├── errors.py          # ApiError exception type
│   ├── flags.py           # flag-field helpers
│   ├── pagination.py      # paginate_sync/async, collect_all_sync/async
│   ├── realtime.py        # experimental SignalR clients
│   ├── timeouts.py        # request timeouts, error codes, retry classification
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
