# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [WalmartApisClient](walmart_apis/client.py)

## Authorization

> Source: [Authorization](walmart_apis/apis/authorization.py)

<details>
<summary><code>def create_token(grant_type: GrantTypeOrStr, *, x_o_tenant: str | None = None, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, code_verifier: str | None = None, refresh_token: str | None = None, redirect_uri: str | None = None, scope: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TokenResponse, CreateTokenErrorBody]</code></summary>

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
result = client.authorization.with_raw_response.create_token(GrantType.CLIENT_CREDENTIALS)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateTokenErrorBody
```

**Async**

```python
result = await async_client.authorization.with_raw_response.create_token(GrantType.CLIENT_CREDENTIALS)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateTokenErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[TokenResponse](walmart_apis/models/token_response.py), [CreateTokenErrorBody](walmart_apis/errors/create_token_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TokenResponse](walmart_apis/models/token_response.py)</code> -- Returns the access token and related token information.

**On `Failure`**: `error` is <code>[CreateTokenErrorBody](walmart_apis/errors/create_token_error.py)</code>

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
<summary><code>def get_catalog_item(walmart_item_id: str, marketplace_ids: list[str], *, included_data: list[IncludedDatumOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Item, GetCatalogItemErrorBody]</code></summary>

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
result = client.catalog.with_raw_response.get_catalog_item("00000000000000", ["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Item
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCatalogItemErrorBody
```

**Async**

```python
result = await async_client.catalog.with_raw_response.get_catalog_item("00000000000000", ["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Item
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCatalogItemErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Item](walmart_apis/models/item.py), [GetCatalogItemErrorBody](walmart_apis/errors/get_catalog_item_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Item](walmart_apis/models/item.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetCatalogItemErrorBody](walmart_apis/errors/get_catalog_item_error.py)</code>

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
<summary><code>def search_catalog_items(marketplace_ids: list[str], *, keywords: str | None = None, walmart_item_ids: str | None = None, seller_sku: str | None = None, gtin: str | None = None, upc: str | None = None, included_data: list[IncludedDatumOrStr] | None = None, page_size: int | None = 10, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemSearchResults, SearchCatalogItemsErrorBody]</code></summary>

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
result = client.catalog.with_raw_response.search_catalog_items(["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchCatalogItemsErrorBody
```

**Async**

```python
result = await async_client.catalog.with_raw_response.search_catalog_items(["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemSearchResults
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchCatalogItemsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ItemSearchResults](walmart_apis/models/item_search_results.py), [SearchCatalogItemsErrorBody](walmart_apis/errors/search_catalog_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemSearchResults](walmart_apis/models/item_search_results.py)</code> -- Success

**On `Failure`**: `error` is <code>[SearchCatalogItemsErrorBody](walmart_apis/errors/search_catalog_items_error.py)</code>

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
<summary><code>def cancel_query(query_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelQueryResponse, CancelQueryErrorBody]</code></summary>

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
result = client.data_kiosk.with_raw_response.cancel_query("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelQueryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelQueryErrorBody
```

**Async**

```python
result = await async_client.data_kiosk.with_raw_response.cancel_query("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelQueryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelQueryErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelQueryResponse](walmart_apis/models/cancel_query_response.py), [CancelQueryErrorBody](walmart_apis/errors/cancel_query_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelQueryResponse](walmart_apis/models/cancel_query_response.py)</code> -- Query cancellation accepted

**On `Failure`**: `error` is <code>[CancelQueryErrorBody](walmart_apis/errors/cancel_query_error.py)</code>

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
<summary><code>def create_query(body: CreateQuerySpecification | CreateQuerySpecificationDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateQueryResponse, CreateQueryErrorBody]</code></summary>

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
result = client.data_kiosk.with_raw_response.create_query(CreateQuerySpecification(query="some example string"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateQueryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateQueryErrorBody
```

**Async**

```python
result = await async_client.data_kiosk.with_raw_response.create_query(
    CreateQuerySpecification(query="some example string")
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateQueryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateQueryErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateQueryResponse](walmart_apis/models/create_query_response.py), [CreateQueryErrorBody](walmart_apis/errors/create_query_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateQueryResponse](walmart_apis/models/create_query_response.py)</code> -- Query request accepted for processing

**On `Failure`**: `error` is <code>[CreateQueryErrorBody](walmart_apis/errors/create_query_error.py)</code>

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
<summary><code>def get_document(document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Document, GetDocumentErrorBody]</code></summary>

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
result = client.data_kiosk.with_raw_response.get_document("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Document
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDocumentErrorBody
```

**Async**

```python
result = await async_client.data_kiosk.with_raw_response.get_document("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Document
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDocumentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Document](walmart_apis/models/document.py), [GetDocumentErrorBody](walmart_apis/errors/get_document_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Document](walmart_apis/models/document.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetDocumentErrorBody](walmart_apis/errors/get_document_error.py)</code>

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
<summary><code>def get_queries(*, processing_statuses: list[ProcessingStatusOrStr] | None = None, page_size: int | None = 10, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetQueriesResponse, GetQueriesErrorBody]</code></summary>

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
result = client.data_kiosk.with_raw_response.get_queries()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetQueriesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetQueriesErrorBody
```

**Async**

```python
result = await async_client.data_kiosk.with_raw_response.get_queries()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetQueriesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetQueriesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetQueriesResponse](walmart_apis/models/get_queries_response.py), [GetQueriesErrorBody](walmart_apis/errors/get_queries_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetQueriesResponse](walmart_apis/models/get_queries_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetQueriesErrorBody](walmart_apis/errors/get_queries_error.py)</code>

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
<summary><code>def get_query(query_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Query, GetQueryErrorBody]</code></summary>

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
result = client.data_kiosk.with_raw_response.get_query("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Query
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetQueryErrorBody
```

**Async**

```python
result = await async_client.data_kiosk.with_raw_response.get_query("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Query
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetQueryErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Query](walmart_apis/models/query.py), [GetQueryErrorBody](walmart_apis/errors/get_query_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Query](walmart_apis/models/query.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetQueryErrorBody](walmart_apis/errors/get_query_error.py)</code>

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
<summary><code>def check_dispute_eligibility(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DisputeEligibilityResponse, CheckDisputeEligibilityErrorBody]</code></summary>

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
result = client.disputes.with_raw_response.check_dispute_eligibility()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisputeEligibilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CheckDisputeEligibilityErrorBody
```

**Async**

```python
result = await async_client.disputes.with_raw_response.check_dispute_eligibility()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisputeEligibilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CheckDisputeEligibilityErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[DisputeEligibilityResponse](walmart_apis/models/dispute_eligibility_response.py), [CheckDisputeEligibilityErrorBody](walmart_apis/errors/check_dispute_eligibility_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DisputeEligibilityResponse](walmart_apis/models/dispute_eligibility_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[CheckDisputeEligibilityErrorBody](walmart_apis/errors/check_dispute_eligibility_error.py)</code>

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
<summary><code>def cancel_feed(feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelFeedResponse, CancelFeedErrorBody]</code></summary>

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
result = client.feeds.with_raw_response.cancel_feed("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelFeedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelFeedErrorBody
```

**Async**

```python
result = await async_client.feeds.with_raw_response.cancel_feed("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelFeedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelFeedErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelFeedResponse](walmart_apis/models/cancel_feed_response.py), [CancelFeedErrorBody](walmart_apis/errors/cancel_feed_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelFeedResponse](walmart_apis/models/cancel_feed_response.py)</code> -- Cancellation accepted

**On `Failure`**: `error` is <code>[CancelFeedErrorBody](walmart_apis/errors/cancel_feed_error.py)</code>

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
<summary><code>def create_feed(feed_type: FeedType1OrStr, file: FileInput, *, content_type: ContentTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateFeedResponse, CreateFeedErrorBody]</code></summary>

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
result = client.feeds.with_raw_response.create_feed(FeedType1.LISTINGS_FEED, Path("path/to/file.bin"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateFeedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateFeedErrorBody
```

**Async**

```python
result = await async_client.feeds.with_raw_response.create_feed(FeedType1.LISTINGS_FEED, Path("path/to/file.bin"))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateFeedResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateFeedErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateFeedResponse](walmart_apis/models/create_feed_response.py), [CreateFeedErrorBody](walmart_apis/errors/create_feed_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateFeedResponse](walmart_apis/models/create_feed_response.py)</code> -- Feed accepted for processing

**On `Failure`**: `error` is <code>[CreateFeedErrorBody](walmart_apis/errors/create_feed_error.py)</code>

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
<summary><code>def get_feed(feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Feed, GetFeedErrorBody]</code></summary>

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
result = client.feeds.with_raw_response.get_feed("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Feed
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFeedErrorBody
```

**Async**

```python
result = await async_client.feeds.with_raw_response.get_feed("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Feed
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFeedErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Feed](walmart_apis/models/feed.py), [GetFeedErrorBody](walmart_apis/errors/get_feed_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Feed](walmart_apis/models/feed.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetFeedErrorBody](walmart_apis/errors/get_feed_error.py)</code>

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
<summary><code>def get_feed_document(feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, GetFeedDocumentErrorBody]</code></summary>

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
result = client.feeds.with_raw_response.get_feed_document("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFeedDocumentErrorBody
```

**Async**

```python
result = await async_client.feeds.with_raw_response.get_feed_document("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFeedDocumentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [GetFeedDocumentErrorBody](walmart_apis/errors/get_feed_document_error.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- Binary file stream

**On `Failure`**: `error` is <code>[GetFeedDocumentErrorBody](walmart_apis/errors/get_feed_document_error.py)</code>

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
<summary><code>def get_feeds(*, feed_types: list[FeedTypeOrStr] | None = None, feed_statuses: list[FeedStatusOrStr] | None = None, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetFeedsResponse, GetFeedsErrorBody]</code></summary>

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
result = client.feeds.with_raw_response.get_feeds()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFeedsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFeedsErrorBody
```

**Async**

```python
result = await async_client.feeds.with_raw_response.get_feeds()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFeedsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFeedsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetFeedsResponse](walmart_apis/models/get_feeds_response.py), [GetFeedsErrorBody](walmart_apis/errors/get_feeds_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetFeedsResponse](walmart_apis/models/get_feeds_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetFeedsErrorBody](walmart_apis/errors/get_feeds_error.py)</code>

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
<summary><code>def get_final_payout_case_status(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FinalPayoutCaseStatusResponse, GetFinalPayoutCaseStatusErrorBody]</code></summary>

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
result = client.final_payout.with_raw_response.get_final_payout_case_status()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FinalPayoutCaseStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFinalPayoutCaseStatusErrorBody
```

**Async**

```python
result = await async_client.final_payout.with_raw_response.get_final_payout_case_status()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FinalPayoutCaseStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFinalPayoutCaseStatusErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FinalPayoutCaseStatusResponse](walmart_apis/models/final_payout_case_status_response.py), [GetFinalPayoutCaseStatusErrorBody](walmart_apis/errors/get_final_payout_case_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FinalPayoutCaseStatusResponse](walmart_apis/models/final_payout_case_status_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetFinalPayoutCaseStatusErrorBody](walmart_apis/errors/get_final_payout_case_status_error.py)</code>

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
<summary><code>def update_final_payout_case_status(body: UpdateFinalPayoutCaseStatusRequest | UpdateFinalPayoutCaseStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FinalPayoutCaseStatusResponse, UpdateFinalPayoutCaseStatusErrorBody]</code></summary>

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
result = client.final_payout.with_raw_response.update_final_payout_case_status(
    UpdateFinalPayoutCaseStatusRequest(status=Status3.RESOLVED)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FinalPayoutCaseStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateFinalPayoutCaseStatusErrorBody
```

**Async**

```python
result = await async_client.final_payout.with_raw_response.update_final_payout_case_status(
    UpdateFinalPayoutCaseStatusRequest(status=Status3.RESOLVED)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FinalPayoutCaseStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateFinalPayoutCaseStatusErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FinalPayoutCaseStatusResponse](walmart_apis/models/final_payout_case_status_response.py), [UpdateFinalPayoutCaseStatusErrorBody](walmart_apis/errors/update_final_payout_case_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FinalPayoutCaseStatusResponse](walmart_apis/models/final_payout_case_status_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[UpdateFinalPayoutCaseStatusErrorBody](walmart_apis/errors/update_final_payout_case_status_error.py)</code>

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
<summary><code>def list_financial_event_groups(*, max_results_per_page: int | None = None, financial_event_group_started_before: RFC3339DateTime | None = None, financial_event_group_started_after: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, ListFinancialEventGroupsErrorBody]</code></summary>

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
result = client.finances.with_raw_response.list_financial_event_groups()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFinancialEventGroupsErrorBody
```

**Async**

```python
result = await async_client.finances.with_raw_response.list_financial_event_groups()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFinancialEventGroupsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [ListFinancialEventGroupsErrorBody](walmart_apis/errors/list_financial_event_groups_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[ListFinancialEventGroupsErrorBody](walmart_apis/errors/list_financial_event_groups_error.py)</code>

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
<summary><code>def list_financial_events(*, max_results_per_page: int | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, ListFinancialEventsErrorBody]</code></summary>

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
result = client.finances.with_raw_response.list_financial_events()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFinancialEventsErrorBody
```

**Async**

```python
result = await async_client.finances.with_raw_response.list_financial_events()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFinancialEventsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [ListFinancialEventsErrorBody](walmart_apis/errors/list_financial_events_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[ListFinancialEventsErrorBody](walmart_apis/errors/list_financial_events_error.py)</code>

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
<summary><code>def list_financial_events_by_group_id(event_group_id: str, *, max_results_per_page: int | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, ListFinancialEventsByGroupIdErrorBody]</code></summary>

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
result = client.finances.with_raw_response.list_financial_events_by_group_id("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFinancialEventsByGroupIdErrorBody
```

**Async**

```python
result = await async_client.finances.with_raw_response.list_financial_events_by_group_id("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFinancialEventsByGroupIdErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [ListFinancialEventsByGroupIdErrorBody](walmart_apis/errors/list_financial_events_by_group_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[ListFinancialEventsByGroupIdErrorBody](walmart_apis/errors/list_financial_events_by_group_id_error.py)</code>

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
<summary><code>def list_financial_events_by_order_id(order_id: str, *, max_results_per_page: int | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, ListFinancialEventsByOrderIdErrorBody]</code></summary>

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
result = client.finances.with_raw_response.list_financial_events_by_order_id("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFinancialEventsByOrderIdErrorBody
```

**Async**

```python
result = await async_client.finances.with_raw_response.list_financial_events_by_order_id("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFinancialEventsByOrderIdErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [ListFinancialEventsByOrderIdErrorBody](walmart_apis/errors/list_financial_events_by_order_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[ListFinancialEventsByOrderIdErrorBody](walmart_apis/errors/list_financial_events_by_order_id_error.py)</code>

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
<summary><code>def cancel_fulfillment_order(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelFulfillmentOrderResponse, CancelFulfillmentOrderErrorBody]</code></summary>

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
result = client.fulfillment_outbound.with_raw_response.cancel_fulfillment_order("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelFulfillmentOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelFulfillmentOrderErrorBody
```

**Async**

```python
result = await async_client.fulfillment_outbound.with_raw_response.cancel_fulfillment_order("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelFulfillmentOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelFulfillmentOrderErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelFulfillmentOrderResponse](walmart_apis/models/cancel_fulfillment_order_response.py), [CancelFulfillmentOrderErrorBody](walmart_apis/errors/cancel_fulfillment_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelFulfillmentOrderResponse](walmart_apis/models/cancel_fulfillment_order_response.py)</code> -- Cancellation request submitted

**On `Failure`**: `error` is <code>[CancelFulfillmentOrderErrorBody](walmart_apis/errors/cancel_fulfillment_order_error.py)</code>

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
<summary><code>def create_fulfillment_order(body: CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateFulfillmentOrderResponse, CreateFulfillmentOrderErrorBody]</code></summary>

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
result = client.fulfillment_outbound.with_raw_response.create_fulfillment_order(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateFulfillmentOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateFulfillmentOrderErrorBody
```

**Async**

```python
result = await async_client.fulfillment_outbound.with_raw_response.create_fulfillment_order(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateFulfillmentOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateFulfillmentOrderErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateFulfillmentOrderResponse](walmart_apis/models/create_fulfillment_order_response.py), [CreateFulfillmentOrderErrorBody](walmart_apis/errors/create_fulfillment_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateFulfillmentOrderResponse](walmart_apis/models/create_fulfillment_order_response.py)</code> -- Fulfillment order created

**On `Failure`**: `error` is <code>[CreateFulfillmentOrderErrorBody](walmart_apis/errors/create_fulfillment_order_error.py)</code>

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
<summary><code>def get_fulfillment_order(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetFulfillmentOrderResponse, GetFulfillmentOrderErrorBody]</code></summary>

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
result = client.fulfillment_outbound.with_raw_response.get_fulfillment_order("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFulfillmentOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFulfillmentOrderErrorBody
```

**Async**

```python
result = await async_client.fulfillment_outbound.with_raw_response.get_fulfillment_order("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFulfillmentOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFulfillmentOrderErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetFulfillmentOrderResponse](walmart_apis/models/get_fulfillment_order_response.py), [GetFulfillmentOrderErrorBody](walmart_apis/errors/get_fulfillment_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetFulfillmentOrderResponse](walmart_apis/models/get_fulfillment_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetFulfillmentOrderErrorBody](walmart_apis/errors/get_fulfillment_order_error.py)</code>

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
<summary><code>def get_fulfillment_order_shipments(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetFulfillmentOrderShipmentsResponse, GetFulfillmentOrderShipmentsErrorBody]</code></summary>

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
result = client.fulfillment_outbound.with_raw_response.get_fulfillment_order_shipments("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFulfillmentOrderShipmentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFulfillmentOrderShipmentsErrorBody
```

**Async**

```python
result = await async_client.fulfillment_outbound.with_raw_response.get_fulfillment_order_shipments(
    "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFulfillmentOrderShipmentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFulfillmentOrderShipmentsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetFulfillmentOrderShipmentsResponse](walmart_apis/models/get_fulfillment_order_shipments_response.py), [GetFulfillmentOrderShipmentsErrorBody](walmart_apis/errors/get_fulfillment_order_shipments_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetFulfillmentOrderShipmentsResponse](walmart_apis/models/get_fulfillment_order_shipments_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetFulfillmentOrderShipmentsErrorBody](walmart_apis/errors/get_fulfillment_order_shipments_error.py)</code>

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
<summary><code>def get_fulfillment_preview(body: GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetFulfillmentPreviewResponse, GetFulfillmentPreviewErrorBody]</code></summary>

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
result = client.fulfillment_outbound.with_raw_response.get_fulfillment_preview(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFulfillmentPreviewResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFulfillmentPreviewErrorBody
```

**Async**

```python
result = await async_client.fulfillment_outbound.with_raw_response.get_fulfillment_preview(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetFulfillmentPreviewResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFulfillmentPreviewErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetFulfillmentPreviewResponse](walmart_apis/models/get_fulfillment_preview_response.py), [GetFulfillmentPreviewErrorBody](walmart_apis/errors/get_fulfillment_preview_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetFulfillmentPreviewResponse](walmart_apis/models/get_fulfillment_preview_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetFulfillmentPreviewErrorBody](walmart_apis/errors/get_fulfillment_preview_error.py)</code>

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
<summary><code>def list_all_fulfillment_orders(*, query_start_date: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListAllFulfillmentOrdersResponse, ListAllFulfillmentOrdersErrorBody]</code></summary>

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
result = client.fulfillment_outbound.with_raw_response.list_all_fulfillment_orders()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListAllFulfillmentOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAllFulfillmentOrdersErrorBody
```

**Async**

```python
result = await async_client.fulfillment_outbound.with_raw_response.list_all_fulfillment_orders()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListAllFulfillmentOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAllFulfillmentOrdersErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListAllFulfillmentOrdersResponse](walmart_apis/models/list_all_fulfillment_orders_response.py), [ListAllFulfillmentOrdersErrorBody](walmart_apis/errors/list_all_fulfillment_orders_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListAllFulfillmentOrdersResponse](walmart_apis/models/list_all_fulfillment_orders_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListAllFulfillmentOrdersErrorBody](walmart_apis/errors/list_all_fulfillment_orders_error.py)</code>

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
<summary><code>def update_fulfillment_order(seller_fulfillment_order_id: str, body: UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateFulfillmentOrderResponse, UpdateFulfillmentOrderErrorBody]</code></summary>

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
result = client.fulfillment_outbound.with_raw_response.update_fulfillment_order(
    "some example string", UpdateFulfillmentOrderRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateFulfillmentOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateFulfillmentOrderErrorBody
```

**Async**

```python
result = await async_client.fulfillment_outbound.with_raw_response.update_fulfillment_order(
    "some example string", UpdateFulfillmentOrderRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateFulfillmentOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateFulfillmentOrderErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[UpdateFulfillmentOrderResponse](walmart_apis/models/update_fulfillment_order_response.py), [UpdateFulfillmentOrderErrorBody](walmart_apis/errors/update_fulfillment_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateFulfillmentOrderResponse](walmart_apis/models/update_fulfillment_order_response.py)</code> -- Order updated

**On `Failure`**: `error` is <code>[UpdateFulfillmentOrderErrorBody](walmart_apis/errors/update_fulfillment_order_error.py)</code>

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
<summary><code>def bulk_update_inventory(body: BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpdateInventoryResponse, BulkUpdateInventoryErrorBody]</code></summary>

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
result = client.inventory.with_raw_response.bulk_update_inventory(
    BulkUpdateInventoryRequest(items=[BulkInventoryItem(seller_sku="some example string", quantity=1)])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpdateInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkUpdateInventoryErrorBody
```

**Async**

```python
result = await async_client.inventory.with_raw_response.bulk_update_inventory(
    BulkUpdateInventoryRequest(items=[BulkInventoryItem(seller_sku="some example string", quantity=1)])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpdateInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BulkUpdateInventoryErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[BulkUpdateInventoryResponse](walmart_apis/models/bulk_update_inventory_response.py), [BulkUpdateInventoryErrorBody](walmart_apis/errors/bulk_update_inventory_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpdateInventoryResponse](walmart_apis/models/bulk_update_inventory_response.py)</code> -- Bulk update accepted

**On `Failure`**: `error` is <code>[BulkUpdateInventoryErrorBody](walmart_apis/errors/bulk_update_inventory_error.py)</code>

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
<summary><code>def get_inventory_for_sku(sku: str, *, ship_node: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InventorySummary, GetInventoryForSkuErrorBody]</code></summary>

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
result = client.inventory.with_raw_response.get_inventory_for_sku("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InventorySummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInventoryForSkuErrorBody
```

**Async**

```python
result = await async_client.inventory.with_raw_response.get_inventory_for_sku("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InventorySummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInventoryForSkuErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[InventorySummary](walmart_apis/models/inventory_summary.py), [GetInventoryForSkuErrorBody](walmart_apis/errors/get_inventory_for_sku_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[InventorySummary](walmart_apis/models/inventory_summary.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetInventoryForSkuErrorBody](walmart_apis/errors/get_inventory_for_sku_error.py)</code>

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
<summary><code>def get_inventory_summaries(*, skus: str | None = None, ship_node: str | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetInventorySummariesResponse, GetInventorySummariesErrorBody]</code></summary>

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
result = client.inventory.with_raw_response.get_inventory_summaries()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetInventorySummariesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInventorySummariesErrorBody
```

**Async**

```python
result = await async_client.inventory.with_raw_response.get_inventory_summaries()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetInventorySummariesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInventorySummariesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetInventorySummariesResponse](walmart_apis/models/get_inventory_summaries_response.py), [GetInventorySummariesErrorBody](walmart_apis/errors/get_inventory_summaries_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetInventorySummariesResponse](walmart_apis/models/get_inventory_summaries_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetInventorySummariesErrorBody](walmart_apis/errors/get_inventory_summaries_error.py)</code>

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
<summary><code>def update_inventory_for_sku(sku: str, body: UpdateInventoryRequest | UpdateInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateInventoryResponse, UpdateInventoryForSkuErrorBody]</code></summary>

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
result = client.inventory.with_raw_response.update_inventory_for_sku(
    "some example string", UpdateInventoryRequest(quantity=1)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateInventoryForSkuErrorBody
```

**Async**

```python
result = await async_client.inventory.with_raw_response.update_inventory_for_sku(
    "some example string", UpdateInventoryRequest(quantity=1)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateInventoryForSkuErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[UpdateInventoryResponse](walmart_apis/models/update_inventory_response.py), [UpdateInventoryForSkuErrorBody](walmart_apis/errors/update_inventory_for_sku_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateInventoryResponse](walmart_apis/models/update_inventory_response.py)</code> -- Inventory updated successfully

**On `Failure`**: `error` is <code>[UpdateInventoryForSkuErrorBody](walmart_apis/errors/update_inventory_for_sku_error.py)</code>

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
<summary><code>def delete_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListingsItemSubmissionResponse, DeleteListingsItemErrorBody]</code></summary>

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
result = client.listings_items.with_raw_response.delete_listings_item(
    "some example string", "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListingsItemSubmissionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteListingsItemErrorBody
```

**Async**

```python
result = await async_client.listings_items.with_raw_response.delete_listings_item(
    "some example string", "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListingsItemSubmissionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteListingsItemErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py), [DeleteListingsItemErrorBody](walmart_apis/errors/delete_listings_item_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py)</code> -- Successfully submitted

**On `Failure`**: `error` is <code>[DeleteListingsItemErrorBody](walmart_apis/errors/delete_listings_item_error.py)</code>

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
<summary><code>def get_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], *, issue_locale: str | None = "en_US", included_data: list[IncludedDatumListingsItemsOrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemListingsItems, GetListingsItemErrorBody]</code></summary>

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
result = client.listings_items.with_raw_response.get_listings_item(
    "some example string", "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemListingsItems
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingsItemErrorBody
```

**Async**

```python
result = await async_client.listings_items.with_raw_response.get_listings_item(
    "some example string", "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemListingsItems
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingsItemErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ItemListingsItems](walmart_apis/models/item_listings_items.py), [GetListingsItemErrorBody](walmart_apis/errors/get_listings_item_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemListingsItems](walmart_apis/models/item_listings_items.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetListingsItemErrorBody](walmart_apis/errors/get_listings_item_error.py)</code>

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
<summary><code>def patch_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], body: ListingsItemPatchRequest | ListingsItemPatchRequestDict, *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListingsItemSubmissionResponse, PatchListingsItemErrorBody]</code></summary>

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
result = client.listings_items.with_raw_response.patch_listings_item(
    "some example string",
    "some example string",
    ["some example string"],
    ListingsItemPatchRequest(
        product_type="some example string", patches=[PatchOperation(op=Op.ADD, path="some example string")]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListingsItemSubmissionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PatchListingsItemErrorBody
```

**Async**

```python
result = await async_client.listings_items.with_raw_response.patch_listings_item(
    "some example string",
    "some example string",
    ["some example string"],
    ListingsItemPatchRequest(
        product_type="some example string", patches=[PatchOperation(op=Op.ADD, path="some example string")]
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListingsItemSubmissionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PatchListingsItemErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py), [PatchListingsItemErrorBody](walmart_apis/errors/patch_listings_item_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py)</code> -- Successfully submitted

**On `Failure`**: `error` is <code>[PatchListingsItemErrorBody](walmart_apis/errors/patch_listings_item_error.py)</code>

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
<summary><code>def put_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], body: ListingsItemPutRequest | ListingsItemPutRequestDict, *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListingsItemSubmissionResponse, PutListingsItemErrorBody]</code></summary>

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
result = client.listings_items.with_raw_response.put_listings_item(
    "some example string",
    "some example string",
    ["some example string"],
    ListingsItemPutRequest(product_type="some example string", attributes={}),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListingsItemSubmissionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PutListingsItemErrorBody
```

**Async**

```python
result = await async_client.listings_items.with_raw_response.put_listings_item(
    "some example string",
    "some example string",
    ["some example string"],
    ListingsItemPutRequest(product_type="some example string", attributes={}),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListingsItemSubmissionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PutListingsItemErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py), [PutListingsItemErrorBody](walmart_apis/errors/put_listings_item_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListingsItemSubmissionResponse](walmart_apis/models/listings_item_submission_response.py)</code> -- Successfully submitted

**On `Failure`**: `error` is <code>[PutListingsItemErrorBody](walmart_apis/errors/put_listings_item_error.py)</code>

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
<summary><code>def search_listings_items(seller_id: str, marketplace_ids: list[str], *, included_data: list[IncludedDatumListingsItemsOrStr] | None = None, identifier_type: IdentifierTypeListingsItemsOrStr | None = None, identifier_value: str | None = None, lifecycle_status: list[str] | None = None, published_status: list[str] | None = None, unpublished_reasons: list[str] | None = None, inventory_status: list[str] | None = None, fulfillment_type: list[str] | None = None, min_customer_rating: float | None = None, max_customer_rating: float | None = None, min_price: float | None = None, max_price: float | None = None, sort_by: SortByOrStr | None = None, sort_order: SortOrderOrStr | None = SortOrder.ASC, page_size: int | None = 10, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ItemSearchResultsListingsItems, SearchListingsItemsErrorBody]</code></summary>

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
result = client.listings_items.with_raw_response.search_listings_items("some example string", ["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemSearchResultsListingsItems
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchListingsItemsErrorBody
```

**Async**

```python
result = await async_client.listings_items.with_raw_response.search_listings_items(
    "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ItemSearchResultsListingsItems
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchListingsItemsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ItemSearchResultsListingsItems](walmart_apis/models/item_search_results_listings_items.py), [SearchListingsItemsErrorBody](walmart_apis/errors/search_listings_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ItemSearchResultsListingsItems](walmart_apis/models/item_search_results_listings_items.py)</code> -- Success

**On `Failure`**: `error` is <code>[SearchListingsItemsErrorBody](walmart_apis/errors/search_listings_items_error.py)</code>

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
<summary><code>def get_listings_restrictions(asin: str, condition_type: ConditionTypeListingsRestrictionsOrStr, seller_id: str, marketplace_ids: list[str], *, reason_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ApiResult[RestrictionList, GetListingsRestrictionsErrorBody]</code></summary>

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
result = client.listings_restrictions.with_raw_response.get_listings_restrictions(
    "some example string", ConditionTypeListingsRestrictions.NEW_NEW, "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RestrictionList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingsRestrictionsErrorBody
```

**Async**

```python
result = await async_client.listings_restrictions.with_raw_response.get_listings_restrictions(
    "some example string", ConditionTypeListingsRestrictions.NEW_NEW, "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RestrictionList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingsRestrictionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[RestrictionList](walmart_apis/models/restriction_list.py), [GetListingsRestrictionsErrorBody](walmart_apis/errors/get_listings_restrictions_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RestrictionList](walmart_apis/models/restriction_list.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetListingsRestrictionsErrorBody](walmart_apis/errors/get_listings_restrictions_error.py)</code>

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
<summary><code>def cancel_shipment(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelShipmentResponse, CancelShipmentErrorBody]</code></summary>

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
result = client.merchant_fulfillment.with_raw_response.cancel_shipment("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelShipmentErrorBody
```

**Async**

```python
result = await async_client.merchant_fulfillment.with_raw_response.cancel_shipment("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelShipmentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelShipmentResponse](walmart_apis/models/cancel_shipment_response.py), [CancelShipmentErrorBody](walmart_apis/errors/cancel_shipment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelShipmentResponse](walmart_apis/models/cancel_shipment_response.py)</code> -- Shipment cancelled

**On `Failure`**: `error` is <code>[CancelShipmentErrorBody](walmart_apis/errors/cancel_shipment_error.py)</code>

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
<summary><code>def create_shipment(body: CreateShipmentRequest | CreateShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateShipmentResponse, CreateShipmentErrorBody]</code></summary>

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
result = client.merchant_fulfillment.with_raw_response.create_shipment(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateShipmentErrorBody
```

**Async**

```python
result = await async_client.merchant_fulfillment.with_raw_response.create_shipment(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateShipmentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateShipmentResponse](walmart_apis/models/create_shipment_response.py), [CreateShipmentErrorBody](walmart_apis/errors/create_shipment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateShipmentResponse](walmart_apis/models/create_shipment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[CreateShipmentErrorBody](walmart_apis/errors/create_shipment_error.py)</code>

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
<summary><code>def get_eligible_shipping_services(body: GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetEligibleShippingServicesResponse, GetEligibleShippingServicesErrorBody]</code></summary>

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
result = client.merchant_fulfillment.with_raw_response.get_eligible_shipping_services(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetEligibleShippingServicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEligibleShippingServicesErrorBody
```

**Async**

```python
result = await async_client.merchant_fulfillment.with_raw_response.get_eligible_shipping_services(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetEligibleShippingServicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEligibleShippingServicesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetEligibleShippingServicesResponse](walmart_apis/models/get_eligible_shipping_services_response.py), [GetEligibleShippingServicesErrorBody](walmart_apis/errors/get_eligible_shipping_services_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetEligibleShippingServicesResponse](walmart_apis/models/get_eligible_shipping_services_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetEligibleShippingServicesErrorBody](walmart_apis/errors/get_eligible_shipping_services_error.py)</code>

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
<summary><code>def get_label(shipment_id: str, *, format_: FormatOrStr | None = Format.PDF, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Label, GetLabelErrorBody]</code></summary>

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
result = client.merchant_fulfillment.with_raw_response.get_label("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Label
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLabelErrorBody
```

**Async**

```python
result = await async_client.merchant_fulfillment.with_raw_response.get_label("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Label
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLabelErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Label](walmart_apis/models/label.py), [GetLabelErrorBody](walmart_apis/errors/get_label_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Label](walmart_apis/models/label.py)</code> -- Label returned

**On `Failure`**: `error` is <code>[GetLabelErrorBody](walmart_apis/errors/get_label_error.py)</code>

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
<summary><code>def get_shipment2(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetShipmentResponse, GetShipment2ErrorBody]</code></summary>

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
result = client.merchant_fulfillment.with_raw_response.get_shipment2("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipment2ErrorBody
```

**Async**

```python
result = await async_client.merchant_fulfillment.with_raw_response.get_shipment2("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipment2ErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetShipmentResponse](walmart_apis/models/get_shipment_response.py), [GetShipment2ErrorBody](walmart_apis/errors/get_shipment2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetShipmentResponse](walmart_apis/models/get_shipment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetShipment2ErrorBody](walmart_apis/errors/get_shipment2_error.py)</code>

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
<summary><code>def acknowledge_order(purchase_order_id: str, body: AcknowledgeOrderRequest | AcknowledgeOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AcknowledgeOrderResponse, AcknowledgeOrderErrorBody]</code></summary>

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
result = client.orders.with_raw_response.acknowledge_order(
    "some example string",
    AcknowledgeOrderRequest(order_lines=[AcknowledgeOrderLine(line_number="some example string")]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AcknowledgeOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AcknowledgeOrderErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.acknowledge_order(
    "some example string",
    AcknowledgeOrderRequest(order_lines=[AcknowledgeOrderLine(line_number="some example string")]),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AcknowledgeOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AcknowledgeOrderErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[AcknowledgeOrderResponse](walmart_apis/models/acknowledge_order_response.py), [AcknowledgeOrderErrorBody](walmart_apis/errors/acknowledge_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AcknowledgeOrderResponse](walmart_apis/models/acknowledge_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[AcknowledgeOrderErrorBody](walmart_apis/errors/acknowledge_order_error.py)</code>

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
<summary><code>def cancel_order_lines(purchase_order_id: str, body: CancelOrderLinesRequest | CancelOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelOrderLinesResponse, CancelOrderLinesErrorBody]</code></summary>

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
result = client.orders.with_raw_response.cancel_order_lines(
    "some example string",
    CancelOrderLinesRequest(
        order_lines=[
            CancelOrderLine(
                line_number="some example string", cancellation_reason=CancellationReason.CUSTOMER_REQUESTED
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelOrderLinesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelOrderLinesErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.cancel_order_lines(
    "some example string",
    CancelOrderLinesRequest(
        order_lines=[
            CancelOrderLine(
                line_number="some example string", cancellation_reason=CancellationReason.CUSTOMER_REQUESTED
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelOrderLinesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelOrderLinesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelOrderLinesResponse](walmart_apis/models/cancel_order_lines_response.py), [CancelOrderLinesErrorBody](walmart_apis/errors/cancel_order_lines_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelOrderLinesResponse](walmart_apis/models/cancel_order_lines_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[CancelOrderLinesErrorBody](walmart_apis/errors/cancel_order_lines_error.py)</code>

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
<summary><code>def deliver_order_lines(purchase_order_id: str, body: DeliverOrderLinesRequest | DeliverOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeliverOrderLinesResponse, DeliverOrderLinesErrorBody]</code></summary>

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
result = client.orders.with_raw_response.deliver_order_lines(
    "some example string", DeliverOrderLinesRequest(order_lines=[DeliverOrderLine(line_number="some example string")])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeliverOrderLinesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeliverOrderLinesErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.deliver_order_lines(
    "some example string", DeliverOrderLinesRequest(order_lines=[DeliverOrderLine(line_number="some example string")])
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeliverOrderLinesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeliverOrderLinesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[DeliverOrderLinesResponse](walmart_apis/models/deliver_order_lines_response.py), [DeliverOrderLinesErrorBody](walmart_apis/errors/deliver_order_lines_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeliverOrderLinesResponse](walmart_apis/models/deliver_order_lines_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[DeliverOrderLinesErrorBody](walmart_apis/errors/deliver_order_lines_error.py)</code>

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
<summary><code>def get_order(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetOrderResponse, GetOrderErrorBody]</code></summary>

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
result = client.orders.with_raw_response.get_order("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.get_order("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetOrderResponse](walmart_apis/models/get_order_response.py), [GetOrderErrorBody](walmart_apis/errors/get_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetOrderResponse](walmart_apis/models/get_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetOrderErrorBody](walmart_apis/errors/get_order_error.py)</code>

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
<summary><code>def get_order_address(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetOrderAddressResponse, GetOrderAddressErrorBody]</code></summary>

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
result = client.orders.with_raw_response.get_order_address("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderAddressResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderAddressErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.get_order_address("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderAddressResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderAddressErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetOrderAddressResponse](walmart_apis/models/get_order_address_response.py), [GetOrderAddressErrorBody](walmart_apis/errors/get_order_address_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetOrderAddressResponse](walmart_apis/models/get_order_address_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetOrderAddressErrorBody](walmart_apis/errors/get_order_address_error.py)</code>

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
<summary><code>def get_order_buyer_info(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetOrderBuyerInfoResponse, GetOrderBuyerInfoErrorBody]</code></summary>

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
result = client.orders.with_raw_response.get_order_buyer_info("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderBuyerInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderBuyerInfoErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.get_order_buyer_info("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderBuyerInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderBuyerInfoErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetOrderBuyerInfoResponse](walmart_apis/models/get_order_buyer_info_response.py), [GetOrderBuyerInfoErrorBody](walmart_apis/errors/get_order_buyer_info_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetOrderBuyerInfoResponse](walmart_apis/models/get_order_buyer_info_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetOrderBuyerInfoErrorBody](walmart_apis/errors/get_order_buyer_info_error.py)</code>

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
<summary><code>def get_order_items(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetOrderItemsResponse, GetOrderItemsErrorBody]</code></summary>

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
result = client.orders.with_raw_response.get_order_items("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderItemsErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.get_order_items("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderItemsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetOrderItemsResponse](walmart_apis/models/get_order_items_response.py), [GetOrderItemsErrorBody](walmart_apis/errors/get_order_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetOrderItemsResponse](walmart_apis/models/get_order_items_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetOrderItemsErrorBody](walmart_apis/errors/get_order_items_error.py)</code>

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
<summary><code>def get_order_regulated_info(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetOrderRegulatedInfoResponse, GetOrderRegulatedInfoErrorBody]</code></summary>

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
result = client.orders.with_raw_response.get_order_regulated_info("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderRegulatedInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderRegulatedInfoErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.get_order_regulated_info("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrderRegulatedInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderRegulatedInfoErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetOrderRegulatedInfoResponse](walmart_apis/models/get_order_regulated_info_response.py), [GetOrderRegulatedInfoErrorBody](walmart_apis/errors/get_order_regulated_info_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetOrderRegulatedInfoResponse](walmart_apis/models/get_order_regulated_info_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetOrderRegulatedInfoErrorBody](walmart_apis/errors/get_order_regulated_info_error.py)</code>

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
<summary><code>def get_orders(*, created_after: RFC3339DateTime | None = None, created_before: RFC3339DateTime | None = None, last_updated_after: RFC3339DateTime | None = None, order_statuses: list[OrderStatus1OrStr] | None = None, fulfillment_types: list[FulfillmentType1OrStr] | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetOrdersResponse, GetOrdersErrorBody]</code></summary>

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
result = client.orders.with_raw_response.get_orders()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrdersErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.get_orders()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrdersErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetOrdersResponse](walmart_apis/models/get_orders_response.py), [GetOrdersErrorBody](walmart_apis/errors/get_orders_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetOrdersResponse](walmart_apis/models/get_orders_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetOrdersErrorBody](walmart_apis/errors/get_orders_error.py)</code>

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
<summary><code>def refund_order_lines(purchase_order_id: str, body: RefundOrderLinesRequest | RefundOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RefundOrderLinesResponse, RefundOrderLinesErrorBody]</code></summary>

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
result = client.orders.with_raw_response.refund_order_lines(
    "some example string",
    RefundOrderLinesRequest(
        order_lines=[
            RefundOrderLine(line_number="some example string", refund_amount=Money(), refund_type=RefundType.RETURN)
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RefundOrderLinesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RefundOrderLinesErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.refund_order_lines(
    "some example string",
    RefundOrderLinesRequest(
        order_lines=[
            RefundOrderLine(line_number="some example string", refund_amount=Money(), refund_type=RefundType.RETURN)
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RefundOrderLinesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RefundOrderLinesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[RefundOrderLinesResponse](walmart_apis/models/refund_order_lines_response.py), [RefundOrderLinesErrorBody](walmart_apis/errors/refund_order_lines_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RefundOrderLinesResponse](walmart_apis/models/refund_order_lines_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RefundOrderLinesErrorBody](walmart_apis/errors/refund_order_lines_error.py)</code>

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
<summary><code>def ship_order_lines(purchase_order_id: str, body: ShipOrderLinesRequest | ShipOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ShipOrderLinesResponse, ShipOrderLinesErrorBody]</code></summary>

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
result = client.orders.with_raw_response.ship_order_lines(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ShipOrderLinesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ShipOrderLinesErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.ship_order_lines(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ShipOrderLinesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ShipOrderLinesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ShipOrderLinesResponse](walmart_apis/models/ship_order_lines_response.py), [ShipOrderLinesErrorBody](walmart_apis/errors/ship_order_lines_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ShipOrderLinesResponse](walmart_apis/models/ship_order_lines_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ShipOrderLinesErrorBody](walmart_apis/errors/ship_order_lines_error.py)</code>

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
<summary><code>def ship_order_multi_package(purchase_order_id: str, body: MultiPackageShipRequest | MultiPackageShipRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[MultiPackageShipResponse, ShipOrderMultiPackageErrorBody]</code></summary>

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
result = client.orders.with_raw_response.ship_order_multi_package(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MultiPackageShipResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ShipOrderMultiPackageErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.ship_order_multi_package(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type MultiPackageShipResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ShipOrderMultiPackageErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[MultiPackageShipResponse](walmart_apis/models/multi_package_ship_response.py), [ShipOrderMultiPackageErrorBody](walmart_apis/errors/ship_order_multi_package_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[MultiPackageShipResponse](walmart_apis/models/multi_package_ship_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ShipOrderMultiPackageErrorBody](walmart_apis/errors/ship_order_multi_package_error.py)</code>

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
<summary><code>def update_shipment_status(purchase_order_id: str, body: UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateShipmentStatusResponse, UpdateShipmentStatusErrorBody]</code></summary>

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
result = client.orders.with_raw_response.update_shipment_status(
    "some example string",
    UpdateShipmentStatusRequest(
        shipment_status=ShipmentStatusOrders.READY_FOR_PICKUP,
        order_lines=[UpdateShipmentStatusLine(line_number="some example string")],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateShipmentStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateShipmentStatusErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.update_shipment_status(
    "some example string",
    UpdateShipmentStatusRequest(
        shipment_status=ShipmentStatusOrders.READY_FOR_PICKUP,
        order_lines=[UpdateShipmentStatusLine(line_number="some example string")],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateShipmentStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateShipmentStatusErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[UpdateShipmentStatusResponse](walmart_apis/models/update_shipment_status_response.py), [UpdateShipmentStatusErrorBody](walmart_apis/errors/update_shipment_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateShipmentStatusResponse](walmart_apis/models/update_shipment_status_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[UpdateShipmentStatusErrorBody](walmart_apis/errors/update_shipment_status_error.py)</code>

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
<summary><code>def update_verification_status(purchase_order_id: str, body: UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateVerificationStatusResponse, UpdateVerificationStatusErrorBody]</code></summary>

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
result = client.orders.with_raw_response.update_verification_status(
    "some example string", UpdateVerificationStatusRequest(verification_status=VerificationStatus.APPROVED)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateVerificationStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateVerificationStatusErrorBody
```

**Async**

```python
result = await async_client.orders.with_raw_response.update_verification_status(
    "some example string", UpdateVerificationStatusRequest(verification_status=VerificationStatus.APPROVED)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateVerificationStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateVerificationStatusErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[UpdateVerificationStatusResponse](walmart_apis/models/update_verification_status_response.py), [UpdateVerificationStatusErrorBody](walmart_apis/errors/update_verification_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateVerificationStatusResponse](walmart_apis/models/update_verification_status_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[UpdateVerificationStatusErrorBody](walmart_apis/errors/update_verification_status_error.py)</code>

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
<summary><code>def configure_auto_payout(body: ConfigureAutoPayoutRequest | ConfigureAutoPayoutRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PayoutStatusResponse, ConfigureAutoPayoutErrorBody]</code></summary>

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
result = client.payouts.with_raw_response.configure_auto_payout(ConfigureAutoPayoutRequest(enabled=True))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PayoutStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfigureAutoPayoutErrorBody
```

**Async**

```python
result = await async_client.payouts.with_raw_response.configure_auto_payout(ConfigureAutoPayoutRequest(enabled=True))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PayoutStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfigureAutoPayoutErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[PayoutStatusResponse](walmart_apis/models/payout_status_response.py), [ConfigureAutoPayoutErrorBody](walmart_apis/errors/configure_auto_payout_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PayoutStatusResponse](walmart_apis/models/payout_status_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ConfigureAutoPayoutErrorBody](walmart_apis/errors/configure_auto_payout_error.py)</code>

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
<summary><code>def get_annual_statement_opts(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AnnualStatementOptsResponse, GetAnnualStatementOptsErrorBody]</code></summary>

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
result = client.payouts.with_raw_response.get_annual_statement_opts()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnnualStatementOptsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAnnualStatementOptsErrorBody
```

**Async**

```python
result = await async_client.payouts.with_raw_response.get_annual_statement_opts()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnnualStatementOptsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAnnualStatementOptsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[AnnualStatementOptsResponse](walmart_apis/models/annual_statement_opts_response.py), [GetAnnualStatementOptsErrorBody](walmart_apis/errors/get_annual_statement_opts_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AnnualStatementOptsResponse](walmart_apis/models/annual_statement_opts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetAnnualStatementOptsErrorBody](walmart_apis/errors/get_annual_statement_opts_error.py)</code>

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
<summary><code>def get_faster_payout_eligibility(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FasterPayoutEligibilityResponse, GetFasterPayoutEligibilityErrorBody]</code></summary>

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
result = client.payouts.with_raw_response.get_faster_payout_eligibility()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FasterPayoutEligibilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFasterPayoutEligibilityErrorBody
```

**Async**

```python
result = await async_client.payouts.with_raw_response.get_faster_payout_eligibility()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FasterPayoutEligibilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetFasterPayoutEligibilityErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[FasterPayoutEligibilityResponse](walmart_apis/models/faster_payout_eligibility_response.py), [GetFasterPayoutEligibilityErrorBody](walmart_apis/errors/get_faster_payout_eligibility_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FasterPayoutEligibilityResponse](walmart_apis/models/faster_payout_eligibility_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetFasterPayoutEligibilityErrorBody](walmart_apis/errors/get_faster_payout_eligibility_error.py)</code>

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
<summary><code>def get_payment_status(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PayoutStatusResponse, GetPaymentStatusErrorBody]</code></summary>

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
result = client.payouts.with_raw_response.get_payment_status()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PayoutStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPaymentStatusErrorBody
```

**Async**

```python
result = await async_client.payouts.with_raw_response.get_payment_status()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PayoutStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPaymentStatusErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[PayoutStatusResponse](walmart_apis/models/payout_status_response.py), [GetPaymentStatusErrorBody](walmart_apis/errors/get_payment_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PayoutStatusResponse](walmart_apis/models/payout_status_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetPaymentStatusErrorBody](walmart_apis/errors/get_payment_status_error.py)</code>

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
<summary><code>def initiate_faster_payout(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InitiatePayoutResponse, InitiateFasterPayoutErrorBody]</code></summary>

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
result = client.payouts.with_raw_response.initiate_faster_payout()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InitiatePayoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InitiateFasterPayoutErrorBody
```

**Async**

```python
result = await async_client.payouts.with_raw_response.initiate_faster_payout()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InitiatePayoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type InitiateFasterPayoutErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[InitiatePayoutResponse](walmart_apis/models/initiate_payout_response.py), [InitiateFasterPayoutErrorBody](walmart_apis/errors/initiate_faster_payout_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[InitiatePayoutResponse](walmart_apis/models/initiate_payout_response.py)</code> -- Payout initiated

**On `Failure`**: `error` is <code>[InitiateFasterPayoutErrorBody](walmart_apis/errors/initiate_faster_payout_error.py)</code>

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
<summary><code>def get_definitions_product_type(product_type: str, *, seller_id: str | None = None, locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProductTypeDefinition, GetDefinitionsProductTypeErrorBody]</code></summary>

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
result = client.product_type_definitions.with_raw_response.get_definitions_product_type("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProductTypeDefinition
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDefinitionsProductTypeErrorBody
```

**Async**

```python
result = await async_client.product_type_definitions.with_raw_response.get_definitions_product_type(
    "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProductTypeDefinition
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDefinitionsProductTypeErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ProductTypeDefinition](walmart_apis/models/product_type_definition.py), [GetDefinitionsProductTypeErrorBody](walmart_apis/errors/get_definitions_product_type_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProductTypeDefinition](walmart_apis/models/product_type_definition.py)</code> -- Product type definition schema

**On `Failure`**: `error` is <code>[GetDefinitionsProductTypeErrorBody](walmart_apis/errors/get_definitions_product_type_error.py)</code>

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
<summary><code>def get_taxonomy(*, category: str | None = None, locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ApiResult[Taxonomy, GetTaxonomyErrorBody]</code></summary>

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
result = client.product_type_definitions.with_raw_response.get_taxonomy()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Taxonomy
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTaxonomyErrorBody
```

**Async**

```python
result = await async_client.product_type_definitions.with_raw_response.get_taxonomy()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Taxonomy
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTaxonomyErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Taxonomy](walmart_apis/models/taxonomy.py), [GetTaxonomyErrorBody](walmart_apis/errors/get_taxonomy_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Taxonomy](walmart_apis/models/taxonomy.py)</code> -- Taxonomy tree

**On `Failure`**: `error` is <code>[GetTaxonomyErrorBody](walmart_apis/errors/get_taxonomy_error.py)</code>

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
<summary><code>def search_definitions_product_types(*, keywords: str | None = None, item_name: str | None = None, locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None) -> ApiResult[ProductTypeList, SearchDefinitionsProductTypesErrorBody]</code></summary>

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
result = client.product_type_definitions.with_raw_response.search_definitions_product_types()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProductTypeList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchDefinitionsProductTypesErrorBody
```

**Async**

```python
result = await async_client.product_type_definitions.with_raw_response.search_definitions_product_types()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ProductTypeList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchDefinitionsProductTypesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ProductTypeList](walmart_apis/models/product_type_list.py), [SearchDefinitionsProductTypesErrorBody](walmart_apis/errors/search_definitions_product_types_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ProductTypeList](walmart_apis/models/product_type_list.py)</code> -- Product type list

**On `Failure`**: `error` is <code>[SearchDefinitionsProductTypesErrorBody](walmart_apis/errors/search_definitions_product_types_error.py)</code>

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
<summary><code>def check_download_report_by_period(partner_id: str, date: Date, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReportAvailabilityResponse, CheckDownloadReportByPeriodErrorBody]</code></summary>

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
result = client.reconciliation.with_raw_response.check_download_report_by_period(
    "some example string", date(2024, 1, 15)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportAvailabilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CheckDownloadReportByPeriodErrorBody
```

**Async**

```python
result = await async_client.reconciliation.with_raw_response.check_download_report_by_period(
    "some example string", date(2024, 1, 15)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportAvailabilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CheckDownloadReportByPeriodErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReportAvailabilityResponse](walmart_apis/models/report_availability_response.py), [CheckDownloadReportByPeriodErrorBody](walmart_apis/errors/check_download_report_by_period_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReportAvailabilityResponse](walmart_apis/models/report_availability_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[CheckDownloadReportByPeriodErrorBody](walmart_apis/errors/check_download_report_by_period_error.py)</code>

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
<summary><code>def download_reconciliation_report(reconciliation_report_id: str, partner_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, DownloadReconciliationReportErrorBody]</code></summary>

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
result = client.reconciliation.with_raw_response.download_reconciliation_report(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadReconciliationReportErrorBody
```

**Async**

```python
result = await async_client.reconciliation.with_raw_response.download_reconciliation_report(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadReconciliationReportErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [DownloadReconciliationReportErrorBody](walmart_apis/errors/download_reconciliation_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- ZIP file stream

**On `Failure`**: `error` is <code>[DownloadReconciliationReportErrorBody](walmart_apis/errors/download_reconciliation_report_error.py)</code>

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
<summary><code>def list_reconciliation_dates(partner_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReportAvailabilityResponse, ListReconciliationDatesErrorBody]</code></summary>

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
result = client.reconciliation.with_raw_response.list_reconciliation_dates("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportAvailabilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListReconciliationDatesErrorBody
```

**Async**

```python
result = await async_client.reconciliation.with_raw_response.list_reconciliation_dates("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportAvailabilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListReconciliationDatesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReportAvailabilityResponse](walmart_apis/models/report_availability_response.py), [ListReconciliationDatesErrorBody](walmart_apis/errors/list_reconciliation_dates_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReportAvailabilityResponse](walmart_apis/models/report_availability_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListReconciliationDatesErrorBody](walmart_apis/errors/list_reconciliation_dates_error.py)</code>

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
<summary><code>def cancel_report_schedule(schedule_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelReportScheduleResponse, CancelReportScheduleErrorBody]</code></summary>

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
result = client.report_schedules.with_raw_response.cancel_report_schedule("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelReportScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelReportScheduleErrorBody
```

**Async**

```python
result = await async_client.report_schedules.with_raw_response.cancel_report_schedule("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelReportScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelReportScheduleErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelReportScheduleResponse](walmart_apis/models/cancel_report_schedule_response.py), [CancelReportScheduleErrorBody](walmart_apis/errors/cancel_report_schedule_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelReportScheduleResponse](walmart_apis/models/cancel_report_schedule_response.py)</code> -- Schedule cancelled

**On `Failure`**: `error` is <code>[CancelReportScheduleErrorBody](walmart_apis/errors/cancel_report_schedule_error.py)</code>

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
<summary><code>def create_report_schedule(body: CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateReportScheduleResponse, CreateReportScheduleErrorBody]</code></summary>

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
result = client.report_schedules.with_raw_response.create_report_schedule(
    CreateReportScheduleSpecification(report_type="some example string", period=Period1.PT5_M)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateReportScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateReportScheduleErrorBody
```

**Async**

```python
result = await async_client.report_schedules.with_raw_response.create_report_schedule(
    CreateReportScheduleSpecification(report_type="some example string", period=Period1.PT5_M)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateReportScheduleResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateReportScheduleErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateReportScheduleResponse](walmart_apis/models/create_report_schedule_response.py), [CreateReportScheduleErrorBody](walmart_apis/errors/create_report_schedule_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateReportScheduleResponse](walmart_apis/models/create_report_schedule_response.py)</code> -- Schedule created

**On `Failure`**: `error` is <code>[CreateReportScheduleErrorBody](walmart_apis/errors/create_report_schedule_error.py)</code>

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
<summary><code>def get_report_schedule(schedule_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReportSchedule, GetReportScheduleErrorBody]</code></summary>

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
result = client.report_schedules.with_raw_response.get_report_schedule("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportSchedule
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportScheduleErrorBody
```

**Async**

```python
result = await async_client.report_schedules.with_raw_response.get_report_schedule("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportSchedule
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportScheduleErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReportSchedule](walmart_apis/models/report_schedule.py), [GetReportScheduleErrorBody](walmart_apis/errors/get_report_schedule_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReportSchedule](walmart_apis/models/report_schedule.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetReportScheduleErrorBody](walmart_apis/errors/get_report_schedule_error.py)</code>

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
<summary><code>def get_report_schedules(*, report_types: list[ReportType1OrStr] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetReportSchedulesResponse, GetReportSchedulesErrorBody]</code></summary>

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
result = client.report_schedules.with_raw_response.get_report_schedules()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetReportSchedulesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportSchedulesErrorBody
```

**Async**

```python
result = await async_client.report_schedules.with_raw_response.get_report_schedules()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetReportSchedulesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportSchedulesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetReportSchedulesResponse](walmart_apis/models/get_report_schedules_response.py), [GetReportSchedulesErrorBody](walmart_apis/errors/get_report_schedules_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetReportSchedulesResponse](walmart_apis/models/get_report_schedules_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetReportSchedulesErrorBody](walmart_apis/errors/get_report_schedules_error.py)</code>

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
<summary><code>def cancel_report(report_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelReportResponse, CancelReportErrorBody]</code></summary>

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
result = client.reports.with_raw_response.cancel_report("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelReportErrorBody
```

**Async**

```python
result = await async_client.reports.with_raw_response.cancel_report("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelReportErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelReportResponse](walmart_apis/models/cancel_report_response.py), [CancelReportErrorBody](walmart_apis/errors/cancel_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelReportResponse](walmart_apis/models/cancel_report_response.py)</code> -- Report cancelled

**On `Failure`**: `error` is <code>[CancelReportErrorBody](walmart_apis/errors/cancel_report_error.py)</code>

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
<summary><code>def create_report(body: CreateReportSpecification | CreateReportSpecificationDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateReportResponse, CreateReportErrorBody]</code></summary>

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
result = client.reports.with_raw_response.create_report(CreateReportSpecification(report_type=ReportType.ITEM))
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateReportErrorBody
```

**Async**

```python
result = await async_client.reports.with_raw_response.create_report(
    CreateReportSpecification(report_type=ReportType.ITEM)
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateReportResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateReportErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateReportResponse](walmart_apis/models/create_report_response.py), [CreateReportErrorBody](walmart_apis/errors/create_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateReportResponse](walmart_apis/models/create_report_response.py)</code> -- Report request accepted

**On `Failure`**: `error` is <code>[CreateReportErrorBody](walmart_apis/errors/create_report_error.py)</code>

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
<summary><code>def download_new_report(summary_report_id: str, partner_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, DownloadNewReportErrorBody]</code></summary>

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
result = client.reports.with_raw_response.download_new_report("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadNewReportErrorBody
```

**Async**

```python
result = await async_client.reports.with_raw_response.download_new_report("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadNewReportErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [DownloadNewReportErrorBody](walmart_apis/errors/download_new_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- ZIP file stream

**On `Failure`**: `error` is <code>[DownloadNewReportErrorBody](walmart_apis/errors/download_new_report_error.py)</code>

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
<summary><code>def download_old_report(summary_report_id: str, partner_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FileResponse, DownloadOldReportErrorBody]</code></summary>

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
result = client.reports.with_raw_response.download_old_report("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadOldReportErrorBody
```

**Async**

```python
result = await async_client.reports.with_raw_response.download_old_report("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsyncFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadOldReportErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;FileResponse, [DownloadOldReportErrorBody](walmart_apis/errors/download_old_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>FileResponse</code>, its body not yet read -- ZIP file stream

**On `Failure`**: `error` is <code>[DownloadOldReportErrorBody](walmart_apis/errors/download_old_report_error.py)</code>

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
<summary><code>def get_report(report_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Report, GetReportErrorBody]</code></summary>

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
result = client.reports.with_raw_response.get_report("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Report
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportErrorBody
```

**Async**

```python
result = await async_client.reports.with_raw_response.get_report("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Report
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Report](walmart_apis/models/report.py), [GetReportErrorBody](walmart_apis/errors/get_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Report](walmart_apis/models/report.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetReportErrorBody](walmart_apis/errors/get_report_error.py)</code>

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
<summary><code>def get_report_document(document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReportDocument, GetReportDocumentErrorBody]</code></summary>

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
result = client.reports.with_raw_response.get_report_document("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportDocument
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportDocumentErrorBody
```

**Async**

```python
result = await async_client.reports.with_raw_response.get_report_document("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReportDocument
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportDocumentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ReportDocument](walmart_apis/models/report_document.py), [GetReportDocumentErrorBody](walmart_apis/errors/get_report_document_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReportDocument](walmart_apis/models/report_document.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetReportDocumentErrorBody](walmart_apis/errors/get_report_document_error.py)</code>

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
<summary><code>def get_reports(*, report_types: list[ReportType1OrStr] | None = None, processing_statuses: list[ProcessingStatusOrStr] | None = None, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetReportsResponse, GetReportsErrorBody]</code></summary>

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
result = client.reports.with_raw_response.get_reports()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetReportsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportsErrorBody
```

**Async**

```python
result = await async_client.reports.with_raw_response.get_reports()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetReportsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetReportsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetReportsResponse](walmart_apis/models/get_reports_response.py), [GetReportsErrorBody](walmart_apis/errors/get_reports_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetReportsResponse](walmart_apis/models/get_reports_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetReportsErrorBody](walmart_apis/errors/get_reports_error.py)</code>

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
<summary><code>def get_account(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SellerAccount, GetAccountErrorBody]</code></summary>

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
result = client.sellers.with_raw_response.get_account()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SellerAccount
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountErrorBody
```

**Async**

```python
result = await async_client.sellers.with_raw_response.get_account()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SellerAccount
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SellerAccount](walmart_apis/models/seller_account.py), [GetAccountErrorBody](walmart_apis/errors/get_account_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SellerAccount](walmart_apis/models/seller_account.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetAccountErrorBody](walmart_apis/errors/get_account_error.py)</code>

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
<summary><code>def get_marketplace_participations(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetMarketplaceParticipationsResponse, GetMarketplaceParticipationsErrorBody]</code></summary>

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
result = client.sellers.with_raw_response.get_marketplace_participations()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetMarketplaceParticipationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMarketplaceParticipationsErrorBody
```

**Async**

```python
result = await async_client.sellers.with_raw_response.get_marketplace_participations()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetMarketplaceParticipationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMarketplaceParticipationsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetMarketplaceParticipationsResponse](walmart_apis/models/get_marketplace_participations_response.py), [GetMarketplaceParticipationsErrorBody](walmart_apis/errors/get_marketplace_participations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetMarketplaceParticipationsResponse](walmart_apis/models/get_marketplace_participations_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetMarketplaceParticipationsErrorBody](walmart_apis/errors/get_marketplace_participations_error.py)</code>

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
<summary><code>def list_settlement_details(partner_id: str, report_date: str, *, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SettlementDetailsResponse, ListSettlementDetailsErrorBody]</code></summary>

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
result = client.settlement.with_raw_response.list_settlement_details("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SettlementDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListSettlementDetailsErrorBody
```

**Async**

```python
result = await async_client.settlement.with_raw_response.list_settlement_details(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SettlementDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListSettlementDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SettlementDetailsResponse](walmart_apis/models/settlement_details_response.py), [ListSettlementDetailsErrorBody](walmart_apis/errors/list_settlement_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SettlementDetailsResponse](walmart_apis/models/settlement_details_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListSettlementDetailsErrorBody](walmart_apis/errors/list_settlement_details_error.py)</code>

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
<summary><code>def list_settlement_periods(*, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SettlementPeriodsResponse, ListSettlementPeriodsErrorBody]</code></summary>

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
result = client.settlement.with_raw_response.list_settlement_periods()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SettlementPeriodsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListSettlementPeriodsErrorBody
```

**Async**

```python
result = await async_client.settlement.with_raw_response.list_settlement_periods()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SettlementPeriodsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListSettlementPeriodsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SettlementPeriodsResponse](walmart_apis/models/settlement_periods_response.py), [ListSettlementPeriodsErrorBody](walmart_apis/errors/list_settlement_periods_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SettlementPeriodsResponse](walmart_apis/models/settlement_periods_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListSettlementPeriodsErrorBody](walmart_apis/errors/list_settlement_periods_error.py)</code>

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
<summary><code>def search_transactions(*, page_size: int | None = 10, next_token: str | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionSearchResponse, SearchTransactionsErrorBody]</code></summary>

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
result = client.settlement.with_raw_response.search_transactions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchTransactionsErrorBody
```

**Async**

```python
result = await async_client.settlement.with_raw_response.search_transactions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionSearchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SearchTransactionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[TransactionSearchResponse](walmart_apis/models/transaction_search_response.py), [SearchTransactionsErrorBody](walmart_apis/errors/search_transactions_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionSearchResponse](walmart_apis/models/transaction_search_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[SearchTransactionsErrorBody](walmart_apis/errors/search_transactions_error.py)</code>

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
<summary><code>def create_supply_source(body: CreateSupplySourceRequest | CreateSupplySourceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateSupplySourceResponse, CreateSupplySourceErrorBody]</code></summary>

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
result = client.supply_source_api.with_raw_response.create_supply_source(
    CreateSupplySourceRequest(supply_source_code="some example string", address=AddressShippingManagement())
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateSupplySourceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateSupplySourceErrorBody
```

**Async**

```python
result = await async_client.supply_source_api.with_raw_response.create_supply_source(
    CreateSupplySourceRequest(supply_source_code="some example string", address=AddressShippingManagement())
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateSupplySourceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateSupplySourceErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateSupplySourceResponse](walmart_apis/models/create_supply_source_response.py), [CreateSupplySourceErrorBody](walmart_apis/errors/create_supply_source_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateSupplySourceResponse](walmart_apis/models/create_supply_source_response.py)</code> -- Supply source created successfully

**On `Failure`**: `error` is <code>[CreateSupplySourceErrorBody](walmart_apis/errors/create_supply_source_error.py)</code>

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
<summary><code>def get_supply_source(supply_source_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SupplySource, GetSupplySourceErrorBody]</code></summary>

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
result = client.supply_source_api.with_raw_response.get_supply_source("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SupplySource
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSupplySourceErrorBody
```

**Async**

```python
result = await async_client.supply_source_api.with_raw_response.get_supply_source("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SupplySource
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSupplySourceErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SupplySource](walmart_apis/models/supply_source.py), [GetSupplySourceErrorBody](walmart_apis/errors/get_supply_source_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SupplySource](walmart_apis/models/supply_source.py)</code> -- Supply source returned successfully

**On `Failure`**: `error` is <code>[GetSupplySourceErrorBody](walmart_apis/errors/get_supply_source_error.py)</code>

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
<summary><code>def list_supply_sources(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[SupplySource], ListSupplySourcesErrorBody]</code></summary>

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
result = client.supply_source_api.with_raw_response.list_supply_sources()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[SupplySource]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListSupplySourcesErrorBody
```

**Async**

```python
result = await async_client.supply_source_api.with_raw_response.list_supply_sources()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[SupplySource]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListSupplySourcesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;list&#91;[SupplySource](walmart_apis/models/supply_source.py)&#93;, [ListSupplySourcesErrorBody](walmart_apis/errors/list_supply_sources_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[SupplySource](walmart_apis/models/supply_source.py)&#93;</code> -- Supply sources returned successfully

**On `Failure`**: `error` is <code>[ListSupplySourcesErrorBody](walmart_apis/errors/list_supply_sources_error.py)</code>

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
<summary><code>def update_supply_source(supply_source_id: str, body: UpdateSupplySourceRequest | UpdateSupplySourceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, UpdateSupplySourceErrorBody]</code></summary>

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
result = client.supply_source_api.with_raw_response.update_supply_source(
    "some example string", UpdateSupplySourceRequest()
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateSupplySourceErrorBody
```

**Async**

```python
result = await async_client.supply_source_api.with_raw_response.update_supply_source(
    "some example string", UpdateSupplySourceRequest()
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateSupplySourceErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;None, [UpdateSupplySourceErrorBody](walmart_apis/errors/update_supply_source_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[UpdateSupplySourceErrorBody](walmart_apis/errors/update_supply_source_error.py)</code>

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
<summary><code>def create_upload_destination_for_resource(resource: ResourceOrStr, content_type: ContentTypeUploadsFeedDocumentsOrStr, marketplace_ids: list[str], content_md5: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateUploadDestinationResponse, CreateUploadDestinationForResourceErrorBody]</code></summary>

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
result = client.uploads.with_raw_response.create_upload_destination_for_resource(
    Resource.FEEDS,
    ContentTypeUploadsFeedDocuments.TEXT_XML_CHARSET_UTF_8,
    ["some example string"],
    "some example string",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateUploadDestinationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateUploadDestinationForResourceErrorBody
```

**Async**

```python
result = await async_client.uploads.with_raw_response.create_upload_destination_for_resource(
    Resource.FEEDS,
    ContentTypeUploadsFeedDocuments.TEXT_XML_CHARSET_UTF_8,
    ["some example string"],
    "some example string",
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateUploadDestinationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateUploadDestinationForResourceErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateUploadDestinationResponse](walmart_apis/models/create_upload_destination_response.py), [CreateUploadDestinationForResourceErrorBody](walmart_apis/errors/create_upload_destination_for_resource_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateUploadDestinationResponse](walmart_apis/models/create_upload_destination_response.py)</code> -- Upload destination created

**On `Failure`**: `error` is <code>[CreateUploadDestinationForResourceErrorBody](walmart_apis/errors/create_upload_destination_for_resource_error.py)</code>

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
<summary><code>def get_wfs_inventory_items(*, skus: str | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetWfsInventoryResponse, GetWfsInventoryItemsErrorBody]</code></summary>

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
result = client.wfs_inventory.with_raw_response.get_wfs_inventory_items()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetWfsInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetWfsInventoryItemsErrorBody
```

**Async**

```python
result = await async_client.wfs_inventory.with_raw_response.get_wfs_inventory_items()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetWfsInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetWfsInventoryItemsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetWfsInventoryResponse](walmart_apis/models/get_wfs_inventory_response.py), [GetWfsInventoryItemsErrorBody](walmart_apis/errors/get_wfs_inventory_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetWfsInventoryResponse](walmart_apis/models/get_wfs_inventory_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetWfsInventoryItemsErrorBody](walmart_apis/errors/get_wfs_inventory_items_error.py)</code>

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
<summary><code>def create_warranty(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateWarrantyErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.create_warranty("some example string", ["some example string"], {})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateWarrantyErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.create_warranty(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateWarrantyErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateWarrantyErrorBody](walmart_apis/errors/create_warranty_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateWarrantyErrorBody](walmart_apis/errors/create_warranty_error.py)</code>

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
<summary><code>def get_attributes(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GetAttributesErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.get_attributes("some example string", ["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAttributesErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.get_attributes("some example string", ["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAttributesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [GetAttributesErrorBody](walmart_apis/errors/get_attributes_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[GetAttributesErrorBody](walmart_apis/errors/get_attributes_error.py)</code>

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
<summary><code>def confirm_customization_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, ConfirmCustomizationDetailsErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.confirm_customization_details(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmCustomizationDetailsErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.confirm_customization_details(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmCustomizationDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [ConfirmCustomizationDetailsErrorBody](walmart_apis/errors/confirm_customization_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[ConfirmCustomizationDetailsErrorBody](walmart_apis/errors/confirm_customization_details_error.py)</code>

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
<summary><code>def create_confirm_delivery_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateConfirmDeliveryDetailsErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.create_confirm_delivery_details(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateConfirmDeliveryDetailsErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.create_confirm_delivery_details(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateConfirmDeliveryDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateConfirmDeliveryDetailsErrorBody](walmart_apis/errors/create_confirm_delivery_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateConfirmDeliveryDetailsErrorBody](walmart_apis/errors/create_confirm_delivery_details_error.py)</code>

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
<summary><code>def create_confirm_order_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateConfirmOrderDetailsErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.create_confirm_order_details(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateConfirmOrderDetailsErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.create_confirm_order_details(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateConfirmOrderDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateConfirmOrderDetailsErrorBody](walmart_apis/errors/create_confirm_order_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateConfirmOrderDetailsErrorBody](walmart_apis/errors/create_confirm_order_details_error.py)</code>

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
<summary><code>def create_confirm_service_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateConfirmServiceDetailsErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.create_confirm_service_details(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateConfirmServiceDetailsErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.create_confirm_service_details(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateConfirmServiceDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateConfirmServiceDetailsErrorBody](walmart_apis/errors/create_confirm_service_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateConfirmServiceDetailsErrorBody](walmart_apis/errors/create_confirm_service_details_error.py)</code>

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
<summary><code>def create_digital_access_key(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateDigitalAccessKeyErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.create_digital_access_key(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateDigitalAccessKeyErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.create_digital_access_key(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateDigitalAccessKeyErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateDigitalAccessKeyErrorBody](walmart_apis/errors/create_digital_access_key_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateDigitalAccessKeyErrorBody](walmart_apis/errors/create_digital_access_key_error.py)</code>

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
<summary><code>def create_legal_disclosure(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateLegalDisclosureErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.create_legal_disclosure("some example string", ["some example string"], {})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateLegalDisclosureErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.create_legal_disclosure(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateLegalDisclosureErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateLegalDisclosureErrorBody](walmart_apis/errors/create_legal_disclosure_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateLegalDisclosureErrorBody](walmart_apis/errors/create_legal_disclosure_error.py)</code>

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
<summary><code>def create_unexpected_problem(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateUnexpectedProblemErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.create_unexpected_problem(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateUnexpectedProblemErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.create_unexpected_problem(
    "some example string", ["some example string"], {}
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateUnexpectedProblemErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateUnexpectedProblemErrorBody](walmart_apis/errors/create_unexpected_problem_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateUnexpectedProblemErrorBody](walmart_apis/errors/create_unexpected_problem_error.py)</code>

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
<summary><code>def get_messaging_actions_for_order(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GetMessagingActionsForOrderErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.get_messaging_actions_for_order(
    "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMessagingActionsForOrderErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.get_messaging_actions_for_order(
    "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMessagingActionsForOrderErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [GetMessagingActionsForOrderErrorBody](walmart_apis/errors/get_messaging_actions_for_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[GetMessagingActionsForOrderErrorBody](walmart_apis/errors/get_messaging_actions_for_order_error.py)</code>

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
<summary><code>def send_invoice(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, SendInvoiceErrorBody]</code></summary>

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
result = client.messaging.with_raw_response.send_invoice("some example string", ["some example string"], {})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SendInvoiceErrorBody
```

**Async**

```python
result = await async_client.messaging.with_raw_response.send_invoice("some example string", ["some example string"], {})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SendInvoiceErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [SendInvoiceErrorBody](walmart_apis/errors/send_invoice_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[SendInvoiceErrorBody](walmart_apis/errors/send_invoice_error.py)</code>

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
<summary><code>def create_destination(body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Channel, CreateDestinationErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.create_destination({})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Channel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateDestinationErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.create_destination({})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Channel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateDestinationErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Channel](walmart_apis/models/channel.py), [CreateDestinationErrorBody](walmart_apis/errors/create_destination_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Channel](walmart_apis/models/channel.py)</code> -- Success

**On `Failure`**: `error` is <code>[CreateDestinationErrorBody](walmart_apis/errors/create_destination_error.py)</code>

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
<summary><code>def create_subscription(notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateSubscriptionErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.create_subscription("some example string", {})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateSubscriptionErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.create_subscription("some example string", {})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateSubscriptionErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateSubscriptionErrorBody](walmart_apis/errors/create_subscription_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateSubscriptionErrorBody](walmart_apis/errors/create_subscription_error.py)</code>

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
<summary><code>def delete_destination(destination_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Channel, DeleteDestinationErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.delete_destination("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Channel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteDestinationErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.delete_destination("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Channel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteDestinationErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Channel](walmart_apis/models/channel.py), [DeleteDestinationErrorBody](walmart_apis/errors/delete_destination_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Channel](walmart_apis/models/channel.py)</code> -- Success

**On `Failure`**: `error` is <code>[DeleteDestinationErrorBody](walmart_apis/errors/delete_destination_error.py)</code>

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
<summary><code>def delete_subscription_by_id(subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, DeleteSubscriptionByIdErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.delete_subscription_by_id("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteSubscriptionByIdErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.delete_subscription_by_id(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteSubscriptionByIdErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [DeleteSubscriptionByIdErrorBody](walmart_apis/errors/delete_subscription_by_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[DeleteSubscriptionByIdErrorBody](walmart_apis/errors/delete_subscription_by_id_error.py)</code>

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
<summary><code>def get_destination(destination_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Channel, GetDestinationErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.get_destination("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Channel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDestinationErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.get_destination("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Channel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDestinationErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[Channel](walmart_apis/models/channel.py), [GetDestinationErrorBody](walmart_apis/errors/get_destination_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Channel](walmart_apis/models/channel.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetDestinationErrorBody](walmart_apis/errors/get_destination_error.py)</code>

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
<summary><code>def get_destinations(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChannelList, GetDestinationsErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.get_destinations()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChannelList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDestinationsErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.get_destinations()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChannelList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDestinationsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ChannelList](walmart_apis/models/channel_list.py), [GetDestinationsErrorBody](walmart_apis/errors/get_destinations_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChannelList](walmart_apis/models/channel_list.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetDestinationsErrorBody](walmart_apis/errors/get_destinations_error.py)</code>

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
<summary><code>def get_subscription(notification_type: str, *, payload_version: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GetSubscriptionErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.get_subscription("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSubscriptionErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.get_subscription("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSubscriptionErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [GetSubscriptionErrorBody](walmart_apis/errors/get_subscription_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[GetSubscriptionErrorBody](walmart_apis/errors/get_subscription_error.py)</code>

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
<summary><code>def get_subscription_by_id(subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GetSubscriptionByIdErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.get_subscription_by_id("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSubscriptionByIdErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.get_subscription_by_id(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSubscriptionByIdErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [GetSubscriptionByIdErrorBody](walmart_apis/errors/get_subscription_by_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[GetSubscriptionByIdErrorBody](walmart_apis/errors/get_subscription_by_id_error.py)</code>

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
<summary><code>def send_test_notification(notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, SendTestNotificationErrorBody]</code></summary>

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
result = client.notifications.with_raw_response.send_test_notification("some example string", {})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SendTestNotificationErrorBody
```

**Async**

```python
result = await async_client.notifications.with_raw_response.send_test_notification("some example string", {})
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SendTestNotificationErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [SendTestNotificationErrorBody](walmart_apis/errors/send_test_notification_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[SendTestNotificationErrorBody](walmart_apis/errors/send_test_notification_error.py)</code>

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
<summary><code>def get_my_fees_estimate_for_item(walmart_item_id: str, body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetMyFeesEstimateResponse, GetMyFeesEstimateForItemErrorBody]</code></summary>

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
result = client.product_fees.with_raw_response.get_my_fees_estimate_for_item(
    "some example string", GetMyFeesEstimateRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetMyFeesEstimateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMyFeesEstimateForItemErrorBody
```

**Async**

```python
result = await async_client.product_fees.with_raw_response.get_my_fees_estimate_for_item(
    "some example string", GetMyFeesEstimateRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetMyFeesEstimateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMyFeesEstimateForItemErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetMyFeesEstimateResponse](walmart_apis/models/get_my_fees_estimate_response.py), [GetMyFeesEstimateForItemErrorBody](walmart_apis/errors/get_my_fees_estimate_for_item_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetMyFeesEstimateResponse](walmart_apis/models/get_my_fees_estimate_response.py)</code> -- Returns the fee estimate result for the requested item.

**On `Failure`**: `error` is <code>[GetMyFeesEstimateForItemErrorBody](walmart_apis/errors/get_my_fees_estimate_for_item_error.py)</code>

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
<summary><code>def get_my_fees_estimate_for_sku(seller_sku: str, marketplace_id: str, body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetMyFeesEstimateResponse, GetMyFeesEstimateForSkuErrorBody]</code></summary>

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
result = client.product_fees.with_raw_response.get_my_fees_estimate_for_sku(
    "some example string", "some example string", GetMyFeesEstimateRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetMyFeesEstimateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMyFeesEstimateForSkuErrorBody
```

**Async**

```python
result = await async_client.product_fees.with_raw_response.get_my_fees_estimate_for_sku(
    "some example string", "some example string", GetMyFeesEstimateRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetMyFeesEstimateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMyFeesEstimateForSkuErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetMyFeesEstimateResponse](walmart_apis/models/get_my_fees_estimate_response.py), [GetMyFeesEstimateForSkuErrorBody](walmart_apis/errors/get_my_fees_estimate_for_sku_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetMyFeesEstimateResponse](walmart_apis/models/get_my_fees_estimate_response.py)</code> -- Returns the fee estimate result for the specified listing.

**On `Failure`**: `error` is <code>[GetMyFeesEstimateForSkuErrorBody](walmart_apis/errors/get_my_fees_estimate_for_sku_error.py)</code>

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
<summary><code>def get_my_fees_estimates(body: list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[FeesEstimateResult], GetMyFeesEstimatesErrorBody]</code></summary>

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
result = client.product_fees.with_raw_response.get_my_fees_estimates(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[FeesEstimateResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMyFeesEstimatesErrorBody
```

**Async**

```python
result = await async_client.product_fees.with_raw_response.get_my_fees_estimates(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[FeesEstimateResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetMyFeesEstimatesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;list&#91;[FeesEstimateResult](walmart_apis/models/fees_estimate_result.py)&#93;, [GetMyFeesEstimatesErrorBody](walmart_apis/errors/get_my_fees_estimates_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[FeesEstimateResult](walmart_apis/models/fees_estimate_result.py)&#93;</code> -- Returns fee estimate results for the requested items.

**On `Failure`**: `error` is <code>[GetMyFeesEstimatesErrorBody](walmart_apis/errors/get_my_fees_estimates_error.py)</code>

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
<summary><code>def get_buybox_offer_expected_price_batch(body: GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetBuyboxOfferExpectedPriceBatchResponse, GetBuyboxOfferExpectedPriceBatchErrorBody]</code></summary>

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
result = client.product_pricing.with_raw_response.get_buybox_offer_expected_price_batch(
    GetBuyboxOfferExpectedPriceBatchRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBuyboxOfferExpectedPriceBatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetBuyboxOfferExpectedPriceBatchErrorBody
```

**Async**

```python
result = await async_client.product_pricing.with_raw_response.get_buybox_offer_expected_price_batch(
    GetBuyboxOfferExpectedPriceBatchRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBuyboxOfferExpectedPriceBatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetBuyboxOfferExpectedPriceBatchErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetBuyboxOfferExpectedPriceBatchResponse](walmart_apis/models/get_buybox_offer_expected_price_batch_response.py), [GetBuyboxOfferExpectedPriceBatchErrorBody](walmart_apis/errors/get_buybox_offer_expected_price_batch_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetBuyboxOfferExpectedPriceBatchResponse](walmart_apis/models/get_buybox_offer_expected_price_batch_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetBuyboxOfferExpectedPriceBatchErrorBody](walmart_apis/errors/get_buybox_offer_expected_price_batch_error.py)</code>

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
<summary><code>def get_competitive_pricing(*, item_type: ItemTypeOrStr = ItemType.SKU, skus: list[str] | None = None, walmart_item_ids: list[str] | None = None, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetPricingResponse, GetCompetitivePricingErrorBody]</code></summary>

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
result = client.product_pricing.with_raw_response.get_competitive_pricing(item_type=ItemType.WALMART_ITEM_ID)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPricingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCompetitivePricingErrorBody
```

**Async**

```python
result = await async_client.product_pricing.with_raw_response.get_competitive_pricing(
    item_type=ItemType.WALMART_ITEM_ID
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPricingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCompetitivePricingErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetPricingResponse](walmart_apis/models/get_pricing_response.py), [GetCompetitivePricingErrorBody](walmart_apis/errors/get_competitive_pricing_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetPricingResponse](walmart_apis/models/get_pricing_response.py)</code> -- Returns competitive pricing information for the requested seller items.

**On `Failure`**: `error` is <code>[GetCompetitivePricingErrorBody](walmart_apis/errors/get_competitive_pricing_error.py)</code>

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
<summary><code>def get_competitive_summary(body: CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CompetitiveSummaryBatchResponse, GetCompetitiveSummaryErrorBody]</code></summary>

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
result = client.product_pricing.with_raw_response.get_competitive_summary(CompetitiveSummaryBatchRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompetitiveSummaryBatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCompetitiveSummaryErrorBody
```

**Async**

```python
result = await async_client.product_pricing.with_raw_response.get_competitive_summary(CompetitiveSummaryBatchRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompetitiveSummaryBatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCompetitiveSummaryErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CompetitiveSummaryBatchResponse](walmart_apis/models/competitive_summary_batch_response.py), [GetCompetitiveSummaryErrorBody](walmart_apis/errors/get_competitive_summary_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CompetitiveSummaryBatchResponse](walmart_apis/models/competitive_summary_batch_response.py)</code> -- Returns competitive summary results for the requested Walmart items.

**On `Failure`**: `error` is <code>[GetCompetitiveSummaryErrorBody](walmart_apis/errors/get_competitive_summary_error.py)</code>

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
<summary><code>def get_item_offers(item_id: str, item_condition: ConditionTypeProductPricingOrStr, *, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetOffersResponse, GetItemOffersErrorBody]</code></summary>

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
result = client.product_pricing.with_raw_response.get_item_offers(
    "some example string", ConditionTypeProductPricing.NEW
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOffersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemOffersErrorBody
```

**Async**

```python
result = await async_client.product_pricing.with_raw_response.get_item_offers(
    "some example string", ConditionTypeProductPricing.NEW
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOffersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemOffersErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetOffersResponse](walmart_apis/models/get_offers_response.py), [GetItemOffersErrorBody](walmart_apis/errors/get_item_offers_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetOffersResponse](walmart_apis/models/get_offers_response.py)</code> -- Returns the lowest-priced offers for the requested Walmart item.

**On `Failure`**: `error` is <code>[GetItemOffersErrorBody](walmart_apis/errors/get_item_offers_error.py)</code>

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
<summary><code>def get_item_offers_batch(body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetItemOffersBatchResponse, GetItemOffersBatchErrorBody]</code></summary>

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
result = client.product_pricing.with_raw_response.get_item_offers_batch(GetItemOffersBatchRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetItemOffersBatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemOffersBatchErrorBody
```

**Async**

```python
result = await async_client.product_pricing.with_raw_response.get_item_offers_batch(GetItemOffersBatchRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetItemOffersBatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemOffersBatchErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetItemOffersBatchResponse](walmart_apis/models/get_item_offers_batch_response.py), [GetItemOffersBatchErrorBody](walmart_apis/errors/get_item_offers_batch_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetItemOffersBatchResponse](walmart_apis/models/get_item_offers_batch_response.py)</code> -- Returns the results for the requested Walmart items.

**On `Failure`**: `error` is <code>[GetItemOffersBatchErrorBody](walmart_apis/errors/get_item_offers_batch_error.py)</code>

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
<summary><code>def get_listing_offers(seller_sku: str, item_condition: ConditionTypeProductPricingOrStr, *, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetOffersResponse, GetListingOffersErrorBody]</code></summary>

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
result = client.product_pricing.with_raw_response.get_listing_offers(
    "some example string", ConditionTypeProductPricing.NEW
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOffersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingOffersErrorBody
```

**Async**

```python
result = await async_client.product_pricing.with_raw_response.get_listing_offers(
    "some example string", ConditionTypeProductPricing.NEW
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetOffersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingOffersErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetOffersResponse](walmart_apis/models/get_offers_response.py), [GetListingOffersErrorBody](walmart_apis/errors/get_listing_offers_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetOffersResponse](walmart_apis/models/get_offers_response.py)</code> -- Returns the lowest-priced offers for the requested seller SKU.

**On `Failure`**: `error` is <code>[GetListingOffersErrorBody](walmart_apis/errors/get_listing_offers_error.py)</code>

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
<summary><code>def get_listing_offers_batch(body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetListingOffersBatchResponse, GetListingOffersBatchErrorBody]</code></summary>

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
result = client.product_pricing.with_raw_response.get_listing_offers_batch(GetListingOffersBatchRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetListingOffersBatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingOffersBatchErrorBody
```

**Async**

```python
result = await async_client.product_pricing.with_raw_response.get_listing_offers_batch(GetListingOffersBatchRequest())
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetListingOffersBatchResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListingOffersBatchErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetListingOffersBatchResponse](walmart_apis/models/get_listing_offers_batch_response.py), [GetListingOffersBatchErrorBody](walmart_apis/errors/get_listing_offers_batch_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetListingOffersBatchResponse](walmart_apis/models/get_listing_offers_batch_response.py)</code> -- Returns the results for the requested seller SKUs.

**On `Failure`**: `error` is <code>[GetListingOffersBatchErrorBody](walmart_apis/errors/get_listing_offers_batch_error.py)</code>

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
<summary><code>def get_pricing(*, item_type: ItemTypeOrStr = ItemType.SKU, skus: list[str] | None = None, walmart_item_ids: list[str] | None = None, item_condition: ConditionTypeProductPricingOrStr | None = None, offer_type: OfferCustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetPricingResponse, GetPricingErrorBody]</code></summary>

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
result = client.product_pricing.with_raw_response.get_pricing(item_type=ItemType.WALMART_ITEM_ID)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPricingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPricingErrorBody
```

**Async**

```python
result = await async_client.product_pricing.with_raw_response.get_pricing(item_type=ItemType.WALMART_ITEM_ID)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPricingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPricingErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetPricingResponse](walmart_apis/models/get_pricing_response.py), [GetPricingErrorBody](walmart_apis/errors/get_pricing_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetPricingResponse](walmart_apis/models/get_pricing_response.py)</code> -- Returns pricing information for the requested seller items.

**On `Failure`**: `error` is <code>[GetPricingErrorBody](walmart_apis/errors/get_pricing_error.py)</code>

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
<summary><code>def get_order_metrics(marketplace_ids: list[str], interval: str, granularity: GranularityOrStr, *, granularity_time_zone: str | None = None, buyer_type: BuyerTypeOrStr | None = None, fulfillment_network: str | None = None, first_day_of_week: FirstDayOfWeekOrStr | None = None, asin: str | None = None, sku: str | None = None, sp_api_program: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GetOrderMetricsErrorBody]</code></summary>

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
result = client.sales.with_raw_response.get_order_metrics(
    ["some example string"], "some example string", Granularity.HOUR
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderMetricsErrorBody
```

**Async**

```python
result = await async_client.sales.with_raw_response.get_order_metrics(
    ["some example string"], "some example string", Granularity.HOUR
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetOrderMetricsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [GetOrderMetricsErrorBody](walmart_apis/errors/get_order_metrics_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[GetOrderMetricsErrorBody](walmart_apis/errors/get_order_metrics_error.py)</code>

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
<summary><code>def cancel_shipment2(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelShipmentResponseShipping, CancelShipment2ErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.cancel_shipment2("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelShipmentResponseShipping
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelShipment2ErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.cancel_shipment2("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelShipmentResponseShipping
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelShipment2ErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelShipmentResponseShipping](walmart_apis/models/cancel_shipment_response_shipping.py), [CancelShipment2ErrorBody](walmart_apis/errors/cancel_shipment2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelShipmentResponseShipping](walmart_apis/models/cancel_shipment_response_shipping.py)</code> -- Cancellation processed

**On `Failure`**: `error` is <code>[CancelShipment2ErrorBody](walmart_apis/errors/cancel_shipment2_error.py)</code>

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
<summary><code>def get_access_points(access_point_types: str, country_code: str, postal_code: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetAccessPointsResponse, GetAccessPointsErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.get_access_points(
    "some example string", "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAccessPointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccessPointsErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.get_access_points(
    "some example string", "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAccessPointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccessPointsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetAccessPointsResponse](walmart_apis/models/get_access_points_response.py), [GetAccessPointsErrorBody](walmart_apis/errors/get_access_points_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetAccessPointsResponse](walmart_apis/models/get_access_points_response.py)</code> -- Access points returned successfully

**On `Failure`**: `error` is <code>[GetAccessPointsErrorBody](walmart_apis/errors/get_access_points_error.py)</code>

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
<summary><code>def get_additional_inputs(rate_id: str, request_token: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetAdditionalInputsResponse, GetAdditionalInputsErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.get_additional_inputs("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAdditionalInputsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAdditionalInputsErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.get_additional_inputs(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAdditionalInputsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAdditionalInputsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetAdditionalInputsResponse](walmart_apis/models/get_additional_inputs_response.py), [GetAdditionalInputsErrorBody](walmart_apis/errors/get_additional_inputs_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetAdditionalInputsResponse](walmart_apis/models/get_additional_inputs_response.py)</code> -- JSON Schema for additional inputs returned successfully

**On `Failure`**: `error` is <code>[GetAdditionalInputsErrorBody](walmart_apis/errors/get_additional_inputs_error.py)</code>

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
<summary><code>def get_rates(body: GetRatesRequest | GetRatesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetRatesResponse, GetRatesErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.get_rates(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetRatesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRatesErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.get_rates(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetRatesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetRatesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetRatesResponse](walmart_apis/models/get_rates_response.py), [GetRatesErrorBody](walmart_apis/errors/get_rates_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetRatesResponse](walmart_apis/models/get_rates_response.py)</code> -- Rate quotes returned successfully

**On `Failure`**: `error` is <code>[GetRatesErrorBody](walmart_apis/errors/get_rates_error.py)</code>

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
<summary><code>def get_shipment_documents(shipment_id: str, *, package_client_reference_id: str | None = None, format_: FormatShippingOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetShipmentDocumentsResponse, GetShipmentDocumentsErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.get_shipment_documents("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentDocumentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentDocumentsErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.get_shipment_documents("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentDocumentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentDocumentsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetShipmentDocumentsResponse](walmart_apis/models/get_shipment_documents_response.py), [GetShipmentDocumentsErrorBody](walmart_apis/errors/get_shipment_documents_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetShipmentDocumentsResponse](walmart_apis/models/get_shipment_documents_response.py)</code> -- Documents returned successfully

**On `Failure`**: `error` is <code>[GetShipmentDocumentsErrorBody](walmart_apis/errors/get_shipment_documents_error.py)</code>

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
<summary><code>def get_tracking(tracking_id: str, *, carrier_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetTrackingResponse, GetTrackingErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.get_tracking("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTrackingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackingErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.get_tracking("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTrackingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetTrackingErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetTrackingResponse](walmart_apis/models/get_tracking_response.py), [GetTrackingErrorBody](walmart_apis/errors/get_tracking_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetTrackingResponse](walmart_apis/models/get_tracking_response.py)</code> -- Tracking details returned successfully

**On `Failure`**: `error` is <code>[GetTrackingErrorBody](walmart_apis/errors/get_tracking_error.py)</code>

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
<summary><code>def one_click_shipment(body: OneClickShipmentRequest | OneClickShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[OneClickShipmentResponse, OneClickShipmentErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.one_click_shipment(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OneClickShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OneClickShipmentErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.one_click_shipment(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type OneClickShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type OneClickShipmentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[OneClickShipmentResponse](walmart_apis/models/one_click_shipment_response.py), [OneClickShipmentErrorBody](walmart_apis/errors/one_click_shipment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[OneClickShipmentResponse](walmart_apis/models/one_click_shipment_response.py)</code> -- Shipment purchased successfully

**On `Failure`**: `error` is <code>[OneClickShipmentErrorBody](walmart_apis/errors/one_click_shipment_error.py)</code>

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
<summary><code>def purchase_shipment(body: PurchaseShipmentRequest | PurchaseShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PurchaseShipmentResponse, PurchaseShipmentErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.purchase_shipment(
    PurchaseShipmentRequest(
        request_token="some example string",
        rate_id="some example string",
        requested_document_specification=RequestedDocumentSpecification(
            format=FormatShipping.PDF, size=Size(), dpi=Dpi.VALUE_203
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PurchaseShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PurchaseShipmentErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.purchase_shipment(
    PurchaseShipmentRequest(
        request_token="some example string",
        rate_id="some example string",
        requested_document_specification=RequestedDocumentSpecification(
            format=FormatShipping.PDF, size=Size(), dpi=Dpi.VALUE_203
        ),
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PurchaseShipmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type PurchaseShipmentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[PurchaseShipmentResponse](walmart_apis/models/purchase_shipment_response.py), [PurchaseShipmentErrorBody](walmart_apis/errors/purchase_shipment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[PurchaseShipmentResponse](walmart_apis/models/purchase_shipment_response.py)</code> -- Shipment purchased successfully

**On `Failure`**: `error` is <code>[PurchaseShipmentErrorBody](walmart_apis/errors/purchase_shipment_error.py)</code>

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
<summary><code>def submit_ndr_feedback(body: SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, SubmitNdrFeedbackErrorBody]</code></summary>

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
result = client.shipping.with_raw_response.submit_ndr_feedback(
    SubmitNdrFeedbackRequest(seller_tracking_id="some example string", ndr_action=NdrAction.RETURN_TO_ORIGIN)
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SubmitNdrFeedbackErrorBody
```

**Async**

```python
result = await async_client.shipping.with_raw_response.submit_ndr_feedback(
    SubmitNdrFeedbackRequest(seller_tracking_id="some example string", ndr_action=NdrAction.RETURN_TO_ORIGIN)
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SubmitNdrFeedbackErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;None, [SubmitNdrFeedbackErrorBody](walmart_apis/errors/submit_ndr_feedback_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[SubmitNdrFeedbackErrorBody](walmart_apis/errors/submit_ndr_feedback_error.py)</code>

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
<summary><code>def create_product_review_and_seller_feedback_solicitation(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, CreateProductReviewAndSellerFeedbackSolicitationErrorBody]</code></summary>

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
result = client.solicitations.with_raw_response.create_product_review_and_seller_feedback_solicitation(
    "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateProductReviewAndSellerFeedbackSolicitationErrorBody
```

**Async**

```python
result = await async_client.solicitations.with_raw_response.create_product_review_and_seller_feedback_solicitation(
    "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateProductReviewAndSellerFeedbackSolicitationErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [CreateProductReviewAndSellerFeedbackSolicitationErrorBody](walmart_apis/errors/create_product_review_and_seller_feedback_solicitation_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[CreateProductReviewAndSellerFeedbackSolicitationErrorBody](walmart_apis/errors/create_product_review_and_seller_feedback_solicitation_error.py)</code>

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
<summary><code>def get_solicitation_actions_for_order(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GetSolicitationActionsForOrderErrorBody]</code></summary>

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
result = client.solicitations.with_raw_response.get_solicitation_actions_for_order(
    "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSolicitationActionsForOrderErrorBody
```

**Async**

```python
result = await async_client.solicitations.with_raw_response.get_solicitation_actions_for_order(
    "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSolicitationActionsForOrderErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;Any, [GetSolicitationActionsForOrderErrorBody](walmart_apis/errors/get_solicitation_actions_for_order_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Success

**On `Failure`**: `error` is <code>[GetSolicitationActionsForOrderErrorBody](walmart_apis/errors/get_solicitation_actions_for_order_error.py)</code>

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
<summary><code>def cancel_inbound_plan(plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelInboundPlanResponse, CancelInboundPlanErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.cancel_inbound_plan("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelInboundPlanResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelInboundPlanErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.cancel_inbound_plan("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelInboundPlanResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelInboundPlanErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py), [CancelInboundPlanErrorBody](walmart_apis/errors/cancel_inbound_plan_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelInboundPlanResponse](walmart_apis/models/cancel_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[CancelInboundPlanErrorBody](walmart_apis/errors/cancel_inbound_plan_error.py)</code>

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
<summary><code>def cancel_self_ship_appointment(plan_id: str, shipment_id: str, body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelSelfShipAppointmentResponse, CancelSelfShipAppointmentErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.cancel_self_ship_appointment(
    "some example string", "some example string", CancelSelfShipAppointmentRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelSelfShipAppointmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelSelfShipAppointmentErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.cancel_self_ship_appointment(
    "some example string", "some example string", CancelSelfShipAppointmentRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelSelfShipAppointmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelSelfShipAppointmentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CancelSelfShipAppointmentResponse](walmart_apis/models/cancel_self_ship_appointment_response.py), [CancelSelfShipAppointmentErrorBody](walmart_apis/errors/cancel_self_ship_appointment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelSelfShipAppointmentResponse](walmart_apis/models/cancel_self_ship_appointment_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[CancelSelfShipAppointmentErrorBody](walmart_apis/errors/cancel_self_ship_appointment_error.py)</code>

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
<summary><code>def confirm_delivery_window_options(plan_id: str, shipment_id: str, delivery_window_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConfirmDeliveryWindowOptionsResponse, ConfirmDeliveryWindowOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.confirm_delivery_window_options(
    "some example string", "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmDeliveryWindowOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmDeliveryWindowOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.confirm_delivery_window_options(
    "some example string", "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmDeliveryWindowOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmDeliveryWindowOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ConfirmDeliveryWindowOptionsResponse](walmart_apis/models/confirm_delivery_window_options_response.py), [ConfirmDeliveryWindowOptionsErrorBody](walmart_apis/errors/confirm_delivery_window_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConfirmDeliveryWindowOptionsResponse](walmart_apis/models/confirm_delivery_window_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[ConfirmDeliveryWindowOptionsErrorBody](walmart_apis/errors/confirm_delivery_window_options_error.py)</code>

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
<summary><code>def confirm_packing_option(plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConfirmPackingOptionResponse, ConfirmPackingOptionErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.confirm_packing_option("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmPackingOptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmPackingOptionErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.confirm_packing_option(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmPackingOptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmPackingOptionErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ConfirmPackingOptionResponse](walmart_apis/models/confirm_packing_option_response.py), [ConfirmPackingOptionErrorBody](walmart_apis/errors/confirm_packing_option_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConfirmPackingOptionResponse](walmart_apis/models/confirm_packing_option_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[ConfirmPackingOptionErrorBody](walmart_apis/errors/confirm_packing_option_error.py)</code>

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
<summary><code>def confirm_placement_option(plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConfirmPlacementOptionResponse, ConfirmPlacementOptionErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.confirm_placement_option("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmPlacementOptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmPlacementOptionErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.confirm_placement_option(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmPlacementOptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmPlacementOptionErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ConfirmPlacementOptionResponse](walmart_apis/models/confirm_placement_option_response.py), [ConfirmPlacementOptionErrorBody](walmart_apis/errors/confirm_placement_option_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConfirmPlacementOptionResponse](walmart_apis/models/confirm_placement_option_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[ConfirmPlacementOptionErrorBody](walmart_apis/errors/confirm_placement_option_error.py)</code>

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
<summary><code>def confirm_shipment_content_update_preview(plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConfirmShipmentContentUpdatePreviewResponse, ConfirmShipmentContentUpdatePreviewErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.confirm_shipment_content_update_preview(
    "some example string", "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmShipmentContentUpdatePreviewResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmShipmentContentUpdatePreviewErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.confirm_shipment_content_update_preview(
    "some example string", "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmShipmentContentUpdatePreviewResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmShipmentContentUpdatePreviewErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ConfirmShipmentContentUpdatePreviewResponse](walmart_apis/models/confirm_shipment_content_update_preview_response.py), [ConfirmShipmentContentUpdatePreviewErrorBody](walmart_apis/errors/confirm_shipment_content_update_preview_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConfirmShipmentContentUpdatePreviewResponse](walmart_apis/models/confirm_shipment_content_update_preview_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[ConfirmShipmentContentUpdatePreviewErrorBody](walmart_apis/errors/confirm_shipment_content_update_preview_error.py)</code>

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
<summary><code>def confirm_transportation_options(plan_id: str, body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConfirmTransportationOptionsResponse, ConfirmTransportationOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.confirm_transportation_options(
    "some example string",
    ConfirmTransportationOptionsRequest(
        transportation_selections=[
            CommonTransportationSelection(
                shipment_id="some example string", transportation_option_id="some example string"
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmTransportationOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmTransportationOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.confirm_transportation_options(
    "some example string",
    ConfirmTransportationOptionsRequest(
        transportation_selections=[
            CommonTransportationSelection(
                shipment_id="some example string", transportation_option_id="some example string"
            ),
        ],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConfirmTransportationOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ConfirmTransportationOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ConfirmTransportationOptionsResponse](walmart_apis/models/confirm_transportation_options_response.py), [ConfirmTransportationOptionsErrorBody](walmart_apis/errors/confirm_transportation_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConfirmTransportationOptionsResponse](walmart_apis/models/confirm_transportation_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[ConfirmTransportationOptionsErrorBody](walmart_apis/errors/confirm_transportation_options_error.py)</code>

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
<summary><code>def create_inbound_plan(body: CreateInboundPlanRequest | CreateInboundPlanRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateInboundPlanResponse, CreateInboundPlanErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.create_inbound_plan(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateInboundPlanResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateInboundPlanErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.create_inbound_plan(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateInboundPlanResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateInboundPlanErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateInboundPlanResponse](walmart_apis/models/create_inbound_plan_response.py), [CreateInboundPlanErrorBody](walmart_apis/errors/create_inbound_plan_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateInboundPlanResponse](walmart_apis/models/create_inbound_plan_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[CreateInboundPlanErrorBody](walmart_apis/errors/create_inbound_plan_error.py)</code>

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
<summary><code>def create_marketplace_item_labels(body: CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateMarketplaceItemLabelsResponse, CreateMarketplaceItemLabelsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.create_marketplace_item_labels(
    CreateMarketplaceItemLabelsRequest(
        label_type=CommonLabelPrintType.STANDARD_FORMAT,
        marketplace_id="some example string",
        msku_quantities=[CommonMskuQuantity(msku="some example string", quantity=1)],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateMarketplaceItemLabelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateMarketplaceItemLabelsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.create_marketplace_item_labels(
    CreateMarketplaceItemLabelsRequest(
        label_type=CommonLabelPrintType.STANDARD_FORMAT,
        marketplace_id="some example string",
        msku_quantities=[CommonMskuQuantity(msku="some example string", quantity=1)],
    ),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateMarketplaceItemLabelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateMarketplaceItemLabelsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CreateMarketplaceItemLabelsResponse](walmart_apis/models/create_marketplace_item_labels_response.py), [CreateMarketplaceItemLabelsErrorBody](walmart_apis/errors/create_marketplace_item_labels_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateMarketplaceItemLabelsResponse](walmart_apis/models/create_marketplace_item_labels_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[CreateMarketplaceItemLabelsErrorBody](walmart_apis/errors/create_marketplace_item_labels_error.py)</code>

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
<summary><code>def generate_delivery_window_options(plan_id: str, shipment_id: str, *, scac: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenerateDeliveryWindowOptionsResponse, GenerateDeliveryWindowOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.generate_delivery_window_options(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateDeliveryWindowOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateDeliveryWindowOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.generate_delivery_window_options(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateDeliveryWindowOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateDeliveryWindowOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GenerateDeliveryWindowOptionsResponse](walmart_apis/models/generate_delivery_window_options_response.py), [GenerateDeliveryWindowOptionsErrorBody](walmart_apis/errors/generate_delivery_window_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenerateDeliveryWindowOptionsResponse](walmart_apis/models/generate_delivery_window_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[GenerateDeliveryWindowOptionsErrorBody](walmart_apis/errors/generate_delivery_window_options_error.py)</code>

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
<summary><code>def generate_packing_options(plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GeneratePackingOptionsResponse, GeneratePackingOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.generate_packing_options("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GeneratePackingOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GeneratePackingOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.generate_packing_options("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GeneratePackingOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GeneratePackingOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GeneratePackingOptionsResponse](walmart_apis/models/generate_packing_options_response.py), [GeneratePackingOptionsErrorBody](walmart_apis/errors/generate_packing_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GeneratePackingOptionsResponse](walmart_apis/models/generate_packing_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[GeneratePackingOptionsErrorBody](walmart_apis/errors/generate_packing_options_error.py)</code>

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
<summary><code>def generate_placement_options(plan_id: str, body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GeneratePlacementOptionsResponse, GeneratePlacementOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.generate_placement_options(
    "some example string", GeneratePlacementOptionsRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GeneratePlacementOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GeneratePlacementOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.generate_placement_options(
    "some example string", GeneratePlacementOptionsRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GeneratePlacementOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GeneratePlacementOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GeneratePlacementOptionsResponse](walmart_apis/models/generate_placement_options_response.py), [GeneratePlacementOptionsErrorBody](walmart_apis/errors/generate_placement_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GeneratePlacementOptionsResponse](walmart_apis/models/generate_placement_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[GeneratePlacementOptionsErrorBody](walmart_apis/errors/generate_placement_options_error.py)</code>

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
<summary><code>def generate_self_ship_appointment_slots(plan_id: str, shipment_id: str, body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenerateSelfShipAppointmentSlotsResponse, GenerateSelfShipAppointmentSlotsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.generate_self_ship_appointment_slots(
    "some example string", "some example string", GenerateSelfShipAppointmentSlotsRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateSelfShipAppointmentSlotsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateSelfShipAppointmentSlotsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.generate_self_ship_appointment_slots(
    "some example string", "some example string", GenerateSelfShipAppointmentSlotsRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateSelfShipAppointmentSlotsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateSelfShipAppointmentSlotsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GenerateSelfShipAppointmentSlotsResponse](walmart_apis/models/generate_self_ship_appointment_slots_response.py), [GenerateSelfShipAppointmentSlotsErrorBody](walmart_apis/errors/generate_self_ship_appointment_slots_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenerateSelfShipAppointmentSlotsResponse](walmart_apis/models/generate_self_ship_appointment_slots_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[GenerateSelfShipAppointmentSlotsErrorBody](walmart_apis/errors/generate_self_ship_appointment_slots_error.py)</code>

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
<summary><code>def generate_shipment_content_update_previews(plan_id: str, shipment_id: str, body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenerateShipmentContentUpdatePreviewsResponse, GenerateShipmentContentUpdatePreviewsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.generate_shipment_content_update_previews(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateShipmentContentUpdatePreviewsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateShipmentContentUpdatePreviewsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.generate_shipment_content_update_previews(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateShipmentContentUpdatePreviewsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateShipmentContentUpdatePreviewsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GenerateShipmentContentUpdatePreviewsResponse](walmart_apis/models/generate_shipment_content_update_previews_response.py), [GenerateShipmentContentUpdatePreviewsErrorBody](walmart_apis/errors/generate_shipment_content_update_previews_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenerateShipmentContentUpdatePreviewsResponse](walmart_apis/models/generate_shipment_content_update_previews_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[GenerateShipmentContentUpdatePreviewsErrorBody](walmart_apis/errors/generate_shipment_content_update_previews_error.py)</code>

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
<summary><code>def generate_transportation_options(plan_id: str, body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenerateTransportationOptionsResponse, GenerateTransportationOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.generate_transportation_options(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateTransportationOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateTransportationOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.generate_transportation_options(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateTransportationOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateTransportationOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GenerateTransportationOptionsResponse](walmart_apis/models/generate_transportation_options_response.py), [GenerateTransportationOptionsErrorBody](walmart_apis/errors/generate_transportation_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenerateTransportationOptionsResponse](walmart_apis/models/generate_transportation_options_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[GenerateTransportationOptionsErrorBody](walmart_apis/errors/generate_transportation_options_error.py)</code>

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
<summary><code>def get_bill_of_lading(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetBillOfLadingResponse, GetBillOfLadingErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_bill_of_lading("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBillOfLadingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetBillOfLadingErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_bill_of_lading("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBillOfLadingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetBillOfLadingErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetBillOfLadingResponse](walmart_apis/models/get_bill_of_lading_response.py), [GetBillOfLadingErrorBody](walmart_apis/errors/get_bill_of_lading_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetBillOfLadingResponse](walmart_apis/models/get_bill_of_lading_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetBillOfLadingErrorBody](walmart_apis/errors/get_bill_of_lading_error.py)</code>

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
<summary><code>def get_delivery_challan_document(plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetDeliveryChallanDocumentResponse, GetDeliveryChallanDocumentErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_delivery_challan_document(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetDeliveryChallanDocumentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeliveryChallanDocumentErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_delivery_challan_document(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetDeliveryChallanDocumentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeliveryChallanDocumentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetDeliveryChallanDocumentResponse](walmart_apis/models/get_delivery_challan_document_response.py), [GetDeliveryChallanDocumentErrorBody](walmart_apis/errors/get_delivery_challan_document_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetDeliveryChallanDocumentResponse](walmart_apis/models/get_delivery_challan_document_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetDeliveryChallanDocumentErrorBody](walmart_apis/errors/get_delivery_challan_document_error.py)</code>

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
<summary><code>def get_inbound_operation_status(operation_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommonInboundOperationStatus, GetInboundOperationStatusErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_inbound_operation_status("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommonInboundOperationStatus
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInboundOperationStatusErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_inbound_operation_status("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommonInboundOperationStatus
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInboundOperationStatusErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CommonInboundOperationStatus](walmart_apis/models/common_inbound_operation_status.py), [GetInboundOperationStatusErrorBody](walmart_apis/errors/get_inbound_operation_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommonInboundOperationStatus](walmart_apis/models/common_inbound_operation_status.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetInboundOperationStatusErrorBody](walmart_apis/errors/get_inbound_operation_status_error.py)</code>

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
<summary><code>def get_inbound_plan(plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[InboundPlan, GetInboundPlanErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_inbound_plan("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InboundPlan
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInboundPlanErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_inbound_plan("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type InboundPlan
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetInboundPlanErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[InboundPlan](walmart_apis/models/inbound_plan.py), [GetInboundPlanErrorBody](walmart_apis/errors/get_inbound_plan_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[InboundPlan](walmart_apis/models/inbound_plan.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetInboundPlanErrorBody](walmart_apis/errors/get_inbound_plan_error.py)</code>

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
<summary><code>def get_item_eligibility_preview(item_id: str, program: Program1OrStr, *, marketplace_ids: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetItemEligibilityPreviewResponse, GetItemEligibilityPreviewErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_item_eligibility_preview("some example string", Program1.INBOUND)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetItemEligibilityPreviewResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemEligibilityPreviewErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_item_eligibility_preview(
    "some example string", Program1.INBOUND
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetItemEligibilityPreviewResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetItemEligibilityPreviewErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetItemEligibilityPreviewResponse](walmart_apis/models/get_item_eligibility_preview_response.py), [GetItemEligibilityPreviewErrorBody](walmart_apis/errors/get_item_eligibility_preview_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetItemEligibilityPreviewResponse](walmart_apis/models/get_item_eligibility_preview_response.py)</code> -- Eligibility preview resolved successfully.

**On `Failure`**: `error` is <code>[GetItemEligibilityPreviewErrorBody](walmart_apis/errors/get_item_eligibility_preview_error.py)</code>

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
<summary><code>def get_labels(shipment_id: str, page_type: PageTypeOrStr, label_type: LabelTypeOrStr, *, page_size: int | None = None, page_start_index: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetLabelsResponse, GetLabelsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_labels(
    "some example string", PageType.PACKAGE_LABEL_4X6, LabelType.UNIQUE
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetLabelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLabelsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_labels(
    "some example string", PageType.PACKAGE_LABEL_4X6, LabelType.UNIQUE
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetLabelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLabelsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetLabelsResponse](walmart_apis/models/get_labels_response.py), [GetLabelsErrorBody](walmart_apis/errors/get_labels_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetLabelsResponse](walmart_apis/models/get_labels_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetLabelsErrorBody](walmart_apis/errors/get_labels_error.py)</code>

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
<summary><code>def get_prep_instructions(ship_to_country_code: str, *, seller_sku_list: list[str] | None = None, asin_list: list[str] | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetPrepInstructionsResponse, GetPrepInstructionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_prep_instructions("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPrepInstructionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPrepInstructionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_prep_instructions("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPrepInstructionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetPrepInstructionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetPrepInstructionsResponse](walmart_apis/models/get_prep_instructions_response.py), [GetPrepInstructionsErrorBody](walmart_apis/errors/get_prep_instructions_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetPrepInstructionsResponse](walmart_apis/models/get_prep_instructions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetPrepInstructionsErrorBody](walmart_apis/errors/get_prep_instructions_error.py)</code>

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
<summary><code>def get_self_ship_appointment_slots(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetSelfShipAppointmentSlotsResponse, GetSelfShipAppointmentSlotsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_self_ship_appointment_slots(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetSelfShipAppointmentSlotsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSelfShipAppointmentSlotsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_self_ship_appointment_slots(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetSelfShipAppointmentSlotsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSelfShipAppointmentSlotsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetSelfShipAppointmentSlotsResponse](walmart_apis/models/get_self_ship_appointment_slots_response.py), [GetSelfShipAppointmentSlotsErrorBody](walmart_apis/errors/get_self_ship_appointment_slots_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetSelfShipAppointmentSlotsResponse](walmart_apis/models/get_self_ship_appointment_slots_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetSelfShipAppointmentSlotsErrorBody](walmart_apis/errors/get_self_ship_appointment_slots_error.py)</code>

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
<summary><code>def get_shipment(plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommonShipment, GetShipmentErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_shipment("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommonShipment
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_shipment("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommonShipment
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CommonShipment](walmart_apis/models/common_shipment.py), [GetShipmentErrorBody](walmart_apis/errors/get_shipment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommonShipment](walmart_apis/models/common_shipment.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetShipmentErrorBody](walmart_apis/errors/get_shipment_error.py)</code>

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
<summary><code>def get_shipment_content_update_preview(plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CommonContentUpdatePreview, GetShipmentContentUpdatePreviewErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_shipment_content_update_preview(
    "some example string", "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommonContentUpdatePreview
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentContentUpdatePreviewErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_shipment_content_update_preview(
    "some example string", "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CommonContentUpdatePreview
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentContentUpdatePreviewErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[CommonContentUpdatePreview](walmart_apis/models/common_content_update_preview.py), [GetShipmentContentUpdatePreviewErrorBody](walmart_apis/errors/get_shipment_content_update_preview_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CommonContentUpdatePreview](walmart_apis/models/common_content_update_preview.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetShipmentContentUpdatePreviewErrorBody](walmart_apis/errors/get_shipment_content_update_preview_error.py)</code>

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
<summary><code>def get_shipment_items(*, date_range_filter: DateRangeFilterOrStr | None = None, date_range_value: str | None = None, page_size: int | None = 10, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetShipmentItemsResponse, GetShipmentItemsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_shipment_items()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentItemsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_shipment_items()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentItemsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetShipmentItemsResponse](walmart_apis/models/get_shipment_items_response.py), [GetShipmentItemsErrorBody](walmart_apis/errors/get_shipment_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetShipmentItemsResponse](walmart_apis/models/get_shipment_items_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetShipmentItemsErrorBody](walmart_apis/errors/get_shipment_items_error.py)</code>

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
<summary><code>def get_shipment_items_by_shipment_id(shipment_id: str, *, page_size: int | None = 10, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetShipmentItemsByShipmentIdResponse, GetShipmentItemsByShipmentIdErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_shipment_items_by_shipment_id("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentItemsByShipmentIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentItemsByShipmentIdErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_shipment_items_by_shipment_id("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentItemsByShipmentIdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentItemsByShipmentIdErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetShipmentItemsByShipmentIdResponse](walmart_apis/models/get_shipment_items_by_shipment_id_response.py), [GetShipmentItemsByShipmentIdErrorBody](walmart_apis/errors/get_shipment_items_by_shipment_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetShipmentItemsByShipmentIdResponse](walmart_apis/models/get_shipment_items_by_shipment_id_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetShipmentItemsByShipmentIdErrorBody](walmart_apis/errors/get_shipment_items_by_shipment_id_error.py)</code>

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
<summary><code>def get_shipments(query_type: ShipmentsQueryTypeOrStr, *, shipment_id_list: list[str] | None = None, shipment_status_list: list[ShipmentStatusOrStr] | None = None, last_updated_after: str | None = None, last_updated_before: str | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetShipmentsResponse, GetShipmentsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.get_shipments(ShipmentsQueryType.SHIPMENT)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.get_shipments(ShipmentsQueryType.SHIPMENT)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShipmentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetShipmentsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[GetShipmentsResponse](walmart_apis/models/get_shipments_response.py), [GetShipmentsErrorBody](walmart_apis/errors/get_shipments_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetShipmentsResponse](walmart_apis/models/get_shipments_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[GetShipmentsErrorBody](walmart_apis/errors/get_shipments_error.py)</code>

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
<summary><code>def list_delivery_window_options(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListDeliveryWindowOptionsResponse, ListDeliveryWindowOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_delivery_window_options("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDeliveryWindowOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDeliveryWindowOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_delivery_window_options(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDeliveryWindowOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDeliveryWindowOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListDeliveryWindowOptionsResponse](walmart_apis/models/list_delivery_window_options_response.py), [ListDeliveryWindowOptionsErrorBody](walmart_apis/errors/list_delivery_window_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListDeliveryWindowOptionsResponse](walmart_apis/models/list_delivery_window_options_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListDeliveryWindowOptionsErrorBody](walmart_apis/errors/list_delivery_window_options_error.py)</code>

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
<summary><code>def list_inbound_plan_boxes(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListInboundPlanBoxesResponse, ListInboundPlanBoxesErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_inbound_plan_boxes("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInboundPlanBoxesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListInboundPlanBoxesErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_inbound_plan_boxes("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInboundPlanBoxesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListInboundPlanBoxesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListInboundPlanBoxesResponse](walmart_apis/models/list_inbound_plan_boxes_response.py), [ListInboundPlanBoxesErrorBody](walmart_apis/errors/list_inbound_plan_boxes_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListInboundPlanBoxesResponse](walmart_apis/models/list_inbound_plan_boxes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListInboundPlanBoxesErrorBody](walmart_apis/errors/list_inbound_plan_boxes_error.py)</code>

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
<summary><code>def list_inbound_plan_items(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListInboundPlanItemsResponse, ListInboundPlanItemsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_inbound_plan_items("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInboundPlanItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListInboundPlanItemsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_inbound_plan_items("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInboundPlanItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListInboundPlanItemsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListInboundPlanItemsResponse](walmart_apis/models/list_inbound_plan_items_response.py), [ListInboundPlanItemsErrorBody](walmart_apis/errors/list_inbound_plan_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListInboundPlanItemsResponse](walmart_apis/models/list_inbound_plan_items_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListInboundPlanItemsErrorBody](walmart_apis/errors/list_inbound_plan_items_error.py)</code>

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
<summary><code>def list_inbound_plan_pallets(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListInboundPlanPalletsResponse, ListInboundPlanPalletsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_inbound_plan_pallets("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInboundPlanPalletsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListInboundPlanPalletsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_inbound_plan_pallets("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInboundPlanPalletsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListInboundPlanPalletsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListInboundPlanPalletsResponse](walmart_apis/models/list_inbound_plan_pallets_response.py), [ListInboundPlanPalletsErrorBody](walmart_apis/errors/list_inbound_plan_pallets_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListInboundPlanPalletsResponse](walmart_apis/models/list_inbound_plan_pallets_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListInboundPlanPalletsErrorBody](walmart_apis/errors/list_inbound_plan_pallets_error.py)</code>

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
<summary><code>def list_inbound_plans(*, page_size: int | None = 10, pagination_token: str | None = None, status: str | None = None, sort_by: str | None = None, sort_order: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListInboundPlansResponse, ListInboundPlansErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_inbound_plans()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInboundPlansResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListInboundPlansErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_inbound_plans()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInboundPlansResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListInboundPlansErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListInboundPlansResponse](walmart_apis/models/list_inbound_plans_response.py), [ListInboundPlansErrorBody](walmart_apis/errors/list_inbound_plans_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListInboundPlansResponse](walmart_apis/models/list_inbound_plans_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListInboundPlansErrorBody](walmart_apis/errors/list_inbound_plans_error.py)</code>

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
<summary><code>def list_item_compliance_details(mskus: list[str], marketplace_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListItemComplianceDetailsResponse, ListItemComplianceDetailsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_item_compliance_details(
    ["some example string"], "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListItemComplianceDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListItemComplianceDetailsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_item_compliance_details(
    ["some example string"], "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListItemComplianceDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListItemComplianceDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListItemComplianceDetailsResponse](walmart_apis/models/list_item_compliance_details_response.py), [ListItemComplianceDetailsErrorBody](walmart_apis/errors/list_item_compliance_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListItemComplianceDetailsResponse](walmart_apis/models/list_item_compliance_details_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListItemComplianceDetailsErrorBody](walmart_apis/errors/list_item_compliance_details_error.py)</code>

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
<summary><code>def list_packing_group_boxes(plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPackingGroupBoxesResponse, ListPackingGroupBoxesErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_packing_group_boxes("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPackingGroupBoxesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPackingGroupBoxesErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_packing_group_boxes(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPackingGroupBoxesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPackingGroupBoxesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListPackingGroupBoxesResponse](walmart_apis/models/list_packing_group_boxes_response.py), [ListPackingGroupBoxesErrorBody](walmart_apis/errors/list_packing_group_boxes_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPackingGroupBoxesResponse](walmart_apis/models/list_packing_group_boxes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListPackingGroupBoxesErrorBody](walmart_apis/errors/list_packing_group_boxes_error.py)</code>

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
<summary><code>def list_packing_group_items(plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPackingGroupItemsResponse, ListPackingGroupItemsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_packing_group_items("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPackingGroupItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPackingGroupItemsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_packing_group_items(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPackingGroupItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPackingGroupItemsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListPackingGroupItemsResponse](walmart_apis/models/list_packing_group_items_response.py), [ListPackingGroupItemsErrorBody](walmart_apis/errors/list_packing_group_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPackingGroupItemsResponse](walmart_apis/models/list_packing_group_items_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListPackingGroupItemsErrorBody](walmart_apis/errors/list_packing_group_items_error.py)</code>

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
<summary><code>def list_packing_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPackingOptionsResponse, ListPackingOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_packing_options("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPackingOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPackingOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_packing_options("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPackingOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPackingOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListPackingOptionsResponse](walmart_apis/models/list_packing_options_response.py), [ListPackingOptionsErrorBody](walmart_apis/errors/list_packing_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPackingOptionsResponse](walmart_apis/models/list_packing_options_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListPackingOptionsErrorBody](walmart_apis/errors/list_packing_options_error.py)</code>

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
<summary><code>def list_placement_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPlacementOptionsResponse, ListPlacementOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_placement_options("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPlacementOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPlacementOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_placement_options("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPlacementOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPlacementOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListPlacementOptionsResponse](walmart_apis/models/list_placement_options_response.py), [ListPlacementOptionsErrorBody](walmart_apis/errors/list_placement_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPlacementOptionsResponse](walmart_apis/models/list_placement_options_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListPlacementOptionsErrorBody](walmart_apis/errors/list_placement_options_error.py)</code>

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
<summary><code>def list_prep_details(marketplace_id: str, mskus: list[str], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPrepDetailsResponse, ListPrepDetailsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_prep_details("some example string", ["some example string"])
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPrepDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPrepDetailsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_prep_details(
    "some example string", ["some example string"]
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPrepDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListPrepDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListPrepDetailsResponse](walmart_apis/models/list_prep_details_response.py), [ListPrepDetailsErrorBody](walmart_apis/errors/list_prep_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPrepDetailsResponse](walmart_apis/models/list_prep_details_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListPrepDetailsErrorBody](walmart_apis/errors/list_prep_details_error.py)</code>

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
<summary><code>def list_shipment_boxes(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListShipmentBoxesResponse, ListShipmentBoxesErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_shipment_boxes("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListShipmentBoxesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListShipmentBoxesErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_shipment_boxes(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListShipmentBoxesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListShipmentBoxesErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListShipmentBoxesResponse](walmart_apis/models/list_shipment_boxes_response.py), [ListShipmentBoxesErrorBody](walmart_apis/errors/list_shipment_boxes_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListShipmentBoxesResponse](walmart_apis/models/list_shipment_boxes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListShipmentBoxesErrorBody](walmart_apis/errors/list_shipment_boxes_error.py)</code>

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
<summary><code>def list_shipment_content_update_previews(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListShipmentContentUpdatePreviewsResponse, ListShipmentContentUpdatePreviewsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_shipment_content_update_previews(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListShipmentContentUpdatePreviewsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListShipmentContentUpdatePreviewsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_shipment_content_update_previews(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListShipmentContentUpdatePreviewsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListShipmentContentUpdatePreviewsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListShipmentContentUpdatePreviewsResponse](walmart_apis/models/list_shipment_content_update_previews_response.py), [ListShipmentContentUpdatePreviewsErrorBody](walmart_apis/errors/list_shipment_content_update_previews_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListShipmentContentUpdatePreviewsResponse](walmart_apis/models/list_shipment_content_update_previews_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListShipmentContentUpdatePreviewsErrorBody](walmart_apis/errors/list_shipment_content_update_previews_error.py)</code>

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
<summary><code>def list_shipment_items(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListShipmentItemsResponse, ListShipmentItemsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_shipment_items("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListShipmentItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListShipmentItemsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_shipment_items(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListShipmentItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListShipmentItemsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListShipmentItemsResponse](walmart_apis/models/list_shipment_items_response.py), [ListShipmentItemsErrorBody](walmart_apis/errors/list_shipment_items_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListShipmentItemsResponse](walmart_apis/models/list_shipment_items_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListShipmentItemsErrorBody](walmart_apis/errors/list_shipment_items_error.py)</code>

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
<summary><code>def list_shipment_pallets(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListShipmentPalletsResponse, ListShipmentPalletsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_shipment_pallets("some example string", "some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListShipmentPalletsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListShipmentPalletsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_shipment_pallets(
    "some example string", "some example string"
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListShipmentPalletsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListShipmentPalletsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListShipmentPalletsResponse](walmart_apis/models/list_shipment_pallets_response.py), [ListShipmentPalletsErrorBody](walmart_apis/errors/list_shipment_pallets_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListShipmentPalletsResponse](walmart_apis/models/list_shipment_pallets_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListShipmentPalletsErrorBody](walmart_apis/errors/list_shipment_pallets_error.py)</code>

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
<summary><code>def list_transportation_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, placement_option_id: str | None = None, shipment_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListTransportationOptionsResponse, ListTransportationOptionsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.list_transportation_options("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListTransportationOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListTransportationOptionsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.list_transportation_options("some example string")
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListTransportationOptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListTransportationOptionsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ListTransportationOptionsResponse](walmart_apis/models/list_transportation_options_response.py), [ListTransportationOptionsErrorBody](walmart_apis/errors/list_transportation_options_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListTransportationOptionsResponse](walmart_apis/models/list_transportation_options_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ListTransportationOptionsErrorBody](walmart_apis/errors/list_transportation_options_error.py)</code>

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
<summary><code>def schedule_self_ship_appointment(plan_id: str, shipment_id: str, slot_id: str, body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ScheduleSelfShipAppointmentResponse, ScheduleSelfShipAppointmentErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.schedule_self_ship_appointment(
    "some example string", "some example string", "some example string", ScheduleSelfShipAppointmentRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ScheduleSelfShipAppointmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleSelfShipAppointmentErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.schedule_self_ship_appointment(
    "some example string", "some example string", "some example string", ScheduleSelfShipAppointmentRequest()
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ScheduleSelfShipAppointmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleSelfShipAppointmentErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[ScheduleSelfShipAppointmentResponse](walmart_apis/models/schedule_self_ship_appointment_response.py), [ScheduleSelfShipAppointmentErrorBody](walmart_apis/errors/schedule_self_ship_appointment_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ScheduleSelfShipAppointmentResponse](walmart_apis/models/schedule_self_ship_appointment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[ScheduleSelfShipAppointmentErrorBody](walmart_apis/errors/schedule_self_ship_appointment_error.py)</code>

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
<summary><code>def set_packing_information(plan_id: str, body: SetPackingInformationRequest | SetPackingInformationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SetPackingInformationResponse, SetPackingInformationErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.set_packing_information(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SetPackingInformationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetPackingInformationErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.set_packing_information(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SetPackingInformationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetPackingInformationErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SetPackingInformationResponse](walmart_apis/models/set_packing_information_response.py), [SetPackingInformationErrorBody](walmart_apis/errors/set_packing_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SetPackingInformationResponse](walmart_apis/models/set_packing_information_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[SetPackingInformationErrorBody](walmart_apis/errors/set_packing_information_error.py)</code>

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
<summary><code>def set_prep_details(body: SetPrepDetailsRequest | SetPrepDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SetPrepDetailsResponse, SetPrepDetailsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.set_prep_details(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SetPrepDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetPrepDetailsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.set_prep_details(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SetPrepDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetPrepDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[SetPrepDetailsResponse](walmart_apis/models/set_prep_details_response.py), [SetPrepDetailsErrorBody](walmart_apis/errors/set_prep_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SetPrepDetailsResponse](walmart_apis/models/set_prep_details_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[SetPrepDetailsErrorBody](walmart_apis/errors/set_prep_details_error.py)</code>

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
<summary><code>def update_inbound_plan_name(plan_id: str, body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, UpdateInboundPlanNameErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.update_inbound_plan_name(
    "some example string", UpdateInboundPlanNameRequest(name="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateInboundPlanNameErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.update_inbound_plan_name(
    "some example string", UpdateInboundPlanNameRequest(name="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateInboundPlanNameErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;None, [UpdateInboundPlanNameErrorBody](walmart_apis/errors/update_inbound_plan_name_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[UpdateInboundPlanNameErrorBody](walmart_apis/errors/update_inbound_plan_name_error.py)</code>

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
<summary><code>def update_item_compliance_details(marketplace_id: str, body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateItemComplianceDetailsResponse, UpdateItemComplianceDetailsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.update_item_compliance_details(
    "some example string",
    UpdateItemComplianceDetailsRequest(msku="some example string", tax_details=CommonTaxDetails()),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateItemComplianceDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateItemComplianceDetailsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.update_item_compliance_details(
    "some example string",
    UpdateItemComplianceDetailsRequest(msku="some example string", tax_details=CommonTaxDetails()),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateItemComplianceDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateItemComplianceDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[UpdateItemComplianceDetailsResponse](walmart_apis/models/update_item_compliance_details_response.py), [UpdateItemComplianceDetailsErrorBody](walmart_apis/errors/update_item_compliance_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateItemComplianceDetailsResponse](walmart_apis/models/update_item_compliance_details_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[UpdateItemComplianceDetailsErrorBody](walmart_apis/errors/update_item_compliance_details_error.py)</code>

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
<summary><code>def update_shipment_name(plan_id: str, shipment_id: str, body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, UpdateShipmentNameErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.update_shipment_name(
    "some example string", "some example string", UpdateShipmentNameRequest(name="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateShipmentNameErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.update_shipment_name(
    "some example string", "some example string", UpdateShipmentNameRequest(name="some example string")
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateShipmentNameErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;None, [UpdateShipmentNameErrorBody](walmart_apis/errors/update_shipment_name_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[UpdateShipmentNameErrorBody](walmart_apis/errors/update_shipment_name_error.py)</code>

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
<summary><code>def update_shipment_source_address(plan_id: str, shipment_id: str, body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateShipmentSourceAddressResponse, UpdateShipmentSourceAddressErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.update_shipment_source_address(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateShipmentSourceAddressResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateShipmentSourceAddressErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.update_shipment_source_address(
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
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateShipmentSourceAddressResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateShipmentSourceAddressErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[UpdateShipmentSourceAddressResponse](walmart_apis/models/update_shipment_source_address_response.py), [UpdateShipmentSourceAddressErrorBody](walmart_apis/errors/update_shipment_source_address_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateShipmentSourceAddressResponse](walmart_apis/models/update_shipment_source_address_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[UpdateShipmentSourceAddressErrorBody](walmart_apis/errors/update_shipment_source_address_error.py)</code>

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
<summary><code>def update_shipment_tracking_details(plan_id: str, shipment_id: str, body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateShipmentTrackingDetailsResponse, UpdateShipmentTrackingDetailsErrorBody]</code></summary>

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
result = client.wfs_inbound.with_raw_response.update_shipment_tracking_details(
    "some example string",
    "some example string",
    UpdateShipmentTrackingDetailsRequest(tracking_details=CommonTrackingDetailsInput()),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateShipmentTrackingDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateShipmentTrackingDetailsErrorBody
```

**Async**

```python
result = await async_client.wfs_inbound.with_raw_response.update_shipment_tracking_details(
    "some example string",
    "some example string",
    UpdateShipmentTrackingDetailsRequest(tracking_details=CommonTrackingDetailsInput()),
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateShipmentTrackingDetailsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateShipmentTrackingDetailsErrorBody
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

**Returns**: <code>[ApiResult](walmart_apis/core/results.py)&#91;[UpdateShipmentTrackingDetailsResponse](walmart_apis/models/update_shipment_tracking_details_response.py), [UpdateShipmentTrackingDetailsErrorBody](walmart_apis/errors/update_shipment_tracking_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateShipmentTrackingDetailsResponse](walmart_apis/models/update_shipment_tracking_details_response.py)</code> -- Accepted — operation submitted asynchronously.

**On `Failure`**: `error` is <code>[UpdateShipmentTrackingDetailsErrorBody](walmart_apis/errors/update_shipment_tracking_details_error.py)</code>

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

