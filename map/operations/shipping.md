<!-- Generated file — do not edit; regenerated with the SDK. -->

# Shipping — operations

Accessor: `client.shipping` · Source: `walmart_apis/apis/shipping.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.shipping.cancel_shipment2

- **Route**: `PUT /v4/fulfillment/shipping/shipments/{shipment-id}/cancel`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def cancel_shipment2(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shipment_id`
- **Params**: `shipment_id` — path `shipment-id`
- **Returns (parsed)**: `CancelShipmentResponseShipping`
- **Returns (raw)**: `ApiResult[CancelShipmentResponseShipping, CancelShipment2ErrorBody]`
- **Error**: `CancelShipment2ErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelShipmentResponseShipping` | `walmart_apis/models/cancel_shipment_response_shipping.py` |
| `CancelShipment2ErrorBody` | `walmart_apis/errors/cancel_shipment2_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.shipping.get_access_points

- **Route**: `GET /v4/fulfillment/shipping/access-points`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_access_points(access_point_types: str, country_code: str, postal_code: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `access_point_types`, `country_code`, `postal_code`
- **Params**: `access_point_types` — query `accessPointTypes` · `country_code` — query `countryCode` · `postal_code` — query `postalCode`
- **Returns (parsed)**: `GetAccessPointsResponse`
- **Returns (raw)**: `ApiResult[GetAccessPointsResponse, GetAccessPointsErrorBody]`
- **Error**: `GetAccessPointsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAccessPointsResponse` | `walmart_apis/models/get_access_points_response.py` |
| `GetAccessPointsErrorBody` | `walmart_apis/errors/get_access_points_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.shipping.get_additional_inputs

- **Route**: `GET /v4/fulfillment/shipping/shipments/additional-input-schemas`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_additional_inputs(rate_id: str, request_token: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `rate_id`, `request_token`
- **Params**: `rate_id` — query `rateId` · `request_token` — query `requestToken`
- **Returns (parsed)**: `GetAdditionalInputsResponse`
- **Returns (raw)**: `ApiResult[GetAdditionalInputsResponse, GetAdditionalInputsErrorBody]`
- **Error**: `GetAdditionalInputsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAdditionalInputsResponse` | `walmart_apis/models/get_additional_inputs_response.py` |
| `GetAdditionalInputsErrorBody` | `walmart_apis/errors/get_additional_inputs_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.shipping.get_rates

- **Route**: `POST /v4/fulfillment/shipping/shipment-rates`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_rates(body: GetRatesRequest | GetRatesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetRatesResponse`
- **Returns (raw)**: `ApiResult[GetRatesResponse, GetRatesErrorBody]`
- **Error**: `GetRatesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetRatesRequest` | `walmart_apis/models/get_rates_request.py` |
| `GetRatesRequestDict` | `walmart_apis/models/get_rates_request.py` |
| `GetRatesResponse` | `walmart_apis/models/get_rates_response.py` |
| `GetRatesErrorBody` | `walmart_apis/errors/get_rates_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.shipping.get_shipment_documents

- **Route**: `GET /v4/fulfillment/shipping/shipments/{shipment-id}/documents`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_shipment_documents(shipment_id: str, *, package_client_reference_id: str | None = None, format_: FormatShippingOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shipment_id`
- **Params**: `shipment_id` — path `shipment-id` · `package_client_reference_id` — query `packageClientReferenceId` · `format_` — query `format`
- **Returns (parsed)**: `GetShipmentDocumentsResponse`
- **Returns (raw)**: `ApiResult[GetShipmentDocumentsResponse, GetShipmentDocumentsErrorBody]`
- **Error**: `GetShipmentDocumentsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FormatShippingOrStr` | `walmart_apis/models/enums/format_shipping.py` |
| `GetShipmentDocumentsResponse` | `walmart_apis/models/get_shipment_documents_response.py` |
| `GetShipmentDocumentsErrorBody` | `walmart_apis/errors/get_shipment_documents_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.shipping.get_tracking

- **Route**: `GET /v4/fulfillment/shipping/tracking-events`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_tracking(tracking_id: str, *, carrier_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `tracking_id`
- **Params**: `tracking_id` — query `trackingId` · `carrier_id` — query `carrierId`
- **Returns (parsed)**: `GetTrackingResponse`
- **Returns (raw)**: `ApiResult[GetTrackingResponse, GetTrackingErrorBody]`
- **Error**: `GetTrackingErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetTrackingResponse` | `walmart_apis/models/get_tracking_response.py` |
| `GetTrackingErrorBody` | `walmart_apis/errors/get_tracking_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.shipping.one_click_shipment

- **Route**: `POST /v4/fulfillment/shipping/shipments/oneClickShipment`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def one_click_shipment(body: OneClickShipmentRequest | OneClickShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `OneClickShipmentResponse`
- **Returns (raw)**: `ApiResult[OneClickShipmentResponse, OneClickShipmentErrorBody]`
- **Error**: `OneClickShipmentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `OneClickShipmentRequest` | `walmart_apis/models/one_click_shipment_request.py` |
| `OneClickShipmentRequestDict` | `walmart_apis/models/one_click_shipment_request.py` |
| `OneClickShipmentResponse` | `walmart_apis/models/one_click_shipment_response.py` |
| `OneClickShipmentErrorBody` | `walmart_apis/errors/one_click_shipment_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.shipping.purchase_shipment

- **Route**: `POST /v4/fulfillment/shipping/shipments`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def purchase_shipment(body: PurchaseShipmentRequest | PurchaseShipmentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PurchaseShipmentResponse`
- **Returns (raw)**: `ApiResult[PurchaseShipmentResponse, PurchaseShipmentErrorBody]`
- **Error**: `PurchaseShipmentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PurchaseShipmentRequest` | `walmart_apis/models/purchase_shipment_request.py` |
| `PurchaseShipmentRequestDict` | `walmart_apis/models/purchase_shipment_request.py` |
| `PurchaseShipmentResponse` | `walmart_apis/models/purchase_shipment_response.py` |
| `PurchaseShipmentErrorBody` | `walmart_apis/errors/purchase_shipment_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.shipping.submit_ndr_feedback

- **Route**: `POST /v4/fulfillment/shipping/ndr-feedback`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def submit_ndr_feedback(body: SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, SubmitNdrFeedbackErrorBody]`
- **Error**: `SubmitNdrFeedbackErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SubmitNdrFeedbackRequest` | `walmart_apis/models/submit_ndr_feedback_request.py` |
| `SubmitNdrFeedbackRequestDict` | `walmart_apis/models/submit_ndr_feedback_request.py` |
| `SubmitNdrFeedbackErrorBody` | `walmart_apis/errors/submit_ndr_feedback_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

