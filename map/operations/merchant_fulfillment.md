<!-- Generated file — do not edit; regenerated with the SDK. -->

# MerchantFulfillment — operations

Accessor: `client.merchant_fulfillment` · Source: `walmart_apis/apis/merchant_fulfillment.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.merchant_fulfillment.cancel_shipment

- **Route**: `DELETE /mfn/v4/shipments/{shipmentId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_shipment(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shipment_id`
- **Params**: `shipment_id` — path `shipmentId`
- **Returns (parsed)**: `CancelShipmentResponse`
- **Returns (raw)**: `ApiResult[CancelShipmentResponse, CancelShipmentErrorBody]`
- **Error**: `CancelShipmentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelShipmentResponse` | `walmart_apis/models/cancel_shipment_response.py` |
| `CancelShipmentErrorBody` | `walmart_apis/errors/cancel_shipment_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.merchant_fulfillment.create_shipment

- **Route**: `POST /mfn/v4/shipments`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_shipment(body: CreateShipmentRequest | CreateShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateShipmentResponse`
- **Returns (raw)**: `ApiResult[CreateShipmentResponse, CreateShipmentErrorBody]`
- **Error**: `CreateShipmentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateShipmentRequest` | `walmart_apis/models/create_shipment_request.py` |
| `CreateShipmentRequestDict` | `walmart_apis/models/create_shipment_request.py` |
| `CreateShipmentResponse` | `walmart_apis/models/create_shipment_response.py` |
| `CreateShipmentErrorBody` | `walmart_apis/errors/create_shipment_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.merchant_fulfillment.get_eligible_shipping_services

- **Route**: `POST /mfn/v4/eligibleShippingServices`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_eligible_shipping_services(body: GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetEligibleShippingServicesResponse`
- **Returns (raw)**: `ApiResult[GetEligibleShippingServicesResponse, GetEligibleShippingServicesErrorBody]`
- **Error**: `GetEligibleShippingServicesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetEligibleShippingServicesRequest` | `walmart_apis/models/get_eligible_shipping_services_request.py` |
| `GetEligibleShippingServicesRequestDict` | `walmart_apis/models/get_eligible_shipping_services_request.py` |
| `GetEligibleShippingServicesResponse` | `walmart_apis/models/get_eligible_shipping_services_response.py` |
| `GetEligibleShippingServicesErrorBody` | `walmart_apis/errors/get_eligible_shipping_services_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.merchant_fulfillment.get_label

- **Route**: `GET /mfn/v4/shipments/{shipmentId}/label`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_label(shipment_id: str, *, format_: FormatOrStr | None = Format.PDF, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shipment_id`
- **Params**: `shipment_id` — path `shipmentId` · `format_` — query `format`
- **Returns (parsed)**: `Label`
- **Returns (raw)**: `ApiResult[Label, GetLabelErrorBody]`
- **Error**: `GetLabelErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatOrStr` | `walmart_apis/models/enums/format.py` |
| `Label` | `walmart_apis/models/label.py` |
| `GetLabelErrorBody` | `walmart_apis/errors/get_label_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.merchant_fulfillment.get_shipment2

- **Route**: `GET /mfn/v4/shipments/{shipmentId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_shipment2(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shipment_id`
- **Params**: `shipment_id` — path `shipmentId`
- **Returns (parsed)**: `GetShipmentResponse`
- **Returns (raw)**: `ApiResult[GetShipmentResponse, GetShipment2ErrorBody]`
- **Error**: `GetShipment2ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetShipmentResponse` | `walmart_apis/models/get_shipment_response.py` |
| `GetShipment2ErrorBody` | `walmart_apis/errors/get_shipment2_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

