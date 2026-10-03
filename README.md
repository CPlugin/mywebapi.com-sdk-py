# CPlugin SaaS WebAPI — Python SDK

Python client for the MyWebAPI.com trading platform management API (v2).

The WebAPI works with MetaTrader 4 and MetaTrader 5 servers through their Manager API, so a Python script or back-office service gets REST and WebSocket (SignalR) access to a broker's trade server without the native Windows Manager API libraries.

- Product and sign-up: <https://mywebapi.com>
- API reference: <https://cplugin.com/docs/webapi> · interactive: <https://cloud.mywebapi.com/swagger>
- Pricing: <https://cplugin.com/docs/pricing-and-terms>

## What brokers do with it

Typical back-office tasks, each with the SDK call that performs it. `client` is created as in [Quick start](#quick-start) and `tp` is the trade platform id. Endpoints without a convenience method are called through `raw()` with the generated operation module; `unwrap()` returns the response data.

**List open positions of a group** (MT4 `TradesRequest`, MT5 `PositionByGroup`):

```python
trades, meta = client.mt4.trades_request(tp, group="real-usd")
positions = client.mt5.positions_by_group(tp, "real\\*")
for p in positions:
    print(p["login"], p["symbol"], p["volume"], p["profit"])
```

**Stream trades in real time** (SignalR, `pip install "mywebapi-sdk[signalr]"`; the MT4 hub streams trades, ticks, account and symbol changes and margin calls):

```python
rt = client.realtime.mt4(tp)
rt.start()
rt.stream_trades().subscribe({
    "next": lambda t: print(t),
    "error": lambda err: print("error:", err),
})
```

**Open an account from a CRM** (`UserRecordNew`, then `UserPasswordSet`):

```python
from cplugin_webapi_sdk._generated.api.mt4_v_2_users import post_api_v_2_mt4_trade_platform_user_record_new as user_new
from cplugin_webapi_sdk._generated.api.mt4_v_2_authentication import post_api_v_2_mt4_trade_platform_user_password_set_login as password_set
from cplugin_webapi_sdk._generated.models import MT4UserCreate

body = MT4UserCreate(login=0, group="real-usd", name="John Smith", email="john@example.com", leverage=100)
user = unwrap(client.mt4.raw(user_new, trade_platform=tp, body=body, idempotency_key=crm_request_id))
unwrap(client.mt4.raw(password_set, trade_platform=tp, login=user["login"], body=new_password))
```

**Post a deposit or a withdrawal** (`TradeTransaction` balance operation; a negative amount withdraws):

```python
from cplugin_webapi_sdk._generated.api.mt4_v_2_trades import post_api_v_2_mt4_trade_platform_trade_transaction as trade_tx
from cplugin_webapi_sdk._generated.models import MT4TradeTransaction

deposit = MT4TradeTransaction(trade_transaction_type="BrBalance", trade_command="Balance",
                              order_by=1001, price=500.0, comment="Deposit #8812")
unwrap(client.mt4.raw(trade_tx, trade_platform=tp, body=deposit, idempotency_key=payment_id))
```

**Move an account to another group or change its leverage** (JSON Merge Patch):

```python
client.mt4.patch_user_record(tp, 1001, {"group": "real-vip", "leverage": 200})
```

**Read trade history for reports and statements** (`TradesUserHistory`):

```python
from datetime import datetime, timezone
from cplugin_webapi_sdk._generated.api.mt4_v_2_history import get_api_v_2_mt4_trade_platform_trades_user_history_login as history

closed = unwrap(client.mt4.raw(history, trade_platform=tp, login=1001,
                               from_time=datetime(2026, 9, 1, tzinfo=timezone.utc),
                               to_time=datetime(2026, 10, 1, tzinfo=timezone.utc)))
```

**Watch margin levels** (cached snapshot of every account; the live stream is `rt.stream_margin_call_updates()`):

```python
from cplugin_webapi_sdk._generated.api.mt4_v_2_margins import get_api_v_2_mt4_trade_platform_margins_get as margins_get

margins = unwrap(client.mt4.raw(margins_get, trade_platform=tp))
at_risk = [m for m in margins if 0 < m["level"] < 100]
```

**Change symbol settings, for example swaps** (`SymbolConfig`, JSON Merge Patch):

```python
from cplugin_webapi_sdk._generated.api.mt4_v_2_symbols import patch_api_v_2_mt4_trade_platform_symbol_config_symbol as symbol_patch
from cplugin_webapi_sdk._generated.models import PatchApiV2MT4TradePlatformSymbolConfigSymbolJsonBody as SymbolPatch

unwrap(client.mt4.raw(symbol_patch, trade_platform=tp, symbol="EURUSD",
                      body=SymbolPatch.from_dict({"swapLong": -6.1, "swapShort": 1.2})))
```

`unwrap` is imported from `cplugin_webapi_sdk`. Every other endpoint (trading groups, server configuration, backups, journal, charts, news) has a generated module under `cplugin_webapi_sdk._generated.api`; the full list is in the [API reference](https://cplugin.com/docs/webapi).

## Install

```bash
pip install mywebapi-sdk            # REST client
pip install "mywebapi-sdk[signalr]" # plus the experimental real-time client
```

The package is on [PyPI](https://pypi.org/project/mywebapi-sdk/) and needs Python 3.10 or later. The distribution is `mywebapi-sdk`; the import name is `cplugin_webapi_sdk`. While it is at `0.x`, a minor release may break compatibility, so pin an exact version (`mywebapi-sdk==0.3.0`).

To work on the SDK itself, install from a checkout of this repository:

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

The value is sent as the `X-Request-Timeout` header; a value outside 1–300 raises `ValueError` before anything is sent. The HTTP client waits at least 30 s longer than the deadline you set: the server may add up to 20 s for connecting to the trading platform, and the rest covers the network. The server's deadline starts after it has read the request and taken the idempotency key, so on a very slow network or database the client can still give up first — raise `timeout=` for such an environment. Without `request_timeout` the same margin is added to the operation's default deadline from the API reference (60 s for an operation that documents none). The client-wide HTTP timeout (`timeout=`, default 30 s) is the floor and is never shortened.

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
    client.mt4.patch_user_record(tp, login, {"leverage": 200}, idempotency_key=key)
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

After `OutcomeUnknown`, repeating with the same key returns the real result for at least one hour after the operation finished on the trading platform. (An answer that arrived in time is kept for the key for one minute.) Without an idempotency key, or when in doubt, check the result yourself (orders, positions, balance, the changed record) before repeating an `OutcomeUnknown` request. If the outcome of a timed-out operation cannot be determined, the server keeps the key taken for one hour; after that, check the outcome and use a new key.

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

The regenerated output lands in `src/cplugin_webapi_sdk/_generated/` and is never edited by hand. `generate_client.py` drops the documented default of the `X-Request-Timeout` header before generating, so a generated call sends the header only when a timeout is set, and writes those defaults to `_generated/operation_timeouts.py`, from which the client sizes its HTTP timeout.

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

## Trademarks

MetaTrader, MT4, MT5, and MetaQuotes are trademarks or registered trademarks of MetaQuotes Ltd. This project is not affiliated with, endorsed by, or sponsored by MetaQuotes Ltd.
