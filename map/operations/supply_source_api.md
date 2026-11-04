<!-- Generated file — do not edit; regenerated with the SDK. -->

# SupplySourceApi — operations

Accessor: `client.supply_source_api` · Source: `walmart_apis/apis/supply_source_api.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.supply_source_api.create_supply_source

- **Route**: `POST /v4/fulfillment/shipping-configuration/supply-sources`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def create_supply_source(body: CreateSupplySourceRequest | CreateSupplySourceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateSupplySourceResponse`
- **Returns (raw)**: `ApiResult[CreateSupplySourceResponse, CreateSupplySourceErrorBody]`
- **Error**: `CreateSupplySourceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListShippingManagement` [400, 401, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateSupplySourceRequest` | `walmart_apis/models/create_supply_source_request.py` |
| `CreateSupplySourceRequestDict` | `walmart_apis/models/create_supply_source_request.py` |
| `CreateSupplySourceResponse` | `walmart_apis/models/create_supply_source_response.py` |
| `CreateSupplySourceErrorBody` | `walmart_apis/errors/create_supply_source_error.py` |
| `ErrorListShippingManagement` | `walmart_apis/models/error_list_shipping_management.py` |

### client.supply_source_api.get_supply_source

- **Route**: `GET /v4/fulfillment/shipping-configuration/supply-sources/{supply-source-id}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_supply_source(supply_source_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `supply_source_id`
- **Params**: `supply_source_id` — path `supply-source-id`
- **Returns (parsed)**: `SupplySource`
- **Returns (raw)**: `ApiResult[SupplySource, GetSupplySourceErrorBody]`
- **Error**: `GetSupplySourceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListShippingManagement` [400, 401, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SupplySource` | `walmart_apis/models/supply_source.py` |
| `GetSupplySourceErrorBody` | `walmart_apis/errors/get_supply_source_error.py` |
| `ErrorListShippingManagement` | `walmart_apis/models/error_list_shipping_management.py` |

### client.supply_source_api.list_supply_sources

- **Route**: `GET /v4/fulfillment/shipping-configuration/supply-sources`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_supply_sources(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `list[SupplySource]`
- **Returns (raw)**: `ApiResult[list[SupplySource], ListSupplySourcesErrorBody]`
- **Error**: `ListSupplySourcesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListShippingManagement` [400, 401, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SupplySource` | `walmart_apis/models/supply_source.py` |
| `ListSupplySourcesErrorBody` | `walmart_apis/errors/list_supply_sources_error.py` |
| `ErrorListShippingManagement` | `walmart_apis/models/error_list_shipping_management.py` |

### client.supply_source_api.update_supply_source

- **Route**: `PUT /v4/fulfillment/shipping-configuration/supply-sources/{supply-source-id}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def update_supply_source(supply_source_id: str, body: UpdateSupplySourceRequest | UpdateSupplySourceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `supply_source_id`, `body`
- **Params**: `supply_source_id` — path `supply-source-id` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UpdateSupplySourceErrorBody]`
- **Error**: `UpdateSupplySourceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorListShippingManagement` [400, 401, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateSupplySourceRequest` | `walmart_apis/models/update_supply_source_request.py` |
| `UpdateSupplySourceRequestDict` | `walmart_apis/models/update_supply_source_request.py` |
| `UpdateSupplySourceErrorBody` | `walmart_apis/errors/update_supply_source_error.py` |
| `ErrorListShippingManagement` | `walmart_apis/models/error_list_shipping_management.py` |

