# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [WalmartApisClient](walmart_apis/client.py)

## Authorization

> Source: [Authorization](walmart_apis/apis/authorization.py)

<details>
<summary><code>def authorize(response_type: ResponseType1OrStr, client_id: str, redirect_uri: str, scope: str, state: str, code_challenge: str, code_challenge_method: CodeChallengeMethodOrStr, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Browser endpoint for the authorization-code grant (RFC 6749 §3.1). The
Solution Provider redirects the seller here; the seller authenticates and
consents at Walmart IAM, and the response redirects to `redirect_uri` with a
single-use `code`.

- **PKCE required** — `code_challenge` + `code_challenge_method=S256`
  (RFC 7636). `plain` is not accepted.
- **Exact** `redirect_uri` match against a value registered for the client.
- `state` required; echoed back verbatim (CSRF).
- The success and error redirects (performed by IAM) carry `iss` (RFC 9207);
  clients MUST validate it.

**Error handling.** For a valid request, this endpoint `302`-redirects to the
Walmart IAM consent URL; IAM then drives consent and performs the RFC 6749
§4.1.2.1 redirect back to the client's `redirect_uri` (success or error),
because IAM is the party that can verify the `redirect_uri` is registered.
For request-level errors that `the Authorization API` itself detects
(missing/invalid `client_id`/`redirect_uri`, `response_type` != `code`,
`code_challenge_method` != `S256`), it returns a JSON `400` (`AuthorizeError`).
It deliberately does **not** redirect these errors to the supplied
`redirect_uri`: the proxy has no client registry, so self-redirecting to an
unverified URI would be an open redirect.

> **Upstream status (, pending):** `iss` emission, exact-redirect
> enforcement, and server-side rejection of `code_challenge_method=plain` are
> IAM / app-store responsibilities not yet fully in place. the Authorization API
> enforces the request-side invariants it can and redirects valid requests to
> IAM; the full guarantee lands when those upstream changes ship.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.authorization.authorize(
        ResponseType1.CODE,
        "some example string",
        "https://example.com",
        "some example string",
        "some example string",
        "some example string",
        CodeChallengeMethod.S256,
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AuthorizeErrorBody
```

**Async**

```python
try:
    await async_client.authorization.authorize(
        ResponseType1.CODE,
        "some example string",
        "https://example.com",
        "some example string",
        "some example string",
        "some example string",
        CodeChallengeMethod.S256,
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AuthorizeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>response_type</code> | <code>[ResponseType1OrStr](walmart_apis/models/enums/response_type1.py)</code> | Must be `code`. |
| <code>client_id</code> | <code>str</code> | The registered client identifier. |
| <code>redirect_uri</code> | <code>str</code> | Callback URI; must exactly match a registered value. |
| <code>scope</code> | <code>str</code> | Space-delimited scopes. Include `offline_access` to receive a refresh token. |
| <code>state</code> | <code>str</code> | Opaque CSRF token; echoed back unchanged. |
| <code>code_challenge</code> | <code>str</code> | PKCE challenge — base64url(SHA-256(code_verifier)). |
| <code>code_challenge_method</code> | <code>[CodeChallengeMethodOrStr](walmart_apis/models/enums/code_challenge_method.py)</code> | Must be `S256`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[AuthorizeErrorBody](walmart_apis/errors/authorize_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[AuthorizeError](walmart_apis/models/authorize_error.py)</code> |
| 429, 500 | <code>[OauthErrorModel](walmart_apis/models/oauth_error_model.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_token(grant_type: GrantTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, code_verifier: str | None = None, refresh_token: str | None = None, redirect_uri: str | None = None, scope: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TokenResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Exchanges a grant for an OAuth access token. Supported `grant_type` values:

| grant_type | Flow | Required (besides grant_type) |
|----------------------|------------------|---------------------------------|
| `client_credentials` | seller-direct | client auth (see below) |
| `authorization_code` | delegated | `code`, `code_verifier` (PKCE) |
| `refresh_token` | delegated | `refresh_token` |

**Client authentication:** credentials in the form body (`client_secret_post`)
— `client_id` + `client_secret`. HTTP Basic is also accepted. **Public
clients** (Solution-Provider apps registered `token_endpoint_auth_method: none`)
send no secret on the delegated grants; PKCE protects the code.

**`client_credentials`:** issues **no** refresh token (re-mint on expiry).
**`scope` is decorative here** — accepted for compatibility but **not honored**;
access is governed by the scopes provisioned per client in IAM ; there
is no down-scoping and the response does not echo `scope`. (Verified: `/v3/token`
ignores any `scope=` value.)

**`authorization_code`:** `redirect_uri` is accepted for OAuth 2.0 back-compat
but not required in 2.1 (PKCE covers injection).

**`refresh_token`:** the response includes a **rotated** `refresh_token` — the
presented token is invalidated (OAuth 2.1 §4.3.1; IAM rotates today, ~1-year
TTL). A requested `scope` MUST NOT exceed the originally granted scope.

**Token:** `Bearer` (RFC 6750), sent downstream as `Authorization: Bearer
<token>` — **not** `WM_SEC.ACCESS_TOKEN`.

**Implemented by `the Authorization API` as a stateless proxy to Walmart IAM .**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.authorization.create_token(GrantType.CLIENT_CREDENTIALS)
    # TODO: Handle 'response' of type TokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateTokenErrorBody
```

**Async**

```python
try:
    response = await async_client.authorization.create_token(GrantType.CLIENT_CREDENTIALS)
    # TODO: Handle 'response' of type TokenResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateTokenErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>grant_type</code> | <code>[GrantTypeOrStr](walmart_apis/models/enums/grant_type.py)</code> | The OAuth grant type. |
| <code>client_id</code> | <code>str \| None</code> | Client identifier (client_secret_post / public clients). Omit if using HTTP Basic.<br>**Default**: <code>None</code> |
| <code>client_secret</code> | <code>str \| None</code> | Client secret (client_secret_post). Omit for public clients or HTTP Basic.<br>**Default**: <code>None</code> |
| <code>code</code> | <code>str \| None</code> | Authorization code from `/auth/v4/authorize` (authorization_code grant).<br>**Default**: <code>None</code> |
| <code>code_verifier</code> | <code>str \| None</code> | PKCE verifier whose S256 hash equals the earlier `code_challenge` (authorization_code grant).<br>**Default**: <code>None</code> |
| <code>refresh_token</code> | <code>str \| None</code> | A previously issued refresh token (refresh_token grant). Rotated on use.<br>**Default**: <code>None</code> |
| <code>redirect_uri</code> | <code>str \| None</code> | Accepted for OAuth 2.0 back-compat on authorization_code; not required in 2.1 (PKCE covers injection).<br>**Default**: <code>None</code> |
| <code>scope</code> | <code>str \| None</code> | **client_credentials:** accepted for compatibility but **not honored**<br> — no down-scoping; not echoed. **refresh_token:** optional;<br>MUST NOT exceed the originally granted scope.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TokenResponse](walmart_apis/models/token_response.py)</code> -- Access token issued.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateTokenErrorBody](walmart_apis/errors/create_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 429, 500 | <code>[OauthErrorModel](walmart_apis/models/oauth_error_model.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_client(body: ClientRegistrationRequest | ClientRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ClientRegistrationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Registers a Solution Provider client and returns its `client_id` (RFC
7591). Lets Solution Providers onboard without manual registration.

Public clients set `token_endpoint_auth_method: none` (no secret; PKCE
required). Confidential clients receive a `client_secret`. `redirect_uris`
are validated and later enforced by exact match at `/auth/v4/authorize`.

Proxied to Walmart IAM's registration endpoint (/). RFC 7592
registration management (read/update/delete via a
`registration_access_token`) is not offered in this version.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.authorization.register_client(ClientRegistrationRequest(redirect_uris=["https://example.com"]))
    # TODO: Handle 'response' of type ClientRegistrationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterClientErrorBody
```

**Async**

```python
try:
    response = await async_client.authorization.register_client(
        ClientRegistrationRequest(redirect_uris=["https://example.com"])
    )
    # TODO: Handle 'response' of type ClientRegistrationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterClientErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ClientRegistrationRequest](walmart_apis/models/client_registration_request.py) \| [ClientRegistrationRequestDict](walmart_apis/models/client_registration_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ClientRegistrationResponse](walmart_apis/models/client_registration_response.py)</code> -- Client registered.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[RegisterClientErrorBody](walmart_apis/errors/register_client_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401 | <code>[RegistrationError](walmart_apis/models/registration_error.py)</code> |
| 429, 500 | <code>[OauthErrorModel](walmart_apis/models/oauth_error_model.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Catalog

> Source: [Catalog](walmart_apis/apis/catalog.py)

<details>
<summary><code>def get_catalog_item(walmart_item_id: str, marketplace_ids: list[str], *, included_data: list[IncludedDatumOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> Item</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.catalog.get_catalog_item("00000000000000", ["some example string"])
    # TODO: Handle 'response' of type Item
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCatalogItemErrorBody
```

**Async**

```python
try:
    response = await async_client.catalog.get_catalog_item("00000000000000", ["some example string"])
    # TODO: Handle 'response' of type Item
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCatalogItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>walmart_item_id</code> | <code>str</code> | Walmart Item ID (14-digit numeric identifier) |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Walmart marketplace identifiers. Use WALMART_US for the US marketplace. |
| <code>included_data</code> | <code>list&#91;[IncludedDatumOrStr](walmart_apis/models/enums/included_datum.py)&#93; \| None</code> | Data sections to include in the response<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Item](walmart_apis/models/item.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetCatalogItemErrorBody](walmart_apis/errors/get_catalog_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_catalog_items(marketplace_ids: list[str], *, keywords: str | None = None, walmart_item_ids: str | None = None, seller_sku: str | None = None, gtin: str | None = None, upc: str | None = None, included_data: list[IncludedDatumOrStr] | None = None, page_size: int | None = 10, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ItemSearchResults</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search the Walmart Marketplace catalog using keywords, WalmartItemId,
GTIN, UPC, or seller SKU. Returns matching catalog items.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.catalog.search_catalog_items(["some example string"])
    # TODO: Handle 'response' of type ItemSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchCatalogItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.catalog.search_catalog_items(["some example string"])
    # TODO: Handle 'response' of type ItemSearchResults
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchCatalogItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Walmart marketplace identifiers. Use WALMART_US for the US marketplace. |
| <code>keywords</code> | <code>str \| None</code> | Keyword search terms<br>**Default**: <code>None</code> |
| <code>walmart_item_ids</code> | <code>str \| None</code> | Comma-separated Walmart Item IDs (14-digit). Max 20.<br>**Default**: <code>None</code> |
| <code>seller_sku</code> | <code>str \| None</code> | Seller-defined SKU<br>**Default**: <code>None</code> |
| <code>gtin</code> | <code>str \| None</code> | Global Trade Item Number (14-digit)<br>**Default**: <code>None</code> |
| <code>upc</code> | <code>str \| None</code> | Universal Product Code (12-digit)<br>**Default**: <code>None</code> |
| <code>included_data</code> | <code>list&#91;[IncludedDatumOrStr](walmart_apis/models/enums/included_datum.py)&#93; \| None</code> | Data sections to include in the response<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Number of results per page (1–20).<br>**Known limitation:** The PIQS keyword search backend hard-caps results at 40 items per call regardless of this value.<br>**Default**: <code>10</code> |
| <code>page_token</code> | <code>str \| None</code> | Token for the next page of results, obtained from `pagination.nextToken` in a previous response.<br>**Known limitation:** Cursor-based pagination is not currently supported for keyword search. The PIQS search backend (`/v3/items/walmart/search`) does not return a `nextCursor` and does not honour this parameter. Results are capped at 40 items per call. Reserved for future use once PIQS exposes pagination support.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemSearchResults](walmart_apis/models/item_search_results.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SearchCatalogItemsErrorBody](walmart_apis/errors/search_catalog_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DataKiosk

> Source: [DataKiosk](walmart_apis/apis/data_kiosk.py)

<details>
<summary><code>def cancel_query(query_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelQueryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.data_kiosk.cancel_query("some example string")
    # TODO: Handle 'response' of type CancelQueryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelQueryErrorBody
```

**Async**

```python
try:
    response = await async_client.data_kiosk.cancel_query("some example string")
    # TODO: Handle 'response' of type CancelQueryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelQueryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelQueryResponse](walmart_apis/models/cancel_query_response.py)</code> -- Query cancellation accepted

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelQueryErrorBody](walmart_apis/errors/cancel_query_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_query(body: CreateQuerySpecification | CreateQuerySpecificationDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateQueryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Submits a structured query for async processing.
Query language TBD pending ADR (GraphQL vs REST hybrid — Pod 4).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.data_kiosk.create_query(CreateQuerySpecification(query="some example string"))
    # TODO: Handle 'response' of type CreateQueryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateQueryErrorBody
```

**Async**

```python
try:
    response = await async_client.data_kiosk.create_query(CreateQuerySpecification(query="some example string"))
    # TODO: Handle 'response' of type CreateQueryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateQueryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateQuerySpecification](walmart_apis/models/create_query_specification.py) \| [CreateQuerySpecificationDict](walmart_apis/models/create_query_specification.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateQueryResponse](walmart_apis/models/create_query_response.py)</code> -- Query request accepted for processing

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateQueryErrorBody](walmart_apis/errors/create_query_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_document(document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Document</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a pre-signed URL for downloading query result data.
Do not log the pre-signed URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.data_kiosk.get_document("some example string")
    # TODO: Handle 'response' of type Document
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDocumentErrorBody
```

**Async**

```python
try:
    response = await async_client.data_kiosk.get_document("some example string")
    # TODO: Handle 'response' of type Document
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDocumentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>document_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Document](walmart_apis/models/document.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetDocumentErrorBody](walmart_apis/errors/get_document_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_queries(*, processing_statuses: list[ProcessingStatusOrStr] | None = None, page_size: int | None = 10, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetQueriesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of Data Kiosk queries submitted by the seller,
optionally filtered by processing status and creation date range.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.data_kiosk.get_queries()
    # TODO: Handle 'response' of type GetQueriesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetQueriesErrorBody
```

**Async**

```python
try:
    response = await async_client.data_kiosk.get_queries()
    # TODO: Handle 'response' of type GetQueriesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetQueriesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>processing_statuses</code> | <code>list&#91;[ProcessingStatusOrStr](walmart_apis/models/enums/processing_status.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>10</code> |
| <code>created_since</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>created_until</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetQueriesResponse](walmart_apis/models/get_queries_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetQueriesErrorBody](walmart_apis/errors/get_queries_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_query(query_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Query</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.data_kiosk.get_query("some example string")
    # TODO: Handle 'response' of type Query
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetQueryErrorBody
```

**Async**

```python
try:
    response = await async_client.data_kiosk.get_query("some example string")
    # TODO: Handle 'response' of type Query
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetQueryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Query](walmart_apis/models/query.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetQueryErrorBody](walmart_apis/errors/get_query_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Disputes

> Source: [Disputes](walmart_apis/apis/disputes.py)

<details>
<summary><code>def check_dispute_eligibility(*, request_options: RequestOptionsOrDict | None = None) -> DisputeEligibilityResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns whether the authenticated seller is eligible to raise a payment
dispute and, if not, the reason for ineligibility. Delegates to
GMPPaymentsPlatform (Phase 5).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.disputes.check_dispute_eligibility()
    # TODO: Handle 'response' of type DisputeEligibilityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckDisputeEligibilityErrorBody
```

**Async**

```python
try:
    response = await async_client.disputes.check_dispute_eligibility()
    # TODO: Handle 'response' of type DisputeEligibilityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckDisputeEligibilityErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DisputeEligibilityResponse](walmart_apis/models/dispute_eligibility_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CheckDisputeEligibilityErrorBody](walmart_apis/errors/check_dispute_eligibility_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Feeds

> Source: [Feeds](walmart_apis/apis/feeds.py)

<details>
<summary><code>def cancel_feed(feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelFeedResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Placeholder — not yet implemented.** Cancels the feed identified by
feedId if it is still queued or in progress. Mirrors Amazon SP-API
`cancelFeed` (DELETE /feeds/2021-06-30/feeds/{feedId}) so partners can
generate a client against the final contract now. A feed that has
already reached DONE or ERROR cannot be cancelled.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feeds.cancel_feed("some example string")
    # TODO: Handle 'response' of type CancelFeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelFeedErrorBody
```

**Async**

```python
try:
    response = await async_client.feeds.cancel_feed("some example string")
    # TODO: Handle 'response' of type CancelFeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelFeedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelFeedResponse](walmart_apis/models/cancel_feed_response.py)</code> -- Cancellation accepted

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelFeedErrorBody](walmart_apis/errors/cancel_feed_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList1](walmart_apis/models/error_list1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_feed(feed_type: FeedTypeOrStr, file: FileInput, *, marketplace_id: str | None = None, content_type: ContentTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CreateFeedResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Upload a feed file and submit it for asynchronous processing in a single call.
The server handles document storage internally. Use the returned feedId to poll
processing status via GET /feeds/v4/feeds/{feedId}.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feeds.create_feed(FeedType.LISTINGS_FEED, Path("path/to/file.bin"))
    # TODO: Handle 'response' of type CreateFeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateFeedErrorBody
```

**Async**

```python
try:
    response = await async_client.feeds.create_feed(FeedType.LISTINGS_FEED, Path("path/to/file.bin"))
    # TODO: Handle 'response' of type CreateFeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateFeedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_type</code> | <code>[FeedTypeOrStr](walmart_apis/models/enums/feed_type.py)</code> | The type of feed being submitted |
| <code>file</code> | <code>FileInput</code> | The feed content file to upload and process |
| <code>marketplace_id</code> | <code>str \| None</code> | Marketplace identifier (opaque token). If omitted, the service applies WALMART_US.<br>**Default**: <code>None</code> |
| <code>content_type</code> | <code>[ContentTypeOrStr](walmart_apis/models/enums/content_type.py) \| None</code> | MIME type of the uploaded feed content.<br>If omitted, the server infers from the file's Content-Type in the multipart header.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateFeedResponse](walmart_apis/models/create_feed_response.py)</code> -- Feed accepted for processing

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateFeedErrorBody](walmart_apis/errors/create_feed_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList1](walmart_apis/models/error_list1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_feed(feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Feed</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feeds.get_feed("some example string")
    # TODO: Handle 'response' of type Feed
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeedErrorBody
```

**Async**

```python
try:
    response = await async_client.feeds.get_feed("some example string")
    # TODO: Handle 'response' of type Feed
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeedErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Feed](walmart_apis/models/feed.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFeedErrorBody](walmart_apis/errors/get_feed_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList1](walmart_apis/models/error_list1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_feed_document(feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Downloads the raw feed document file. The response is a binary stream
(application/octet-stream). The Content-Disposition header contains the
original filename when available. Content-Length header is always set
to enable download progress tracking.

An IDOR check is performed before the download — the authenticated
seller must own the feed referenced by feedId.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feeds.get_feed_document("some example string")
    # TODO: Handle 'response' of type FileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeedDocumentErrorBody
```

**Async**

```python
try:
    response = await async_client.feeds.get_feed_document("some example string")
    # TODO: Handle 'response' of type AsyncFileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeedDocumentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>FileResponse</code> -- Binary file stream

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFeedDocumentErrorBody](walmart_apis/errors/get_feed_document_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList1](walmart_apis/models/error_list1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_feeds(*, feed_types: list[FeedTypeOrStr] | None = None, feed_statuses: list[FeedStatusOrStr] | None = None, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetFeedsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feeds.get_feeds()
    # TODO: Handle 'response' of type GetFeedsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeedsErrorBody
```

**Async**

```python
try:
    response = await async_client.feeds.get_feeds()
    # TODO: Handle 'response' of type GetFeedsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeedsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>feed_types</code> | <code>list&#91;[FeedTypeOrStr](walmart_apis/models/enums/feed_type.py)&#93; \| None</code> | Feed type filter<br>**Default**: <code>None</code> |
| <code>feed_statuses</code> | <code>list&#91;[FeedStatusOrStr](walmart_apis/models/enums/feed_status.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>created_since</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>created_until</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>10</code> |
| <code>next_token</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFeedsResponse](walmart_apis/models/get_feeds_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFeedsErrorBody](walmart_apis/errors/get_feeds_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList1](walmart_apis/models/error_list1.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## FinalPayout

> Source: [FinalPayout](walmart_apis/apis/final_payout.py)

<details>
<summary><code>def get_final_payout_case_status(*, request_options: RequestOptionsOrDict | None = None) -> FinalPayoutCaseStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the current state, case ID, and payable amount for the authenticated
seller's final payout case (used when a seller account is being offboarded).
Delegates to GMPPaymentsPlatform (Phase 5).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.final_payout.get_final_payout_case_status()
    # TODO: Handle 'response' of type FinalPayoutCaseStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFinalPayoutCaseStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.final_payout.get_final_payout_case_status()
    # TODO: Handle 'response' of type FinalPayoutCaseStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFinalPayoutCaseStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FinalPayoutCaseStatusResponse](walmart_apis/models/final_payout_case_status_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFinalPayoutCaseStatusErrorBody](walmart_apis/errors/get_final_payout_case_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 404, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_final_payout_case_status(body: DisbursementsV4FinalPayoutCaseUpdateStatusRequest | DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FinalPayoutCaseStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Transitions the authenticated seller's final payout case to Resolved or
Closed, optionally including resolution notes. Requires disbursements:write
scope. Delegates to GMPPaymentsPlatform (Phase 5).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.final_payout.update_final_payout_case_status(
        DisbursementsV4FinalPayoutCaseUpdateStatusRequest(status=Status3.RESOLVED)
    )
    # TODO: Handle 'response' of type FinalPayoutCaseStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFinalPayoutCaseStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.final_payout.update_final_payout_case_status(
        DisbursementsV4FinalPayoutCaseUpdateStatusRequest(status=Status3.RESOLVED)
    )
    # TODO: Handle 'response' of type FinalPayoutCaseStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFinalPayoutCaseStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DisbursementsV4FinalPayoutCaseUpdateStatusRequest](walmart_apis/models/disbursements_v4_final_payout_case_update_status_request.py) \| [DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict](walmart_apis/models/disbursements_v4_final_payout_case_update_status_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FinalPayoutCaseStatusResponse](walmart_apis/models/final_payout_case_status_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateFinalPayoutCaseStatusErrorBody](walmart_apis/errors/update_final_payout_case_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Finances

> Source: [Finances](walmart_apis/apis/finances.py)

<details>
<summary><code>def list_financial_event_groups(*, max_results_per_page: int | None = None, financial_event_group_started_before: RFC3339DateTime | None = None, financial_event_group_started_after: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns financial event groups for the seller.

**Status: stub** — no upstream endpoint found that models the SP-API
FinancialEventGroup (requires eventGroupId keying, date-range filter,
and cursor pagination). Returns empty response pending Phase 5.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.finances.list_financial_event_groups()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFinancialEventGroupsErrorBody
```

**Async**

```python
try:
    response = await async_client.finances.list_financial_event_groups()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFinancialEventGroupsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>max_results_per_page</code> | <code>int \| None</code> | The maximum number of results per page.<br>**Default**: <code>None</code> |
| <code>financial_event_group_started_before</code> | <code>RFC3339DateTime \| None</code> | Financial event groups that opened before this date/time (ISO 8601).<br>**Default**: <code>None</code> |
| <code>financial_event_group_started_after</code> | <code>RFC3339DateTime \| None</code> | Financial event groups that opened after this date/time (ISO 8601).<br>**Default**: <code>None</code> |
| <code>next_token</code> | <code>str \| None</code> | Cursor token for the next page of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListFinancialEventGroupsErrorBody](walmart_apis/errors/list_financial_event_groups_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_financial_events(*, max_results_per_page: int | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns financial events for the authenticated seller via GMP partnerTxnSearch.

**Best-effort implementation** — backed by GMP partnerTxnSearch.
Returns transaction records for the seller keyed by partnerId.

**Unsupported parameters:** PostedAfter, PostedBefore, and NextToken are not
supported by the upstream. Supplying any of these parameters returns 400 Bad Request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.finances.list_financial_events()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFinancialEventsErrorBody
```

**Async**

```python
try:
    response = await async_client.finances.list_financial_events()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFinancialEventsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>max_results_per_page</code> | <code>int \| None</code> | Ignored — GMP returns all results in a single page.<br>**Default**: <code>None</code> |
| <code>posted_after</code> | <code>RFC3339DateTime \| None</code> | Not supported — returns 400 Bad Request if supplied.<br>**Default**: <code>None</code> |
| <code>posted_before</code> | <code>RFC3339DateTime \| None</code> | Not supported — returns 400 Bad Request if supplied.<br>**Default**: <code>None</code> |
| <code>next_token</code> | <code>str \| None</code> | Not supported — returns 400 Bad Request if supplied.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListFinancialEventsErrorBody](walmart_apis/errors/list_financial_events_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_financial_events_by_group_id(event_group_id: str, *, max_results_per_page: int | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns financial events for a specific financial event group.

**Status: stub** — no upstream maps eventGroupId to a financial event
set. Returns empty response pending Phase 5.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.finances.list_financial_events_by_group_id("some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFinancialEventsByGroupIdErrorBody
```

**Async**

```python
try:
    response = await async_client.finances.list_financial_events_by_group_id("some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFinancialEventsByGroupIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>event_group_id</code> | <code>str</code> | The identifier of the financial event group. |
| <code>max_results_per_page</code> | <code>int \| None</code> | The maximum number of results to return per page.<br>**Default**: <code>None</code> |
| <code>posted_after</code> | <code>RFC3339DateTime \| None</code> | Financial events posted after (or on) this date (ISO 8601).<br>**Default**: <code>None</code> |
| <code>posted_before</code> | <code>RFC3339DateTime \| None</code> | Financial events posted before (but not on) this date (ISO 8601).<br>**Default**: <code>None</code> |
| <code>next_token</code> | <code>str \| None</code> | Cursor token for the next page of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListFinancialEventsByGroupIdErrorBody](walmart_apis/errors/list_financial_events_by_group_id_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_financial_events_by_order_id(order_id: str, *, max_results_per_page: int | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns financial events for a specific order via GMP commission endpoint.

**Best-effort implementation** — returns commission charges only;
refunds, fees, and adjustments are absent. IDOR ownership gate enforced.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.finances.list_financial_events_by_order_id("some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFinancialEventsByOrderIdErrorBody
```

**Async**

```python
try:
    response = await async_client.finances.list_financial_events_by_order_id("some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFinancialEventsByOrderIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>str</code> | Walmart order number — must be numeric (1–50 digits). |
| <code>max_results_per_page</code> | <code>int \| None</code> | Ignored — GMP returns all commission entries in one page.<br>**Default**: <code>None</code> |
| <code>next_token</code> | <code>str \| None</code> | Not supported — returns 400 Bad Request if supplied.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListFinancialEventsByOrderIdErrorBody](walmart_apis/errors/list_financial_events_by_order_id_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## FulfillmentOutbound

> Source: [FulfillmentOutbound](walmart_apis/apis/fulfillment_outbound.py)

<details>
<summary><code>def cancel_fulfillment_order(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelFulfillmentOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fulfillment_outbound.cancel_fulfillment_order("some example string")
    # TODO: Handle 'response' of type CancelFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelFulfillmentOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.fulfillment_outbound.cancel_fulfillment_order("some example string")
    # TODO: Handle 'response' of type CancelFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelFulfillmentOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_fulfillment_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelFulfillmentOrderResponse](walmart_apis/models/cancel_fulfillment_order_response.py)</code> -- Cancellation request submitted

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelFulfillmentOrderErrorBody](walmart_apis/errors/cancel_fulfillment_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_fulfillment_order(body: CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateFulfillmentOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fulfillment_outbound.create_fulfillment_order(
        CreateFulfillmentOrderRequest(
            seller_fulfillment_order_id="some example string",
            displayable_order_id="some example string",
            displayable_order_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
            shipping_speed_category=ShippingSpeedCategory.STANDARD,
            destination_address=Address(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            items=[
                CreateFulfillmentOrderItem(
                    seller_sku="some example string", seller_fulfillment_order_item_id="some example string", quantity=1
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CreateFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateFulfillmentOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.fulfillment_outbound.create_fulfillment_order(
        CreateFulfillmentOrderRequest(
            seller_fulfillment_order_id="some example string",
            displayable_order_id="some example string",
            displayable_order_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
            shipping_speed_category=ShippingSpeedCategory.STANDARD,
            destination_address=Address(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            items=[
                CreateFulfillmentOrderItem(
                    seller_sku="some example string", seller_fulfillment_order_item_id="some example string", quantity=1
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CreateFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateFulfillmentOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateFulfillmentOrderRequest](walmart_apis/models/create_fulfillment_order_request.py) \| [CreateFulfillmentOrderRequestDict](walmart_apis/models/create_fulfillment_order_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateFulfillmentOrderResponse](walmart_apis/models/create_fulfillment_order_response.py)</code> -- Fulfillment order created

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateFulfillmentOrderErrorBody](walmart_apis/errors/create_fulfillment_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fulfillment_order(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetFulfillmentOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fulfillment_outbound.get_fulfillment_order("some example string")
    # TODO: Handle 'response' of type GetFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFulfillmentOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.fulfillment_outbound.get_fulfillment_order("some example string")
    # TODO: Handle 'response' of type GetFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFulfillmentOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_fulfillment_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFulfillmentOrderResponse](walmart_apis/models/get_fulfillment_order_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFulfillmentOrderErrorBody](walmart_apis/errors/get_fulfillment_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fulfillment_order_shipments(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetFulfillmentOrderShipmentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fulfillment_outbound.get_fulfillment_order_shipments("some example string")
    # TODO: Handle 'response' of type GetFulfillmentOrderShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFulfillmentOrderShipmentsErrorBody
```

**Async**

```python
try:
    response = await async_client.fulfillment_outbound.get_fulfillment_order_shipments("some example string")
    # TODO: Handle 'response' of type GetFulfillmentOrderShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFulfillmentOrderShipmentsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_fulfillment_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFulfillmentOrderShipmentsResponse](walmart_apis/models/get_fulfillment_order_shipments_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFulfillmentOrderShipmentsErrorBody](walmart_apis/errors/get_fulfillment_order_shipments_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_fulfillment_preview(body: GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetFulfillmentPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns estimated delivery dates, shipping costs, and available ship nodes
for a prospective fulfillment order. Use before creating the order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fulfillment_outbound.get_fulfillment_preview(
        GetFulfillmentPreviewRequest(
            address=Address(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            items=[
                GetFulfillmentPreviewItem(
                    seller_sku="some example string", quantity=1, seller_fulfillment_order_item_id="some example string"
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type GetFulfillmentPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFulfillmentPreviewErrorBody
```

**Async**

```python
try:
    response = await async_client.fulfillment_outbound.get_fulfillment_preview(
        GetFulfillmentPreviewRequest(
            address=Address(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            items=[
                GetFulfillmentPreviewItem(
                    seller_sku="some example string", quantity=1, seller_fulfillment_order_item_id="some example string"
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type GetFulfillmentPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFulfillmentPreviewErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetFulfillmentPreviewRequest](walmart_apis/models/get_fulfillment_preview_request.py) \| [GetFulfillmentPreviewRequestDict](walmart_apis/models/get_fulfillment_preview_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFulfillmentPreviewResponse](walmart_apis/models/get_fulfillment_preview_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFulfillmentPreviewErrorBody](walmart_apis/errors/get_fulfillment_preview_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_all_fulfillment_orders(*, query_start_date: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListAllFulfillmentOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fulfillment_outbound.list_all_fulfillment_orders()
    # TODO: Handle 'response' of type ListAllFulfillmentOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllFulfillmentOrdersErrorBody
```

**Async**

```python
try:
    response = await async_client.fulfillment_outbound.list_all_fulfillment_orders()
    # TODO: Handle 'response' of type ListAllFulfillmentOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAllFulfillmentOrdersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query_start_date</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>next_token</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListAllFulfillmentOrdersResponse](walmart_apis/models/list_all_fulfillment_orders_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListAllFulfillmentOrdersErrorBody](walmart_apis/errors/list_all_fulfillment_orders_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_fulfillment_order(seller_fulfillment_order_id: str, body: UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UpdateFulfillmentOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.fulfillment_outbound.update_fulfillment_order(
        "some example string", UpdateFulfillmentOrderRequest()
    )
    # TODO: Handle 'response' of type UpdateFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFulfillmentOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.fulfillment_outbound.update_fulfillment_order(
        "some example string", UpdateFulfillmentOrderRequest()
    )
    # TODO: Handle 'response' of type UpdateFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFulfillmentOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_fulfillment_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UpdateFulfillmentOrderRequest](walmart_apis/models/update_fulfillment_order_request.py) \| [UpdateFulfillmentOrderRequestDict](walmart_apis/models/update_fulfillment_order_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UpdateFulfillmentOrderResponse](walmart_apis/models/update_fulfillment_order_response.py)</code> -- Order updated

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateFulfillmentOrderErrorBody](walmart_apis/errors/update_fulfillment_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Inventory

> Source: [Inventory](walmart_apis/apis/inventory.py)

<details>
<summary><code>def bulk_update_inventory(body: BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BulkUpdateInventoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Bulk inventory update. Max 500 items per request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.inventory.bulk_update_inventory(
        BulkUpdateInventoryRequest(items=[BulkInventoryItem(seller_sku="some example string", quantity=1)])
    )
    # TODO: Handle 'response' of type BulkUpdateInventoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkUpdateInventoryErrorBody
```

**Async**

```python
try:
    response = await async_client.inventory.bulk_update_inventory(
        BulkUpdateInventoryRequest(items=[BulkInventoryItem(seller_sku="some example string", quantity=1)])
    )
    # TODO: Handle 'response' of type BulkUpdateInventoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BulkUpdateInventoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpdateInventoryRequest](walmart_apis/models/bulk_update_inventory_request.py) \| [BulkUpdateInventoryRequestDict](walmart_apis/models/bulk_update_inventory_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[BulkUpdateInventoryResponse](walmart_apis/models/bulk_update_inventory_response.py)</code> -- Bulk update accepted

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[BulkUpdateInventoryErrorBody](walmart_apis/errors/bulk_update_inventory_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_inventory_for_sku(sku: str, *, ship_node: str | None = None, request_options: RequestOptionsOrDict | None = None) -> InventorySummary</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.inventory.get_inventory_for_sku("some example string")
    # TODO: Handle 'response' of type InventorySummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInventoryForSkuErrorBody
```

**Async**

```python
try:
    response = await async_client.inventory.get_inventory_for_sku("some example string")
    # TODO: Handle 'response' of type InventorySummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInventoryForSkuErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sku</code> | <code>str</code> | Value sent with the request. |
| <code>ship_node</code> | <code>str \| None</code> | Walmart Ship Node ID (for multi-node sellers)<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InventorySummary](walmart_apis/models/inventory_summary.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetInventoryForSkuErrorBody](walmart_apis/errors/get_inventory_for_sku_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_inventory_summaries(*, skus: str | None = None, ship_node: str | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetInventorySummariesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.inventory.get_inventory_summaries()
    # TODO: Handle 'response' of type GetInventorySummariesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInventorySummariesErrorBody
```

**Async**

```python
try:
    response = await async_client.inventory.get_inventory_summaries()
    # TODO: Handle 'response' of type GetInventorySummariesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInventorySummariesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>skus</code> | <code>str \| None</code> | Comma-separated seller SKUs (max 50)<br>**Default**: <code>None</code> |
| <code>ship_node</code> | <code>str \| None</code> | Walmart Ship Node ID (for multi-node sellers)<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>100</code> |
| <code>next_token</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetInventorySummariesResponse](walmart_apis/models/get_inventory_summaries_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetInventorySummariesErrorBody](walmart_apis/errors/get_inventory_summaries_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_inventory_for_sku(sku: str, body: UpdateInventoryRequest | UpdateInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UpdateInventoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.inventory.update_inventory_for_sku("some example string", UpdateInventoryRequest(quantity=1))
    # TODO: Handle 'response' of type UpdateInventoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateInventoryForSkuErrorBody
```

**Async**

```python
try:
    response = await async_client.inventory.update_inventory_for_sku(
        "some example string", UpdateInventoryRequest(quantity=1)
    )
    # TODO: Handle 'response' of type UpdateInventoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateInventoryForSkuErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sku</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UpdateInventoryRequest](walmart_apis/models/update_inventory_request.py) \| [UpdateInventoryRequestDict](walmart_apis/models/update_inventory_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UpdateInventoryResponse](walmart_apis/models/update_inventory_response.py)</code> -- Inventory updated successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateInventoryForSkuErrorBody](walmart_apis/errors/update_inventory_for_sku_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ListingsItems

> Source: [ListingsItems](walmart_apis/apis/listings_items.py)

<details>
<summary><code>def delete_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ListingsItemSubmissionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.listings_items.delete_listings_item(
        "some example string", "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type ListingsItemSubmissionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteListingsItemErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_items.delete_listings_item(
        "some example string", "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type ListingsItemSubmissionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteListingsItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_id</code> | <code>str</code> | Seller identifier |
| <code>sku</code> | <code>str</code> | Seller SKU identifying the listing |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>issue_locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"en_US"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py)</code> -- Successfully submitted

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[DeleteListingsItemErrorBody](walmart_apis/errors/delete_listings_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], *, issue_locale: str | None = "en_US", included_data: list[IncludedDatum1OrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> Item1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.listings_items.get_listings_item(
        "some example string", "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type Item1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingsItemErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_items.get_listings_item(
        "some example string", "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type Item1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingsItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_id</code> | <code>str</code> | Seller identifier |
| <code>sku</code> | <code>str</code> | Seller SKU identifying the listing |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>issue_locale</code> | <code>str \| None</code> | Locale for issue messages (e.g. en_US)<br>**Default**: <code>"en_US"</code> |
| <code>included_data</code> | <code>list&#91;[IncludedDatum1OrStr](walmart_apis/models/enums/included_datum1.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Item1](walmart_apis/models/item1.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetListingsItemErrorBody](walmart_apis/errors/get_listings_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def patch_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], body: ListingsItemPatchRequest | ListingsItemPatchRequestDict, *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ListingsItemSubmissionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PATCH` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.listings_items.patch_listings_item(
        "some example string",
        "some example string",
        ["some example string"],
        ListingsItemPatchRequest(
            product_type="some example string", patches=[PatchOperation(op=Op.ADD, path="some example string")]
        ),
    )
    # TODO: Handle 'response' of type ListingsItemSubmissionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PatchListingsItemErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_items.patch_listings_item(
        "some example string",
        "some example string",
        ["some example string"],
        ListingsItemPatchRequest(
            product_type="some example string", patches=[PatchOperation(op=Op.ADD, path="some example string")]
        ),
    )
    # TODO: Handle 'response' of type ListingsItemSubmissionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PatchListingsItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_id</code> | <code>str</code> | Seller identifier |
| <code>sku</code> | <code>str</code> | Seller SKU identifying the listing |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>body</code> | <code>[ListingsItemPatchRequest](walmart_apis/models/listings_item_patch_request.py) \| [ListingsItemPatchRequestDict](walmart_apis/models/listings_item_patch_request.py)</code> | The request body. |
| <code>issue_locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"en_US"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py)</code> -- Successfully submitted

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[PatchListingsItemErrorBody](walmart_apis/errors/patch_listings_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def put_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], body: ListingsItemPutRequest | ListingsItemPutRequestDict, *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ListingsItemSubmissionResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.listings_items.put_listings_item(
        "some example string",
        "some example string",
        ["some example string"],
        ListingsItemPutRequest(product_type="some example string", attributes={}),
    )
    # TODO: Handle 'response' of type ListingsItemSubmissionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PutListingsItemErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_items.put_listings_item(
        "some example string",
        "some example string",
        ["some example string"],
        ListingsItemPutRequest(product_type="some example string", attributes={}),
    )
    # TODO: Handle 'response' of type ListingsItemSubmissionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PutListingsItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_id</code> | <code>str</code> | Seller identifier |
| <code>sku</code> | <code>str</code> | Seller SKU identifying the listing |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>body</code> | <code>[ListingsItemPutRequest](walmart_apis/models/listings_item_put_request.py) \| [ListingsItemPutRequestDict](walmart_apis/models/listings_item_put_request.py)</code> | The request body. |
| <code>issue_locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"en_US"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py)</code> -- Successfully submitted

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[PutListingsItemErrorBody](walmart_apis/errors/put_listings_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_listings_items(seller_id: str, marketplace_ids: list[str], *, included_data: list[IncludedDatum1OrStr] | None = None, page_size: int | None = 10, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ItemSearchResults1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of the seller's listings items. Mirrors Amazon
SP-API `searchListingsItems` so an existing SP-API client can call the
seller-level collection endpoint (no SKU in the path) against v4.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.listings_items.search_listings_items("some example string", ["some example string"])
    # TODO: Handle 'response' of type ItemSearchResults1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchListingsItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_items.search_listings_items("some example string", ["some example string"])
    # TODO: Handle 'response' of type ItemSearchResults1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchListingsItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_id</code> | <code>str</code> | Seller identifier |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>included_data</code> | <code>list&#91;[IncludedDatum1OrStr](walmart_apis/models/enums/included_datum1.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Maximum number of results per page<br>**Default**: <code>10</code> |
| <code>page_token</code> | <code>str \| None</code> | Opaque cursor returned by a previous call for the next page<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemSearchResults1](walmart_apis/models/item_search_results1.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SearchListingsItemsErrorBody](walmart_apis/errors/search_listings_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ListingsRestrictions

> Source: [ListingsRestrictions](walmart_apis/apis/listings_restrictions.py)

<details>
<summary><code>def get_listings_restrictions(asin: str, condition_type: ConditionType1OrStr, seller_id: str, marketplace_ids: list[str], *, reason_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> RestrictionList</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns restrictions on listing an item for a given ASIN and seller.
A successful response does not guarantee the seller can list — check
the restrictions array.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.listings_restrictions.get_listings_restrictions(
        "some example string", ConditionType1.NEW_NEW, "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type RestrictionList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingsRestrictionsErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_restrictions.get_listings_restrictions(
        "some example string", ConditionType1.NEW_NEW, "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type RestrictionList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingsRestrictionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>asin</code> | <code>str</code> | Walmart Item ID (maps to ASIN in Walmart Seller API) |
| <code>condition_type</code> | <code>[ConditionType1OrStr](walmart_apis/models/enums/condition_type1.py)</code> | Value sent with the request. |
| <code>seller_id</code> | <code>str</code> | Value sent with the request. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>reason_locale</code> | <code>str \| None</code> | Locale for localized restriction reason messages<br>**Default**: <code>"en_US"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RestrictionList](walmart_apis/models/restriction_list.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetListingsRestrictionsErrorBody](walmart_apis/errors/get_listings_restrictions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## MerchantFulfillment

> Source: [MerchantFulfillment](walmart_apis/apis/merchant_fulfillment.py)

<details>
<summary><code>def cancel_shipment(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelShipmentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.merchant_fulfillment.cancel_shipment("some example string")
    # TODO: Handle 'response' of type CancelShipmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelShipmentErrorBody
```

**Async**

```python
try:
    response = await async_client.merchant_fulfillment.cancel_shipment("some example string")
    # TODO: Handle 'response' of type CancelShipmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelShipmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shipment_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelShipmentResponse](walmart_apis/models/cancel_shipment_response.py)</code> -- Shipment cancelled

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelShipmentErrorBody](walmart_apis/errors/cancel_shipment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_shipment(body: CreateShipmentRequest | CreateShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateShipmentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a shipment for an order, purchases a shipping label from the
selected carrier, and returns the label for printing.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.merchant_fulfillment.create_shipment(
        CreateShipmentRequest(
            shipment_request_details=ShipmentRequestDetails(
                purchase_order_id="some example string",
                ship_from_address=Address1(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                ship_to_address=Address1(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                package_dimensions=PackageDimensions(length=1.5, width=1.5, height=1.5, unit=Unit.INCHES),
                weight=Weight(value=1.5, unit=Unit1.OZ),
                ship_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
                shipping_service_options=ShippingServiceOptions(),
            ),
            shipping_service_id="some example string",
        ),
    )
    # TODO: Handle 'response' of type CreateShipmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateShipmentErrorBody
```

**Async**

```python
try:
    response = await async_client.merchant_fulfillment.create_shipment(
        CreateShipmentRequest(
            shipment_request_details=ShipmentRequestDetails(
                purchase_order_id="some example string",
                ship_from_address=Address1(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                ship_to_address=Address1(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                package_dimensions=PackageDimensions(length=1.5, width=1.5, height=1.5, unit=Unit.INCHES),
                weight=Weight(value=1.5, unit=Unit1.OZ),
                ship_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
                shipping_service_options=ShippingServiceOptions(),
            ),
            shipping_service_id="some example string",
        ),
    )
    # TODO: Handle 'response' of type CreateShipmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateShipmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateShipmentRequest](walmart_apis/models/create_shipment_request.py) \| [CreateShipmentRequestDict](walmart_apis/models/create_shipment_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateShipmentResponse](walmart_apis/models/create_shipment_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateShipmentErrorBody](walmart_apis/errors/create_shipment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_eligible_shipping_services(body: GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetEligibleShippingServicesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns available carriers and rates for a shipment based on package
dimensions, weight, and destination address.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.merchant_fulfillment.get_eligible_shipping_services(
        GetEligibleShippingServicesRequest(
            shipment_request_details=ShipmentRequestDetails(
                purchase_order_id="some example string",
                ship_from_address=Address1(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                ship_to_address=Address1(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                package_dimensions=PackageDimensions(length=1.5, width=1.5, height=1.5, unit=Unit.INCHES),
                weight=Weight(value=1.5, unit=Unit1.OZ),
                ship_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
                shipping_service_options=ShippingServiceOptions(),
            ),
        ),
    )
    # TODO: Handle 'response' of type GetEligibleShippingServicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEligibleShippingServicesErrorBody
```

**Async**

```python
try:
    response = await async_client.merchant_fulfillment.get_eligible_shipping_services(
        GetEligibleShippingServicesRequest(
            shipment_request_details=ShipmentRequestDetails(
                purchase_order_id="some example string",
                ship_from_address=Address1(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                ship_to_address=Address1(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                package_dimensions=PackageDimensions(length=1.5, width=1.5, height=1.5, unit=Unit.INCHES),
                weight=Weight(value=1.5, unit=Unit1.OZ),
                ship_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
                shipping_service_options=ShippingServiceOptions(),
            ),
        ),
    )
    # TODO: Handle 'response' of type GetEligibleShippingServicesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEligibleShippingServicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetEligibleShippingServicesRequest](walmart_apis/models/get_eligible_shipping_services_request.py) \| [GetEligibleShippingServicesRequestDict](walmart_apis/models/get_eligible_shipping_services_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetEligibleShippingServicesResponse](walmart_apis/models/get_eligible_shipping_services_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetEligibleShippingServicesErrorBody](walmart_apis/errors/get_eligible_shipping_services_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_label(shipment_id: str, *, format_: FormatOrStr | None = Format.PDF, request_options: RequestOptionsOrDict | None = None) -> Label</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the purchased shipping label for a shipment in the requested
file format for printing.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.merchant_fulfillment.get_label("some example string")
    # TODO: Handle 'response' of type Label
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLabelErrorBody
```

**Async**

```python
try:
    response = await async_client.merchant_fulfillment.get_label("some example string")
    # TODO: Handle 'response' of type Label
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLabelErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shipment_id</code> | <code>str</code> | Value sent with the request. |
| <code>format_</code> | <code>[FormatOrStr](walmart_apis/models/enums/format.py) \| None</code> | Value sent with the request.<br>**Default**: <code>Format.PDF</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Label](walmart_apis/models/label.py)</code> -- Label returned

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetLabelErrorBody](walmart_apis/errors/get_label_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment2(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetShipmentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.merchant_fulfillment.get_shipment2("some example string")
    # TODO: Handle 'response' of type GetShipmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipment2ErrorBody
```

**Async**

```python
try:
    response = await async_client.merchant_fulfillment.get_shipment2("some example string")
    # TODO: Handle 'response' of type GetShipmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipment2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shipment_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetShipmentResponse](walmart_apis/models/get_shipment_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetShipment2ErrorBody](walmart_apis/errors/get_shipment2_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Orders

> Source: [Orders](walmart_apis/apis/orders.py)

<details>
<summary><code>def acknowledge_order(purchase_order_id: str, body: AcknowledgeOrderRequest | AcknowledgeOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AcknowledgeOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.acknowledge_order(
        "some example string",
        AcknowledgeOrderRequest(order_lines=[AcknowledgeOrderLine(line_number="some example string")]),
    )
    # TODO: Handle 'response' of type AcknowledgeOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AcknowledgeOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.acknowledge_order(
        "some example string",
        AcknowledgeOrderRequest(order_lines=[AcknowledgeOrderLine(line_number="some example string")]),
    )
    # TODO: Handle 'response' of type AcknowledgeOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AcknowledgeOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[AcknowledgeOrderRequest](walmart_apis/models/acknowledge_order_request.py) \| [AcknowledgeOrderRequestDict](walmart_apis/models/acknowledge_order_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AcknowledgeOrderResponse](walmart_apis/models/acknowledge_order_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[AcknowledgeOrderErrorBody](walmart_apis/errors/acknowledge_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_order_lines(purchase_order_id: str, body: CancelOrderLinesRequest | CancelOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelOrderLinesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.cancel_order_lines(
        "some example string",
        CancelOrderLinesRequest(
            order_lines=[
                CancelOrderLine(
                    line_number="some example string", cancellation_reason=CancellationReason.CUSTOMER_REQUESTED
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelOrderLinesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelOrderLinesErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.cancel_order_lines(
        "some example string",
        CancelOrderLinesRequest(
            order_lines=[
                CancelOrderLine(
                    line_number="some example string", cancellation_reason=CancellationReason.CUSTOMER_REQUESTED
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelOrderLinesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelOrderLinesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[CancelOrderLinesRequest](walmart_apis/models/cancel_order_lines_request.py) \| [CancelOrderLinesRequestDict](walmart_apis/models/cancel_order_lines_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelOrderLinesResponse](walmart_apis/models/cancel_order_lines_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelOrderLinesErrorBody](walmart_apis/errors/cancel_order_lines_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deliver_order_lines(purchase_order_id: str, body: DeliverOrderLinesRequest | DeliverOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeliverOrderLinesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Records the terminal `Delivered` event for one or more order
lines, optionally with package-level proof-of-delivery
(tracking number, package number, delivery timestamp). This is
separated from `/shipment-status` because delivery is a
terminal state and carries different downstream semantics
(invoicing windows open, return windows start).

Walmart parity from gmp-orders-mono `deliverOrder`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.deliver_order_lines(
        "some example string",
        DeliverOrderLinesRequest(order_lines=[DeliverOrderLine(line_number="some example string")]),
    )
    # TODO: Handle 'response' of type DeliverOrderLinesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeliverOrderLinesErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.deliver_order_lines(
        "some example string",
        DeliverOrderLinesRequest(order_lines=[DeliverOrderLine(line_number="some example string")]),
    )
    # TODO: Handle 'response' of type DeliverOrderLinesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeliverOrderLinesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[DeliverOrderLinesRequest](walmart_apis/models/deliver_order_lines_request.py) \| [DeliverOrderLinesRequestDict](walmart_apis/models/deliver_order_lines_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[DeliverOrderLinesResponse](walmart_apis/models/deliver_order_lines_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[DeliverOrderLinesErrorBody](walmart_apis/errors/deliver_order_lines_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_order(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_order("some example string")
    # TODO: Handle 'response' of type GetOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_order("some example string")
    # TODO: Handle 'response' of type GetOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Walmart Purchase Order ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOrderResponse](walmart_apis/models/get_order_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetOrderErrorBody](walmart_apis/errors/get_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_order_address(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetOrderAddressResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the ship-to postal address for a single purchase order.
Mirrors Amazon SP-API `getOrderAddress`. PII-restricted endpoint:
handlers are marked `@RestrictedData` server-side and the
response body must NOT be logged.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_order_address("some example string")
    # TODO: Handle 'response' of type GetOrderAddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderAddressErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_order_address("some example string")
    # TODO: Handle 'response' of type GetOrderAddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderAddressErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOrderAddressResponse](walmart_apis/models/get_order_address_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetOrderAddressErrorBody](walmart_apis/errors/get_order_address_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_order_buyer_info(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetOrderBuyerInfoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the buyer's display name, email address, and an
anonymized phone (last 4 digits only). Mirrors Amazon SP-API
`getOrderBuyerInfo`. PII-restricted endpoint: handlers are
marked `@RestrictedData` server-side and request/response
bodies must NOT be logged.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_order_buyer_info("some example string")
    # TODO: Handle 'response' of type GetOrderBuyerInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderBuyerInfoErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_order_buyer_info("some example string")
    # TODO: Handle 'response' of type GetOrderBuyerInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderBuyerInfoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOrderBuyerInfoResponse](walmart_apis/models/get_order_buyer_info_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetOrderBuyerInfoErrorBody](walmart_apis/errors/get_order_buyer_info_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_order_items(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetFulfillmentOrderShipmentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the SKU / quantity / item-price projection of a single
purchase order. Mirrors Amazon SP-API `getOrderItems`. Not
PII-restricted: only product, quantity, and price are returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_order_items("some example string")
    # TODO: Handle 'response' of type GetFulfillmentOrderShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_order_items("some example string")
    # TODO: Handle 'response' of type GetFulfillmentOrderShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFulfillmentOrderShipmentsResponse](walmart_apis/models/get_fulfillment_order_shipments_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetOrderItemsErrorBody](walmart_apis/errors/get_order_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_order_regulated_info(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetOrderRegulatedInfoResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Parity with Amazon SP-API Orders v0 `getOrderRegulatedInfo`. Returns
the verification requirements that apply to an order containing
regulated items (alcohol, tobacco, age-restricted goods): the
required ID-verification method, the minimum buyer age, the
regulated category, and any value-added services the order ships
with.

**Walmart OMS coverage gap .** The the underlying service Order
Lookup response does not currently surface regulated-item
metadata. Until upstream support lands (tracked separately as a
follow-up to this PR), every order returns the safe default
`regulatedCategory=NOT_REGULATED` with `requiredVerificationMethod=NONE`.
The endpoint shape and contract are stable; only the projected
values will become richer once OMS exposes the fields.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_order_regulated_info("some example string")
    # TODO: Handle 'response' of type GetOrderRegulatedInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderRegulatedInfoErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_order_regulated_info("some example string")
    # TODO: Handle 'response' of type GetOrderRegulatedInfoResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderRegulatedInfoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Walmart Purchase Order ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOrderRegulatedInfoResponse](walmart_apis/models/get_order_regulated_info_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetOrderRegulatedInfoErrorBody](walmart_apis/errors/get_order_regulated_info_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_orders(*, created_after: RFC3339DateTime | None = None, created_before: RFC3339DateTime | None = None, last_updated_after: RFC3339DateTime | None = None, order_statuses: list[OrderStatusOrStr] | None = None, fulfillment_types: list[FulfillmentTypeOrStr] | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetFulfillmentOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns orders matching the given filters. Orders are fulfilled by
sellers (WFS or seller-fulfilled). Maps to Walmart OMS order queries.

### Current limitations (roadmap)

The underlying the Orders service backend does not yet support
every filter declared below. Calls using any of the following will
return `400 Bad Request` with `code=FILTER_NOT_SUPPORTED` and a
human-readable `message` explaining the specific rejection. Phase
2
will lift these one-by-one as the underlying service adds capability.

| Filter | Status today | Reason |
|---|---|---|
| `createdAfter`, `createdBefore` | Rejected (400) | the Orders service does not accept date-range filters at the order level. |
| `lastUpdatedAfter` | Rejected (400) | the underlying service has no order-level update-date index. |
| `orderStatuses` with >1 value | Rejected (400) | the underlying service accepts one status per call; pass a single value or omit to match all. |
| `fulfillmentTypes` | Rejected (400) | the underlying service accepts one shipNodeType per call; multi-type fan-out is Phase 2. |

These parameters remain in the contract (rather than being removed)
so that SDKs generated today stay forward-compatible with the
the roadmap surface — your code keeps compiling, only the runtime
behaviour changes when Phase 2 ships. Until then, omit them or
handle the documented 400 gracefully. The `tools/loadgen-orders.sh --contract`
smoke sweep exercises the rejection contract on every run.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_orders()
    # TODO: Handle 'response' of type GetFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrdersErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_orders()
    # TODO: Handle 'response' of type GetFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrdersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>created_after</code> | <code>RFC3339DateTime \| None</code> | Filter orders created after this date-time (ISO 8601).<br><br>**the roadmap — not yet supported.** Sending this parameter today<br>returns `400 FILTER_NOT_SUPPORTED`; the Orders service does not<br>accept date-range filters at the order level. Tracked by<br>.<br>Retained in the contract so SDKs generated today stay<br>forward-compatible.<br>**Default**: <code>None</code> |
| <code>created_before</code> | <code>RFC3339DateTime \| None</code> | Filter orders created before this date-time (ISO 8601).<br><br>**the roadmap — not yet supported.** See `createdAfter` for the<br>rationale and the tracking ticket.<br>**Default**: <code>None</code> |
| <code>last_updated_after</code> | <code>RFC3339DateTime \| None</code> | Filter orders updated after this date-time (ISO 8601).<br><br>**the roadmap — not yet supported.** Sending this parameter today<br>returns `400 FILTER_NOT_SUPPORTED`; the Orders service has no<br>order-level update-date index. Tracked by<br>.<br>**Default**: <code>None</code> |
| <code>order_statuses</code> | <code>list&#91;[OrderStatusOrStr](walmart_apis/models/enums/order_status.py)&#93; \| None</code> | Filter by order status.<br><br>**the roadmap limitation:** the Orders service accepts AT MOST ONE<br>status per call. Passing multiple values today returns `400<br>FILTER_NOT_SUPPORTED`; pass a single value or omit to match all.<br>Multi-status fan-out tracked by<br>.<br>**Default**: <code>None</code> |
| <code>fulfillment_types</code> | <code>list&#91;[FulfillmentTypeOrStr](walmart_apis/models/enums/fulfillment_type.py)&#93; \| None</code> | Filter by fulfillment type.<br><br>**the roadmap — not yet supported.** Sending this parameter today<br>returns `400 FILTER_NOT_SUPPORTED`; the underlying service accepts one<br>shipNodeType per call and multi-type fan-out is Phase 2. Tracked<br>by .<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>100</code> |
| <code>next_token</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFulfillmentOrderResponse](walmart_apis/models/get_fulfillment_order_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetOrdersErrorBody](walmart_apis/errors/get_orders_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def refund_order_lines(purchase_order_id: str, body: RefundOrderLinesRequest | RefundOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RefundOrderLinesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Walmart-specific write — no Amazon SP-API Orders v0 equivalent
(Amazon refunds live in the Finance API). Mirrors
gmp-orders-mono's legacy `/partner-api/{market}/v3/orders/{po}/refund`
contract, simplified for the v4 surface: a flat `orderLines[]` with
per-line refund amount + reason instead of the legacy three-level
nesting (`orderLines → refunds → refundCharges`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.refund_order_lines(
        "some example string",
        RefundOrderLinesRequest(
            order_lines=[
                RefundOrderLine(line_number="some example string", refund_amount=Money(), refund_type=RefundType.RETURN)
            ],
        ),
    )
    # TODO: Handle 'response' of type RefundOrderLinesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RefundOrderLinesErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.refund_order_lines(
        "some example string",
        RefundOrderLinesRequest(
            order_lines=[
                RefundOrderLine(line_number="some example string", refund_amount=Money(), refund_type=RefundType.RETURN)
            ],
        ),
    )
    # TODO: Handle 'response' of type RefundOrderLinesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RefundOrderLinesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[RefundOrderLinesRequest](walmart_apis/models/refund_order_lines_request.py) \| [RefundOrderLinesRequestDict](walmart_apis/models/refund_order_lines_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[RefundOrderLinesResponse](walmart_apis/models/refund_order_lines_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[RefundOrderLinesErrorBody](walmart_apis/errors/refund_order_lines_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ship_order_lines(purchase_order_id: str, body: ShipOrderLinesRequest | ShipOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ShipOrderLinesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.ship_order_lines(
        "some example string",
        ShipOrderLinesRequest(
            order_lines=[
                ShipOrderLine(
                    line_number="some example string",
                    tracking_info=TrackingInfo(
                        carrier=CarrierName.UPS,
                        tracking_number="some example string",
                        shipped_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
                    ),
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type ShipOrderLinesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ShipOrderLinesErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.ship_order_lines(
        "some example string",
        ShipOrderLinesRequest(
            order_lines=[
                ShipOrderLine(
                    line_number="some example string",
                    tracking_info=TrackingInfo(
                        carrier=CarrierName.UPS,
                        tracking_number="some example string",
                        shipped_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
                    ),
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type ShipOrderLinesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ShipOrderLinesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[ShipOrderLinesRequest](walmart_apis/models/ship_order_lines_request.py) \| [ShipOrderLinesRequestDict](walmart_apis/models/ship_order_lines_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ShipOrderLinesResponse](walmart_apis/models/ship_order_lines_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ShipOrderLinesErrorBody](walmart_apis/errors/ship_order_lines_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ship_order_multi_package(purchase_order_id: str, body: MultiPackageShipRequest | MultiPackageShipRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> MultiPackageShipResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Walmart-specific extension of `/shipping`. Each package carries
its own tracking number, carrier, dimensions, and the order
lines it covers. Maps onto FMS's existing `shipments[]` envelope
(one FMS shipment per v4 package). Inspired by gmp-orders-mono's
`shipOrderV2` (multiPackageShipping) operation; we hoist
`packages[]` to the top level rather than nesting it under each
line so the request stays self-evidently package-oriented.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.ship_order_multi_package(
        "some example string",
        MultiPackageShipRequest(
            packages=[
                ShipPackage(
                    tracking_info=TrackingInfo(
                        carrier=CarrierName.UPS,
                        tracking_number="some example string",
                        shipped_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
                    ),
                    lines=[ShipPackageLine(line_number="some example string")],
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type MultiPackageShipResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ShipOrderMultiPackageErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.ship_order_multi_package(
        "some example string",
        MultiPackageShipRequest(
            packages=[
                ShipPackage(
                    tracking_info=TrackingInfo(
                        carrier=CarrierName.UPS,
                        tracking_number="some example string",
                        shipped_date=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc),
                    ),
                    lines=[ShipPackageLine(line_number="some example string")],
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type MultiPackageShipResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ShipOrderMultiPackageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[MultiPackageShipRequest](walmart_apis/models/multi_package_ship_request.py) \| [MultiPackageShipRequestDict](walmart_apis/models/multi_package_ship_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[MultiPackageShipResponse](walmart_apis/models/multi_package_ship_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ShipOrderMultiPackageErrorBody](walmart_apis/errors/ship_order_multi_package_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_shipment_status(purchase_order_id: str, body: UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UpdateShipmentStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Records a non-terminal shipment-lifecycle event for an order
(ready for pickup, picked up, in transit, out for delivery).
Use the dedicated `/deliver` endpoint for terminal delivery —
it carries proof-of-delivery semantics this endpoint does not.

Amazon SP-API Orders v0 `updateShipmentStatus` parity.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.update_shipment_status(
        "some example string",
        UpdateShipmentStatusRequest(
            shipment_status=ShipmentStatus1.READY_FOR_PICKUP,
            order_lines=[UpdateShipmentStatusLine(line_number="some example string")],
        ),
    )
    # TODO: Handle 'response' of type UpdateShipmentStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateShipmentStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.update_shipment_status(
        "some example string",
        UpdateShipmentStatusRequest(
            shipment_status=ShipmentStatus1.READY_FOR_PICKUP,
            order_lines=[UpdateShipmentStatusLine(line_number="some example string")],
        ),
    )
    # TODO: Handle 'response' of type UpdateShipmentStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateShipmentStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UpdateShipmentStatusRequest](walmart_apis/models/update_shipment_status_request.py) \| [UpdateShipmentStatusRequestDict](walmart_apis/models/update_shipment_status_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UpdateShipmentStatusResponse](walmart_apis/models/update_shipment_status_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateShipmentStatusErrorBody](walmart_apis/errors/update_shipment_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_verification_status(purchase_order_id: str, body: UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UpdateVerificationStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Parity with Amazon SP-API Orders v0 `updateVerificationStatus`. The
seller calls this after delivering a regulated-item order to
record whether the buyer's identity / age was verified at the
doorstep. An APPROVED status releases the order for settlement;
REJECTED requires a `rejectionReason` and triggers downstream
return-processing.

Gated by the CCM-managed `orders.features.regulatedInfoEnabled`
kill-switch (live-refreshable, parity with the cancel kill-switch).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.update_verification_status(
        "some example string", UpdateVerificationStatusRequest(verification_status=VerificationStatus.APPROVED)
    )
    # TODO: Handle 'response' of type UpdateVerificationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateVerificationStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.update_verification_status(
        "some example string", UpdateVerificationStatusRequest(verification_status=VerificationStatus.APPROVED)
    )
    # TODO: Handle 'response' of type UpdateVerificationStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateVerificationStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>purchase_order_id</code> | <code>str</code> | Walmart Purchase Order ID |
| <code>body</code> | <code>[UpdateVerificationStatusRequest](walmart_apis/models/update_verification_status_request.py) \| [UpdateVerificationStatusRequestDict](walmart_apis/models/update_verification_status_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UpdateVerificationStatusResponse](walmart_apis/models/update_verification_status_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateVerificationStatusErrorBody](walmart_apis/errors/update_verification_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500, 503 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Payouts

> Source: [Payouts](walmart_apis/apis/payouts.py)

<details>
<summary><code>def configure_auto_payout(body: DisbursementsV4PaymentAutoPayoutRequest | DisbursementsV4PaymentAutoPayoutRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PayoutStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables or disables automatic scheduled payouts for the authenticated seller.
When enabled, payouts are triggered automatically on the standard settlement
cadence. Returns updated payout status. Requires disbursements:write scope.
Delegates to GMPPaymentsPlatform (Phase 5).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payouts.configure_auto_payout(DisbursementsV4PaymentAutoPayoutRequest(enabled=True))
    # TODO: Handle 'response' of type PayoutStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfigureAutoPayoutErrorBody
```

**Async**

```python
try:
    response = await async_client.payouts.configure_auto_payout(DisbursementsV4PaymentAutoPayoutRequest(enabled=True))
    # TODO: Handle 'response' of type PayoutStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfigureAutoPayoutErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DisbursementsV4PaymentAutoPayoutRequest](walmart_apis/models/disbursements_v4_payment_auto_payout_request.py) \| [DisbursementsV4PaymentAutoPayoutRequestDict](walmart_apis/models/disbursements_v4_payment_auto_payout_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PayoutStatusResponse](walmart_apis/models/payout_status_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfigureAutoPayoutErrorBody](walmart_apis/errors/configure_auto_payout_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_annual_statement_opts(*, request_options: RequestOptionsOrDict | None = None) -> AnnualStatementOptsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns whether the authenticated seller is opted in to annual statement
generation and the current statement year. Delegates to GMPPaymentsPlatform
GET /annualStatementOpts/{partnerId}.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payouts.get_annual_statement_opts()
    # TODO: Handle 'response' of type AnnualStatementOptsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnnualStatementOptsErrorBody
```

**Async**

```python
try:
    response = await async_client.payouts.get_annual_statement_opts()
    # TODO: Handle 'response' of type AnnualStatementOptsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAnnualStatementOptsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[AnnualStatementOptsResponse](walmart_apis/models/annual_statement_opts_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetAnnualStatementOptsErrorBody](walmart_apis/errors/get_annual_statement_opts_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_faster_payout_eligibility(*, request_options: RequestOptionsOrDict | None = None) -> FasterPayoutEligibilityResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns whether the authenticated seller is eligible for an on-demand
faster payout, along with the approved amount and any ineligibility reason.
Delegates to GMPPaymentsPlatform GET /fasterPayout/eligibility/{partnerId}.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payouts.get_faster_payout_eligibility()
    # TODO: Handle 'response' of type FasterPayoutEligibilityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFasterPayoutEligibilityErrorBody
```

**Async**

```python
try:
    response = await async_client.payouts.get_faster_payout_eligibility()
    # TODO: Handle 'response' of type FasterPayoutEligibilityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFasterPayoutEligibilityErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[FasterPayoutEligibilityResponse](walmart_apis/models/faster_payout_eligibility_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFasterPayoutEligibilityErrorBody](walmart_apis/errors/get_faster_payout_eligibility_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_payment_status(*, request_options: RequestOptionsOrDict | None = None) -> PayoutStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the current payout status for the authenticated seller, including
scheduled payout date, amount, and lifecycle state (Pending, Processing,
Completed, Failed, OnHold). Delegates to GMPPaymentsPlatform (Phase 5).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payouts.get_payment_status()
    # TODO: Handle 'response' of type PayoutStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPaymentStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.payouts.get_payment_status()
    # TODO: Handle 'response' of type PayoutStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPaymentStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[PayoutStatusResponse](walmart_apis/models/payout_status_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetPaymentStatusErrorBody](walmart_apis/errors/get_payment_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def initiate_faster_payout(*, request_options: RequestOptionsOrDict | None = None) -> InitiatePayoutResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Triggers an immediate on-demand payout for the authenticated seller,
bypassing the standard settlement schedule. Returns the payout ID and
initial status. Requires disbursements:write scope.
Delegates to GMPPaymentsPlatform (Phase 5).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payouts.initiate_faster_payout()
    # TODO: Handle 'response' of type InitiatePayoutResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InitiateFasterPayoutErrorBody
```

**Async**

```python
try:
    response = await async_client.payouts.initiate_faster_payout()
    # TODO: Handle 'response' of type InitiatePayoutResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type InitiateFasterPayoutErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InitiatePayoutResponse](walmart_apis/models/initiate_payout_response.py)</code> -- Payout initiated

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[InitiateFasterPayoutErrorBody](walmart_apis/errors/initiate_faster_payout_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 409, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ProductTypeDefinitions

> Source: [ProductTypeDefinitions](walmart_apis/apis/product_type_definitions.py)

<details>
<summary><code>def get_definitions_product_type(product_type: str, *, seller_id: str | None = None, locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ProductTypeDefinition</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Placeholder — not yet implemented.**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_type_definitions.get_definitions_product_type("some example string")
    # TODO: Handle 'response' of type ProductTypeDefinition
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDefinitionsProductTypeErrorBody
```

**Async**

```python
try:
    response = await async_client.product_type_definitions.get_definitions_product_type("some example string")
    # TODO: Handle 'response' of type ProductTypeDefinition
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDefinitionsProductTypeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>product_type</code> | <code>str</code> | Value sent with the request. |
| <code>seller_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"en_US"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductTypeDefinition](walmart_apis/models/product_type_definition.py)</code> -- Product type definition schema

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetDefinitionsProductTypeErrorBody](walmart_apis/errors/get_definitions_product_type_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_definitions_product_types(*, keywords: str | None = None, item_name: str | None = None, locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ProductTypeList</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Placeholder — not yet implemented.**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_type_definitions.search_definitions_product_types()
    # TODO: Handle 'response' of type ProductTypeList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchDefinitionsProductTypesErrorBody
```

**Async**

```python
try:
    response = await async_client.product_type_definitions.search_definitions_product_types()
    # TODO: Handle 'response' of type ProductTypeList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchDefinitionsProductTypesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>keywords</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>item_name</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"en_US"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ProductTypeList](walmart_apis/models/product_type_list.py)</code> -- Product type list

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SearchDefinitionsProductTypesErrorBody](walmart_apis/errors/search_definitions_product_types_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Reconciliation

> Source: [Reconciliation](walmart_apis/apis/reconciliation.py)

<details>
<summary><code>def check_download_report_by_period(partner_id: str, date: Date, *, request_options: RequestOptionsOrDict | None = None) -> ReportAvailabilityResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Checks which reconciliation report versions (legacy, v1/WFS) are available
for a given partner and date. Delegates to mp-payment-reporting
GET /v3/report/reconreport/reconReportAvailability.
Note: the upstream date param is named `date` (not `reportDate`).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reconciliation.check_download_report_by_period("some example string", date(2024, 1, 15))
    # TODO: Handle 'response' of type ReportAvailabilityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckDownloadReportByPeriodErrorBody
```

**Async**

```python
try:
    response = await async_client.reconciliation.check_download_report_by_period(
        "some example string", date(2024, 1, 15)
    )
    # TODO: Handle 'response' of type ReportAvailabilityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckDownloadReportByPeriodErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
| <code>date</code> | <code>Date</code> | Report date in yyyy-MM-dd format |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReportAvailabilityResponse](walmart_apis/models/report_availability_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CheckDownloadReportByPeriodErrorBody](walmart_apis/errors/check_download_report_by_period_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_reconciliation_report(partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None) -> FileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Downloads a reconciliation report ZIP for the given partner and date.
Delegates to mp-payment-reporting GET /v1/mt/report/reconreport/reconFile (Azure MT storage).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reconciliation.download_reconciliation_report("some example string", "some example string")
    # TODO: Handle 'response' of type FileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadReconciliationReportErrorBody
```

**Async**

```python
try:
    response = await async_client.reconciliation.download_reconciliation_report(
        "some example string", "some example string"
    )
    # TODO: Handle 'response' of type AsyncFileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadReconciliationReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
| <code>report_date</code> | <code>str</code> | Report date in MMddyyyy format (e.g. 06172026) |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>FileResponse</code> -- ZIP file stream

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[DownloadReconciliationReportErrorBody](walmart_apis/errors/download_reconciliation_report_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 404, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_reconciliation_dates(partner_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ReportAvailabilityResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the set of available reconciliation report dates for a partner.
Delegates to mp-payment-reporting GET /v3/report/reconreport/availableReconFiles.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reconciliation.list_reconciliation_dates("some example string")
    # TODO: Handle 'response' of type ReportAvailabilityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListReconciliationDatesErrorBody
```

**Async**

```python
try:
    response = await async_client.reconciliation.list_reconciliation_dates("some example string")
    # TODO: Handle 'response' of type ReportAvailabilityResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListReconciliationDatesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReportAvailabilityResponse](walmart_apis/models/report_availability_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListReconciliationDatesErrorBody](walmart_apis/errors/list_reconciliation_dates_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ReportSchedules

> Source: [ReportSchedules](walmart_apis/apis/report_schedules.py)

<details>
<summary><code>def cancel_report_schedule(report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelReportScheduleResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.report_schedules.cancel_report_schedule("some example string")
    # TODO: Handle 'response' of type CancelReportScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelReportScheduleErrorBody
```

**Async**

```python
try:
    response = await async_client.report_schedules.cancel_report_schedule("some example string")
    # TODO: Handle 'response' of type CancelReportScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelReportScheduleErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_schedule_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelReportScheduleResponse](walmart_apis/models/cancel_report_schedule_response.py)</code> -- Schedule cancelled

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelReportScheduleErrorBody](walmart_apis/errors/cancel_report_schedule_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_report_schedule(body: CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateReportScheduleResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.report_schedules.create_report_schedule(
        CreateReportScheduleSpecification(report_type="some example string", period=Period1.PT5_M)
    )
    # TODO: Handle 'response' of type CreateReportScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateReportScheduleErrorBody
```

**Async**

```python
try:
    response = await async_client.report_schedules.create_report_schedule(
        CreateReportScheduleSpecification(report_type="some example string", period=Period1.PT5_M)
    )
    # TODO: Handle 'response' of type CreateReportScheduleResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateReportScheduleErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateReportScheduleSpecification](walmart_apis/models/create_report_schedule_specification.py) \| [CreateReportScheduleSpecificationDict](walmart_apis/models/create_report_schedule_specification.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateReportScheduleResponse](walmart_apis/models/create_report_schedule_response.py)</code> -- Schedule created

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateReportScheduleErrorBody](walmart_apis/errors/create_report_schedule_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_report_schedule(report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ReportSchedule</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.report_schedules.get_report_schedule("some example string")
    # TODO: Handle 'response' of type ReportSchedule
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportScheduleErrorBody
```

**Async**

```python
try:
    response = await async_client.report_schedules.get_report_schedule("some example string")
    # TODO: Handle 'response' of type ReportSchedule
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportScheduleErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_schedule_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReportSchedule](walmart_apis/models/report_schedule.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetReportScheduleErrorBody](walmart_apis/errors/get_report_schedule_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_report_schedules(*, report_types: list[ReportType1OrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> GetReportSchedulesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.report_schedules.get_report_schedules()
    # TODO: Handle 'response' of type GetReportSchedulesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportSchedulesErrorBody
```

**Async**

```python
try:
    response = await async_client.report_schedules.get_report_schedules()
    # TODO: Handle 'response' of type GetReportSchedulesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportSchedulesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_types</code> | <code>list&#91;[ReportType1OrStr](walmart_apis/models/enums/report_type1.py)&#93; \| None</code> | Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime availability is CCM-controlled; consult PRP docs for current PROD-enabled types.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetReportSchedulesResponse](walmart_apis/models/get_report_schedules_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetReportSchedulesErrorBody](walmart_apis/errors/get_report_schedules_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Reports

> Source: [Reports](walmart_apis/apis/reports.py)

<details>
<summary><code>def cancel_report(report_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelReportResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reports.cancel_report("some example string")
    # TODO: Handle 'response' of type CancelReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelReportErrorBody
```

**Async**

```python
try:
    response = await async_client.reports.cancel_report("some example string")
    # TODO: Handle 'response' of type CancelReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelReportResponse](walmart_apis/models/cancel_report_response.py)</code> -- Report cancelled

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelReportErrorBody](walmart_apis/errors/cancel_report_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_report(body: CreateReportSpecification | CreateReportSpecificationDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateReportResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Submits a report request. Poll `GET /reports/{reportId}` for status.
Report type taxonomy TBD — coordinate with Pod 5 for financial reports.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reports.create_report(CreateReportSpecification(report_type=ReportType.ITEM))
    # TODO: Handle 'response' of type CreateReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateReportErrorBody
```

**Async**

```python
try:
    response = await async_client.reports.create_report(CreateReportSpecification(report_type=ReportType.ITEM))
    # TODO: Handle 'response' of type CreateReportResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateReportSpecification](walmart_apis/models/create_report_specification.py) \| [CreateReportSpecificationDict](walmart_apis/models/create_report_specification.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateReportResponse](walmart_apis/models/create_report_response.py)</code> -- Report request accepted

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateReportErrorBody](walmart_apis/errors/create_report_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_new_report(partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None) -> FileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Downloads the current-format settlement summary report ZIP.
Delegates to mp-payment-reporting GET /v3/report/reconreport/v1/reconFile (Swift v1 storage).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reports.download_new_report("some example string", "some example string")
    # TODO: Handle 'response' of type FileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadNewReportErrorBody
```

**Async**

```python
try:
    response = await async_client.reports.download_new_report("some example string", "some example string")
    # TODO: Handle 'response' of type AsyncFileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadNewReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
| <code>report_date</code> | <code>str</code> | Report date in MMddyyyy format (e.g. 06172026) |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>FileResponse</code> -- ZIP file stream

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[DownloadNewReportErrorBody](walmart_apis/errors/download_new_report_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_old_report(partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None) -> FileResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Downloads the legacy-format settlement summary report ZIP.
Delegates to mp-payment-reporting GET /v3/report/reconreport/reconFile (legacy Swift storage).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reports.download_old_report("some example string", "some example string")
    # TODO: Handle 'response' of type FileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadOldReportErrorBody
```

**Async**

```python
try:
    response = await async_client.reports.download_old_report("some example string", "some example string")
    # TODO: Handle 'response' of type AsyncFileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadOldReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
| <code>report_date</code> | <code>str</code> | Report date in MMddyyyy format (e.g. 06172026) |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>FileResponse</code> -- ZIP file stream

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[DownloadOldReportErrorBody](walmart_apis/errors/download_old_report_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 404, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_report(report_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Report</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reports.get_report("some example string")
    # TODO: Handle 'response' of type Report
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportErrorBody
```

**Async**

```python
try:
    response = await async_client.reports.get_report("some example string")
    # TODO: Handle 'response' of type Report
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Report](walmart_apis/models/report.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetReportErrorBody](walmart_apis/errors/get_report_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_report_document(report_document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ReportDocument</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a pre-signed URL for downloading the completed report.
Do not log the pre-signed URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reports.get_report_document("some example string")
    # TODO: Handle 'response' of type ReportDocument
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportDocumentErrorBody
```

**Async**

```python
try:
    response = await async_client.reports.get_report_document("some example string")
    # TODO: Handle 'response' of type ReportDocument
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportDocumentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_document_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ReportDocument](walmart_apis/models/report_document.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetReportDocumentErrorBody](walmart_apis/errors/get_report_document_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_reports(*, report_types: list[ReportType1OrStr] | None = None, processing_statuses: list[ProcessingStatusOrStr] | None = None, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetReportsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.reports.get_reports()
    # TODO: Handle 'response' of type GetReportsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportsErrorBody
```

**Async**

```python
try:
    response = await async_client.reports.get_reports()
    # TODO: Handle 'response' of type GetReportsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetReportsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>report_types</code> | <code>list&#91;[ReportType1OrStr](walmart_apis/models/enums/report_type1.py)&#93; \| None</code> | Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime availability is CCM-controlled; consult PRP docs for current PROD-enabled types.<br>**Default**: <code>None</code> |
| <code>processing_statuses</code> | <code>list&#91;[ProcessingStatusOrStr](walmart_apis/models/enums/processing_status.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>created_since</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>created_until</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>10</code> |
| <code>next_token</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetReportsResponse](walmart_apis/models/get_reports_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetReportsErrorBody](walmart_apis/errors/get_reports_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Sellers

> Source: [Sellers](walmart_apis/apis/sellers.py)

<details>
<summary><code>def get_account(*, request_options: RequestOptionsOrDict | None = None) -> SellerAccount</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the authenticated seller's account information including
business name, email, account status, and seller type.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sellers.get_account()
    # TODO: Handle 'response' of type SellerAccount
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.sellers.get_account()
    # TODO: Handle 'response' of type SellerAccount
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SellerAccount](walmart_apis/models/seller_account.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetAccountErrorBody](walmart_apis/errors/get_account_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_marketplace_participations(*, request_options: RequestOptionsOrDict | None = None) -> GetMarketplaceParticipationsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the list of marketplaces the authenticated seller participates in
(e.g. Walmart US, Walmart Canada, Walmart Mexico).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sellers.get_marketplace_participations()
    # TODO: Handle 'response' of type GetMarketplaceParticipationsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMarketplaceParticipationsErrorBody
```

**Async**

```python
try:
    response = await async_client.sellers.get_marketplace_participations()
    # TODO: Handle 'response' of type GetMarketplaceParticipationsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMarketplaceParticipationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetMarketplaceParticipationsResponse](walmart_apis/models/get_marketplace_participations_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetMarketplaceParticipationsErrorBody](walmart_apis/errors/get_marketplace_participations_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Settlement

> Source: [Settlement](walmart_apis/apis/settlement.py)

<details>
<summary><code>def list_settlement_details(partner_id: str, report_date: str, *, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> SettlementDetailsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns paginated settlement transaction detail for the given partner and report date.
Contains PII (purchase order IDs). Delegates to mp-payment-reporting
GET /v3/report/reconreport/v1/getJson with offset-based pagination.
nextToken is a Base64-encoded offset into the report file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.settlement.list_settlement_details("some example string", "some example string")
    # TODO: Handle 'response' of type SettlementDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSettlementDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.settlement.list_settlement_details("some example string", "some example string")
    # TODO: Handle 'response' of type SettlementDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSettlementDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
| <code>report_date</code> | <code>str</code> | Report date in MMddyyyy format (e.g. 06172026) |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>10</code> |
| <code>next_token</code> | <code>str \| None</code> | Opaque cursor from a prior response; omit for first page<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SettlementDetailsResponse](walmart_apis/models/settlement_details_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListSettlementDetailsErrorBody](walmart_apis/errors/list_settlement_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_settlement_periods(*, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> SettlementPeriodsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns available settlement period dates for the authenticated seller.
Delegates to mp-payment-reporting GET /v3/report/reconreport/v1/availableReconFiles.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.settlement.list_settlement_periods()
    # TODO: Handle 'response' of type SettlementPeriodsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSettlementPeriodsErrorBody
```

**Async**

```python
try:
    response = await async_client.settlement.list_settlement_periods()
    # TODO: Handle 'response' of type SettlementPeriodsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSettlementPeriodsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>10</code> |
| <code>next_token</code> | <code>str \| None</code> | Opaque cursor from a prior response; omit for first page<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SettlementPeriodsResponse](walmart_apis/models/settlement_periods_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListSettlementPeriodsErrorBody](walmart_apis/errors/list_settlement_periods_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_transactions(*, page_size: int | None = 10, next_token: str | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None) -> TransactionSearchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of payment transactions for the authenticated seller
filtered by optional date range. Contains PII (purchase order IDs).
Delegates to GMPPaymentsPlatform (Phase 5).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.settlement.search_transactions()
    # TODO: Handle 'response' of type TransactionSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchTransactionsErrorBody
```

**Async**

```python
try:
    response = await async_client.settlement.search_transactions()
    # TODO: Handle 'response' of type TransactionSearchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchTransactionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>10</code> |
| <code>next_token</code> | <code>str \| None</code> | Opaque cursor from a prior response; omit for first page<br>**Default**: <code>None</code> |
| <code>posted_after</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>posted_before</code> | <code>RFC3339DateTime \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TransactionSearchResponse](walmart_apis/models/transaction_search_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SearchTransactionsErrorBody](walmart_apis/errors/search_transactions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Uploads

> Source: [Uploads](walmart_apis/apis/uploads.py)

<details>
<summary><code>def create_upload_destination_for_resource(resource: ResourceOrStr, content_type: ContentType1OrStr, marketplace_ids: list[str], content_md5: str, *, request_options: RequestOptionsOrDict | None = None) -> CreateUploadDestinationResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a pre-signed URL and upload destination ID for uploading
a document for the given resource (e.g. feeds, reports).
**Do not log the pre-signed URL — it contains temporary credentials.**

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.uploads.create_upload_destination_for_resource(
        Resource.FEEDS, ContentType1.TEXT_XML_CHARSET_UTF_8, ["some example string"], "some example string"
    )
    # TODO: Handle 'response' of type CreateUploadDestinationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateUploadDestinationForResourceErrorBody
```

**Async**

```python
try:
    response = await async_client.uploads.create_upload_destination_for_resource(
        Resource.FEEDS, ContentType1.TEXT_XML_CHARSET_UTF_8, ["some example string"], "some example string"
    )
    # TODO: Handle 'response' of type CreateUploadDestinationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateUploadDestinationForResourceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>resource</code> | <code>[ResourceOrStr](walmart_apis/models/enums/resource.py)</code> | The resource type for the upload destination (e.g. feeds) |
| <code>content_type</code> | <code>[ContentType1OrStr](walmart_apis/models/enums/content_type1.py)</code> | MIME type of the content to be uploaded |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Value sent with the request. |
| <code>content_md5</code> | <code>str</code> | MD5 hash of the content to be uploaded, encoded as base64 |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateUploadDestinationResponse](walmart_apis/models/create_upload_destination_response.py)</code> -- Upload destination created

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateUploadDestinationForResourceErrorBody](walmart_apis/errors/create_upload_destination_for_resource_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WfsInventory

> Source: [WfsInventory](walmart_apis/apis/wfs_inventory.py)

<details>
<summary><code>def get_wfs_inventory_items(*, skus: str | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetWfsInventoryResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns inventory for items managed by Walmart Fulfillment Services (WFS).
Includes stock health, age buckets, and demand-intelligence fields
not available on seller-fulfilled inventory.

**Rate limit:** 300 items per page maximum.
Requests retrieving more than 100 items per page will receive
`X-RateLimit-Limit` and `X-RateLimit-Remaining` headers in the response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inventory.get_wfs_inventory_items()
    # TODO: Handle 'response' of type GetWfsInventoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWfsInventoryItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inventory.get_wfs_inventory_items()
    # TODO: Handle 'response' of type GetWfsInventoryResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetWfsInventoryItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>skus</code> | <code>str \| None</code> | Comma-separated seller SKUs to filter (max 50). Omit to return all WFS items.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Value sent with the request.<br>**Default**: <code>100</code> |
| <code>next_token</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetWfsInventoryResponse](walmart_apis/models/get_wfs_inventory_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetWfsInventoryItemsErrorBody](walmart_apis/errors/get_wfs_inventory_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Messaging

> Source: [Messaging](walmart_apis/apis/messaging.py)

<details>
<summary><code>def create_warranty(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.create_warranty("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWarrantyErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.create_warranty("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateWarrantyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateWarrantyErrorBody](walmart_apis/errors/create_warranty_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_attributes(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.get_attributes("some example string", ["some example string"])
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAttributesErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.get_attributes("some example string", ["some example string"])
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAttributesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetAttributesErrorBody](walmart_apis/errors/get_attributes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_customization_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.confirm_customization_details("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmCustomizationDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.confirm_customization_details(
        "some example string", ["some example string"], {}
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmCustomizationDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmCustomizationDetailsErrorBody](walmart_apis/errors/confirm_customization_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_confirm_delivery_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.create_confirm_delivery_details("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConfirmDeliveryDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.create_confirm_delivery_details(
        "some example string", ["some example string"], {}
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConfirmDeliveryDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateConfirmDeliveryDetailsErrorBody](walmart_apis/errors/create_confirm_delivery_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_confirm_order_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.create_confirm_order_details("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConfirmOrderDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.create_confirm_order_details(
        "some example string", ["some example string"], {}
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConfirmOrderDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateConfirmOrderDetailsErrorBody](walmart_apis/errors/create_confirm_order_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_confirm_service_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.create_confirm_service_details("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConfirmServiceDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.create_confirm_service_details(
        "some example string", ["some example string"], {}
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConfirmServiceDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateConfirmServiceDetailsErrorBody](walmart_apis/errors/create_confirm_service_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_digital_access_key(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.create_digital_access_key("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateDigitalAccessKeyErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.create_digital_access_key(
        "some example string", ["some example string"], {}
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateDigitalAccessKeyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateDigitalAccessKeyErrorBody](walmart_apis/errors/create_digital_access_key_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_legal_disclosure(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.create_legal_disclosure("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateLegalDisclosureErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.create_legal_disclosure("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateLegalDisclosureErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateLegalDisclosureErrorBody](walmart_apis/errors/create_legal_disclosure_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_unexpected_problem(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.create_unexpected_problem("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateUnexpectedProblemErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.create_unexpected_problem(
        "some example string", ["some example string"], {}
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateUnexpectedProblemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateUnexpectedProblemErrorBody](walmart_apis/errors/create_unexpected_problem_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_messaging_actions_for_order(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.get_messaging_actions_for_order("some example string", ["some example string"])
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMessagingActionsForOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.get_messaging_actions_for_order(
        "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMessagingActionsForOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This specifies the order for which you want a list of available message types. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetMessagingActionsForOrderErrorBody](walmart_apis/errors/get_messaging_actions_for_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_invoice(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.messaging.send_invoice("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendInvoiceErrorBody
```

**Async**

```python
try:
    response = await async_client.messaging.send_invoice("some example string", ["some example string"], {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendInvoiceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | A marketplace order identifier. This identifies the order for which a message is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This identifies the marketplace in which the order was placed. You can only specify one market |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SendInvoiceErrorBody](walmart_apis/errors/send_invoice_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Notifications

> Source: [Notifications](walmart_apis/apis/notifications.py)

<details>
<summary><code>def create_destination(body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Channel</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.create_destination({})
    # TODO: Handle 'response' of type Channel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateDestinationErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.create_destination({})
    # TODO: Handle 'response' of type Channel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateDestinationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Channel](walmart_apis/models/channel.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateDestinationErrorBody](walmart_apis/errors/create_destination_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_subscription(notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.create_subscription("some example string", {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.create_subscription("some example string", {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>notification_type</code> | <code>str</code> | The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH. |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateSubscriptionErrorBody](walmart_apis/errors/create_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_destination(destination_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Channel</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.delete_destination("some example string")
    # TODO: Handle 'response' of type Channel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteDestinationErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.delete_destination("some example string")
    # TODO: Handle 'response' of type Channel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteDestinationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>destination_id</code> | <code>str</code> | The identifier for the destination that you want to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Channel](walmart_apis/models/channel.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[DeleteDestinationErrorBody](walmart_apis/errors/delete_destination_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscription_by_id(subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.delete_subscription_by_id("some example string", "some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteSubscriptionByIdErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.delete_subscription_by_id("some example string", "some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteSubscriptionByIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The identifier for the subscription that you want to delete. |
| <code>notification_type</code> | <code>str</code> | The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[DeleteSubscriptionByIdErrorBody](walmart_apis/errors/delete_subscription_by_id_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_destination(destination_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Channel</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.get_destination("some example string")
    # TODO: Handle 'response' of type Channel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDestinationErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.get_destination("some example string")
    # TODO: Handle 'response' of type Channel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDestinationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>destination_id</code> | <code>str</code> | The identifier generated when you created the destination. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Channel](walmart_apis/models/channel.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetDestinationErrorBody](walmart_apis/errors/get_destination_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_destinations(*, request_options: RequestOptionsOrDict | None = None) -> ChannelList</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.get_destinations()
    # TODO: Handle 'response' of type ChannelList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDestinationsErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.get_destinations()
    # TODO: Handle 'response' of type ChannelList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDestinationsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ChannelList](walmart_apis/models/channel_list.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetDestinationsErrorBody](walmart_apis/errors/get_destinations_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_subscription(notification_type: str, *, payload_version: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.get_subscription("some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSubscriptionErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.get_subscription("some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSubscriptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>notification_type</code> | <code>str</code> | The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH. |
| <code>payload_version</code> | <code>str \| None</code> | The version of the payload object to be used in the notification.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetSubscriptionErrorBody](walmart_apis/errors/get_subscription_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_subscription_by_id(subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.get_subscription_by_id("some example string", "some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSubscriptionByIdErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.get_subscription_by_id("some example string", "some example string")
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSubscriptionByIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The identifier for the subscription that you want to get. |
| <code>notification_type</code> | <code>str</code> | The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetSubscriptionByIdErrorBody](walmart_apis/errors/get_subscription_by_id_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_test_notification(notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.notifications.send_test_notification("some example string", {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendTestNotificationErrorBody
```

**Async**

```python
try:
    response = await async_client.notifications.send_test_notification("some example string", {})
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendTestNotificationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>notification_type</code> | <code>str</code> | The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH. |
| <code>body</code> | <code>Any</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SendTestNotificationErrorBody](walmart_apis/errors/send_test_notification_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ProductFees

> Source: [ProductFees](walmart_apis/apis/product_fees.py)

<details>
<summary><code>def get_my_fees_estimate_for_item(walmart_item_id: str, body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetMyFeesEstimateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an estimated fee for a single item identified by Walmart Item ID.
Walmart Item ID replaces the SP-API ASIN path parameter.

SP-API equivalent: `getMyFeesEstimateForASIN` (identifier changed from
ASIN to Walmart Item ID; request/response shape is otherwise 1:1).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_fees.get_my_fees_estimate_for_item("some example string", GetMyFeesEstimateRequest())
    # TODO: Handle 'response' of type GetMyFeesEstimateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMyFeesEstimateForItemErrorBody
```

**Async**

```python
try:
    response = await async_client.product_fees.get_my_fees_estimate_for_item(
        "some example string", GetMyFeesEstimateRequest()
    )
    # TODO: Handle 'response' of type GetMyFeesEstimateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMyFeesEstimateForItemErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>walmart_item_id</code> | <code>str</code> | The Walmart Item ID of the item. Replaces SP-API ASIN. |
| <code>body</code> | <code>[GetMyFeesEstimateRequest](walmart_apis/models/get_my_fees_estimate_request.py) \| [GetMyFeesEstimateRequestDict](walmart_apis/models/get_my_fees_estimate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetMyFeesEstimateResponse](walmart_apis/models/get_my_fees_estimate_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetMyFeesEstimateForItemErrorBody](walmart_apis/errors/get_my_fees_estimate_for_item_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_my_fees_estimate_for_sku(seller_sku: str, marketplace_id: str, body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetMyFeesEstimateResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an estimated fee for a seller listing identified by Seller SKU.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_fees.get_my_fees_estimate_for_sku(
        "some example string", "some example string", GetMyFeesEstimateRequest()
    )
    # TODO: Handle 'response' of type GetMyFeesEstimateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMyFeesEstimateForSkuErrorBody
```

**Async**

```python
try:
    response = await async_client.product_fees.get_my_fees_estimate_for_sku(
        "some example string", "some example string", GetMyFeesEstimateRequest()
    )
    # TODO: Handle 'response' of type GetMyFeesEstimateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMyFeesEstimateForSkuErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_sku</code> | <code>str</code> | The seller's SKU for the listing. Scoped to the authenticated seller. |
| <code>marketplace_id</code> | <code>str</code> | Marketplace identifier. |
| <code>body</code> | <code>[GetMyFeesEstimateRequest](walmart_apis/models/get_my_fees_estimate_request.py) \| [GetMyFeesEstimateRequestDict](walmart_apis/models/get_my_fees_estimate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetMyFeesEstimateResponse](walmart_apis/models/get_my_fees_estimate_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetMyFeesEstimateForSkuErrorBody](walmart_apis/errors/get_my_fees_estimate_for_sku_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_my_fees_estimates(body: list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict], *, request_options: RequestOptionsOrDict | None = None) -> list[FeesEstimateResult]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns estimated Walmart fees for a list of items identified by
Walmart Item ID or Seller SKU.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_fees.get_my_fees_estimates(
        [
            FeesEstimateByIdRequest(
                id_type=IdType.WALMART_ITEM_ID,
                id_value="some example string",
                fees_estimate_request=FeesEstimateRequest(
                    marketplace_id="some example string",
                    is_walmart_fulfilled=True,
                    price_to_estimate_fees=PriceToEstimateFees(listing_price=MoneyType1()),
                ),
            ),
        ],
    )
    # TODO: Handle 'response' of type list[FeesEstimateResult]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMyFeesEstimatesErrorBody
```

**Async**

```python
try:
    response = await async_client.product_fees.get_my_fees_estimates(
        [
            FeesEstimateByIdRequest(
                id_type=IdType.WALMART_ITEM_ID,
                id_value="some example string",
                fees_estimate_request=FeesEstimateRequest(
                    marketplace_id="some example string",
                    is_walmart_fulfilled=True,
                    price_to_estimate_fees=PriceToEstimateFees(listing_price=MoneyType1()),
                ),
            ),
        ],
    )
    # TODO: Handle 'response' of type list[FeesEstimateResult]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetMyFeesEstimatesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>list&#91;[FeesEstimateByIdRequest](walmart_apis/models/fees_estimate_by_id_request.py) \| [FeesEstimateByIdRequestDict](walmart_apis/models/fees_estimate_by_id_request.py)&#93;</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[FeesEstimateResult](walmart_apis/models/fees_estimate_result.py)&#93;</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetMyFeesEstimatesErrorBody](walmart_apis/errors/get_my_fees_estimates_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ProductPricing

> Source: [ProductPricing](walmart_apis/apis/product_pricing.py)

<details>
<summary><code>def get_competitive_pricing(marketplace_id: str, *, item_type: ItemTypeOrStr = ItemType.SKU, skus: list[str] | None = None, walmart_item_ids: list[str] | None = None, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetPricingResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns competitive pricing information for a seller's offer listings based on seller SKU or Walmart Item ID .

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_competitive_pricing("some example string", item_type=ItemType.WALMART_ITEM_ID)
    # TODO: Handle 'response' of type GetPricingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCompetitivePricingErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_competitive_pricing(
        "some example string", item_type=ItemType.WALMART_ITEM_ID
    )
    # TODO: Handle 'response' of type GetPricingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCompetitivePricingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>marketplace_id</code> | <code>str</code> | A marketplace identifier. Specifies the marketplace for which prices are returned. |
| <code>item_type</code> | <code>[ItemTypeOrStr](walmart_apis/models/enums/item_type.py)</code> | Indicates whether Walmart Item ID values or seller SKU values are used to identify items.<br>**Default**: <code>ItemType.SKU</code> |
| <code>skus</code> | <code>list&#91;str&#93; \| None</code> | A list of up to twenty seller SKU values used to identify items in the given marketplace.<br>**Default**: <code>None</code> |
| <code>walmart_item_ids</code> | <code>list&#91;str&#93; \| None</code> | A list of up to twenty Walmart Item ID values used to identify items in the given marketplace.<br>**Default**: <code>None</code> |
| <code>customer_type</code> | <code>[CustomerTypeOrStr](walmart_apis/models/enums/customer_type.py) \| None</code> | Indicates whether to request pricing information from the point of view of Consumer or Business buyers. Default is Consumer.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetPricingResponse](walmart_apis/models/get_pricing_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetCompetitivePricingErrorBody](walmart_apis/errors/get_competitive_pricing_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[Error3](walmart_apis/models/error3.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_competitive_summary(body: CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CompetitiveSummaryBatchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Planned — not yet available in production.** Returns competitive summary including featured buying options and lowest priced offers
for a batch of Walmart Item IDs .

**Phase 1 stub** — no upstream data source identified.
Returns HTTP 501 until an upstream is confirmed.
Track: .

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_competitive_summary(CompetitiveSummaryBatchRequest())
    # TODO: Handle 'response' of type CompetitiveSummaryBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCompetitiveSummaryErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_competitive_summary(CompetitiveSummaryBatchRequest())
    # TODO: Handle 'response' of type CompetitiveSummaryBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCompetitiveSummaryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CompetitiveSummaryBatchRequest](walmart_apis/models/competitive_summary_batch_request.py) \| [CompetitiveSummaryBatchRequestDict](walmart_apis/models/competitive_summary_batch_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CompetitiveSummaryBatchResponse](walmart_apis/models/competitive_summary_batch_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetCompetitiveSummaryErrorBody](walmart_apis/errors/get_competitive_summary_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[Error3](walmart_apis/models/error3.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_featured_offer_expected_price_batch(body: GetFeaturedOfferExpectedPriceBatchRequest | GetFeaturedOfferExpectedPriceBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetFeaturedOfferExpectedPriceBatchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Planned — not yet available in production.** Returns the featured offer expected price (FOEP) for a batch of seller SKUs.

**Phase 1 stub** — no upstream data source identified.
Returns HTTP 501 until an upstream is confirmed.
Track: .

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_featured_offer_expected_price_batch(
        GetFeaturedOfferExpectedPriceBatchRequest()
    )
    # TODO: Handle 'response' of type GetFeaturedOfferExpectedPriceBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeaturedOfferExpectedPriceBatchErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_featured_offer_expected_price_batch(
        GetFeaturedOfferExpectedPriceBatchRequest()
    )
    # TODO: Handle 'response' of type GetFeaturedOfferExpectedPriceBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetFeaturedOfferExpectedPriceBatchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetFeaturedOfferExpectedPriceBatchRequest](walmart_apis/models/get_featured_offer_expected_price_batch_request.py) \| [GetFeaturedOfferExpectedPriceBatchRequestDict](walmart_apis/models/get_featured_offer_expected_price_batch_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFeaturedOfferExpectedPriceBatchResponse](walmart_apis/models/get_featured_offer_expected_price_batch_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetFeaturedOfferExpectedPriceBatchErrorBody](walmart_apis/errors/get_featured_offer_expected_price_batch_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[Error3](walmart_apis/models/error3.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_item_offers(item_id: str, marketplace_id: str, item_condition: ConditionType2OrStr, *, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetOffersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the lowest priced offers for a single item based on Walmart Item ID and item condition.

Uses Walmart Item ID as the primary identifier(ASIN not supported —
no ASIN resolver exists in the Walmart platform; IQS queries by product.item_id).

Backed by IQS catalog_index cross-seller query (same as getListingOffers hop-2).
Returns 404 when no offers are found for the given itemId.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_item_offers("some example string", "some example string", ConditionType2.NEW)
    # TODO: Handle 'response' of type GetOffersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetItemOffersErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_item_offers(
        "some example string", "some example string", ConditionType2.NEW
    )
    # TODO: Handle 'response' of type GetOffersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetItemOffersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>item_id</code> | <code>str</code> | The Walmart Item ID of the item. |
| <code>marketplace_id</code> | <code>str</code> | A marketplace identifier. Specifies the marketplace for which prices are returned. |
| <code>item_condition</code> | <code>[ConditionType2OrStr](walmart_apis/models/enums/condition_type2.py)</code> | Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club. |
| <code>customer_type</code> | <code>[CustomerTypeOrStr](walmart_apis/models/enums/customer_type.py) \| None</code> | Indicates whether to request Consumer or Business offers. Default is Consumer.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOffersResponse](walmart_apis/models/get_offers_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetItemOffersErrorBody](walmart_apis/errors/get_item_offers_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[Error3](walmart_apis/models/error3.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_item_offers_batch(body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetItemOffersBatchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Batch version of getItemOffers. Accepts up to 20 Walmart Item ID requests.
Uses Walmart Item ID as the primary identifier.

Implemented as in-process fan-out over getItemOffers.
Each item gets its own per-item HTTP status code in the response body;
the outer HTTP response is always 200.
Implemented: .

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_item_offers_batch(GetItemOffersBatchRequest())
    # TODO: Handle 'response' of type GetItemOffersBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetItemOffersBatchErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_item_offers_batch(GetItemOffersBatchRequest())
    # TODO: Handle 'response' of type GetItemOffersBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetItemOffersBatchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetItemOffersBatchRequest](walmart_apis/models/get_item_offers_batch_request.py) \| [GetItemOffersBatchRequestDict](walmart_apis/models/get_item_offers_batch_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetItemOffersBatchResponse](walmart_apis/models/get_item_offers_batch_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetItemOffersBatchErrorBody](walmart_apis/errors/get_item_offers_batch_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[Error3](walmart_apis/models/error3.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_listing_offers(seller_sku: str, marketplace_id: str, item_condition: ConditionType2OrStr, *, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetOffersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the lowest priced offers for a single SKU listing, based on SKU and item condition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_listing_offers(
        "some example string", "some example string", ConditionType2.NEW
    )
    # TODO: Handle 'response' of type GetOffersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingOffersErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_listing_offers(
        "some example string", "some example string", ConditionType2.NEW
    )
    # TODO: Handle 'response' of type GetOffersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingOffersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>seller_sku</code> | <code>str</code> | Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId. |
| <code>marketplace_id</code> | <code>str</code> | A marketplace identifier. Specifies the marketplace for which prices are returned. |
| <code>item_condition</code> | <code>[ConditionType2OrStr](walmart_apis/models/enums/condition_type2.py)</code> | Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club. |
| <code>customer_type</code> | <code>[CustomerTypeOrStr](walmart_apis/models/enums/customer_type.py) \| None</code> | Indicates whether to request Consumer or Business offers. Default is Consumer.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOffersResponse](walmart_apis/models/get_offers_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetListingOffersErrorBody](walmart_apis/errors/get_listing_offers_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[Error3](walmart_apis/models/error3.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_listing_offers_batch(body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetListingOffersBatchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Batch version of getListingOffers. Accepts up to 20 SKU requests.

Implemented as in-process fan-out over getListingOffers (IQS-backed).
Each SKU gets its own per-item HTTP status code in the response body;
the outer HTTP response is always 200.
Implemented: .

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_listing_offers_batch(GetListingOffersBatchRequest())
    # TODO: Handle 'response' of type GetListingOffersBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingOffersBatchErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_listing_offers_batch(GetListingOffersBatchRequest())
    # TODO: Handle 'response' of type GetListingOffersBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingOffersBatchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetListingOffersBatchRequest](walmart_apis/models/get_listing_offers_batch_request.py) \| [GetListingOffersBatchRequestDict](walmart_apis/models/get_listing_offers_batch_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetListingOffersBatchResponse](walmart_apis/models/get_listing_offers_batch_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetListingOffersBatchErrorBody](walmart_apis/errors/get_listing_offers_batch_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[Error3](walmart_apis/models/error3.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_pricing(marketplace_id: str, *, item_type: ItemTypeOrStr = ItemType.SKU, skus: list[str] | None = None, walmart_item_ids: list[str] | None = None, item_condition: ConditionType2OrStr | None = None, offer_type: OfferTypeOrStr | None = None, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetPricingResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns pricing information for a seller's active offer listings based on seller SKU or Walmart Item ID .

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_pricing("some example string", item_type=ItemType.WALMART_ITEM_ID)
    # TODO: Handle 'response' of type GetPricingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPricingErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_pricing("some example string", item_type=ItemType.WALMART_ITEM_ID)
    # TODO: Handle 'response' of type GetPricingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPricingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>marketplace_id</code> | <code>str</code> | A marketplace identifier. Specifies the marketplace for which prices are returned. |
| <code>item_type</code> | <code>[ItemTypeOrStr](walmart_apis/models/enums/item_type.py)</code> | Indicates whether Walmart Item ID values or seller SKU values are used to identify items.<br>**Default**: <code>ItemType.SKU</code> |
| <code>skus</code> | <code>list&#91;str&#93; \| None</code> | A list of up to twenty seller SKU values used to identify items in the given marketplace.<br>**Default**: <code>None</code> |
| <code>walmart_item_ids</code> | <code>list&#91;str&#93; \| None</code> | A list of up to twenty Walmart Item ID values used to identify items in the given marketplace.<br>**Default**: <code>None</code> |
| <code>item_condition</code> | <code>[ConditionType2OrStr](walmart_apis/models/enums/condition_type2.py) \| None</code> | Filters the offer listings based on item condition. Possible values: New, Used, Collectible, Refurbished, Club.<br>**Default**: <code>None</code> |
| <code>offer_type</code> | <code>[OfferTypeOrStr](walmart_apis/models/enums/offer_type.py) \| None</code> | Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is B2C.<br>**Default**: <code>None</code> |
| <code>customer_type</code> | <code>[CustomerTypeOrStr](walmart_apis/models/enums/customer_type.py) \| None</code> | Indicates whether to request Consumer or Business offers. Default is Consumer.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetPricingResponse](walmart_apis/models/get_pricing_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetPricingErrorBody](walmart_apis/errors/get_pricing_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[Error3](walmart_apis/models/error3.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Sales

> Source: [Sales](walmart_apis/apis/sales.py)

<details>
<summary><code>def get_order_metrics(marketplace_ids: list[str], interval: str, granularity: GranularityOrStr, *, granularity_time_zone: str | None = None, buyer_type: BuyerTypeOrStr | None = None, fulfillment_network: str | None = None, first_day_of_week: FirstDayOfWeekOrStr | None = None, asin: str | None = None, sku: str | None = None, sp_api_program: str | None = None, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.sales.get_order_metrics(["some example string"], "some example string", Granularity.HOUR)
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderMetricsErrorBody
```

**Async**

```python
try:
    response = await async_client.sales.get_order_metrics(
        ["some example string"], "some example string", Granularity.HOUR
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderMetricsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be specified |
| <code>interval</code> | <code>str</code> | A time interval used for selecting order metrics. This takes the form of two dates separated by two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must represent absolute time (either Z notation or offset notation). Example: 2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in the -07:00 zone. |
| <code>granularity</code> | <code>[GranularityOrStr](walmart_apis/models/enums/granularity.py)</code> | The granularity of the grouping of order metrics, based on a unit of time. Specifying granularity=Hour results in a successful request only if the interval specified is less than or equal to 30 days from now. For all other granularities, the interval specified must be less or equal to 2 years from now. Specifying granularity=Total results in order metrics that are aggregated over the entire interval that you specify. If the interval start and end date don’t align with the specified granularity, the head and tail end of the response interval will contain partial data. Example: Day to get a daily breakdown of the request interval, where the day boundary is defined by the granularityTimeZone. |
| <code>granularity_time_zone</code> | <code>str \| None</code> | An IANA-compatible time zone for determining the day boundary. Required when specifying a granularity value greater than Hour. The granularityTimeZone value must align with the offset of the specified interval value. For example, if the interval value uses Z notation, then granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries, accounting for daylight time savings, for US/Pacific zone.<br>**Default**: <code>None</code> |
| <code>buyer_type</code> | <code>[BuyerTypeOrStr](walmart_apis/models/enums/buyer_type.py) \| None</code> | Filters the results by the buyer type that you specify, B2B (business to business) or B2C (business to customer). Example: B2B, if you want the response to include order metrics for only B2B buyers.<br>**Default**: <code>None</code> |
| <code>fulfillment_network</code> | <code>str \| None</code> | Filters the results by the fulfillment network that you specify, MFN (merchant fulfillment network) or AFN (marketplace fulfillment network). Do not include this filter if you want the response to include order metrics for all fulfillment networks. Example: AFN, if you want the response to include order metrics for only the marketplace fulfillment network.<br>**Default**: <code>None</code> |
| <code>first_day_of_week</code> | <code>[FirstDayOfWeekOrStr](walmart_apis/models/enums/first_day_of_week.py) \| None</code> | Specifies the day that the week starts on when granularity=Week, either Monday or Sunday. Default: Monday. Example: Sund<br>**Default**: <code>None</code> |
| <code>asin</code> | <code>str \| None</code> | Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all ASINs. Example: B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.<br>**Default**: <code>None</code> |
| <code>sku</code> | <code>str \| None</code> | Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if you want the response to include order metrics for only SKU TestSKU.<br>**Default**: <code>None</code> |
| <code>sp_api_program</code> | <code>str \| None</code> | Filters the results by the program that you specify. Do not include this filter if you want the response to inclu<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetOrderMetricsErrorBody](walmart_apis/errors/get_order_metrics_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Shipping

> Source: [Shipping](walmart_apis/apis/shipping.py)

<details>
<summary><code>def cancel_shipment2(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelShipmentResponse1</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels a shipment that has not yet shipped. Cancellation
eligibility is carrier-dependent; refer to the response
cancellation status to confirm.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shipping.cancel_shipment2("some example string")
    # TODO: Handle 'response' of type CancelShipmentResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelShipment2ErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.cancel_shipment2("some example string")
    # TODO: Handle 'response' of type CancelShipmentResponse1
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelShipment2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shipment_id</code> | <code>str</code> | Identifier of the shipment to cancel. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelShipmentResponse1](walmart_apis/models/cancel_shipment_response1.py)</code> -- Cancellation processed

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelShipment2ErrorBody](walmart_apis/errors/cancel_shipment2_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_access_points(access_point_types: str, country_code: str, postal_code: str, *, request_options: RequestOptionsOrDict | None = None) -> GetAccessPointsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns access points (pickup and dropoff locations) near the
supplied postal code and country, optionally filtered by access
point type.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shipping.get_access_points("some example string", "some example string", "some example string")
    # TODO: Handle 'response' of type GetAccessPointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccessPointsErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.get_access_points(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type GetAccessPointsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccessPointsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>access_point_types</code> | <code>str</code> | Comma-separated list of access point types to include. |
| <code>country_code</code> | <code>str</code> | ISO 3166-1 alpha-2 country code (e.g. US, CA, MX). |
| <code>postal_code</code> | <code>str</code> | Postal code to search around. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetAccessPointsResponse](walmart_apis/models/get_access_points_response.py)</code> -- Access points returned successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetAccessPointsErrorBody](walmart_apis/errors/get_access_points_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_additional_inputs(rate_id: str, request_token: str, *, request_options: RequestOptionsOrDict | None = None) -> GetAdditionalInputsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a JSON Schema document describing any
carrier-and-service-specific inputs required to purchase a
shipment for the supplied requestToken + rateId. The schema is
served verbatim and the calling client should validate the
seller's input against it before issuing purchaseShipment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shipping.get_additional_inputs("some example string", "some example string")
    # TODO: Handle 'response' of type GetAdditionalInputsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAdditionalInputsErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.get_additional_inputs("some example string", "some example string")
    # TODO: Handle 'response' of type GetAdditionalInputsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAdditionalInputsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>rate_id</code> | <code>str</code> | rateId returned by a prior getRates response. |
| <code>request_token</code> | <code>str</code> | requestToken returned by a prior getRates response. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetAdditionalInputsResponse](walmart_apis/models/get_additional_inputs_response.py)</code> -- JSON Schema for additional inputs returned successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetAdditionalInputsErrorBody](walmart_apis/errors/get_additional_inputs_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_rates(body: GetRatesRequest | GetRatesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetFulfillmentOrderResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of shipping rate quotes for the given shipment
request. The seller can then call purchaseShipment with the
selected rateId to commit to a label purchase.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shipping.get_rates(
        GetRatesRequest(
            ship_to=Address1(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            ship_from=Address1(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            packages=[
                Package(
                    dimensions=PackageDimensions(length=1.5, width=1.5, height=1.5, unit=Unit.INCHES),
                    weight=Weight(value=1.5, unit=Unit1.OZ),
                    package_client_reference_id="some example string",
                ),
            ],
            channel_details=ChannelDetails(channel_type=ChannelType.WALMART_MARKETPLACE),
        ),
    )
    # TODO: Handle 'response' of type GetFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRatesErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.get_rates(
        GetRatesRequest(
            ship_to=Address1(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            ship_from=Address1(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            packages=[
                Package(
                    dimensions=PackageDimensions(length=1.5, width=1.5, height=1.5, unit=Unit.INCHES),
                    weight=Weight(value=1.5, unit=Unit1.OZ),
                    package_client_reference_id="some example string",
                ),
            ],
            channel_details=ChannelDetails(channel_type=ChannelType.WALMART_MARKETPLACE),
        ),
    )
    # TODO: Handle 'response' of type GetFulfillmentOrderResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRatesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetRatesRequest](walmart_apis/models/get_rates_request.py) \| [GetRatesRequestDict](walmart_apis/models/get_rates_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFulfillmentOrderResponse](walmart_apis/models/get_fulfillment_order_response.py)</code> -- Rate quotes returned successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetRatesErrorBody](walmart_apis/errors/get_rates_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment_documents(shipment_id: str, *, package_client_reference_id: str | None = None, format_: Format1OrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetShipmentDocumentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the label, customs, and other printable documents
associated with a previously-purchased shipment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shipping.get_shipment_documents("some example string")
    # TODO: Handle 'response' of type GetShipmentDocumentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentDocumentsErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.get_shipment_documents("some example string")
    # TODO: Handle 'response' of type GetShipmentDocumentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentDocumentsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shipment_id</code> | <code>str</code> | Identifier of the shipment whose documents to retrieve. |
| <code>package_client_reference_id</code> | <code>str \| None</code> | Optional package-level reference id to retrieve documents<br>for a specific package within a multi-package shipment.<br>**Default**: <code>None</code> |
| <code>format_</code> | <code>[Format1OrStr](walmart_apis/models/enums/format1.py) \| None</code> | Requested document format (defaults to PDF).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetShipmentDocumentsResponse](walmart_apis/models/get_shipment_documents_response.py)</code> -- Documents returned successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetShipmentDocumentsErrorBody](walmart_apis/errors/get_shipment_documents_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_tracking(tracking_id: str, *, carrier_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetTrackingResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the current tracking status, event history, and any
proof-of-delivery details for the given trackingId. TNT
resolves carrier internally from the trackingId alone, so
carrierId is optional -- confirmed unnecessary by the TNT/
Vulcan team (STRIDE-TNT-CORE-PACKAGE-SERVICES) 2026-08-19.
When provided, it's used only as a defense-in-depth check
against the resolved carrier; a mismatch surfaces as 404.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shipping.get_tracking("some example string")
    # TODO: Handle 'response' of type GetTrackingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackingErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.get_tracking("some example string")
    # TODO: Handle 'response' of type GetTrackingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTrackingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>tracking_id</code> | <code>str</code> | Tracking identifier returned by purchaseShipment. |
| <code>carrier_id</code> | <code>str \| None</code> | Optional carrier identifier for defense-in-depth validation<br>against TNT's resolved carrier. Not required by TNT itself<br>-- omit unless you specifically want mismatch protection.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetTrackingResponse](walmart_apis/models/get_tracking_response.py)</code> -- Tracking details returned successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetTrackingErrorBody](walmart_apis/errors/get_tracking_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def one_click_shipment(body: OneClickShipmentRequest | OneClickShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetFulfillmentOrderShipmentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Convenience endpoint that combines rate quote and purchase into
a single round trip when the seller already knows the desired
service level. Returns the purchased shipment record directly.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shipping.one_click_shipment(
        OneClickShipmentRequest(
            ship_to=Address1(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            ship_from=Address1(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            packages=[
                Package(
                    dimensions=PackageDimensions(length=1.5, width=1.5, height=1.5, unit=Unit.INCHES),
                    weight=Weight(value=1.5, unit=Unit1.OZ),
                    package_client_reference_id="some example string",
                ),
            ],
            service_selection=ServiceSelection(),
            requested_document_specification=RequestedDocumentSpecification(
                format=Format1.PDF, size=LabelDimensions(), dpi=Dpi.VALUE_203
            ),
            channel_details=ChannelDetails(channel_type=ChannelType.WALMART_MARKETPLACE),
        ),
    )
    # TODO: Handle 'response' of type GetFulfillmentOrderShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OneClickShipmentErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.one_click_shipment(
        OneClickShipmentRequest(
            ship_to=Address1(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            ship_from=Address1(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            packages=[
                Package(
                    dimensions=PackageDimensions(length=1.5, width=1.5, height=1.5, unit=Unit.INCHES),
                    weight=Weight(value=1.5, unit=Unit1.OZ),
                    package_client_reference_id="some example string",
                ),
            ],
            service_selection=ServiceSelection(),
            requested_document_specification=RequestedDocumentSpecification(
                format=Format1.PDF, size=LabelDimensions(), dpi=Dpi.VALUE_203
            ),
            channel_details=ChannelDetails(channel_type=ChannelType.WALMART_MARKETPLACE),
        ),
    )
    # TODO: Handle 'response' of type GetFulfillmentOrderShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OneClickShipmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[OneClickShipmentRequest](walmart_apis/models/one_click_shipment_request.py) \| [OneClickShipmentRequestDict](walmart_apis/models/one_click_shipment_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFulfillmentOrderShipmentsResponse](walmart_apis/models/get_fulfillment_order_shipments_response.py)</code> -- Shipment purchased successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[OneClickShipmentErrorBody](walmart_apis/errors/one_click_shipment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def purchase_shipment(body: PurchaseShipmentRequest | PurchaseShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetFulfillmentOrderShipmentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Purchases the shipping label for the rate selected from a prior
getRates response. Returns the shipment record with label
document references.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.shipping.purchase_shipment(
        PurchaseShipmentRequest(
            request_token="some example string",
            rate_id="some example string",
            requested_document_specification=RequestedDocumentSpecification(
                format=Format1.PDF, size=LabelDimensions(), dpi=Dpi.VALUE_203
            ),
        ),
    )
    # TODO: Handle 'response' of type GetFulfillmentOrderShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PurchaseShipmentErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.purchase_shipment(
        PurchaseShipmentRequest(
            request_token="some example string",
            rate_id="some example string",
            requested_document_specification=RequestedDocumentSpecification(
                format=Format1.PDF, size=LabelDimensions(), dpi=Dpi.VALUE_203
            ),
        ),
    )
    # TODO: Handle 'response' of type GetFulfillmentOrderShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type PurchaseShipmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[PurchaseShipmentRequest](walmart_apis/models/purchase_shipment_request.py) \| [PurchaseShipmentRequestDict](walmart_apis/models/purchase_shipment_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetFulfillmentOrderShipmentsResponse](walmart_apis/models/get_fulfillment_order_shipments_response.py)</code> -- Shipment purchased successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[PurchaseShipmentErrorBody](walmart_apis/errors/purchase_shipment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def submit_ndr_feedback(body: SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Submits seller feedback on a non-delivery event for a shipment,
instructing the carrier on how to proceed (return, reattempt,
redirect, etc).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.shipping.submit_ndr_feedback(
        SubmitNdrFeedbackRequest(seller_tracking_id="some example string", ndr_action=NdrAction.RETURN_TO_ORIGIN)
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubmitNdrFeedbackErrorBody
```

**Async**

```python
try:
    await async_client.shipping.submit_ndr_feedback(
        SubmitNdrFeedbackRequest(seller_tracking_id="some example string", ndr_action=NdrAction.RETURN_TO_ORIGIN)
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SubmitNdrFeedbackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SubmitNdrFeedbackRequest](walmart_apis/models/submit_ndr_feedback_request.py) \| [SubmitNdrFeedbackRequestDict](walmart_apis/models/submit_ndr_feedback_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SubmitNdrFeedbackErrorBody](walmart_apis/errors/submit_ndr_feedback_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Solicitations

> Source: [Solicitations](walmart_apis/apis/solicitations.py)

<details>
<summary><code>def create_product_review_and_seller_feedback_solicitation(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.solicitations.create_product_review_and_seller_feedback_solicitation(
        "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductReviewAndSellerFeedbackSolicitationErrorBody
```

**Async**

```python
try:
    response = await async_client.solicitations.create_product_review_and_seller_feedback_solicitation(
        "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateProductReviewAndSellerFeedbackSolicitationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | An SP-API order identifier. This specifies the order for which a solicitation is sent. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be spec |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateProductReviewAndSellerFeedbackSolicitationErrorBody](walmart_apis/errors/create_product_review_and_seller_feedback_solicitation_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_solicitation_actions_for_order(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.solicitations.get_solicitation_actions_for_order("some example string", ["some example string"])
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSolicitationActionsForOrderErrorBody
```

**Async**

```python
try:
    response = await async_client.solicitations.get_solicitation_actions_for_order(
        "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSolicitationActionsForOrderErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>sp_api_order_id</code> | <code>str</code> | An SP-API order identifier. This specifies the order for which you want a list of available solicitation types. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | A marketplace identifier. This specifies the marketplace in which the order was placed. Only one marketplace can be spec |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>Any</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetSolicitationActionsForOrderErrorBody](walmart_apis/errors/get_solicitation_actions_for_order_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WfsInbound

> Source: [WfsInbound](walmart_apis/apis/wfs_inbound.py)

<details>
<summary><code>def cancel_inbound_plan(inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.cancel_inbound_plan("some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelInboundPlanErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.cancel_inbound_plan("some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelInboundPlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelInboundPlanErrorBody](walmart_apis/errors/cancel_inbound_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_self_ship_appointment(inbound_plan_id: str, shipment_id: str, body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.cancel_self_ship_appointment(
        "some example string", "some example string", CancelSelfShipAppointmentRequest()
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSelfShipAppointmentErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.cancel_self_ship_appointment(
        "some example string", "some example string", CancelSelfShipAppointmentRequest()
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSelfShipAppointmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[CancelSelfShipAppointmentRequest](walmart_apis/models/cancel_self_ship_appointment_request.py) \| [CancelSelfShipAppointmentRequestDict](walmart_apis/models/cancel_self_ship_appointment_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelSelfShipAppointmentErrorBody](walmart_apis/errors/cancel_self_ship_appointment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_delivery_window_options(inbound_plan_id: str, shipment_id: str, delivery_window_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.confirm_delivery_window_options(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmDeliveryWindowOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_delivery_window_options(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmDeliveryWindowOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | The shipment to confirm the delivery window option for. |
| <code>delivery_window_option_id</code> | <code>str</code> | The ID of the delivery window option to be confirmed. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmDeliveryWindowOptionsErrorBody](walmart_apis/errors/confirm_delivery_window_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_packing_option(inbound_plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.confirm_packing_option("some example string", "some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmPackingOptionErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_packing_option("some example string", "some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmPackingOptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>packing_option_id</code> | <code>str</code> | Identifier of a packing option. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmPackingOptionErrorBody](walmart_apis/errors/confirm_packing_option_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_placement_option(inbound_plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.confirm_placement_option("some example string", "some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmPlacementOptionErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_placement_option("some example string", "some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmPlacementOptionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>placement_option_id</code> | <code>str</code> | The identifier of a placement option. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmPlacementOptionErrorBody](walmart_apis/errors/confirm_placement_option_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_shipment_content_update_preview(inbound_plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.confirm_shipment_content_update_preview(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmShipmentContentUpdatePreviewErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_shipment_content_update_preview(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmShipmentContentUpdatePreviewErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>content_update_preview_id</code> | <code>str</code> | Identifier of a content update preview. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmShipmentContentUpdatePreviewErrorBody](walmart_apis/errors/confirm_shipment_content_update_preview_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_transportation_options(inbound_plan_id: str, body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.confirm_transportation_options(
        "some example string",
        ConfirmTransportationOptionsRequest(
            transportation_selections=[
                CommonTransportationSelection(
                    shipment_id="some example string", transportation_option_id="some example string"
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmTransportationOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_transportation_options(
        "some example string",
        ConfirmTransportationOptionsRequest(
            transportation_selections=[
                CommonTransportationSelection(
                    shipment_id="some example string", transportation_option_id="some example string"
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmTransportationOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[ConfirmTransportationOptionsRequest](walmart_apis/models/confirm_transportation_options_request.py) \| [ConfirmTransportationOptionsRequestDict](walmart_apis/models/confirm_transportation_options_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmTransportationOptionsErrorBody](walmart_apis/errors/confirm_transportation_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_inbound_plan(body: CreateInboundPlanRequest | CreateInboundPlanRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.create_inbound_plan(
        CreateInboundPlanRequest(
            destination_marketplaces=["some example string"],
            items=[
                CommonItemInput(
                    label_owner=CommonLabelOwner.SELLER,
                    msku="some example string",
                    prep_owner=CommonPrepOwner.SELLER,
                    quantity=1,
                ),
            ],
            source_address=CommonAddressInput(
                address_line1="some example string",
                city="some example string",
                country_code="some example string",
                name="some example string",
                phone_number="some example string",
                postal_code="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type CreateInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateInboundPlanErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.create_inbound_plan(
        CreateInboundPlanRequest(
            destination_marketplaces=["some example string"],
            items=[
                CommonItemInput(
                    label_owner=CommonLabelOwner.SELLER,
                    msku="some example string",
                    prep_owner=CommonPrepOwner.SELLER,
                    quantity=1,
                ),
            ],
            source_address=CommonAddressInput(
                address_line1="some example string",
                city="some example string",
                country_code="some example string",
                name="some example string",
                phone_number="some example string",
                postal_code="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type CreateInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateInboundPlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateInboundPlanRequest](walmart_apis/models/create_inbound_plan_request.py) \| [CreateInboundPlanRequestDict](walmart_apis/models/create_inbound_plan_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateInboundPlanResponse](walmart_apis/models/create_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateInboundPlanErrorBody](walmart_apis/errors/create_inbound_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_marketplace_item_labels(body: CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateMarketplaceItemLabelsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.create_marketplace_item_labels(
        CreateMarketplaceItemLabelsRequest(
            label_type=CommonLabelPrintType.STANDARD_FORMAT,
            marketplace_id="some example string",
            msku_quantities=[CommonMskuQuantity(msku="some example string", quantity=1)],
        ),
    )
    # TODO: Handle 'response' of type CreateMarketplaceItemLabelsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMarketplaceItemLabelsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.create_marketplace_item_labels(
        CreateMarketplaceItemLabelsRequest(
            label_type=CommonLabelPrintType.STANDARD_FORMAT,
            marketplace_id="some example string",
            msku_quantities=[CommonMskuQuantity(msku="some example string", quantity=1)],
        ),
    )
    # TODO: Handle 'response' of type CreateMarketplaceItemLabelsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateMarketplaceItemLabelsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateMarketplaceItemLabelsRequest](walmart_apis/models/create_marketplace_item_labels_request.py) \| [CreateMarketplaceItemLabelsRequestDict](walmart_apis/models/create_marketplace_item_labels_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateMarketplaceItemLabelsResponse](walmart_apis/models/create_marketplace_item_labels_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateMarketplaceItemLabelsErrorBody](walmart_apis/errors/create_marketplace_item_labels_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_delivery_window_options(inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.generate_delivery_window_options("some example string", "some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateDeliveryWindowOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_delivery_window_options(
        "some example string", "some example string"
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateDeliveryWindowOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | The shipment to generate delivery window options for. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GenerateDeliveryWindowOptionsErrorBody](walmart_apis/errors/generate_delivery_window_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_packing_options(inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.generate_packing_options("some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePackingOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_packing_options("some example string")
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePackingOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GeneratePackingOptionsErrorBody](walmart_apis/errors/generate_packing_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_placement_options(inbound_plan_id: str, body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.generate_placement_options("some example string", GeneratePlacementOptionsRequest())
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePlacementOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_placement_options(
        "some example string", GeneratePlacementOptionsRequest()
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePlacementOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[GeneratePlacementOptionsRequest](walmart_apis/models/generate_placement_options_request.py) \| [GeneratePlacementOptionsRequestDict](walmart_apis/models/generate_placement_options_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GeneratePlacementOptionsErrorBody](walmart_apis/errors/generate_placement_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_self_ship_appointment_slots(inbound_plan_id: str, shipment_id: str, body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.generate_self_ship_appointment_slots(
        "some example string", "some example string", GenerateSelfShipAppointmentSlotsRequest()
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateSelfShipAppointmentSlotsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_self_ship_appointment_slots(
        "some example string", "some example string", GenerateSelfShipAppointmentSlotsRequest()
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateSelfShipAppointmentSlotsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[GenerateSelfShipAppointmentSlotsRequest](walmart_apis/models/generate_self_ship_appointment_slots_request.py) \| [GenerateSelfShipAppointmentSlotsRequestDict](walmart_apis/models/generate_self_ship_appointment_slots_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GenerateSelfShipAppointmentSlotsErrorBody](walmart_apis/errors/generate_self_ship_appointment_slots_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_shipment_content_update_previews(inbound_plan_id: str, shipment_id: str, body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.generate_shipment_content_update_previews(
        "some example string",
        "some example string",
        GenerateShipmentContentUpdatePreviewsRequest(
            boxes=[
                CommonBoxUpdateInput(
                    content_information_source=CommonBoxContentInformationSource.BOX_CONTENT_PROVIDED,
                    dimensions=CommonDimensions(
                        height=1.5, length=1.5, width=1.5, unit_of_measurement=CommonUnitOfMeasurement.IN
                    ),
                    quantity=1,
                    weight=CommonWeight(unit=CommonUnitOfWeight.LB, value=1.5),
                ),
            ],
            items=[
                CommonItemInput(
                    label_owner=CommonLabelOwner.SELLER,
                    msku="some example string",
                    prep_owner=CommonPrepOwner.SELLER,
                    quantity=1,
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateShipmentContentUpdatePreviewsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_shipment_content_update_previews(
        "some example string",
        "some example string",
        GenerateShipmentContentUpdatePreviewsRequest(
            boxes=[
                CommonBoxUpdateInput(
                    content_information_source=CommonBoxContentInformationSource.BOX_CONTENT_PROVIDED,
                    dimensions=CommonDimensions(
                        height=1.5, length=1.5, width=1.5, unit_of_measurement=CommonUnitOfMeasurement.IN
                    ),
                    quantity=1,
                    weight=CommonWeight(unit=CommonUnitOfWeight.LB, value=1.5),
                ),
            ],
            items=[
                CommonItemInput(
                    label_owner=CommonLabelOwner.SELLER,
                    msku="some example string",
                    prep_owner=CommonPrepOwner.SELLER,
                    quantity=1,
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateShipmentContentUpdatePreviewsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[GenerateShipmentContentUpdatePreviewsRequest](walmart_apis/models/generate_shipment_content_update_previews_request.py) \| [GenerateShipmentContentUpdatePreviewsRequestDict](walmart_apis/models/generate_shipment_content_update_previews_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GenerateShipmentContentUpdatePreviewsErrorBody](walmart_apis/errors/generate_shipment_content_update_previews_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_transportation_options(inbound_plan_id: str, body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.generate_transportation_options(
        "some example string",
        GenerateTransportationOptionsRequest(
            placement_option_id="some example string",
            shipment_transportation_configurations=[
                CommonShipmentTransportationConfiguration(
                    ready_to_ship_window=CommonWindowInput(start=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)),
                    shipment_id="some example string",
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateTransportationOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_transportation_options(
        "some example string",
        GenerateTransportationOptionsRequest(
            placement_option_id="some example string",
            shipment_transportation_configurations=[
                CommonShipmentTransportationConfiguration(
                    ready_to_ship_window=CommonWindowInput(start=datetime(2024, 1, 15, 9, 30, 0, tzinfo=timezone.utc)),
                    shipment_id="some example string",
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateTransportationOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[GenerateTransportationOptionsRequest](walmart_apis/models/generate_transportation_options_request.py) \| [GenerateTransportationOptionsRequestDict](walmart_apis/models/generate_transportation_options_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GenerateTransportationOptionsErrorBody](walmart_apis/errors/generate_transportation_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_delivery_challan_document(inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetDeliveryChallanDocumentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_delivery_challan_document("some example string", "some example string")
    # TODO: Handle 'response' of type GetDeliveryChallanDocumentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeliveryChallanDocumentErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_delivery_challan_document(
        "some example string", "some example string"
    )
    # TODO: Handle 'response' of type GetDeliveryChallanDocumentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeliveryChallanDocumentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetDeliveryChallanDocumentResponse](walmart_apis/models/get_delivery_challan_document_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetDeliveryChallanDocumentErrorBody](walmart_apis/errors/get_delivery_challan_document_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_inbound_operation_status(operation_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CommonInboundOperationStatus</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_inbound_operation_status("some example string")
    # TODO: Handle 'response' of type CommonInboundOperationStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInboundOperationStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_inbound_operation_status("some example string")
    # TODO: Handle 'response' of type CommonInboundOperationStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInboundOperationStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>operation_id</code> | <code>str</code> | Identifier of an asynchronous operation. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommonInboundOperationStatus](walmart_apis/models/common_inbound_operation_status.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetInboundOperationStatusErrorBody](walmart_apis/errors/get_inbound_operation_status_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_inbound_plan(inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> InboundPlan</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_inbound_plan("some example string")
    # TODO: Handle 'response' of type InboundPlan
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInboundPlanErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_inbound_plan("some example string")
    # TODO: Handle 'response' of type InboundPlan
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetInboundPlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[InboundPlan](walmart_apis/models/inbound_plan.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetInboundPlanErrorBody](walmart_apis/errors/get_inbound_plan_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_self_ship_appointment_slots(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetSelfShipAppointmentSlotsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_self_ship_appointment_slots("some example string", "some example string")
    # TODO: Handle 'response' of type GetSelfShipAppointmentSlotsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSelfShipAppointmentSlotsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_self_ship_appointment_slots(
        "some example string", "some example string"
    )
    # TODO: Handle 'response' of type GetSelfShipAppointmentSlotsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSelfShipAppointmentSlotsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>page_size</code> | <code>int \| None</code> | The number of self ship appointment slots to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetSelfShipAppointmentSlotsResponse](walmart_apis/models/get_self_ship_appointment_slots_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetSelfShipAppointmentSlotsErrorBody](walmart_apis/errors/get_self_ship_appointment_slots_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment(inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CommonShipment</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_shipment("some example string", "some example string")
    # TODO: Handle 'response' of type CommonShipment
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_shipment("some example string", "some example string")
    # TODO: Handle 'response' of type CommonShipment
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. A shipment contains the boxes and units being inbounded. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommonShipment](walmart_apis/models/common_shipment.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetShipmentErrorBody](walmart_apis/errors/get_shipment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment_content_update_preview(inbound_plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CommonContentUpdatePreview</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_shipment_content_update_preview(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type CommonContentUpdatePreview
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentContentUpdatePreviewErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_shipment_content_update_preview(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type CommonContentUpdatePreview
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentContentUpdatePreviewErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>content_update_preview_id</code> | <code>str</code> | Identifier of a content update preview. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CommonContentUpdatePreview](walmart_apis/models/common_content_update_preview.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetShipmentContentUpdatePreviewErrorBody](walmart_apis/errors/get_shipment_content_update_preview_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_delivery_window_options(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListDeliveryWindowOptionsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_delivery_window_options("some example string", "some example string")
    # TODO: Handle 'response' of type ListDeliveryWindowOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDeliveryWindowOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_delivery_window_options("some example string", "some example string")
    # TODO: Handle 'response' of type ListDeliveryWindowOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDeliveryWindowOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | The shipment to get delivery window options for. |
| <code>page_size</code> | <code>int \| None</code> | The number of delivery window options to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListDeliveryWindowOptionsResponse](walmart_apis/models/list_delivery_window_options_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListDeliveryWindowOptionsErrorBody](walmart_apis/errors/list_delivery_window_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_inbound_plan_boxes(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanBoxesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_inbound_plan_boxes("some example string")
    # TODO: Handle 'response' of type ListInboundPlanBoxesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListInboundPlanBoxesErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_inbound_plan_boxes("some example string")
    # TODO: Handle 'response' of type ListInboundPlanBoxesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListInboundPlanBoxesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | The number of boxes to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlanBoxesResponse](walmart_apis/models/list_inbound_plan_boxes_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListInboundPlanBoxesErrorBody](walmart_apis/errors/list_inbound_plan_boxes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_inbound_plan_items(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanItemsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_inbound_plan_items("some example string")
    # TODO: Handle 'response' of type ListInboundPlanItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListInboundPlanItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_inbound_plan_items("some example string")
    # TODO: Handle 'response' of type ListInboundPlanItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListInboundPlanItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | The number of items to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlanItemsResponse](walmart_apis/models/list_inbound_plan_items_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListInboundPlanItemsErrorBody](walmart_apis/errors/list_inbound_plan_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_inbound_plan_pallets(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanPalletsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_inbound_plan_pallets("some example string")
    # TODO: Handle 'response' of type ListInboundPlanPalletsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListInboundPlanPalletsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_inbound_plan_pallets("some example string")
    # TODO: Handle 'response' of type ListInboundPlanPalletsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListInboundPlanPalletsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | The number of pallets to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlanPalletsResponse](walmart_apis/models/list_inbound_plan_pallets_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListInboundPlanPalletsErrorBody](walmart_apis/errors/list_inbound_plan_pallets_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_inbound_plans(*, page_size: int | None = 10, pagination_token: str | None = None, status: str | None = None, sort_by: str | None = None, sort_order: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlansResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_inbound_plans()
    # TODO: Handle 'response' of type ListInboundPlansResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListInboundPlansErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_inbound_plans()
    # TODO: Handle 'response' of type ListInboundPlansResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListInboundPlansErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>page_size</code> | <code>int \| None</code> | The number of inbound plans to return in the response matching the given query.<br>**Default**: <code>10</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>str \| None</code> | The status of an inbound plan. Possible values: `ACTIVE`, `VOIDED`, `SHIPPED`, `ERRORED`.<br>**Default**: <code>None</code> |
| <code>sort_by</code> | <code>str \| None</code> | Sort by field.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>str \| None</code> | The sort order. Possible values: `ASC`, `DESC`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlansResponse](walmart_apis/models/list_inbound_plans_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListInboundPlansErrorBody](walmart_apis/errors/list_inbound_plans_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_item_compliance_details(mskus: list[str], marketplace_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ListItemComplianceDetailsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_item_compliance_details(["some example string"], "some example string")
    # TODO: Handle 'response' of type ListItemComplianceDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListItemComplianceDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_item_compliance_details(
        ["some example string"], "some example string"
    )
    # TODO: Handle 'response' of type ListItemComplianceDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListItemComplianceDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>mskus</code> | <code>list&#91;str&#93;</code> | A list of merchant SKUs, a merchant-supplied identifier of a specific SKU. |
| <code>marketplace_id</code> | <code>str</code> | The Walmart Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.walmart.com/seller-api/docs/marketplace-ids). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListItemComplianceDetailsResponse](walmart_apis/models/list_item_compliance_details_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListItemComplianceDetailsErrorBody](walmart_apis/errors/list_item_compliance_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_packing_group_boxes(inbound_plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanBoxesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_packing_group_boxes("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanBoxesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPackingGroupBoxesErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_packing_group_boxes("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanBoxesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPackingGroupBoxesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>packing_group_id</code> | <code>str</code> | Identifier of a packing group. |
| <code>page_size</code> | <code>int \| None</code> | The number of packing group boxes to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlanBoxesResponse](walmart_apis/models/list_inbound_plan_boxes_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListPackingGroupBoxesErrorBody](walmart_apis/errors/list_packing_group_boxes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_packing_group_items(inbound_plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanItemsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_packing_group_items("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPackingGroupItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_packing_group_items("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPackingGroupItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>packing_group_id</code> | <code>str</code> | Identifier of a packing group. |
| <code>page_size</code> | <code>int \| None</code> | The number of packing group items to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlanItemsResponse](walmart_apis/models/list_inbound_plan_items_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListPackingGroupItemsErrorBody](walmart_apis/errors/list_packing_group_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_packing_options(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListPackingOptionsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_packing_options("some example string")
    # TODO: Handle 'response' of type ListPackingOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPackingOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_packing_options("some example string")
    # TODO: Handle 'response' of type ListPackingOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPackingOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | The number of packing options to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListPackingOptionsResponse](walmart_apis/models/list_packing_options_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListPackingOptionsErrorBody](walmart_apis/errors/list_packing_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_placement_options(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListPlacementOptionsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_placement_options("some example string")
    # TODO: Handle 'response' of type ListPlacementOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPlacementOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_placement_options("some example string")
    # TODO: Handle 'response' of type ListPlacementOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPlacementOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | The number of placement options to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListPlacementOptionsResponse](walmart_apis/models/list_placement_options_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListPlacementOptionsErrorBody](walmart_apis/errors/list_placement_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_prep_details(marketplace_id: str, mskus: list[str], *, request_options: RequestOptionsOrDict | None = None) -> ListPrepDetailsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_prep_details("some example string", ["some example string"])
    # TODO: Handle 'response' of type ListPrepDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPrepDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_prep_details("some example string", ["some example string"])
    # TODO: Handle 'response' of type ListPrepDetailsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPrepDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>marketplace_id</code> | <code>str</code> | The Walmart Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.walmart.com/seller-api/docs/marketplace-ids). |
| <code>mskus</code> | <code>list&#91;str&#93;</code> | A list of merchant SKUs, a merchant-supplied identifier of a specific SKU. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListPrepDetailsResponse](walmart_apis/models/list_prep_details_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListPrepDetailsErrorBody](walmart_apis/errors/list_prep_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_shipment_boxes(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanBoxesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_shipment_boxes("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanBoxesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentBoxesErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_shipment_boxes("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanBoxesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentBoxesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. A shipment contains the boxes and units being inbounded. |
| <code>page_size</code> | <code>int \| None</code> | The number of boxes to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlanBoxesResponse](walmart_apis/models/list_inbound_plan_boxes_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListShipmentBoxesErrorBody](walmart_apis/errors/list_shipment_boxes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_shipment_content_update_previews(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListShipmentContentUpdatePreviewsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_shipment_content_update_previews("some example string", "some example string")
    # TODO: Handle 'response' of type ListShipmentContentUpdatePreviewsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentContentUpdatePreviewsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_shipment_content_update_previews(
        "some example string", "some example string"
    )
    # TODO: Handle 'response' of type ListShipmentContentUpdatePreviewsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentContentUpdatePreviewsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>page_size</code> | <code>int \| None</code> | The number of content update previews to return.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListShipmentContentUpdatePreviewsResponse](walmart_apis/models/list_shipment_content_update_previews_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListShipmentContentUpdatePreviewsErrorBody](walmart_apis/errors/list_shipment_content_update_previews_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_shipment_items(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanItemsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_shipment_items("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_shipment_items("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. A shipment contains the boxes and units being inbounded. |
| <code>page_size</code> | <code>int \| None</code> | The number of items to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlanItemsResponse](walmart_apis/models/list_inbound_plan_items_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListShipmentItemsErrorBody](walmart_apis/errors/list_shipment_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_shipment_pallets(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanPalletsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_shipment_pallets("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanPalletsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentPalletsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_shipment_pallets("some example string", "some example string")
    # TODO: Handle 'response' of type ListInboundPlanPalletsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentPalletsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>page_size</code> | <code>int \| None</code> | The number of pallets to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListInboundPlanPalletsResponse](walmart_apis/models/list_inbound_plan_pallets_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListShipmentPalletsErrorBody](walmart_apis/errors/list_shipment_pallets_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_transportation_options(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, placement_option_id: str | None = None, shipment_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListTransportationOptionsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.list_transportation_options("some example string")
    # TODO: Handle 'response' of type ListTransportationOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListTransportationOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_transportation_options("some example string")
    # TODO: Handle 'response' of type ListTransportationOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListTransportationOptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | The number of transportation options to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>placement_option_id</code> | <code>str \| None</code> | The placement option to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified.<br>**Default**: <code>None</code> |
| <code>shipment_id</code> | <code>str \| None</code> | The shipment to get transportation options for. Either `placementOptionId` or `shipmentId` must be specified.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListTransportationOptionsResponse](walmart_apis/models/list_transportation_options_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListTransportationOptionsErrorBody](walmart_apis/errors/list_transportation_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def schedule_self_ship_appointment(inbound_plan_id: str, shipment_id: str, slot_id: str, body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ScheduleSelfShipAppointmentResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.schedule_self_ship_appointment(
        "some example string", "some example string", "some example string", ScheduleSelfShipAppointmentRequest()
    )
    # TODO: Handle 'response' of type ScheduleSelfShipAppointmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleSelfShipAppointmentErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.schedule_self_ship_appointment(
        "some example string", "some example string", "some example string", ScheduleSelfShipAppointmentRequest()
    )
    # TODO: Handle 'response' of type ScheduleSelfShipAppointmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleSelfShipAppointmentErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>slot_id</code> | <code>str</code> | An identifier to a self-ship appointment slot. |
| <code>body</code> | <code>[ScheduleSelfShipAppointmentRequest](walmart_apis/models/schedule_self_ship_appointment_request.py) \| [ScheduleSelfShipAppointmentRequestDict](walmart_apis/models/schedule_self_ship_appointment_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ScheduleSelfShipAppointmentResponse](walmart_apis/models/schedule_self_ship_appointment_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ScheduleSelfShipAppointmentErrorBody](walmart_apis/errors/schedule_self_ship_appointment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_packing_information(inbound_plan_id: str, body: SetPackingInformationRequest | SetPackingInformationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.set_packing_information(
        "some example string",
        SetPackingInformationRequest(
            package_groupings=[
                CommonPackageGroupingInput(
                    boxes=[
                        CommonBoxInput(
                            content_information_source=CommonBoxContentInformationSource.BOX_CONTENT_PROVIDED,
                            dimensions=CommonDimensions(),
                            quantity=1,
                            weight=CommonWeight(),
                        ),
                    ],
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetPackingInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.set_packing_information(
        "some example string",
        SetPackingInformationRequest(
            package_groupings=[
                CommonPackageGroupingInput(
                    boxes=[
                        CommonBoxInput(
                            content_information_source=CommonBoxContentInformationSource.BOX_CONTENT_PROVIDED,
                            dimensions=CommonDimensions(),
                            quantity=1,
                            weight=CommonWeight(),
                        ),
                    ],
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetPackingInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[SetPackingInformationRequest](walmart_apis/models/set_packing_information_request.py) \| [SetPackingInformationRequestDict](walmart_apis/models/set_packing_information_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SetPackingInformationErrorBody](walmart_apis/errors/set_packing_information_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_prep_details(body: SetPrepDetailsRequest | SetPrepDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.set_prep_details(
        SetPrepDetailsRequest(
            marketplace_id="some example string",
            msku_prep_details=[
                CommonMskuPrepDetailInput(
                    msku="some example string",
                    prep_category=CommonPrepCategory.ADULT,
                    prep_types=[CommonPrepType.ITEM_BLACK_SHRINKWRAP],
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetPrepDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.set_prep_details(
        SetPrepDetailsRequest(
            marketplace_id="some example string",
            msku_prep_details=[
                CommonMskuPrepDetailInput(
                    msku="some example string",
                    prep_category=CommonPrepCategory.ADULT,
                    prep_types=[CommonPrepType.ITEM_BLACK_SHRINKWRAP],
                ),
            ],
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetPrepDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SetPrepDetailsRequest](walmart_apis/models/set_prep_details_request.py) \| [SetPrepDetailsRequestDict](walmart_apis/models/set_prep_details_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SetPrepDetailsErrorBody](walmart_apis/errors/set_prep_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_inbound_plan_name(inbound_plan_id: str, body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.wfs_inbound.update_inbound_plan_name(
        "some example string", UpdateInboundPlanNameRequest(name="some example string")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateInboundPlanNameErrorBody
```

**Async**

```python
try:
    await async_client.wfs_inbound.update_inbound_plan_name(
        "some example string", UpdateInboundPlanNameRequest(name="some example string")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateInboundPlanNameErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[UpdateInboundPlanNameRequest](walmart_apis/models/update_inbound_plan_name_request.py) \| [UpdateInboundPlanNameRequestDict](walmart_apis/models/update_inbound_plan_name_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateInboundPlanNameErrorBody](walmart_apis/errors/update_inbound_plan_name_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_item_compliance_details(marketplace_id: str, body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.update_item_compliance_details(
        "some example string",
        UpdateItemComplianceDetailsRequest(msku="some example string", tax_details=CommonTaxDetails()),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateItemComplianceDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.update_item_compliance_details(
        "some example string",
        UpdateItemComplianceDetailsRequest(msku="some example string", tax_details=CommonTaxDetails()),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateItemComplianceDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>marketplace_id</code> | <code>str</code> | The Walmart Marketplace ID. For a list of possible values, refer to [Marketplace IDs](https://developer-docs.walmart.com/seller-api/docs/marketplace-ids). |
| <code>body</code> | <code>[UpdateItemComplianceDetailsRequest](walmart_apis/models/update_item_compliance_details_request.py) \| [UpdateItemComplianceDetailsRequestDict](walmart_apis/models/update_item_compliance_details_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateItemComplianceDetailsErrorBody](walmart_apis/errors/update_item_compliance_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_shipment_name(inbound_plan_id: str, shipment_id: str, body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.wfs_inbound.update_shipment_name(
        "some example string", "some example string", UpdateShipmentNameRequest(name="some example string")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateShipmentNameErrorBody
```

**Async**

```python
try:
    await async_client.wfs_inbound.update_shipment_name(
        "some example string", "some example string", UpdateShipmentNameRequest(name="some example string")
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateShipmentNameErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[UpdateShipmentNameRequest](walmart_apis/models/update_shipment_name_request.py) \| [UpdateShipmentNameRequestDict](walmart_apis/models/update_shipment_name_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateShipmentNameErrorBody](walmart_apis/errors/update_shipment_name_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_shipment_source_address(inbound_plan_id: str, shipment_id: str, body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.update_shipment_source_address(
        "some example string",
        "some example string",
        UpdateShipmentSourceAddressRequest(
            address=CommonAddressInput(
                address_line1="some example string",
                city="some example string",
                country_code="some example string",
                name="some example string",
                phone_number="some example string",
                postal_code="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateShipmentSourceAddressErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.update_shipment_source_address(
        "some example string",
        "some example string",
        UpdateShipmentSourceAddressRequest(
            address=CommonAddressInput(
                address_line1="some example string",
                city="some example string",
                country_code="some example string",
                name="some example string",
                phone_number="some example string",
                postal_code="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateShipmentSourceAddressErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[UpdateShipmentSourceAddressRequest](walmart_apis/models/update_shipment_source_address_request.py) \| [UpdateShipmentSourceAddressRequestDict](walmart_apis/models/update_shipment_source_address_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateShipmentSourceAddressErrorBody](walmart_apis/errors/update_shipment_source_address_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_shipment_tracking_details(inbound_plan_id: str, shipment_id: str, body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.update_shipment_tracking_details(
        "some example string",
        "some example string",
        UpdateShipmentTrackingDetailsRequest(tracking_details=CommonTrackingDetailsInput()),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateShipmentTrackingDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.update_shipment_tracking_details(
        "some example string",
        "some example string",
        UpdateShipmentTrackingDetailsRequest(tracking_details=CommonTrackingDetailsInput()),
    )
    # TODO: Handle 'response' of type CancelInboundPlanResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateShipmentTrackingDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>inbound_plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[UpdateShipmentTrackingDetailsRequest](walmart_apis/models/update_shipment_tracking_details_request.py) \| [UpdateShipmentTrackingDetailsRequestDict](walmart_apis/models/update_shipment_tracking_details_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateShipmentTrackingDetailsErrorBody](walmart_apis/errors/update_shipment_tracking_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorList](walmart_apis/models/common_error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

