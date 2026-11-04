<!-- Generated file — do not edit; regenerated with the SDK. -->

# ListingsItems — operations

Accessor: `client.listings_items` · Source: `walmart_apis/apis/listings_items.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.listings_items.delete_listings_item

- **Route**: `DELETE /v4/items/listings/{seller-id}/{sku}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def delete_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_id`, `sku`, `marketplace_ids`
- **Params**: `seller_id` — path `seller-id` · `sku` — path · `marketplace_ids` — query `marketplaceIds` · `issue_locale` — query `issueLocale`
- **Returns (parsed)**: `ListingsItemSubmissionResponse`
- **Returns (raw)**: `ApiResult[ListingsItemSubmissionResponse, DeleteListingsItemErrorBody]`
- **Error**: `DeleteListingsItemErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListingsItemSubmissionResponse` | `walmart_apis/models/listings_item_submission_response.py` |
| `DeleteListingsItemErrorBody` | `walmart_apis/errors/delete_listings_item_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.listings_items.get_listings_item

- **Route**: `GET /v4/items/listings/{seller-id}/{sku}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], *, issue_locale: str | None = "en_US", included_data: list[IncludedDatumListingsItemsOrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_id`, `sku`, `marketplace_ids`
- **Params**: `seller_id` — path `seller-id` · `sku` — path · `marketplace_ids` — query `marketplaceIds` · `issue_locale` — query `issueLocale` · `included_data` — query `includedData`
- **Returns (parsed)**: `ItemListingsItems`
- **Returns (raw)**: `ApiResult[ItemListingsItems, GetListingsItemErrorBody]`
- **Error**: `GetListingsItemErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IncludedDatumListingsItemsOrStr` | `walmart_apis/models/enums/included_datum_listings_items.py` |
| `ItemListingsItems` | `walmart_apis/models/item_listings_items.py` |
| `GetListingsItemErrorBody` | `walmart_apis/errors/get_listings_item_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.listings_items.patch_listings_item

- **Route**: `PATCH /v4/items/listings/{seller-id}/{sku}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def patch_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], body: ListingsItemPatchRequest | ListingsItemPatchRequestDict, *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_id`, `sku`, `marketplace_ids`, `body`
- **Params**: `seller_id` — path `seller-id` · `sku` — path · `marketplace_ids` — query `marketplaceIds` · `issue_locale` — query `issueLocale` · `body` — JSON body
- **Returns (parsed)**: `ListingsItemSubmissionResponse`
- **Returns (raw)**: `ApiResult[ListingsItemSubmissionResponse, PatchListingsItemErrorBody]`
- **Error**: `PatchListingsItemErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListingsItemPatchRequest` | `walmart_apis/models/listings_item_patch_request.py` |
| `ListingsItemPatchRequestDict` | `walmart_apis/models/listings_item_patch_request.py` |
| `ListingsItemSubmissionResponse` | `walmart_apis/models/listings_item_submission_response.py` |
| `PatchListingsItemErrorBody` | `walmart_apis/errors/patch_listings_item_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.listings_items.put_listings_item

- **Route**: `PUT /v4/items/listings/{seller-id}/{sku}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def put_listings_item(seller_id: str, sku: str, marketplace_ids: list[str], body: ListingsItemPutRequest | ListingsItemPutRequestDict, *, issue_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_id`, `sku`, `marketplace_ids`, `body`
- **Params**: `seller_id` — path `seller-id` · `sku` — path · `marketplace_ids` — query `marketplaceIds` · `issue_locale` — query `issueLocale` · `body` — JSON body
- **Returns (parsed)**: `ListingsItemSubmissionResponse`
- **Returns (raw)**: `ApiResult[ListingsItemSubmissionResponse, PutListingsItemErrorBody]`
- **Error**: `PutListingsItemErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListingsItemPutRequest` | `walmart_apis/models/listings_item_put_request.py` |
| `ListingsItemPutRequestDict` | `walmart_apis/models/listings_item_put_request.py` |
| `ListingsItemSubmissionResponse` | `walmart_apis/models/listings_item_submission_response.py` |
| `PutListingsItemErrorBody` | `walmart_apis/errors/put_listings_item_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.listings_items.search_listings_items

- **Route**: `GET /v4/items/listings/{seller-id}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def search_listings_items(seller_id: str, marketplace_ids: list[str], *, included_data: list[IncludedDatumListingsItemsOrStr] | None = None, identifier_type: IdentifierTypeListingsItemsOrStr | None = None, identifier_value: str | None = None, lifecycle_status: list[str] | None = None, published_status: list[str] | None = None, unpublished_reasons: list[str] | None = None, inventory_status: list[str] | None = None, fulfillment_type: list[str] | None = None, min_customer_rating: float | None = None, max_customer_rating: float | None = None, min_price: float | None = None, max_price: float | None = None, sort_by: SortByOrStr | None = None, sort_order: SortOrderOrStr | None = SortOrder.ASC, page_size: int | None = 10, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_id`, `marketplace_ids`
- **Params**: `seller_id` — path `seller-id` · `marketplace_ids` — query `marketplaceIds` · `included_data` — query `includedData` · `identifier_type` — query `identifierType` · `identifier_value` — query `identifierValue` · `lifecycle_status` — query `lifecycleStatus` · `published_status` — query `publishedStatus` · `unpublished_reasons` — query `unpublishedReasons` · `inventory_status` — query `inventoryStatus` · `fulfillment_type` — query `fulfillmentType` · `min_customer_rating` — query `minCustomerRating` · `max_customer_rating` — query `maxCustomerRating` · `min_price` — query `minPrice` · `max_price` — query `maxPrice` · `sort_by` — query `sortBy` · `sort_order` — query `sortOrder` · `page_size` — query `pageSize` · `page_token` — query `pageToken`
- **Returns (parsed)**: `ItemSearchResultsListingsItems`
- **Returns (raw)**: `ApiResult[ItemSearchResultsListingsItems, SearchListingsItemsErrorBody]`
- **Error**: `SearchListingsItemsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IncludedDatumListingsItemsOrStr` | `walmart_apis/models/enums/included_datum_listings_items.py` |
| `IdentifierTypeListingsItemsOrStr` | `walmart_apis/models/enums/identifier_type_listings_items.py` |
| `SortByOrStr` | `walmart_apis/models/enums/sort_by.py` |
| `SortOrderOrStr` | `walmart_apis/models/enums/sort_order.py` |
| `ItemSearchResultsListingsItems` | `walmart_apis/models/item_search_results_listings_items.py` |
| `SearchListingsItemsErrorBody` | `walmart_apis/errors/search_listings_items_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

