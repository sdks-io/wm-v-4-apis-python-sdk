<!-- Generated file — do not edit; regenerated with the SDK. -->

# WfsInbound — operations

Accessor: `client.wfs_inbound` · Source: `walmart_apis/apis/wfs_inbound.py` · 45 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.wfs_inbound.cancel_inbound_plan

- **Route**: `PUT /inbound/wfs/v4/inboundPlans/{inboundPlanId}/cancellation`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_inbound_plan(inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId`
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, CancelInboundPlanErrorBody]`
- **Error**: `CancelInboundPlanErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `CancelInboundPlanErrorBody` | `walmart_apis/errors/cancel_inbound_plan_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.cancel_self_ship_appointment

- **Route**: `PUT /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentCancellation`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_self_ship_appointment(inbound_plan_id: str, shipment_id: str, body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, CancelSelfShipAppointmentErrorBody]`
- **Error**: `CancelSelfShipAppointmentErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelSelfShipAppointmentRequest` | `walmart_apis/models/cancel_self_ship_appointment_request.py` |
| `CancelSelfShipAppointmentRequestDict` | `walmart_apis/models/cancel_self_ship_appointment_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `CancelSelfShipAppointmentErrorBody` | `walmart_apis/errors/cancel_self_ship_appointment_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.confirm_delivery_window_options

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions/{deliveryWindowOptionId}/confirmation`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def confirm_delivery_window_options(inbound_plan_id: str, shipment_id: str, delivery_window_option_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `delivery_window_option_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `delivery_window_option_id` — path `deliveryWindowOptionId`
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, ConfirmDeliveryWindowOptionsErrorBody]`
- **Error**: `ConfirmDeliveryWindowOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `ConfirmDeliveryWindowOptionsErrorBody` | `walmart_apis/errors/confirm_delivery_window_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.confirm_packing_option

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions/{packingOptionId}/confirmation`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def confirm_packing_option(inbound_plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `packing_option_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `packing_option_id` — path `packingOptionId`
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, ConfirmPackingOptionErrorBody]`
- **Error**: `ConfirmPackingOptionErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `ConfirmPackingOptionErrorBody` | `walmart_apis/errors/confirm_packing_option_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.confirm_placement_option

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions/{placementOptionId}/confirmation`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def confirm_placement_option(inbound_plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `placement_option_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `placement_option_id` — path `placementOptionId`
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, ConfirmPlacementOptionErrorBody]`
- **Error**: `ConfirmPlacementOptionErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `ConfirmPlacementOptionErrorBody` | `walmart_apis/errors/confirm_placement_option_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.confirm_shipment_content_update_preview

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}/confirmation`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def confirm_shipment_content_update_preview(inbound_plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `content_update_preview_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `content_update_preview_id` — path `contentUpdatePreviewId`
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, ConfirmShipmentContentUpdatePreviewErrorBody]`
- **Error**: `ConfirmShipmentContentUpdatePreviewErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `ConfirmShipmentContentUpdatePreviewErrorBody` | `walmart_apis/errors/confirm_shipment_content_update_preview_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.confirm_transportation_options

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions/confirmation`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def confirm_transportation_options(inbound_plan_id: str, body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, ConfirmTransportationOptionsErrorBody]`
- **Error**: `ConfirmTransportationOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfirmTransportationOptionsRequest` | `walmart_apis/models/confirm_transportation_options_request.py` |
| `ConfirmTransportationOptionsRequestDict` | `walmart_apis/models/confirm_transportation_options_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `ConfirmTransportationOptionsErrorBody` | `walmart_apis/errors/confirm_transportation_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.create_inbound_plan

- **Route**: `POST /inbound/wfs/v4/inboundPlans`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_inbound_plan(body: CreateInboundPlanRequest | CreateInboundPlanRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CreateInboundPlanResponse, CreateInboundPlanErrorBody]`
- **Error**: `CreateInboundPlanErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateInboundPlanRequest` | `walmart_apis/models/create_inbound_plan_request.py` |
| `CreateInboundPlanRequestDict` | `walmart_apis/models/create_inbound_plan_request.py` |
| `CreateInboundPlanResponse` | `walmart_apis/models/create_inbound_plan_response.py` |
| `CreateInboundPlanErrorBody` | `walmart_apis/errors/create_inbound_plan_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.create_marketplace_item_labels

- **Route**: `POST /inbound/wfs/v4/items/labels`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_marketplace_item_labels(body: CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateMarketplaceItemLabelsResponse`
- **Returns (raw)**: `ApiResult[CreateMarketplaceItemLabelsResponse, CreateMarketplaceItemLabelsErrorBody]`
- **Error**: `CreateMarketplaceItemLabelsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateMarketplaceItemLabelsRequest` | `walmart_apis/models/create_marketplace_item_labels_request.py` |
| `CreateMarketplaceItemLabelsRequestDict` | `walmart_apis/models/create_marketplace_item_labels_request.py` |
| `CreateMarketplaceItemLabelsResponse` | `walmart_apis/models/create_marketplace_item_labels_response.py` |
| `CreateMarketplaceItemLabelsErrorBody` | `walmart_apis/errors/create_marketplace_item_labels_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.generate_delivery_window_options

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def generate_delivery_window_options(inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId`
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, GenerateDeliveryWindowOptionsErrorBody]`
- **Error**: `GenerateDeliveryWindowOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `GenerateDeliveryWindowOptionsErrorBody` | `walmart_apis/errors/generate_delivery_window_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.generate_packing_options

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def generate_packing_options(inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId`
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, GeneratePackingOptionsErrorBody]`
- **Error**: `GeneratePackingOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `GeneratePackingOptionsErrorBody` | `walmart_apis/errors/generate_packing_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.generate_placement_options

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def generate_placement_options(inbound_plan_id: str, body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, GeneratePlacementOptionsErrorBody]`
- **Error**: `GeneratePlacementOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GeneratePlacementOptionsRequest` | `walmart_apis/models/generate_placement_options_request.py` |
| `GeneratePlacementOptionsRequestDict` | `walmart_apis/models/generate_placement_options_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `GeneratePlacementOptionsErrorBody` | `walmart_apis/errors/generate_placement_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.generate_self_ship_appointment_slots

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def generate_self_ship_appointment_slots(inbound_plan_id: str, shipment_id: str, body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, GenerateSelfShipAppointmentSlotsErrorBody]`
- **Error**: `GenerateSelfShipAppointmentSlotsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateSelfShipAppointmentSlotsRequest` | `walmart_apis/models/generate_self_ship_appointment_slots_request.py` |
| `GenerateSelfShipAppointmentSlotsRequestDict` | `walmart_apis/models/generate_self_ship_appointment_slots_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `GenerateSelfShipAppointmentSlotsErrorBody` | `walmart_apis/errors/generate_self_ship_appointment_slots_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.generate_shipment_content_update_previews

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def generate_shipment_content_update_previews(inbound_plan_id: str, shipment_id: str, body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, GenerateShipmentContentUpdatePreviewsErrorBody]`
- **Error**: `GenerateShipmentContentUpdatePreviewsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateShipmentContentUpdatePreviewsRequest` | `walmart_apis/models/generate_shipment_content_update_previews_request.py` |
| `GenerateShipmentContentUpdatePreviewsRequestDict` | `walmart_apis/models/generate_shipment_content_update_previews_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `GenerateShipmentContentUpdatePreviewsErrorBody` | `walmart_apis/errors/generate_shipment_content_update_previews_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.generate_transportation_options

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def generate_transportation_options(inbound_plan_id: str, body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, GenerateTransportationOptionsErrorBody]`
- **Error**: `GenerateTransportationOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GenerateTransportationOptionsRequest` | `walmart_apis/models/generate_transportation_options_request.py` |
| `GenerateTransportationOptionsRequestDict` | `walmart_apis/models/generate_transportation_options_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `GenerateTransportationOptionsErrorBody` | `walmart_apis/errors/generate_transportation_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.get_delivery_challan_document

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryChallanDocument`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_delivery_challan_document(inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId`
- **Returns (parsed)**: `GetDeliveryChallanDocumentResponse`
- **Returns (raw)**: `ApiResult[GetDeliveryChallanDocumentResponse, GetDeliveryChallanDocumentErrorBody]`
- **Error**: `GetDeliveryChallanDocumentErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetDeliveryChallanDocumentResponse` | `walmart_apis/models/get_delivery_challan_document_response.py` |
| `GetDeliveryChallanDocumentErrorBody` | `walmart_apis/errors/get_delivery_challan_document_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.get_inbound_operation_status

- **Route**: `GET /inbound/wfs/v4/operations/{operationId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_inbound_operation_status(operation_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `operation_id`
- **Params**: `operation_id` — path `operationId`
- **Returns (parsed)**: `CommonInboundOperationStatus`
- **Returns (raw)**: `ApiResult[CommonInboundOperationStatus, GetInboundOperationStatusErrorBody]`
- **Error**: `GetInboundOperationStatusErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CommonInboundOperationStatus` | `walmart_apis/models/common_inbound_operation_status.py` |
| `GetInboundOperationStatusErrorBody` | `walmart_apis/errors/get_inbound_operation_status_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.get_inbound_plan

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_inbound_plan(inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId`
- **Returns (parsed)**: `InboundPlan`
- **Returns (raw)**: `ApiResult[InboundPlan, GetInboundPlanErrorBody]`
- **Error**: `GetInboundPlanErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InboundPlan` | `walmart_apis/models/inbound_plan.py` |
| `GetInboundPlanErrorBody` | `walmart_apis/errors/get_inbound_plan_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.get_self_ship_appointment_slots

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_self_ship_appointment_slots(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `GetSelfShipAppointmentSlotsResponse`
- **Returns (raw)**: `ApiResult[GetSelfShipAppointmentSlotsResponse, GetSelfShipAppointmentSlotsErrorBody]`
- **Error**: `GetSelfShipAppointmentSlotsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetSelfShipAppointmentSlotsResponse` | `walmart_apis/models/get_self_ship_appointment_slots_response.py` |
| `GetSelfShipAppointmentSlotsErrorBody` | `walmart_apis/errors/get_self_ship_appointment_slots_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.get_shipment

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_shipment(inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId`
- **Returns (parsed)**: `CommonShipment`
- **Returns (raw)**: `ApiResult[CommonShipment, GetShipmentErrorBody]`
- **Error**: `GetShipmentErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CommonShipment` | `walmart_apis/models/common_shipment.py` |
| `GetShipmentErrorBody` | `walmart_apis/errors/get_shipment_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.get_shipment_content_update_preview

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_shipment_content_update_preview(inbound_plan_id: str, shipment_id: str, content_update_preview_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `content_update_preview_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `content_update_preview_id` — path `contentUpdatePreviewId`
- **Returns (parsed)**: `CommonContentUpdatePreview`
- **Returns (raw)**: `ApiResult[CommonContentUpdatePreview, GetShipmentContentUpdatePreviewErrorBody]`
- **Error**: `GetShipmentContentUpdatePreviewErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CommonContentUpdatePreview` | `walmart_apis/models/common_content_update_preview.py` |
| `GetShipmentContentUpdatePreviewErrorBody` | `walmart_apis/errors/get_shipment_content_update_preview_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_delivery_window_options

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_delivery_window_options(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListDeliveryWindowOptionsResponse`
- **Returns (raw)**: `ApiResult[ListDeliveryWindowOptionsResponse, ListDeliveryWindowOptionsErrorBody]`
- **Error**: `ListDeliveryWindowOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListDeliveryWindowOptionsResponse` | `walmart_apis/models/list_delivery_window_options_response.py` |
| `ListDeliveryWindowOptionsErrorBody` | `walmart_apis/errors/list_delivery_window_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_inbound_plan_boxes

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/boxes`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_inbound_plan_boxes(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanBoxesResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanBoxesResponse, ListInboundPlanBoxesErrorBody]`
- **Error**: `ListInboundPlanBoxesErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanBoxesResponse` | `walmart_apis/models/list_inbound_plan_boxes_response.py` |
| `ListInboundPlanBoxesErrorBody` | `walmart_apis/errors/list_inbound_plan_boxes_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_inbound_plan_items

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/items`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_inbound_plan_items(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanItemsResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanItemsResponse, ListInboundPlanItemsErrorBody]`
- **Error**: `ListInboundPlanItemsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanItemsResponse` | `walmart_apis/models/list_inbound_plan_items_response.py` |
| `ListInboundPlanItemsErrorBody` | `walmart_apis/errors/list_inbound_plan_items_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_inbound_plan_pallets

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/pallets`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_inbound_plan_pallets(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanPalletsResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanPalletsResponse, ListInboundPlanPalletsErrorBody]`
- **Error**: `ListInboundPlanPalletsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanPalletsResponse` | `walmart_apis/models/list_inbound_plan_pallets_response.py` |
| `ListInboundPlanPalletsErrorBody` | `walmart_apis/errors/list_inbound_plan_pallets_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_inbound_plans

- **Route**: `GET /inbound/wfs/v4/inboundPlans`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_inbound_plans(*, page_size: int | None = 10, pagination_token: str | None = None, status: str | None = None, sort_by: str | None = None, sort_order: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `pageSize` · `pagination_token` — query `paginationToken` · `status` — query · `sort_by` — query `sortBy` · `sort_order` — query `sortOrder`
- **Returns (parsed)**: `ListInboundPlansResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlansResponse, ListInboundPlansErrorBody]`
- **Error**: `ListInboundPlansErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlansResponse` | `walmart_apis/models/list_inbound_plans_response.py` |
| `ListInboundPlansErrorBody` | `walmart_apis/errors/list_inbound_plans_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_item_compliance_details

- **Route**: `GET /inbound/wfs/v4/items/compliance`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_item_compliance_details(mskus: list[str], marketplace_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `mskus`, `marketplace_id`
- **Params**: `mskus` — query · `marketplace_id` — query `marketplaceId`
- **Returns (parsed)**: `ListItemComplianceDetailsResponse`
- **Returns (raw)**: `ApiResult[ListItemComplianceDetailsResponse, ListItemComplianceDetailsErrorBody]`
- **Error**: `ListItemComplianceDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListItemComplianceDetailsResponse` | `walmart_apis/models/list_item_compliance_details_response.py` |
| `ListItemComplianceDetailsErrorBody` | `walmart_apis/errors/list_item_compliance_details_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_packing_group_boxes

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/boxes`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_packing_group_boxes(inbound_plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `packing_group_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `packing_group_id` — path `packingGroupId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanBoxesResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanBoxesResponse, ListPackingGroupBoxesErrorBody]`
- **Error**: `ListPackingGroupBoxesErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanBoxesResponse` | `walmart_apis/models/list_inbound_plan_boxes_response.py` |
| `ListPackingGroupBoxesErrorBody` | `walmart_apis/errors/list_packing_group_boxes_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_packing_group_items

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/items`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_packing_group_items(inbound_plan_id: str, packing_group_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `packing_group_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `packing_group_id` — path `packingGroupId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanItemsResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanItemsResponse, ListPackingGroupItemsErrorBody]`
- **Error**: `ListPackingGroupItemsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanItemsResponse` | `walmart_apis/models/list_inbound_plan_items_response.py` |
| `ListPackingGroupItemsErrorBody` | `walmart_apis/errors/list_packing_group_items_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_packing_options

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_packing_options(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListPackingOptionsResponse`
- **Returns (raw)**: `ApiResult[ListPackingOptionsResponse, ListPackingOptionsErrorBody]`
- **Error**: `ListPackingOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListPackingOptionsResponse` | `walmart_apis/models/list_packing_options_response.py` |
| `ListPackingOptionsErrorBody` | `walmart_apis/errors/list_packing_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_placement_options

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_placement_options(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListPlacementOptionsResponse`
- **Returns (raw)**: `ApiResult[ListPlacementOptionsResponse, ListPlacementOptionsErrorBody]`
- **Error**: `ListPlacementOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListPlacementOptionsResponse` | `walmart_apis/models/list_placement_options_response.py` |
| `ListPlacementOptionsErrorBody` | `walmart_apis/errors/list_placement_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_prep_details

- **Route**: `GET /inbound/wfs/v4/items/prepDetails`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_prep_details(marketplace_id: str, mskus: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `marketplace_id`, `mskus`
- **Params**: `marketplace_id` — query `marketplaceId` · `mskus` — query
- **Returns (parsed)**: `ListPrepDetailsResponse`
- **Returns (raw)**: `ApiResult[ListPrepDetailsResponse, ListPrepDetailsErrorBody]`
- **Error**: `ListPrepDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListPrepDetailsResponse` | `walmart_apis/models/list_prep_details_response.py` |
| `ListPrepDetailsErrorBody` | `walmart_apis/errors/list_prep_details_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_shipment_boxes

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/boxes`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_shipment_boxes(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanBoxesResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanBoxesResponse, ListShipmentBoxesErrorBody]`
- **Error**: `ListShipmentBoxesErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanBoxesResponse` | `walmart_apis/models/list_inbound_plan_boxes_response.py` |
| `ListShipmentBoxesErrorBody` | `walmart_apis/errors/list_shipment_boxes_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_shipment_content_update_previews

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_shipment_content_update_previews(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListShipmentContentUpdatePreviewsResponse`
- **Returns (raw)**: `ApiResult[ListShipmentContentUpdatePreviewsResponse, ListShipmentContentUpdatePreviewsErrorBody]`
- **Error**: `ListShipmentContentUpdatePreviewsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListShipmentContentUpdatePreviewsResponse` | `walmart_apis/models/list_shipment_content_update_previews_response.py` |
| `ListShipmentContentUpdatePreviewsErrorBody` | `walmart_apis/errors/list_shipment_content_update_previews_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_shipment_items

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/items`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_shipment_items(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanItemsResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanItemsResponse, ListShipmentItemsErrorBody]`
- **Error**: `ListShipmentItemsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanItemsResponse` | `walmart_apis/models/list_inbound_plan_items_response.py` |
| `ListShipmentItemsErrorBody` | `walmart_apis/errors/list_shipment_items_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_shipment_pallets

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/pallets`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_shipment_pallets(inbound_plan_id: str, shipment_id: str, *, page_size: int | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `ListInboundPlanPalletsResponse`
- **Returns (raw)**: `ApiResult[ListInboundPlanPalletsResponse, ListShipmentPalletsErrorBody]`
- **Error**: `ListShipmentPalletsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListInboundPlanPalletsResponse` | `walmart_apis/models/list_inbound_plan_pallets_response.py` |
| `ListShipmentPalletsErrorBody` | `walmart_apis/errors/list_shipment_pallets_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.list_transportation_options

- **Route**: `GET /inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_transportation_options(inbound_plan_id: str, *, page_size: int | None = None, pagination_token: str | None = None, placement_option_id: str | None = None, shipment_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `page_size` — query `pageSize` · `pagination_token` — query `paginationToken` · `placement_option_id` — query `placementOptionId` · `shipment_id` — query `shipmentId`
- **Returns (parsed)**: `ListTransportationOptionsResponse`
- **Returns (raw)**: `ApiResult[ListTransportationOptionsResponse, ListTransportationOptionsErrorBody]`
- **Error**: `ListTransportationOptionsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListTransportationOptionsResponse` | `walmart_apis/models/list_transportation_options_response.py` |
| `ListTransportationOptionsErrorBody` | `walmart_apis/errors/list_transportation_options_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.schedule_self_ship_appointment

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots/{slotId}/schedule`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def schedule_self_ship_appointment(inbound_plan_id: str, shipment_id: str, slot_id: str, body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `slot_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `slot_id` — path `slotId` · `body` — JSON body
- **Returns (parsed)**: `ScheduleSelfShipAppointmentResponse`
- **Returns (raw)**: `ApiResult[ScheduleSelfShipAppointmentResponse, ScheduleSelfShipAppointmentErrorBody]`
- **Error**: `ScheduleSelfShipAppointmentErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ScheduleSelfShipAppointmentRequest` | `walmart_apis/models/schedule_self_ship_appointment_request.py` |
| `ScheduleSelfShipAppointmentRequestDict` | `walmart_apis/models/schedule_self_ship_appointment_request.py` |
| `ScheduleSelfShipAppointmentResponse` | `walmart_apis/models/schedule_self_ship_appointment_response.py` |
| `ScheduleSelfShipAppointmentErrorBody` | `walmart_apis/errors/schedule_self_ship_appointment_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.set_packing_information

- **Route**: `POST /inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingInformation`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def set_packing_information(inbound_plan_id: str, body: SetPackingInformationRequest | SetPackingInformationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, SetPackingInformationErrorBody]`
- **Error**: `SetPackingInformationErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetPackingInformationRequest` | `walmart_apis/models/set_packing_information_request.py` |
| `SetPackingInformationRequestDict` | `walmart_apis/models/set_packing_information_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `SetPackingInformationErrorBody` | `walmart_apis/errors/set_packing_information_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.set_prep_details

- **Route**: `POST /inbound/wfs/v4/items/prepDetails`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def set_prep_details(body: SetPrepDetailsRequest | SetPrepDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, SetPrepDetailsErrorBody]`
- **Error**: `SetPrepDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SetPrepDetailsRequest` | `walmart_apis/models/set_prep_details_request.py` |
| `SetPrepDetailsRequestDict` | `walmart_apis/models/set_prep_details_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `SetPrepDetailsErrorBody` | `walmart_apis/errors/set_prep_details_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.update_inbound_plan_name

- **Route**: `PUT /inbound/wfs/v4/inboundPlans/{inboundPlanId}/name`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_inbound_plan_name(inbound_plan_id: str, body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UpdateInboundPlanNameErrorBody]`
- **Error**: `UpdateInboundPlanNameErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateInboundPlanNameRequest` | `walmart_apis/models/update_inbound_plan_name_request.py` |
| `UpdateInboundPlanNameRequestDict` | `walmart_apis/models/update_inbound_plan_name_request.py` |
| `UpdateInboundPlanNameErrorBody` | `walmart_apis/errors/update_inbound_plan_name_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.update_item_compliance_details

- **Route**: `PUT /inbound/wfs/v4/items/compliance`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_item_compliance_details(marketplace_id: str, body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `marketplace_id`, `body`
- **Params**: `marketplace_id` — query `marketplaceId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, UpdateItemComplianceDetailsErrorBody]`
- **Error**: `UpdateItemComplianceDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateItemComplianceDetailsRequest` | `walmart_apis/models/update_item_compliance_details_request.py` |
| `UpdateItemComplianceDetailsRequestDict` | `walmart_apis/models/update_item_compliance_details_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `UpdateItemComplianceDetailsErrorBody` | `walmart_apis/errors/update_item_compliance_details_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.update_shipment_name

- **Route**: `PUT /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/name`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_shipment_name(inbound_plan_id: str, shipment_id: str, body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `body` — JSON body
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UpdateShipmentNameErrorBody]`
- **Error**: `UpdateShipmentNameErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateShipmentNameRequest` | `walmart_apis/models/update_shipment_name_request.py` |
| `UpdateShipmentNameRequestDict` | `walmart_apis/models/update_shipment_name_request.py` |
| `UpdateShipmentNameErrorBody` | `walmart_apis/errors/update_shipment_name_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.update_shipment_source_address

- **Route**: `PUT /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/sourceAddress`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_shipment_source_address(inbound_plan_id: str, shipment_id: str, body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, UpdateShipmentSourceAddressErrorBody]`
- **Error**: `UpdateShipmentSourceAddressErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateShipmentSourceAddressRequest` | `walmart_apis/models/update_shipment_source_address_request.py` |
| `UpdateShipmentSourceAddressRequestDict` | `walmart_apis/models/update_shipment_source_address_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `UpdateShipmentSourceAddressErrorBody` | `walmart_apis/errors/update_shipment_source_address_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

### client.wfs_inbound.update_shipment_tracking_details

- **Route**: `PUT /inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/trackingDetails`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def update_shipment_tracking_details(inbound_plan_id: str, shipment_id: str, body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `inbound_plan_id`, `shipment_id`, `body`
- **Params**: `inbound_plan_id` — path `inboundPlanId` · `shipment_id` — path `shipmentId` · `body` — JSON body
- **Returns (parsed)**: `CancelInboundPlanResponse`
- **Returns (raw)**: `ApiResult[CancelInboundPlanResponse, UpdateShipmentTrackingDetailsErrorBody]`
- **Error**: `UpdateShipmentTrackingDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `CommonErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateShipmentTrackingDetailsRequest` | `walmart_apis/models/update_shipment_tracking_details_request.py` |
| `UpdateShipmentTrackingDetailsRequestDict` | `walmart_apis/models/update_shipment_tracking_details_request.py` |
| `CancelInboundPlanResponse` | `walmart_apis/models/cancel_inbound_plan_response.py` |
| `UpdateShipmentTrackingDetailsErrorBody` | `walmart_apis/errors/update_shipment_tracking_details_error.py` |
| `CommonErrorList` | `walmart_apis/models/common_error_list.py` |

