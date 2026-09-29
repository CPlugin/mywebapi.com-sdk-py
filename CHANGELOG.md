# Changelog

All notable changes to `mywebapi-sdk` (import name `cplugin_webapi_sdk`). The package follows [semver](https://semver.org/); while it is at `0.x`, a minor release may contain breaking changes.

## 0.3.0

First release on PyPI. The version continues the numbering of the JavaScript, .NET and PowerShell SDKs, which ship the same features as 0.3.0. Request timeouts need a server that answers with `X-Request-Outcome`; older servers ignore the new header and keep working.

### Added

- `request_timeout=` (seconds, 1–300) on every namespace method and on `raw()`, and client-wide on `CPluginWebApiClient` / `CPluginWebApiAsyncClient`. Sent as `X-Request-Timeout`; an out-of-range value raises `ValueError` before anything is sent. `raw()` also accepts the generated name `x_request_timeout`.
- The HTTP timeout of every trade-platform call is stretched to at least its server deadline + 30 s — `request_timeout`, else the operation's default from the spec (60 s where none is documented): the server may add up to 20 s for connecting to the trading platform, and the client must not give up before the server says whether the operation was applied. The client-wide `timeout` (still 30 s by default) is the floor and is never shortened.
- `idempotency_key=` on `patch_user_record()` and `raw()`, sent as `Idempotency-Key` — the safe way to recover from `OutcomeUnknown`.
- `ApiError.outcome` (`X-Request-Outcome`: `timeout`, `unknown`, `not-started`, `in-progress`), `ApiError.applied_timeout` (`X-Request-Timeout-Applied`), `ApiError.headers`, and the `outcome_unknown` / `safe_to_retry` properties.
- `is_outcome_unknown(err)`, `is_safe_to_retry(err)`, `ErrorCode` (including the new `Timeout`, `OutcomeUnknown`, `Busy`), `RequestOutcome`, `MIN_REQUEST_TIMEOUT`, `MAX_REQUEST_TIMEOUT`.
- Flag-field helpers `parse_flags`, `format_flags`, `has_flag`, `with_flag`.
- README sections "Timeouts and retries" and "Flag fields".

### Changed

- Regenerated from the current server spec (172 paths). Every guarded operation documents its default timeout in its docstring; the generated functions take `x_request_timeout` and send it only when set.
- Flag fields (user rights, group permissions, symbol, order, position and deal flags) are `str` — the names of the set bits joined by `", "` — instead of single-value enums that rejected every combination. The enum modules `users_rights`, `group_rights`, the `en_*_flags` modules except `en_gateway_account_flags`, `trade_activation_flags`, `trade_modify_flags` and `tick_request_flags` under `_generated.models` are removed.
- The six v2 `PATCH` operations (MT4 `GroupRecord`, `SymbolConfig`, `UserRecord`; MT5 `GroupRecord`, `UserRecord`, `SymbolRecord`) now take a required `body` — a JSON Merge Patch object with only the fields to change — and `ExternalCommandJSON` takes a required `body` (any JSON value). Previously the spec declared no body, so the generated functions could not send one.
- `patch_user_record(trade_platform, login, changes)` takes the changed fields as a mapping (wire names, e.g. `{"leverage": 200}`) and sends them; before, it sent no body at all. An empty or non-mapping `changes` is rejected before sending.
- History calls (30 s server default) and server maintenance (60 s) are no longer cut off by the 30 s client timeout before the server answers.
- `ApiError` takes an optional fourth argument, the response headers; `unwrap()` passes them from any response that has `.headers`.

### Unchanged on purpose

- No request is repeated because of a timeout or an error — not on `OutcomeUnknown`, `in-progress`, `Timeout` or `Busy`, not on a transport error. `retries=` repeats only opening the connection, before any byte of the request is sent; the one re-send after a `401` (fresh token) is unchanged, the server refuses an unauthenticated request before running it.

### Fixed

- README: the real-time extra is `signalr`, not `realtime`; the streaming example used a handler as an iterator.
