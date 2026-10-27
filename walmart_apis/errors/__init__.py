from .acknowledge_order_error import AcknowledgeOrderErrorBody, acknowledge_order_error_mapper
from .authorize_error import AuthorizeErrorBody, authorize_error_mapper
from .bulk_update_inventory_error import BulkUpdateInventoryErrorBody, bulk_update_inventory_error_mapper
from .cancel_feed_error import CancelFeedErrorBody, cancel_feed_error_mapper
from .cancel_fulfillment_order_error import CancelFulfillmentOrderErrorBody, cancel_fulfillment_order_error_mapper
from .cancel_inbound_plan_error import CancelInboundPlanErrorBody, cancel_inbound_plan_error_mapper
from .cancel_order_lines_error import CancelOrderLinesErrorBody, cancel_order_lines_error_mapper
from .cancel_query_error import CancelQueryErrorBody, cancel_query_error_mapper
from .cancel_report_error import CancelReportErrorBody, cancel_report_error_mapper
from .cancel_report_schedule_error import CancelReportScheduleErrorBody, cancel_report_schedule_error_mapper
from .cancel_self_ship_appointment_error import (
    CancelSelfShipAppointmentErrorBody,
    cancel_self_ship_appointment_error_mapper,
)
from .cancel_shipment2_error import CancelShipment2ErrorBody, cancel_shipment2_error_mapper
from .cancel_shipment_error import CancelShipmentErrorBody, cancel_shipment_error_mapper
from .check_dispute_eligibility_error import CheckDisputeEligibilityErrorBody, check_dispute_eligibility_error_mapper
from .check_download_report_by_period_error import (
    CheckDownloadReportByPeriodErrorBody,
    check_download_report_by_period_error_mapper,
)
from .configure_auto_payout_error import ConfigureAutoPayoutErrorBody, configure_auto_payout_error_mapper
from .confirm_customization_details_error import (
    ConfirmCustomizationDetailsErrorBody,
    confirm_customization_details_error_mapper,
)
from .confirm_delivery_window_options_error import (
    ConfirmDeliveryWindowOptionsErrorBody,
    confirm_delivery_window_options_error_mapper,
)
from .confirm_packing_option_error import ConfirmPackingOptionErrorBody, confirm_packing_option_error_mapper
from .confirm_placement_option_error import ConfirmPlacementOptionErrorBody, confirm_placement_option_error_mapper
from .confirm_shipment_content_update_preview_error import (
    ConfirmShipmentContentUpdatePreviewErrorBody,
    confirm_shipment_content_update_preview_error_mapper,
)
from .confirm_transportation_options_error import (
    ConfirmTransportationOptionsErrorBody,
    confirm_transportation_options_error_mapper,
)
from .create_confirm_delivery_details_error import (
    CreateConfirmDeliveryDetailsErrorBody,
    create_confirm_delivery_details_error_mapper,
)
from .create_confirm_order_details_error import (
    CreateConfirmOrderDetailsErrorBody,
    create_confirm_order_details_error_mapper,
)
from .create_confirm_service_details_error import (
    CreateConfirmServiceDetailsErrorBody,
    create_confirm_service_details_error_mapper,
)
from .create_destination_error import CreateDestinationErrorBody, create_destination_error_mapper
from .create_digital_access_key_error import CreateDigitalAccessKeyErrorBody, create_digital_access_key_error_mapper
from .create_feed_error import CreateFeedErrorBody, create_feed_error_mapper
from .create_fulfillment_order_error import CreateFulfillmentOrderErrorBody, create_fulfillment_order_error_mapper
from .create_inbound_plan_error import CreateInboundPlanErrorBody, create_inbound_plan_error_mapper
from .create_legal_disclosure_error import CreateLegalDisclosureErrorBody, create_legal_disclosure_error_mapper
from .create_marketplace_item_labels_error import (
    CreateMarketplaceItemLabelsErrorBody,
    create_marketplace_item_labels_error_mapper,
)
from .create_product_review_and_seller_feedback_solicitation_error import (
    CreateProductReviewAndSellerFeedbackSolicitationErrorBody,
    create_product_review_and_seller_feedback_solicitation_error_mapper,
)
from .create_query_error import CreateQueryErrorBody, create_query_error_mapper
from .create_report_error import CreateReportErrorBody, create_report_error_mapper
from .create_report_schedule_error import CreateReportScheduleErrorBody, create_report_schedule_error_mapper
from .create_shipment_error import CreateShipmentErrorBody, create_shipment_error_mapper
from .create_subscription_error import CreateSubscriptionErrorBody, create_subscription_error_mapper
from .create_token_error import CreateTokenErrorBody, create_token_error_mapper
from .create_unexpected_problem_error import CreateUnexpectedProblemErrorBody, create_unexpected_problem_error_mapper
from .create_upload_destination_for_resource_error import (
    CreateUploadDestinationForResourceErrorBody,
    create_upload_destination_for_resource_error_mapper,
)
from .create_warranty_error import CreateWarrantyErrorBody, create_warranty_error_mapper
from .delete_destination_error import DeleteDestinationErrorBody, delete_destination_error_mapper
from .delete_listings_item_error import DeleteListingsItemErrorBody, delete_listings_item_error_mapper
from .delete_subscription_by_id_error import DeleteSubscriptionByIdErrorBody, delete_subscription_by_id_error_mapper
from .deliver_order_lines_error import DeliverOrderLinesErrorBody, deliver_order_lines_error_mapper
from .download_new_report_error import DownloadNewReportErrorBody, download_new_report_error_mapper
from .download_old_report_error import DownloadOldReportErrorBody, download_old_report_error_mapper
from .download_reconciliation_report_error import (
    DownloadReconciliationReportErrorBody,
    download_reconciliation_report_error_mapper,
)
from .generate_delivery_window_options_error import (
    GenerateDeliveryWindowOptionsErrorBody,
    generate_delivery_window_options_error_mapper,
)
from .generate_packing_options_error import GeneratePackingOptionsErrorBody, generate_packing_options_error_mapper
from .generate_placement_options_error import GeneratePlacementOptionsErrorBody, generate_placement_options_error_mapper
from .generate_self_ship_appointment_slots_error import (
    GenerateSelfShipAppointmentSlotsErrorBody,
    generate_self_ship_appointment_slots_error_mapper,
)
from .generate_shipment_content_update_previews_error import (
    GenerateShipmentContentUpdatePreviewsErrorBody,
    generate_shipment_content_update_previews_error_mapper,
)
from .generate_transportation_options_error import (
    GenerateTransportationOptionsErrorBody,
    generate_transportation_options_error_mapper,
)
from .get_access_points_error import GetAccessPointsErrorBody, get_access_points_error_mapper
from .get_account_error import GetAccountErrorBody, get_account_error_mapper
from .get_additional_inputs_error import GetAdditionalInputsErrorBody, get_additional_inputs_error_mapper
from .get_annual_statement_opts_error import GetAnnualStatementOptsErrorBody, get_annual_statement_opts_error_mapper
from .get_attributes_error import GetAttributesErrorBody, get_attributes_error_mapper
from .get_catalog_item_error import GetCatalogItemErrorBody, get_catalog_item_error_mapper
from .get_competitive_pricing_error import GetCompetitivePricingErrorBody, get_competitive_pricing_error_mapper
from .get_competitive_summary_error import GetCompetitiveSummaryErrorBody, get_competitive_summary_error_mapper
from .get_definitions_product_type_error import (
    GetDefinitionsProductTypeErrorBody,
    get_definitions_product_type_error_mapper,
)
from .get_delivery_challan_document_error import (
    GetDeliveryChallanDocumentErrorBody,
    get_delivery_challan_document_error_mapper,
)
from .get_destination_error import GetDestinationErrorBody, get_destination_error_mapper
from .get_destinations_error import GetDestinationsErrorBody, get_destinations_error_mapper
from .get_document_error import GetDocumentErrorBody, get_document_error_mapper
from .get_eligible_shipping_services_error import (
    GetEligibleShippingServicesErrorBody,
    get_eligible_shipping_services_error_mapper,
)
from .get_faster_payout_eligibility_error import (
    GetFasterPayoutEligibilityErrorBody,
    get_faster_payout_eligibility_error_mapper,
)
from .get_featured_offer_expected_price_batch_error import (
    GetFeaturedOfferExpectedPriceBatchErrorBody,
    get_featured_offer_expected_price_batch_error_mapper,
)
from .get_feed_document_error import GetFeedDocumentErrorBody, get_feed_document_error_mapper
from .get_feed_error import GetFeedErrorBody, get_feed_error_mapper
from .get_feeds_error import GetFeedsErrorBody, get_feeds_error_mapper
from .get_final_payout_case_status_error import (
    GetFinalPayoutCaseStatusErrorBody,
    get_final_payout_case_status_error_mapper,
)
from .get_fulfillment_order_error import GetFulfillmentOrderErrorBody, get_fulfillment_order_error_mapper
from .get_fulfillment_order_shipments_error import (
    GetFulfillmentOrderShipmentsErrorBody,
    get_fulfillment_order_shipments_error_mapper,
)
from .get_fulfillment_preview_error import GetFulfillmentPreviewErrorBody, get_fulfillment_preview_error_mapper
from .get_inbound_operation_status_error import (
    GetInboundOperationStatusErrorBody,
    get_inbound_operation_status_error_mapper,
)
from .get_inbound_plan_error import GetInboundPlanErrorBody, get_inbound_plan_error_mapper
from .get_inventory_for_sku_error import GetInventoryForSkuErrorBody, get_inventory_for_sku_error_mapper
from .get_inventory_summaries_error import GetInventorySummariesErrorBody, get_inventory_summaries_error_mapper
from .get_item_offers_batch_error import GetItemOffersBatchErrorBody, get_item_offers_batch_error_mapper
from .get_item_offers_error import GetItemOffersErrorBody, get_item_offers_error_mapper
from .get_label_error import GetLabelErrorBody, get_label_error_mapper
from .get_listing_offers_batch_error import GetListingOffersBatchErrorBody, get_listing_offers_batch_error_mapper
from .get_listing_offers_error import GetListingOffersErrorBody, get_listing_offers_error_mapper
from .get_listings_item_error import GetListingsItemErrorBody, get_listings_item_error_mapper
from .get_listings_restrictions_error import GetListingsRestrictionsErrorBody, get_listings_restrictions_error_mapper
from .get_marketplace_participations_error import (
    GetMarketplaceParticipationsErrorBody,
    get_marketplace_participations_error_mapper,
)
from .get_messaging_actions_for_order_error import (
    GetMessagingActionsForOrderErrorBody,
    get_messaging_actions_for_order_error_mapper,
)
from .get_my_fees_estimate_for_item_error import (
    GetMyFeesEstimateForItemErrorBody,
    get_my_fees_estimate_for_item_error_mapper,
)
from .get_my_fees_estimate_for_sku_error import (
    GetMyFeesEstimateForSkuErrorBody,
    get_my_fees_estimate_for_sku_error_mapper,
)
from .get_my_fees_estimates_error import GetMyFeesEstimatesErrorBody, get_my_fees_estimates_error_mapper
from .get_order_address_error import GetOrderAddressErrorBody, get_order_address_error_mapper
from .get_order_buyer_info_error import GetOrderBuyerInfoErrorBody, get_order_buyer_info_error_mapper
from .get_order_error import GetOrderErrorBody, get_order_error_mapper
from .get_order_items_error import GetOrderItemsErrorBody, get_order_items_error_mapper
from .get_order_metrics_error import GetOrderMetricsErrorBody, get_order_metrics_error_mapper
from .get_order_regulated_info_error import GetOrderRegulatedInfoErrorBody, get_order_regulated_info_error_mapper
from .get_orders_error import GetOrdersErrorBody, get_orders_error_mapper
from .get_payment_status_error import GetPaymentStatusErrorBody, get_payment_status_error_mapper
from .get_pricing_error import GetPricingErrorBody, get_pricing_error_mapper
from .get_queries_error import GetQueriesErrorBody, get_queries_error_mapper
from .get_query_error import GetQueryErrorBody, get_query_error_mapper
from .get_rates_error import GetRatesErrorBody, get_rates_error_mapper
from .get_report_document_error import GetReportDocumentErrorBody, get_report_document_error_mapper
from .get_report_error import GetReportErrorBody, get_report_error_mapper
from .get_report_schedule_error import GetReportScheduleErrorBody, get_report_schedule_error_mapper
from .get_report_schedules_error import GetReportSchedulesErrorBody, get_report_schedules_error_mapper
from .get_reports_error import GetReportsErrorBody, get_reports_error_mapper
from .get_self_ship_appointment_slots_error import (
    GetSelfShipAppointmentSlotsErrorBody,
    get_self_ship_appointment_slots_error_mapper,
)
from .get_shipment2_error import GetShipment2ErrorBody, get_shipment2_error_mapper
from .get_shipment_content_update_preview_error import (
    GetShipmentContentUpdatePreviewErrorBody,
    get_shipment_content_update_preview_error_mapper,
)
from .get_shipment_documents_error import GetShipmentDocumentsErrorBody, get_shipment_documents_error_mapper
from .get_shipment_error import GetShipmentErrorBody, get_shipment_error_mapper
from .get_solicitation_actions_for_order_error import (
    GetSolicitationActionsForOrderErrorBody,
    get_solicitation_actions_for_order_error_mapper,
)
from .get_subscription_by_id_error import GetSubscriptionByIdErrorBody, get_subscription_by_id_error_mapper
from .get_subscription_error import GetSubscriptionErrorBody, get_subscription_error_mapper
from .get_tracking_error import GetTrackingErrorBody, get_tracking_error_mapper
from .get_wfs_inventory_items_error import GetWfsInventoryItemsErrorBody, get_wfs_inventory_items_error_mapper
from .initiate_faster_payout_error import InitiateFasterPayoutErrorBody, initiate_faster_payout_error_mapper
from .list_all_fulfillment_orders_error import (
    ListAllFulfillmentOrdersErrorBody,
    list_all_fulfillment_orders_error_mapper,
)
from .list_delivery_window_options_error import (
    ListDeliveryWindowOptionsErrorBody,
    list_delivery_window_options_error_mapper,
)
from .list_financial_event_groups_error import (
    ListFinancialEventGroupsErrorBody,
    list_financial_event_groups_error_mapper,
)
from .list_financial_events_by_group_id_error import (
    ListFinancialEventsByGroupIdErrorBody,
    list_financial_events_by_group_id_error_mapper,
)
from .list_financial_events_by_order_id_error import (
    ListFinancialEventsByOrderIdErrorBody,
    list_financial_events_by_order_id_error_mapper,
)
from .list_financial_events_error import ListFinancialEventsErrorBody, list_financial_events_error_mapper
from .list_inbound_plan_boxes_error import ListInboundPlanBoxesErrorBody, list_inbound_plan_boxes_error_mapper
from .list_inbound_plan_items_error import ListInboundPlanItemsErrorBody, list_inbound_plan_items_error_mapper
from .list_inbound_plan_pallets_error import ListInboundPlanPalletsErrorBody, list_inbound_plan_pallets_error_mapper
from .list_inbound_plans_error import ListInboundPlansErrorBody, list_inbound_plans_error_mapper
from .list_item_compliance_details_error import (
    ListItemComplianceDetailsErrorBody,
    list_item_compliance_details_error_mapper,
)
from .list_packing_group_boxes_error import ListPackingGroupBoxesErrorBody, list_packing_group_boxes_error_mapper
from .list_packing_group_items_error import ListPackingGroupItemsErrorBody, list_packing_group_items_error_mapper
from .list_packing_options_error import ListPackingOptionsErrorBody, list_packing_options_error_mapper
from .list_placement_options_error import ListPlacementOptionsErrorBody, list_placement_options_error_mapper
from .list_prep_details_error import ListPrepDetailsErrorBody, list_prep_details_error_mapper
from .list_reconciliation_dates_error import ListReconciliationDatesErrorBody, list_reconciliation_dates_error_mapper
from .list_settlement_details_error import ListSettlementDetailsErrorBody, list_settlement_details_error_mapper
from .list_settlement_periods_error import ListSettlementPeriodsErrorBody, list_settlement_periods_error_mapper
from .list_shipment_boxes_error import ListShipmentBoxesErrorBody, list_shipment_boxes_error_mapper
from .list_shipment_content_update_previews_error import (
    ListShipmentContentUpdatePreviewsErrorBody,
    list_shipment_content_update_previews_error_mapper,
)
from .list_shipment_items_error import ListShipmentItemsErrorBody, list_shipment_items_error_mapper
from .list_shipment_pallets_error import ListShipmentPalletsErrorBody, list_shipment_pallets_error_mapper
from .list_transportation_options_error import (
    ListTransportationOptionsErrorBody,
    list_transportation_options_error_mapper,
)
from .one_click_shipment_error import OneClickShipmentErrorBody, one_click_shipment_error_mapper
from .patch_listings_item_error import PatchListingsItemErrorBody, patch_listings_item_error_mapper
from .purchase_shipment_error import PurchaseShipmentErrorBody, purchase_shipment_error_mapper
from .put_listings_item_error import PutListingsItemErrorBody, put_listings_item_error_mapper
from .refund_order_lines_error import RefundOrderLinesErrorBody, refund_order_lines_error_mapper
from .register_client_error import RegisterClientErrorBody, register_client_error_mapper
from .schedule_self_ship_appointment_error import (
    ScheduleSelfShipAppointmentErrorBody,
    schedule_self_ship_appointment_error_mapper,
)
from .search_catalog_items_error import SearchCatalogItemsErrorBody, search_catalog_items_error_mapper
from .search_definitions_product_types_error import (
    SearchDefinitionsProductTypesErrorBody,
    search_definitions_product_types_error_mapper,
)
from .search_listings_items_error import SearchListingsItemsErrorBody, search_listings_items_error_mapper
from .search_transactions_error import SearchTransactionsErrorBody, search_transactions_error_mapper
from .send_invoice_error import SendInvoiceErrorBody, send_invoice_error_mapper
from .send_test_notification_error import SendTestNotificationErrorBody, send_test_notification_error_mapper
from .set_packing_information_error import SetPackingInformationErrorBody, set_packing_information_error_mapper
from .set_prep_details_error import SetPrepDetailsErrorBody, set_prep_details_error_mapper
from .ship_order_lines_error import ShipOrderLinesErrorBody, ship_order_lines_error_mapper
from .ship_order_multi_package_error import ShipOrderMultiPackageErrorBody, ship_order_multi_package_error_mapper
from .submit_ndr_feedback_error import SubmitNdrFeedbackErrorBody, submit_ndr_feedback_error_mapper
from .update_final_payout_case_status_error import (
    UpdateFinalPayoutCaseStatusErrorBody,
    update_final_payout_case_status_error_mapper,
)
from .update_fulfillment_order_error import UpdateFulfillmentOrderErrorBody, update_fulfillment_order_error_mapper
from .update_inbound_plan_name_error import UpdateInboundPlanNameErrorBody, update_inbound_plan_name_error_mapper
from .update_inventory_for_sku_error import UpdateInventoryForSkuErrorBody, update_inventory_for_sku_error_mapper
from .update_item_compliance_details_error import (
    UpdateItemComplianceDetailsErrorBody,
    update_item_compliance_details_error_mapper,
)
from .update_shipment_name_error import UpdateShipmentNameErrorBody, update_shipment_name_error_mapper
from .update_shipment_source_address_error import (
    UpdateShipmentSourceAddressErrorBody,
    update_shipment_source_address_error_mapper,
)
from .update_shipment_status_error import UpdateShipmentStatusErrorBody, update_shipment_status_error_mapper
from .update_shipment_tracking_details_error import (
    UpdateShipmentTrackingDetailsErrorBody,
    update_shipment_tracking_details_error_mapper,
)
from .update_verification_status_error import UpdateVerificationStatusErrorBody, update_verification_status_error_mapper

__all__ = [
    "AcknowledgeOrderErrorBody",
    "AuthorizeErrorBody",
    "BulkUpdateInventoryErrorBody",
    "CancelFeedErrorBody",
    "CancelFulfillmentOrderErrorBody",
    "CancelInboundPlanErrorBody",
    "CancelOrderLinesErrorBody",
    "CancelQueryErrorBody",
    "CancelReportErrorBody",
    "CancelReportScheduleErrorBody",
    "CancelSelfShipAppointmentErrorBody",
    "CancelShipment2ErrorBody",
    "CancelShipmentErrorBody",
    "CheckDisputeEligibilityErrorBody",
    "CheckDownloadReportByPeriodErrorBody",
    "ConfigureAutoPayoutErrorBody",
    "ConfirmCustomizationDetailsErrorBody",
    "ConfirmDeliveryWindowOptionsErrorBody",
    "ConfirmPackingOptionErrorBody",
    "ConfirmPlacementOptionErrorBody",
    "ConfirmShipmentContentUpdatePreviewErrorBody",
    "ConfirmTransportationOptionsErrorBody",
    "CreateConfirmDeliveryDetailsErrorBody",
    "CreateConfirmOrderDetailsErrorBody",
    "CreateConfirmServiceDetailsErrorBody",
    "CreateDestinationErrorBody",
    "CreateDigitalAccessKeyErrorBody",
    "CreateFeedErrorBody",
    "CreateFulfillmentOrderErrorBody",
    "CreateInboundPlanErrorBody",
    "CreateLegalDisclosureErrorBody",
    "CreateMarketplaceItemLabelsErrorBody",
    "CreateProductReviewAndSellerFeedbackSolicitationErrorBody",
    "CreateQueryErrorBody",
    "CreateReportErrorBody",
    "CreateReportScheduleErrorBody",
    "CreateShipmentErrorBody",
    "CreateSubscriptionErrorBody",
    "CreateTokenErrorBody",
    "CreateUnexpectedProblemErrorBody",
    "CreateUploadDestinationForResourceErrorBody",
    "CreateWarrantyErrorBody",
    "DeleteDestinationErrorBody",
    "DeleteListingsItemErrorBody",
    "DeleteSubscriptionByIdErrorBody",
    "DeliverOrderLinesErrorBody",
    "DownloadNewReportErrorBody",
    "DownloadOldReportErrorBody",
    "DownloadReconciliationReportErrorBody",
    "GenerateDeliveryWindowOptionsErrorBody",
    "GeneratePackingOptionsErrorBody",
    "GeneratePlacementOptionsErrorBody",
    "GenerateSelfShipAppointmentSlotsErrorBody",
    "GenerateShipmentContentUpdatePreviewsErrorBody",
    "GenerateTransportationOptionsErrorBody",
    "GetAccessPointsErrorBody",
    "GetAccountErrorBody",
    "GetAdditionalInputsErrorBody",
    "GetAnnualStatementOptsErrorBody",
    "GetAttributesErrorBody",
    "GetCatalogItemErrorBody",
    "GetCompetitivePricingErrorBody",
    "GetCompetitiveSummaryErrorBody",
    "GetDefinitionsProductTypeErrorBody",
    "GetDeliveryChallanDocumentErrorBody",
    "GetDestinationErrorBody",
    "GetDestinationsErrorBody",
    "GetDocumentErrorBody",
    "GetEligibleShippingServicesErrorBody",
    "GetFasterPayoutEligibilityErrorBody",
    "GetFeaturedOfferExpectedPriceBatchErrorBody",
    "GetFeedDocumentErrorBody",
    "GetFeedErrorBody",
    "GetFeedsErrorBody",
    "GetFinalPayoutCaseStatusErrorBody",
    "GetFulfillmentOrderErrorBody",
    "GetFulfillmentOrderShipmentsErrorBody",
    "GetFulfillmentPreviewErrorBody",
    "GetInboundOperationStatusErrorBody",
    "GetInboundPlanErrorBody",
    "GetInventoryForSkuErrorBody",
    "GetInventorySummariesErrorBody",
    "GetItemOffersBatchErrorBody",
    "GetItemOffersErrorBody",
    "GetLabelErrorBody",
    "GetListingOffersBatchErrorBody",
    "GetListingOffersErrorBody",
    "GetListingsItemErrorBody",
    "GetListingsRestrictionsErrorBody",
    "GetMarketplaceParticipationsErrorBody",
    "GetMessagingActionsForOrderErrorBody",
    "GetMyFeesEstimateForItemErrorBody",
    "GetMyFeesEstimateForSkuErrorBody",
    "GetMyFeesEstimatesErrorBody",
    "GetOrderAddressErrorBody",
    "GetOrderBuyerInfoErrorBody",
    "GetOrderErrorBody",
    "GetOrderItemsErrorBody",
    "GetOrderMetricsErrorBody",
    "GetOrderRegulatedInfoErrorBody",
    "GetOrdersErrorBody",
    "GetPaymentStatusErrorBody",
    "GetPricingErrorBody",
    "GetQueriesErrorBody",
    "GetQueryErrorBody",
    "GetRatesErrorBody",
    "GetReportDocumentErrorBody",
    "GetReportErrorBody",
    "GetReportScheduleErrorBody",
    "GetReportSchedulesErrorBody",
    "GetReportsErrorBody",
    "GetSelfShipAppointmentSlotsErrorBody",
    "GetShipment2ErrorBody",
    "GetShipmentContentUpdatePreviewErrorBody",
    "GetShipmentDocumentsErrorBody",
    "GetShipmentErrorBody",
    "GetSolicitationActionsForOrderErrorBody",
    "GetSubscriptionByIdErrorBody",
    "GetSubscriptionErrorBody",
    "GetTrackingErrorBody",
    "GetWfsInventoryItemsErrorBody",
    "InitiateFasterPayoutErrorBody",
    "ListAllFulfillmentOrdersErrorBody",
    "ListDeliveryWindowOptionsErrorBody",
    "ListFinancialEventGroupsErrorBody",
    "ListFinancialEventsByGroupIdErrorBody",
    "ListFinancialEventsByOrderIdErrorBody",
    "ListFinancialEventsErrorBody",
    "ListInboundPlanBoxesErrorBody",
    "ListInboundPlanItemsErrorBody",
    "ListInboundPlanPalletsErrorBody",
    "ListInboundPlansErrorBody",
    "ListItemComplianceDetailsErrorBody",
    "ListPackingGroupBoxesErrorBody",
    "ListPackingGroupItemsErrorBody",
    "ListPackingOptionsErrorBody",
    "ListPlacementOptionsErrorBody",
    "ListPrepDetailsErrorBody",
    "ListReconciliationDatesErrorBody",
    "ListSettlementDetailsErrorBody",
    "ListSettlementPeriodsErrorBody",
    "ListShipmentBoxesErrorBody",
    "ListShipmentContentUpdatePreviewsErrorBody",
    "ListShipmentItemsErrorBody",
    "ListShipmentPalletsErrorBody",
    "ListTransportationOptionsErrorBody",
    "OneClickShipmentErrorBody",
    "PatchListingsItemErrorBody",
    "PurchaseShipmentErrorBody",
    "PutListingsItemErrorBody",
    "RefundOrderLinesErrorBody",
    "RegisterClientErrorBody",
    "ScheduleSelfShipAppointmentErrorBody",
    "SearchCatalogItemsErrorBody",
    "SearchDefinitionsProductTypesErrorBody",
    "SearchListingsItemsErrorBody",
    "SearchTransactionsErrorBody",
    "SendInvoiceErrorBody",
    "SendTestNotificationErrorBody",
    "SetPackingInformationErrorBody",
    "SetPrepDetailsErrorBody",
    "ShipOrderLinesErrorBody",
    "ShipOrderMultiPackageErrorBody",
    "SubmitNdrFeedbackErrorBody",
    "UpdateFinalPayoutCaseStatusErrorBody",
    "UpdateFulfillmentOrderErrorBody",
    "UpdateInboundPlanNameErrorBody",
    "UpdateInventoryForSkuErrorBody",
    "UpdateItemComplianceDetailsErrorBody",
    "UpdateShipmentNameErrorBody",
    "UpdateShipmentSourceAddressErrorBody",
    "UpdateShipmentStatusErrorBody",
    "UpdateShipmentTrackingDetailsErrorBody",
    "UpdateVerificationStatusErrorBody",
    "acknowledge_order_error_mapper",
    "authorize_error_mapper",
    "bulk_update_inventory_error_mapper",
    "cancel_feed_error_mapper",
    "cancel_fulfillment_order_error_mapper",
    "cancel_inbound_plan_error_mapper",
    "cancel_order_lines_error_mapper",
    "cancel_query_error_mapper",
    "cancel_report_error_mapper",
    "cancel_report_schedule_error_mapper",
    "cancel_self_ship_appointment_error_mapper",
    "cancel_shipment2_error_mapper",
    "cancel_shipment_error_mapper",
    "check_dispute_eligibility_error_mapper",
    "check_download_report_by_period_error_mapper",
    "configure_auto_payout_error_mapper",
    "confirm_customization_details_error_mapper",
    "confirm_delivery_window_options_error_mapper",
    "confirm_packing_option_error_mapper",
    "confirm_placement_option_error_mapper",
    "confirm_shipment_content_update_preview_error_mapper",
    "confirm_transportation_options_error_mapper",
    "create_confirm_delivery_details_error_mapper",
    "create_confirm_order_details_error_mapper",
    "create_confirm_service_details_error_mapper",
    "create_destination_error_mapper",
    "create_digital_access_key_error_mapper",
    "create_feed_error_mapper",
    "create_fulfillment_order_error_mapper",
    "create_inbound_plan_error_mapper",
    "create_legal_disclosure_error_mapper",
    "create_marketplace_item_labels_error_mapper",
    "create_product_review_and_seller_feedback_solicitation_error_mapper",
    "create_query_error_mapper",
    "create_report_error_mapper",
    "create_report_schedule_error_mapper",
    "create_shipment_error_mapper",
    "create_subscription_error_mapper",
    "create_token_error_mapper",
    "create_unexpected_problem_error_mapper",
    "create_upload_destination_for_resource_error_mapper",
    "create_warranty_error_mapper",
    "delete_destination_error_mapper",
    "delete_listings_item_error_mapper",
    "delete_subscription_by_id_error_mapper",
    "deliver_order_lines_error_mapper",
    "download_new_report_error_mapper",
    "download_old_report_error_mapper",
    "download_reconciliation_report_error_mapper",
    "generate_delivery_window_options_error_mapper",
    "generate_packing_options_error_mapper",
    "generate_placement_options_error_mapper",
    "generate_self_ship_appointment_slots_error_mapper",
    "generate_shipment_content_update_previews_error_mapper",
    "generate_transportation_options_error_mapper",
    "get_access_points_error_mapper",
    "get_account_error_mapper",
    "get_additional_inputs_error_mapper",
    "get_annual_statement_opts_error_mapper",
    "get_attributes_error_mapper",
    "get_catalog_item_error_mapper",
    "get_competitive_pricing_error_mapper",
    "get_competitive_summary_error_mapper",
    "get_definitions_product_type_error_mapper",
    "get_delivery_challan_document_error_mapper",
    "get_destination_error_mapper",
    "get_destinations_error_mapper",
    "get_document_error_mapper",
    "get_eligible_shipping_services_error_mapper",
    "get_faster_payout_eligibility_error_mapper",
    "get_featured_offer_expected_price_batch_error_mapper",
    "get_feed_document_error_mapper",
    "get_feed_error_mapper",
    "get_feeds_error_mapper",
    "get_final_payout_case_status_error_mapper",
    "get_fulfillment_order_error_mapper",
    "get_fulfillment_order_shipments_error_mapper",
    "get_fulfillment_preview_error_mapper",
    "get_inbound_operation_status_error_mapper",
    "get_inbound_plan_error_mapper",
    "get_inventory_for_sku_error_mapper",
    "get_inventory_summaries_error_mapper",
    "get_item_offers_batch_error_mapper",
    "get_item_offers_error_mapper",
    "get_label_error_mapper",
    "get_listing_offers_batch_error_mapper",
    "get_listing_offers_error_mapper",
    "get_listings_item_error_mapper",
    "get_listings_restrictions_error_mapper",
    "get_marketplace_participations_error_mapper",
    "get_messaging_actions_for_order_error_mapper",
    "get_my_fees_estimate_for_item_error_mapper",
    "get_my_fees_estimate_for_sku_error_mapper",
    "get_my_fees_estimates_error_mapper",
    "get_order_address_error_mapper",
    "get_order_buyer_info_error_mapper",
    "get_order_error_mapper",
    "get_order_items_error_mapper",
    "get_order_metrics_error_mapper",
    "get_order_regulated_info_error_mapper",
    "get_orders_error_mapper",
    "get_payment_status_error_mapper",
    "get_pricing_error_mapper",
    "get_queries_error_mapper",
    "get_query_error_mapper",
    "get_rates_error_mapper",
    "get_report_document_error_mapper",
    "get_report_error_mapper",
    "get_report_schedule_error_mapper",
    "get_report_schedules_error_mapper",
    "get_reports_error_mapper",
    "get_self_ship_appointment_slots_error_mapper",
    "get_shipment2_error_mapper",
    "get_shipment_content_update_preview_error_mapper",
    "get_shipment_documents_error_mapper",
    "get_shipment_error_mapper",
    "get_solicitation_actions_for_order_error_mapper",
    "get_subscription_by_id_error_mapper",
    "get_subscription_error_mapper",
    "get_tracking_error_mapper",
    "get_wfs_inventory_items_error_mapper",
    "initiate_faster_payout_error_mapper",
    "list_all_fulfillment_orders_error_mapper",
    "list_delivery_window_options_error_mapper",
    "list_financial_event_groups_error_mapper",
    "list_financial_events_by_group_id_error_mapper",
    "list_financial_events_by_order_id_error_mapper",
    "list_financial_events_error_mapper",
    "list_inbound_plan_boxes_error_mapper",
    "list_inbound_plan_items_error_mapper",
    "list_inbound_plan_pallets_error_mapper",
    "list_inbound_plans_error_mapper",
    "list_item_compliance_details_error_mapper",
    "list_packing_group_boxes_error_mapper",
    "list_packing_group_items_error_mapper",
    "list_packing_options_error_mapper",
    "list_placement_options_error_mapper",
    "list_prep_details_error_mapper",
    "list_reconciliation_dates_error_mapper",
    "list_settlement_details_error_mapper",
    "list_settlement_periods_error_mapper",
    "list_shipment_boxes_error_mapper",
    "list_shipment_content_update_previews_error_mapper",
    "list_shipment_items_error_mapper",
    "list_shipment_pallets_error_mapper",
    "list_transportation_options_error_mapper",
    "one_click_shipment_error_mapper",
    "patch_listings_item_error_mapper",
    "purchase_shipment_error_mapper",
    "put_listings_item_error_mapper",
    "refund_order_lines_error_mapper",
    "register_client_error_mapper",
    "schedule_self_ship_appointment_error_mapper",
    "search_catalog_items_error_mapper",
    "search_definitions_product_types_error_mapper",
    "search_listings_items_error_mapper",
    "search_transactions_error_mapper",
    "send_invoice_error_mapper",
    "send_test_notification_error_mapper",
    "set_packing_information_error_mapper",
    "set_prep_details_error_mapper",
    "ship_order_lines_error_mapper",
    "ship_order_multi_package_error_mapper",
    "submit_ndr_feedback_error_mapper",
    "update_final_payout_case_status_error_mapper",
    "update_fulfillment_order_error_mapper",
    "update_inbound_plan_name_error_mapper",
    "update_inventory_for_sku_error_mapper",
    "update_item_compliance_details_error_mapper",
    "update_shipment_name_error_mapper",
    "update_shipment_source_address_error_mapper",
    "update_shipment_status_error_mapper",
    "update_shipment_tracking_details_error_mapper",
    "update_verification_status_error_mapper",
]
