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
from ..errors.get_delivery_challan_document_error import (
    GetDeliveryChallanDocumentErrorBody,
    get_delivery_challan_document_error_mapper,
)
from ..errors.get_inbound_operation_status_error import (
    GetInboundOperationStatusErrorBody,
    get_inbound_operation_status_error_mapper,
)
from ..errors.get_inbound_plan_error import GetInboundPlanErrorBody, get_inbound_plan_error_mapper
from ..errors.get_self_ship_appointment_slots_error import (
    GetSelfShipAppointmentSlotsErrorBody,
    get_self_ship_appointment_slots_error_mapper,
)
from ..errors.get_shipment_content_update_preview_error import (
    GetShipmentContentUpdatePreviewErrorBody,
    get_shipment_content_update_preview_error_mapper,
)
from ..errors.get_shipment_error import GetShipmentErrorBody, get_shipment_error_mapper
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
from ..models.common_content_update_preview import CommonContentUpdatePreview
from ..models.common_inbound_operation_status import CommonInboundOperationStatus
from ..models.common_shipment import CommonShipment
from ..models.confirm_transportation_options_request import (
    ConfirmTransportationOptionsRequest,
    ConfirmTransportationOptionsRequestDict,
)
from ..models.create_inbound_plan_request import CreateInboundPlanRequest, CreateInboundPlanRequestDict
from ..models.create_inbound_plan_response import CreateInboundPlanResponse
from ..models.create_marketplace_item_labels_request import (
    CreateMarketplaceItemLabelsRequest,
    CreateMarketplaceItemLabelsRequestDict,
)
from ..models.create_marketplace_item_labels_response import CreateMarketplaceItemLabelsResponse
from ..models.generate_placement_options_request import (
    GeneratePlacementOptionsRequest,
    GeneratePlacementOptionsRequestDict,
)
from ..models.generate_self_ship_appointment_slots_request import (
    GenerateSelfShipAppointmentSlotsRequest,
    GenerateSelfShipAppointmentSlotsRequestDict,
)
from ..models.generate_shipment_content_update_previews_request import (
    GenerateShipmentContentUpdatePreviewsRequest,
    GenerateShipmentContentUpdatePreviewsRequestDict,
)
from ..models.generate_transportation_options_request import (
    GenerateTransportationOptionsRequest,
    GenerateTransportationOptionsRequestDict,
)
from ..models.get_delivery_challan_document_response import GetDeliveryChallanDocumentResponse
from ..models.get_self_ship_appointment_slots_response import GetSelfShipAppointmentSlotsResponse
from ..models.inbound_plan import InboundPlan
from ..models.list_delivery_window_options_response import ListDeliveryWindowOptionsResponse
from ..models.list_inbound_plan_boxes_response import ListInboundPlanBoxesResponse
from ..models.list_inbound_plan_items_response import ListInboundPlanItemsResponse
from ..models.list_inbound_plan_pallets_response import ListInboundPlanPalletsResponse
from ..models.list_inbound_plans_response import ListInboundPlansResponse
from ..models.list_item_compliance_details_response import ListItemComplianceDetailsResponse
from ..models.list_packing_options_response import ListPackingOptionsResponse
from ..models.list_placement_options_response import ListPlacementOptionsResponse
from ..models.list_prep_details_response import ListPrepDetailsResponse
from ..models.list_shipment_content_update_previews_response import ListShipmentContentUpdatePreviewsResponse
from ..models.list_transportation_options_response import ListTransportationOptionsResponse
from ..models.schedule_self_ship_appointment_request import (
    ScheduleSelfShipAppointmentRequest,
    ScheduleSelfShipAppointmentRequestDict,
)
from ..models.schedule_self_ship_appointment_response import ScheduleSelfShipAppointmentResponse
from ..models.set_packing_information_request import SetPackingInformationRequest, SetPackingInformationRequestDict
from ..models.set_prep_details_request import SetPrepDetailsRequest, SetPrepDetailsRequestDict
from ..models.update_inbound_plan_name_request import UpdateInboundPlanNameRequest, UpdateInboundPlanNameRequestDict
from ..models.update_item_compliance_details_request import (
    UpdateItemComplianceDetailsRequest,
    UpdateItemComplianceDetailsRequestDict,
)
from ..models.update_shipment_name_request import UpdateShipmentNameRequest, UpdateShipmentNameRequestDict
from ..models.update_shipment_source_address_request import (
    UpdateShipmentSourceAddressRequest,
    UpdateShipmentSourceAddressRequestDict,
)
from ..models.update_shipment_tracking_details_request import (
    UpdateShipmentTrackingDetailsRequest,
    UpdateShipmentTrackingDetailsRequestDict,
)
from ..server.server import Server


class WfsInbound:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WfsInboundWithRawResponse(client, server, auth)

    def cancel_inbound_plan(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(self._with_raw_response.cancel_inbound_plan(inbound_plan_id, request_options=request_options))

    def cancel_self_ship_appointment(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.cancel_self_ship_appointment(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def confirm_delivery_window_options(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        delivery_window_option_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to confirm the delivery window option for.
            delivery_window_option_id: The ID of the delivery window option to be confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_delivery_window_options(
                inbound_plan_id, shipment_id, delivery_window_option_id, request_options=request_options
            ),
        )

    def confirm_packing_option(
        self, inbound_plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_option_id: Identifier of a packing option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_packing_option(
                inbound_plan_id, packing_option_id, request_options=request_options
            ),
        )

    def confirm_placement_option(
        self, inbound_plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            placement_option_id: The identifier of a placement option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_placement_option(
                inbound_plan_id, placement_option_id, request_options=request_options
            ),
        )

    def confirm_shipment_content_update_preview(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_shipment_content_update_preview(
                inbound_plan_id, shipment_id, content_update_preview_id, request_options=request_options
            ),
        )

    def confirm_transportation_options(
        self,
        inbound_plan_id: str,
        body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_transportation_options(
                inbound_plan_id, body, request_options=request_options
            ),
        )

    def create_inbound_plan(
        self,
        body: CreateInboundPlanRequest | CreateInboundPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
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
                ``CommonErrorList | RawError``."""
        return unwrap(self._with_raw_response.create_marketplace_item_labels(body, request_options=request_options))

    def generate_delivery_window_options(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to generate delivery window options for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.generate_delivery_window_options(
                inbound_plan_id, shipment_id, request_options=request_options
            ),
        )

    def generate_packing_options(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.generate_packing_options(inbound_plan_id, request_options=request_options)
        )

    def generate_placement_options(
        self,
        inbound_plan_id: str,
        body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.generate_placement_options(inbound_plan_id, body, request_options=request_options)
        )

    def generate_self_ship_appointment_slots(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.generate_self_ship_appointment_slots(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def generate_shipment_content_update_previews(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.generate_shipment_content_update_previews(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def generate_transportation_options(
        self,
        inbound_plan_id: str,
        body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.generate_transportation_options(
                inbound_plan_id, body, request_options=request_options
            ),
        )

    def get_delivery_challan_document(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetDeliveryChallanDocumentResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.get_delivery_challan_document(
                inbound_plan_id, shipment_id, request_options=request_options
            ),
        )

    def get_inbound_operation_status(
        self, operation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommonInboundOperationStatus:
        """Send a ``GET`` request.

        Args:
            operation_id: Identifier of an asynchronous operation.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.get_inbound_operation_status(operation_id, request_options=request_options)
        )

    def get_inbound_plan(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InboundPlan:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_inbound_plan(inbound_plan_id, request_options=request_options))

    def get_self_ship_appointment_slots(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetSelfShipAppointmentSlotsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of self ship appointment slots to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.get_self_ship_appointment_slots(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def get_shipment(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommonShipment:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipment(inbound_plan_id, shipment_id, request_options=request_options)
        )

    def get_shipment_content_update_preview(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommonContentUpdatePreview:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipment_content_update_preview(
                inbound_plan_id, shipment_id, content_update_preview_id, request_options=request_options
            ),
        )

    def list_delivery_window_options(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDeliveryWindowOptionsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to get delivery window options for.
            page_size: The number of delivery window options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_delivery_window_options(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_inbound_plan_boxes(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanBoxesResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_inbound_plan_boxes(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def list_inbound_plan_items(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanItemsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_inbound_plan_items(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def list_inbound_plan_pallets(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanPalletsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_inbound_plan_pallets(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
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
        """Send a ``GET`` request.

        Args:
            page_size: The number of inbound plans to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            status: The status of an inbound plan. Possible values: ``ACTIVE``, ``VOIDED``, ``SHIPPED``, ``ERRORED``.
            sort_by: Sort by field.
            sort_order: The sort order. Possible values: ``ASC``, ``DESC``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
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
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_item_compliance_details(mskus, marketplace_id, request_options=request_options)
        )

    def list_packing_group_boxes(
        self,
        inbound_plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanBoxesResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_packing_group_boxes(
                inbound_plan_id,
                packing_group_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_packing_group_items(
        self,
        inbound_plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanItemsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_packing_group_items(
                inbound_plan_id,
                packing_group_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_packing_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPackingOptionsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of packing options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_packing_options(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    def list_placement_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPlacementOptionsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of placement options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_placement_options(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
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
                ``CommonErrorList | RawError``."""
        return unwrap(self._with_raw_response.list_prep_details(marketplace_id, mskus, request_options=request_options))

    def list_shipment_boxes(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanBoxesResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_shipment_boxes(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_shipment_content_update_previews(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentContentUpdatePreviewsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of content update previews to return.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_shipment_content_update_previews(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_shipment_items(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanItemsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_shipment_items(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_shipment_pallets(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanPalletsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_shipment_pallets(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def list_transportation_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        placement_option_id: str | None = None,
        shipment_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTransportationOptionsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
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
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_transportation_options(
                inbound_plan_id,
                page_size=page_size,
                pagination_token=pagination_token,
                placement_option_id=placement_option_id,
                shipment_id=shipment_id,
                request_options=request_options,
            ),
        )

    def schedule_self_ship_appointment(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        slot_id: str,
        body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduleSelfShipAppointmentResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            slot_id: An identifier to a self-ship appointment slot.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.schedule_self_ship_appointment(
                inbound_plan_id, shipment_id, slot_id, body, request_options=request_options
            ),
        )

    def set_packing_information(
        self,
        inbound_plan_id: str,
        body: SetPackingInformationRequest | SetPackingInformationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.set_packing_information(inbound_plan_id, body, request_options=request_options)
        )

    def set_prep_details(
        self,
        body: SetPrepDetailsRequest | SetPrepDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(self._with_raw_response.set_prep_details(body, request_options=request_options))

    def update_inbound_plan_name(
        self,
        inbound_plan_id: str,
        body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No content — name updated successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.update_inbound_plan_name(inbound_plan_id, body, request_options=request_options)
        )

    def update_item_compliance_details(
        self,
        marketplace_id: str,
        body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
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
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.update_item_compliance_details(
                marketplace_id, body, request_options=request_options
            ),
        )

    def update_shipment_name(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No content — name updated successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.update_shipment_name(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def update_shipment_source_address(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.update_shipment_source_address(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    def update_shipment_tracking_details(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.update_shipment_tracking_details(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> WfsInboundWithRawResponse:
        return self._with_raw_response


class AsyncWfsInbound:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWfsInboundWithRawResponse(client, server, auth)

    async def cancel_inbound_plan(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_inbound_plan(inbound_plan_id, request_options=request_options)
        )

    async def cancel_self_ship_appointment(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_self_ship_appointment(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def confirm_delivery_window_options(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        delivery_window_option_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to confirm the delivery window option for.
            delivery_window_option_id: The ID of the delivery window option to be confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_delivery_window_options(
                inbound_plan_id, shipment_id, delivery_window_option_id, request_options=request_options
            ),
        )

    async def confirm_packing_option(
        self, inbound_plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_option_id: Identifier of a packing option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_packing_option(
                inbound_plan_id, packing_option_id, request_options=request_options
            ),
        )

    async def confirm_placement_option(
        self, inbound_plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            placement_option_id: The identifier of a placement option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_placement_option(
                inbound_plan_id, placement_option_id, request_options=request_options
            ),
        )

    async def confirm_shipment_content_update_preview(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_shipment_content_update_preview(
                inbound_plan_id, shipment_id, content_update_preview_id, request_options=request_options
            ),
        )

    async def confirm_transportation_options(
        self,
        inbound_plan_id: str,
        body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_transportation_options(
                inbound_plan_id, body, request_options=request_options
            ),
        )

    async def create_inbound_plan(
        self,
        body: CreateInboundPlanRequest | CreateInboundPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
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
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.create_marketplace_item_labels(body, request_options=request_options)
        )

    async def generate_delivery_window_options(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to generate delivery window options for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_delivery_window_options(
                inbound_plan_id, shipment_id, request_options=request_options
            ),
        )

    async def generate_packing_options(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_packing_options(inbound_plan_id, request_options=request_options)
        )

    async def generate_placement_options(
        self,
        inbound_plan_id: str,
        body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_placement_options(
                inbound_plan_id, body, request_options=request_options
            ),
        )

    async def generate_self_ship_appointment_slots(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_self_ship_appointment_slots(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def generate_shipment_content_update_previews(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_shipment_content_update_previews(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def generate_transportation_options(
        self,
        inbound_plan_id: str,
        body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.generate_transportation_options(
                inbound_plan_id, body, request_options=request_options
            ),
        )

    async def get_delivery_challan_document(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetDeliveryChallanDocumentResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_delivery_challan_document(
                inbound_plan_id, shipment_id, request_options=request_options
            ),
        )

    async def get_inbound_operation_status(
        self, operation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommonInboundOperationStatus:
        """Send a ``GET`` request.

        Args:
            operation_id: Identifier of an asynchronous operation.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_inbound_operation_status(operation_id, request_options=request_options)
        )

    async def get_inbound_plan(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> InboundPlan:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(await self._with_raw_response.get_inbound_plan(inbound_plan_id, request_options=request_options))

    async def get_self_ship_appointment_slots(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetSelfShipAppointmentSlotsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of self ship appointment slots to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_self_ship_appointment_slots(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def get_shipment(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CommonShipment:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipment(inbound_plan_id, shipment_id, request_options=request_options)
        )

    async def get_shipment_content_update_preview(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CommonContentUpdatePreview:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipment_content_update_preview(
                inbound_plan_id, shipment_id, content_update_preview_id, request_options=request_options
            ),
        )

    async def list_delivery_window_options(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDeliveryWindowOptionsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to get delivery window options for.
            page_size: The number of delivery window options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_delivery_window_options(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_inbound_plan_boxes(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanBoxesResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_inbound_plan_boxes(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def list_inbound_plan_items(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanItemsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_inbound_plan_items(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def list_inbound_plan_pallets(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanPalletsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_inbound_plan_pallets(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
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
        """Send a ``GET`` request.

        Args:
            page_size: The number of inbound plans to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            status: The status of an inbound plan. Possible values: ``ACTIVE``, ``VOIDED``, ``SHIPPED``, ``ERRORED``.
            sort_by: Sort by field.
            sort_order: The sort order. Possible values: ``ASC``, ``DESC``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
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
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_item_compliance_details(
                mskus, marketplace_id, request_options=request_options
            ),
        )

    async def list_packing_group_boxes(
        self,
        inbound_plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanBoxesResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_packing_group_boxes(
                inbound_plan_id,
                packing_group_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_packing_group_items(
        self,
        inbound_plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanItemsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_packing_group_items(
                inbound_plan_id,
                packing_group_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_packing_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPackingOptionsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of packing options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_packing_options(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
            ),
        )

    async def list_placement_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPlacementOptionsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of placement options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_placement_options(
                inbound_plan_id, page_size=page_size, pagination_token=pagination_token, request_options=request_options
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
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_prep_details(marketplace_id, mskus, request_options=request_options)
        )

    async def list_shipment_boxes(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanBoxesResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_shipment_boxes(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_shipment_content_update_previews(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListShipmentContentUpdatePreviewsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of content update previews to return.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_shipment_content_update_previews(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_shipment_items(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanItemsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_shipment_items(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_shipment_pallets(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInboundPlanPalletsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_shipment_pallets(
                inbound_plan_id,
                shipment_id,
                page_size=page_size,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def list_transportation_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        placement_option_id: str | None = None,
        shipment_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTransportationOptionsResponse:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
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
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_transportation_options(
                inbound_plan_id,
                page_size=page_size,
                pagination_token=pagination_token,
                placement_option_id=placement_option_id,
                shipment_id=shipment_id,
                request_options=request_options,
            ),
        )

    async def schedule_self_ship_appointment(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        slot_id: str,
        body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ScheduleSelfShipAppointmentResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            slot_id: An identifier to a self-ship appointment slot.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.schedule_self_ship_appointment(
                inbound_plan_id, shipment_id, slot_id, body, request_options=request_options
            ),
        )

    async def set_packing_information(
        self,
        inbound_plan_id: str,
        body: SetPackingInformationRequest | SetPackingInformationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.set_packing_information(
                inbound_plan_id, body, request_options=request_options
            ),
        )

    async def set_prep_details(
        self,
        body: SetPrepDetailsRequest | SetPrepDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(await self._with_raw_response.set_prep_details(body, request_options=request_options))

    async def update_inbound_plan_name(
        self,
        inbound_plan_id: str,
        body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No content — name updated successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.update_inbound_plan_name(
                inbound_plan_id, body, request_options=request_options
            ),
        )

    async def update_item_compliance_details(
        self,
        marketplace_id: str,
        body: UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
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
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.update_item_compliance_details(
                marketplace_id, body, request_options=request_options
            ),
        )

    async def update_shipment_name(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No content — name updated successfully.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.update_shipment_name(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def update_shipment_source_address(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.update_shipment_source_address(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    async def update_shipment_tracking_details(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInboundPlanResponse:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Accepted — operation submitted asynchronously.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``CommonErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.update_shipment_tracking_details(
                inbound_plan_id, shipment_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWfsInboundWithRawResponse:
        return self._with_raw_response


class WfsInboundWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_inbound_plan(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, CancelInboundPlanErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/cancellation"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=cancel_inbound_plan_error_mapper,
            request_options=request_options,
        )

    def cancel_self_ship_appointment(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, CancelSelfShipAppointmentErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentCancellation"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=cancel_self_ship_appointment_error_mapper,
            request_options=request_options,
        )

    def confirm_delivery_window_options(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        delivery_window_option_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmDeliveryWindowOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to confirm the delivery window option for.
            delivery_window_option_id: The ID of the delivery window option to be confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions/{deliveryWindowOptionId}/confirmation",
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id),
                param[str]("shipmentId", shipment_id),
                param[str]("deliveryWindowOptionId", delivery_window_option_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    def confirm_packing_option(
        self, inbound_plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmPackingOptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_option_id: Identifier of a packing option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions/{packingOptionId}/confirmation"
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id), param[str]("packingOptionId", packing_option_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_packing_option_error_mapper,
            request_options=request_options,
        )

    def confirm_placement_option(
        self, inbound_plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmPlacementOptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            placement_option_id: The identifier of a placement option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions/{placementOptionId}/confirmation"
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id), param[str]("placementOptionId", placement_option_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_placement_option_error_mapper,
            request_options=request_options,
        )

    def confirm_shipment_content_update_preview(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmShipmentContentUpdatePreviewErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}/confirmation",
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id),
                param[str]("shipmentId", shipment_id),
                param[str]("contentUpdatePreviewId", content_update_preview_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_shipment_content_update_preview_error_mapper,
            request_options=request_options,
        )

    def confirm_transportation_options(
        self,
        inbound_plan_id: str,
        body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmTransportationOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions/confirmation"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_transportation_options_error_mapper,
            request_options=request_options,
        )

    def create_inbound_plan(
        self,
        body: CreateInboundPlanRequest | CreateInboundPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInboundPlanResponse, CreateInboundPlanErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans"),
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
            url_template=self._server.default1("/inbound/wfs/v4/items/labels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateMarketplaceItemLabelsResponse],
            error_mapper=create_marketplace_item_labels_error_mapper,
            request_options=request_options,
        )

    def generate_delivery_window_options(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, GenerateDeliveryWindowOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to generate delivery window options for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    def generate_packing_options(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, GeneratePackingOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_packing_options_error_mapper,
            request_options=request_options,
        )

    def generate_placement_options(
        self,
        inbound_plan_id: str,
        body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, GeneratePlacementOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_placement_options_error_mapper,
            request_options=request_options,
        )

    def generate_self_ship_appointment_slots(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, GenerateSelfShipAppointmentSlotsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_self_ship_appointment_slots_error_mapper,
            request_options=request_options,
        )

    def generate_shipment_content_update_previews(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, GenerateShipmentContentUpdatePreviewsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict
            ](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_shipment_content_update_previews_error_mapper,
            request_options=request_options,
        )

    def generate_transportation_options(
        self,
        inbound_plan_id: str,
        body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, GenerateTransportationOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_transportation_options_error_mapper,
            request_options=request_options,
        )

    def get_delivery_challan_document(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetDeliveryChallanDocumentResponse, GetDeliveryChallanDocumentErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryChallanDocument"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetDeliveryChallanDocumentResponse],
            error_mapper=get_delivery_challan_document_error_mapper,
            request_options=request_options,
        )

    def get_inbound_operation_status(
        self, operation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommonInboundOperationStatus, GetInboundOperationStatusErrorBody]:
        """Send a ``GET`` request.

        Args:
            operation_id: Identifier of an asynchronous operation.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/operations/{operationId}"),
            path_params=[param[str]("operationId", operation_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CommonInboundOperationStatus],
            error_mapper=get_inbound_operation_status_error_mapper,
            request_options=request_options,
        )

    def get_inbound_plan(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InboundPlan, GetInboundPlanErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[InboundPlan],
            error_mapper=get_inbound_plan_error_mapper,
            request_options=request_options,
        )

    def get_self_ship_appointment_slots(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetSelfShipAppointmentSlotsResponse, GetSelfShipAppointmentSlotsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of self ship appointment slots to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetSelfShipAppointmentSlotsResponse],
            error_mapper=get_self_ship_appointment_slots_error_mapper,
            request_options=request_options,
        )

    def get_shipment(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommonShipment, GetShipmentErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CommonShipment],
            error_mapper=get_shipment_error_mapper,
            request_options=request_options,
        )

    def get_shipment_content_update_preview(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommonContentUpdatePreview, GetShipmentContentUpdatePreviewErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}",
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id),
                param[str]("shipmentId", shipment_id),
                param[str]("contentUpdatePreviewId", content_update_preview_id),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CommonContentUpdatePreview],
            error_mapper=get_shipment_content_update_preview_error_mapper,
            request_options=request_options,
        )

    def list_delivery_window_options(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDeliveryWindowOptionsResponse, ListDeliveryWindowOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to get delivery window options for.
            page_size: The number of delivery window options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
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
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanBoxesResponse, ListInboundPlanBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/boxes"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanItemsResponse, ListInboundPlanItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/items"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanPalletsResponse, ListInboundPlanPalletsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/pallets"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        """Send a ``GET`` request.

        Args:
            page_size: The number of inbound plans to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            status: The status of an inbound plan. Possible values: ``ACTIVE``, ``VOIDED``, ``SHIPPED``, ``ERRORED``.
            sort_by: Sort by field.
            sort_order: The sort order. Possible values: ``ASC``, ``DESC``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans"),
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
            url_template=self._server.default1("/inbound/wfs/v4/items/compliance"),
            query_params=[param[list[str]]("mskus", mskus), param[str]("marketplaceId", marketplace_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListItemComplianceDetailsResponse],
            error_mapper=list_item_compliance_details_error_mapper,
            request_options=request_options,
        )

    def list_packing_group_boxes(
        self,
        inbound_plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanBoxesResponse, ListPackingGroupBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/boxes"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("packingGroupId", packing_group_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlanBoxesResponse],
            error_mapper=list_packing_group_boxes_error_mapper,
            request_options=request_options,
        )

    def list_packing_group_items(
        self,
        inbound_plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanItemsResponse, ListPackingGroupItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/items"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("packingGroupId", packing_group_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlanItemsResponse],
            error_mapper=list_packing_group_items_error_mapper,
            request_options=request_options,
        )

    def list_packing_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPackingOptionsResponse, ListPackingOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of packing options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPlacementOptionsResponse, ListPlacementOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of placement options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
            url_template=self._server.default1("/inbound/wfs/v4/items/prepDetails"),
            query_params=[param[str]("marketplaceId", marketplace_id), param[list[str]]("mskus", mskus)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListPrepDetailsResponse],
            error_mapper=list_prep_details_error_mapper,
            request_options=request_options,
        )

    def list_shipment_boxes(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanBoxesResponse, ListShipmentBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/boxes"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlanBoxesResponse],
            error_mapper=list_shipment_boxes_error_mapper,
            request_options=request_options,
        )

    def list_shipment_content_update_previews(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentContentUpdatePreviewsResponse, ListShipmentContentUpdatePreviewsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of content update previews to return.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
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
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanItemsResponse, ListShipmentItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/items"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlanItemsResponse],
            error_mapper=list_shipment_items_error_mapper,
            request_options=request_options,
        )

    def list_shipment_pallets(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanPalletsResponse, ListShipmentPalletsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/pallets"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListInboundPlanPalletsResponse],
            error_mapper=list_shipment_pallets_error_mapper,
            request_options=request_options,
        )

    def list_transportation_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        placement_option_id: str | None = None,
        shipment_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTransportationOptionsResponse, ListTransportationOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
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
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        inbound_plan_id: str,
        shipment_id: str,
        slot_id: str,
        body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduleSelfShipAppointmentResponse, ScheduleSelfShipAppointmentErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            slot_id: An identifier to a self-ship appointment slot.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots/{slotId}/schedule",
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id),
                param[str]("shipmentId", shipment_id),
                param[str]("slotId", slot_id),
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
        inbound_plan_id: str,
        body: SetPackingInformationRequest | SetPackingInformationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, SetPackingInformationErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingInformation"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetPackingInformationRequest | SetPackingInformationRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=set_packing_information_error_mapper,
            request_options=request_options,
        )

    def set_prep_details(
        self,
        body: SetPrepDetailsRequest | SetPrepDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, SetPrepDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/items/prepDetails"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetPrepDetailsRequest | SetPrepDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=set_prep_details_error_mapper,
            request_options=request_options,
        )

    def update_inbound_plan_name(
        self,
        inbound_plan_id: str,
        body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateInboundPlanNameErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/name"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
    ) -> ApiResult[CancelInboundPlanResponse, UpdateItemComplianceDetailsErrorBody]:
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
            url_template=self._server.default1("/inbound/wfs/v4/items/compliance"),
            query_params=[param[str]("marketplaceId", marketplace_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=update_item_compliance_details_error_mapper,
            request_options=request_options,
        )

    def update_shipment_name(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateShipmentNameErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/name"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentNameRequest | UpdateShipmentNameRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=empty_response,
            error_mapper=update_shipment_name_error_mapper,
            request_options=request_options,
        )

    def update_shipment_source_address(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, UpdateShipmentSourceAddressErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/sourceAddress"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=update_shipment_source_address_error_mapper,
            request_options=request_options,
        )

    def update_shipment_tracking_details(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, UpdateShipmentTrackingDetailsErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/trackingDetails"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelInboundPlanResponse],
            error_mapper=update_shipment_tracking_details_error_mapper,
            request_options=request_options,
        )


class AsyncWfsInboundWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_inbound_plan(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, CancelInboundPlanErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/cancellation"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=cancel_inbound_plan_error_mapper,
            request_options=request_options,
        )

    async def cancel_self_ship_appointment(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, CancelSelfShipAppointmentErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentCancellation"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelSelfShipAppointmentRequest | CancelSelfShipAppointmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=cancel_self_ship_appointment_error_mapper,
            request_options=request_options,
        )

    async def confirm_delivery_window_options(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        delivery_window_option_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmDeliveryWindowOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to confirm the delivery window option for.
            delivery_window_option_id: The ID of the delivery window option to be confirmed.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions/{deliveryWindowOptionId}/confirmation",
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id),
                param[str]("shipmentId", shipment_id),
                param[str]("deliveryWindowOptionId", delivery_window_option_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    async def confirm_packing_option(
        self, inbound_plan_id: str, packing_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmPackingOptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_option_id: Identifier of a packing option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions/{packingOptionId}/confirmation"
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id), param[str]("packingOptionId", packing_option_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_packing_option_error_mapper,
            request_options=request_options,
        )

    async def confirm_placement_option(
        self, inbound_plan_id: str, placement_option_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmPlacementOptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            placement_option_id: The identifier of a placement option.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions/{placementOptionId}/confirmation"
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id), param[str]("placementOptionId", placement_option_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_placement_option_error_mapper,
            request_options=request_options,
        )

    async def confirm_shipment_content_update_preview(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmShipmentContentUpdatePreviewErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}/confirmation",
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id),
                param[str]("shipmentId", shipment_id),
                param[str]("contentUpdatePreviewId", content_update_preview_id),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_shipment_content_update_preview_error_mapper,
            request_options=request_options,
        )

    async def confirm_transportation_options(
        self,
        inbound_plan_id: str,
        body: ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, ConfirmTransportationOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions/confirmation"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ConfirmTransportationOptionsRequest | ConfirmTransportationOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=confirm_transportation_options_error_mapper,
            request_options=request_options,
        )

    async def create_inbound_plan(
        self,
        body: CreateInboundPlanRequest | CreateInboundPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInboundPlanResponse, CreateInboundPlanErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans"),
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
            url_template=self._server.default1("/inbound/wfs/v4/items/labels"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateMarketplaceItemLabelsRequest | CreateMarketplaceItemLabelsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateMarketplaceItemLabelsResponse],
            error_mapper=create_marketplace_item_labels_error_mapper,
            request_options=request_options,
        )

    async def generate_delivery_window_options(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, GenerateDeliveryWindowOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to generate delivery window options for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_delivery_window_options_error_mapper,
            request_options=request_options,
        )

    async def generate_packing_options(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelInboundPlanResponse, GeneratePackingOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_packing_options_error_mapper,
            request_options=request_options,
        )

    async def generate_placement_options(
        self,
        inbound_plan_id: str,
        body: GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, GeneratePlacementOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeneratePlacementOptionsRequest | GeneratePlacementOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_placement_options_error_mapper,
            request_options=request_options,
        )

    async def generate_self_ship_appointment_slots(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, GenerateSelfShipAppointmentSlotsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateSelfShipAppointmentSlotsRequest | GenerateSelfShipAppointmentSlotsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_self_ship_appointment_slots_error_mapper,
            request_options=request_options,
        )

    async def generate_shipment_content_update_previews(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, GenerateShipmentContentUpdatePreviewsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                GenerateShipmentContentUpdatePreviewsRequest | GenerateShipmentContentUpdatePreviewsRequestDict
            ](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_shipment_content_update_previews_error_mapper,
            request_options=request_options,
        )

    async def generate_transportation_options(
        self,
        inbound_plan_id: str,
        body: GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, GenerateTransportationOptionsErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GenerateTransportationOptionsRequest | GenerateTransportationOptionsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=generate_transportation_options_error_mapper,
            request_options=request_options,
        )

    async def get_delivery_challan_document(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetDeliveryChallanDocumentResponse, GetDeliveryChallanDocumentErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryChallanDocument"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetDeliveryChallanDocumentResponse],
            error_mapper=get_delivery_challan_document_error_mapper,
            request_options=request_options,
        )

    async def get_inbound_operation_status(
        self, operation_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommonInboundOperationStatus, GetInboundOperationStatusErrorBody]:
        """Send a ``GET`` request.

        Args:
            operation_id: Identifier of an asynchronous operation.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/operations/{operationId}"),
            path_params=[param[str]("operationId", operation_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CommonInboundOperationStatus],
            error_mapper=get_inbound_operation_status_error_mapper,
            request_options=request_options,
        )

    async def get_inbound_plan(
        self, inbound_plan_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InboundPlan, GetInboundPlanErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[InboundPlan],
            error_mapper=get_inbound_plan_error_mapper,
            request_options=request_options,
        )

    async def get_self_ship_appointment_slots(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetSelfShipAppointmentSlotsResponse, GetSelfShipAppointmentSlotsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of self ship appointment slots to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetSelfShipAppointmentSlotsResponse],
            error_mapper=get_self_ship_appointment_slots_error_mapper,
            request_options=request_options,
        )

    async def get_shipment(
        self, inbound_plan_id: str, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CommonShipment, GetShipmentErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CommonShipment],
            error_mapper=get_shipment_error_mapper,
            request_options=request_options,
        )

    async def get_shipment_content_update_preview(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        content_update_preview_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CommonContentUpdatePreview, GetShipmentContentUpdatePreviewErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            content_update_preview_id: Identifier of a content update preview.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews/{contentUpdatePreviewId}",
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id),
                param[str]("shipmentId", shipment_id),
                param[str]("contentUpdatePreviewId", content_update_preview_id),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CommonContentUpdatePreview],
            error_mapper=get_shipment_content_update_preview_error_mapper,
            request_options=request_options,
        )

    async def list_delivery_window_options(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDeliveryWindowOptionsResponse, ListDeliveryWindowOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: The shipment to get delivery window options for.
            page_size: The number of delivery window options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/deliveryWindowOptions"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
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
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanBoxesResponse, ListInboundPlanBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/boxes"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanItemsResponse, ListInboundPlanItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/items"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanPalletsResponse, ListInboundPlanPalletsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/pallets"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        """Send a ``GET`` request.

        Args:
            page_size: The number of inbound plans to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            status: The status of an inbound plan. Possible values: ``ACTIVE``, ``VOIDED``, ``SHIPPED``, ``ERRORED``.
            sort_by: Sort by field.
            sort_order: The sort order. Possible values: ``ASC``, ``DESC``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans"),
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
            url_template=self._server.default1("/inbound/wfs/v4/items/compliance"),
            query_params=[param[list[str]]("mskus", mskus), param[str]("marketplaceId", marketplace_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListItemComplianceDetailsResponse],
            error_mapper=list_item_compliance_details_error_mapper,
            request_options=request_options,
        )

    async def list_packing_group_boxes(
        self,
        inbound_plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanBoxesResponse, ListPackingGroupBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/boxes"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("packingGroupId", packing_group_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlanBoxesResponse],
            error_mapper=list_packing_group_boxes_error_mapper,
            request_options=request_options,
        )

    async def list_packing_group_items(
        self,
        inbound_plan_id: str,
        packing_group_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanItemsResponse, ListPackingGroupItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            packing_group_id: Identifier of a packing group.
            page_size: The number of packing group items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingGroups/{packingGroupId}/items"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("packingGroupId", packing_group_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlanItemsResponse],
            error_mapper=list_packing_group_items_error_mapper,
            request_options=request_options,
        )

    async def list_packing_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPackingOptionsResponse, ListPackingOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of packing options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPlacementOptionsResponse, ListPlacementOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            page_size: The number of placement options to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/placementOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
            url_template=self._server.default1("/inbound/wfs/v4/items/prepDetails"),
            query_params=[param[str]("marketplaceId", marketplace_id), param[list[str]]("mskus", mskus)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListPrepDetailsResponse],
            error_mapper=list_prep_details_error_mapper,
            request_options=request_options,
        )

    async def list_shipment_boxes(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanBoxesResponse, ListShipmentBoxesErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of boxes to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/boxes"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlanBoxesResponse],
            error_mapper=list_shipment_boxes_error_mapper,
            request_options=request_options,
        )

    async def list_shipment_content_update_previews(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListShipmentContentUpdatePreviewsResponse, ListShipmentContentUpdatePreviewsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of content update previews to return.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/contentUpdatePreviews"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
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
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanItemsResponse, ListShipmentItemsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment. A shipment contains the boxes and units being inbounded.
            page_size: The number of items to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/items"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlanItemsResponse],
            error_mapper=list_shipment_items_error_mapper,
            request_options=request_options,
        )

    async def list_shipment_pallets(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInboundPlanPalletsResponse, ListShipmentPalletsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            page_size: The number of pallets to return in the response matching the given query.
            pagination_token: A token to fetch a certain page when there are multiple pages worth of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/pallets"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            query_params=[
                param[int | None]("pageSize", page_size), param[str | None]("paginationToken", pagination_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListInboundPlanPalletsResponse],
            error_mapper=list_shipment_pallets_error_mapper,
            request_options=request_options,
        )

    async def list_transportation_options(
        self,
        inbound_plan_id: str,
        *,
        page_size: int | None = None,
        pagination_token: str | None = None,
        placement_option_id: str | None = None,
        shipment_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTransportationOptionsResponse, ListTransportationOptionsErrorBody]:
        """Send a ``GET`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
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
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/transportationOptions"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
        inbound_plan_id: str,
        shipment_id: str,
        slot_id: str,
        body: ScheduleSelfShipAppointmentRequest | ScheduleSelfShipAppointmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ScheduleSelfShipAppointmentResponse, ScheduleSelfShipAppointmentErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            slot_id: An identifier to a self-ship appointment slot.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/selfShipAppointmentSlots/{slotId}/schedule",
            ),
            path_params=[
                param[str]("inboundPlanId", inbound_plan_id),
                param[str]("shipmentId", shipment_id),
                param[str]("slotId", slot_id),
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
        inbound_plan_id: str,
        body: SetPackingInformationRequest | SetPackingInformationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, SetPackingInformationErrorBody]:
        """Send a ``POST`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/packingInformation"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetPackingInformationRequest | SetPackingInformationRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=set_packing_information_error_mapper,
            request_options=request_options,
        )

    async def set_prep_details(
        self,
        body: SetPrepDetailsRequest | SetPrepDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, SetPrepDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inbound/wfs/v4/items/prepDetails"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SetPrepDetailsRequest | SetPrepDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=set_prep_details_error_mapper,
            request_options=request_options,
        )

    async def update_inbound_plan_name(
        self,
        inbound_plan_id: str,
        body: UpdateInboundPlanNameRequest | UpdateInboundPlanNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateInboundPlanNameErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/inbound/wfs/v4/inboundPlans/{inboundPlanId}/name"),
            path_params=[param[str]("inboundPlanId", inbound_plan_id)],
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
    ) -> ApiResult[CancelInboundPlanResponse, UpdateItemComplianceDetailsErrorBody]:
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
            url_template=self._server.default1("/inbound/wfs/v4/items/compliance"),
            query_params=[param[str]("marketplaceId", marketplace_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateItemComplianceDetailsRequest | UpdateItemComplianceDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=update_item_compliance_details_error_mapper,
            request_options=request_options,
        )

    async def update_shipment_name(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentNameRequest | UpdateShipmentNameRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateShipmentNameErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/name"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentNameRequest | UpdateShipmentNameRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_empty_response,
            error_mapper=update_shipment_name_error_mapper,
            request_options=request_options,
        )

    async def update_shipment_source_address(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, UpdateShipmentSourceAddressErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/sourceAddress"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentSourceAddressRequest | UpdateShipmentSourceAddressRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=update_shipment_source_address_error_mapper,
            request_options=request_options,
        )

    async def update_shipment_tracking_details(
        self,
        inbound_plan_id: str,
        shipment_id: str,
        body: UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInboundPlanResponse, UpdateShipmentTrackingDetailsErrorBody]:
        """Send a ``PUT`` request.

        Args:
            inbound_plan_id: Identifier of an inbound plan.
            shipment_id: Identifier of a shipment.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1(
                "/inbound/wfs/v4/inboundPlans/{inboundPlanId}/shipments/{shipmentId}/trackingDetails"
            ),
            path_params=[param[str]("inboundPlanId", inbound_plan_id), param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentTrackingDetailsRequest | UpdateShipmentTrackingDetailsRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelInboundPlanResponse],
            error_mapper=update_shipment_tracking_details_error_mapper,
            request_options=request_options,
        )
