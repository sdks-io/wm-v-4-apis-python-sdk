<!-- Generated file — do not edit; regenerated with the SDK. -->

# Orders — operations

Accessor: `client.orders` · Source: `walmart_apis/apis/orders.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.orders.acknowledge_order

- **Route**: `POST /orders/v4/orders/{purchaseOrderId}/acknowledge`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def acknowledge_order(purchase_order_id: str, body: AcknowledgeOrderRequest | AcknowledgeOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `body`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `body` — JSON body
- **Returns (parsed)**: `AcknowledgeOrderResponse`
- **Returns (raw)**: `ApiResult[AcknowledgeOrderResponse, AcknowledgeOrderErrorBody]`
- **Error**: `AcknowledgeOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AcknowledgeOrderRequest` | `walmart_apis/models/acknowledge_order_request.py` |
| `AcknowledgeOrderRequestDict` | `walmart_apis/models/acknowledge_order_request.py` |
| `AcknowledgeOrderResponse` | `walmart_apis/models/acknowledge_order_response.py` |
| `AcknowledgeOrderErrorBody` | `walmart_apis/errors/acknowledge_order_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.cancel_order_lines

- **Route**: `POST /orders/v4/orders/{purchaseOrderId}/cancel`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_order_lines(purchase_order_id: str, body: CancelOrderLinesRequest | CancelOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `body`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `body` — JSON body
- **Returns (parsed)**: `CancelOrderLinesResponse`
- **Returns (raw)**: `ApiResult[CancelOrderLinesResponse, CancelOrderLinesErrorBody]`
- **Error**: `CancelOrderLinesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelOrderLinesRequest` | `walmart_apis/models/cancel_order_lines_request.py` |
| `CancelOrderLinesRequestDict` | `walmart_apis/models/cancel_order_lines_request.py` |
| `CancelOrderLinesResponse` | `walmart_apis/models/cancel_order_lines_response.py` |
| `CancelOrderLinesErrorBody` | `walmart_apis/errors/cancel_order_lines_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.deliver_order_lines

- **Route**: `POST /orders/v4/orders/{purchaseOrderId}/deliver`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def deliver_order_lines(purchase_order_id: str, body: DeliverOrderLinesRequest | DeliverOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `body`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `body` — JSON body
- **Returns (parsed)**: `DeliverOrderLinesResponse`
- **Returns (raw)**: `ApiResult[DeliverOrderLinesResponse, DeliverOrderLinesErrorBody]`
- **Error**: `DeliverOrderLinesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeliverOrderLinesRequest` | `walmart_apis/models/deliver_order_lines_request.py` |
| `DeliverOrderLinesRequestDict` | `walmart_apis/models/deliver_order_lines_request.py` |
| `DeliverOrderLinesResponse` | `walmart_apis/models/deliver_order_lines_response.py` |
| `DeliverOrderLinesErrorBody` | `walmart_apis/errors/deliver_order_lines_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.get_order

- **Route**: `GET /orders/v4/orders/{purchaseOrderId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_order(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`
- **Params**: `purchase_order_id` — path `purchaseOrderId`
- **Returns (parsed)**: `GetOrderResponse`
- **Returns (raw)**: `ApiResult[GetOrderResponse, GetOrderErrorBody]`
- **Error**: `GetOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetOrderResponse` | `walmart_apis/models/get_order_response.py` |
| `GetOrderErrorBody` | `walmart_apis/errors/get_order_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.get_order_address

- **Route**: `GET /orders/v4/orders/{purchaseOrderId}/address`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_order_address(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`
- **Params**: `purchase_order_id` — path `purchaseOrderId`
- **Returns (parsed)**: `GetOrderAddressResponse`
- **Returns (raw)**: `ApiResult[GetOrderAddressResponse, GetOrderAddressErrorBody]`
- **Error**: `GetOrderAddressErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetOrderAddressResponse` | `walmart_apis/models/get_order_address_response.py` |
| `GetOrderAddressErrorBody` | `walmart_apis/errors/get_order_address_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.get_order_buyer_info

- **Route**: `GET /orders/v4/orders/{purchaseOrderId}/buyerInfo`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_order_buyer_info(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`
- **Params**: `purchase_order_id` — path `purchaseOrderId`
- **Returns (parsed)**: `GetOrderBuyerInfoResponse`
- **Returns (raw)**: `ApiResult[GetOrderBuyerInfoResponse, GetOrderBuyerInfoErrorBody]`
- **Error**: `GetOrderBuyerInfoErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetOrderBuyerInfoResponse` | `walmart_apis/models/get_order_buyer_info_response.py` |
| `GetOrderBuyerInfoErrorBody` | `walmart_apis/errors/get_order_buyer_info_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.get_order_items

- **Route**: `GET /orders/v4/orders/{purchaseOrderId}/items`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_order_items(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`
- **Params**: `purchase_order_id` — path `purchaseOrderId`
- **Returns (parsed)**: `GetFulfillmentOrderShipmentsResponse`
- **Returns (raw)**: `ApiResult[GetFulfillmentOrderShipmentsResponse, GetOrderItemsErrorBody]`
- **Error**: `GetOrderItemsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetFulfillmentOrderShipmentsResponse` | `walmart_apis/models/get_fulfillment_order_shipments_response.py` |
| `GetOrderItemsErrorBody` | `walmart_apis/errors/get_order_items_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.get_order_regulated_info

- **Route**: `GET /orders/v4/orders/{purchaseOrderId}/regulatedInfo`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_order_regulated_info(purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`
- **Params**: `purchase_order_id` — path `purchaseOrderId`
- **Returns (parsed)**: `GetOrderRegulatedInfoResponse`
- **Returns (raw)**: `ApiResult[GetOrderRegulatedInfoResponse, GetOrderRegulatedInfoErrorBody]`
- **Error**: `GetOrderRegulatedInfoErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetOrderRegulatedInfoResponse` | `walmart_apis/models/get_order_regulated_info_response.py` |
| `GetOrderRegulatedInfoErrorBody` | `walmart_apis/errors/get_order_regulated_info_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.get_orders

- **Route**: `GET /orders/v4/orders`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_orders(*, created_after: RFC3339DateTime | None = None, created_before: RFC3339DateTime | None = None, last_updated_after: RFC3339DateTime | None = None, order_statuses: list[OrderStatusOrStr] | None = None, fulfillment_types: list[FulfillmentTypeOrStr] | None = None, page_size: int | None = 100, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `created_after` — query `createdAfter` · `created_before` — query `createdBefore` · `last_updated_after` — query `lastUpdatedAfter` · `order_statuses` — query `orderStatuses` · `fulfillment_types` — query `fulfillmentTypes` · `page_size` — query `pageSize` · `next_token` — query `nextToken`
- **Returns (parsed)**: `GetFulfillmentOrderResponse`
- **Returns (raw)**: `ApiResult[GetFulfillmentOrderResponse, GetOrdersErrorBody]`
- **Error**: `GetOrdersErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OrderStatusOrStr` | `walmart_apis/models/enums/order_status.py` |
| `FulfillmentTypeOrStr` | `walmart_apis/models/enums/fulfillment_type.py` |
| `GetFulfillmentOrderResponse` | `walmart_apis/models/get_fulfillment_order_response.py` |
| `GetOrdersErrorBody` | `walmart_apis/errors/get_orders_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.refund_order_lines

- **Route**: `POST /orders/v4/orders/{purchaseOrderId}/refund`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def refund_order_lines(purchase_order_id: str, body: RefundOrderLinesRequest | RefundOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `body`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `body` — JSON body
- **Returns (parsed)**: `RefundOrderLinesResponse`
- **Returns (raw)**: `ApiResult[RefundOrderLinesResponse, RefundOrderLinesErrorBody]`
- **Error**: `RefundOrderLinesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RefundOrderLinesRequest` | `walmart_apis/models/refund_order_lines_request.py` |
| `RefundOrderLinesRequestDict` | `walmart_apis/models/refund_order_lines_request.py` |
| `RefundOrderLinesResponse` | `walmart_apis/models/refund_order_lines_response.py` |
| `RefundOrderLinesErrorBody` | `walmart_apis/errors/refund_order_lines_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.ship_order_lines

- **Route**: `POST /orders/v4/orders/{purchaseOrderId}/shipping`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def ship_order_lines(purchase_order_id: str, body: ShipOrderLinesRequest | ShipOrderLinesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `body`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `body` — JSON body
- **Returns (parsed)**: `ShipOrderLinesResponse`
- **Returns (raw)**: `ApiResult[ShipOrderLinesResponse, ShipOrderLinesErrorBody]`
- **Error**: `ShipOrderLinesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ShipOrderLinesRequest` | `walmart_apis/models/ship_order_lines_request.py` |
| `ShipOrderLinesRequestDict` | `walmart_apis/models/ship_order_lines_request.py` |
| `ShipOrderLinesResponse` | `walmart_apis/models/ship_order_lines_response.py` |
| `ShipOrderLinesErrorBody` | `walmart_apis/errors/ship_order_lines_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.ship_order_multi_package

- **Route**: `POST /orders/v4/orders/{purchaseOrderId}/multi-package-shipping`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def ship_order_multi_package(purchase_order_id: str, body: MultiPackageShipRequest | MultiPackageShipRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `body`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `body` — JSON body
- **Returns (parsed)**: `MultiPackageShipResponse`
- **Returns (raw)**: `ApiResult[MultiPackageShipResponse, ShipOrderMultiPackageErrorBody]`
- **Error**: `ShipOrderMultiPackageErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `MultiPackageShipRequest` | `walmart_apis/models/multi_package_ship_request.py` |
| `MultiPackageShipRequestDict` | `walmart_apis/models/multi_package_ship_request.py` |
| `MultiPackageShipResponse` | `walmart_apis/models/multi_package_ship_response.py` |
| `ShipOrderMultiPackageErrorBody` | `walmart_apis/errors/ship_order_multi_package_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.update_shipment_status

- **Route**: `POST /orders/v4/orders/{purchaseOrderId}/shipment-status`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_shipment_status(purchase_order_id: str, body: UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `body`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `body` — JSON body
- **Returns (parsed)**: `UpdateShipmentStatusResponse`
- **Returns (raw)**: `ApiResult[UpdateShipmentStatusResponse, UpdateShipmentStatusErrorBody]`
- **Error**: `UpdateShipmentStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateShipmentStatusRequest` | `walmart_apis/models/update_shipment_status_request.py` |
| `UpdateShipmentStatusRequestDict` | `walmart_apis/models/update_shipment_status_request.py` |
| `UpdateShipmentStatusResponse` | `walmart_apis/models/update_shipment_status_response.py` |
| `UpdateShipmentStatusErrorBody` | `walmart_apis/errors/update_shipment_status_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.orders.update_verification_status

- **Route**: `PATCH /orders/v4/orders/{purchaseOrderId}/regulatedInfo`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_verification_status(purchase_order_id: str, body: UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `purchase_order_id`, `body`
- **Params**: `purchase_order_id` — path `purchaseOrderId` · `body` — JSON body
- **Returns (parsed)**: `UpdateVerificationStatusResponse`
- **Returns (raw)**: `ApiResult[UpdateVerificationStatusResponse, UpdateVerificationStatusErrorBody]`
- **Error**: `UpdateVerificationStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateVerificationStatusRequest` | `walmart_apis/models/update_verification_status_request.py` |
| `UpdateVerificationStatusRequestDict` | `walmart_apis/models/update_verification_status_request.py` |
| `UpdateVerificationStatusResponse` | `walmart_apis/models/update_verification_status_response.py` |
| `UpdateVerificationStatusErrorBody` | `walmart_apis/errors/update_verification_status_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

