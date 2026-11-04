from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.cancel_inbound_plan_error import CancelInboundPlanErrorBody, cancel_inbound_plan_error_mapper
from ..errors.cancel_self_ship_appointment_error import (
    CancelSelfShipAppointmentErrorBody,
    cancel_self_ship_appointment_error_mapper,
)
from ..errors.confirm_delivery_window_options_error import (
    ConfirmDeliveryWindowOptionsErrorBody,
    confirm_delivery_window_options_error_mapper,
)
from ..errors.confirm_packing_option_error import ConfirmPackingOptionErrorBody, confirm_packing_option_error_mapper
from ..errors.confirm_placement_option_error import (
    ConfirmPlacementOptionErrorBody,
    confirm_placement_option_error_mapper,
)
from ..errors.confirm_shipment_content_update_preview_error import (
    ConfirmShipmentContentUpdatePreviewErrorBody,
    confirm_shipment_content_update_preview_error_mapper,
)
from ..errors.confirm_transportation_options_error import (
    ConfirmTransportationOptionsErrorBody,
    confirm_transportation_options_error_mapper,
)
from ..errors.create_inbound_plan_error import CreateInboundPlanErrorBody, create_inbound_plan_error_mapper
from ..errors.create_marketplace_item_labels_error import (
    CreateMarketplaceItemLabelsErrorBody,
    create_marketplace_item_labels_error_mapper,
)
from ..errors.generate_delivery_window_options_error import (
    GenerateDeliveryWindowOptionsErrorBody,
    generate_delivery_window_options_error_mapper,
)
from ..errors.generate_packing_options_error import (
    GeneratePackingOptionsErrorBody,
    generate_packing_options_error_mapper,
)
from ..errors.generate_placement_options_error import (
    GeneratePlacementOptionsErrorBody,
    generate_placement_options_error_mapper,
)
from ..errors.generate_self_ship_appointment_slots_error import (
    GenerateSelfShipAppointmentSlotsErrorBody,
    generate_self_ship_appointment_slots_error_mapper,
)
from ..errors.generate_shipment_content_update_previews_error import (
    GenerateShipmentContentUpdatePreviewsErrorBody,
    generate_shipment_content_update_previews_error_mapper,
)
from ..errors.generate_transportation_options_error import (
    GenerateTransportationOptionsErrorBody,
    generate_transportation_options_error_mapper,
)
from ..errors.get_bill_of_lading_error import GetBillOfLadingErrorBody, get_bill_of_lading_error_mapper
from ..errors.get_delivery_challan_document_error import (
    GetDeliveryChallanDocumentErrorBody,
    get_delivery_challan_document_error_mapper,
)
from ..errors.get_inbound_operation_status_error import (
    GetInboundOperationStatusErrorBody,
    get_inbound_operation_status_error_mapper,
)
from ..errors.get_inbound_plan_error import GetInboundPlanErrorBody, get_inbound_plan_error_mapper
from ..errors.get_item_eligibility_preview_error import (
    GetItemEligibilityPreviewErrorBody,
    get_item_eligibility_preview_error_mapper,
)
from ..errors.get_labels_error import GetLabelsErrorBody, get_labels_error_mapper
from ..errors.get_prep_instructions_error import GetPrepInstructionsErrorBody, get_prep_instructions_error_mapper
from ..errors.get_self_ship_appointment_slots_error import (
    GetSelfShipAppointmentSlotsErrorBody,
    get_self_ship_appointment_slots_error_mapper,
)
from ..errors.get_shipment_content_update_preview_error import (
    GetShipmentContentUpdatePreviewErrorBody,
    get_shipment_content_update_preview_error_mapper,
)
from ..errors.get_shipment_error import GetShipmentErrorBody, get_shipment_error_mapper
from ..errors.get_shipment_items_by_shipment_id_error import (
    GetShipmentItemsByShipmentIdErrorBody,
    get_shipment_items_by_shipment_id_error_mapper,
)
from ..errors.get_shipment_items_error import GetShipmentItemsErrorBody, get_shipment_items_error_mapper
from ..errors.get_shipments_error import GetShipmentsErrorBody, get_shipments_error_mapper
from ..errors.list_delivery_window_options_error import (
    ListDeliveryWindowOptionsErrorBody,
    list_delivery_window_options_error_mapper,
)
from ..errors.list_inbound_plan_boxes_error import ListInboundPlanBoxesErrorBody, list_inbound_plan_boxes_error_mapper
from ..errors.list_inbound_plan_items_error import ListInboundPlanItemsErrorBody, list_inbound_plan_items_error_mapper
from ..errors.list_inbound_plan_pallets_error import (
    ListInboundPlanPalletsErrorBody,
    list_inbound_plan_pallets_error_mapper,
)
from ..errors.list_inbound_plans_error import ListInboundPlansErrorBody, list_inbound_plans_error_mapper
from ..errors.list_item_compliance_details_error import (
    ListItemComplianceDetailsErrorBody,
    list_item_compliance_details_error_mapper,
)
from ..errors.list_packing_group_boxes_error import (
    ListPackingGroupBoxesErrorBody,
    list_packing_group_boxes_error_mapper,
)
from ..errors.list_packing_group_items_error import (
    ListPackingGroupItemsErrorBody,
    list_packing_group_items_error_mapper,
)
from ..errors.list_packing_options_error import ListPackingOptionsErrorBody, list_packing_options_error_mapper
from ..errors.list_placement_options_error import ListPlacementOptionsErrorBody, list_placement_options_error_mapper
from ..errors.list_prep_details_error import ListPrepDetailsErrorBody, list_prep_details_error_mapper
from ..errors.list_shipment_boxes_error import ListShipmentBoxesErrorBody, list_shipment_boxes_error_mapper
from ..errors.list_shipment_content_update_previews_error import (
    ListShipmentContentUpdatePreviewsErrorBody,
    list_shipment_content_update_previews_error_mapper,
)
from ..errors.list_shipment_items_error import ListShipmentItemsErrorBody, list_shipment_items_error_mapper
from ..errors.list_shipment_pallets_error import ListShipmentPalletsErrorBody, list_shipment_pallets_error_mapper
from ..errors.list_transportation_options_error import (
    ListTransportationOptionsErrorBody,
    list_transportation_options_error_mapper,
)
from ..errors.schedule_self_ship_appointment_error import (
    ScheduleSelfShipAppointmentErrorBody,
    schedule_self_ship_appointment_error_mapper,
)
from ..errors.set_packing_information_error import SetPackingInformationErrorBody, set_packing_information_error_mapper
from ..errors.set_prep_details_error import SetPrepDetailsErrorBody, set_prep_details_error_mapper
from ..errors.update_inbound_plan_name_error import (
    UpdateInboundPlanNameErrorBody,
    update_inbound_plan_name_error_mapper,
)
from ..errors.update_item_compliance_details_error import (
    UpdateItemComplianceDetailsErrorBody,
    update_item_compliance_details_error_mapper,
)
from ..errors.update_shipment_name_error import UpdateShipmentNameErrorBody, update_shipment_name_error_mapper
from ..errors.update_shipment_source_address_error import (
    UpdateShipmentSourceAddressErrorBody,
    update_shipment_source_address_error_mapper,
)
from ..errors.update_shipment_tracking_details_error import (
    UpdateShipmentTrackingDetailsErrorBody,
    update_shipment_tracking_details_error_mapper,
)
from ..models.cancel_inbound_plan_response import CancelInboundPlanResponse
from ..models.cancel_self_ship_appointment_request import (
    CancelSelfShipAppointmentRequest,
    CancelSelfShipAppointmentRequestDict,
)
from ..models.cancel_self_ship_appointment_response import CancelSelfShipAppointmentResponse
from ..models.common_content_update_preview import CommonContentUpdatePreview
from ..models.common_inbound_operation_status import CommonInboundOperationStatus
from ..models.common_shipment import CommonShipment
from ..models.confirm_delivery_window_options_response import ConfirmDeliveryWindowOptionsResponse
from ..models.confirm_packing_option_response import ConfirmPackingOptionResponse
from ..models.confirm_placement_option_response import ConfirmPlacementOptionResponse
from ..models.confirm_shipment_content_update_preview_response import ConfirmShipmentContentUpdatePreviewResponse
from ..models.confirm_transportation_options_request import (
    ConfirmTransportationOptionsRequest,
    ConfirmTransportationOptionsRequestDict,
)
from ..models.confirm_transportation_options_response import ConfirmTransportationOptionsResponse
from ..models.create_inbound_plan_request import CreateInboundPlanRequest, CreateInboundPlanRequestDict
from ..models.create_inbound_plan_response import CreateInboundPlanResponse
from ..models.create_marketplace_item_labels_request import (
    CreateMarketplaceItemLabelsRequest,
    CreateMarketplaceItemLabelsRequestDict,
)
from ..models.create_marketplace_item_labels_response import CreateMarketplaceItemLabelsResponse
from ..models.enums.date_range_filter import DateRangeFilterOrStr
from ..models.enums.label_type import LabelTypeOrStr
from ..models.enums.page_type import PageTypeOrStr
from ..models.enums.program1 import Program1OrStr
from ..models.enums.shipment_status import ShipmentStatusOrStr
from ..models.enums.shipments_query_type import ShipmentsQueryTypeOrStr
from ..models.generate_delivery_window_options_response import GenerateDeliveryWindowOptionsResponse
from ..models.generate_packing_options_response import GeneratePackingOptionsResponse
from ..models.generate_placement_options_request import (
    GeneratePlacementOptionsRequest,
    GeneratePlacementOptionsRequestDict,
)
from ..models.generate_placement_options_response import GeneratePlacementOptionsResponse
from ..models.generate_self_ship_appointment_slots_request import (
    GenerateSelfShipAppointmentSlotsRequest,
    GenerateSelfShipAppointmentSlotsRequestDict,
)
from ..models.generate_self_ship_appointment_slots_response import GenerateSelfShipAppointmentSlotsResponse
from ..models.generate_shipment_content_update_previews_request import (
    GenerateShipmentContentUpdatePreviewsRequest,
    GenerateShipmentContentUpdatePreviewsRequestDict,
)
from ..models.generate_shipment_content_update_previews_response import GenerateShipmentContentUpdatePreviewsResponse
from ..models.generate_transportation_options_request import (
    GenerateTransportationOptionsRequest,
    GenerateTransportationOptionsRequestDict,
)
from ..models.generate_transportation_options_response import GenerateTransportationOptionsResponse
from ..models.get_bill_of_lading_response import GetBillOfLadingResponse
from ..models.get_delivery_challan_document_response import GetDeliveryChallanDocumentResponse
from ..models.get_item_eligibility_preview_response import GetItemEligibilityPreviewResponse
from ..models.get_labels_response import GetLabelsResponse
from ..models.get_prep_instructions_response import GetPrepInstructionsResponse
from ..models.get_self_ship_appointment_slots_response import GetSelfShipAppointmentSlotsResponse
from ..models.get_shipment_items_by_shipment_id_response import GetShipmentItemsByShipmentIdResponse
from ..models.get_shipment_items_response import GetShipmentItemsResponse
from ..models.get_shipments_response import GetShipmentsResponse
from ..models.inbound_plan import InboundPlan
from ..models.list_delivery_window_options_response import ListDeliveryWindowOptionsResponse
from ..models.list_inbound_plan_boxes_response import ListInboundPlanBoxesResponse
from ..models.list_inbound_plan_items_response import ListInboundPlanItemsResponse
from ..models.list_inbound_plan_pallets_response import ListInboundPlanPalletsResponse
from ..models.list_inbound_plans_response import ListInboundPlansResponse
from ..models.list_item_compliance_details_response import ListItemComplianceDetailsResponse
from ..models.list_packing_group_boxes_response import ListPackingGroupBoxesResponse
from ..models.list_packing_group_items_response import ListPackingGroupItemsResponse
from ..models.list_packing_options_response import ListPackingOptionsResponse
from ..models.list_placement_options_response import ListPlacementOptionsResponse
from ..models.list_prep_details_response import ListPrepDetailsResponse
from ..models.list_shipment_boxes_response import ListShipmentBoxesResponse
from ..models.list_shipment_content_update_previews_response import ListShipmentContentUpdatePreviewsResponse
from ..models.list_shipment_items_response import ListShipmentItemsResponse
from ..models.list_shipment_pallets_response import ListShipmentPalletsResponse
from ..models.list_transportation_options_response import ListTransportationOptionsResponse
from ..models.schedule_self_ship_appointment_request import (
    ScheduleSelfShipAppointmentRequest,
    ScheduleSelfShipAppointmentRequestDict,
)
from ..models.schedule_self_ship_appointment_response import ScheduleSelfShipAppointmentResponse
from ..models.set_packing_information_request import SetPackingInformationRequest, SetPackingInformationRequestDict
from ..models.set_packing_information_response import SetPackingInformationResponse
from ..models.set_prep_details_request import SetPrepDetailsRequest, SetPrepDetailsRequestDict
from ..models.set_prep_details_response import SetPrepDetailsResponse
from ..models.update_inbound_plan_name_request import UpdateInboundPlanNameRequest, UpdateInboundPlanNameRequestDict
from ..models.update_item_compliance_details_request import (
    UpdateItemComplianceDetailsRequest,
    UpdateItemComplianceDetailsRequestDict,
)
from ..models.update_item_compliance_details_response import UpdateItemComplianceDetailsResponse
from ..models.update_shipment_name_request import UpdateShipmentNameRequest, UpdateShipmentNameRequestDict
from ..models.update_shipment_source_address_request import (
    UpdateShipmentSourceAddressRequest,
    UpdateShipmentSourceAddressRequestDict,
)
from ..models.update_shipment_source_address_response import UpdateShipmentSourceAddressResponse
from ..models.update_shipment_tracking_details_request import (
    UpdateShipmentTrackingDetailsRequest,
    UpdateShipmentTrackingDetailsRequestDict,
)
from ..models.update_shipment_tracking_details_response import UpdateShipmentTrackingDetailsResponse
from ..server.server import Server


class WfsInbound:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WfsInboundWithRawResponse(client, server, auth)

    def cancel_inbound_plan(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Cancels an inbound plan when its current status allows cancellation.

        Args:
            plan_id: Unique identifier of the inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.cancel_inbound_plan(plan_id, request_options=request_options))

    def cancel_self_ship_appointment(
        self,
        plan_id: str,
        shipment_id: str,
        body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelSelfShipAppointmentResponse:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.cancel_self_ship_appointment(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def confirm_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        delivery_window_option_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConfirmDeliveryWindowOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to confirm the delivery window option for.
            delivery_window_option_id: The ID of the delivery window option to be confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_delivery_window_options(
                plan_id, shipment_id, delivery_window_option_id, request_options=request_options
            ),
        )

    def confirm_packing_option(
        self, plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConfirmPackingOptionResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_option_id: Identifier of a packing option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_packing_option(plan_id, packing_option_id, request_options=request_options)
        )

    def confirm_placement_option(
        self, plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConfirmPlacementOptionResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            placement_option_id: The identifier of a placement option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_placement_option(
                plan_id, placement_option_id, request_options=request_options
            ),
        )

    def confirm_shipment_content_update_preview(
        self,
        plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConfirmShipmentContentUpdatePreviewResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_shipment_content_update_preview(
                plan_id, shipment_id, content_update_preview_id, request_options=request_options
            ),
        )

    def confirm_transportation_options(
        self,
        plan_id: str,
        body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConfirmTransportationOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_transportation_options(plan_id, body, request_options=request_options)
        )

    def create_inbound_plan(
        self,
        body: CreateInboundPlanRequest | CreateInboundPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInboundPlanResponse:
        """Creates an inbound plan for items to be shipped to Walmart fulfillment centers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.create_inbound_plan(body, request_options=request_options))

    def create_marketplace_item_labels(
        self,
        body: CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateMarketplaceItemLabelsResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.create_marketplace_item_labels(body, request_options=request_options))

    def generate_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        scac: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateDeliveryWindowOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to generate delivery window options for.
            scac: Walmart extension (not in SP-API). Standard Carrier Alpha Code of the carrier delivering the shipment,
                case preserved. Supplying it generates drop trailer windows; omitting it generates live unload windows.
                The delivery type chosen here is kept when a generated window is confirmed. Carrier existence and drop
                trailer eligibility are validated when the window is confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.generate_delivery_window_options(
                plan_id, shipment_id, scac=scac, request_options=request_options
            ),
        )

    def generate_packing_options(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GeneratePackingOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.generate_packing_options(plan_id, request_options=request_options))

    def generate_placement_options(
        self,
        plan_id: str,
        body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GeneratePlacementOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.generate_placement_options(plan_id, body, request_options=request_options)
        )

    def generate_self_ship_appointment_slots(
        self,
        plan_id: str,
        shipment_id: str,
        body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateSelfShipAppointmentSlotsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.generate_self_ship_appointment_slots(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def generate_shipment_content_update_previews(
        self,
        plan_id: str,
        shipment_id: str,
        body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateShipmentContentUpdatePreviewsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.generate_shipment_content_update_previews(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def generate_transportation_options(
        self,
        plan_id: str,
        body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateTransportationOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.generate_transportation_options(plan_id, body, request_options=request_options)
        )

    def get_bill_of_lading(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetBillOfLadingResponse:
        """Send a ``GET`` request.

        Args:
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.get_bill_of_lading(shipment_id, request_options=request_options))

    def get_delivery_challan_document(
        self, plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetDeliveryChallanDocumentResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_delivery_challan_document(plan_id, shipment_id, request_options=request_options)
        )

    def get_inbound_operation_status(
        self, operation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommonInboundOperationStatus:
        """Retrieves the status of an inbound plan operation, such as creating or canceling a plan.

        Args:
            operation_id: Unique identifier for the operation.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_inbound_operation_status(operation_id, request_options=request_options)
        )

    def get_inbound_plan(self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None) -> InboundPlan:
        """Retrieves the details of an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.get_inbound_plan(plan_id, request_options=request_options))

    def get_item_eligibility_preview(
        self,
        item_id: str,
        program: Program1OrStr,
        *,
        marketplace_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetItemEligibilityPreviewResponse:
        """Checks whether an item is eligible for the specified program.

        Args:
            item_id: Walmart item identifier for which to retrieve an eligibility preview.
            program: Program for which to evaluate item eligibility.
            marketplace_ids: Marketplace identifier to use when determining item eligibility.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Eligibility preview resolved successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_item_eligibility_preview(
                item_id, program, marketplace_ids=marketplace_ids, request_options=request_options
            ),
        )

    def get_labels(
        self,
        shipment_id: str,
        page_type: PageTypeOrStr,
        label_type: LabelTypeOrStr,
        *,
        page_size: int | None = None,
        page_start_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetLabelsResponse:
        """Returns package/pallet labels for faster and more accurate shipment processing at the Walmart fulfillment
        center.

        Args:
            shipment_id: Identifier of a shipment.
            page_type: The page size/format to use for label printing (upstream ``PageType``). Determines the physical
                layout of the generated label file.
            label_type: The type of label to retrieve (upstream ``LabelType``). ``UNIQUE`` is a carrier-assigned unique
                shipping label (PARCEL shipments only); ``BARCODE_2D`` is a 2D barcode receiving/box label; ``PALLET``
                is a pallet receiving label (non-PARCEL modes only).
            page_size: The page size for paginating through the total packages' labels. Maximum 1000 (upstream
                ``PageSize``, default 100).
            page_start_index: The zero-based page start index for paginating through the total packages' labels
                (upstream ``PageStartIndex``, default 0).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_labels(
                shipment_id,
                page_type,
                label_type,
                page_size=page_size,
                page_start_index=page_start_index,
                request_options=request_options,
            ),
        )

    def get_prep_instructions(
        self,
        ship_to_country_code: str,
        *,
        seller_sku_list: list[str] | None = None,
        asin_list: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPrepInstructionsResponse:
        """Send a ``GET`` request.

        Args:
            ship_to_country_code: The two-letter country code of the destination the item(s) will ship to.
            seller_sku_list: A list of seller SKUs to retrieve prep instructions for.
            asin_list: A list of ASINs to retrieve prep instructions for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_prep_instructions(
                ship_to_country_code,
                seller_sku_list=seller_sku_list,
                asin_list=asin_list,
                request_options=request_options,
            ),
        )

    def get_self_ship_appointment_slots(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetSelfShipAppointmentSlotsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of self ship appointment slots to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_self_ship_appointment_slots(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def get_shipment(
        self, plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommonShipment:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.get_shipment(plan_id, shipment_id, request_options=request_options))

    def get_shipment_content_update_preview(
        self,
        plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommonContentUpdatePreview:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipment_content_update_preview(
                plan_id, shipment_id, content_update_preview_id, request_options=request_options
            ),
        )

    def get_shipment_items(
        self,
        *,
        date_range_filter: DateRangeFilterOrStr | None = None,
        date_range_value: str | None = None,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetShipmentItemsResponse:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike
            ``getShipmentItemsByShipmentId`` and ``listShipmentItems``, this op is NOT shipment- or plan-scoped -- it
            searches item rows across ALL of a seller's shipments, date- filtered. Field naming deliberately uses the
            Amazon SP-API-parity names ``sellerSku``/ ``fulfillmentNetworkSKU`` (per explicit mapping instructions)
            rather than the ``msku``/``fnsku`` shorthand its shipment-/plan-scoped siblings settled on -- this is a
            genuinely new v4 response shape with no naming precedent of its own to preserve.

        Args:
            date_range_filter: Which date field ``dateRangeValue`` filters on (upstream ``dateRangeFilter``).
            date_range_value: ISO 8601 datetime paired with ``dateRangeFilter`` (upstream ``dateRangeValue``).
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch the next page of a previous ``getShipmentItems`` query. Pass the value of
                ``pagination.nextToken`` from a previous response. Forwarded upstream as ``nextToken`` (already
                lowerCamelCase on this op, unlike ``getShipments``' ``NextToken``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipment_items(
                date_range_filter=date_range_filter,
                date_range_value=date_range_value,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def get_shipment_items_by_shipment_id(
        self,
        shipment_id: str,
        *,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetShipmentItemsByShipmentIdResponse:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike
            listShipmentItems, this op is NOT inboundPlan-scoped -- it reads a CONFIRMED shipment directly by shipmentId
            (the upstream shipmentRefId / externalReferenceId), with no draft-lookup fallback.

        Args:
            shipment_id: Identifier of a confirmed shipment (shipmentRefId / externalReferenceId).
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results. Pass the
                value of ``pagination.nextToken`` from a previous response to fetch the next page. Upstream Inbound
                Order Workflow returns this cursor as ``NextToken`` in the response payload ; it is mapped through
                unchanged into ``pagination.nextToken`` here -- the request-side parameter name stays
                ``paginationToken`` for consistency with every other list operation in this API.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipment_items_by_shipment_id(
                shipment_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def get_shipments(
        self,
        query_type: ShipmentsQueryTypeOrStr,
        *,
        shipment_id_list: list[str] | None = None,
        shipment_status_list: list[ShipmentStatusOrStr] | None = None,
        last_updated_after: str | None = None,
        last_updated_before: str | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetShipmentsResponse:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike every shipment op
            above, this is NOT plan- or shipment-scoped -- it searches across ALL of a seller's shipments. Behavior is
            driven by ``queryType``:
          - ``SHIPMENT``: requires exactly one of ``shipmentIdList`` or ``shipmentStatusList`` (never
            both, never neither -- , tightened to match an upstream spec update).
          - ``DATE_RANGE``: requires ``lastUpdatedAfter`` (``lastUpdatedBefore`` is optional);
            ``shipmentStatusList`` may be supplied as an additional filter.
          - ``NEXT_TOKEN``: requires ``paginationToken`` (the value returned in a previous response's
            ``pagination.nextToken``) to fetch the next page of the SAME query; resend the original
            ``shipmentIdList``/``shipmentStatusList``/``lastUpdatedAfter``/``lastUpdatedBefore`` filters,
            since ``paginationToken`` only encodes the paging cursor, not the filters themselves.

        Args:
            query_type: Determines which combination of filters below is required (upstream ``QueryType``).
            shipment_id_list: Shipment identifiers (external reference ids) to filter by. When ``queryType=SHIPMENT``,
                exactly one of ``shipmentIdList``/``shipmentStatusList`` is required -- never both, never neither .
                Maximum 999 entries (upstream ``ShipmentIdList``).
            shipment_status_list: Shipment statuses to filter by (upstream ``ShipmentStatusList``; same vocabulary as
                ``getShipment``'s free-string ``status`` field, minus ``UNCONFIRMED``, which upstream documents as never
                applying to a confirmed shipment). When ``queryType=SHIPMENT``, exactly one of
                ``shipmentIdList``/``shipmentStatusList`` is required -- never both, never neither ; for
                ``queryType=DATE_RANGE`` it remains an optional additional filter.
            last_updated_after: Only return shipments last updated at or after this date, ISO 8601 datetime. Required
                when ``queryType=DATE_RANGE`` (upstream ``LastUpdatedAfter``).
            last_updated_before: Only return shipments last updated at or before this date, ISO 8601 datetime. Optional
                when ``queryType=DATE_RANGE``, defaults to now (upstream ``LastUpdatedBefore``).
            pagination_token: A token to fetch the next page of a previous ``getShipments`` query. Pass the value of
                ``pagination.nextToken`` from a previous response. Required when ``queryType=NEXT_TOKEN``. Forwarded
                upstream as ``NextToken``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipments(
                query_type,
                shipment_id_list=shipment_id_list,
                shipment_status_list=shipment_status_list,
                last_updated_after=last_updated_after,
                last_updated_before=last_updated_before,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDeliveryWindowOptionsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to get delivery window options for.
            page_size: The number of delivery window options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_delivery_window_options(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_inbound_plan_boxes(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanBoxesResponse:
        """Retrieves a paginated list of shipping boxes included in an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of boxes to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_inbound_plan_boxes(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def list_inbound_plan_items(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanItemsResponse:
        """Retrieves a paginated list of items in an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of items to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_inbound_plan_items(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def list_inbound_plan_pallets(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanPalletsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of pallets to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_inbound_plan_pallets(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def list_inbound_plans(
        self,
        *,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        status: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlansResponse:
        """Retrieves a paginated list of inbound plans. Filter by status, sort the results, and use ``paginationToken``
        to retrieve subsequent pages.

        Args:
            page_size: Maximum number of inbound plans to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            status: Filters results by inbound plan status. Supported values are ``ACTIVE``, ``VOIDED``, ``SHIPPED``,
                and ``ERRORED``.
            sort_by: Field used to sort the returned inbound plans.
            sort_order: Sort direction for the returned inbound plans. Supported values are ``ASC`` and ``DESC``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_inbound_plans(
                page_size=page_size,
                pagination_token=pagination_token,
                status=status,
                sort_by=sort_by,
                sort_order=sort_order,
                request_options=request_options,
            ),
        )

    def list_item_compliance_details(
        self, mskus: list[str], marketplace_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListItemComplianceDetailsResponse:
        """Send a ``GET`` request.

        Args:
            mskus: A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_item_compliance_details(mskus, marketplace_id, request_options=request_options)
        )

    def list_packing_group_boxes(
        self,
        plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPackingGroupBoxesResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_packing_group_boxes(
                plan_id,
                packing_group_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_packing_group_items(
        self,
        plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPackingGroupItemsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_packing_group_items(
                plan_id,
                packing_group_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_packing_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPackingOptionsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of packing options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_packing_options(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def list_placement_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPlacementOptionsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of placement options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_placement_options(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def list_prep_details(
        self, marketplace_id: str, mskus: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ListPrepDetailsResponse:
        """Send a ``GET`` request.

        Args:
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            mskus: A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.list_prep_details(marketplace_id, mskus, request_options=request_options))

    def list_shipment_boxes(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentBoxesResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_shipment_boxes(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_shipment_content_update_previews(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentContentUpdatePreviewsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of content update previews to return.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_shipment_content_update_previews(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_shipment_items(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentItemsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_shipment_items(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_shipment_pallets(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentPalletsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_shipment_pallets(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_transportation_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        placement_option_id: str | None = None,
        shipment_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTransportationOptionsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of transportation options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            placement_option_id: The placement option to get transportation options for. Either ``placementOptionId`` or
                ``shipmentId`` must be specified.
            shipment_id: The shipment to get transportation options for. Either ``placementOptionId`` or ``shipmentId``
                must be specified.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.list_transportation_options(
                plan_id,
                page_size=page_size,
                pagination_token=pagination_token,
                placement_option_id=placement_option_id,
                shipment_id=shipment_id,
                request_options=request_options,
            ),
        )

    def schedule_self_ship_appointment(
        self,
        plan_id: str,
        shipment_id: str,
        slot_id: str,
        body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduleSelfShipAppointmentResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            slot_id: An identifier to a self-ship appointment slot.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.schedule_self_ship_appointment(
                plan_id, shipment_id, slot_id, body, request_options=request_options
            ),
        )

    def set_packing_information(
        self,
        plan_id: str,
        body: SetPackingInformationRequest | SetPackingInformationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SetPackingInformationResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.set_packing_information(plan_id, body, request_options=request_options))

    def set_prep_details(
        self,
        body: SetPrepDetailsRequest | SetPrepDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SetPrepDetailsResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.set_prep_details(body, request_options=request_options))

    def update_inbound_plan_name(
        self,
        plan_id: str,
        body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the name of an existing inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No content — name updated successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(self._with_raw_response.update_inbound_plan_name(plan_id, body, request_options=request_options))

    def update_item_compliance_details(
        self,
        marketplace_id: str,
        body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateItemComplianceDetailsResponse:
        """Send a ``PUT`` request.

        Args:
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.update_item_compliance_details(
                marketplace_id, body, request_options=request_options
            ),
        )

    def update_shipment_name(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No content — name updated successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.update_shipment_name(plan_id, shipment_id, body, request_options=request_options)
        )

    def update_shipment_source_address(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateShipmentSourceAddressResponse:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.update_shipment_source_address(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def update_shipment_tracking_details(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateShipmentTrackingDetailsResponse:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            self._with_raw_response.update_shipment_tracking_details(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> WfsInboundWithRawResponse:
        return self._with_raw_response


class AsyncWfsInbound:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWfsInboundWithRawResponse(client, server, auth)

    async def cancel_inbound_plan(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Cancels an inbound plan when its current status allows cancellation.

        Args:
            plan_id: Unique identifier of the inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(await self._with_raw_response.cancel_inbound_plan(plan_id, request_options=request_options))

    async def cancel_self_ship_appointment(
        self,
        plan_id: str,
        shipment_id: str,
        body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelSelfShipAppointmentResponse:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_self_ship_appointment(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def confirm_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        delivery_window_option_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConfirmDeliveryWindowOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to confirm the delivery window option for.
            delivery_window_option_id: The ID of the delivery window option to be confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_delivery_window_options(
                plan_id, shipment_id, delivery_window_option_id, request_options=request_options
            ),
        )

    async def confirm_packing_option(
        self, plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConfirmPackingOptionResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_option_id: Identifier of a packing option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_packing_option(
                plan_id, packing_option_id, request_options=request_options
            ),
        )

    async def confirm_placement_option(
        self, plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConfirmPlacementOptionResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            placement_option_id: The identifier of a placement option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_placement_option(
                plan_id, placement_option_id, request_options=request_options
            ),
        )

    async def confirm_shipment_content_update_preview(
        self,
        plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConfirmShipmentContentUpdatePreviewResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_shipment_content_update_preview(
                plan_id, shipment_id, content_update_preview_id, request_options=request_options
            ),
        )

    async def confirm_transportation_options(
        self,
        plan_id: str,
        body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConfirmTransportationOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_transportation_options(plan_id, body, request_options=request_options)
        )

    async def create_inbound_plan(
        self,
        body: CreateInboundPlanRequest | CreateInboundPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInboundPlanResponse:
        """Creates an inbound plan for items to be shipped to Walmart fulfillment centers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(await self._with_raw_response.create_inbound_plan(body, request_options=request_options))

    async def create_marketplace_item_labels(
        self,
        body: CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateMarketplaceItemLabelsResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.create_marketplace_item_labels(body, request_options=request_options)
        )

    async def generate_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        scac: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateDeliveryWindowOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to generate delivery window options for.
            scac: Walmart extension (not in SP-API). Standard Carrier Alpha Code of the carrier delivering the shipment,
                case preserved. Supplying it generates drop trailer windows; omitting it generates live unload windows.
                The delivery type chosen here is kept when a generated window is confirmed. Carrier existence and drop
                trailer eligibility are validated when the window is confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_delivery_window_options(
                plan_id, shipment_id, scac=scac, request_options=request_options
            ),
        )

    async def generate_packing_options(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GeneratePackingOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(await self._with_raw_response.generate_packing_options(plan_id, request_options=request_options))

    async def generate_placement_options(
        self,
        plan_id: str,
        body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GeneratePlacementOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_placement_options(plan_id, body, request_options=request_options)
        )

    async def generate_self_ship_appointment_slots(
        self,
        plan_id: str,
        shipment_id: str,
        body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateSelfShipAppointmentSlotsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_self_ship_appointment_slots(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def generate_shipment_content_update_previews(
        self,
        plan_id: str,
        shipment_id: str,
        body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateShipmentContentUpdatePreviewsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_shipment_content_update_previews(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def generate_transportation_options(
        self,
        plan_id: str,
        body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenerateTransportationOptionsResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_transportation_options(
                plan_id, body, request_options=request_options
            ),
        )

    async def get_bill_of_lading(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetBillOfLadingResponse:
        """Send a ``GET`` request.

        Args:
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(await self._with_raw_response.get_bill_of_lading(shipment_id, request_options=request_options))

    async def get_delivery_challan_document(
        self, plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetDeliveryChallanDocumentResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_delivery_challan_document(
                plan_id, shipment_id, request_options=request_options
            ),
        )

    async def get_inbound_operation_status(
        self, operation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommonInboundOperationStatus:
        """Retrieves the status of an inbound plan operation, such as creating or canceling a plan.

        Args:
            operation_id: Unique identifier for the operation.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_inbound_operation_status(operation_id, request_options=request_options)
        )

    async def get_inbound_plan(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InboundPlan:
        """Retrieves the details of an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(await self._with_raw_response.get_inbound_plan(plan_id, request_options=request_options))

    async def get_item_eligibility_preview(
        self,
        item_id: str,
        program: Program1OrStr,
        *,
        marketplace_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetItemEligibilityPreviewResponse:
        """Checks whether an item is eligible for the specified program.

        Args:
            item_id: Walmart item identifier for which to retrieve an eligibility preview.
            program: Program for which to evaluate item eligibility.
            marketplace_ids: Marketplace identifier to use when determining item eligibility.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Eligibility preview resolved successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_item_eligibility_preview(
                item_id, program, marketplace_ids=marketplace_ids, request_options=request_options
            ),
        )

    async def get_labels(
        self,
        shipment_id: str,
        page_type: PageTypeOrStr,
        label_type: LabelTypeOrStr,
        *,
        page_size: int | None = None,
        page_start_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetLabelsResponse:
        """Returns package/pallet labels for faster and more accurate shipment processing at the Walmart fulfillment
        center.

        Args:
            shipment_id: Identifier of a shipment.
            page_type: The page size/format to use for label printing (upstream ``PageType``). Determines the physical
                layout of the generated label file.
            label_type: The type of label to retrieve (upstream ``LabelType``). ``UNIQUE`` is a carrier-assigned unique
                shipping label (PARCEL shipments only); ``BARCODE_2D`` is a 2D barcode receiving/box label; ``PALLET``
                is a pallet receiving label (non-PARCEL modes only).
            page_size: The page size for paginating through the total packages' labels. Maximum 1000 (upstream
                ``PageSize``, default 100).
            page_start_index: The zero-based page start index for paginating through the total packages' labels
                (upstream ``PageStartIndex``, default 0).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_labels(
                shipment_id,
                page_type,
                label_type,
                page_size=page_size,
                page_start_index=page_start_index,
                request_options=request_options,
            ),
        )

    async def get_prep_instructions(
        self,
        ship_to_country_code: str,
        *,
        seller_sku_list: list[str] | None = None,
        asin_list: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPrepInstructionsResponse:
        """Send a ``GET`` request.

        Args:
            ship_to_country_code: The two-letter country code of the destination the item(s) will ship to.
            seller_sku_list: A list of seller SKUs to retrieve prep instructions for.
            asin_list: A list of ASINs to retrieve prep instructions for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_prep_instructions(
                ship_to_country_code,
                seller_sku_list=seller_sku_list,
                asin_list=asin_list,
                request_options=request_options,
            ),
        )

    async def get_self_ship_appointment_slots(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetSelfShipAppointmentSlotsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of self ship appointment slots to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_self_ship_appointment_slots(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def get_shipment(
        self, plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommonShipment:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(await self._with_raw_response.get_shipment(plan_id, shipment_id, request_options=request_options))

    async def get_shipment_content_update_preview(
        self,
        plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommonContentUpdatePreview:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipment_content_update_preview(
                plan_id, shipment_id, content_update_preview_id, request_options=request_options
            ),
        )

    async def get_shipment_items(
        self,
        *,
        date_range_filter: DateRangeFilterOrStr | None = None,
        date_range_value: str | None = None,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetShipmentItemsResponse:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike
            ``getShipmentItemsByShipmentId`` and ``listShipmentItems``, this op is NOT shipment- or plan-scoped -- it
            searches item rows across ALL of a seller's shipments, date- filtered. Field naming deliberately uses the
            Amazon SP-API-parity names ``sellerSku``/ ``fulfillmentNetworkSKU`` (per explicit mapping instructions)
            rather than the ``msku``/``fnsku`` shorthand its shipment-/plan-scoped siblings settled on -- this is a
            genuinely new v4 response shape with no naming precedent of its own to preserve.

        Args:
            date_range_filter: Which date field ``dateRangeValue`` filters on (upstream ``dateRangeFilter``).
            date_range_value: ISO 8601 datetime paired with ``dateRangeFilter`` (upstream ``dateRangeValue``).
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch the next page of a previous ``getShipmentItems`` query. Pass the value of
                ``pagination.nextToken`` from a previous response. Forwarded upstream as ``nextToken`` (already
                lowerCamelCase on this op, unlike ``getShipments``' ``NextToken``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipment_items(
                date_range_filter=date_range_filter,
                date_range_value=date_range_value,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def get_shipment_items_by_shipment_id(
        self,
        shipment_id: str,
        *,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetShipmentItemsByShipmentIdResponse:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike
            listShipmentItems, this op is NOT inboundPlan-scoped -- it reads a CONFIRMED shipment directly by shipmentId
            (the upstream shipmentRefId / externalReferenceId), with no draft-lookup fallback.

        Args:
            shipment_id: Identifier of a confirmed shipment (shipmentRefId / externalReferenceId).
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results. Pass the
                value of ``pagination.nextToken`` from a previous response to fetch the next page. Upstream Inbound
                Order Workflow returns this cursor as ``NextToken`` in the response payload ; it is mapped through
                unchanged into ``pagination.nextToken`` here -- the request-side parameter name stays
                ``paginationToken`` for consistency with every other list operation in this API.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipment_items_by_shipment_id(
                shipment_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def get_shipments(
        self,
        query_type: ShipmentsQueryTypeOrStr,
        *,
        shipment_id_list: list[str] | None = None,
        shipment_status_list: list[ShipmentStatusOrStr] | None = None,
        last_updated_after: str | None = None,
        last_updated_before: str | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetShipmentsResponse:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike every shipment op
            above, this is NOT plan- or shipment-scoped -- it searches across ALL of a seller's shipments. Behavior is
            driven by ``queryType``:
          - ``SHIPMENT``: requires exactly one of ``shipmentIdList`` or ``shipmentStatusList`` (never
            both, never neither -- , tightened to match an upstream spec update).
          - ``DATE_RANGE``: requires ``lastUpdatedAfter`` (``lastUpdatedBefore`` is optional);
            ``shipmentStatusList`` may be supplied as an additional filter.
          - ``NEXT_TOKEN``: requires ``paginationToken`` (the value returned in a previous response's
            ``pagination.nextToken``) to fetch the next page of the SAME query; resend the original
            ``shipmentIdList``/``shipmentStatusList``/``lastUpdatedAfter``/``lastUpdatedBefore`` filters,
            since ``paginationToken`` only encodes the paging cursor, not the filters themselves.

        Args:
            query_type: Determines which combination of filters below is required (upstream ``QueryType``).
            shipment_id_list: Shipment identifiers (external reference ids) to filter by. When ``queryType=SHIPMENT``,
                exactly one of ``shipmentIdList``/``shipmentStatusList`` is required -- never both, never neither .
                Maximum 999 entries (upstream ``ShipmentIdList``).
            shipment_status_list: Shipment statuses to filter by (upstream ``ShipmentStatusList``; same vocabulary as
                ``getShipment``'s free-string ``status`` field, minus ``UNCONFIRMED``, which upstream documents as never
                applying to a confirmed shipment). When ``queryType=SHIPMENT``, exactly one of
                ``shipmentIdList``/``shipmentStatusList`` is required -- never both, never neither ; for
                ``queryType=DATE_RANGE`` it remains an optional additional filter.
            last_updated_after: Only return shipments last updated at or after this date, ISO 8601 datetime. Required
                when ``queryType=DATE_RANGE`` (upstream ``LastUpdatedAfter``).
            last_updated_before: Only return shipments last updated at or before this date, ISO 8601 datetime. Optional
                when ``queryType=DATE_RANGE``, defaults to now (upstream ``LastUpdatedBefore``).
            pagination_token: A token to fetch the next page of a previous ``getShipments`` query. Pass the value of
                ``pagination.nextToken`` from a previous response. Required when ``queryType=NEXT_TOKEN``. Forwarded
                upstream as ``NextToken``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipments(
                query_type,
                shipment_id_list=shipment_id_list,
                shipment_status_list=shipment_status_list,
                last_updated_after=last_updated_after,
                last_updated_before=last_updated_before,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDeliveryWindowOptionsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to get delivery window options for.
            page_size: The number of delivery window options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_delivery_window_options(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_inbound_plan_boxes(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanBoxesResponse:
        """Retrieves a paginated list of shipping boxes included in an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of boxes to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_inbound_plan_boxes(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def list_inbound_plan_items(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanItemsResponse:
        """Retrieves a paginated list of items in an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of items to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_inbound_plan_items(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def list_inbound_plan_pallets(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanPalletsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of pallets to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_inbound_plan_pallets(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def list_inbound_plans(
        self,
        *,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        status: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlansResponse:
        """Retrieves a paginated list of inbound plans. Filter by status, sort the results, and use ``paginationToken``
        to retrieve subsequent pages.

        Args:
            page_size: Maximum number of inbound plans to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            status: Filters results by inbound plan status. Supported values are ``ACTIVE``, ``VOIDED``, ``SHIPPED``,
                and ``ERRORED``.
            sort_by: Field used to sort the returned inbound plans.
            sort_order: Sort direction for the returned inbound plans. Supported values are ``ASC`` and ``DESC``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_inbound_plans(
                page_size=page_size,
                pagination_token=pagination_token,
                status=status,
                sort_by=sort_by,
                sort_order=sort_order,
                request_options=request_options,
            ),
        )

    async def list_item_compliance_details(
        self, mskus: list[str], marketplace_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListItemComplianceDetailsResponse:
        """Send a ``GET`` request.

        Args:
            mskus: A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_item_compliance_details(
                mskus, marketplace_id, request_options=request_options
            ),
        )

    async def list_packing_group_boxes(
        self,
        plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPackingGroupBoxesResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_packing_group_boxes(
                plan_id,
                packing_group_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_packing_group_items(
        self,
        plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPackingGroupItemsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_packing_group_items(
                plan_id,
                packing_group_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_packing_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPackingOptionsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of packing options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_packing_options(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def list_placement_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPlacementOptionsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of placement options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_placement_options(
                plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def list_prep_details(
        self, marketplace_id: str, mskus: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ListPrepDetailsResponse:
        """Send a ``GET`` request.

        Args:
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            mskus: A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_prep_details(marketplace_id, mskus, request_options=request_options)
        )

    async def list_shipment_boxes(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentBoxesResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_shipment_boxes(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_shipment_content_update_previews(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentContentUpdatePreviewsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of content update previews to return.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_shipment_content_update_previews(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_shipment_items(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentItemsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_shipment_items(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_shipment_pallets(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentPalletsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_shipment_pallets(
                plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_transportation_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        placement_option_id: str | None = None,
        shipment_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTransportationOptionsResponse:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of transportation options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            placement_option_id: The placement option to get transportation options for. Either ``placementOptionId`` or
                ``shipmentId`` must be specified.
            shipment_id: The shipment to get transportation options for. Either ``placementOptionId`` or ``shipmentId``
                must be specified.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.list_transportation_options(
                plan_id,
                page_size=page_size,
                pagination_token=pagination_token,
                placement_option_id=placement_option_id,
                shipment_id=shipment_id,
                request_options=request_options,
            ),
        )

    async def schedule_self_ship_appointment(
        self,
        plan_id: str,
        shipment_id: str,
        slot_id: str,
        body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduleSelfShipAppointmentResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            slot_id: An identifier to a self-ship appointment slot.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.schedule_self_ship_appointment(
                plan_id, shipment_id, slot_id, body, request_options=request_options
            ),
        )

    async def set_packing_information(
        self,
        plan_id: str,
        body: SetPackingInformationRequest | SetPackingInformationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SetPackingInformationResponse:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.set_packing_information(plan_id, body, request_options=request_options)
        )

    async def set_prep_details(
        self,
        body: SetPrepDetailsRequest | SetPrepDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SetPrepDetailsResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(await self._with_raw_response.set_prep_details(body, request_options=request_options))

    async def update_inbound_plan_name(
        self,
        plan_id: str,
        body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the name of an existing inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No content — name updated successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.update_inbound_plan_name(plan_id, body, request_options=request_options)
        )

    async def update_item_compliance_details(
        self,
        marketplace_id: str,
        body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateItemComplianceDetailsResponse:
        """Send a ``PUT`` request.

        Args:
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.update_item_compliance_details(
                marketplace_id, body, request_options=request_options
            ),
        )

    async def update_shipment_name(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No content — name updated successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.update_shipment_name(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def update_shipment_source_address(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateShipmentSourceAddressResponse:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.update_shipment_source_address(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def update_shipment_tracking_details(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateShipmentTrackingDetailsResponse:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorListFulfillmentInboundPlans | RawError``."""
        return unwrap(
            await self._with_raw_response.update_shipment_tracking_details(
                plan_id, shipment_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWfsInboundWithRawResponse:
        return self._with_raw_response


class WfsInboundWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_inbound_plan(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, CancelInboundPlanErrorBody]:
        """Cancels an inbound plan when its current status allows cancellation.

        Args:
            plan_id: Unique identifier of the inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/cancel"),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=cancel_inbound_plan_error_mapper,
            request_options=request_options,
        )

    def cancel_self_ship_appointment(
        self,
        plan_id: str,
        shipment_id: str,
        body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelSelfShipAppointmentResponse, CancelSelfShipAppointmentErrorBody]:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-cancel"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelSelfShipAppointmentResponse],
            error_mapper=cancel_self_ship_appointment_error_mapper,
            request_options=request_options,
        )

    def confirm_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        delivery_window_option_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConfirmDeliveryWindowOptionsResponse, ConfirmDeliveryWindowOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to confirm the delivery window option for.
            delivery_window_option_id: The ID of the delivery window option to be confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options/{delivery-window-option-id}/confirm",
            ),
            path_params=[
                param[str]("plan-id", plan_id),
                param[str]("shipment-id", shipment_id),
                param[str]("delivery-window-option-id", delivery_window_option_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ConfirmDeliveryWindowOptionsResponse],
            error_mapper=confirm_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    def confirm_packing_option(
        self, plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConfirmPackingOptionResponse, ConfirmPackingOptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_option_id: Identifier of a packing option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/packing-options/{packing-option-id}/confirm"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("packing-option-id", packing_option_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ConfirmPackingOptionResponse],
            error_mapper=confirm_packing_option_error_mapper,
            request_options=request_options,
        )

    def confirm_placement_option(
        self, plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConfirmPlacementOptionResponse, ConfirmPlacementOptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            placement_option_id: The identifier of a placement option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/placement-options/{placement-option-id}/confirm"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("placement-option-id", placement_option_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ConfirmPlacementOptionResponse],
            error_mapper=confirm_placement_option_error_mapper,
            request_options=request_options,
        )

    def confirm_shipment_content_update_preview(
        self,
        plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConfirmShipmentContentUpdatePreviewResponse, ConfirmShipmentContentUpdatePreviewErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews/{content-update-preview-id}/confirm",
            ),
            path_params=[
                param[str]("plan-id", plan_id),
                param[str]("shipment-id", shipment_id),
                param[str]("content-update-preview-id", content_update_preview_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ConfirmShipmentContentUpdatePreviewResponse],
            error_mapper=confirm_shipment_content_update_preview_error_mapper,
            request_options=request_options,
        )

    def confirm_transportation_options(
        self,
        plan_id: str,
        body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConfirmTransportationOptionsResponse, ConfirmTransportationOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/transportation-options/confirm"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ConfirmTransportationOptionsResponse],
            error_mapper=confirm_transportation_options_error_mapper,
            request_options=request_options,
        )

    def create_inbound_plan(
        self,
        body: CreateInboundPlanRequest | CreateInboundPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInboundPlanResponse, CreateInboundPlanErrorBody]:
        """Creates an inbound plan for items to be shipped to Walmart fulfillment centers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateInboundPlanRequest | CreateInboundPlanRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateInboundPlanResponse],
            error_mapper=create_inbound_plan_error_mapper,
            request_options=request_options,
        )

    def create_marketplace_item_labels(
        self,
        body: CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateMarketplaceItemLabelsResponse, CreateMarketplaceItemLabelsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/labels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateMarketplaceItemLabelsResponse],
            error_mapper=create_marketplace_item_labels_error_mapper,
            request_options=request_options,
        )

    def generate_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        scac: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateDeliveryWindowOptionsResponse, GenerateDeliveryWindowOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to generate delivery window options for.
            scac: Walmart extension (not in SP-API). Standard Carrier Alpha Code of the carrier delivering the shipment,
                case preserved. Supplying it generates drop trailer windows; omitting it generates live unload windows.
                The delivery type chosen here is kept when a generated window is confirmed. Carrier existence and drop
                trailer eligibility are validated when the window is confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[param[str | None]("scac", scac)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GenerateDeliveryWindowOptionsResponse],
            error_mapper=generate_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    def generate_packing_options(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GeneratePackingOptionsResponse, GeneratePackingOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/packing-options"),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GeneratePackingOptionsResponse],
            error_mapper=generate_packing_options_error_mapper,
            request_options=request_options,
        )

    def generate_placement_options(
        self,
        plan_id: str,
        body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GeneratePlacementOptionsResponse, GeneratePlacementOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/placement-options"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GeneratePlacementOptionsResponse],
            error_mapper=generate_placement_options_error_mapper,
            request_options=request_options,
        )

    def generate_self_ship_appointment_slots(
        self,
        plan_id: str,
        shipment_id: str,
        body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateSelfShipAppointmentSlotsResponse, GenerateSelfShipAppointmentSlotsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GenerateSelfShipAppointmentSlotsResponse],
            error_mapper=generate_self_ship_appointment_slots_error_mapper,
            request_options=request_options,
        )

    def generate_shipment_content_update_previews(
        self,
        plan_id: str,
        shipment_id: str,
        body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateShipmentContentUpdatePreviewsResponse, GenerateShipmentContentUpdatePreviewsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict
            ](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GenerateShipmentContentUpdatePreviewsResponse],
            error_mapper=generate_shipment_content_update_previews_error_mapper,
            request_options=request_options,
        )

    def generate_transportation_options(
        self,
        plan_id: str,
        body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateTransportationOptionsResponse, GenerateTransportationOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/transportation-options"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GenerateTransportationOptionsResponse],
            error_mapper=generate_transportation_options_error_mapper,
            request_options=request_options,
        )

    def get_bill_of_lading(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetBillOfLadingResponse, GetBillOfLadingErrorBody]:
        """Send a ``GET`` request.

        Args:
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/shipments/{shipment-id}/bill-of-lading"
            ),
            path_params=[param[str]("shipment-id", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetBillOfLadingResponse],
            error_mapper=get_bill_of_lading_error_mapper,
            request_options=request_options,
        )

    def get_delivery_challan_document(
        self, plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetDeliveryChallanDocumentResponse, GetDeliveryChallanDocumentErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-challan-document"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetDeliveryChallanDocumentResponse],
            error_mapper=get_delivery_challan_document_error_mapper,
            request_options=request_options,
        )

    def get_inbound_operation_status(
        self, operation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommonInboundOperationStatus, GetInboundOperationStatusErrorBody]:
        """Retrieves the status of an inbound plan operation, such as creating or canceling a plan.

        Args:
            operation_id: Unique identifier for the operation.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/operations/{operation-id}"),
            path_params=[param[str]("operation-id", operation_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CommonInboundOperationStatus],
            error_mapper=get_inbound_operation_status_error_mapper,
            request_options=request_options,
        )

    def get_inbound_plan(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InboundPlan, GetInboundPlanErrorBody]:
        """Retrieves the details of an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}"),
            path_params=[param[str]("plan-id", plan_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[InboundPlan],
            error_mapper=get_inbound_plan_error_mapper,
            request_options=request_options,
        )

    def get_item_eligibility_preview(
        self,
        item_id: str,
        program: Program1OrStr,
        *,
        marketplace_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetItemEligibilityPreviewResponse, GetItemEligibilityPreviewErrorBody]:
        """Checks whether an item is eligible for the specified program.

        Args:
            item_id: Walmart item identifier for which to retrieve an eligibility preview.
            program: Program for which to evaluate item eligibility.
            marketplace_ids: Marketplace identifier to use when determining item eligibility.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/eligibility/item-preview"),
            query_params=[
                param[str]("itemId", item_id),
                param[Program1OrStr]("program", program),
                param[str | None]("marketplaceIds", marketplace_ids),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetItemEligibilityPreviewResponse],
            error_mapper=get_item_eligibility_preview_error_mapper,
            request_options=request_options,
        )

    def get_labels(
        self,
        shipment_id: str,
        page_type: PageTypeOrStr,
        label_type: LabelTypeOrStr,
        *,
        page_size: int | None = None,
        page_start_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetLabelsResponse, GetLabelsErrorBody]:
        """Returns package/pallet labels for faster and more accurate shipment processing at the Walmart fulfillment
        center.

        Args:
            shipment_id: Identifier of a shipment.
            page_type: The page size/format to use for label printing (upstream ``PageType``). Determines the physical
                layout of the generated label file.
            label_type: The type of label to retrieve (upstream ``LabelType``). ``UNIQUE`` is a carrier-assigned unique
                shipping label (PARCEL shipments only); ``BARCODE_2D`` is a 2D barcode receiving/box label; ``PALLET``
                is a pallet receiving label (non-PARCEL modes only).
            page_size: The page size for paginating through the total packages' labels. Maximum 1000 (upstream
                ``PageSize``, default 100).
            page_start_index: The zero-based page start index for paginating through the total packages' labels
                (upstream ``PageStartIndex``, default 0).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/shipments/{shipment-id}/labels"),
            path_params=[param[str]("shipment-id", shipment_id)],
            query_params=[
                param[PageTypeOrStr]("pageType", page_type),
                param[LabelTypeOrStr]("labelType", label_type),
                param[int | None]("pageSize", page_size),
                param[int | None]("pageStartIndex", page_start_index),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetLabelsResponse],
            error_mapper=get_labels_error_mapper,
            request_options=request_options,
        )

    def get_prep_instructions(
        self,
        ship_to_country_code: str,
        *,
        seller_sku_list: list[str] | None = None,
        asin_list: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPrepInstructionsResponse, GetPrepInstructionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            ship_to_country_code: The two-letter country code of the destination the item(s) will ship to.
            seller_sku_list: A list of seller SKUs to retrieve prep instructions for.
            asin_list: A list of ASINs to retrieve prep instructions for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/prep-instructions"),
            query_params=[
                param[str]("shipToCountryCode", ship_to_country_code),
                param[list[str] | None]("sellerSkuList", seller_sku_list),
                param[list[str] | None]("asinList", asin_list),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetPrepInstructionsResponse],
            error_mapper=get_prep_instructions_error_mapper,
            request_options=request_options,
        )

    def get_self_ship_appointment_slots(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetSelfShipAppointmentSlotsResponse, GetSelfShipAppointmentSlotsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of self ship appointment slots to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetSelfShipAppointmentSlotsResponse],
            error_mapper=get_self_ship_appointment_slots_error_mapper,
            request_options=request_options,
        )

    def get_shipment(
        self, plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommonShipment, GetShipmentErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CommonShipment],
            error_mapper=get_shipment_error_mapper,
            request_options=request_options,
        )

    def get_shipment_content_update_preview(
        self,
        plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommonContentUpdatePreview, GetShipmentContentUpdatePreviewErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews/{content-update-preview-id}",
            ),
            path_params=[
                param[str]("plan-id", plan_id),
                param[str]("shipment-id", shipment_id),
                param[str]("content-update-preview-id", content_update_preview_id),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CommonContentUpdatePreview],
            error_mapper=get_shipment_content_update_preview_error_mapper,
            request_options=request_options,
        )

    def get_shipment_items(
        self,
        *,
        date_range_filter: DateRangeFilterOrStr | None = None,
        date_range_value: str | None = None,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetShipmentItemsResponse, GetShipmentItemsErrorBody]:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike
            ``getShipmentItemsByShipmentId`` and ``listShipmentItems``, this op is NOT shipment- or plan-scoped -- it
            searches item rows across ALL of a seller's shipments, date- filtered. Field naming deliberately uses the
            Amazon SP-API-parity names ``sellerSku``/ ``fulfillmentNetworkSKU`` (per explicit mapping instructions)
            rather than the ``msku``/``fnsku`` shorthand its shipment-/plan-scoped siblings settled on -- this is a
            genuinely new v4 response shape with no naming precedent of its own to preserve.

        Args:
            date_range_filter: Which date field ``dateRangeValue`` filters on (upstream ``dateRangeFilter``).
            date_range_value: ISO 8601 datetime paired with ``dateRangeFilter`` (upstream ``dateRangeValue``).
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch the next page of a previous ``getShipmentItems`` query. Pass the value of
                ``pagination.nextToken`` from a previous response. Forwarded upstream as ``nextToken`` (already
                lowerCamelCase on this op, unlike ``getShipments``' ``NextToken``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/shipment-items"),
            query_params=[
                param[DateRangeFilterOrStr | None]("dateRangeFilter", date_range_filter),
                param[str | None]("dateRangeValue", date_range_value),
                param[int | None]("pageSize", page_size),
                param[str | None]("paginationToken", pagination_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetShipmentItemsResponse],
            error_mapper=get_shipment_items_error_mapper,
            request_options=request_options,
        )

    def get_shipment_items_by_shipment_id(
        self,
        shipment_id: str,
        *,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetShipmentItemsByShipmentIdResponse, GetShipmentItemsByShipmentIdErrorBody]:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike
            listShipmentItems, this op is NOT inboundPlan-scoped -- it reads a CONFIRMED shipment directly by shipmentId
            (the upstream shipmentRefId / externalReferenceId), with no draft-lookup fallback.

        Args:
            shipment_id: Identifier of a confirmed shipment (shipmentRefId / externalReferenceId).
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results. Pass the
                value of ``pagination.nextToken`` from a previous response to fetch the next page. Upstream Inbound
                Order Workflow returns this cursor as ``NextToken`` in the response payload ; it is mapped through
                unchanged into ``pagination.nextToken`` here -- the request-side parameter name stays
                ``paginationToken`` for consistency with every other list operation in this API.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/shipments/{shipment-id}/items"),
            path_params=[param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetShipmentItemsByShipmentIdResponse],
            error_mapper=get_shipment_items_by_shipment_id_error_mapper,
            request_options=request_options,
        )

    def get_shipments(
        self,
        query_type: ShipmentsQueryTypeOrStr,
        *,
        shipment_id_list: list[str] | None = None,
        shipment_status_list: list[ShipmentStatusOrStr] | None = None,
        last_updated_after: str | None = None,
        last_updated_before: str | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetShipmentsResponse, GetShipmentsErrorBody]:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike every shipment op
            above, this is NOT plan- or shipment-scoped -- it searches across ALL of a seller's shipments. Behavior is
            driven by ``queryType``:
          - ``SHIPMENT``: requires exactly one of ``shipmentIdList`` or ``shipmentStatusList`` (never
            both, never neither -- , tightened to match an upstream spec update).
          - ``DATE_RANGE``: requires ``lastUpdatedAfter`` (``lastUpdatedBefore`` is optional);
            ``shipmentStatusList`` may be supplied as an additional filter.
          - ``NEXT_TOKEN``: requires ``paginationToken`` (the value returned in a previous response's
            ``pagination.nextToken``) to fetch the next page of the SAME query; resend the original
            ``shipmentIdList``/``shipmentStatusList``/``lastUpdatedAfter``/``lastUpdatedBefore`` filters,
            since ``paginationToken`` only encodes the paging cursor, not the filters themselves.

        Args:
            query_type: Determines which combination of filters below is required (upstream ``QueryType``).
            shipment_id_list: Shipment identifiers (external reference ids) to filter by. When ``queryType=SHIPMENT``,
                exactly one of ``shipmentIdList``/``shipmentStatusList`` is required -- never both, never neither .
                Maximum 999 entries (upstream ``ShipmentIdList``).
            shipment_status_list: Shipment statuses to filter by (upstream ``ShipmentStatusList``; same vocabulary as
                ``getShipment``'s free-string ``status`` field, minus ``UNCONFIRMED``, which upstream documents as never
                applying to a confirmed shipment). When ``queryType=SHIPMENT``, exactly one of
                ``shipmentIdList``/``shipmentStatusList`` is required -- never both, never neither ; for
                ``queryType=DATE_RANGE`` it remains an optional additional filter.
            last_updated_after: Only return shipments last updated at or after this date, ISO 8601 datetime. Required
                when ``queryType=DATE_RANGE`` (upstream ``LastUpdatedAfter``).
            last_updated_before: Only return shipments last updated at or before this date, ISO 8601 datetime. Optional
                when ``queryType=DATE_RANGE``, defaults to now (upstream ``LastUpdatedBefore``).
            pagination_token: A token to fetch the next page of a previous ``getShipments`` query. Pass the value of
                ``pagination.nextToken`` from a previous response. Required when ``queryType=NEXT_TOKEN``. Forwarded
                upstream as ``NextToken``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/shipments"),
            query_params=[
                param[ShipmentsQueryTypeOrStr]("queryType", query_type),
                param[list[str] | None]("shipmentIdList", shipment_id_list),
                param[list[ShipmentStatusOrStr] | None]("shipmentStatusList", shipment_status_list),
                param[str | None]("lastUpdatedAfter", last_updated_after),
                param[str | None]("lastUpdatedBefore", last_updated_before),
                param[str | None]("paginationToken", pagination_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetShipmentsResponse],
            error_mapper=get_shipments_error_mapper,
            request_options=request_options,
        )

    def list_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDeliveryWindowOptionsResponse, ListDeliveryWindowOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to get delivery window options for.
            page_size: The number of delivery window options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListDeliveryWindowOptionsResponse],
            error_mapper=list_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    def list_inbound_plan_boxes(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanBoxesResponse, ListInboundPlanBoxesErrorBody]:
        """Retrieves a paginated list of shipping boxes included in an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of boxes to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/boxes"),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlanBoxesResponse],
            error_mapper=list_inbound_plan_boxes_error_mapper,
            request_options=request_options,
        )

    def list_inbound_plan_items(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanItemsResponse, ListInboundPlanItemsErrorBody]:
        """Retrieves a paginated list of items in an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of items to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/items"),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlanItemsResponse],
            error_mapper=list_inbound_plan_items_error_mapper,
            request_options=request_options,
        )

    def list_inbound_plan_pallets(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanPalletsResponse, ListInboundPlanPalletsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of pallets to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/pallets"),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlanPalletsResponse],
            error_mapper=list_inbound_plan_pallets_error_mapper,
            request_options=request_options,
        )

    def list_inbound_plans(
        self,
        *,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        status: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlansResponse, ListInboundPlansErrorBody]:
        """Retrieves a paginated list of inbound plans. Filter by status, sort the results, and use ``paginationToken``
        to retrieve subsequent pages.

        Args:
            page_size: Maximum number of inbound plans to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            status: Filters results by inbound plan status. Supported values are ``ACTIVE``, ``VOIDED``, ``SHIPPED``,
                and ``ERRORED``.
            sort_by: Field used to sort the returned inbound plans.
            sort_order: Sort direction for the returned inbound plans. Supported values are ``ASC`` and ``DESC``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans"),
            query_params=[
                param[int | None]("pageSize", page_size),
                param[str | None]("paginationToken", pagination_token),
                param[str | None]("status", status),
                param[str | None]("sortBy", sort_by),
                param[str | None]("sortOrder", sort_order),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlansResponse],
            error_mapper=list_inbound_plans_error_mapper,
            request_options=request_options,
        )

    def list_item_compliance_details(
        self, mskus: list[str], marketplace_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListItemComplianceDetailsResponse, ListItemComplianceDetailsErrorBody]:
        """Send a ``GET`` request.

        Args:
            mskus: A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/compliance"),
            query_params=[param[list[str]]("mskus", mskus), param[str]("marketplaceId", marketplace_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListItemComplianceDetailsResponse],
            error_mapper=list_item_compliance_details_error_mapper,
            request_options=request_options,
        )

    def list_packing_group_boxes(
        self,
        plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPackingGroupBoxesResponse, ListPackingGroupBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/packing-groups/{packing-group-id}/boxes"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("packing-group-id", packing_group_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListPackingGroupBoxesResponse],
            error_mapper=list_packing_group_boxes_error_mapper,
            request_options=request_options,
        )

    def list_packing_group_items(
        self,
        plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPackingGroupItemsResponse, ListPackingGroupItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/packing-groups/{packing-group-id}/items"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("packing-group-id", packing_group_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListPackingGroupItemsResponse],
            error_mapper=list_packing_group_items_error_mapper,
            request_options=request_options,
        )

    def list_packing_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPackingOptionsResponse, ListPackingOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of packing options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/packing-options"),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListPackingOptionsResponse],
            error_mapper=list_packing_options_error_mapper,
            request_options=request_options,
        )

    def list_placement_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPlacementOptionsResponse, ListPlacementOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of placement options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/placement-options"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListPlacementOptionsResponse],
            error_mapper=list_placement_options_error_mapper,
            request_options=request_options,
        )

    def list_prep_details(
        self, marketplace_id: str, mskus: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListPrepDetailsResponse, ListPrepDetailsErrorBody]:
        """Send a ``GET`` request.

        Args:
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            mskus: A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/prep-details"),
            query_params=[param[str]("marketplaceId", marketplace_id), param[list[str]]("mskus", mskus)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListPrepDetailsResponse],
            error_mapper=list_prep_details_error_mapper,
            request_options=request_options,
        )

    def list_shipment_boxes(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentBoxesResponse, ListShipmentBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/boxes"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListShipmentBoxesResponse],
            error_mapper=list_shipment_boxes_error_mapper,
            request_options=request_options,
        )

    def list_shipment_content_update_previews(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentContentUpdatePreviewsResponse, ListShipmentContentUpdatePreviewsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of content update previews to return.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListShipmentContentUpdatePreviewsResponse],
            error_mapper=list_shipment_content_update_previews_error_mapper,
            request_options=request_options,
        )

    def list_shipment_items(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentItemsResponse, ListShipmentItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/items"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListShipmentItemsResponse],
            error_mapper=list_shipment_items_error_mapper,
            request_options=request_options,
        )

    def list_shipment_pallets(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentPalletsResponse, ListShipmentPalletsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/pallets"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListShipmentPalletsResponse],
            error_mapper=list_shipment_pallets_error_mapper,
            request_options=request_options,
        )

    def list_transportation_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        placement_option_id: str | None = None,
        shipment_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTransportationOptionsResponse, ListTransportationOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of transportation options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            placement_option_id: The placement option to get transportation options for. Either ``placementOptionId`` or
                ``shipmentId`` must be specified.
            shipment_id: The shipment to get transportation options for. Either ``placementOptionId`` or ``shipmentId``
                must be specified.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/transportation-options"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size),
                param[str | None]("paginationToken", pagination_token),
                param[str | None]("placementOptionId", placement_option_id),
                param[str | None]("shipmentId", shipment_id),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListTransportationOptionsResponse],
            error_mapper=list_transportation_options_error_mapper,
            request_options=request_options,
        )

    def schedule_self_ship_appointment(
        self,
        plan_id: str,
        shipment_id: str,
        slot_id: str,
        body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduleSelfShipAppointmentResponse, ScheduleSelfShipAppointmentErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            slot_id: An identifier to a self-ship appointment slot.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots/{slot-id}/schedule",
            ),
            path_params=[
                param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id), param[str]("slot-id", slot_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ScheduleSelfShipAppointmentResponse],
            error_mapper=schedule_self_ship_appointment_error_mapper,
            request_options=request_options,
        )

    def set_packing_information(
        self,
        plan_id: str,
        body: SetPackingInformationRequest | SetPackingInformationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SetPackingInformationResponse, SetPackingInformationErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/packing-information"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetPackingInformationRequest | SetPackingInformationRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[SetPackingInformationResponse],
            error_mapper=set_packing_information_error_mapper,
            request_options=request_options,
        )

    def set_prep_details(
        self,
        body: SetPrepDetailsRequest | SetPrepDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SetPrepDetailsResponse, SetPrepDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/prep-details"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetPrepDetailsRequest | SetPrepDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[SetPrepDetailsResponse],
            error_mapper=set_prep_details_error_mapper,
            request_options=request_options,
        )

    def update_inbound_plan_name(
        self,
        plan_id: str,
        body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateInboundPlanNameErrorBody]:
        """Updates the name of an existing inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/name"),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=empty_response,
            error_mapper=update_inbound_plan_name_error_mapper,
            request_options=request_options,
        )

    def update_item_compliance_details(
        self,
        marketplace_id: str,
        body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateItemComplianceDetailsResponse, UpdateItemComplianceDetailsErrorBody]:
        """Send a ``PUT`` request.

        Args:
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/compliance"),
            query_params=[param[str]("marketplaceId", marketplace_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[UpdateItemComplianceDetailsResponse],
            error_mapper=update_item_compliance_details_error_mapper,
            request_options=request_options,
        )

    def update_shipment_name(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateShipmentNameErrorBody]:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/name"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentNameRequest | UpdateShipmentNameRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=empty_response,
            error_mapper=update_shipment_name_error_mapper,
            request_options=request_options,
        )

    def update_shipment_source_address(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateShipmentSourceAddressResponse, UpdateShipmentSourceAddressErrorBody]:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/source-address"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[UpdateShipmentSourceAddressResponse],
            error_mapper=update_shipment_source_address_error_mapper,
            request_options=request_options,
        )

    def update_shipment_tracking_details(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateShipmentTrackingDetailsResponse, UpdateShipmentTrackingDetailsErrorBody]:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/tracking-details"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[UpdateShipmentTrackingDetailsResponse],
            error_mapper=update_shipment_tracking_details_error_mapper,
            request_options=request_options,
        )


class AsyncWfsInboundWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_inbound_plan(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, CancelInboundPlanErrorBody]:
        """Cancels an inbound plan when its current status allows cancellation.

        Args:
            plan_id: Unique identifier of the inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/cancel"),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=cancel_inbound_plan_error_mapper,
            request_options=request_options,
        )

    async def cancel_self_ship_appointment(
        self,
        plan_id: str,
        shipment_id: str,
        body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelSelfShipAppointmentResponse, CancelSelfShipAppointmentErrorBody]:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-cancel"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelSelfShipAppointmentResponse],
            error_mapper=cancel_self_ship_appointment_error_mapper,
            request_options=request_options,
        )

    async def confirm_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        delivery_window_option_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConfirmDeliveryWindowOptionsResponse, ConfirmDeliveryWindowOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to confirm the delivery window option for.
            delivery_window_option_id: The ID of the delivery window option to be confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options/{delivery-window-option-id}/confirm",
            ),
            path_params=[
                param[str]("plan-id", plan_id),
                param[str]("shipment-id", shipment_id),
                param[str]("delivery-window-option-id", delivery_window_option_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ConfirmDeliveryWindowOptionsResponse],
            error_mapper=confirm_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    async def confirm_packing_option(
        self, plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConfirmPackingOptionResponse, ConfirmPackingOptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_option_id: Identifier of a packing option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/packing-options/{packing-option-id}/confirm"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("packing-option-id", packing_option_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ConfirmPackingOptionResponse],
            error_mapper=confirm_packing_option_error_mapper,
            request_options=request_options,
        )

    async def confirm_placement_option(
        self, plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConfirmPlacementOptionResponse, ConfirmPlacementOptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            placement_option_id: The identifier of a placement option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/placement-options/{placement-option-id}/confirm"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("placement-option-id", placement_option_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ConfirmPlacementOptionResponse],
            error_mapper=confirm_placement_option_error_mapper,
            request_options=request_options,
        )

    async def confirm_shipment_content_update_preview(
        self,
        plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConfirmShipmentContentUpdatePreviewResponse, ConfirmShipmentContentUpdatePreviewErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews/{content-update-preview-id}/confirm",
            ),
            path_params=[
                param[str]("plan-id", plan_id),
                param[str]("shipment-id", shipment_id),
                param[str]("content-update-preview-id", content_update_preview_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ConfirmShipmentContentUpdatePreviewResponse],
            error_mapper=confirm_shipment_content_update_preview_error_mapper,
            request_options=request_options,
        )

    async def confirm_transportation_options(
        self,
        plan_id: str,
        body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConfirmTransportationOptionsResponse, ConfirmTransportationOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/transportation-options/confirm"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ConfirmTransportationOptionsResponse],
            error_mapper=confirm_transportation_options_error_mapper,
            request_options=request_options,
        )

    async def create_inbound_plan(
        self,
        body: CreateInboundPlanRequest | CreateInboundPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInboundPlanResponse, CreateInboundPlanErrorBody]:
        """Creates an inbound plan for items to be shipped to Walmart fulfillment centers.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateInboundPlanRequest | CreateInboundPlanRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateInboundPlanResponse],
            error_mapper=create_inbound_plan_error_mapper,
            request_options=request_options,
        )

    async def create_marketplace_item_labels(
        self,
        body: CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateMarketplaceItemLabelsResponse, CreateMarketplaceItemLabelsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/labels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateMarketplaceItemLabelsResponse],
            error_mapper=create_marketplace_item_labels_error_mapper,
            request_options=request_options,
        )

    async def generate_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        scac: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateDeliveryWindowOptionsResponse, GenerateDeliveryWindowOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to generate delivery window options for.
            scac: Walmart extension (not in SP-API). Standard Carrier Alpha Code of the carrier delivering the shipment,
                case preserved. Supplying it generates drop trailer windows; omitting it generates live unload windows.
                The delivery type chosen here is kept when a generated window is confirmed. Carrier existence and drop
                trailer eligibility are validated when the window is confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[param[str | None]("scac", scac)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GenerateDeliveryWindowOptionsResponse],
            error_mapper=generate_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    async def generate_packing_options(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GeneratePackingOptionsResponse, GeneratePackingOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/packing-options"),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GeneratePackingOptionsResponse],
            error_mapper=generate_packing_options_error_mapper,
            request_options=request_options,
        )

    async def generate_placement_options(
        self,
        plan_id: str,
        body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GeneratePlacementOptionsResponse, GeneratePlacementOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/placement-options"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GeneratePlacementOptionsResponse],
            error_mapper=generate_placement_options_error_mapper,
            request_options=request_options,
        )

    async def generate_self_ship_appointment_slots(
        self,
        plan_id: str,
        shipment_id: str,
        body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateSelfShipAppointmentSlotsResponse, GenerateSelfShipAppointmentSlotsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GenerateSelfShipAppointmentSlotsResponse],
            error_mapper=generate_self_ship_appointment_slots_error_mapper,
            request_options=request_options,
        )

    async def generate_shipment_content_update_previews(
        self,
        plan_id: str,
        shipment_id: str,
        body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateShipmentContentUpdatePreviewsResponse, GenerateShipmentContentUpdatePreviewsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict
            ](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GenerateShipmentContentUpdatePreviewsResponse],
            error_mapper=generate_shipment_content_update_previews_error_mapper,
            request_options=request_options,
        )

    async def generate_transportation_options(
        self,
        plan_id: str,
        body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenerateTransportationOptionsResponse, GenerateTransportationOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/transportation-options"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GenerateTransportationOptionsResponse],
            error_mapper=generate_transportation_options_error_mapper,
            request_options=request_options,
        )

    async def get_bill_of_lading(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetBillOfLadingResponse, GetBillOfLadingErrorBody]:
        """Send a ``GET`` request.

        Args:
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/shipments/{shipment-id}/bill-of-lading"
            ),
            path_params=[param[str]("shipment-id", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetBillOfLadingResponse],
            error_mapper=get_bill_of_lading_error_mapper,
            request_options=request_options,
        )

    async def get_delivery_challan_document(
        self, plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetDeliveryChallanDocumentResponse, GetDeliveryChallanDocumentErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-challan-document"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetDeliveryChallanDocumentResponse],
            error_mapper=get_delivery_challan_document_error_mapper,
            request_options=request_options,
        )

    async def get_inbound_operation_status(
        self, operation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommonInboundOperationStatus, GetInboundOperationStatusErrorBody]:
        """Retrieves the status of an inbound plan operation, such as creating or canceling a plan.

        Args:
            operation_id: Unique identifier for the operation.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/operations/{operation-id}"),
            path_params=[param[str]("operation-id", operation_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CommonInboundOperationStatus],
            error_mapper=get_inbound_operation_status_error_mapper,
            request_options=request_options,
        )

    async def get_inbound_plan(
        self, plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InboundPlan, GetInboundPlanErrorBody]:
        """Retrieves the details of an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}"),
            path_params=[param[str]("plan-id", plan_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[InboundPlan],
            error_mapper=get_inbound_plan_error_mapper,
            request_options=request_options,
        )

    async def get_item_eligibility_preview(
        self,
        item_id: str,
        program: Program1OrStr,
        *,
        marketplace_ids: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetItemEligibilityPreviewResponse, GetItemEligibilityPreviewErrorBody]:
        """Checks whether an item is eligible for the specified program.

        Args:
            item_id: Walmart item identifier for which to retrieve an eligibility preview.
            program: Program for which to evaluate item eligibility.
            marketplace_ids: Marketplace identifier to use when determining item eligibility.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/eligibility/item-preview"),
            query_params=[
                param[str]("itemId", item_id),
                param[Program1OrStr]("program", program),
                param[str | None]("marketplaceIds", marketplace_ids),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetItemEligibilityPreviewResponse],
            error_mapper=get_item_eligibility_preview_error_mapper,
            request_options=request_options,
        )

    async def get_labels(
        self,
        shipment_id: str,
        page_type: PageTypeOrStr,
        label_type: LabelTypeOrStr,
        *,
        page_size: int | None = None,
        page_start_index: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetLabelsResponse, GetLabelsErrorBody]:
        """Returns package/pallet labels for faster and more accurate shipment processing at the Walmart fulfillment
        center.

        Args:
            shipment_id: Identifier of a shipment.
            page_type: The page size/format to use for label printing (upstream ``PageType``). Determines the physical
                layout of the generated label file.
            label_type: The type of label to retrieve (upstream ``LabelType``). ``UNIQUE`` is a carrier-assigned unique
                shipping label (PARCEL shipments only); ``BARCODE_2D`` is a 2D barcode receiving/box label; ``PALLET``
                is a pallet receiving label (non-PARCEL modes only).
            page_size: The page size for paginating through the total packages' labels. Maximum 1000 (upstream
                ``PageSize``, default 100).
            page_start_index: The zero-based page start index for paginating through the total packages' labels
                (upstream ``PageStartIndex``, default 0).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/shipments/{shipment-id}/labels"),
            path_params=[param[str]("shipment-id", shipment_id)],
            query_params=[
                param[PageTypeOrStr]("pageType", page_type),
                param[LabelTypeOrStr]("labelType", label_type),
                param[int | None]("pageSize", page_size),
                param[int | None]("pageStartIndex", page_start_index),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetLabelsResponse],
            error_mapper=get_labels_error_mapper,
            request_options=request_options,
        )

    async def get_prep_instructions(
        self,
        ship_to_country_code: str,
        *,
        seller_sku_list: list[str] | None = None,
        asin_list: list[str] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPrepInstructionsResponse, GetPrepInstructionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            ship_to_country_code: The two-letter country code of the destination the item(s) will ship to.
            seller_sku_list: A list of seller SKUs to retrieve prep instructions for.
            asin_list: A list of ASINs to retrieve prep instructions for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/prep-instructions"),
            query_params=[
                param[str]("shipToCountryCode", ship_to_country_code),
                param[list[str] | None]("sellerSkuList", seller_sku_list),
                param[list[str] | None]("asinList", asin_list),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetPrepInstructionsResponse],
            error_mapper=get_prep_instructions_error_mapper,
            request_options=request_options,
        )

    async def get_self_ship_appointment_slots(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetSelfShipAppointmentSlotsResponse, GetSelfShipAppointmentSlotsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of self ship appointment slots to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetSelfShipAppointmentSlotsResponse],
            error_mapper=get_self_ship_appointment_slots_error_mapper,
            request_options=request_options,
        )

    async def get_shipment(
        self, plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommonShipment, GetShipmentErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CommonShipment],
            error_mapper=get_shipment_error_mapper,
            request_options=request_options,
        )

    async def get_shipment_content_update_preview(
        self,
        plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommonContentUpdatePreview, GetShipmentContentUpdatePreviewErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews/{content-update-preview-id}",
            ),
            path_params=[
                param[str]("plan-id", plan_id),
                param[str]("shipment-id", shipment_id),
                param[str]("content-update-preview-id", content_update_preview_id),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CommonContentUpdatePreview],
            error_mapper=get_shipment_content_update_preview_error_mapper,
            request_options=request_options,
        )

    async def get_shipment_items(
        self,
        *,
        date_range_filter: DateRangeFilterOrStr | None = None,
        date_range_value: str | None = None,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetShipmentItemsResponse, GetShipmentItemsErrorBody]:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike
            ``getShipmentItemsByShipmentId`` and ``listShipmentItems``, this op is NOT shipment- or plan-scoped -- it
            searches item rows across ALL of a seller's shipments, date- filtered. Field naming deliberately uses the
            Amazon SP-API-parity names ``sellerSku``/ ``fulfillmentNetworkSKU`` (per explicit mapping instructions)
            rather than the ``msku``/``fnsku`` shorthand its shipment-/plan-scoped siblings settled on -- this is a
            genuinely new v4 response shape with no naming precedent of its own to preserve.

        Args:
            date_range_filter: Which date field ``dateRangeValue`` filters on (upstream ``dateRangeFilter``).
            date_range_value: ISO 8601 datetime paired with ``dateRangeFilter`` (upstream ``dateRangeValue``).
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch the next page of a previous ``getShipmentItems`` query. Pass the value of
                ``pagination.nextToken`` from a previous response. Forwarded upstream as ``nextToken`` (already
                lowerCamelCase on this op, unlike ``getShipments``' ``NextToken``).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/shipment-items"),
            query_params=[
                param[DateRangeFilterOrStr | None]("dateRangeFilter", date_range_filter),
                param[str | None]("dateRangeValue", date_range_value),
                param[int | None]("pageSize", page_size),
                param[str | None]("paginationToken", pagination_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetShipmentItemsResponse],
            error_mapper=get_shipment_items_error_mapper,
            request_options=request_options,
        )

    async def get_shipment_items_by_shipment_id(
        self,
        shipment_id: str,
        *,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetShipmentItemsByShipmentIdResponse, GetShipmentItemsByShipmentIdErrorBody]:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike
            listShipmentItems, this op is NOT inboundPlan-scoped -- it reads a CONFIRMED shipment directly by shipmentId
            (the upstream shipmentRefId / externalReferenceId), with no draft-lookup fallback.

        Args:
            shipment_id: Identifier of a confirmed shipment (shipmentRefId / externalReferenceId).
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results. Pass the
                value of ``pagination.nextToken`` from a previous response to fetch the next page. Upstream Inbound
                Order Workflow returns this cursor as ``NextToken`` in the response payload ; it is mapped through
                unchanged into ``pagination.nextToken`` here -- the request-side parameter name stays
                ``paginationToken`` for consistency with every other list operation in this API.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/shipments/{shipment-id}/items"),
            path_params=[param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetShipmentItemsByShipmentIdResponse],
            error_mapper=get_shipment_items_by_shipment_id_error_mapper,
            request_options=request_options,
        )

    async def get_shipments(
        self,
        query_type: ShipmentsQueryTypeOrStr,
        *,
        shipment_id_list: list[str] | None = None,
        shipment_status_list: list[ShipmentStatusOrStr] | None = None,
        last_updated_after: str | None = None,
        last_updated_before: str | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetShipmentsResponse, GetShipmentsErrorBody]:
        """: net-new v4 operation (source-to-target: SAME operationId upstream and downstream). Unlike every shipment op
            above, this is NOT plan- or shipment-scoped -- it searches across ALL of a seller's shipments. Behavior is
            driven by ``queryType``:
          - ``SHIPMENT``: requires exactly one of ``shipmentIdList`` or ``shipmentStatusList`` (never
            both, never neither -- , tightened to match an upstream spec update).
          - ``DATE_RANGE``: requires ``lastUpdatedAfter`` (``lastUpdatedBefore`` is optional);
            ``shipmentStatusList`` may be supplied as an additional filter.
          - ``NEXT_TOKEN``: requires ``paginationToken`` (the value returned in a previous response's
            ``pagination.nextToken``) to fetch the next page of the SAME query; resend the original
            ``shipmentIdList``/``shipmentStatusList``/``lastUpdatedAfter``/``lastUpdatedBefore`` filters,
            since ``paginationToken`` only encodes the paging cursor, not the filters themselves.

        Args:
            query_type: Determines which combination of filters below is required (upstream ``QueryType``).
            shipment_id_list: Shipment identifiers (external reference ids) to filter by. When ``queryType=SHIPMENT``,
                exactly one of ``shipmentIdList``/``shipmentStatusList`` is required -- never both, never neither .
                Maximum 999 entries (upstream ``ShipmentIdList``).
            shipment_status_list: Shipment statuses to filter by (upstream ``ShipmentStatusList``; same vocabulary as
                ``getShipment``'s free-string ``status`` field, minus ``UNCONFIRMED``, which upstream documents as never
                applying to a confirmed shipment). When ``queryType=SHIPMENT``, exactly one of
                ``shipmentIdList``/``shipmentStatusList`` is required -- never both, never neither ; for
                ``queryType=DATE_RANGE`` it remains an optional additional filter.
            last_updated_after: Only return shipments last updated at or after this date, ISO 8601 datetime. Required
                when ``queryType=DATE_RANGE`` (upstream ``LastUpdatedAfter``).
            last_updated_before: Only return shipments last updated at or before this date, ISO 8601 datetime. Optional
                when ``queryType=DATE_RANGE``, defaults to now (upstream ``LastUpdatedBefore``).
            pagination_token: A token to fetch the next page of a previous ``getShipments`` query. Pass the value of
                ``pagination.nextToken`` from a previous response. Required when ``queryType=NEXT_TOKEN``. Forwarded
                upstream as ``NextToken``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/shipments"),
            query_params=[
                param[ShipmentsQueryTypeOrStr]("queryType", query_type),
                param[list[str] | None]("shipmentIdList", shipment_id_list),
                param[list[ShipmentStatusOrStr] | None]("shipmentStatusList", shipment_status_list),
                param[str | None]("lastUpdatedAfter", last_updated_after),
                param[str | None]("lastUpdatedBefore", last_updated_before),
                param[str | None]("paginationToken", pagination_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetShipmentsResponse],
            error_mapper=get_shipments_error_mapper,
            request_options=request_options,
        )

    async def list_delivery_window_options(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDeliveryWindowOptionsResponse, ListDeliveryWindowOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to get delivery window options for.
            page_size: The number of delivery window options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/delivery-window-options"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListDeliveryWindowOptionsResponse],
            error_mapper=list_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    async def list_inbound_plan_boxes(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanBoxesResponse, ListInboundPlanBoxesErrorBody]:
        """Retrieves a paginated list of shipping boxes included in an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of boxes to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/boxes"),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlanBoxesResponse],
            error_mapper=list_inbound_plan_boxes_error_mapper,
            request_options=request_options,
        )

    async def list_inbound_plan_items(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanItemsResponse, ListInboundPlanItemsErrorBody]:
        """Retrieves a paginated list of items in an inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of items to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/items"),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlanItemsResponse],
            error_mapper=list_inbound_plan_items_error_mapper,
            request_options=request_options,
        )

    async def list_inbound_plan_pallets(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanPalletsResponse, ListInboundPlanPalletsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Unique identifier of the inbound plan.
            page_size: Maximum number of pallets to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/pallets"),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlanPalletsResponse],
            error_mapper=list_inbound_plan_pallets_error_mapper,
            request_options=request_options,
        )

    async def list_inbound_plans(
        self,
        *,
        page_size: int | None = 10,
        pagination_token: str | None = None,
        status: str | None = None,
        sort_by: str | None = None,
        sort_order: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlansResponse, ListInboundPlansErrorBody]:
        """Retrieves a paginated list of inbound plans. Filter by status, sort the results, and use ``paginationToken``
        to retrieve subsequent pages.

        Args:
            page_size: Maximum number of inbound plans to return in the response.
            pagination_token: Pagination token returned in a previous response. Specify this parameter to retrieve the
                next page of results.
            status: Filters results by inbound plan status. Supported values are ``ACTIVE``, ``VOIDED``, ``SHIPPED``,
                and ``ERRORED``.
            sort_by: Field used to sort the returned inbound plans.
            sort_order: Sort direction for the returned inbound plans. Supported values are ``ASC`` and ``DESC``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans"),
            query_params=[
                param[int | None]("pageSize", page_size),
                param[str | None]("paginationToken", pagination_token),
                param[str | None]("status", status),
                param[str | None]("sortBy", sort_by),
                param[str | None]("sortOrder", sort_order),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlansResponse],
            error_mapper=list_inbound_plans_error_mapper,
            request_options=request_options,
        )

    async def list_item_compliance_details(
        self, mskus: list[str], marketplace_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListItemComplianceDetailsResponse, ListItemComplianceDetailsErrorBody]:
        """Send a ``GET`` request.

        Args:
            mskus: A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/compliance"),
            query_params=[param[list[str]]("mskus", mskus), param[str]("marketplaceId", marketplace_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListItemComplianceDetailsResponse],
            error_mapper=list_item_compliance_details_error_mapper,
            request_options=request_options,
        )

    async def list_packing_group_boxes(
        self,
        plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPackingGroupBoxesResponse, ListPackingGroupBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/packing-groups/{packing-group-id}/boxes"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("packing-group-id", packing_group_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListPackingGroupBoxesResponse],
            error_mapper=list_packing_group_boxes_error_mapper,
            request_options=request_options,
        )

    async def list_packing_group_items(
        self,
        plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPackingGroupItemsResponse, ListPackingGroupItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/packing-groups/{packing-group-id}/items"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("packing-group-id", packing_group_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListPackingGroupItemsResponse],
            error_mapper=list_packing_group_items_error_mapper,
            request_options=request_options,
        )

    async def list_packing_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPackingOptionsResponse, ListPackingOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of packing options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/packing-options"),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListPackingOptionsResponse],
            error_mapper=list_packing_options_error_mapper,
            request_options=request_options,
        )

    async def list_placement_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPlacementOptionsResponse, ListPlacementOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of placement options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/placement-options"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListPlacementOptionsResponse],
            error_mapper=list_placement_options_error_mapper,
            request_options=request_options,
        )

    async def list_prep_details(
        self, marketplace_id: str, mskus: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListPrepDetailsResponse, ListPrepDetailsErrorBody]:
        """Send a ``GET`` request.

        Args:
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            mskus: A list of merchant SKUs, a merchant-supplied identifier of a specific SKU.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/prep-details"),
            query_params=[param[str]("marketplaceId", marketplace_id), param[list[str]]("mskus", mskus)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListPrepDetailsResponse],
            error_mapper=list_prep_details_error_mapper,
            request_options=request_options,
        )

    async def list_shipment_boxes(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentBoxesResponse, ListShipmentBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/boxes"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListShipmentBoxesResponse],
            error_mapper=list_shipment_boxes_error_mapper,
            request_options=request_options,
        )

    async def list_shipment_content_update_previews(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentContentUpdatePreviewsResponse, ListShipmentContentUpdatePreviewsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of content update previews to return.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/content-update-previews"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListShipmentContentUpdatePreviewsResponse],
            error_mapper=list_shipment_content_update_previews_error_mapper,
            request_options=request_options,
        )

    async def list_shipment_items(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentItemsResponse, ListShipmentItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/items"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListShipmentItemsResponse],
            error_mapper=list_shipment_items_error_mapper,
            request_options=request_options,
        )

    async def list_shipment_pallets(
        self,
        plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentPalletsResponse, ListShipmentPalletsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/pallets"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListShipmentPalletsResponse],
            error_mapper=list_shipment_pallets_error_mapper,
            request_options=request_options,
        )

    async def list_transportation_options(
        self,
        plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        placement_option_id: str | None = None,
        shipment_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTransportationOptionsResponse, ListTransportationOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            page_size: The number of transportation options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            placement_option_id: The placement option to get transportation options for. Either ``placementOptionId`` or
                ``shipmentId`` must be specified.
            shipment_id: The shipment to get transportation options for. Either ``placementOptionId`` or ``shipmentId``
                must be specified.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/transportation-options"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            query_params=[
                param[int | None]("pageSize", page_size),
                param[str | None]("paginationToken", pagination_token),
                param[str | None]("placementOptionId", placement_option_id),
                param[str | None]("shipmentId", shipment_id),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListTransportationOptionsResponse],
            error_mapper=list_transportation_options_error_mapper,
            request_options=request_options,
        )

    async def schedule_self_ship_appointment(
        self,
        plan_id: str,
        shipment_id: str,
        slot_id: str,
        body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduleSelfShipAppointmentResponse, ScheduleSelfShipAppointmentErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            slot_id: An identifier to a self-ship appointment slot.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/self-ship-appointment-slots/{slot-id}/schedule",
            ),
            path_params=[
                param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id), param[str]("slot-id", slot_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ScheduleSelfShipAppointmentResponse],
            error_mapper=schedule_self_ship_appointment_error_mapper,
            request_options=request_options,
        )

    async def set_packing_information(
        self,
        plan_id: str,
        body: SetPackingInformationRequest | SetPackingInformationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SetPackingInformationResponse, SetPackingInformationErrorBody]:
        """Send a ``POST`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/packing-information"
            ),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetPackingInformationRequest | SetPackingInformationRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[SetPackingInformationResponse],
            error_mapper=set_packing_information_error_mapper,
            request_options=request_options,
        )

    async def set_prep_details(
        self,
        body: SetPrepDetailsRequest | SetPrepDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SetPrepDetailsResponse, SetPrepDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/prep-details"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetPrepDetailsRequest | SetPrepDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[SetPrepDetailsResponse],
            error_mapper=set_prep_details_error_mapper,
            request_options=request_options,
        )

    async def update_inbound_plan_name(
        self,
        plan_id: str,
        body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateInboundPlanNameErrorBody]:
        """Updates the name of an existing inbound plan.

        Args:
            plan_id: Unique identifier of the inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/plans/{plan-id}/name"),
            path_params=[param[str]("plan-id", plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_empty_response,
            error_mapper=update_inbound_plan_name_error_mapper,
            request_options=request_options,
        )

    async def update_item_compliance_details(
        self,
        marketplace_id: str,
        body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateItemComplianceDetailsResponse, UpdateItemComplianceDetailsErrorBody]:
        """Send a ``PUT`` request.

        Args:
            marketplace_id: The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
                <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items("/v4/fulfillment/inbound/items/compliance"),
            query_params=[param[str]("marketplaceId", marketplace_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[UpdateItemComplianceDetailsResponse],
            error_mapper=update_item_compliance_details_error_mapper,
            request_options=request_options,
        )

    async def update_shipment_name(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateShipmentNameErrorBody]:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/name"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentNameRequest | UpdateShipmentNameRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_empty_response,
            error_mapper=update_shipment_name_error_mapper,
            request_options=request_options,
        )

    async def update_shipment_source_address(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateShipmentSourceAddressResponse, UpdateShipmentSourceAddressErrorBody]:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/source-address"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[UpdateShipmentSourceAddressResponse],
            error_mapper=update_shipment_source_address_error_mapper,
            request_options=request_options,
        )

    async def update_shipment_tracking_details(
        self,
        plan_id: str,
        shipment_id: str,
        body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateShipmentTrackingDetailsResponse, UpdateShipmentTrackingDetailsErrorBody]:
        """Send a ``PUT`` request.

        Args:
            plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/inbound/plans/{plan-id}/shipments/{shipment-id}/tracking-details"
            ),
            path_params=[param[str]("plan-id", plan_id), param[str]("shipment-id", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[UpdateShipmentTrackingDetailsResponse],
            error_mapper=update_shipment_tracking_details_error_mapper,
            request_options=request_options,
        )
