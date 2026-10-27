<!-- Generated file — do not edit; regenerated with the SDK. -->

# WfsInventory — operations

Accessor: `client.wfs_inventory` · Source: `walmart_apis/apis/wfs_inventory.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wfs_inventory.get_wfs_inventory_items

- **Route**: `GET /inventory/v4/wfs/items`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_wfs_inventory_items(*, skus: str | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `skus` — query · `page_size` — query `pageSize` · `next_token` — query `nextToken`
- **Returns (parsed)**: `GetWfsInventoryResponse`
- **Returns (raw)**: `ApiResult[GetWfsInventoryResponse, GetWfsInventoryItemsErrorBody]`
- **Error**: `GetWfsInventoryItemsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetWfsInventoryResponse` | `walmart_apis/models/get_wfs_inventory_response.py` |
| `GetWfsInventoryItemsErrorBody` | `walmart_apis/errors/get_wfs_inventory_items_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

