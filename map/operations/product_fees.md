<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductFees — operations

Accessor: `client.product_fees` · Source: `walmart_apis/apis/product_fees.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.product_fees.get_my_fees_estimate_for_item

- **Route**: `POST /products/fees/v4/items/{WalmartItemId}/feesEstimate`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_my_fees_estimate_for_item(walmart_item_id: str, body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `walmart_item_id`, `body`
- **Params**: `walmart_item_id` — path `WalmartItemId` · `body` — JSON body
- **Returns (parsed)**: `GetMyFeesEstimateResponse`
- **Returns (raw)**: `ApiResult[GetMyFeesEstimateResponse, GetMyFeesEstimateForItemErrorBody]`
- **Error**: `GetMyFeesEstimateForItemErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetMyFeesEstimateRequest` | `walmart_apis/models/get_my_fees_estimate_request.py` |
| `GetMyFeesEstimateRequestDict` | `walmart_apis/models/get_my_fees_estimate_request.py` |
| `GetMyFeesEstimateResponse` | `walmart_apis/models/get_my_fees_estimate_response.py` |
| `GetMyFeesEstimateForItemErrorBody` | `walmart_apis/errors/get_my_fees_estimate_for_item_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.product_fees.get_my_fees_estimate_for_sku

- **Route**: `POST /products/fees/v4/listings/{SellerSKU}/feesEstimate`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_my_fees_estimate_for_sku(seller_sku: str, marketplace_id: str, body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_sku`, `marketplace_id`, `body`
- **Params**: `seller_sku` — path `SellerSKU` · `marketplace_id` — query `MarketplaceId` · `body` — JSON body
- **Returns (parsed)**: `GetMyFeesEstimateResponse`
- **Returns (raw)**: `ApiResult[GetMyFeesEstimateResponse, GetMyFeesEstimateForSkuErrorBody]`
- **Error**: `GetMyFeesEstimateForSkuErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetMyFeesEstimateRequest` | `walmart_apis/models/get_my_fees_estimate_request.py` |
| `GetMyFeesEstimateRequestDict` | `walmart_apis/models/get_my_fees_estimate_request.py` |
| `GetMyFeesEstimateResponse` | `walmart_apis/models/get_my_fees_estimate_response.py` |
| `GetMyFeesEstimateForSkuErrorBody` | `walmart_apis/errors/get_my_fees_estimate_for_sku_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.product_fees.get_my_fees_estimates

- **Route**: `POST /products/fees/v4/feesEstimate`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_my_fees_estimates(body: list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[FeesEstimateResult]`
- **Returns (raw)**: `ApiResult[list[FeesEstimateResult], GetMyFeesEstimatesErrorBody]`
- **Error**: `GetMyFeesEstimatesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FeesEstimateByIdRequest` | `walmart_apis/models/fees_estimate_by_id_request.py` |
| `FeesEstimateByIdRequestDict` | `walmart_apis/models/fees_estimate_by_id_request.py` |
| `FeesEstimateResult` | `walmart_apis/models/fees_estimate_result.py` |
| `GetMyFeesEstimatesErrorBody` | `walmart_apis/errors/get_my_fees_estimates_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

