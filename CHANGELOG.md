# Changelog

All notable changes to `mywebapi-sdk` (import name `cplugin_webapi_sdk`). The package follows [semver](https://semver.org/); while it is at `0.x`, a minor release may contain breaking changes.

## 0.6.0

Regenerated from the WebAPI v2 specification of 24.11.2026: 453 paths and 456 operations, 452 schemas (438 model modules). The vendored document is the union of the main service and the MT4 x86 sidecar, as before. Contains no new operations. Versions move together with the JavaScript, .NET and PowerShell SDKs.

### Added

- `MT5ConSubscription.price_cost` — the real cost of a subscription, the amount the client is actually charged, next to the list `price` and `price_pro`. Sent as `priceCost`.
- `MT5SubscriptionHistory.time` — when the action happened, in seconds since 1970-01-01, next to `amount`. Sent as `time`.

### Changed

- The `limit` parameter of `TickHistoryRequestRaw` describes its cap as applying within the window; `0` still returns the whole window.
- `servers` of the vendored document list the sandbox and production hosts in that order; the development host of the previous document is gone. No generated code reads it.
- `tests/test_generated_smoke.py` covers `price_cost` and the history `time`.

## 0.5.1

Regenerated from the WebAPI v2 specification of 23.11.2026: 453 paths and 456 operations, 452 schemas. The vendored document is the union of the main service and the MT4 x86 sidecar, as before. Contains no new operations. Versions move together with the JavaScript, .NET and PowerShell SDKs.

### Added

- Tick statistics (`MT5MarketTickStat`) carry the option pricing fields of the trade server: `price_greeks_delta`, `price_greeks_theta`, `price_greeks_gamma`, `price_greeks_vega`, `price_greeks_rho`, `price_greeks_omega` and `price_sensitivity`, sent as `priceGreeksDelta`, `priceGreeksTheta`, `priceGreeksGamma`, `priceGreeksVega`, `priceGreeksRho`, `priceGreeksOmega` and `priceSensitivity`.
- Named subscription enumerations: `MT5SubscriptionType`, `MT5SubscriptionPeriod`, `MT5SubscriptionStatus`, `MT5SubscriptionFreePeriod`, `MT5SubscriptionControlMode`, `MT5SubscriptionAction`, `MT5SubscriptionSymbolLevel` and `MT5SubscriptionTickHistory`. A configuration or a subscription now reads `cfg.type_ is MT5SubscriptionType.FOLDER`, `sub.period_mode is MT5SubscriptionPeriod.MONTHLY` and so on; every value is the name the API sends (`"Folder"`, `"Monthly"`, `"Cancel"`).

### Changed

- Subscription and subscription-history fields that used to be integer codes are now these enumerations: `MT5ConSubscription.type_`, `control_mode`, `period_mode`, `period_free_mode`; `MT5Subscription.status`; `MT5SubscriptionHistory.action`; `MT5ConSubscriptionSymbol.level`, `tick_history`. Reading code that compared them to numbers needs the enumeration members. A numeric value still decodes unchanged, so a mixed document does not fail.
- `flags` of a subscription configuration (`MT5ConSubscription.flags`) and of a subscription (`MT5Subscription.flags`) is a string of the names of the set bits (`"FreePeriod"`, `"None"`) instead of a bit mask. `parse_flags` / `format_flags` work on it like on the other flag fields.
- `MT5News.time` and `MT5NewsSendRequest` publication time are the wall-clock time of the trade server, not UTC: the value carries no zone, so a naive `datetime` is returned. Convert it with the server offset of the platform before showing it to a user.
- Default read timeouts follow the specification: the client and group read operations (`OnlineGet`, `OnlineRequest`, `ClientRequest*`, `CommentRequest*`, `DocumentRequest*`, `NewsRequest` and the other communication reads) now document 30 s instead of 10 s. Passing `request_timeout=` still overrides them.
- `tests/test_generated_smoke.py` covers the named subscription codes, the subscription flags string, the option greek fields and the zone-less news time.

## 0.5.0

Regenerated from the WebAPI v2 specification of 23.11.2026 that carries the full Manager API surface: 453 paths and 456 operations (was 223 paths and 224 operations), 442 schemas. The vendored document is the union of the main service and the MT4 x86 sidecar, as before. Versions move together with the JavaScript, .NET and PowerShell SDKs.

### Added

- **Generated layer covers every new v2 group** — `MT4 v2 :: Dealer`; `MT5 v2 :: Clients`, `Communications`, `Configuration`, `Market Data`, `Market Insight`, `Reports`, `Subscriptions`, `Trade Operations`, `Trading` and the extended `Users`. Each operation is its own module and reaches the SDK without a hand-written wrapper.
- **MT4 dealer facade**: `mt4.summary_get_all()`, `summary_get(symbol)`, `summary_currency()`, `exposure_get()`, `exposure_value(currency)`, `trade_calc_profit(body)`.
- **MT5 reports facade**: `mt5.summary_get_all()`, `summary_get(symbol)`, `summary_currency()`, `exposure_get_all()`, `exposure_get(symbol)`, `daily_request(login)`, `daily_request_light(login)`.
- **MT5 subscriptions facade**: `subscription_cfg_request(name)`, `subscription_cfg_get(name)`, `subscription_request(login)`, `subscription_history_request(login)`.
- **MT5 users facade**: `user_cert_get(login)`, `user_account_get(login)`, `user_get_by_logins(logins)`, `user_group(login)`, `user_logins(group)`, `user_cert_confirm(login)`.
- **MT5 trading and dealer facade**: `request_get_all(from_, count)`, `request_get(id)`, `trade_profit(body)`, `order_get(ticket)`, `order_add(body)`, `order_cancel(ticket)`, `deal_request(login, from_, to)`, `history_request(login, from_, to)`, plus `time_get()`.
- **MT5 market data and insight facade**: `tick_last(symbol)`, `tick_stat(symbol)`, `book_get(symbol)`, `online_request(from_, count)`.
- **MT5 configuration, communications and clients facade**: `symbol_request(symbol, group)`, `symbol_exist(symbol, group)`, `leverage_get(name)`, `mail_request()`, `news_request()`, `setting_get(section, key)`, `mail_send(body)`, `client_user_request(client_id)`, `document_request(document_id)`, `client_update(body)`.
- Request-body methods accept a plain mapping with wire (camelCase) names as well as a ready generated model; the mapping is turned into the generated request model.
- `tests/test_v2_operations.py` — route, verb, optional-filter, body-mapping and async-mirror tests for the new groups.

### Changed

- The generated tree is rebuilt from the merged document: 456 operation modules and 430 model modules. `operation_timeouts.py` now maps 456 operations to their server default timeout.
- No existing facade method changed its name, signature or behaviour; the previous release's methods keep working.

## 0.4.0

Regenerated from the WebAPI v2 specification of 23.11.2026 (223 paths, 293 schemas). The v2 routes now carry the names of v1 and the duplicates are gone, and the MT5 area covers the manager surface v1 had. Versions move together with the JavaScript, .NET and PowerShell SDKs.

### Added

- MT5 client operations and models: `GET ClientRequest/{clientId}`, `POST ClientAdd`, `POST ClientDelete/{clientId}`, `POST ClientUserAdd/{clientId}/{login}`; `MT5Client`, `MT5ClientApiResponse`, `ClientTypes`, `ClientStatuses`, `ClientOrigins`.
- MT5 account operations: `GET UserRequest/{login}`, `GET UserAccountRequest/{login}`, `GET UserAccountGet/{login}`, `GET UserGetByGroup/{mask}`, `GET UserGetByLogins`, `POST UserAdd`, `POST UserUpdate`, `POST UserDelete/{login}`, `POST UserPasswordCheck/{login}/{type}`, `POST UserPasswordChange/{login}/{type}`; `MT5UserAddRequest`, `MT5UserAddResult`, `MT5UserUpdate`, `MT5Account`, `MT5UserListApiResponse`.
- MT5 deal and trade-history operations: `GET DealRequest/{login}`, `GET DealRequestByGroup/{mask}`, `GET DealRequestByGroupSymbol/{mask}/{symbol}`, `GET DealRequestByLogins`, `GET DealRequestByTicket/{ticket}`, `GET` and `POST DealRequestByTickets`, `POST DealDeleteBatch`, `POST DealUpdate`, `POST DealerBalance`, `POST DealerBalanceRaw`, `POST DealerSend`; `GET HistoryRequest/{login}`, `GET HistoryRequestByGroup/{mask}`, `GET` and `POST HistoryRequestByTickets`; `MT5DealApiResponse`, `MT5Request`, `MT5Result`, `DealerBalanceRequest`, `EnDealAction`.
- MT5 order operations: `GET OrderGet/{ticket}`, `GET OrderGetByGroup/{mask}`, `GET OrderGetByLogins`, `GET OrderGetBySymbol/{mask}/{symbol}`, `GET OrderGetByTickets`, `GET OrderRequestByGroup/{mask}`, `GET OrderRequestByGroupSymbol/{mask}/{symbol}`, `POST OrderRequestByTickets`, `POST OrderDeleteBatch`; `MT5OrderApiResponse`.
- MT5 position operations: `GET PositionGet/{login}`, `GET PositionGetByLogins`, `GET PositionGetBySymbol/{mask}/{symbol}`, `GET PositionGetByTickets`, `POST PositionDeleteBatch`.
- MT5 group and symbol reads: `GET GroupRequest/{group}`, `GET GroupRequestArray/{mask}`, `GET SymbolRequestArray/{mask}`, `POST SymbolUpdate/{symbol}`; `MT5ConGroupListApiResponse`, `MT5SymbolListApiResponse`, `MT5SymbolUpdate`.
- MT4 operations: `GET CfgRequestGroup`, `GET CfgRequestSymbolGroup`, `GET ManagerCommonEx`, `GET SymbolsGetAll`, `GET SymbolsGetAll/{symbol}`, `GET UsersGet`, `POST CfgUpdateGroup`, `POST UserRecordUpdate`; body models `MT4GroupUpdate` and `MT4UserUpdate`, and `MT4CommonShort`.
- Generated models for the MT5 request enums: `DemoAccountType`, `EducationLevel`, `Employment`, `EmploymentIndustry`, `Genders`, `KYCStatuses`, `LiveUpdateMode`, `MonthlyStatementMode`, `PreferredCommunication`, `RolloverMode`, `ServerStopReason`, `SoActivation`, `StatementMode`.
- Real-time: the connection-status callback is now per platform — `on_mt4_connection_status()` binds `OnMT4ConnectionStatus` and `on_mt5_connection_status()` binds `OnMT5ConnectionStatus`, the names the v2 hubs actually broadcast.

### Changed

- **Breaking — MT5 routes renamed to their v1 names:** `ServerTime` → `TimeServer`, `PositionByGroup/{mask}` → `PositionRequestByGroup/{mask}`, `OrderByGroup/{mask}` → `OrderGetByGroup/{mask}`, `DealByGroup/{mask}` → `DealRequestByGroup/{mask}`. `GroupGet` is again offered next to `GroupRequest`. The facade methods (`mt5.get_server_time()`, `mt5.positions_by_group()`) keep their names; only code that imports a generated operation module by its old name is affected.
- **Breaking — duplicate routes removed:** MT4 `GET SymbolsGroupsGet`, `POST GroupRecordUpdate/{group}`, `POST UserRecordUpdate/{login}`; use `SymbolsGetAll`, `PATCH GroupRecord` and `PATCH UserRecord` or `POST UserRecordUpdate`. The MT4 module `get_api_v_2_mt4_trade_platform_symbols_groups_get` no longer exists.
- **Breaking — the real-time callback `on_connection_status()` is gone**; register `on_mt4_connection_status()` or `on_mt5_connection_status()` on the platform client instead.
- Update operations accept only the fields the caller sends; omitted fields keep their server value, and an empty body is refused. `CfgUpdateCommon` additionally accepts a plain `application/json` body next to `application/json-patch+json`.
- Trade-platform permissions are checked by the effect of the operation: `AdmBalanceFix`, `SymbolAdd`, `SymbolHide` and `SymbolsRefresh` require `Update` rather than `Request`, and `TradeTransaction` requires `Update` rather than `Create`; MT5 `DealRequestByTicket` is checked against the order permission. The behaviour belongs to the server and applies to every SDK version — check the rights of the accounts your script runs under.
- The vendored `spec/v2.json` is the specification of 23.11.2026. `UsersRights` is replaced by `MT5UserRights`, a flag field that stays `str` — the names of the set bits joined by `, `.

## 0.3.4

MT5 chart and tick history, ticks on the MT5 real-time hub, and batched ticks on both real-time hubs. Versions move together with the JavaScript, .NET and PowerShell SDKs.

### Added

- Generated MT5 history calls, from the new tag `MT5 v2 :: History Data`:
  - `GET /api/v2/MT5/{tradePlatform}/ChartRequest/{symbol}` — OHLC bars of a symbol for a time window, ordered by time ascending. `period` is one of `M1`, `M5`, `M15`, `M30`, `H1`, `H4`, `D1`, `W1`, `MN1` (default `M1`); `from` and `to` are trading times of the trade server, both optional — the beginning of the history and the current server time respectively; `limit` caps the number of bars, `0` (the default) returns the whole window. The answer is `MT5ChartBarPage` — `bars`, `total`, `truncated`.
  - `GET /api/v2/MT5/{tradePlatform}/TicksHistory/{symbol}` — historical ticks of a symbol for a time window, filtered by the symbol's tick filters, ordered by time ascending. `from` and `to` are optional in the same way, `limit` works as it does for bars. The answer is `MT5TickPage` — `ticks`, `total`, `truncated`; there is no pagination, so read further by moving `from` past the last returned tick.
  - Models `MT5ChartBarV2`, `MT5ChartBarPage`, `MT5ChartBarPageApiResponse`, `MT5ChartPeriod`, `MT5TickV2`, `MT5TickPage`, `MT5TickPageApiResponse`.
- MT5 real-time (`/hubs/mt5/v2`): `on_tick()` (`OnTick` events), `subscribe_to_ticks(symbol)` / `unsubscribe_from_ticks(symbol)` and `stream_ticks(symbol=None)`, where the symbol of the stream is optional — omit it to receive every symbol subscribed on the connection. Each tick carries `symbol`, `bid`, `ask`, `last`, `lastTime`, `volumeExt` and `flags`.
- Batched ticks on both real-time hubs: `on_ticks_batch()` (`OnTicksBatch` events), `subscribe_to_ticks_batch(symbol, interval_ms=200, max_batch_size=200)` and `unsubscribe_from_ticks_batch(symbol)`. The payload is `{"symbol": …, "ticks": [...]}`. `interval_ms` is 20–60000 and `max_batch_size` is 1–10000; out-of-range values are refused by the server. A symbol subscribed to batches receives no per-tick `OnTick` events until it is subscribed the plain way again, and the subscriptions last until the connection closes.

### Changed

- The vendored `spec/v2.json` is the specification of 30.10.2026 (174 paths): the two MT5 history operations above are added to the previous document, and every operation it already had is unchanged.
- `scripts/fetch_spec.py` reads a local main-service document when `WEBAPI_SPEC_FILE` is set, without a network call; in that mode the previous vendored file supplies the MT4 x86 sidecar routes, which the x64 document does not contain. The merge keeps the document-level keys of that previous union as well.

## 0.3.3

Regenerated from the WebAPI v2 specification of 05.10.2026; no change to the API surface or to the generated models' fields and types.

### Changed

- The docstrings of the generated operations and models, and the vendored `spec/v2.json` header they come from, no longer name the server's internal library; the texts speak about the trading platform itself. Documentation only; no change in behaviour.

## 0.3.1

Regenerated from the WebAPI v2 specification of 03.10.2026; no change to the API surface or to the generated models' fields and types.

### Changed

- The MT4 enum fields of `MT4TradeTransaction` (`trade_transaction_type`, `trade_command`, `trade_request_flags`, used by the TradeTransaction and TradeCheckStops operations) and `MT4UsersGroupOp.command` now document the values the server accepts; the old docstrings listed names such as `ModifyTrade` and `BalanceAdd` that the server does not know. Values are case-insensitive, and the numeric value is accepted too.
- An unknown value in `trade_transaction_type`, `trade_command` or `MT4UsersGroupOp.command` is now refused by the server with `ApiError` code `Validation`; until 03.10.2026 it was silently replaced by the enum's default. The behaviour belongs to the server, so it applies to every SDK version; check code that builds these values from user input.
- The vendored `spec/v2.json` is the specification of 03.10.2026.

### Documentation

- README: "What brokers do with it" — eight common back-office tasks (open positions of a group, trade stream, account creation, deposits and withdrawals, group and leverage changes, trade history, margin levels, symbol swaps), each with the SDK call that performs it; links to the product site, API reference and pricing; the trademark notice is now a section of its own.
- Package metadata: the PyPI homepage is now <https://mywebapi.com>, with documentation, API reference and pricing links; the description, keywords and classifiers name the compatible trading platforms (MetaTrader 4 and MetaTrader 5) and the financial audience.
- The `raw()` docstring example imported a generated module that does not exist; it now uses `TradesUserHistory`.

## 0.3.0

First release on PyPI. The version continues the numbering of the JavaScript, .NET and PowerShell SDKs, which ship the same features as 0.3.0. Request timeouts need a server that answers with `X-Request-Outcome`; older servers ignore the new header and keep working.

### Added

- `request_timeout=` (seconds, 1–300) on every namespace method and on `raw()`, and client-wide on `CPluginWebApiClient` / `CPluginWebApiAsyncClient`. Sent as `X-Request-Timeout`; an out-of-range value raises `ValueError` before anything is sent. `raw()` also accepts the generated name `x_request_timeout`.
- The HTTP timeout of every trade-platform call is stretched to at least its server deadline + 30 s — `request_timeout`, else the operation's default from the spec (60 s for an operation that documents none): the server may add up to 20 s for connecting to the trading platform, and the client must not give up before the server says whether the operation was applied. The client-wide `timeout` (still 30 s by default) is the floor and is never shortened.
- `idempotency_key=` on `patch_user_record()` and `raw()`, sent as `Idempotency-Key` — the safe way to recover from `OutcomeUnknown`.
- `ApiError.outcome` (`X-Request-Outcome`: `timeout`, `unknown`, `not-started`, `in-progress`), `ApiError.applied_timeout` (`X-Request-Timeout-Applied`), `ApiError.headers`, and the `outcome_unknown` / `safe_to_retry` properties.
- `is_outcome_unknown(err)`, `is_safe_to_retry(err)`, `ErrorCode` (including the new `Timeout`, `OutcomeUnknown`, `Busy`), `RequestOutcome`, `MIN_REQUEST_TIMEOUT`, `MAX_REQUEST_TIMEOUT`.
- Flag-field helpers `parse_flags`, `format_flags`, `has_flag`, `with_flag`.
- README sections "Timeouts and retries" and "Flag fields".

### Changed

- Regenerated from the current server spec (172 paths). Every trade-platform operation, the MT4 x86 sidecar ones included (plugins, mails and news, batch snapshots and sync reads, `ExternalCommandBinary`), documents its default timeout in its docstring; the generated functions take `x_request_timeout` and send it only when set.
- Flag fields (user rights, group permissions, symbol, order, position and deal flags) are `str` — the names of the set bits joined by `", "` — instead of single-value enums that rejected every combination. The enum modules `users_rights`, `group_rights`, the `en_*_flags` modules except `en_gateway_account_flags`, `trade_activation_flags`, `trade_modify_flags` and `tick_request_flags` under `_generated.models` are removed.
- The six v2 `PATCH` operations (MT4 `GroupRecord`, `SymbolConfig`, `UserRecord`; MT5 `GroupRecord`, `UserRecord`, `SymbolRecord`) now take a required `body` — a JSON Merge Patch object with only the fields to change — and `ExternalCommandJSON` takes a required `body` (any JSON value). Previously the spec declared no body, so the generated functions could not send one.
- `patch_user_record(trade_platform, login, changes)` takes the changed fields as a mapping (wire names, e.g. `{"leverage": 200}`) and sends them; before, it sent no body at all. An empty or non-mapping `changes` is rejected before sending.
- History calls (30 s server default) and server maintenance (60 s) are no longer cut off by the 30 s client timeout before the server answers.
- `ApiError` takes an optional fourth argument, the response headers; `unwrap()` passes them from any response that has `.headers`.

### Unchanged on purpose

- No request is repeated because of a timeout or an error — not on `OutcomeUnknown`, `in-progress`, `Timeout` or `Busy`, not on a transport error. `retries=` repeats only opening the connection, before any byte of the request is sent; the one re-send after a `401` (fresh token) is unchanged, the server refuses an unauthenticated request before running it.

### Fixed

- README: the real-time extra is `signalr`, not `realtime`; the streaming example used a handler as an iterator.
