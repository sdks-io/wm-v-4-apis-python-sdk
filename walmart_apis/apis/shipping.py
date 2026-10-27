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
from ..errors.cancel_shipment2_error import CancelShipment2ErrorBody, cancel_shipment2_error_mapper
from ..errors.get_access_points_error import GetAccessPointsErrorBody, get_access_points_error_mapper
from ..errors.get_additional_inputs_error import GetAdditionalInputsErrorBody, get_additional_inputs_error_mapper
from ..errors.get_rates_error import GetRatesErrorBody, get_rates_error_mapper
from ..errors.get_shipment_documents_error import GetShipmentDocumentsErrorBody, get_shipment_documents_error_mapper
from ..errors.get_tracking_error import GetTrackingErrorBody, get_tracking_error_mapper
from ..errors.one_click_shipment_error import OneClickShipmentErrorBody, one_click_shipment_error_mapper
from ..errors.purchase_shipment_error import PurchaseShipmentErrorBody, purchase_shipment_error_mapper
from ..errors.submit_ndr_feedback_error import SubmitNdrFeedbackErrorBody, submit_ndr_feedback_error_mapper
from ..models.cancel_shipment_response1 import CancelShipmentResponse1
from ..models.enums.format1 import Format1OrStr
from ..models.get_access_points_response import GetAccessPointsResponse
from ..models.get_additional_inputs_response import GetAdditionalInputsResponse
from ..models.get_fulfillment_order_response import GetFulfillmentOrderResponse
from ..models.get_fulfillment_order_shipments_response import GetFulfillmentOrderShipmentsResponse
from ..models.get_rates_request import GetRatesRequest, GetRatesRequestDict
from ..models.get_shipment_documents_response import GetShipmentDocumentsResponse
from ..models.get_tracking_response import GetTrackingResponse
from ..models.one_click_shipment_request import OneClickShipmentRequest, OneClickShipmentRequestDict
from ..models.purchase_shipment_request import PurchaseShipmentRequest, PurchaseShipmentRequestDict
from ..models.submit_ndr_feedback_request import SubmitNdrFeedbackRequest, SubmitNdrFeedbackRequestDict
from ..server.server import Server


class Shipping:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ShippingWithRawResponse(client, server, auth)

    def cancel_shipment2(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelShipmentResponse1:
        """Cancels a shipment that has not yet shipped. Cancellation eligibility is carrier-dependent; refer to the
        response cancellation status to confirm.

        Args:
            shipment_id: Identifier of the shipment to cancel.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation processed

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.cancel_shipment2(shipment_id, request_options=request_options))

    def get_access_points(
        self,
        access_point_types: str,
        country_code: str,
        postal_code: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetAccessPointsResponse:
        """Returns access points (pickup and dropoff locations) near the supplied postal code and country, optionally
        filtered by access point type.

        Args:
            access_point_types: Comma-separated list of access point types to include.
            country_code: ISO 3166-1 alpha-2 country code (e.g. US, CA, MX).
            postal_code: Postal code to search around.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Access points returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_access_points(
                access_point_types, country_code, postal_code, request_options=request_options
            ),
        )

    def get_additional_inputs(
        self, rate_id: str, request_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetAdditionalInputsResponse:
        """Returns a JSON Schema document describing any carrier-and-service-specific inputs required to purchase a
        shipment for the supplied requestToken + rateId. The schema is served verbatim and the calling client should
        validate the seller's input against it before issuing purchaseShipment.

        Args:
            rate_id: rateId returned by a prior getRates response.
            request_token: requestToken returned by a prior getRates response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            JSON Schema for additional inputs returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_additional_inputs(rate_id, request_token, request_options=request_options)
        )

    def get_rates(
        self, body: GetRatesRequest | GetRatesRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetFulfillmentOrderResponse:
        """Returns a list of shipping rate quotes for the given shipment request. The seller can then call
        purchaseShipment with the selected rateId to commit to a label purchase.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Rate quotes returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_rates(body, request_options=request_options))

    def get_shipment_documents(
        self,
        shipment_id: str,
        *,
        package_client_reference_id: str | None = None,
        format_: Format1OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetShipmentDocumentsResponse:
        """Returns the label, customs, and other printable documents associated with a previously-purchased shipment.

        Args:
            shipment_id: Identifier of the shipment whose documents to retrieve.
            package_client_reference_id: Optional package-level reference id to retrieve documents for a specific
                package within a multi-package shipment.
            format_: Requested document format (defaults to PDF).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Documents returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_shipment_documents(
                shipment_id,
                package_client_reference_id=package_client_reference_id,
                format_=format_,
                request_options=request_options,
            ),
        )

    def get_tracking(
        self, tracking_id: str, *, carrier_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GetTrackingResponse:
        """Returns the current tracking status, event history, and any proof-of-delivery details for the given
        trackingId. TNT resolves carrier internally from the trackingId alone, so carrierId is optional -- confirmed
        unnecessary by the TNT/ Vulcan team (STRIDE-TNT-CORE-PACKAGE-SERVICES) 2026-08-19. When provided, it's used only
        as a defense-in-depth check against the resolved carrier; a mismatch surfaces as 404.

        Args:
            tracking_id: Tracking identifier returned by purchaseShipment.
            carrier_id: Optional carrier identifier for defense-in-depth validation against TNT's resolved carrier. Not
                required by TNT itself -- omit unless you specifically want mismatch protection.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Tracking details returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_tracking(tracking_id, carrier_id=carrier_id, request_options=request_options)
        )

    def one_click_shipment(
        self,
        body: OneClickShipmentRequest | OneClickShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFulfillmentOrderShipmentsResponse:
        """Convenience endpoint that combines rate quote and purchase into a single round trip when the seller already
        knows the desired service level. Returns the purchased shipment record directly.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Shipment purchased successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.one_click_shipment(body, request_options=request_options))

    def purchase_shipment(
        self,
        body: PurchaseShipmentRequest | PurchaseShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFulfillmentOrderShipmentsResponse:
        """Purchases the shipping label for the rate selected from a prior getRates response. Returns the shipment
        record with label document references.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Shipment purchased successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.purchase_shipment(body, request_options=request_options))

    def submit_ndr_feedback(
        self,
        body: SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Submits seller feedback on a non-delivery event for a shipment, instructing the carrier on how to proceed
        (return, reattempt, redirect, etc).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Feedback recorded successfully (no body)

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.submit_ndr_feedback(body, request_options=request_options))

    @property
    def with_raw_response(self) -> ShippingWithRawResponse:
        return self._with_raw_response


class AsyncShipping:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncShippingWithRawResponse(client, server, auth)

    async def cancel_shipment2(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelShipmentResponse1:
        """Cancels a shipment that has not yet shipped. Cancellation eligibility is carrier-dependent; refer to the
        response cancellation status to confirm.

        Args:
            shipment_id: Identifier of the shipment to cancel.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation processed

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.cancel_shipment2(shipment_id, request_options=request_options))

    async def get_access_points(
        self,
        access_point_types: str,
        country_code: str,
        postal_code: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetAccessPointsResponse:
        """Returns access points (pickup and dropoff locations) near the supplied postal code and country, optionally
        filtered by access point type.

        Args:
            access_point_types: Comma-separated list of access point types to include.
            country_code: ISO 3166-1 alpha-2 country code (e.g. US, CA, MX).
            postal_code: Postal code to search around.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Access points returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_access_points(
                access_point_types, country_code, postal_code, request_options=request_options
            ),
        )

    async def get_additional_inputs(
        self, rate_id: str, request_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetAdditionalInputsResponse:
        """Returns a JSON Schema document describing any carrier-and-service-specific inputs required to purchase a
        shipment for the supplied requestToken + rateId. The schema is served verbatim and the calling client should
        validate the seller's input against it before issuing purchaseShipment.

        Args:
            rate_id: rateId returned by a prior getRates response.
            request_token: requestToken returned by a prior getRates response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            JSON Schema for additional inputs returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_additional_inputs(rate_id, request_token, request_options=request_options)
        )

    async def get_rates(
        self, body: GetRatesRequest | GetRatesRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetFulfillmentOrderResponse:
        """Returns a list of shipping rate quotes for the given shipment request. The seller can then call
        purchaseShipment with the selected rateId to commit to a label purchase.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Rate quotes returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.get_rates(body, request_options=request_options))

    async def get_shipment_documents(
        self,
        shipment_id: str,
        *,
        package_client_reference_id: str | None = None,
        format_: Format1OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetShipmentDocumentsResponse:
        """Returns the label, customs, and other printable documents associated with a previously-purchased shipment.

        Args:
            shipment_id: Identifier of the shipment whose documents to retrieve.
            package_client_reference_id: Optional package-level reference id to retrieve documents for a specific
                package within a multi-package shipment.
            format_: Requested document format (defaults to PDF).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Documents returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_shipment_documents(
                shipment_id,
                package_client_reference_id=package_client_reference_id,
                format_=format_,
                request_options=request_options,
            ),
        )

    async def get_tracking(
        self, tracking_id: str, *, carrier_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GetTrackingResponse:
        """Returns the current tracking status, event history, and any proof-of-delivery details for the given
        trackingId. TNT resolves carrier internally from the trackingId alone, so carrierId is optional -- confirmed
        unnecessary by the TNT/ Vulcan team (STRIDE-TNT-CORE-PACKAGE-SERVICES) 2026-08-19. When provided, it's used only
        as a defense-in-depth check against the resolved carrier; a mismatch surfaces as 404.

        Args:
            tracking_id: Tracking identifier returned by purchaseShipment.
            carrier_id: Optional carrier identifier for defense-in-depth validation against TNT's resolved carrier. Not
                required by TNT itself -- omit unless you specifically want mismatch protection.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Tracking details returned successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_tracking(
                tracking_id, carrier_id=carrier_id, request_options=request_options
            ),
        )

    async def one_click_shipment(
        self,
        body: OneClickShipmentRequest | OneClickShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFulfillmentOrderShipmentsResponse:
        """Convenience endpoint that combines rate quote and purchase into a single round trip when the seller already
        knows the desired service level. Returns the purchased shipment record directly.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Shipment purchased successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.one_click_shipment(body, request_options=request_options))

    async def purchase_shipment(
        self,
        body: PurchaseShipmentRequest | PurchaseShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFulfillmentOrderShipmentsResponse:
        """Purchases the shipping label for the rate selected from a prior getRates response. Returns the shipment
        record with label document references.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Shipment purchased successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.purchase_shipment(body, request_options=request_options))

    async def submit_ndr_feedback(
        self,
        body: SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Submits seller feedback on a non-delivery event for a shipment, instructing the carrier on how to proceed
        (return, reattempt, redirect, etc).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Feedback recorded successfully (no body)

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.submit_ndr_feedback(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncShippingWithRawResponse:
        return self._with_raw_response


class ShippingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_shipment2(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelShipmentResponse1, CancelShipment2ErrorBody]:
        """Cancels a shipment that has not yet shipped. Cancellation eligibility is carrier-dependent; refer to the
        response cancellation status to confirm.

        Args:
            shipment_id: Identifier of the shipment to cancel.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/shipping/v4/shipments/{shipmentId}/cancel"),
            path_params=[param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelShipmentResponse1],
            error_mapper=cancel_shipment2_error_mapper,
            request_options=request_options,
        )

    def get_access_points(
        self,
        access_point_types: str,
        country_code: str,
        postal_code: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetAccessPointsResponse, GetAccessPointsErrorBody]:
        """Returns access points (pickup and dropoff locations) near the supplied postal code and country, optionally
        filtered by access point type.

        Args:
            access_point_types: Comma-separated list of access point types to include.
            country_code: ISO 3166-1 alpha-2 country code (e.g. US, CA, MX).
            postal_code: Postal code to search around.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/shipping/v4/accessPoints"),
            query_params=[
                param[str]("accessPointTypes", access_point_types),
                param[str]("countryCode", country_code),
                param[str]("postalCode", postal_code),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetAccessPointsResponse],
            error_mapper=get_access_points_error_mapper,
            request_options=request_options,
        )

    def get_additional_inputs(
        self, rate_id: str, request_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetAdditionalInputsResponse, GetAdditionalInputsErrorBody]:
        """Returns a JSON Schema document describing any carrier-and-service-specific inputs required to purchase a
        shipment for the supplied requestToken + rateId. The schema is served verbatim and the calling client should
        validate the seller's input against it before issuing purchaseShipment.

        Args:
            rate_id: rateId returned by a prior getRates response.
            request_token: requestToken returned by a prior getRates response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/shipping/v4/shipments/additionalInputs/schema"),
            query_params=[param[str]("rateId", rate_id), param[str]("requestToken", request_token)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetAdditionalInputsResponse],
            error_mapper=get_additional_inputs_error_mapper,
            request_options=request_options,
        )

    def get_rates(
        self, body: GetRatesRequest | GetRatesRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetFulfillmentOrderResponse, GetRatesErrorBody]:
        """Returns a list of shipping rate quotes for the given shipment request. The seller can then call
        purchaseShipment with the selected rateId to commit to a label purchase.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/shipping/v4/shipments/rates"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetRatesRequest | GetRatesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFulfillmentOrderResponse],
            error_mapper=get_rates_error_mapper,
            request_options=request_options,
        )

    def get_shipment_documents(
        self,
        shipment_id: str,
        *,
        package_client_reference_id: str | None = None,
        format_: Format1OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetShipmentDocumentsResponse, GetShipmentDocumentsErrorBody]:
        """Returns the label, customs, and other printable documents associated with a previously-purchased shipment.

        Args:
            shipment_id: Identifier of the shipment whose documents to retrieve.
            package_client_reference_id: Optional package-level reference id to retrieve documents for a specific
                package within a multi-package shipment.
            format_: Requested document format (defaults to PDF).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/shipping/v4/shipments/{shipmentId}/documents"),
            path_params=[param[str]("shipmentId", shipment_id)],
            query_params=[
                param[str | None]("packageClientReferenceId", package_client_reference_id),
                param[Format1OrStr | None]("format", format_),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetShipmentDocumentsResponse],
            error_mapper=get_shipment_documents_error_mapper,
            request_options=request_options,
        )

    def get_tracking(
        self, tracking_id: str, *, carrier_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTrackingResponse, GetTrackingErrorBody]:
        """Returns the current tracking status, event history, and any proof-of-delivery details for the given
        trackingId. TNT resolves carrier internally from the trackingId alone, so carrierId is optional -- confirmed
        unnecessary by the TNT/ Vulcan team (STRIDE-TNT-CORE-PACKAGE-SERVICES) 2026-08-19. When provided, it's used only
        as a defense-in-depth check against the resolved carrier; a mismatch surfaces as 404.

        Args:
            tracking_id: Tracking identifier returned by purchaseShipment.
            carrier_id: Optional carrier identifier for defense-in-depth validation against TNT's resolved carrier. Not
                required by TNT itself -- omit unless you specifically want mismatch protection.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/shipping/v4/tracking"),
            query_params=[param[str]("trackingId", tracking_id), param[str | None]("carrierId", carrier_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetTrackingResponse],
            error_mapper=get_tracking_error_mapper,
            request_options=request_options,
        )

    def one_click_shipment(
        self,
        body: OneClickShipmentRequest | OneClickShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFulfillmentOrderShipmentsResponse, OneClickShipmentErrorBody]:
        """Convenience endpoint that combines rate quote and purchase into a single round trip when the seller already
        knows the desired service level. Returns the purchased shipment record directly.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/shipping/v4/oneClickShipment"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OneClickShipmentRequest | OneClickShipmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFulfillmentOrderShipmentsResponse],
            error_mapper=one_click_shipment_error_mapper,
            request_options=request_options,
        )

    def purchase_shipment(
        self,
        body: PurchaseShipmentRequest | PurchaseShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFulfillmentOrderShipmentsResponse, PurchaseShipmentErrorBody]:
        """Purchases the shipping label for the rate selected from a prior getRates response. Returns the shipment
        record with label document references.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/shipping/v4/shipments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PurchaseShipmentRequest | PurchaseShipmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFulfillmentOrderShipmentsResponse],
            error_mapper=purchase_shipment_error_mapper,
            request_options=request_options,
        )

    def submit_ndr_feedback(
        self,
        body: SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SubmitNdrFeedbackErrorBody]:
        """Submits seller feedback on a non-delivery event for a shipment, instructing the carrier on how to proceed
        (return, reattempt, redirect, etc).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/shipping/v4/ndrFeedback"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=empty_response,
            error_mapper=submit_ndr_feedback_error_mapper,
            request_options=request_options,
        )


class AsyncShippingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_shipment2(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelShipmentResponse1, CancelShipment2ErrorBody]:
        """Cancels a shipment that has not yet shipped. Cancellation eligibility is carrier-dependent; refer to the
        response cancellation status to confirm.

        Args:
            shipment_id: Identifier of the shipment to cancel.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/shipping/v4/shipments/{shipmentId}/cancel"),
            path_params=[param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelShipmentResponse1],
            error_mapper=cancel_shipment2_error_mapper,
            request_options=request_options,
        )

    async def get_access_points(
        self,
        access_point_types: str,
        country_code: str,
        postal_code: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetAccessPointsResponse, GetAccessPointsErrorBody]:
        """Returns access points (pickup and dropoff locations) near the supplied postal code and country, optionally
        filtered by access point type.

        Args:
            access_point_types: Comma-separated list of access point types to include.
            country_code: ISO 3166-1 alpha-2 country code (e.g. US, CA, MX).
            postal_code: Postal code to search around.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/shipping/v4/accessPoints"),
            query_params=[
                param[str]("accessPointTypes", access_point_types),
                param[str]("countryCode", country_code),
                param[str]("postalCode", postal_code),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetAccessPointsResponse],
            error_mapper=get_access_points_error_mapper,
            request_options=request_options,
        )

    async def get_additional_inputs(
        self, rate_id: str, request_token: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetAdditionalInputsResponse, GetAdditionalInputsErrorBody]:
        """Returns a JSON Schema document describing any carrier-and-service-specific inputs required to purchase a
        shipment for the supplied requestToken + rateId. The schema is served verbatim and the calling client should
        validate the seller's input against it before issuing purchaseShipment.

        Args:
            rate_id: rateId returned by a prior getRates response.
            request_token: requestToken returned by a prior getRates response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/shipping/v4/shipments/additionalInputs/schema"),
            query_params=[param[str]("rateId", rate_id), param[str]("requestToken", request_token)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetAdditionalInputsResponse],
            error_mapper=get_additional_inputs_error_mapper,
            request_options=request_options,
        )

    async def get_rates(
        self, body: GetRatesRequest | GetRatesRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetFulfillmentOrderResponse, GetRatesErrorBody]:
        """Returns a list of shipping rate quotes for the given shipment request. The seller can then call
        purchaseShipment with the selected rateId to commit to a label purchase.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/shipping/v4/shipments/rates"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetRatesRequest | GetRatesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFulfillmentOrderResponse],
            error_mapper=get_rates_error_mapper,
            request_options=request_options,
        )

    async def get_shipment_documents(
        self,
        shipment_id: str,
        *,
        package_client_reference_id: str | None = None,
        format_: Format1OrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetShipmentDocumentsResponse, GetShipmentDocumentsErrorBody]:
        """Returns the label, customs, and other printable documents associated with a previously-purchased shipment.

        Args:
            shipment_id: Identifier of the shipment whose documents to retrieve.
            package_client_reference_id: Optional package-level reference id to retrieve documents for a specific
                package within a multi-package shipment.
            format_: Requested document format (defaults to PDF).
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/shipping/v4/shipments/{shipmentId}/documents"),
            path_params=[param[str]("shipmentId", shipment_id)],
            query_params=[
                param[str | None]("packageClientReferenceId", package_client_reference_id),
                param[Format1OrStr | None]("format", format_),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetShipmentDocumentsResponse],
            error_mapper=get_shipment_documents_error_mapper,
            request_options=request_options,
        )

    async def get_tracking(
        self, tracking_id: str, *, carrier_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTrackingResponse, GetTrackingErrorBody]:
        """Returns the current tracking status, event history, and any proof-of-delivery details for the given
        trackingId. TNT resolves carrier internally from the trackingId alone, so carrierId is optional -- confirmed
        unnecessary by the TNT/ Vulcan team (STRIDE-TNT-CORE-PACKAGE-SERVICES) 2026-08-19. When provided, it's used only
        as a defense-in-depth check against the resolved carrier; a mismatch surfaces as 404.

        Args:
            tracking_id: Tracking identifier returned by purchaseShipment.
            carrier_id: Optional carrier identifier for defense-in-depth validation against TNT's resolved carrier. Not
                required by TNT itself -- omit unless you specifically want mismatch protection.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/shipping/v4/tracking"),
            query_params=[param[str]("trackingId", tracking_id), param[str | None]("carrierId", carrier_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetTrackingResponse],
            error_mapper=get_tracking_error_mapper,
            request_options=request_options,
        )

    async def one_click_shipment(
        self,
        body: OneClickShipmentRequest | OneClickShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFulfillmentOrderShipmentsResponse, OneClickShipmentErrorBody]:
        """Convenience endpoint that combines rate quote and purchase into a single round trip when the seller already
        knows the desired service level. Returns the purchased shipment record directly.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/shipping/v4/oneClickShipment"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OneClickShipmentRequest | OneClickShipmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFulfillmentOrderShipmentsResponse],
            error_mapper=one_click_shipment_error_mapper,
            request_options=request_options,
        )

    async def purchase_shipment(
        self,
        body: PurchaseShipmentRequest | PurchaseShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFulfillmentOrderShipmentsResponse, PurchaseShipmentErrorBody]:
        """Purchases the shipping label for the rate selected from a prior getRates response. Returns the shipment
        record with label document references.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/shipping/v4/shipments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PurchaseShipmentRequest | PurchaseShipmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFulfillmentOrderShipmentsResponse],
            error_mapper=purchase_shipment_error_mapper,
            request_options=request_options,
        )

    async def submit_ndr_feedback(
        self,
        body: SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, SubmitNdrFeedbackErrorBody]:
        """Submits seller feedback on a non-delivery event for a shipment, instructing the carrier on how to proceed
        (return, reattempt, redirect, etc).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/shipping/v4/ndrFeedback"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubmitNdrFeedbackRequest | SubmitNdrFeedbackRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_empty_response,
            error_mapper=submit_ndr_feedback_error_mapper,
            request_options=request_options,
        )
