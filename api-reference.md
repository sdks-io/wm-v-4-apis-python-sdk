# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [WalmartApisClient](walmart_apis/client.py)

## Authorization

> Source: [Authorization](walmart_apis/apis/authorization.py)

<details>
<summary><code>def create_token(grant_type: GrantTypeOrStr, *, x_o_tenant: str | None = None, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, code_verifier: str | None = None, refresh_token: str | None = None, redirect_uri: str | None = None, scope: str | None = None, request_options: RequestOptionsOrDict | None = None) -> TokenResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The Authorization API exchanges an OAuth grant for an access token. It supports the `client_credentials`, `authorization_code`, and `refresh_token` grant types.

| `grant_type` | Authorization flow | Additional requirements |
|--------------|--------------------|-------------------------|
| `client_credentials` | Seller-direct | Client authentication |
| `authorization_code` | Delegated | `code` and PKCE, or confidential-client authentication and `redirect_uri` |
| `refresh_token` | Delegated | `refresh_token`; public clients also send `client_id` |

**Client authentication:** Confidential clients can authenticate by sending
`client_id` and `client_secret` in the form body (`client_secret_post`) or
by using HTTP Basic authentication. Use only one authentication method.
When using HTTP Basic authentication, omit `client_id` and `client_secret`
from the request body. A request that combines HTTP Basic authentication
with body credentials returns `400` with `invalid_request`.

Public clients send no client secret. Public clients using the
`authorization_code` grant must use PKCE.

**`client_credentials`:** Returns an access token without a refresh token.
To obtain another access token after expiration, submit another
`client_credentials` request. The optional `scope` value is accepted but
does not reduce the access provisioned for the client, and the response
does not echo `scope`.

**`authorization_code`:** Public clients must send a PKCE `code_verifier`.
PKCE uses the `S256` challenge method; `plain` is not accepted.
Confidential clients can omit `code_verifier` when they authenticate at
the token operation and send `redirect_uri`.

**`refresh_token`:** Submit a previously issued `refresh_token` to request
another access token. Public clients also send `client_id`. If `scope` is
provided, it must not exceed the scope originally granted.

Send the returned access token with Marketplace V4 API requests as
`Authorization: Bearer <token>`. Do not use `WM_SEC.ACCESS_TOKEN`.

`x-o-tenant` selects one market when supplied. A direct client active in multiple
markets must supply it; a delegated token's IAM market must match it. Without it,
a direct client with exactly one active market uses that market, and a delegated
token uses its IAM market. Supported values are `WALMART_US`, `WALMART_CA`,
`WALMART_MX`, and `WALMART_CL`.

Treat access tokens, refresh tokens, and client secrets as sensitive values
and do not log them.

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
| <code>grant_type</code> | <code>[GrantTypeOrStr](walmart_apis/models/enums/grant_type.py)</code> | OAuth grant type used to request the access token. |
| <code>x_o_tenant</code> | <code>str \| None</code> | One supported market for the issued access token. Comma-separated values are rejected.<br>**Default**: <code>None</code> |
| <code>client_id</code> | <code>str \| None</code> | Client ID for the application. Provide this property when using client credentials in the request body or when required for a public client. Omit it from the request body when using HTTP Basic authentication.<br>**Default**: <code>None</code> |
| <code>client_secret</code> | <code>str \| None</code> | Client secret used to authenticate a confidential client with credentials in the request body. Omit for public clients and when using HTTP Basic authentication. Treat as a secret and do not log it.<br>**Default**: <code>None</code> |
| <code>code</code> | <code>str \| None</code> | Authorization code returned by Walmart Account Login. Used with the `authorization_code` grant.<br>**Default**: <code>None</code> |
| <code>code_verifier</code> | <code>str \| None</code> | PKCE verifier associated with the `code_challenge` from the authorization<br>request. Required for public clients using the `authorization_code` grant<br>and recommended for all clients. Confidential clients can omit this<br>property only when authenticating at the token operation and providing<br>`redirect_uri`.<br>**Default**: <code>None</code> |
| <code>refresh_token</code> | <code>str \| None</code> | Previously issued refresh token used with the `refresh_token` grant. Treat as a secret and do not log it.<br>**Default**: <code>None</code> |
| <code>redirect_uri</code> | <code>str \| None</code> | Redirect URI for the authorization flow. Required when a confidential<br>client uses the `authorization_code` grant without `code_verifier`.<br>**Default**: <code>None</code> |
| <code>scope</code> | <code>str \| None</code> | Requested OAuth scope. For `client_credentials`, this property is<br>accepted but does not reduce the access provisioned for the client,<br>and the response does not echo the value. For `refresh_token`, the<br>requested scope must not exceed the scope originally granted.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[TokenResponse](walmart_apis/models/token_response.py)</code> -- Returns the access token and related token information.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateTokenErrorBody](walmart_apis/errors/create_token_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 429, 500, 502 | <code>[OAuthErrorModel](walmart_apis/models/o_auth_error_model.py)</code> |
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

Retrieves information about an item in the Walmart Marketplace
catalog using its Walmart Item ID. Returns available product
information for the specified marketplace. Use `includedData`
to select specific data sections, such as attributes, identifiers,
images, and product types.

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
| <code>walmart_item_id</code> | <code>str</code> | Specifies the 14-digit Walmart Item ID of the catalog item to retrieve. |
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Walmart Marketplace identifiers that scope the request. Use `WALMART_US` for the US marketplace. |
| <code>included_data</code> | <code>list&#91;[IncludedDatumOrStr](walmart_apis/models/enums/included_datum.py)&#93; \| None</code> | Product information sections to include in the response.<br>**Default**: <code>None</code> |
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

Searches the Walmart Marketplace catalog using keywords or item identifiers, including Walmart Item IDs, Global Trade Item Numbers (GTINs),
Universal Product Codes (UPCs), and seller SKUs. Returns matching catalog items and requested product information for the specified marketplace.

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
| <code>marketplace_ids</code> | <code>list&#91;str&#93;</code> | Walmart Marketplace identifiers that scope the request. Use `WALMART_US` for the US marketplace. |
| <code>keywords</code> | <code>str \| None</code> | Keywords used to search for matching catalog items.<br>**Default**: <code>None</code> |
| <code>walmart_item_ids</code> | <code>str \| None</code> | Comma-separated Walmart Item IDs to search for, with a maximum of 20 IDs.<br>**Default**: <code>None</code> |
| <code>seller_sku</code> | <code>str \| None</code> | Seller-defined stock keeping unit (SKU) used to search for catalog items.<br>**Default**: <code>None</code> |
| <code>gtin</code> | <code>str \| None</code> | Global Trade Item Number (GTIN) used to search for catalog items. Must contain 14 digits.<br>**Default**: <code>None</code> |
| <code>upc</code> | <code>str \| None</code> | Universal Product Code (UPC) used to search for catalog items. Must contain 12 digits.<br>**Default**: <code>None</code> |
| <code>included_data</code> | <code>list&#91;[IncludedDatumOrStr](walmart_apis/models/enums/included_datum.py)&#93; \| None</code> | Product information sections to include in the response.<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Maximum number of results requested per page (1–20). Defaults to 10.<br>**Default**: <code>10</code> |
| <code>page_token</code> | <code>str \| None</code> | Token for requesting another page, when cursor-based pagination is supported.<br>**Default**: <code>None</code> |
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
Query language is not yet finalized pending ADR (GraphQL vs
REST hybrid — Pod 4).

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
dispute and, if not, the reason for ineligibility.

**Status: not supported** — no GMPPaymentsPlatform endpoint exists for
dispute eligibility checks. Kept in the spec for SDK/client parity and
contract completeness ; always returns 501..

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
| 400, 401, 500, 501 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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

Cancels the feed identified by feedId if it is still queued or in
progress. Mirrors Amazon SP-API `cancelFeed`
(DELETE /feeds/2021-06-30/feeds/{feedId}) for contract-shape parity
above). A feed that has already reached DONE or ERROR cannot be
cancelled.

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
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_feed(feed_type: FeedType1OrStr, file: FileInput, *, content_type: ContentTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> CreateFeedResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Upload a feed file and submit it for asynchronous processing in a single call.
The server handles document storage internally. Use the returned feedId to poll
processing status via GET /v4/feeds/{feed-id}.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.feeds.create_feed(FeedType1.LISTINGS_FEED, Path("path/to/file.bin"))
    # TODO: Handle 'response' of type CreateFeedResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateFeedErrorBody
```

**Async**

```python
try:
    response = await async_client.feeds.create_feed(FeedType1.LISTINGS_FEED, Path("path/to/file.bin"))
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
| <code>feed_type</code> | <code>[FeedType1OrStr](walmart_apis/models/enums/feed_type1.py)</code> | The type of feed being submitted |
| <code>file</code> | <code>FileInput</code> | The feed content file to upload and process |
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
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 403, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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

**Status: not supported** — no GMPPaymentsPlatform endpoint exists for final
payout case tracking. Kept in the spec for SDK/client parity and contract
completeness ; always returns 501..

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
| 400, 401, 404, 500, 501 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_final_payout_case_status(body: UpdateFinalPayoutCaseStatusRequest | UpdateFinalPayoutCaseStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FinalPayoutCaseStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Transitions the authenticated seller's final payout case to Resolved or
Closed, optionally including resolution notes. Requires disbursements:write
scope.

**Status: not supported** — no GMPPaymentsPlatform endpoint exists for final
payout case status writes. Kept in the spec for SDK/client parity and
contract completeness ; always returns 501..

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.final_payout.update_final_payout_case_status(
        UpdateFinalPayoutCaseStatusRequest(status=Status3.RESOLVED)
    )
    # TODO: Handle 'response' of type FinalPayoutCaseStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFinalPayoutCaseStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.final_payout.update_final_payout_case_status(
        UpdateFinalPayoutCaseStatusRequest(status=Status3.RESOLVED)
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
| <code>body</code> | <code>[UpdateFinalPayoutCaseStatusRequest](walmart_apis/models/update_final_payout_case_status_request.py) \| [UpdateFinalPayoutCaseStatusRequestDict](walmart_apis/models/update_final_payout_case_status_request.py)</code> | The request body. |
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
| 400, 401, 404, 500, 501 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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

**Status: not supported** — no upstream endpoint found that models the SP-API
FinancialEventGroup (requires eventGroupId keying, date-range filter, and
cursor pagination). Kept in the spec for SDK/client parity and contract
completeness ; always returns 501..

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
| 400, 401, 403, 404, 429, 500, 501 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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

**Status: not supported** — no upstream maps eventGroupId to a financial
event set. Kept in the spec for SDK/client parity and contract completeness
; always returns 501..

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
| 400, 401, 403, 404, 429, 500, 501 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
            destination_address=AddressFulfillmentOutboundWfs(
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
            destination_address=AddressFulfillmentOutboundWfs(
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
            address=AddressFulfillmentOutboundWfs(
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
            address=AddressFulfillmentOutboundWfs(
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

Bulk inventory update. Max 10 items per request. Exceeding 10 items
returns 400 before this service would otherwise forward the request upstream.

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
| <code>skus</code> | <code>str \| None</code> | Comma-separated seller SKUs (max 10). Exceeding it returns 400 INVALID_REQUEST.<br>**Default**: <code>None</code> |
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
<summary><code>def get_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], *, issue_locale: str | None = "en_US", included_data: list[IncludedDatumListingsItemsOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ItemListingsItems</code></summary>

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
    # TODO: Handle 'response' of type ItemListingsItems
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingsItemErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_items.get_listings_item(
        "some example string", "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type ItemListingsItems
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
| <code>included_data</code> | <code>list&#91;[IncludedDatumListingsItemsOrStr](walmart_apis/models/enums/included_datum_listings_items.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemListingsItems](walmart_apis/models/item_listings_items.py)</code> -- Success

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
<summary><code>def search_listings_items(seller_id: str, marketplace_ids: list[str], *, included_data: list[IncludedDatumListingsItemsOrStr] | None = None, identifier_type: IdentifierTypeListingsItemsOrStr | None = None, identifier_value: str | None = None, lifecycle_status: list[str] | None = None, published_status: list[str] | None = None, unpublished_reasons: list[str] | None = None, inventory_status: list[str] | None = None, fulfillment_type: list[str] | None = None, min_customer_rating: float | None = None, max_customer_rating: float | None = None, min_price: float | None = None, max_price: float | None = None, sort_by: SortByOrStr | None = None, sort_order: SortOrderOrStr | None = SortOrder.ASC, page_size: int | None = 10, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ItemSearchResultsListingsItems</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of the seller's listings items. Mirrors Amazon
SP-API `searchListingsItems` so an existing SP-API client can call the
seller-level collection endpoint (no SKU in the path) against v4.

Filtering and sorting are pushed down to PIQS (Partner Item Query
Service) `POST /v3/items/catalog/search` — the server does the
filtering; callers no longer need to page through the full seller
catalog and filter client-side.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.listings_items.search_listings_items("some example string", ["some example string"])
    # TODO: Handle 'response' of type ItemSearchResultsListingsItems
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SearchListingsItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_items.search_listings_items("some example string", ["some example string"])
    # TODO: Handle 'response' of type ItemSearchResultsListingsItems
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
| <code>included_data</code> | <code>list&#91;[IncludedDatumListingsItemsOrStr](walmart_apis/models/enums/included_datum_listings_items.py)&#93; \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>identifier_type</code> | <code>[IdentifierTypeListingsItemsOrStr](walmart_apis/models/enums/identifier_type_listings_items.py) \| None</code> | Identifier field to search by (PIQS `query.field`). Requires<br>`identifierValue`. PIQS accepts a single field/value pair per<br>call — not a list.<br>**Default**: <code>None</code> |
| <code>identifier_value</code> | <code>str \| None</code> | Value to match for `identifierType`. Ignored if `identifierType` is absent.<br>**Default**: <code>None</code> |
| <code>lifecycle_status</code> | <code>list&#91;str&#93; \| None</code> | Filter to items with any of these lifecycle statuses (PIQS `filters[].field=lifecycleStatus`, op `equals`).<br>**Default**: <code>None</code> |
| <code>published_status</code> | <code>list&#91;str&#93; \| None</code> | Filter to items with any of these publication statuses (e.g. PUBLISHED, UNPUBLISHED, SYSTEM_PROBLEM).<br>**Default**: <code>None</code> |
| <code>unpublished_reasons</code> | <code>list&#91;str&#93; \| None</code> | Filter to items carrying any of these unpublished reasons.<br>**Default**: <code>None</code> |
| <code>inventory_status</code> | <code>list&#91;str&#93; \| None</code> | Filter to items with any of these inventory statuses.<br>**Default**: <code>None</code> |
| <code>fulfillment_type</code> | <code>list&#91;str&#93; \| None</code> | Filter to items with any of these fulfillment types.<br>**Default**: <code>None</code> |
| <code>min_customer_rating</code> | <code>float \| None</code> | Minimum customer rating, inclusive (PIQS `filters[].field=customerRating`, op `between`/`greater_than`).<br>**Default**: <code>None</code> |
| <code>max_customer_rating</code> | <code>float \| None</code> | Maximum customer rating, inclusive.<br>**Default**: <code>None</code> |
| <code>min_price</code> | <code>float \| None</code> | Minimum price, inclusive (PIQS `filters[].field=price`, op `between`/`greater_than`).<br>**Default**: <code>None</code> |
| <code>max_price</code> | <code>float \| None</code> | Maximum price, inclusive.<br>**Default**: <code>None</code> |
| <code>sort_by</code> | <code>[SortByOrStr](walmart_apis/models/enums/sort_by.py) \| None</code> | Field to sort results by (PIQS `sort.field`).<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](walmart_apis/models/enums/sort_order.py) \| None</code> | Sort direction. Ignored if `sortBy` is absent.<br>**Default**: <code>SortOrder.ASC</code> |
| <code>page_size</code> | <code>int \| None</code> | Maximum number of results per page<br>**Default**: <code>10</code> |
| <code>page_token</code> | <code>str \| None</code> | Opaque cursor returned by a previous call for the next page<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ItemSearchResultsListingsItems](walmart_apis/models/item_search_results_listings_items.py)</code> -- Success

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
<summary><code>def get_listings_restrictions(asin: str, condition_type: ConditionTypeListingsRestrictionsOrStr, seller_id: str, marketplace_ids: list[str], *, reason_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> RestrictionList</code></summary>

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
        "some example string", ConditionTypeListingsRestrictions.NEW_NEW, "some example string", ["some example string"]
    )
    # TODO: Handle 'response' of type RestrictionList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingsRestrictionsErrorBody
```

**Async**

```python
try:
    response = await async_client.listings_restrictions.get_listings_restrictions(
        "some example string", ConditionTypeListingsRestrictions.NEW_NEW, "some example string", ["some example string"]
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
| <code>condition_type</code> | <code>[ConditionTypeListingsRestrictionsOrStr](walmart_apis/models/enums/condition_type_listings_restrictions.py)</code> | Value sent with the request. |
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
                ship_from_address=AddressMerchantFulfillmentSellerFulfilledLabels(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                ship_to_address=AddressMerchantFulfillmentSellerFulfilledLabels(
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
                ship_from_address=AddressMerchantFulfillmentSellerFulfilledLabels(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                ship_to_address=AddressMerchantFulfillmentSellerFulfilledLabels(
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
                ship_from_address=AddressMerchantFulfillmentSellerFulfilledLabels(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                ship_to_address=AddressMerchantFulfillmentSellerFulfilledLabels(
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
                ship_from_address=AddressMerchantFulfillmentSellerFulfilledLabels(
                    name="some example string",
                    address_line1="some example string",
                    city="some example string",
                    state_or_region="some example string",
                    postal_code="some example string",
                    country_code="some example string",
                ),
                ship_to_address=AddressMerchantFulfillmentSellerFulfilledLabels(
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

Acknowledges receipt of the specified order lines in a Walmart Marketplace order. Returns the purchase order ID and the timestamp when the acknowledgment was recorded.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Cancels the specified order lines in a Walmart Marketplace order and records the cancellation reason for each line. You can specify the quantity to cancel for each order line. Returns the purchase order ID and the cancellation timestamp.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Records delivery of the specified order lines. For each line, you can provide the delivered quantity,
tracking number, package number, and delivery timestamp. Recording delivery begins the associated invoicing
and return windows.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Retrieves a Walmart Marketplace order, including order status, fulfillment information, and order line details.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Retrieves the shipping address associated with a Walmart Marketplace order,
including the recipient's name and postal address.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Retrieves buyer contact information for a Walmart Marketplace order,
including the buyer's name, email address, and a masked phone number
showing only the last four digits.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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
<summary><code>def get_order_items(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetOrderItemsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the order lines for a Walmart Marketplace order, including
item identifiers, quantities, prices, order line statuses, and
fulfillment information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_order_items("some example string")
    # TODO: Handle 'response' of type GetOrderItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrderItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_order_items("some example string")
    # TODO: Handle 'response' of type GetOrderItemsResponse
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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOrderItemsResponse](walmart_apis/models/get_order_items_response.py)</code> -- Success

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

Retrieves regulated-item verification information for a Walmart Marketplace order,
including applicable age and identity verification requirements.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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
<summary><code>def get_orders(*, created_after: RFC3339DateTime | None = None, created_before: RFC3339DateTime | None = None, last_updated_after: RFC3339DateTime | None = None, order_statuses: list[OrderStatus1OrStr] | None = None, fulfillment_types: list[FulfillmentType1OrStr] | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetOrdersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves Walmart Marketplace orders, including order status,
fulfillment information, and order line details. You can filter
results by a single order status and use pagination to retrieve
additional orders. Use `pageSize` to control the number of orders
returned per page and `nextToken` to retrieve subsequent pages.

## Current limitations (roadmap)
## The underlying the Orders service backend does not yet support
## every filter declared below. Calls using any of the following will
## return `400 Bad Request` with `code=FILTER_NOT_SUPPORTED` and a
## human-readable `message` explaining the specific rejection. Phase
## 2 will lift these one-by-one as the underlying service adds capability.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.orders.get_orders()
    # TODO: Handle 'response' of type GetOrdersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetOrdersErrorBody
```

**Async**

```python
try:
    response = await async_client.orders.get_orders()
    # TODO: Handle 'response' of type GetOrdersResponse
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
| <code>created_after</code> | <code>RFC3339DateTime \| None</code> | Filters orders created after the specified date and time (ISO 8601).<br>This parameter is not currently supported. If provided, the API<br>returns `400` with `FILTER_NOT_SUPPORTED`.<br>**Default**: <code>None</code> |
| <code>created_before</code> | <code>RFC3339DateTime \| None</code> | Filters orders created before the specified date and time (ISO 8601).<br>This parameter is not currently supported. If provided, the API<br>returns `400` with `FILTER_NOT_SUPPORTED`.<br>**Default**: <code>None</code> |
| <code>last_updated_after</code> | <code>RFC3339DateTime \| None</code> | Filters orders updated after the specified date and time (ISO 8601).<br>This parameter is not currently supported. If provided, the API<br>returns `400` with `FILTER_NOT_SUPPORTED`.<br>**Default**: <code>None</code> |
| <code>order_statuses</code> | <code>list&#91;[OrderStatus1OrStr](walmart_apis/models/enums/order_status1.py)&#93; \| None</code> | Filters orders by status. Only one status is supported per request.<br>Providing multiple statuses returns `400` with `FILTER_NOT_SUPPORTED`.<br>**Default**: <code>None</code> |
| <code>fulfillment_types</code> | <code>list&#91;[FulfillmentType1OrStr](walmart_apis/models/enums/fulfillment_type1.py)&#93; \| None</code> | Filters orders by fulfillment type.<br>Not currently supported: Providing this parameter returns `400` with `FILTER_NOT_SUPPORTED`<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | Maximum number of orders to return per page.<br>**Default**: <code>100</code> |
| <code>next_token</code> | <code>str \| None</code> | Pagination token returned in `payload.nextToken` from the previous response. Use this token to retrieve the next page of orders.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOrdersResponse](walmart_apis/models/get_orders_response.py)</code> -- Success

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

Issues a seller-initiated refund for one or more order lines. Provide `refundAmount` and `refundType`
for each line, and optionally include `reason`.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Confirms shipment of the specified order lines in a Walmart Marketplace order, including carrier, tracking number, and shipment date. Returns the purchase order ID and the timestamp when the shipment was recorded.

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
                        carrier=Carrier.UPS,
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
                        carrier=Carrier.UPS,
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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Confirms shipment of a Walmart Marketplace order across multiple
packages and returns the shipment confirmation, including the
number of packages accepted.

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
                        carrier=Carrier.UPS,
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
                        carrier=Carrier.UPS,
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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Updates the shipment status of specified order lines in a Walmart
  Marketplace order, including pickup and in-transit milestones.
  Use the delivery operation to record completed deliveries.

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
            shipment_status=ShipmentStatusOrders.READY_FOR_PICKUP,
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
            shipment_status=ShipmentStatusOrders.READY_FOR_PICKUP,
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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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

Records the outcome of buyer identity or age verification at delivery
for a regulated Walmart Marketplace order. The verification status
indicates whether the buyer's identity was successfully verified or rejected.

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
| <code>purchase_order_id</code> | <code>str</code> | Purchase order identifier assigned by Walmart. |
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
<summary><code>def configure_auto_payout(body: ConfigureAutoPayoutRequest | ConfigureAutoPayoutRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PayoutStatusResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables or disables automatic scheduled payouts for the authenticated seller.
When enabled, payouts are triggered automatically on the standard settlement
cadence. Returns updated payout status. Requires disbursements:write scope.

**Status: not supported** — no GMPPaymentsPlatform endpoint exists for
writing auto-payout configuration. Kept in the spec for SDK/client parity
and contract completeness ; always returns 501..

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.payouts.configure_auto_payout(ConfigureAutoPayoutRequest(enabled=True))
    # TODO: Handle 'response' of type PayoutStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfigureAutoPayoutErrorBody
```

**Async**

```python
try:
    response = await async_client.payouts.configure_auto_payout(ConfigureAutoPayoutRequest(enabled=True))
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
| <code>body</code> | <code>[ConfigureAutoPayoutRequest](walmart_apis/models/configure_auto_payout_request.py) \| [ConfigureAutoPayoutRequestDict](walmart_apis/models/configure_auto_payout_request.py)</code> | The request body. |
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
| 400, 401, 500, 501 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
Completed, Failed, OnHold). Delegates to GMPPaymentsPlatform.

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

**Status: not supported** — no GMPPaymentsPlatform endpoint exists for
initiating a payout on demand. Kept in the spec for SDK/client parity
and contract completeness ; always returns 501..

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
| 400, 401, 409, 500, 501 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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

Returns the attribute JSON Schema for one product type. Validates the product type exists against the live taxonomy (404 otherwise).

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
<summary><code>def get_taxonomy(*, category: str | None = None, locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> Taxonomy</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the category -> product-type-group -> product-type hierarchy, or the subset under one category when `category` is supplied.

** D1 consolidation.** Replaces four V3 operations with one V4 endpoint: `items.getTaxonomyResponse`, `utilities.getTaxonomyResponse` (duplicate full-tree reads), `utilities.getDepartmentList` (call this with no `category`), and `utilities.getCategories` (call this with `category` set to the department/category name — the taxonomy has no separate numeric department id, so the name is the identifier).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_type_definitions.get_taxonomy()
    # TODO: Handle 'response' of type Taxonomy
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTaxonomyErrorBody
```

**Async**

```python
try:
    response = await async_client.product_type_definitions.get_taxonomy()
    # TODO: Handle 'response' of type Taxonomy
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetTaxonomyErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>category</code> | <code>str \| None</code> | Scope the response to one category (matches `TaxonomyCategory.category`).<br>**Default**: <code>None</code> |
| <code>locale</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>"en_US"</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[Taxonomy](walmart_apis/models/taxonomy.py)</code> -- Taxonomy tree

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetTaxonomyErrorBody](walmart_apis/errors/get_taxonomy_error.py)&#93;</code>

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

Lists product types from the Walmart Item Classification taxonomy, optionally narrowed by `keywords` (substring search) or `itemName` (model-backed product-type recommendation for a free-text title).

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
<summary><code>def download_reconciliation_report(reconciliation_report_id: str, partner_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileResponse</code></summary>

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
| <code>reconciliation_report_id</code> | <code>str</code> | Reconciliation report identifier — the report date in MMddyyyy format (e.g. 06172026) |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
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
<summary><code>def cancel_report_schedule(schedule_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelReportScheduleResponse</code></summary>

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
| <code>schedule_id</code> | <code>str</code> | Value sent with the request. |
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
<summary><code>def get_report_schedule(schedule_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ReportSchedule</code></summary>

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
| <code>schedule_id</code> | <code>str</code> | Value sent with the request. |
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

Submits a report request. Poll `GET /v4/reports/{report-id}` for status.
The report type taxonomy for financial reports is not yet finalized.

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
<summary><code>def download_new_report(summary_report_id: str, partner_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileResponse</code></summary>

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
| <code>summary_report_id</code> | <code>str</code> | Settlement summary report identifier — the report date in MMddyyyy format (e.g. 06172026) |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
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
| 400, 401, 404, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_old_report(summary_report_id: str, partner_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileResponse</code></summary>

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
| <code>summary_report_id</code> | <code>str</code> | Settlement summary report identifier — the report date in MMddyyyy format (e.g. 06172026) |
| <code>partner_id</code> | <code>str</code> | Numeric partner/seller ID |
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
| 400, 401, 404, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
<summary><code>def get_report_document(document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ReportDocument</code></summary>

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
| <code>document_id</code> | <code>str</code> | Value sent with the request. |
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
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| <code>page_size</code> | <code>int \| None</code> | Maximum number of results to return per page.<br>**Default**: <code>10</code> |
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
| <code>page_size</code> | <code>int \| None</code> | Maximum number of results to return per page.<br>**Default**: <code>10</code> |
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

**Status: not supported** — no GMPPaymentsPlatform endpoint exists for a
general date-ranged transaction search across all transaction types.
Kept in the spec for SDK/client parity and contract completeness
, including the SP-API `listTransactions` alias above; always
returns 501..

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
| <code>page_size</code> | <code>int \| None</code> | Maximum number of results to return per page.<br>**Default**: <code>10</code> |
| <code>next_token</code> | <code>str \| None</code> | Opaque cursor from a prior response; omit for first page<br>**Default**: <code>None</code> |
| <code>posted_after</code> | <code>RFC3339DateTime \| None</code> | Only return transactions posted after (or on) this date/time (ISO 8601).<br>**Default**: <code>None</code> |
| <code>posted_before</code> | <code>RFC3339DateTime \| None</code> | Only return transactions posted before (but not on) this date/time (ISO 8601).<br>**Default**: <code>None</code> |
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
| 400, 401, 500, 501 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SupplySourceApi

> Source: [SupplySourceApi](walmart_apis/apis/supply_source_api.py)

<details>
<summary><code>def create_supply_source(body: CreateSupplySourceRequest | CreateSupplySourceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateSupplySourceResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new supply source (fulfillment center). Returns only the
`supplySourceId` and `supplySourceCode` of the newly created resource.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.supply_source_api.create_supply_source(
        CreateSupplySourceRequest(supply_source_code="some example string", address=AddressShippingManagement())
    )
    # TODO: Handle 'response' of type CreateSupplySourceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSupplySourceErrorBody
```

**Async**

```python
try:
    response = await async_client.supply_source_api.create_supply_source(
        CreateSupplySourceRequest(supply_source_code="some example string", address=AddressShippingManagement())
    )
    # TODO: Handle 'response' of type CreateSupplySourceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateSupplySourceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateSupplySourceRequest](walmart_apis/models/create_supply_source_request.py) \| [CreateSupplySourceRequestDict](walmart_apis/models/create_supply_source_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CreateSupplySourceResponse](walmart_apis/models/create_supply_source_response.py)</code> -- Supply source created successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CreateSupplySourceErrorBody](walmart_apis/errors/create_supply_source_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 500 | <code>[ErrorListShippingManagement](walmart_apis/models/error_list_shipping_management.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_supply_source(supply_source_id: str, *, request_options: RequestOptionsOrDict | None = None) -> SupplySource</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the supply source (fulfillment center) identified by
`supplySourceId`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.supply_source_api.get_supply_source("some example string")
    # TODO: Handle 'response' of type SupplySource
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSupplySourceErrorBody
```

**Async**

```python
try:
    response = await async_client.supply_source_api.get_supply_source("some example string")
    # TODO: Handle 'response' of type SupplySource
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSupplySourceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>supply_source_id</code> | <code>str</code> | The unique identifier of the supply source. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SupplySource](walmart_apis/models/supply_source.py)</code> -- Supply source returned successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetSupplySourceErrorBody](walmart_apis/errors/get_supply_source_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 429, 500 | <code>[ErrorListShippingManagement](walmart_apis/models/error_list_shipping_management.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_supply_sources(*, request_options: RequestOptionsOrDict | None = None) -> list[SupplySource]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns every supply source (fulfillment center) registered to the
seller ( Phase 2 parity gap: V3's `getAllFulfillmentCenters`
had no V4 equivalent before this).

No pagination today. Planned enhancements for this operation,
including pagination, are tracked and documented in the
[Shipping Settings APIs - V4 Integration](https://confluence.walmart.com/spaces/MTMKTP/pages/3700253502/Shipping+Settings+APIs+-+V4+Integration)
reference doc.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.supply_source_api.list_supply_sources()
    # TODO: Handle 'response' of type list[SupplySource]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSupplySourcesErrorBody
```

**Async**

```python
try:
    response = await async_client.supply_source_api.list_supply_sources()
    # TODO: Handle 'response' of type list[SupplySource]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListSupplySourcesErrorBody
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

**OnSuccess**: <code>list&#91;[SupplySource](walmart_apis/models/supply_source.py)&#93;</code> -- Supply sources returned successfully

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListSupplySourcesErrorBody](walmart_apis/errors/list_supply_sources_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 500 | <code>[ErrorListShippingManagement](walmart_apis/models/error_list_shipping_management.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_supply_source(supply_source_id: str, body: UpdateSupplySourceRequest | UpdateSupplySourceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the supply source (fulfillment center) identified by
`supplySourceId`. Returns 204 on success with no body. On error,
returns the standard error envelope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    client.supply_source_api.update_supply_source("some example string", UpdateSupplySourceRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSupplySourceErrorBody
```

**Async**

```python
try:
    await async_client.supply_source_api.update_supply_source("some example string", UpdateSupplySourceRequest())
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateSupplySourceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>supply_source_id</code> | <code>str</code> | The unique identifier of the supply source to update. |
| <code>body</code> | <code>[UpdateSupplySourceRequest](walmart_apis/models/update_supply_source_request.py) \| [UpdateSupplySourceRequestDict](walmart_apis/models/update_supply_source_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: No content

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateSupplySourceErrorBody](walmart_apis/errors/update_supply_source_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 429, 500 | <code>[ErrorListShippingManagement](walmart_apis/models/error_list_shipping_management.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Uploads

> Source: [Uploads](walmart_apis/apis/uploads.py)

<details>
<summary><code>def create_upload_destination_for_resource(resource: ResourceOrStr, content_type: ContentTypeUploadsFeedDocumentsOrStr, marketplace_ids: list[str], content_md5: str, *, request_options: RequestOptionsOrDict | None = None) -> CreateUploadDestinationResponse</code></summary>

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
        Resource.FEEDS,
        ContentTypeUploadsFeedDocuments.TEXT_XML_CHARSET_UTF_8,
        ["some example string"],
        "some example string",
    )
    # TODO: Handle 'response' of type CreateUploadDestinationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateUploadDestinationForResourceErrorBody
```

**Async**

```python
try:
    response = await async_client.uploads.create_upload_destination_for_resource(
        Resource.FEEDS,
        ContentTypeUploadsFeedDocuments.TEXT_XML_CHARSET_UTF_8,
        ["some example string"],
        "some example string",
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
| <code>content_type</code> | <code>[ContentTypeUploadsFeedDocumentsOrStr](walmart_apis/models/enums/content_type_uploads_feed_documents.py)</code> | MIME type of the content to be uploaded |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[RawError](walmart_apis/core/results.py)</code> |
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

Returns the estimated fees for an item identified by Walmart Item ID, based on the pricing and fulfillment information provided in the request.

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
| <code>walmart_item_id</code> | <code>str</code> | Walmart Item ID of the item. |
| <code>body</code> | <code>[GetMyFeesEstimateRequest](walmart_apis/models/get_my_fees_estimate_request.py) \| [GetMyFeesEstimateRequestDict](walmart_apis/models/get_my_fees_estimate_request.py)</code> | Pricing and fulfillment information used to estimate fees for the item. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetMyFeesEstimateResponse](walmart_apis/models/get_my_fees_estimate_response.py)</code> -- Returns the fee estimate result for the requested item.

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

Returns the estimated fees for a seller listing identified by seller SKU using the pricing and fulfillment information provided in the request.

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
| <code>seller_sku</code> | <code>str</code> | Seller SKU for the listing. Scoped to the authenticated seller. |
| <code>marketplace_id</code> | <code>str</code> | Marketplace identifier. |
| <code>body</code> | <code>[GetMyFeesEstimateRequest](walmart_apis/models/get_my_fees_estimate_request.py) \| [GetMyFeesEstimateRequestDict](walmart_apis/models/get_my_fees_estimate_request.py)</code> | Pricing and fulfillment information used to estimate fees for the listing. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetMyFeesEstimateResponse](walmart_apis/models/get_my_fees_estimate_response.py)</code> -- Returns the fee estimate result for the specified listing.

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

Returns estimated Walmart fees for multiple items identified by Walmart Item ID or seller SKU.

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
                    price_to_estimate_fees=PriceToEstimateFees(listing_price=MoneyTypeProductFees()),
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
                    price_to_estimate_fees=PriceToEstimateFees(listing_price=MoneyTypeProductFees()),
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
| <code>body</code> | <code>list&#91;[FeesEstimateByIdRequest](walmart_apis/models/fees_estimate_by_id_request.py) \| [FeesEstimateByIdRequestDict](walmart_apis/models/fees_estimate_by_id_request.py)&#93;</code> | Fee estimate requests for items identified by Walmart Item ID or seller SKU, including pricing and fulfillment information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>list&#91;[FeesEstimateResult](walmart_apis/models/fees_estimate_result.py)&#93;</code> -- Returns fee estimate results for the requested items.

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
<summary><code>def get_buybox_offer_expected_price_batch(body: GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetBuyboxOfferExpectedPriceBatchResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

**Planned — not yet available in production.** Returns the Buybox Offer Expected Price (BOEP) for a batch of seller SKUs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_buybox_offer_expected_price_batch(GetBuyboxOfferExpectedPriceBatchRequest())
    # TODO: Handle 'response' of type GetBuyboxOfferExpectedPriceBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBuyboxOfferExpectedPriceBatchErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_buybox_offer_expected_price_batch(
        GetBuyboxOfferExpectedPriceBatchRequest()
    )
    # TODO: Handle 'response' of type GetBuyboxOfferExpectedPriceBatchResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBuyboxOfferExpectedPriceBatchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetBuyboxOfferExpectedPriceBatchRequest](walmart_apis/models/get_buybox_offer_expected_price_batch_request.py) \| [GetBuyboxOfferExpectedPriceBatchRequestDict](walmart_apis/models/get_buybox_offer_expected_price_batch_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetBuyboxOfferExpectedPriceBatchResponse](walmart_apis/models/get_buybox_offer_expected_price_batch_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetBuyboxOfferExpectedPriceBatchErrorBody](walmart_apis/errors/get_buybox_offer_expected_price_batch_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[ErrorCatalogItems](walmart_apis/models/error_catalog_items.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_competitive_pricing(*, item_type: ItemTypeOrStr = ItemType.SKU, skus: list[str] | None = None, walmart_item_ids: list[str] | None = None, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetPricingResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns competitive pricing information for seller offer listings identified by seller SKU or Walmart Item ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_competitive_pricing(item_type=ItemType.WALMART_ITEM_ID)
    # TODO: Handle 'response' of type GetPricingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCompetitivePricingErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_competitive_pricing(item_type=ItemType.WALMART_ITEM_ID)
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
| <code>item_type</code> | <code>[ItemTypeOrStr](walmart_apis/models/enums/item_type.py)</code> | Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested items.<br>**Default**: <code>ItemType.SKU</code> |
| <code>skus</code> | <code>list&#91;str&#93; \| None</code> | Seller SKUs that identify the items to return. Supports up to 20 values.<br>**Default**: <code>None</code> |
| <code>walmart_item_ids</code> | <code>list&#91;str&#93; \| None</code> | Walmart Item IDs that identify the items to return. Supports up to 20 values.<br>**Default**: <code>None</code> |
| <code>customer_type</code> | <code>[CustomerTypeOrStr](walmart_apis/models/enums/customer_type.py) \| None</code> | Indicates whether to request `Consumer` or `Business` offers. The default is `Consumer`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetPricingResponse](walmart_apis/models/get_pricing_response.py)</code> -- Returns competitive pricing information for the requested seller items.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetCompetitivePricingErrorBody](walmart_apis/errors/get_competitive_pricing_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[ErrorCatalogItems](walmart_apis/models/error_catalog_items.py)&#93;</code> |
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

**Planned — not yet available in production.** Returns competitive summary information, including featured buying options and lowest-priced offers, for a batch of Walmart Item IDs.

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

**OnSuccess**: <code>[CompetitiveSummaryBatchResponse](walmart_apis/models/competitive_summary_batch_response.py)</code> -- Returns competitive summary results for the requested Walmart items.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetCompetitiveSummaryErrorBody](walmart_apis/errors/get_competitive_summary_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[ErrorCatalogItems](walmart_apis/models/error_catalog_items.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_item_offers(item_id: str, item_condition: ConditionTypeProductPricingOrStr, *, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetOffersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the lowest-priced offers for a Walmart item with the specified item condition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_item_offers("some example string", ConditionTypeProductPricing.NEW)
    # TODO: Handle 'response' of type GetOffersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetItemOffersErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_item_offers(
        "some example string", ConditionTypeProductPricing.NEW
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
| <code>item_id</code> | <code>str</code> | Walmart Item ID that identifies the item. |
| <code>item_condition</code> | <code>[ConditionTypeProductPricingOrStr](walmart_apis/models/enums/condition_type_product_pricing.py)</code> | Filters the offer listings based on item condition. Possible values are `New`, `Restored`, and `Pre-Owned`. |
| <code>customer_type</code> | <code>[CustomerTypeOrStr](walmart_apis/models/enums/customer_type.py) \| None</code> | Indicates whether to request `Consumer` or `Business` offers. The default is `Consumer`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOffersResponse](walmart_apis/models/get_offers_response.py)</code> -- Returns the lowest-priced offers for the requested Walmart item.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetItemOffersErrorBody](walmart_apis/errors/get_item_offers_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[ErrorCatalogItems](walmart_apis/models/error_catalog_items.py)&#93;</code> |
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

Returns offer information for up to 20 Walmart Item ID requests. Each response entry contains an HTTP status for its corresponding item request.

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

**OnSuccess**: <code>[GetItemOffersBatchResponse](walmart_apis/models/get_item_offers_batch_response.py)</code> -- Returns the results for the requested Walmart items.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetItemOffersBatchErrorBody](walmart_apis/errors/get_item_offers_batch_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[ErrorCatalogItems](walmart_apis/models/error_catalog_items.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_listing_offers(seller_sku: str, item_condition: ConditionTypeProductPricingOrStr, *, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetOffersResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the lowest-priced offers for a single SKU listing, based on SKU and item condition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_listing_offers("some example string", ConditionTypeProductPricing.NEW)
    # TODO: Handle 'response' of type GetOffersResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListingOffersErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_listing_offers(
        "some example string", ConditionTypeProductPricing.NEW
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
| <code>seller_sku</code> | <code>str</code> | Seller SKU that identifies the item in the specified marketplace. The `SellerSKU` value is qualified by the seller's `SellerId`. |
| <code>item_condition</code> | <code>[ConditionTypeProductPricingOrStr](walmart_apis/models/enums/condition_type_product_pricing.py)</code> | Filters the offer listings based on item condition. Possible values are `New`, `Restored`, and `Pre-Owned`. |
| <code>customer_type</code> | <code>[CustomerTypeOrStr](walmart_apis/models/enums/customer_type.py) \| None</code> | Indicates whether to request `Consumer` or `Business` offers. The default is `Consumer`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetOffersResponse](walmart_apis/models/get_offers_response.py)</code> -- Returns the lowest-priced offers for the requested seller SKU.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetListingOffersErrorBody](walmart_apis/errors/get_listing_offers_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[ErrorCatalogItems](walmart_apis/models/error_catalog_items.py)&#93;</code> |
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

Returns offer information for up to 20 seller SKU requests. Each response entry contains an HTTP status for its corresponding seller SKU request.

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

**OnSuccess**: <code>[GetListingOffersBatchResponse](walmart_apis/models/get_listing_offers_batch_response.py)</code> -- Returns the results for the requested seller SKUs.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetListingOffersBatchErrorBody](walmart_apis/errors/get_listing_offers_batch_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[ErrorCatalogItems](walmart_apis/models/error_catalog_items.py)&#93;</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_pricing(*, item_type: ItemTypeOrStr = ItemType.SKU, skus: list[str] | None = None, walmart_item_ids: list[str] | None = None, item_condition: ConditionTypeProductPricingOrStr | None = None, offer_type: OfferCustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetPricingResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns pricing information for the seller's listings, identified by seller SKU or Walmart Item ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.product_pricing.get_pricing(item_type=ItemType.WALMART_ITEM_ID)
    # TODO: Handle 'response' of type GetPricingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPricingErrorBody
```

**Async**

```python
try:
    response = await async_client.product_pricing.get_pricing(item_type=ItemType.WALMART_ITEM_ID)
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
| <code>item_type</code> | <code>[ItemTypeOrStr](walmart_apis/models/enums/item_type.py)</code> | Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested items.<br>**Default**: <code>ItemType.SKU</code> |
| <code>skus</code> | <code>list&#91;str&#93; \| None</code> | Seller SKUs that identify the items to return. Supports up to 20 values.<br>**Default**: <code>None</code> |
| <code>walmart_item_ids</code> | <code>list&#91;str&#93; \| None</code> | Walmart Item IDs that identify the items to return. Supports up to 20 values.<br>**Default**: <code>None</code> |
| <code>item_condition</code> | <code>[ConditionTypeProductPricingOrStr](walmart_apis/models/enums/condition_type_product_pricing.py) \| None</code> | Filters the offer listings based on item condition. Possible values are `New`, `Restored`, and `Pre-Owned`.<br>**Default**: <code>None</code> |
| <code>offer_type</code> | <code>[OfferCustomerTypeOrStr](walmart_apis/models/enums/offer_customer_type.py) \| None</code> | Filters pricing information by business-to-consumer (`B2C`) or business-to-business (`B2B`) offer type. Default is `B2C`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetPricingResponse](walmart_apis/models/get_pricing_response.py)</code> -- Returns pricing information for the requested seller items.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetPricingErrorBody](walmart_apis/errors/get_pricing_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>list&#91;[ErrorCatalogItems](walmart_apis/models/error_catalog_items.py)&#93;</code> |
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
<summary><code>def cancel_shipment2(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelShipmentResponseShipping</code></summary>

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
    # TODO: Handle 'response' of type CancelShipmentResponseShipping
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelShipment2ErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.cancel_shipment2("some example string")
    # TODO: Handle 'response' of type CancelShipmentResponseShipping
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

**OnSuccess**: <code>[CancelShipmentResponseShipping](walmart_apis/models/cancel_shipment_response_shipping.py)</code> -- Cancellation processed

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
<summary><code>def get_rates(body: GetRatesRequest | GetRatesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GetRatesResponse</code></summary>

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
            ship_to=AddressMerchantFulfillmentSellerFulfilledLabels(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            ship_from=AddressMerchantFulfillmentSellerFulfilledLabels(
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
    # TODO: Handle 'response' of type GetRatesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetRatesErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.get_rates(
        GetRatesRequest(
            ship_to=AddressMerchantFulfillmentSellerFulfilledLabels(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            ship_from=AddressMerchantFulfillmentSellerFulfilledLabels(
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
    # TODO: Handle 'response' of type GetRatesResponse
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

**OnSuccess**: <code>[GetRatesResponse](walmart_apis/models/get_rates_response.py)</code> -- Rate quotes returned successfully

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
<summary><code>def get_shipment_documents(shipment_id: str, *, package_client_reference_id: str | None = None, format_: FormatShippingOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> GetShipmentDocumentsResponse</code></summary>

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
| <code>format_</code> | <code>[FormatShippingOrStr](walmart_apis/models/enums/format_shipping.py) \| None</code> | Requested document format (defaults to PDF).<br>**Default**: <code>None</code> |
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
<summary><code>def one_click_shipment(body: OneClickShipmentRequest | OneClickShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> OneClickShipmentResponse</code></summary>

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
            ship_to=AddressMerchantFulfillmentSellerFulfilledLabels(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            ship_from=AddressMerchantFulfillmentSellerFulfilledLabels(
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
                format=FormatShipping.PDF, size=Size(), dpi=Dpi.VALUE_203
            ),
            channel_details=ChannelDetails(channel_type=ChannelType.WALMART_MARKETPLACE),
        ),
    )
    # TODO: Handle 'response' of type OneClickShipmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type OneClickShipmentErrorBody
```

**Async**

```python
try:
    response = await async_client.shipping.one_click_shipment(
        OneClickShipmentRequest(
            ship_to=AddressMerchantFulfillmentSellerFulfilledLabels(
                name="some example string",
                address_line1="some example string",
                city="some example string",
                state_or_region="some example string",
                postal_code="some example string",
                country_code="some example string",
            ),
            ship_from=AddressMerchantFulfillmentSellerFulfilledLabels(
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
                format=FormatShipping.PDF, size=Size(), dpi=Dpi.VALUE_203
            ),
            channel_details=ChannelDetails(channel_type=ChannelType.WALMART_MARKETPLACE),
        ),
    )
    # TODO: Handle 'response' of type OneClickShipmentResponse
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

**OnSuccess**: <code>[OneClickShipmentResponse](walmart_apis/models/one_click_shipment_response.py)</code> -- Shipment purchased successfully

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
<summary><code>def purchase_shipment(body: PurchaseShipmentRequest | PurchaseShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> PurchaseShipmentResponse</code></summary>

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
                format=FormatShipping.PDF, size=Size(), dpi=Dpi.VALUE_203
            ),
        ),
    )
    # TODO: Handle 'response' of type PurchaseShipmentResponse
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
                format=FormatShipping.PDF, size=Size(), dpi=Dpi.VALUE_203
            ),
        ),
    )
    # TODO: Handle 'response' of type PurchaseShipmentResponse
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

**OnSuccess**: <code>[PurchaseShipmentResponse](walmart_apis/models/purchase_shipment_response.py)</code> -- Shipment purchased successfully

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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
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
| 400, 401, 403, 404, 429, 500 | <code>[ErrorList](walmart_apis/models/error_list.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WfsInbound

> Source: [WfsInbound](walmart_apis/apis/wfs_inbound.py)

<details>
<summary><code>def cancel_inbound_plan(plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelInboundPlanResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels an inbound plan when its current status allows cancellation.

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
| <code>plan_id</code> | <code>str</code> | Unique identifier of the inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_self_ship_appointment(plan_id: str, shipment_id: str, body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CancelSelfShipAppointmentResponse</code></summary>

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
    # TODO: Handle 'response' of type CancelSelfShipAppointmentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelSelfShipAppointmentErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.cancel_self_ship_appointment(
        "some example string", "some example string", CancelSelfShipAppointmentRequest()
    )
    # TODO: Handle 'response' of type CancelSelfShipAppointmentResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[CancelSelfShipAppointmentRequest](walmart_apis/models/cancel_self_ship_appointment_request.py) \| [CancelSelfShipAppointmentRequestDict](walmart_apis/models/cancel_self_ship_appointment_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[CancelSelfShipAppointmentResponse](walmart_apis/models/cancel_self_ship_appointment_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[CancelSelfShipAppointmentErrorBody](walmart_apis/errors/cancel_self_ship_appointment_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_delivery_window_options(plan_id: str, shipment_id: str, delivery_window_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ConfirmDeliveryWindowOptionsResponse</code></summary>

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
    # TODO: Handle 'response' of type ConfirmDeliveryWindowOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmDeliveryWindowOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_delivery_window_options(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type ConfirmDeliveryWindowOptionsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | The shipment to confirm the delivery window option for. |
| <code>delivery_window_option_id</code> | <code>str</code> | The ID of the delivery window option to be confirmed. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConfirmDeliveryWindowOptionsResponse](walmart_apis/models/confirm_delivery_window_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmDeliveryWindowOptionsErrorBody](walmart_apis/errors/confirm_delivery_window_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_packing_option(plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ConfirmPackingOptionResponse</code></summary>

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
    # TODO: Handle 'response' of type ConfirmPackingOptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmPackingOptionErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_packing_option("some example string", "some example string")
    # TODO: Handle 'response' of type ConfirmPackingOptionResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>packing_option_id</code> | <code>str</code> | Identifier of a packing option. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConfirmPackingOptionResponse](walmart_apis/models/confirm_packing_option_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmPackingOptionErrorBody](walmart_apis/errors/confirm_packing_option_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_placement_option(plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ConfirmPlacementOptionResponse</code></summary>

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
    # TODO: Handle 'response' of type ConfirmPlacementOptionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmPlacementOptionErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_placement_option("some example string", "some example string")
    # TODO: Handle 'response' of type ConfirmPlacementOptionResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>placement_option_id</code> | <code>str</code> | The identifier of a placement option. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConfirmPlacementOptionResponse](walmart_apis/models/confirm_placement_option_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmPlacementOptionErrorBody](walmart_apis/errors/confirm_placement_option_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_shipment_content_update_preview(plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ConfirmShipmentContentUpdatePreviewResponse</code></summary>

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
    # TODO: Handle 'response' of type ConfirmShipmentContentUpdatePreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ConfirmShipmentContentUpdatePreviewErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.confirm_shipment_content_update_preview(
        "some example string", "some example string", "some example string"
    )
    # TODO: Handle 'response' of type ConfirmShipmentContentUpdatePreviewResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>content_update_preview_id</code> | <code>str</code> | Identifier of a content update preview. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConfirmShipmentContentUpdatePreviewResponse](walmart_apis/models/confirm_shipment_content_update_preview_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmShipmentContentUpdatePreviewErrorBody](walmart_apis/errors/confirm_shipment_content_update_preview_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def confirm_transportation_options(plan_id: str, body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ConfirmTransportationOptionsResponse</code></summary>

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
    # TODO: Handle 'response' of type ConfirmTransportationOptionsResponse
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
    # TODO: Handle 'response' of type ConfirmTransportationOptionsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[ConfirmTransportationOptionsRequest](walmart_apis/models/confirm_transportation_options_request.py) \| [ConfirmTransportationOptionsRequestDict](walmart_apis/models/confirm_transportation_options_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ConfirmTransportationOptionsResponse](walmart_apis/models/confirm_transportation_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ConfirmTransportationOptionsErrorBody](walmart_apis/errors/confirm_transportation_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
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

Creates an inbound plan for items to be shipped to Walmart fulfillment centers.

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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_delivery_window_options(plan_id: str, shipment_id: str, *, scac: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GenerateDeliveryWindowOptionsResponse</code></summary>

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
    # TODO: Handle 'response' of type GenerateDeliveryWindowOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateDeliveryWindowOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_delivery_window_options(
        "some example string", "some example string"
    )
    # TODO: Handle 'response' of type GenerateDeliveryWindowOptionsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | The shipment to generate delivery window options for. |
| <code>scac</code> | <code>str \| None</code> | Walmart extension (not in SP-API). Standard Carrier Alpha Code of the carrier delivering the shipment, case preserved. Supplying it generates drop trailer windows; omitting it generates live unload windows. The delivery type chosen here is kept when a generated window is confirmed. Carrier existence and drop trailer eligibility are validated when the window is confirmed.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenerateDeliveryWindowOptionsResponse](walmart_apis/models/generate_delivery_window_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GenerateDeliveryWindowOptionsErrorBody](walmart_apis/errors/generate_delivery_window_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_packing_options(plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GeneratePackingOptionsResponse</code></summary>

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
    # TODO: Handle 'response' of type GeneratePackingOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePackingOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_packing_options("some example string")
    # TODO: Handle 'response' of type GeneratePackingOptionsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GeneratePackingOptionsResponse](walmart_apis/models/generate_packing_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GeneratePackingOptionsErrorBody](walmart_apis/errors/generate_packing_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_placement_options(plan_id: str, body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GeneratePlacementOptionsResponse</code></summary>

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
    # TODO: Handle 'response' of type GeneratePlacementOptionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GeneratePlacementOptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_placement_options(
        "some example string", GeneratePlacementOptionsRequest()
    )
    # TODO: Handle 'response' of type GeneratePlacementOptionsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[GeneratePlacementOptionsRequest](walmart_apis/models/generate_placement_options_request.py) \| [GeneratePlacementOptionsRequestDict](walmart_apis/models/generate_placement_options_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GeneratePlacementOptionsResponse](walmart_apis/models/generate_placement_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GeneratePlacementOptionsErrorBody](walmart_apis/errors/generate_placement_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_self_ship_appointment_slots(plan_id: str, shipment_id: str, body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenerateSelfShipAppointmentSlotsResponse</code></summary>

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
    # TODO: Handle 'response' of type GenerateSelfShipAppointmentSlotsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateSelfShipAppointmentSlotsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.generate_self_ship_appointment_slots(
        "some example string", "some example string", GenerateSelfShipAppointmentSlotsRequest()
    )
    # TODO: Handle 'response' of type GenerateSelfShipAppointmentSlotsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[GenerateSelfShipAppointmentSlotsRequest](walmart_apis/models/generate_self_ship_appointment_slots_request.py) \| [GenerateSelfShipAppointmentSlotsRequestDict](walmart_apis/models/generate_self_ship_appointment_slots_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenerateSelfShipAppointmentSlotsResponse](walmart_apis/models/generate_self_ship_appointment_slots_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GenerateSelfShipAppointmentSlotsErrorBody](walmart_apis/errors/generate_self_ship_appointment_slots_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_shipment_content_update_previews(plan_id: str, shipment_id: str, body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenerateShipmentContentUpdatePreviewsResponse</code></summary>

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
    # TODO: Handle 'response' of type GenerateShipmentContentUpdatePreviewsResponse
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
    # TODO: Handle 'response' of type GenerateShipmentContentUpdatePreviewsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[GenerateShipmentContentUpdatePreviewsRequest](walmart_apis/models/generate_shipment_content_update_previews_request.py) \| [GenerateShipmentContentUpdatePreviewsRequestDict](walmart_apis/models/generate_shipment_content_update_previews_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenerateShipmentContentUpdatePreviewsResponse](walmart_apis/models/generate_shipment_content_update_previews_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GenerateShipmentContentUpdatePreviewsErrorBody](walmart_apis/errors/generate_shipment_content_update_previews_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_transportation_options(plan_id: str, body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenerateTransportationOptionsResponse</code></summary>

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
    # TODO: Handle 'response' of type GenerateTransportationOptionsResponse
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
    # TODO: Handle 'response' of type GenerateTransportationOptionsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[GenerateTransportationOptionsRequest](walmart_apis/models/generate_transportation_options_request.py) \| [GenerateTransportationOptionsRequestDict](walmart_apis/models/generate_transportation_options_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GenerateTransportationOptionsResponse](walmart_apis/models/generate_transportation_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GenerateTransportationOptionsErrorBody](walmart_apis/errors/generate_transportation_options_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_bill_of_lading(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetBillOfLadingResponse</code></summary>

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
    response = client.wfs_inbound.get_bill_of_lading("some example string")
    # TODO: Handle 'response' of type GetBillOfLadingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBillOfLadingErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_bill_of_lading("some example string")
    # TODO: Handle 'response' of type GetBillOfLadingResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetBillOfLadingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetBillOfLadingResponse](walmart_apis/models/get_bill_of_lading_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetBillOfLadingErrorBody](walmart_apis/errors/get_bill_of_lading_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_delivery_challan_document(plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetDeliveryChallanDocumentResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
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

Retrieves the status of an inbound plan operation, such as creating or canceling a plan.

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
| <code>operation_id</code> | <code>str</code> | Unique identifier for the operation. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_inbound_plan(plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> InboundPlan</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the details of an inbound plan.

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
| <code>plan_id</code> | <code>str</code> | Unique identifier of the inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_item_eligibility_preview(item_id: str, program: Program1OrStr, *, marketplace_ids: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetItemEligibilityPreviewResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Checks whether an item is eligible for the specified program.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_item_eligibility_preview("some example string", Program1.INBOUND)
    # TODO: Handle 'response' of type GetItemEligibilityPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetItemEligibilityPreviewErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_item_eligibility_preview("some example string", Program1.INBOUND)
    # TODO: Handle 'response' of type GetItemEligibilityPreviewResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetItemEligibilityPreviewErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>item_id</code> | <code>str</code> | Walmart item identifier for which to retrieve an eligibility preview. |
| <code>program</code> | <code>[Program1OrStr](walmart_apis/models/enums/program1.py)</code> | Program for which to evaluate item eligibility. |
| <code>marketplace_ids</code> | <code>str \| None</code> | Marketplace identifier to use when determining item eligibility.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetItemEligibilityPreviewResponse](walmart_apis/models/get_item_eligibility_preview_response.py)</code> -- Eligibility preview resolved successfully.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetItemEligibilityPreviewErrorBody](walmart_apis/errors/get_item_eligibility_preview_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_labels(shipment_id: str, page_type: PageTypeOrStr, label_type: LabelTypeOrStr, *, page_size: int | None = None, page_start_index: int | None = None, request_options: RequestOptionsOrDict | None = None) -> GetLabelsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns package/pallet labels for faster and more accurate shipment processing at the Walmart fulfillment center.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_labels("some example string", PageType.PACKAGE_LABEL_4X6, LabelType.UNIQUE)
    # TODO: Handle 'response' of type GetLabelsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLabelsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_labels(
        "some example string", PageType.PACKAGE_LABEL_4X6, LabelType.UNIQUE
    )
    # TODO: Handle 'response' of type GetLabelsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLabelsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>page_type</code> | <code>[PageTypeOrStr](walmart_apis/models/enums/page_type.py)</code> | The page size/format to use for label printing (upstream `PageType`). Determines the physical layout of the generated label file. |
| <code>label_type</code> | <code>[LabelTypeOrStr](walmart_apis/models/enums/label_type.py)</code> | The type of label to retrieve (upstream `LabelType`). `UNIQUE` is a carrier-assigned unique shipping label (PARCEL shipments only); `BARCODE_2D` is a 2D barcode receiving/box label; `PALLET` is a pallet receiving label (non-PARCEL modes only). |
| <code>page_size</code> | <code>int \| None</code> | The page size for paginating through the total packages' labels. Maximum 1000 (upstream `PageSize`, default 100).<br>**Default**: <code>None</code> |
| <code>page_start_index</code> | <code>int \| None</code> | The zero-based page start index for paginating through the total packages' labels (upstream `PageStartIndex`, default 0).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetLabelsResponse](walmart_apis/models/get_labels_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetLabelsErrorBody](walmart_apis/errors/get_labels_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_prep_instructions(ship_to_country_code: str, *, seller_sku_list: list[str] | None = None, asin_list: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> GetPrepInstructionsResponse</code></summary>

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
    response = client.wfs_inbound.get_prep_instructions("some example string")
    # TODO: Handle 'response' of type GetPrepInstructionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPrepInstructionsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_prep_instructions("some example string")
    # TODO: Handle 'response' of type GetPrepInstructionsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetPrepInstructionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ship_to_country_code</code> | <code>str</code> | The two-letter country code of the destination the item(s) will ship to. |
| <code>seller_sku_list</code> | <code>list&#91;str&#93; \| None</code> | A list of seller SKUs to retrieve prep instructions for.<br>**Default**: <code>None</code> |
| <code>asin_list</code> | <code>list&#91;str&#93; \| None</code> | A list of ASINs to retrieve prep instructions for.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetPrepInstructionsResponse](walmart_apis/models/get_prep_instructions_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetPrepInstructionsErrorBody](walmart_apis/errors/get_prep_instructions_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_self_ship_appointment_slots(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetSelfShipAppointmentSlotsResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment(plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CommonShipment</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment_content_update_preview(plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CommonContentUpdatePreview</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment_items(*, date_range_filter: DateRangeFilterOrStr | None = None, date_range_value: str | None = None, page_size: int | None = 10, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetShipmentItemsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike `getShipmentItemsByShipmentId` and `listShipmentItems`, this op is NOT shipment- or plan-scoped -- it searches item rows across ALL of a seller's shipments, date- filtered. Field naming deliberately uses the Amazon SP-API-parity names `sellerSku`/ `fulfillmentNetworkSKU` (per explicit mapping instructions) rather than the `msku`/`fnsku` shorthand its shipment-/plan-scoped siblings settled on -- this is a genuinely new v4 response shape with no naming precedent of its own to preserve.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_shipment_items()
    # TODO: Handle 'response' of type GetShipmentItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_shipment_items()
    # TODO: Handle 'response' of type GetShipmentItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentItemsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>date_range_filter</code> | <code>[DateRangeFilterOrStr](walmart_apis/models/enums/date_range_filter.py) \| None</code> | Which date field `dateRangeValue` filters on (upstream `dateRangeFilter`).<br>**Default**: <code>None</code> |
| <code>date_range_value</code> | <code>str \| None</code> | ISO 8601 datetime paired with `dateRangeFilter` (upstream `dateRangeValue`).<br>**Default**: <code>None</code> |
| <code>page_size</code> | <code>int \| None</code> | The number of items to return in the response matching the given query.<br>**Default**: <code>10</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch the next page of a previous `getShipmentItems` query. Pass the value of `pagination.nextToken` from a previous response. Forwarded upstream as `nextToken` (already lowerCamelCase on this op, unlike `getShipments`' `NextToken`).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetShipmentItemsResponse](walmart_apis/models/get_shipment_items_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetShipmentItemsErrorBody](walmart_apis/errors/get_shipment_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipment_items_by_shipment_id(shipment_id: str, *, page_size: int | None = 10, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetShipmentItemsByShipmentIdResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike listShipmentItems, this op is NOT inboundPlan-scoped -- it reads a CONFIRMED shipment directly by shipmentId (the upstream shipmentRefId / externalReferenceId), with no draft-lookup fallback.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_shipment_items_by_shipment_id("some example string")
    # TODO: Handle 'response' of type GetShipmentItemsByShipmentIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentItemsByShipmentIdErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_shipment_items_by_shipment_id("some example string")
    # TODO: Handle 'response' of type GetShipmentItemsByShipmentIdResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentItemsByShipmentIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shipment_id</code> | <code>str</code> | Identifier of a confirmed shipment (shipmentRefId / externalReferenceId). |
| <code>page_size</code> | <code>int \| None</code> | The number of items to return in the response matching the given query.<br>**Default**: <code>10</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results. Pass the value of `pagination.nextToken` from a previous response to fetch the next page. Upstream Inbound Order Workflow returns this cursor as `NextToken` in the response payload ; it is mapped through unchanged into `pagination.nextToken` here -- the request-side parameter name stays `paginationToken` for consistency with every other list operation in this API.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetShipmentItemsByShipmentIdResponse](walmart_apis/models/get_shipment_items_by_shipment_id_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetShipmentItemsByShipmentIdErrorBody](walmart_apis/errors/get_shipment_items_by_shipment_id_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shipments(query_type: ShipmentsQueryTypeOrStr, *, shipment_id_list: list[str] | None = None, shipment_status_list: list[ShipmentStatusOrStr] | None = None, last_updated_after: str | None = None, last_updated_before: str | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetShipmentsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike every shipment op above, this is NOT plan- or shipment-scoped -- it searches across ALL of a seller's shipments. Behavior is driven by `queryType`:
  - `SHIPMENT`: requires exactly one of `shipmentIdList` or `shipmentStatusList` (never
    both, never neither -- , tightened to match an upstream spec update).
  - `DATE_RANGE`: requires `lastUpdatedAfter` (`lastUpdatedBefore` is optional);
    `shipmentStatusList` may be supplied as an additional filter.
  - `NEXT_TOKEN`: requires `paginationToken` (the value returned in a previous response's
    `pagination.nextToken`) to fetch the next page of the SAME query; resend the original
    `shipmentIdList`/`shipmentStatusList`/`lastUpdatedAfter`/`lastUpdatedBefore` filters,
    since `paginationToken` only encodes the paging cursor, not the filters themselves.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
try:
    response = client.wfs_inbound.get_shipments(ShipmentsQueryType.SHIPMENT)
    # TODO: Handle 'response' of type GetShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.get_shipments(ShipmentsQueryType.SHIPMENT)
    # TODO: Handle 'response' of type GetShipmentsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetShipmentsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>query_type</code> | <code>[ShipmentsQueryTypeOrStr](walmart_apis/models/enums/shipments_query_type.py)</code> | Determines which combination of filters below is required (upstream `QueryType`). |
| <code>shipment_id_list</code> | <code>list&#91;str&#93; \| None</code> | Shipment identifiers (external reference ids) to filter by. When `queryType=SHIPMENT`, exactly one of `shipmentIdList`/`shipmentStatusList` is required -- never both, never neither . Maximum 999 entries (upstream `ShipmentIdList`).<br>**Default**: <code>None</code> |
| <code>shipment_status_list</code> | <code>list&#91;[ShipmentStatusOrStr](walmart_apis/models/enums/shipment_status.py)&#93; \| None</code> | Shipment statuses to filter by (upstream `ShipmentStatusList`; same vocabulary as `getShipment`'s free-string `status` field, minus `UNCONFIRMED`, which upstream documents as never applying to a confirmed shipment). When `queryType=SHIPMENT`, exactly one of `shipmentIdList`/`shipmentStatusList` is required -- never both, never neither ; for `queryType=DATE_RANGE` it remains an optional additional filter.<br>**Default**: <code>None</code> |
| <code>last_updated_after</code> | <code>str \| None</code> | Only return shipments last updated at or after this date, ISO 8601 datetime. Required when `queryType=DATE_RANGE` (upstream `LastUpdatedAfter`).<br>**Default**: <code>None</code> |
| <code>last_updated_before</code> | <code>str \| None</code> | Only return shipments last updated at or before this date, ISO 8601 datetime. Optional when `queryType=DATE_RANGE`, defaults to now (upstream `LastUpdatedBefore`).<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch the next page of a previous `getShipments` query. Pass the value of `pagination.nextToken` from a previous response. Required when `queryType=NEXT_TOKEN`. Forwarded upstream as `NextToken`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[GetShipmentsResponse](walmart_apis/models/get_shipments_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[GetShipmentsErrorBody](walmart_apis/errors/get_shipments_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_delivery_window_options(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListDeliveryWindowOptionsResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_inbound_plan_boxes(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanBoxesResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a paginated list of shipping boxes included in an inbound plan.

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
| <code>plan_id</code> | <code>str</code> | Unique identifier of the inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | Maximum number of boxes to return in the response.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | Pagination token returned in a previous response. Specify this parameter to retrieve the next page of results.<br>**Default**: <code>None</code> |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_inbound_plan_items(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanItemsResponse</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a paginated list of items in an inbound plan.

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
| <code>plan_id</code> | <code>str</code> | Unique identifier of the inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | Maximum number of items to return in the response.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | Pagination token returned in a previous response. Specify this parameter to retrieve the next page of results.<br>**Default**: <code>None</code> |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_inbound_plan_pallets(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListInboundPlanPalletsResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Unique identifier of the inbound plan. |
| <code>page_size</code> | <code>int \| None</code> | Maximum number of pallets to return in the response.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | Pagination token returned in a previous response. Specify this parameter to retrieve the next page of results.<br>**Default**: <code>None</code> |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
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

Retrieves a paginated list of inbound plans. Filter by status, sort the results, and use `paginationToken` to retrieve subsequent pages.

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
| <code>page_size</code> | <code>int \| None</code> | Maximum number of inbound plans to return in the response.<br>**Default**: <code>10</code> |
| <code>pagination_token</code> | <code>str \| None</code> | Pagination token returned in a previous response. Specify this parameter to retrieve the next page of results.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>str \| None</code> | Filters results by inbound plan status. Supported values are `ACTIVE`, `VOIDED`, `SHIPPED`, and `ERRORED`.<br>**Default**: <code>None</code> |
| <code>sort_by</code> | <code>str \| None</code> | Field used to sort the returned inbound plans.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>str \| None</code> | Sort direction for the returned inbound plans. Supported values are `ASC` and `DESC`.<br>**Default**: <code>None</code> |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_packing_group_boxes(plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListPackingGroupBoxesResponse</code></summary>

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
    # TODO: Handle 'response' of type ListPackingGroupBoxesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPackingGroupBoxesErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_packing_group_boxes("some example string", "some example string")
    # TODO: Handle 'response' of type ListPackingGroupBoxesResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>packing_group_id</code> | <code>str</code> | Identifier of a packing group. |
| <code>page_size</code> | <code>int \| None</code> | The number of packing group boxes to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListPackingGroupBoxesResponse](walmart_apis/models/list_packing_group_boxes_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListPackingGroupBoxesErrorBody](walmart_apis/errors/list_packing_group_boxes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_packing_group_items(plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListPackingGroupItemsResponse</code></summary>

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
    # TODO: Handle 'response' of type ListPackingGroupItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListPackingGroupItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_packing_group_items("some example string", "some example string")
    # TODO: Handle 'response' of type ListPackingGroupItemsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>packing_group_id</code> | <code>str</code> | Identifier of a packing group. |
| <code>page_size</code> | <code>int \| None</code> | The number of packing group items to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListPackingGroupItemsResponse](walmart_apis/models/list_packing_group_items_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListPackingGroupItemsErrorBody](walmart_apis/errors/list_packing_group_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_packing_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListPackingOptionsResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_placement_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListPlacementOptionsResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_shipment_boxes(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListShipmentBoxesResponse</code></summary>

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
    # TODO: Handle 'response' of type ListShipmentBoxesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentBoxesErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_shipment_boxes("some example string", "some example string")
    # TODO: Handle 'response' of type ListShipmentBoxesResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. A shipment contains the boxes and units being inbounded. |
| <code>page_size</code> | <code>int \| None</code> | The number of boxes to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListShipmentBoxesResponse](walmart_apis/models/list_shipment_boxes_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListShipmentBoxesErrorBody](walmart_apis/errors/list_shipment_boxes_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_shipment_content_update_previews(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListShipmentContentUpdatePreviewsResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_shipment_items(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListShipmentItemsResponse</code></summary>

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
    # TODO: Handle 'response' of type ListShipmentItemsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentItemsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_shipment_items("some example string", "some example string")
    # TODO: Handle 'response' of type ListShipmentItemsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. A shipment contains the boxes and units being inbounded. |
| <code>page_size</code> | <code>int \| None</code> | The number of items to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListShipmentItemsResponse](walmart_apis/models/list_shipment_items_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListShipmentItemsErrorBody](walmart_apis/errors/list_shipment_items_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_shipment_pallets(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListShipmentPalletsResponse</code></summary>

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
    # TODO: Handle 'response' of type ListShipmentPalletsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListShipmentPalletsErrorBody
```

**Async**

```python
try:
    response = await async_client.wfs_inbound.list_shipment_pallets("some example string", "some example string")
    # TODO: Handle 'response' of type ListShipmentPalletsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>page_size</code> | <code>int \| None</code> | The number of pallets to return in the response matching the given query.<br>**Default**: <code>None</code> |
| <code>pagination_token</code> | <code>str \| None</code> | A token to fetch a certain page when there are multiple pages worth of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[ListShipmentPalletsResponse](walmart_apis/models/list_shipment_pallets_response.py)</code> -- Success

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[ListShipmentPalletsErrorBody](walmart_apis/errors/list_shipment_pallets_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_transportation_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, placement_option_id: str | None = None, shipment_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ListTransportationOptionsResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def schedule_self_ship_appointment(plan_id: str, shipment_id: str, slot_id: str, body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ScheduleSelfShipAppointmentResponse</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_packing_information(plan_id: str, body: SetPackingInformationRequest | SetPackingInformationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SetPackingInformationResponse</code></summary>

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
    # TODO: Handle 'response' of type SetPackingInformationResponse
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
    # TODO: Handle 'response' of type SetPackingInformationResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>body</code> | <code>[SetPackingInformationRequest](walmart_apis/models/set_packing_information_request.py) \| [SetPackingInformationRequestDict](walmart_apis/models/set_packing_information_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[SetPackingInformationResponse](walmart_apis/models/set_packing_information_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SetPackingInformationErrorBody](walmart_apis/errors/set_packing_information_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_prep_details(body: SetPrepDetailsRequest | SetPrepDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SetPrepDetailsResponse</code></summary>

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
    # TODO: Handle 'response' of type SetPrepDetailsResponse
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
    # TODO: Handle 'response' of type SetPrepDetailsResponse
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

**OnSuccess**: <code>[SetPrepDetailsResponse](walmart_apis/models/set_prep_details_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[SetPrepDetailsErrorBody](walmart_apis/errors/set_prep_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_inbound_plan_name(plan_id: str, body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the name of an existing inbound plan.

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
| <code>plan_id</code> | <code>str</code> | Unique identifier of the inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_item_compliance_details(marketplace_id: str, body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UpdateItemComplianceDetailsResponse</code></summary>

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
    # TODO: Handle 'response' of type UpdateItemComplianceDetailsResponse
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
    # TODO: Handle 'response' of type UpdateItemComplianceDetailsResponse
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

**OnSuccess**: <code>[UpdateItemComplianceDetailsResponse](walmart_apis/models/update_item_compliance_details_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateItemComplianceDetailsErrorBody](walmart_apis/errors/update_item_compliance_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_shipment_name(plan_id: str, shipment_id: str, body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
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
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_shipment_source_address(plan_id: str, shipment_id: str, body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UpdateShipmentSourceAddressResponse</code></summary>

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
            address=AddressInput(
                address_line1="some example string",
                city="some example string",
                country_code="some example string",
                name="some example string",
                phone_number="some example string",
                postal_code="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type UpdateShipmentSourceAddressResponse
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
            address=AddressInput(
                address_line1="some example string",
                city="some example string",
                country_code="some example string",
                name="some example string",
                phone_number="some example string",
                postal_code="some example string",
            ),
        ),
    )
    # TODO: Handle 'response' of type UpdateShipmentSourceAddressResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[UpdateShipmentSourceAddressRequest](walmart_apis/models/update_shipment_source_address_request.py) \| [UpdateShipmentSourceAddressRequestDict](walmart_apis/models/update_shipment_source_address_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UpdateShipmentSourceAddressResponse](walmart_apis/models/update_shipment_source_address_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateShipmentSourceAddressErrorBody](walmart_apis/errors/update_shipment_source_address_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_shipment_tracking_details(plan_id: str, shipment_id: str, body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UpdateShipmentTrackingDetailsResponse</code></summary>

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
    # TODO: Handle 'response' of type UpdateShipmentTrackingDetailsResponse
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
    # TODO: Handle 'response' of type UpdateShipmentTrackingDetailsResponse
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
| <code>plan_id</code> | <code>str</code> | Identifier of an inbound plan. |
| <code>shipment_id</code> | <code>str</code> | Identifier of a shipment. |
| <code>body</code> | <code>[UpdateShipmentTrackingDetailsRequest](walmart_apis/models/update_shipment_tracking_details_request.py) \| [UpdateShipmentTrackingDetailsRequestDict](walmart_apis/models/update_shipment_tracking_details_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](walmart_apis/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout, extra headers, or its retry count and statuses. |

</dd>
</dl>

### Response

<dl>
<dd>

**OnSuccess**: <code>[UpdateShipmentTrackingDetailsResponse](walmart_apis/models/update_shipment_tracking_details_response.py)</code> -- Accepted — operation submitted asynchronously.

**OnError**: <code>[ApiError](walmart_apis/core/exceptions.py)&#91;[UpdateShipmentTrackingDetailsErrorBody](walmart_apis/errors/update_shipment_tracking_details_error.py)&#93;</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429, 500 | <code>[CommonErrorListFulfillmentInboundPlans](walmart_apis/models/common_error_list_fulfillment_inbound_plans.py)</code> |
| anything unmapped | <code>[RawError](walmart_apis/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

