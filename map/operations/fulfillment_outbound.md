<!-- Generated file — do not edit; regenerated with the SDK. -->

# FulfillmentOutbound — operations

Accessor: `client.fulfillment_outbound` · Source: `walmart_apis/apis/fulfillment_outbound.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.fulfillment_outbound.cancel_fulfillment_order

- **Route**: `PUT /wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_fulfillment_order(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_fulfillment_order_id`
- **Params**: `seller_fulfillment_order_id` — path `sellerFulfillmentOrderId`
- **Returns (parsed)**: `CancelFulfillmentOrderResponse`
- **Returns (raw)**: `ApiResult[CancelFulfillmentOrderResponse, CancelFulfillmentOrderErrorBody]`
- **Error**: `CancelFulfillmentOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelFulfillmentOrderResponse` | `walmart_apis/models/cancel_fulfillment_order_response.py` |
| `CancelFulfillmentOrderErrorBody` | `walmart_apis/errors/cancel_fulfillment_order_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.fulfillment_outbound.create_fulfillment_order

- **Route**: `POST /wfs/outbound/v4/fulfillmentOrders`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_fulfillment_order(body: CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateFulfillmentOrderResponse`
- **Returns (raw)**: `ApiResult[CreateFulfillmentOrderResponse, CreateFulfillmentOrderErrorBody]`
- **Error**: `CreateFulfillmentOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateFulfillmentOrderRequest` | `walmart_apis/models/create_fulfillment_order_request.py` |
| `CreateFulfillmentOrderRequestDict` | `walmart_apis/models/create_fulfillment_order_request.py` |
| `CreateFulfillmentOrderResponse` | `walmart_apis/models/create_fulfillment_order_response.py` |
| `CreateFulfillmentOrderErrorBody` | `walmart_apis/errors/create_fulfillment_order_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.fulfillment_outbound.get_fulfillment_order

- **Route**: `GET /wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_fulfillment_order(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_fulfillment_order_id`
- **Params**: `seller_fulfillment_order_id` — path `sellerFulfillmentOrderId`
- **Returns (parsed)**: `GetFulfillmentOrderResponse`
- **Returns (raw)**: `ApiResult[GetFulfillmentOrderResponse, GetFulfillmentOrderErrorBody]`
- **Error**: `GetFulfillmentOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetFulfillmentOrderResponse` | `walmart_apis/models/get_fulfillment_order_response.py` |
| `GetFulfillmentOrderErrorBody` | `walmart_apis/errors/get_fulfillment_order_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.fulfillment_outbound.get_fulfillment_order_shipments

- **Route**: `GET /wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}/shipments`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_fulfillment_order_shipments(seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_fulfillment_order_id`
- **Params**: `seller_fulfillment_order_id` — path `sellerFulfillmentOrderId`
- **Returns (parsed)**: `GetFulfillmentOrderShipmentsResponse`
- **Returns (raw)**: `ApiResult[GetFulfillmentOrderShipmentsResponse, GetFulfillmentOrderShipmentsErrorBody]`
- **Error**: `GetFulfillmentOrderShipmentsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetFulfillmentOrderShipmentsResponse` | `walmart_apis/models/get_fulfillment_order_shipments_response.py` |
| `GetFulfillmentOrderShipmentsErrorBody` | `walmart_apis/errors/get_fulfillment_order_shipments_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.fulfillment_outbound.get_fulfillment_preview

- **Route**: `POST /wfs/outbound/v4/fulfillmentOrders/preview`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_fulfillment_preview(body: GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetFulfillmentPreviewResponse`
- **Returns (raw)**: `ApiResult[GetFulfillmentPreviewResponse, GetFulfillmentPreviewErrorBody]`
- **Error**: `GetFulfillmentPreviewErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetFulfillmentPreviewRequest` | `walmart_apis/models/get_fulfillment_preview_request.py` |
| `GetFulfillmentPreviewRequestDict` | `walmart_apis/models/get_fulfillment_preview_request.py` |
| `GetFulfillmentPreviewResponse` | `walmart_apis/models/get_fulfillment_preview_response.py` |
| `GetFulfillmentPreviewErrorBody` | `walmart_apis/errors/get_fulfillment_preview_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.fulfillment_outbound.list_all_fulfillment_orders

- **Route**: `GET /wfs/outbound/v4/fulfillmentOrders`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_all_fulfillment_orders(*, query_start_date: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `query_start_date` — query `queryStartDate` · `next_token` — query `nextToken`
- **Returns (parsed)**: `ListAllFulfillmentOrdersResponse`
- **Returns (raw)**: `ApiResult[ListAllFulfillmentOrdersResponse, ListAllFulfillmentOrdersErrorBody]`
- **Error**: `ListAllFulfillmentOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListAllFulfillmentOrdersResponse` | `walmart_apis/models/list_all_fulfillment_orders_response.py` |
| `ListAllFulfillmentOrdersErrorBody` | `walmart_apis/errors/list_all_fulfillment_orders_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.fulfillment_outbound.update_fulfillment_order

- **Route**: `PUT /wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_fulfillment_order(seller_fulfillment_order_id: str, body: UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_fulfillment_order_id`, `body`
- **Params**: `seller_fulfillment_order_id` — path `sellerFulfillmentOrderId` · `body` — JSON body
- **Returns (parsed)**: `UpdateFulfillmentOrderResponse`
- **Returns (raw)**: `ApiResult[UpdateFulfillmentOrderResponse, UpdateFulfillmentOrderErrorBody]`
- **Error**: `UpdateFulfillmentOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateFulfillmentOrderRequest` | `walmart_apis/models/update_fulfillment_order_request.py` |
| `UpdateFulfillmentOrderRequestDict` | `walmart_apis/models/update_fulfillment_order_request.py` |
| `UpdateFulfillmentOrderResponse` | `walmart_apis/models/update_fulfillment_order_response.py` |
| `UpdateFulfillmentOrderErrorBody` | `walmart_apis/errors/update_fulfillment_order_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

