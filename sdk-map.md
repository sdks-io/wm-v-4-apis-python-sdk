<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Walmart APIs (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Walmart APIs |
| Root package | `walmart_apis` |
| Distribution name | `wm-v-4-apis-sdk` |
| Requires | Python 3.10 or later |
| API spec version | `v4` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from walmart_apis import WalmartApisClient
from walmart_apis.auth import SellerAuthAuthorizationCodeScope, SellerAuthClientCredentialsScope, WalletAuthScope
from walmart_apis.core import AuthorizationCodeCredentials, BasicAuthCredentials, ClientCredentials


def prompt(url: str) -> str:
    return input(f"Open {url}, then paste the code: ")


client = WalmartApisClient(
    seller_auth_authorization_code=AuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope](
        client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
    ),
    seller_auth_client_credentials=ClientCredentials[SellerAuthClientCredentialsScope](
        client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
    ),
    basic_client_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
    wallet_auth=ClientCredentials[WalletAuthScope](client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with WalmartApisClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run, to_thread

from walmart_apis import AsyncWalmartApisClient
from walmart_apis.auth import SellerAuthAuthorizationCodeScope, SellerAuthClientCredentialsScope, WalletAuthScope
from walmart_apis.core import AsyncAuthorizationCodeCredentials, BasicAuthCredentials, ClientCredentials


async def prompt(url: str) -> str:
    print(f"Open {url}")
    return await to_thread(input, "Paste the code: ")


async def main() -> None:
    client = AsyncWalmartApisClient(
        seller_auth_authorization_code=AsyncAuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope](
            client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
        ),
        seller_auth_client_credentials=ClientCredentials[SellerAuthClientCredentialsScope](
            client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
        ),
        basic_client_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
        wallet_auth=ClientCredentials[WalletAuthScope](client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
        environment="production",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncWalmartApisClient(...) as client:` closes the pool on exit.

`AsyncClient` (`walmart_apis/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `WalmartApisClient` and `AsyncWalmartApisClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.authorization`). Every constructor argument is optional and keyword-only. Sources: `walmart_apis/client.py`, `walmart_apis/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `server_config` | `ServerConfigOrDict \| None` | `ServerConfigOrDict \| None` | `None` |
| `retry_options` | `int \| RetryOptionsOrDict \| None` | `int \| RetryOptionsOrDict \| None` | `None` |
| `logging_options` | `LoggingOptionsOrDict \| None` | `LoggingOptionsOrDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `seller_auth_authorization_code` | `AuthorizationCodeCredentialsOrDict[SellerAuthAuthorizationCodeScope] \| None` | `AsyncAuthorizationCodeCredentialsOrDict[SellerAuthAuthorizationCodeScope] \| None` | `None` |
| `seller_auth_authorization_code_token_source` | `RefreshableTokenSource[AuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope]] \| None` | `AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope]] \| None` | `None` |
| `seller_auth_client_credentials` | `ClientCredentialsOrDict[SellerAuthClientCredentialsScope] \| None` | `ClientCredentialsOrDict[SellerAuthClientCredentialsScope] \| None` | `None` |
| `seller_auth_client_credentials_token_source` | `TokenSource[ClientCredentials[SellerAuthClientCredentialsScope]] \| None` | `AsyncTokenSource[ClientCredentials[SellerAuthClientCredentialsScope]] \| None` | `None` |
| `basic_client_auth` | `BasicAuthCredentialsOrDict \| None` | `BasicAuthCredentialsOrDict \| None` | `None` |
| `wallet_auth` | `ClientCredentialsOrDict[WalletAuthScope] \| None` | `ClientCredentialsOrDict[WalletAuthScope] \| None` | `None` |
| `wallet_auth_token_source` | `TokenSource[ClientCredentials[WalletAuthScope]] \| None` | `AsyncTokenSource[ClientCredentials[WalletAuthScope]] \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `walmart_apis.server` | `Literal` of the Environments table's names |
| `ServerConfigOrDict` | `walmart_apis.server` | keys as the Servers & auth tables read |
| `RetryOptionsOrDict` | `walmart_apis.core` | a retry count, `RetryOptions`, or a dict: `max_retries: int` · `initial_delay: float` · `backoff_factor: float` · `max_delay: float` · `max_jitter: float` · `status_codes_to_retry: frozenset[int]` · `http_methods_to_retry: frozenset[HttpMethod]` |
| `LoggingOptionsOrDict` | `walmart_apis.core` | `LoggingOptions` or a dict: `log_request_headers: bool` · `log_response_headers: bool` · `log_request_body: bool` · `body_size_limit: int` · `redaction_placeholder: str` · `unmask_headers: AbstractSet[str]` · `mask_headers: AbstractSet[str]` · `mask_keys: AbstractSet[str]` |
| `HttpClient` | `walmart_apis.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()`; `send` returns once the head has arrived and never reads the body, and raises `TransportError` (from `core`) when no response arrives — anything else it raises is never retried |
| `AuthorizationCodeCredentialsOrDict` | `walmart_apis.core` | `AuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `SellerAuthAuthorizationCodeScope` | `walmart_apis.auth` | `Enum` of the declared scopes |
| `RefreshableTokenSource` | `walmart_apis.core` | protocol — `fetch(credentials) -> OAuthTokenRefreshable` · `refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AuthorizationCodeCredentials` | `walmart_apis.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AuthorizationCodePrompt` |
| `ClientCredentialsOrDict` | `walmart_apis.core` | `ClientCredentials` or a dict: `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `SellerAuthClientCredentialsScope` | `walmart_apis.auth` | `Enum` of the declared scopes |
| `TokenSource` | `walmart_apis.core` | protocol — `fetch(credentials) -> OAuthToken` |
| `ClientCredentials` | `walmart_apis.core` | `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `BasicAuthCredentialsOrDict` | `walmart_apis.core` | `BasicAuthCredentials` or a dict: `username: str` · `password: str` |
| `WalletAuthScope` | `walmart_apis.auth` | `Enum` of the declared scopes |
| `AsyncHttpClient` | `walmart_apis.core` | protocol — `async send(request: HttpRequest) -> AsyncHttpResponse` · `async aclose()`; the same obligation, awaited |
| `AsyncAuthorizationCodeCredentialsOrDict` | `walmart_apis.core` | `AsyncAuthorizationCodeCredentials` or a dict: `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncRefreshableTokenSource` | `walmart_apis.core` | protocol — `async fetch(credentials) -> OAuthTokenRefreshable` · `async refresh(credentials, refresh_token) -> OAuthTokenRefreshable \| None` |
| `AsyncAuthorizationCodeCredentials` | `walmart_apis.core` | `client_id: str` · `client_secret: str \| None` · `redirect_uri: str` · `scopes: list[Scope] \| None` · `state: str \| None` · `pkce: PkceMethod \| None = "S256"` · `prompt_for_authorization_code: AsyncAuthorizationCodePrompt` |
| `AsyncTokenSource` | `walmart_apis.core` | protocol — `async fetch(credentials) -> OAuthToken` |

### Retries — on by default

`retry_options` left at `None` applies the default `RetryOptions` policy below, so an unconfigured client **retries**: a request whose method is in `http_methods_to_retry` is sent again when it gets a status in `status_codes_to_retry`, or no response at all, and the last outcome reaches you only once its retries are spent. A body that cannot be re-sent byte for byte — a streamed file upload — is never retried. `retry_options=0` (or `{"max_retries": 0}`) turns retrying off; a bare count sets `max_retries` and leaves every other field at its default.

`RetryOptions` fields (source: `walmart_apis/core/retries.py`). Pass only the fields you change; each one left out takes its default:

| Field | Type | Default |
| --- | --- | --- |
| `max_retries` | `int` | `3` |
| `initial_delay` | `float` (seconds) | `1.0` |
| `backoff_factor` | `float` | `2.0` |
| `max_delay` | `float` (seconds) | `60.0` |
| `max_jitter` | `float` (seconds) | `0.5` |
| `status_codes_to_retry` | `frozenset[int]` | `frozenset({408, 429, 500, 502, 503, 504})` |
| `http_methods_to_retry` | `frozenset[HttpMethod]` | `frozenset({"GET", "HEAD", "PUT", "OPTIONS"})` |

The wait before retry *n* is `initial_delay × backoff_factor^(n−1)` plus up to `max_jitter` of random delay, the sum capped at `max_delay`; a `Retry-After` header replaces it, trimmed to `max_delay`.

A single call overrides two of these through `request_options` (`walmart_apis/core/request_options.py`): `max_retries` and `status_codes_to_retry`, each merged over the client's policy field by field — `request_options={"max_retries": 0}` turns retrying off for that one call and leaves every other call alone.

### Logging — off by default

Every HTTP exchange is written through the standard `logging` module under the `walmart_apis` logger, and the SDK configures nothing itself. Set that logger's level to turn it on: INFO writes the request line and a 2xx response line, WARNING a non-2xx response line and each retry, ERROR a call that ends in an exception, and DEBUG the header dumps and the request body that the flags below turn on. Or set `WALMART_APIS_LOG=info|debug` before the process starts: it sets the level, turns the three flags on for `debug`, and adds a stderr handler only where nothing listens.

`LoggingOptions` fields (source: `walmart_apis/core/logging.py`). Pass only the fields you change; each one left out takes its default, and a name set you pass replaces its default:

| Field | Type | Default |
| --- | --- | --- |
| `log_request_headers` | `bool` | `False` |
| `log_response_headers` | `bool` | `False` |
| `log_request_body` | `bool` | `False` |
| `body_size_limit` | `int` (bytes) | `32768` |
| `redaction_placeholder` | `str` | `"REDACTED"` |
| `unmask_headers` | `AbstractSet[str]` | `frozenset()` |
| `mask_headers` | `AbstractSet[str]` | `frozenset()` |
| `mask_keys` | `AbstractSet[str]` | `frozenset({"sig", "signature", "access_token", "apikey", "api_key", "client_secret", "password", "refresh_token", "code", "assertion", "client_assertion"})` |

A single call is quietened through `request_options` (`walmart_apis/core/request_options.py`): `log_level`, a `logging` level constant, is a floor below which that call's records are not written; it never turns a dump or the body on. A header value prints `REDACTED` unless its name is on the runtime's safe list, a query value unless its key is a paging name, and a form field whose key is in `mask_keys` always; a JSON body prints as sent; a response body is never logged.

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.status_code` and `.headers`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `walmart_apis/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`walmart_apis/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any`.

Core runtime types (`walmart_apis/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `walmart_apis/errors/` or `RawError` | `error: E` · `status_code: int` · `headers: Mapping[str, str]` | `walmart_apis/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `status_code: int` · `headers: Mapping[str, str]` (both on either) | `walmart_apis/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` | `walmart_apis/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
try:
    response = client.authorization.create_token(GrantType.CLIENT_CREDENTIALS)
except ApiError as e:
    # Case A — typed error: e.error is CreateTokenErrorBody
    if isinstance(e.error, OAuthErrorModel):
        # Handle 400, 401, 429, 500, 502
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **184 operations**, **184 are Case A (typed)** and **0 are Case B (raw)**.

---

## Operations — by controller (31 pages, 184 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every *generated* type it names, with the module that declares it. A runtime type — a file alias, a date/time or byte converter — is not listed there.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout, extra headers, `max_retries`, `status_codes_to_retry` or `log_level`; every signature ends with it | here (`walmart_apis/core/request_options.py`), Retries, Logging |
| **Each operation names its own server** — this SDK declares several, so every block carries a **Server** bullet with the server's key in `server_config=` | its block |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Class | Ops | Page |
| --- | --- | --- | --- |
| `client.authorization` | `Authorization` / `AsyncAuthorization` | 1 | [map/operations/authorization.md](map/operations/authorization.md) |
| `client.catalog` | `Catalog` / `AsyncCatalog` | 2 | [map/operations/catalog.md](map/operations/catalog.md) |
| `client.data_kiosk` | `DataKiosk` / `AsyncDataKiosk` | 5 | [map/operations/data_kiosk.md](map/operations/data_kiosk.md) |
| `client.disputes` | `Disputes` / `AsyncDisputes` | 1 | [map/operations/disputes.md](map/operations/disputes.md) |
| `client.feeds` | `Feeds` / `AsyncFeeds` | 5 | [map/operations/feeds.md](map/operations/feeds.md) |
| `client.final_payout` | `FinalPayout` / `AsyncFinalPayout` | 2 | [map/operations/final_payout.md](map/operations/final_payout.md) |
| `client.finances` | `Finances` / `AsyncFinances` | 4 | [map/operations/finances.md](map/operations/finances.md) |
| `client.fulfillment_outbound` | `FulfillmentOutbound` / `AsyncFulfillmentOutbound` | 7 | [map/operations/fulfillment_outbound.md](map/operations/fulfillment_outbound.md) |
| `client.inventory` | `Inventory` / `AsyncInventory` | 4 | [map/operations/inventory.md](map/operations/inventory.md) |
| `client.listings_items` | `ListingsItems` / `AsyncListingsItems` | 5 | [map/operations/listings_items.md](map/operations/listings_items.md) |
| `client.listings_restrictions` | `ListingsRestrictions` / `AsyncListingsRestrictions` | 1 | [map/operations/listings_restrictions.md](map/operations/listings_restrictions.md) |
| `client.merchant_fulfillment` | `MerchantFulfillment` / `AsyncMerchantFulfillment` | 5 | [map/operations/merchant_fulfillment.md](map/operations/merchant_fulfillment.md) |
| `client.orders` | `Orders` / `AsyncOrders` | 14 | [map/operations/orders.md](map/operations/orders.md) |
| `client.payouts` | `Payouts` / `AsyncPayouts` | 5 | [map/operations/payouts.md](map/operations/payouts.md) |
| `client.product_type_definitions` | `ProductTypeDefinitions` / `AsyncProductTypeDefinitions` | 3 | [map/operations/product_type_definitions.md](map/operations/product_type_definitions.md) |
| `client.reconciliation` | `Reconciliation` / `AsyncReconciliation` | 3 | [map/operations/reconciliation.md](map/operations/reconciliation.md) |
| `client.report_schedules` | `ReportSchedules` / `AsyncReportSchedules` | 4 | [map/operations/report_schedules.md](map/operations/report_schedules.md) |
| `client.reports` | `Reports` / `AsyncReports` | 7 | [map/operations/reports.md](map/operations/reports.md) |
| `client.sellers` | `Sellers` / `AsyncSellers` | 2 | [map/operations/sellers.md](map/operations/sellers.md) |
| `client.settlement` | `Settlement` / `AsyncSettlement` | 3 | [map/operations/settlement.md](map/operations/settlement.md) |
| `client.supply_source_api` | `SupplySourceApi` / `AsyncSupplySourceApi` | 4 | [map/operations/supply_source_api.md](map/operations/supply_source_api.md) |
| `client.uploads` | `Uploads` / `AsyncUploads` | 1 | [map/operations/uploads.md](map/operations/uploads.md) |
| `client.wfs_inventory` | `WfsInventory` / `AsyncWfsInventory` | 1 | [map/operations/wfs_inventory.md](map/operations/wfs_inventory.md) |
| `client.messaging` | `Messaging` / `AsyncMessaging` | 11 | [map/operations/messaging.md](map/operations/messaging.md) |
| `client.notifications` | `Notifications` / `AsyncNotifications` | 9 | [map/operations/notifications.md](map/operations/notifications.md) |
| `client.product_fees` | `ProductFees` / `AsyncProductFees` | 3 | [map/operations/product_fees.md](map/operations/product_fees.md) |
| `client.product_pricing` | `ProductPricing` / `AsyncProductPricing` | 8 | [map/operations/product_pricing.md](map/operations/product_pricing.md) |
| `client.sales` | `Sales` / `AsyncSales` | 1 | [map/operations/sales.md](map/operations/sales.md) |
| `client.shipping` | `Shipping` / `AsyncShipping` | 9 | [map/operations/shipping.md](map/operations/shipping.md) |
| `client.solicitations` | `Solicitations` / `AsyncSolicitations` | 2 | [map/operations/solicitations.md](map/operations/solicitations.md) |
| `client.wfs_inbound` | `WfsInbound` / `AsyncWfsInbound` | 52 | [map/operations/wfs_inbound.md](map/operations/wfs_inbound.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `walmart_apis/models/` declares one type plus its input companion, and every module under `walmart_apis/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`AccessPoint` ↔ `access_point.py`; an error alias drops its `Body` suffix: `CreateWarrantyErrorBody` ↔ `create_warranty_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 474 | `walmart_apis/models/` |
| Enums (`Enum` over `str` / `int`) — Python member names + wire values | 138 | `walmart_apis/models/enums/` |
| Error aliases (one per Case A operation) | 184 | `walmart_apis/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`access_point_id` ↔ `"accessPointId"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model and enum also has an **input companion**, exported beside it from the same package (`AccessPoint` ↔ `AccessPointDict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str` / `int`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AccountStatus` ↔ `AccountStatusOrStr`) and additionally accepts a wire value this SDK version does not know.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `walmart_apis` |
| Operation controllers | `walmart_apis.apis` |
| Models | `walmart_apis.models` |
| Enums | `walmart_apis.models.enums` |
| Error aliases | `walmart_apis.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `walmart_apis.core` |

---

## Servers & auth

**OAuth2 (authorization code).** Pass `seller_auth_authorization_code` your client id, redirect URI and authorization code; authorization is at `/authorize` and tokens come from `/v4/auth/token`, both on the `default` server. Scopes are the `SellerAuthAuthorizationCodeScope` alias.

**OAuth2 (client credentials).** Pass `seller_auth_client_credentials` your client id and secret; tokens come from `/v4/auth/token` on the `default` server. Scopes are the `SellerAuthClientCredentialsScope` alias.

**Basic auth.** Pass `basic_client_auth={"username": …, "password": …}`, or a `BasicAuthCredentials`.

**OAuth2 (client credentials).** Pass `wallet_auth` your client id and secret; tokens come from `/token` on the `access_token_server` server. Scopes are the `WalletAuthScope` alias.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**Environments.** `environment=` selects the target environment (`walmart_apis/server/environment.py`):

| Environment | Hosting |
| --- | --- |
| `"production"` *(default)* | Production |
| `"environment2"` | Sandbox |

**4 servers.** Base-URL templates and override points (`walmart_apis/server/server_config.py`):

| Server | `"production"` base URL | `"environment2"` base URL | Override point |
| --- | --- | --- | --- |
| `default` | `https://marketplace.walmart.com/seller` | `https://sandbox.marketplace.walmart.com/seller` | `{"default": {"production": {"base_url": …}}}` (and the other environments) |
| `auth_server` | `https://login.account.wal-mart.com` | `https://login.account.wal-mart.com` | `{"auth_server": {"production": {"base_url": …}}}` (and the other environments) |
| `default_catalog_items` | `https://marketplace.walmart.com/seller/v1` | `https://sandbox.marketplace.walmart.com/seller/v1` | `{"default_catalog_items": {"production": {"base_url": …}}}` (and the other environments) |
| `access_token_server` | `https://marketplace.walmart.com/seller/auth/v4` | `https://marketplace.walmart.com/seller/auth/v4` | `{"access_token_server": {"production": {"base_url": …}}}` (and the other environments) |

Pick a row with `environment=`, and override any of these by passing `server_config=` a dict nested exactly as the columns above read — `{"default": {"production": {"base_url": …}}}` — with each row's variables sitting beside its `base_url`.

