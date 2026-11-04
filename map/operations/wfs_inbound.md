<!-- Generated file — do not edit; regenerated with the SDK. -->

# WfsInbound — operations

Accessor: `client.wfs_inbound` · Source: `walmart_apis/apis/wfs_inbound.py` · 52 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wfs_inbound.cancel_inbound_plan

- **Route**: `PUT /v4/fulfillment/inbound/plans/{plan-id}/cancel`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def cancel_inbound_plan(plan_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id`
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, CancelInboundPlanErrorBody]`
- **Error**: `CancelInboundPlanErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `CancelInboundPlanErrorBody` | `walmart_apis/errors/cancel_inbound_plan_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.cancel_self_ship_appointment

- **Route**: `PUT /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-cancel`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def cancel_self_ship_appointment(plan_id: str, shipment_id: str, body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `body` — JSON body
- **Returns (parsed)**: `CancelSelfShipAppointmentResponse`
- **Returns (raw)**: `ApiResult[CancelSelfShipAppointmentResponse, CancelSelfShipAppointmentErrorBody]`
- **Error**: `CancelSelfShipAppointmentErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelSelfShipAppointmentRequest` | `walmart_apis/models/cancel_self_ship_appointment_request.py` |
| `CancelSelfShipAppointmentRequestDict` | `walmart_apis/models/cancel_self_ship_appointment_request.py` |
| `CancelSelfShipAppointmentResponse` | `walmart_apis/models/cancel_self_ship_appointment_response.py` |
| `CancelSelfShipAppointmentErrorBody` | `walmart_apis/errors/cancel_self_ship_appointment_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.confirm_delivery_window_options

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options/{delivery-window-option-id}/confirm`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def confirm_delivery_window_options(plan_id: str, shipment_id: str, delivery_window_option_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `delivery_window_option_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `delivery_window_option_id` — path `delivery-window-option-id`
- **Returns (parsed)**: `ConfirmDeliveryWindowOptionsResponse`
- **Returns (raw)**: `ApiResult[ConfirmDeliveryWindowOptionsResponse, ConfirmDeliveryWindowOptionsErrorBody]`
- **Error**: `ConfirmDeliveryWindowOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfirmDeliveryWindowOptionsResponse` | `walmart_apis/models/confirm_delivery_window_options_response.py` |
| `ConfirmDeliveryWindowOptionsErrorBody` | `walmart_apis/errors/confirm_delivery_window_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.confirm_packing_option

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/packing-options/{packing-option-id}/confirm`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def confirm_packing_option(plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `packing_option_id`
- **Params**: `plan_id` — path `plan-id` · `packing_option_id` — path `packing-option-id`
- **Returns (parsed)**: `ConfirmPackingOptionResponse`
- **Returns (raw)**: `ApiResult[ConfirmPackingOptionResponse, ConfirmPackingOptionErrorBody]`
- **Error**: `ConfirmPackingOptionErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfirmPackingOptionResponse` | `walmart_apis/models/confirm_packing_option_response.py` |
| `ConfirmPackingOptionErrorBody` | `walmart_apis/errors/confirm_packing_option_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.confirm_placement_option

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/placement-options/{placement-option-id}/confirm`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def confirm_placement_option(plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `placement_option_id`
- **Params**: `plan_id` — path `plan-id` · `placement_option_id` — path `placement-option-id`
- **Returns (parsed)**: `ConfirmPlacementOptionResponse`
- **Returns (raw)**: `ApiResult[ConfirmPlacementOptionResponse, ConfirmPlacementOptionErrorBody]`
- **Error**: `ConfirmPlacementOptionErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfirmPlacementOptionResponse` | `walmart_apis/models/confirm_placement_option_response.py` |
| `ConfirmPlacementOptionErrorBody` | `walmart_apis/errors/confirm_placement_option_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.confirm_shipment_content_update_preview

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews/{content-update-preview-id}/confirm`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def confirm_shipment_content_update_preview(plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `content_update_preview_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `content_update_preview_id` — path `content-update-preview-id`
- **Returns (parsed)**: `ConfirmShipmentContentUpdatePreviewResponse`
- **Returns (raw)**: `ApiResult[ConfirmShipmentContentUpdatePreviewResponse, ConfirmShipmentContentUpdatePreviewErrorBody]`
- **Error**: `ConfirmShipmentContentUpdatePreviewErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfirmShipmentContentUpdatePreviewResponse` | `walmart_apis/models/confirm_shipment_content_update_preview_response.py` |
| `ConfirmShipmentContentUpdatePreviewErrorBody` | `walmart_apis/errors/confirm_shipment_content_update_preview_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.confirm_transportation_options

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/transportation-options/confirm`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def confirm_transportation_options(plan_id: str, body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `body` — JSON body
- **Returns (parsed)**: `ConfirmTransportationOptionsResponse`
- **Returns (raw)**: `ApiResult[ConfirmTransportationOptionsResponse, ConfirmTransportationOptionsErrorBody]`
- **Error**: `ConfirmTransportationOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfirmTransportationOptionsRequest` | `walmart_apis/models/confirm_transportation_options_request.py` |
| `ConfirmTransportationOptionsRequestDict` | `walmart_apis/models/confirm_transportation_options_request.py` |
| `ConfirmTransportationOptionsResponse` | `walmart_apis/models/confirm_transportation_options_response.py` |
| `ConfirmTransportationOptionsErrorBody` | `walmart_apis/errors/confirm_transportation_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.create_inbound_plan

- **Route**: `POST /v4/fulfillment/inbound/plans`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def create_inbound_plan(body: CreateInboundPlanRequest | CreateInboundPlanRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CreateInboundPlanResponse, CreateInboundPlanErrorBody]`
- **Error**: `CreateInboundPlanErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateInboundPlanRequest` | `walmart_apis/models/create_inbound_plan_request.py` |
| `CreateInboundPlanRequestDict` | `walmart_apis/models/create_inbound_plan_request.py` |
| `CreateInboundPlanResponse` | `walmart_apis/models/create_inbound_plan_response.py` |
| `CreateInboundPlanErrorBody` | `walmart_apis/errors/create_inbound_plan_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.create_marketplace_item_labels

- **Route**: `POST /v4/fulfillment/inbound/items/labels`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def create_marketplace_item_labels(body: CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateMarketplaceItemLabelsResponse`
- **Returns (raw)**: `ApiResult[CreateMarketplaceItemLabelsResponse, CreateMarketplaceItemLabelsErrorBody]`
- **Error**: `CreateMarketplaceItemLabelsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMarketplaceItemLabelsRequest` | `walmart_apis/models/create_marketplace_item_labels_request.py` |
| `CreateMarketplaceItemLabelsRequestDict` | `walmart_apis/models/create_marketplace_item_labels_request.py` |
| `CreateMarketplaceItemLabelsResponse` | `walmart_apis/models/create_marketplace_item_labels_response.py` |
| `CreateMarketplaceItemLabelsErrorBody` | `walmart_apis/errors/create_marketplace_item_labels_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.generate_delivery_window_options

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def generate_delivery_window_options(plan_id: str, shipment_id: str, *, scac: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `scac` — query
- **Returns (parsed)**: `GenerateDeliveryWindowOptionsResponse`
- **Returns (raw)**: `ApiResult[GenerateDeliveryWindowOptionsResponse, GenerateDeliveryWindowOptionsErrorBody]`
- **Error**: `GenerateDeliveryWindowOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateDeliveryWindowOptionsResponse` | `walmart_apis/models/generate_delivery_window_options_response.py` |
| `GenerateDeliveryWindowOptionsErrorBody` | `walmart_apis/errors/generate_delivery_window_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.generate_packing_options

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/packing-options`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def generate_packing_options(plan_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id`
- **Returns (parsed)**: `GeneratePackingOptionsResponse`
- **Returns (raw)**: `ApiResult[GeneratePackingOptionsResponse, GeneratePackingOptionsErrorBody]`
- **Error**: `GeneratePackingOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GeneratePackingOptionsResponse` | `walmart_apis/models/generate_packing_options_response.py` |
| `GeneratePackingOptionsErrorBody` | `walmart_apis/errors/generate_packing_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.generate_placement_options

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/placement-options`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def generate_placement_options(plan_id: str, body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `body` — JSON body
- **Returns (parsed)**: `GeneratePlacementOptionsResponse`
- **Returns (raw)**: `ApiResult[GeneratePlacementOptionsResponse, GeneratePlacementOptionsErrorBody]`
- **Error**: `GeneratePlacementOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GeneratePlacementOptionsRequest` | `walmart_apis/models/generate_placement_options_request.py` |
| `GeneratePlacementOptionsRequestDict` | `walmart_apis/models/generate_placement_options_request.py` |
| `GeneratePlacementOptionsResponse` | `walmart_apis/models/generate_placement_options_response.py` |
| `GeneratePlacementOptionsErrorBody` | `walmart_apis/errors/generate_placement_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.generate_self_ship_appointment_slots

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def generate_self_ship_appointment_slots(plan_id: str, shipment_id: str, body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `body` — JSON body
- **Returns (parsed)**: `GenerateSelfShipAppointmentSlotsResponse`
- **Returns (raw)**: `ApiResult[GenerateSelfShipAppointmentSlotsResponse, GenerateSelfShipAppointmentSlotsErrorBody]`
- **Error**: `GenerateSelfShipAppointmentSlotsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateSelfShipAppointmentSlotsRequest` | `walmart_apis/models/generate_self_ship_appointment_slots_request.py` |
| `GenerateSelfShipAppointmentSlotsRequestDict` | `walmart_apis/models/generate_self_ship_appointment_slots_request.py` |
| `GenerateSelfShipAppointmentSlotsResponse` | `walmart_apis/models/generate_self_ship_appointment_slots_response.py` |
| `GenerateSelfShipAppointmentSlotsErrorBody` | `walmart_apis/errors/generate_self_ship_appointment_slots_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.generate_shipment_content_update_previews

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def generate_shipment_content_update_previews(plan_id: str, shipment_id: str, body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `body` — JSON body
- **Returns (parsed)**: `GenerateShipmentContentUpdatePreviewsResponse`
- **Returns (raw)**: `ApiResult[GenerateShipmentContentUpdatePreviewsResponse, GenerateShipmentContentUpdatePreviewsErrorBody]`
- **Error**: `GenerateShipmentContentUpdatePreviewsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateShipmentContentUpdatePreviewsRequest` | `walmart_apis/models/generate_shipment_content_update_previews_request.py` |
| `GenerateShipmentContentUpdatePreviewsRequestDict` | `walmart_apis/models/generate_shipment_content_update_previews_request.py` |
| `GenerateShipmentContentUpdatePreviewsResponse` | `walmart_apis/models/generate_shipment_content_update_previews_response.py` |
| `GenerateShipmentContentUpdatePreviewsErrorBody` | `walmart_apis/errors/generate_shipment_content_update_previews_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.generate_transportation_options

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/transportation-options`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def generate_transportation_options(plan_id: str, body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `body` — JSON body
- **Returns (parsed)**: `GenerateTransportationOptionsResponse`
- **Returns (raw)**: `ApiResult[GenerateTransportationOptionsResponse, GenerateTransportationOptionsErrorBody]`
- **Error**: `GenerateTransportationOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateTransportationOptionsRequest` | `walmart_apis/models/generate_transportation_options_request.py` |
| `GenerateTransportationOptionsRequestDict` | `walmart_apis/models/generate_transportation_options_request.py` |
| `GenerateTransportationOptionsResponse` | `walmart_apis/models/generate_transportation_options_response.py` |
| `GenerateTransportationOptionsErrorBody` | `walmart_apis/errors/generate_transportation_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_bill_of_lading

- **Route**: `GET /v4/fulfillment/inbound/shipments/{shipment-id}/bill-of-lading`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_bill_of_lading(shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shipment_id`
- **Params**: `shipment_id` — path `shipment-id`
- **Returns (parsed)**: `GetBillOfLadingResponse`
- **Returns (raw)**: `ApiResult[GetBillOfLadingResponse, GetBillOfLadingErrorBody]`
- **Error**: `GetBillOfLadingErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetBillOfLadingResponse` | `walmart_apis/models/get_bill_of_lading_response.py` |
| `GetBillOfLadingErrorBody` | `walmart_apis/errors/get_bill_of_lading_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_delivery_challan_document

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-challan-document`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_delivery_challan_document(plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id`
- **Returns (parsed)**: `GetDeliveryChallanDocumentResponse`
- **Returns (raw)**: `ApiResult[GetDeliveryChallanDocumentResponse, GetDeliveryChallanDocumentErrorBody]`
- **Error**: `GetDeliveryChallanDocumentErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetDeliveryChallanDocumentResponse` | `walmart_apis/models/get_delivery_challan_document_response.py` |
| `GetDeliveryChallanDocumentErrorBody` | `walmart_apis/errors/get_delivery_challan_document_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_inbound_operation_status

- **Route**: `GET /v4/fulfillment/inbound/operations/{operation-id}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_inbound_operation_status(operation_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `operation_id`
- **Params**: `operation_id` — path `operation-id`
- **Returns (parsed)**: `CommonInboundOperationStatus`
- **Returns (raw)**: `ApiResult[CommonInboundOperationStatus, GetInboundOperationStatusErrorBody]`
- **Error**: `GetInboundOperationStatusErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CommonInboundOperationStatus` | `walmart_apis/models/common_inbound_operation_status.py` |
| `GetInboundOperationStatusErrorBody` | `walmart_apis/errors/get_inbound_operation_status_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_inbound_plan

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_inbound_plan(plan_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id`
- **Returns (parsed)**: `InboundPlan`
- **Returns (raw)**: `ApiResult[InboundPlan, GetInboundPlanErrorBody]`
- **Error**: `GetInboundPlanErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InboundPlan` | `walmart_apis/models/inbound_plan.py` |
| `GetInboundPlanErrorBody` | `walmart_apis/errors/get_inbound_plan_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_item_eligibility_preview

- **Route**: `GET /v4/fulfillment/inbound/eligibility/item-preview`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_item_eligibility_preview(item_id: str, program: Program1OrStr, *, marketplace_ids: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `item_id`, `program`
- **Params**: `item_id` — query `itemId` · `program` — query · `marketplace_ids` — query `marketplaceIds`
- **Returns (parsed)**: `GetItemEligibilityPreviewResponse`
- **Returns (raw)**: `ApiResult[GetItemEligibilityPreviewResponse, GetItemEligibilityPreviewErrorBody]`
- **Error**: `GetItemEligibilityPreviewErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Program1OrStr` | `walmart_apis/models/enums/program1.py` |
| `GetItemEligibilityPreviewResponse` | `walmart_apis/models/get_item_eligibility_preview_response.py` |
| `GetItemEligibilityPreviewErrorBody` | `walmart_apis/errors/get_item_eligibility_preview_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_labels

- **Route**: `GET /v4/fulfillment/inbound/shipments/{shipment-id}/labels`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_labels(shipment_id: str, page_type: PageTypeOrStr, label_type: LabelTypeOrStr, *, page_size: int | None = None, page_start_index: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shipment_id`, `page_type`, `label_type`
- **Params**: `shipment_id` — path `shipment-id` · `page_type` — query `pageType` · `label_type` — query `labelType` · `page_size` — query `pageSize` · `page_start_index` — query `pageStartIndex`
- **Returns (parsed)**: `GetLabelsResponse`
- **Returns (raw)**: `ApiResult[GetLabelsResponse, GetLabelsErrorBody]`
- **Error**: `GetLabelsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PageTypeOrStr` | `walmart_apis/models/enums/page_type.py` |
| `LabelTypeOrStr` | `walmart_apis/models/enums/label_type.py` |
| `GetLabelsResponse` | `walmart_apis/models/get_labels_response.py` |
| `GetLabelsErrorBody` | `walmart_apis/errors/get_labels_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_prep_instructions

- **Route**: `GET /v4/fulfillment/inbound/items/prep-instructions`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_prep_instructions(ship_to_country_code: str, *, seller_sku_list: list[str] | None = None, asin_list: list[str] | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `ship_to_country_code`
- **Params**: `ship_to_country_code` — query `shipToCountryCode` · `seller_sku_list` — query `sellerSkuList` · `asin_list` — query `asinList`
- **Returns (parsed)**: `GetPrepInstructionsResponse`
- **Returns (raw)**: `ApiResult[GetPrepInstructionsResponse, GetPrepInstructionsErrorBody]`
- **Error**: `GetPrepInstructionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetPrepInstructionsResponse` | `walmart_apis/models/get_prep_instructions_response.py` |
| `GetPrepInstructionsErrorBody` | `walmart_apis/errors/get_prep_instructions_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_self_ship_appointment_slots

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_self_ship_appointment_slots(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `GetSelfShipAppointmentSlotsResponse`
- **Returns (raw)**: `ApiResult[GetSelfShipAppointmentSlotsResponse, GetSelfShipAppointmentSlotsErrorBody]`
- **Error**: `GetSelfShipAppointmentSlotsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetSelfShipAppointmentSlotsResponse` | `walmart_apis/models/get_self_ship_appointment_slots_response.py` |
| `GetSelfShipAppointmentSlotsErrorBody` | `walmart_apis/errors/get_self_ship_appointment_slots_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_shipment

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_shipment(plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id`
- **Returns (parsed)**: `CommonShipment`
- **Returns (raw)**: `ApiResult[CommonShipment, GetShipmentErrorBody]`
- **Error**: `GetShipmentErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CommonShipment` | `walmart_apis/models/common_shipment.py` |
| `GetShipmentErrorBody` | `walmart_apis/errors/get_shipment_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_shipment_content_update_preview

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews/{content-update-preview-id}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_shipment_content_update_preview(plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `content_update_preview_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `content_update_preview_id` — path `content-update-preview-id`
- **Returns (parsed)**: `CommonContentUpdatePreview`
- **Returns (raw)**: `ApiResult[CommonContentUpdatePreview, GetShipmentContentUpdatePreviewErrorBody]`
- **Error**: `GetShipmentContentUpdatePreviewErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CommonContentUpdatePreview` | `walmart_apis/models/common_content_update_preview.py` |
| `GetShipmentContentUpdatePreviewErrorBody` | `walmart_apis/errors/get_shipment_content_update_preview_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_shipment_items

- **Route**: `GET /v4/fulfillment/inbound/shipment-items`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_shipment_items(*, date_range_filter: DateRangeFilterOrStr | None = None, date_range_value: str | None = None, page_size: int | None = 10, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `date_range_filter` — query `dateRangeFilter` · `date_range_value` — query `dateRangeValue` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `GetShipmentItemsResponse`
- **Returns (raw)**: `ApiResult[GetShipmentItemsResponse, GetShipmentItemsErrorBody]`
- **Error**: `GetShipmentItemsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DateRangeFilterOrStr` | `walmart_apis/models/enums/date_range_filter.py` |
| `GetShipmentItemsResponse` | `walmart_apis/models/get_shipment_items_response.py` |
| `GetShipmentItemsErrorBody` | `walmart_apis/errors/get_shipment_items_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_shipment_items_by_shipment_id

- **Route**: `GET /v4/fulfillment/inbound/shipments/{shipment-id}/items`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_shipment_items_by_shipment_id(shipment_id: str, *, page_size: int | None = 10, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shipment_id`
- **Params**: `shipment_id` — path `shipment-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `GetShipmentItemsByShipmentIdResponse`
- **Returns (raw)**: `ApiResult[GetShipmentItemsByShipmentIdResponse, GetShipmentItemsByShipmentIdErrorBody]`
- **Error**: `GetShipmentItemsByShipmentIdErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetShipmentItemsByShipmentIdResponse` | `walmart_apis/models/get_shipment_items_by_shipment_id_response.py` |
| `GetShipmentItemsByShipmentIdErrorBody` | `walmart_apis/errors/get_shipment_items_by_shipment_id_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.get_shipments

- **Route**: `GET /v4/fulfillment/inbound/shipments`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_shipments(query_type: ShipmentsQueryTypeOrStr, *, shipment_id_list: list[str] | None = None, shipment_status_list: list[ShipmentStatusOrStr] | None = None, last_updated_after: str | None = None, last_updated_before: str | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query_type`
- **Params**: `query_type` — query `queryType` · `shipment_id_list` — query `shipmentIdList` · `shipment_status_list` — query `shipmentStatusList` · `last_updated_after` — query `lastUpdatedAfter` · `last_updated_before` — query `lastUpdatedBefore` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `GetShipmentsResponse`
- **Returns (raw)**: `ApiResult[GetShipmentsResponse, GetShipmentsErrorBody]`
- **Error**: `GetShipmentsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ShipmentsQueryTypeOrStr` | `walmart_apis/models/enums/shipments_query_type.py` |
| `ShipmentStatusOrStr` | `walmart_apis/models/enums/shipment_status.py` |
| `GetShipmentsResponse` | `walmart_apis/models/get_shipments_response.py` |
| `GetShipmentsErrorBody` | `walmart_apis/errors/get_shipments_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_delivery_window_options

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_delivery_window_options(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListDeliveryWindowOptionsResponse`
- **Returns (raw)**: `ApiResult[ListDeliveryWindowOptionsResponse, ListDeliveryWindowOptionsErrorBody]`
- **Error**: `ListDeliveryWindowOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListDeliveryWindowOptionsResponse` | `walmart_apis/models/list_delivery_window_options_response.py` |
| `ListDeliveryWindowOptionsErrorBody` | `walmart_apis/errors/list_delivery_window_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_inbound_plan_boxes

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/boxes`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_inbound_plan_boxes(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanBoxesResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanBoxesResponse, ListInboundPlanBoxesErrorBody]`
- **Error**: `ListInboundPlanBoxesErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanBoxesResponse` | `walmart_apis/models/list_inbound_plan_boxes_response.py` |
| `ListInboundPlanBoxesErrorBody` | `walmart_apis/errors/list_inbound_plan_boxes_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_inbound_plan_items

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/items`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_inbound_plan_items(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanItemsResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanItemsResponse, ListInboundPlanItemsErrorBody]`
- **Error**: `ListInboundPlanItemsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanItemsResponse` | `walmart_apis/models/list_inbound_plan_items_response.py` |
| `ListInboundPlanItemsErrorBody` | `walmart_apis/errors/list_inbound_plan_items_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_inbound_plan_pallets

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/pallets`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_inbound_plan_pallets(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanPalletsResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanPalletsResponse, ListInboundPlanPalletsErrorBody]`
- **Error**: `ListInboundPlanPalletsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanPalletsResponse` | `walmart_apis/models/list_inbound_plan_pallets_response.py` |
| `ListInboundPlanPalletsErrorBody` | `walmart_apis/errors/list_inbound_plan_pallets_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_inbound_plans

- **Route**: `GET /v4/fulfillment/inbound/plans`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_inbound_plans(*, page_size: int | None = 10, pagination_token: str | None = None, status: str | None = None, sort_by: str | None = None, sort_order: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `pageSize` · `pagination_token` — query `paginationToken` · `status` — query · `sort_by` — query `sortBy` · `sort_order` — query `sortOrder`
- **Returns (parsed)**: `ListInboundPlansResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlansResponse, ListInboundPlansErrorBody]`
- **Error**: `ListInboundPlansErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlansResponse` | `walmart_apis/models/list_inbound_plans_response.py` |
| `ListInboundPlansErrorBody` | `walmart_apis/errors/list_inbound_plans_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_item_compliance_details

- **Route**: `GET /v4/fulfillment/inbound/items/compliance`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_item_compliance_details(mskus: list[str], marketplace_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `mskus`, `marketplace_id`
- **Params**: `mskus` — query · `marketplace_id` — query `marketplaceId`
- **Returns (parsed)**: `ListItemComplianceDetailsResponse`
- **Returns (raw)**: `ApiResult[ListItemComplianceDetailsResponse, ListItemComplianceDetailsErrorBody]`
- **Error**: `ListItemComplianceDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListItemComplianceDetailsResponse` | `walmart_apis/models/list_item_compliance_details_response.py` |
| `ListItemComplianceDetailsErrorBody` | `walmart_apis/errors/list_item_compliance_details_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_packing_group_boxes

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/packing-groups/{packing-group-id}/boxes`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_packing_group_boxes(plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `packing_group_id`
- **Params**: `plan_id` — path `plan-id` · `packing_group_id` — path `packing-group-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListPackingGroupBoxesResponse`
- **Returns (raw)**: `ApiResult[ListPackingGroupBoxesResponse, ListPackingGroupBoxesErrorBody]`
- **Error**: `ListPackingGroupBoxesErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListPackingGroupBoxesResponse` | `walmart_apis/models/list_packing_group_boxes_response.py` |
| `ListPackingGroupBoxesErrorBody` | `walmart_apis/errors/list_packing_group_boxes_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_packing_group_items

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/packing-groups/{packing-group-id}/items`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_packing_group_items(plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `packing_group_id`
- **Params**: `plan_id` — path `plan-id` · `packing_group_id` — path `packing-group-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListPackingGroupItemsResponse`
- **Returns (raw)**: `ApiResult[ListPackingGroupItemsResponse, ListPackingGroupItemsErrorBody]`
- **Error**: `ListPackingGroupItemsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListPackingGroupItemsResponse` | `walmart_apis/models/list_packing_group_items_response.py` |
| `ListPackingGroupItemsErrorBody` | `walmart_apis/errors/list_packing_group_items_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_packing_options

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/packing-options`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_packing_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListPackingOptionsResponse`
- **Returns (raw)**: `ApiResult[ListPackingOptionsResponse, ListPackingOptionsErrorBody]`
- **Error**: `ListPackingOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListPackingOptionsResponse` | `walmart_apis/models/list_packing_options_response.py` |
| `ListPackingOptionsErrorBody` | `walmart_apis/errors/list_packing_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_placement_options

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/placement-options`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_placement_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListPlacementOptionsResponse`
- **Returns (raw)**: `ApiResult[ListPlacementOptionsResponse, ListPlacementOptionsErrorBody]`
- **Error**: `ListPlacementOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListPlacementOptionsResponse` | `walmart_apis/models/list_placement_options_response.py` |
| `ListPlacementOptionsErrorBody` | `walmart_apis/errors/list_placement_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_prep_details

- **Route**: `GET /v4/fulfillment/inbound/items/prep-details`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_prep_details(marketplace_id: str, mskus: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `marketplace_id`, `mskus`
- **Params**: `marketplace_id` — query `marketplaceId` · `mskus` — query
- **Returns (parsed)**: `ListPrepDetailsResponse`
- **Returns (raw)**: `ApiResult[ListPrepDetailsResponse, ListPrepDetailsErrorBody]`
- **Error**: `ListPrepDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListPrepDetailsResponse` | `walmart_apis/models/list_prep_details_response.py` |
| `ListPrepDetailsErrorBody` | `walmart_apis/errors/list_prep_details_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_shipment_boxes

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/boxes`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_shipment_boxes(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListShipmentBoxesResponse`
- **Returns (raw)**: `ApiResult[ListShipmentBoxesResponse, ListShipmentBoxesErrorBody]`
- **Error**: `ListShipmentBoxesErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListShipmentBoxesResponse` | `walmart_apis/models/list_shipment_boxes_response.py` |
| `ListShipmentBoxesErrorBody` | `walmart_apis/errors/list_shipment_boxes_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_shipment_content_update_previews

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_shipment_content_update_previews(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListShipmentContentUpdatePreviewsResponse`
- **Returns (raw)**: `ApiResult[ListShipmentContentUpdatePreviewsResponse, ListShipmentContentUpdatePreviewsErrorBody]`
- **Error**: `ListShipmentContentUpdatePreviewsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListShipmentContentUpdatePreviewsResponse` | `walmart_apis/models/list_shipment_content_update_previews_response.py` |
| `ListShipmentContentUpdatePreviewsErrorBody` | `walmart_apis/errors/list_shipment_content_update_previews_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_shipment_items

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/items`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_shipment_items(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListShipmentItemsResponse`
- **Returns (raw)**: `ApiResult[ListShipmentItemsResponse, ListShipmentItemsErrorBody]`
- **Error**: `ListShipmentItemsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListShipmentItemsResponse` | `walmart_apis/models/list_shipment_items_response.py` |
| `ListShipmentItemsErrorBody` | `walmart_apis/errors/list_shipment_items_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_shipment_pallets

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/pallets`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_shipment_pallets(plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListShipmentPalletsResponse`
- **Returns (raw)**: `ApiResult[ListShipmentPalletsResponse, ListShipmentPalletsErrorBody]`
- **Error**: `ListShipmentPalletsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListShipmentPalletsResponse` | `walmart_apis/models/list_shipment_pallets_response.py` |
| `ListShipmentPalletsErrorBody` | `walmart_apis/errors/list_shipment_pallets_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.list_transportation_options

- **Route**: `GET /v4/fulfillment/inbound/plans/{plan-id}/transportation-options`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def list_transportation_options(plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, placement_option_id: str | None = None, shipment_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`
- **Params**: `plan_id` — path `plan-id` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken` · `placement_option_id` — query `placementOptionId` · `shipment_id` — query `shipmentId`
- **Returns (parsed)**: `ListTransportationOptionsResponse`
- **Returns (raw)**: `ApiResult[ListTransportationOptionsResponse, ListTransportationOptionsErrorBody]`
- **Error**: `ListTransportationOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListTransportationOptionsResponse` | `walmart_apis/models/list_transportation_options_response.py` |
| `ListTransportationOptionsErrorBody` | `walmart_apis/errors/list_transportation_options_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.schedule_self_ship_appointment

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots/{slot-id}/schedule`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def schedule_self_ship_appointment(plan_id: str, shipment_id: str, slot_id: str, body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `slot_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `slot_id` — path `slot-id` · `body` — JSON body
- **Returns (parsed)**: `ScheduleSelfShipAppointmentResponse`
- **Returns (raw)**: `ApiResult[ScheduleSelfShipAppointmentResponse, ScheduleSelfShipAppointmentErrorBody]`
- **Error**: `ScheduleSelfShipAppointmentErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScheduleSelfShipAppointmentRequest` | `walmart_apis/models/schedule_self_ship_appointment_request.py` |
| `ScheduleSelfShipAppointmentRequestDict` | `walmart_apis/models/schedule_self_ship_appointment_request.py` |
| `ScheduleSelfShipAppointmentResponse` | `walmart_apis/models/schedule_self_ship_appointment_response.py` |
| `ScheduleSelfShipAppointmentErrorBody` | `walmart_apis/errors/schedule_self_ship_appointment_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.set_packing_information

- **Route**: `POST /v4/fulfillment/inbound/plans/{plan-id}/packing-information`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def set_packing_information(plan_id: str, body: SetPackingInformationRequest | SetPackingInformationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `body` — JSON body
- **Returns (parsed)**: `SetPackingInformationResponse`
- **Returns (raw)**: `ApiResult[SetPackingInformationResponse, SetPackingInformationErrorBody]`
- **Error**: `SetPackingInformationErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetPackingInformationRequest` | `walmart_apis/models/set_packing_information_request.py` |
| `SetPackingInformationRequestDict` | `walmart_apis/models/set_packing_information_request.py` |
| `SetPackingInformationResponse` | `walmart_apis/models/set_packing_information_response.py` |
| `SetPackingInformationErrorBody` | `walmart_apis/errors/set_packing_information_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.set_prep_details

- **Route**: `POST /v4/fulfillment/inbound/items/prep-details`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def set_prep_details(body: SetPrepDetailsRequest | SetPrepDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SetPrepDetailsResponse`
- **Returns (raw)**: `ApiResult[SetPrepDetailsResponse, SetPrepDetailsErrorBody]`
- **Error**: `SetPrepDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetPrepDetailsRequest` | `walmart_apis/models/set_prep_details_request.py` |
| `SetPrepDetailsRequestDict` | `walmart_apis/models/set_prep_details_request.py` |
| `SetPrepDetailsResponse` | `walmart_apis/models/set_prep_details_response.py` |
| `SetPrepDetailsErrorBody` | `walmart_apis/errors/set_prep_details_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.update_inbound_plan_name

- **Route**: `PUT /v4/fulfillment/inbound/plans/{plan-id}/name`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def update_inbound_plan_name(plan_id: str, body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UpdateInboundPlanNameErrorBody]`
- **Error**: `UpdateInboundPlanNameErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateInboundPlanNameRequest` | `walmart_apis/models/update_inbound_plan_name_request.py` |
| `UpdateInboundPlanNameRequestDict` | `walmart_apis/models/update_inbound_plan_name_request.py` |
| `UpdateInboundPlanNameErrorBody` | `walmart_apis/errors/update_inbound_plan_name_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.update_item_compliance_details

- **Route**: `PUT /v4/fulfillment/inbound/items/compliance`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def update_item_compliance_details(marketplace_id: str, body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `marketplace_id`, `body`
- **Params**: `marketplace_id` — query `marketplaceId` · `body` — JSON body
- **Returns (parsed)**: `UpdateItemComplianceDetailsResponse`
- **Returns (raw)**: `ApiResult[UpdateItemComplianceDetailsResponse, UpdateItemComplianceDetailsErrorBody]`
- **Error**: `UpdateItemComplianceDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateItemComplianceDetailsRequest` | `walmart_apis/models/update_item_compliance_details_request.py` |
| `UpdateItemComplianceDetailsRequestDict` | `walmart_apis/models/update_item_compliance_details_request.py` |
| `UpdateItemComplianceDetailsResponse` | `walmart_apis/models/update_item_compliance_details_response.py` |
| `UpdateItemComplianceDetailsErrorBody` | `walmart_apis/errors/update_item_compliance_details_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.update_shipment_name

- **Route**: `PUT /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/name`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def update_shipment_name(plan_id: str, shipment_id: str, body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UpdateShipmentNameErrorBody]`
- **Error**: `UpdateShipmentNameErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateShipmentNameRequest` | `walmart_apis/models/update_shipment_name_request.py` |
| `UpdateShipmentNameRequestDict` | `walmart_apis/models/update_shipment_name_request.py` |
| `UpdateShipmentNameErrorBody` | `walmart_apis/errors/update_shipment_name_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.update_shipment_source_address

- **Route**: `PUT /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/source-address`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def update_shipment_source_address(plan_id: str, shipment_id: str, body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `body` — JSON body
- **Returns (parsed)**: `UpdateShipmentSourceAddressResponse`
- **Returns (raw)**: `ApiResult[UpdateShipmentSourceAddressResponse, UpdateShipmentSourceAddressErrorBody]`
- **Error**: `UpdateShipmentSourceAddressErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateShipmentSourceAddressRequest` | `walmart_apis/models/update_shipment_source_address_request.py` |
| `UpdateShipmentSourceAddressRequestDict` | `walmart_apis/models/update_shipment_source_address_request.py` |
| `UpdateShipmentSourceAddressResponse` | `walmart_apis/models/update_shipment_source_address_response.py` |
| `UpdateShipmentSourceAddressErrorBody` | `walmart_apis/errors/update_shipment_source_address_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

### client.wfs_inbound.update_shipment_tracking_details

- **Route**: `PUT /v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/tracking-details`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def update_shipment_tracking_details(plan_id: str, shipment_id: str, body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `plan_id`, `shipment_id`, `body`
- **Params**: `plan_id` — path `plan-id` · `shipment_id` — path `shipment-id` · `body` — JSON body
- **Returns (parsed)**: `UpdateShipmentTrackingDetailsResponse`
- **Returns (raw)**: `ApiResult[UpdateShipmentTrackingDetailsResponse, UpdateShipmentTrackingDetailsErrorBody]`
- **Error**: `UpdateShipmentTrackingDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorListFulfillmentInboundPlans` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateShipmentTrackingDetailsRequest` | `walmart_apis/models/update_shipment_tracking_details_request.py` |
| `UpdateShipmentTrackingDetailsRequestDict` | `walmart_apis/models/update_shipment_tracking_details_request.py` |
| `UpdateShipmentTrackingDetailsResponse` | `walmart_apis/models/update_shipment_tracking_details_response.py` |
| `UpdateShipmentTrackingDetailsErrorBody` | `walmart_apis/errors/update_shipment_tracking_details_error.py` |
| `CommonErrorListFulfillmentInboundPlans` | `walmart_apis/models/common_error_list_fulfillment_inbound_plans.py` |

