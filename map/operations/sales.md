<!-- Generated file — do not edit; regenerated with the SDK. -->

# Sales — operations

Accessor: `client.sales` · Source: `walmart_apis/apis/sales.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sales.get_order_metrics

- **Route**: `GET /sales/v4/orderMetrics`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_order_metrics(marketplace_ids: list[str], interval: str, granularity: GranularityOrStr, *, granularity_time_zone: str | None = None, buyer_type: BuyerTypeOrStr | None = None, fulfillment_network: str | None = None, first_day_of_week: FirstDayOfWeekOrStr | None = None, asin: str | None = None, sku: str | None = None, sp_api_program: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `marketplace_ids`, `interval`, `granularity`
- **Params**: `marketplace_ids` — query `marketplaceIds` · `interval` — query · `granularity` — query · `granularity_time_zone` — query `granularityTimeZone` · `buyer_type` — query `buyerType` · `fulfillment_network` — query `fulfillmentNetwork` · `first_day_of_week` — query `firstDayOfWeek` · `asin` — query · `sku` — query · `sp_api_program` — query `sp-apiProgram`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GetOrderMetricsErrorBody]`
- **Error**: `GetOrderMetricsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GranularityOrStr` | `walmart_apis/models/enums/granularity.py` |
| `BuyerTypeOrStr` | `walmart_apis/models/enums/buyer_type.py` |
| `FirstDayOfWeekOrStr` | `walmart_apis/models/enums/first_day_of_week.py` |
| `GetOrderMetricsErrorBody` | `walmart_apis/errors/get_order_metrics_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

