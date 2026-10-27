<!-- Generated file — do not edit; regenerated with the SDK. -->

# Catalog — operations

Accessor: `client.catalog` · Source: `walmart_apis/apis/catalog.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.catalog.get_catalog_item

- **Route**: `GET /catalog/v4/items/{walmartItemId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_catalog_item(walmart_item_id: str, marketplace_ids: list[str], *, included_data: list[IncludedDatumOrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `walmart_item_id`, `marketplace_ids`
- **Params**: `walmart_item_id` — path `walmartItemId` · `marketplace_ids` — query `marketplaceIds` · `included_data` — query `includedData`
- **Returns (parsed)**: `Item`
- **Returns (raw)**: `ApiResult[Item, GetCatalogItemErrorBody]`
- **Error**: `GetCatalogItemErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IncludedDatumOrStr` | `walmart_apis/models/enums/included_datum.py` |
| `Item` | `walmart_apis/models/item.py` |
| `GetCatalogItemErrorBody` | `walmart_apis/errors/get_catalog_item_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.catalog.search_catalog_items

- **Route**: `GET /catalog/v4/items`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def search_catalog_items(marketplace_ids: list[str], *, keywords: str | None = None, walmart_item_ids: str | None = None, seller_sku: str | None = None, gtin: str | None = None, upc: str | None = None, included_data: list[IncludedDatumOrStr] | None = None, page_size: int | None = 10, page_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `marketplace_ids`
- **Params**: `marketplace_ids` — query `marketplaceIds` · `keywords` — query · `walmart_item_ids` — query `walmartItemIds` · `seller_sku` — query `sellerSku` · `gtin` — query · `upc` — query · `included_data` — query `includedData` · `page_size` — query `pageSize` · `page_token` — query `pageToken`
- **Returns (parsed)**: `ItemSearchResults`
- **Returns (raw)**: `ApiResult[ItemSearchResults, SearchCatalogItemsErrorBody]`
- **Error**: `SearchCatalogItemsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `IncludedDatumOrStr` | `walmart_apis/models/enums/included_datum.py` |
| `ItemSearchResults` | `walmart_apis/models/item_search_results.py` |
| `SearchCatalogItemsErrorBody` | `walmart_apis/errors/search_catalog_items_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

