<!-- Generated file — do not edit; regenerated with the SDK. -->

# Inventory — operations

Accessor: `client.inventory` · Source: `walmart_apis/apis/inventory.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.inventory.bulk_update_inventory

- **Route**: `POST /inventory/v4/items/bulk`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def bulk_update_inventory(body: BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpdateInventoryResponse`
- **Returns (raw)**: `ApiResult[BulkUpdateInventoryResponse, BulkUpdateInventoryErrorBody]`
- **Error**: `BulkUpdateInventoryErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `BulkUpdateInventoryRequest` | `walmart_apis/models/bulk_update_inventory_request.py` |
| `BulkUpdateInventoryRequestDict` | `walmart_apis/models/bulk_update_inventory_request.py` |
| `BulkUpdateInventoryResponse` | `walmart_apis/models/bulk_update_inventory_response.py` |
| `BulkUpdateInventoryErrorBody` | `walmart_apis/errors/bulk_update_inventory_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.inventory.get_inventory_for_sku

- **Route**: `GET /inventory/v4/items/{sku}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_inventory_for_sku(sku: str, *, ship_node: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sku`
- **Params**: `sku` — path · `ship_node` — query `shipNode`
- **Returns (parsed)**: `InventorySummary`
- **Returns (raw)**: `ApiResult[InventorySummary, GetInventoryForSkuErrorBody]`
- **Error**: `GetInventoryForSkuErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InventorySummary` | `walmart_apis/models/inventory_summary.py` |
| `GetInventoryForSkuErrorBody` | `walmart_apis/errors/get_inventory_for_sku_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.inventory.get_inventory_summaries

- **Route**: `GET /inventory/v4/items`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_inventory_summaries(*, skus: str | None = None, ship_node: str | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `skus` — query · `ship_node` — query `shipNode` · `page_size` — query `pageSize` · `next_token` — query `nextToken`
- **Returns (parsed)**: `GetInventorySummariesResponse`
- **Returns (raw)**: `ApiResult[GetInventorySummariesResponse, GetInventorySummariesErrorBody]`
- **Error**: `GetInventorySummariesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetInventorySummariesResponse` | `walmart_apis/models/get_inventory_summaries_response.py` |
| `GetInventorySummariesErrorBody` | `walmart_apis/errors/get_inventory_summaries_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.inventory.update_inventory_for_sku

- **Route**: `PUT /inventory/v4/items/{sku}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_inventory_for_sku(sku: str, body: UpdateInventoryRequest | UpdateInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sku`, `body`
- **Params**: `sku` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateInventoryResponse`
- **Returns (raw)**: `ApiResult[UpdateInventoryResponse, UpdateInventoryForSkuErrorBody]`
- **Error**: `UpdateInventoryForSkuErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateInventoryRequest` | `walmart_apis/models/update_inventory_request.py` |
| `UpdateInventoryRequestDict` | `walmart_apis/models/update_inventory_request.py` |
| `UpdateInventoryResponse` | `walmart_apis/models/update_inventory_response.py` |
| `UpdateInventoryForSkuErrorBody` | `walmart_apis/errors/update_inventory_for_sku_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

