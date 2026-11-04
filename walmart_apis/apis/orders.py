from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.acknowledge_order_error import AcknowledgeOrderErrorBody, acknowledge_order_error_mapper
from ..errors.cancel_order_lines_error import CancelOrderLinesErrorBody, cancel_order_lines_error_mapper
from ..errors.deliver_order_lines_error import DeliverOrderLinesErrorBody, deliver_order_lines_error_mapper
from ..errors.get_order_address_error import GetOrderAddressErrorBody, get_order_address_error_mapper
from ..errors.get_order_buyer_info_error import GetOrderBuyerInfoErrorBody, get_order_buyer_info_error_mapper
from ..errors.get_order_error import GetOrderErrorBody, get_order_error_mapper
from ..errors.get_order_items_error import GetOrderItemsErrorBody, get_order_items_error_mapper
from ..errors.get_order_regulated_info_error import (
    GetOrderRegulatedInfoErrorBody,
    get_order_regulated_info_error_mapper,
)
from ..errors.get_orders_error import GetOrdersErrorBody, get_orders_error_mapper
from ..errors.refund_order_lines_error import RefundOrderLinesErrorBody, refund_order_lines_error_mapper
from ..errors.ship_order_lines_error import ShipOrderLinesErrorBody, ship_order_lines_error_mapper
from ..errors.ship_order_multi_package_error import (
    ShipOrderMultiPackageErrorBody,
    ship_order_multi_package_error_mapper,
)
from ..errors.update_shipment_status_error import UpdateShipmentStatusErrorBody, update_shipment_status_error_mapper
from ..errors.update_verification_status_error import (
    UpdateVerificationStatusErrorBody,
    update_verification_status_error_mapper,
)
from ..models.acknowledge_order_request import AcknowledgeOrderRequest, AcknowledgeOrderRequestDict
from ..models.acknowledge_order_response import AcknowledgeOrderResponse
from ..models.cancel_order_lines_request import CancelOrderLinesRequest, CancelOrderLinesRequestDict
from ..models.cancel_order_lines_response import CancelOrderLinesResponse
from ..models.deliver_order_lines_request import DeliverOrderLinesRequest, DeliverOrderLinesRequestDict
from ..models.deliver_order_lines_response import DeliverOrderLinesResponse
from ..models.enums.fulfillment_type1 import FulfillmentType1OrStr
from ..models.enums.order_status1 import OrderStatus1OrStr
from ..models.get_order_address_response import GetOrderAddressResponse
from ..models.get_order_buyer_info_response import GetOrderBuyerInfoResponse
from ..models.get_order_items_response import GetOrderItemsResponse
from ..models.get_order_regulated_info_response import GetOrderRegulatedInfoResponse
from ..models.get_order_response import GetOrderResponse
from ..models.get_orders_response import GetOrdersResponse
from ..models.multi_package_ship_request import MultiPackageShipRequest, MultiPackageShipRequestDict
from ..models.multi_package_ship_response import MultiPackageShipResponse
from ..models.refund_order_lines_request import RefundOrderLinesRequest, RefundOrderLinesRequestDict
from ..models.refund_order_lines_response import RefundOrderLinesResponse
from ..models.ship_order_lines_request import ShipOrderLinesRequest, ShipOrderLinesRequestDict
from ..models.ship_order_lines_response import ShipOrderLinesResponse
from ..models.update_shipment_status_request import UpdateShipmentStatusRequest, UpdateShipmentStatusRequestDict
from ..models.update_shipment_status_response import UpdateShipmentStatusResponse
from ..models.update_verification_status_request import (
    UpdateVerificationStatusRequest,
    UpdateVerificationStatusRequestDict,
)
from ..models.update_verification_status_response import UpdateVerificationStatusResponse
from ..server.server import Server


class Orders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OrdersWithRawResponse(client, server, auth)

    def acknowledge_order(
        self,
        purchase_order_id: str,
        body: AcknowledgeOrderRequest | AcknowledgeOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AcknowledgeOrderResponse:
        """Acknowledges receipt of the specified order lines in a Walmart Marketplace order. Returns the purchase order
        ID and the timestamp when the acknowledgment was recorded.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.acknowledge_order(purchase_order_id, body, request_options=request_options)
        )

    def cancel_order_lines(
        self,
        purchase_order_id: str,
        body: CancelOrderLinesRequest | CancelOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelOrderLinesResponse:
        """Cancels the specified order lines in a Walmart Marketplace order and records the cancellation reason for each
        line. You can specify the quantity to cancel for each order line. Returns the purchase order ID and the
        cancellation timestamp.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.cancel_order_lines(purchase_order_id, body, request_options=request_options)
        )

    def deliver_order_lines(
        self,
        purchase_order_id: str,
        body: DeliverOrderLinesRequest | DeliverOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeliverOrderLinesResponse:
        """Records delivery of the specified order lines. For each line, you can provide the delivered quantity,
        tracking number, package number, and delivery timestamp. Recording delivery begins the associated invoicing and
        return windows.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.deliver_order_lines(purchase_order_id, body, request_options=request_options)
        )

    def get_order(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderResponse:
        """Retrieves a Walmart Marketplace order, including order status, fulfillment information, and order line
        details.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_order(purchase_order_id, request_options=request_options))

    def get_order_address(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderAddressResponse:
        """Retrieves the shipping address associated with a Walmart Marketplace order, including the recipient's name
        and postal address.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_order_address(purchase_order_id, request_options=request_options))

    def get_order_buyer_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderBuyerInfoResponse:
        """Retrieves buyer contact information for a Walmart Marketplace order, including the buyer's name, email
        address, and a masked phone number showing only the last four digits.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_order_buyer_info(purchase_order_id, request_options=request_options))

    def get_order_items(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderItemsResponse:
        """Retrieves the order lines for a Walmart Marketplace order, including item identifiers, quantities, prices,
        order line statuses, and fulfillment information.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_order_items(purchase_order_id, request_options=request_options))

    def get_order_regulated_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderRegulatedInfoResponse:
        """Retrieves regulated-item verification information for a Walmart Marketplace order, including applicable age
        and identity verification requirements.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.get_order_regulated_info(purchase_order_id, request_options=request_options)
        )

    def get_orders(
        self,
        *,
        created_after: RFC3339DateTime | None = None,
        created_before: RFC3339DateTime | None = None,
        last_updated_after: RFC3339DateTime | None = None,
        order_statuses: list[OrderStatus1OrStr] | None = None,
        fulfillment_types: list[FulfillmentType1OrStr] | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOrdersResponse:
        """Retrieves Walmart Marketplace orders, including order status, fulfillment information, and order line
        details. You can filter results by a single order status and use pagination to retrieve additional orders. Use
        ``pageSize`` to control the number of orders returned per page and ``nextToken`` to retrieve subsequent pages.

        ## Current limitations (roadmap) ## The underlying the Orders service backend does not yet support ## every
        filter declared below. Calls using any of the following will ## return ``400 Bad Request`` with
        ``code=FILTER_NOT_SUPPORTED`` and a ## human-readable ``message`` explaining the specific rejection. Phase ## 2
        will lift these one-by-one as the underlying service adds capability.

        Args:
            created_after: Filters orders created after the specified date and time (ISO 8601). This parameter is not
                currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            created_before: Filters orders created before the specified date and time (ISO 8601). This parameter is not
                currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            last_updated_after: Filters orders updated after the specified date and time (ISO 8601). This parameter is
                not currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            order_statuses: Filters orders by status. Only one status is supported per request. Providing multiple
                statuses returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            fulfillment_types: Filters orders by fulfillment type. Not currently supported: Providing this parameter
                returns ``400`` with ``FILTER_NOT_SUPPORTED``
            page_size: Maximum number of orders to return per page.
            next_token: Pagination token returned in ``payload.nextToken`` from the previous response. Use this token to
                retrieve the next page of orders.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Rate limit exceeded Internal Server Error ``error`` is
                ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.get_orders(
                created_after=created_after,
                created_before=created_before,
                last_updated_after=last_updated_after,
                order_statuses=order_statuses,
                fulfillment_types=fulfillment_types,
                page_size=page_size,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    def refund_order_lines(
        self,
        purchase_order_id: str,
        body: RefundOrderLinesRequest | RefundOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RefundOrderLinesResponse:
        """Issues a seller-initiated refund for one or more order lines. Provide ``refundAmount`` and ``refundType`` for
        each line, and optionally include ``reason``.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.refund_order_lines(purchase_order_id, body, request_options=request_options)
        )

    def ship_order_lines(
        self,
        purchase_order_id: str,
        body: ShipOrderLinesRequest | ShipOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShipOrderLinesResponse:
        """Confirms shipment of the specified order lines in a Walmart Marketplace order, including carrier, tracking
        number, and shipment date. Returns the purchase order ID and the timestamp when the shipment was recorded.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.ship_order_lines(purchase_order_id, body, request_options=request_options)
        )

    def ship_order_multi_package(
        self,
        purchase_order_id: str,
        body: MultiPackageShipRequest | MultiPackageShipRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiPackageShipResponse:
        """Confirms shipment of a Walmart Marketplace order across multiple packages and returns the shipment
        confirmation, including the number of packages accepted.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.ship_order_multi_package(purchase_order_id, body, request_options=request_options)
        )

    def update_shipment_status(
        self,
        purchase_order_id: str,
        body: UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateShipmentStatusResponse:
        """Updates the shipment status of specified order lines in a Walmart
          Marketplace order, including pickup and in-transit milestones.
          Use the delivery operation to record completed deliveries.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.update_shipment_status(purchase_order_id, body, request_options=request_options)
        )

    def update_verification_status(
        self,
        purchase_order_id: str,
        body: UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateVerificationStatusResponse:
        """Records the outcome of buyer identity or age verification at delivery for a regulated Walmart Marketplace
        order. The verification status indicates whether the buyer's identity was successfully verified or rejected.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.update_verification_status(purchase_order_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> OrdersWithRawResponse:
        return self._with_raw_response


class AsyncOrders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOrdersWithRawResponse(client, server, auth)

    async def acknowledge_order(
        self,
        purchase_order_id: str,
        body: AcknowledgeOrderRequest | AcknowledgeOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AcknowledgeOrderResponse:
        """Acknowledges receipt of the specified order lines in a Walmart Marketplace order. Returns the purchase order
        ID and the timestamp when the acknowledgment was recorded.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.acknowledge_order(purchase_order_id, body, request_options=request_options)
        )

    async def cancel_order_lines(
        self,
        purchase_order_id: str,
        body: CancelOrderLinesRequest | CancelOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelOrderLinesResponse:
        """Cancels the specified order lines in a Walmart Marketplace order and records the cancellation reason for each
        line. You can specify the quantity to cancel for each order line. Returns the purchase order ID and the
        cancellation timestamp.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_order_lines(purchase_order_id, body, request_options=request_options)
        )

    async def deliver_order_lines(
        self,
        purchase_order_id: str,
        body: DeliverOrderLinesRequest | DeliverOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeliverOrderLinesResponse:
        """Records delivery of the specified order lines. For each line, you can provide the delivered quantity,
        tracking number, package number, and delivery timestamp. Recording delivery begins the associated invoicing and
        return windows.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.deliver_order_lines(purchase_order_id, body, request_options=request_options)
        )

    async def get_order(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderResponse:
        """Retrieves a Walmart Marketplace order, including order status, fulfillment information, and order line
        details.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.get_order(purchase_order_id, request_options=request_options))

    async def get_order_address(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderAddressResponse:
        """Retrieves the shipping address associated with a Walmart Marketplace order, including the recipient's name
        and postal address.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_order_address(purchase_order_id, request_options=request_options)
        )

    async def get_order_buyer_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderBuyerInfoResponse:
        """Retrieves buyer contact information for a Walmart Marketplace order, including the buyer's name, email
        address, and a masked phone number showing only the last four digits.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_order_buyer_info(purchase_order_id, request_options=request_options)
        )

    async def get_order_items(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderItemsResponse:
        """Retrieves the order lines for a Walmart Marketplace order, including item identifiers, quantities, prices,
        order line statuses, and fulfillment information.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.get_order_items(purchase_order_id, request_options=request_options))

    async def get_order_regulated_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetOrderRegulatedInfoResponse:
        """Retrieves regulated-item verification information for a Walmart Marketplace order, including applicable age
        and identity verification requirements.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_order_regulated_info(purchase_order_id, request_options=request_options)
        )

    async def get_orders(
        self,
        *,
        created_after: RFC3339DateTime | None = None,
        created_before: RFC3339DateTime | None = None,
        last_updated_after: RFC3339DateTime | None = None,
        order_statuses: list[OrderStatus1OrStr] | None = None,
        fulfillment_types: list[FulfillmentType1OrStr] | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOrdersResponse:
        """Retrieves Walmart Marketplace orders, including order status, fulfillment information, and order line
        details. You can filter results by a single order status and use pagination to retrieve additional orders. Use
        ``pageSize`` to control the number of orders returned per page and ``nextToken`` to retrieve subsequent pages.

        ## Current limitations (roadmap) ## The underlying the Orders service backend does not yet support ## every
        filter declared below. Calls using any of the following will ## return ``400 Bad Request`` with
        ``code=FILTER_NOT_SUPPORTED`` and a ## human-readable ``message`` explaining the specific rejection. Phase ## 2
        will lift these one-by-one as the underlying service adds capability.

        Args:
            created_after: Filters orders created after the specified date and time (ISO 8601). This parameter is not
                currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            created_before: Filters orders created before the specified date and time (ISO 8601). This parameter is not
                currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            last_updated_after: Filters orders updated after the specified date and time (ISO 8601). This parameter is
                not currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            order_statuses: Filters orders by status. Only one status is supported per request. Providing multiple
                statuses returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            fulfillment_types: Filters orders by fulfillment type. Not currently supported: Providing this parameter
                returns ``400`` with ``FILTER_NOT_SUPPORTED``
            page_size: Maximum number of orders to return per page.
            next_token: Pagination token returned in ``payload.nextToken`` from the previous response. Use this token to
                retrieve the next page of orders.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Rate limit exceeded Internal Server Error ``error`` is
                ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_orders(
                created_after=created_after,
                created_before=created_before,
                last_updated_after=last_updated_after,
                order_statuses=order_statuses,
                fulfillment_types=fulfillment_types,
                page_size=page_size,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    async def refund_order_lines(
        self,
        purchase_order_id: str,
        body: RefundOrderLinesRequest | RefundOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RefundOrderLinesResponse:
        """Issues a seller-initiated refund for one or more order lines. Provide ``refundAmount`` and ``refundType`` for
        each line, and optionally include ``reason``.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.refund_order_lines(purchase_order_id, body, request_options=request_options)
        )

    async def ship_order_lines(
        self,
        purchase_order_id: str,
        body: ShipOrderLinesRequest | ShipOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ShipOrderLinesResponse:
        """Confirms shipment of the specified order lines in a Walmart Marketplace order, including carrier, tracking
        number, and shipment date. Returns the purchase order ID and the timestamp when the shipment was recorded.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.ship_order_lines(purchase_order_id, body, request_options=request_options)
        )

    async def ship_order_multi_package(
        self,
        purchase_order_id: str,
        body: MultiPackageShipRequest | MultiPackageShipRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> MultiPackageShipResponse:
        """Confirms shipment of a Walmart Marketplace order across multiple packages and returns the shipment
        confirmation, including the number of packages accepted.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.ship_order_multi_package(
                purchase_order_id, body, request_options=request_options
            ),
        )

    async def update_shipment_status(
        self,
        purchase_order_id: str,
        body: UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateShipmentStatusResponse:
        """Updates the shipment status of specified order lines in a Walmart
          Marketplace order, including pickup and in-transit milestones.
          Use the delivery operation to record completed deliveries.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.update_shipment_status(
                purchase_order_id, body, request_options=request_options
            ),
        )

    async def update_verification_status(
        self,
        purchase_order_id: str,
        body: UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateVerificationStatusResponse:
        """Records the outcome of buyer identity or age verification at delivery for a regulated Walmart Marketplace
        order. The verification status indicates whether the buyer's identity was successfully verified or rejected.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /v4/orders`` surface here with
                ``code=FILTER_NOT_SUPPORTED`` and a human-readable ``message`` naming the specific rejected filter.
                Other validation failures (malformed body, missing required field, unknown enum, etc.) reuse this
                response with their own ``code`` value. The ``code`` field is intentionally an open string — new error
                codes can be added without a breaking spec change — but the example below is the canonical shape SDK
                consumers should be prepared to handle. Forbidden Not Found Rate limit exceeded Internal Server Error
                Service temporarily unavailable — the capability is momentarily disabled (e.g. an operational
                kill-switch) or a dependency is in maintenance. Retryable. ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.update_verification_status(
                purchase_order_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncOrdersWithRawResponse:
        return self._with_raw_response


class OrdersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def acknowledge_order(
        self,
        purchase_order_id: str,
        body: AcknowledgeOrderRequest | AcknowledgeOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AcknowledgeOrderResponse, AcknowledgeOrderErrorBody]:
        """Acknowledges receipt of the specified order lines in a Walmart Marketplace order. Returns the purchase order
        ID and the timestamp when the acknowledgment was recorded.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/acknowledge"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AcknowledgeOrderRequest | AcknowledgeOrderRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[AcknowledgeOrderResponse],
            error_mapper=acknowledge_order_error_mapper,
            request_options=request_options,
        )

    def cancel_order_lines(
        self,
        purchase_order_id: str,
        body: CancelOrderLinesRequest | CancelOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelOrderLinesResponse, CancelOrderLinesErrorBody]:
        """Cancels the specified order lines in a Walmart Marketplace order and records the cancellation reason for each
        line. You can specify the quantity to cancel for each order line. Returns the purchase order ID and the
        cancellation timestamp.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/cancel"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelOrderLinesRequest | CancelOrderLinesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelOrderLinesResponse],
            error_mapper=cancel_order_lines_error_mapper,
            request_options=request_options,
        )

    def deliver_order_lines(
        self,
        purchase_order_id: str,
        body: DeliverOrderLinesRequest | DeliverOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeliverOrderLinesResponse, DeliverOrderLinesErrorBody]:
        """Records delivery of the specified order lines. For each line, you can provide the delivered quantity,
        tracking number, package number, and delivery timestamp. Recording delivery begins the associated invoicing and
        return windows.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/deliver"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeliverOrderLinesRequest | DeliverOrderLinesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[DeliverOrderLinesResponse],
            error_mapper=deliver_order_lines_error_mapper,
            request_options=request_options,
        )

    def get_order(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderResponse, GetOrderErrorBody]:
        """Retrieves a Walmart Marketplace order, including order status, fulfillment information, and order line
        details.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrderResponse],
            error_mapper=get_order_error_mapper,
            request_options=request_options,
        )

    def get_order_address(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderAddressResponse, GetOrderAddressErrorBody]:
        """Retrieves the shipping address associated with a Walmart Marketplace order, including the recipient's name
        and postal address.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/address"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrderAddressResponse],
            error_mapper=get_order_address_error_mapper,
            request_options=request_options,
        )

    def get_order_buyer_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderBuyerInfoResponse, GetOrderBuyerInfoErrorBody]:
        """Retrieves buyer contact information for a Walmart Marketplace order, including the buyer's name, email
        address, and a masked phone number showing only the last four digits.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/buyer-info"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrderBuyerInfoResponse],
            error_mapper=get_order_buyer_info_error_mapper,
            request_options=request_options,
        )

    def get_order_items(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderItemsResponse, GetOrderItemsErrorBody]:
        """Retrieves the order lines for a Walmart Marketplace order, including item identifiers, quantities, prices,
        order line statuses, and fulfillment information.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/items"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrderItemsResponse],
            error_mapper=get_order_items_error_mapper,
            request_options=request_options,
        )

    def get_order_regulated_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderRegulatedInfoResponse, GetOrderRegulatedInfoErrorBody]:
        """Retrieves regulated-item verification information for a Walmart Marketplace order, including applicable age
        and identity verification requirements.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/regulated-info"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrderRegulatedInfoResponse],
            error_mapper=get_order_regulated_info_error_mapper,
            request_options=request_options,
        )

    def get_orders(
        self,
        *,
        created_after: RFC3339DateTime | None = None,
        created_before: RFC3339DateTime | None = None,
        last_updated_after: RFC3339DateTime | None = None,
        order_statuses: list[OrderStatus1OrStr] | None = None,
        fulfillment_types: list[FulfillmentType1OrStr] | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOrdersResponse, GetOrdersErrorBody]:
        """Retrieves Walmart Marketplace orders, including order status, fulfillment information, and order line
        details. You can filter results by a single order status and use pagination to retrieve additional orders. Use
        ``pageSize`` to control the number of orders returned per page and ``nextToken`` to retrieve subsequent pages.

        ## Current limitations (roadmap) ## The underlying the Orders service backend does not yet support ## every
        filter declared below. Calls using any of the following will ## return ``400 Bad Request`` with
        ``code=FILTER_NOT_SUPPORTED`` and a ## human-readable ``message`` explaining the specific rejection. Phase ## 2
        will lift these one-by-one as the underlying service adds capability.

        Args:
            created_after: Filters orders created after the specified date and time (ISO 8601). This parameter is not
                currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            created_before: Filters orders created before the specified date and time (ISO 8601). This parameter is not
                currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            last_updated_after: Filters orders updated after the specified date and time (ISO 8601). This parameter is
                not currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            order_statuses: Filters orders by status. Only one status is supported per request. Providing multiple
                statuses returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            fulfillment_types: Filters orders by fulfillment type. Not currently supported: Providing this parameter
                returns ``400`` with ``FILTER_NOT_SUPPORTED``
            page_size: Maximum number of orders to return per page.
            next_token: Pagination token returned in ``payload.nextToken`` from the previous response. Use this token to
                retrieve the next page of orders.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders"),
            query_params=[
                param[RFC3339DateTime | None]("createdAfter", created_after),
                param[RFC3339DateTime | None]("createdBefore", created_before),
                param[RFC3339DateTime | None]("lastUpdatedAfter", last_updated_after),
                param[list[OrderStatus1OrStr] | None]("orderStatuses", order_statuses),
                param[list[FulfillmentType1OrStr] | None]("fulfillmentTypes", fulfillment_types),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrdersResponse],
            error_mapper=get_orders_error_mapper,
            request_options=request_options,
        )

    def refund_order_lines(
        self,
        purchase_order_id: str,
        body: RefundOrderLinesRequest | RefundOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RefundOrderLinesResponse, RefundOrderLinesErrorBody]:
        """Issues a seller-initiated refund for one or more order lines. Provide ``refundAmount`` and ``refundType`` for
        each line, and optionally include ``reason``.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/refund"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundOrderLinesRequest | RefundOrderLinesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[RefundOrderLinesResponse],
            error_mapper=refund_order_lines_error_mapper,
            request_options=request_options,
        )

    def ship_order_lines(
        self,
        purchase_order_id: str,
        body: ShipOrderLinesRequest | ShipOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShipOrderLinesResponse, ShipOrderLinesErrorBody]:
        """Confirms shipment of the specified order lines in a Walmart Marketplace order, including carrier, tracking
        number, and shipment date. Returns the purchase order ID and the timestamp when the shipment was recorded.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/shipping"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ShipOrderLinesRequest | ShipOrderLinesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ShipOrderLinesResponse],
            error_mapper=ship_order_lines_error_mapper,
            request_options=request_options,
        )

    def ship_order_multi_package(
        self,
        purchase_order_id: str,
        body: MultiPackageShipRequest | MultiPackageShipRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiPackageShipResponse, ShipOrderMultiPackageErrorBody]:
        """Confirms shipment of a Walmart Marketplace order across multiple packages and returns the shipment
        confirmation, including the number of packages accepted.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/multi-package-shipping"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MultiPackageShipRequest | MultiPackageShipRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[MultiPackageShipResponse],
            error_mapper=ship_order_multi_package_error_mapper,
            request_options=request_options,
        )

    def update_shipment_status(
        self,
        purchase_order_id: str,
        body: UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateShipmentStatusResponse, UpdateShipmentStatusErrorBody]:
        """Updates the shipment status of specified order lines in a Walmart
          Marketplace order, including pickup and in-transit milestones.
          Use the delivery operation to record completed deliveries.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/shipment-status"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[UpdateShipmentStatusResponse],
            error_mapper=update_shipment_status_error_mapper,
            request_options=request_options,
        )

    def update_verification_status(
        self,
        purchase_order_id: str,
        body: UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateVerificationStatusResponse, UpdateVerificationStatusErrorBody]:
        """Records the outcome of buyer identity or age verification at delivery for a regulated Walmart Marketplace
        order. The verification status indicates whether the buyer's identity was successfully verified or rejected.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/regulated-info"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[UpdateVerificationStatusResponse],
            error_mapper=update_verification_status_error_mapper,
            request_options=request_options,
        )


class AsyncOrdersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def acknowledge_order(
        self,
        purchase_order_id: str,
        body: AcknowledgeOrderRequest | AcknowledgeOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AcknowledgeOrderResponse, AcknowledgeOrderErrorBody]:
        """Acknowledges receipt of the specified order lines in a Walmart Marketplace order. Returns the purchase order
        ID and the timestamp when the acknowledgment was recorded.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/acknowledge"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AcknowledgeOrderRequest | AcknowledgeOrderRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[AcknowledgeOrderResponse],
            error_mapper=acknowledge_order_error_mapper,
            request_options=request_options,
        )

    async def cancel_order_lines(
        self,
        purchase_order_id: str,
        body: CancelOrderLinesRequest | CancelOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelOrderLinesResponse, CancelOrderLinesErrorBody]:
        """Cancels the specified order lines in a Walmart Marketplace order and records the cancellation reason for each
        line. You can specify the quantity to cancel for each order line. Returns the purchase order ID and the
        cancellation timestamp.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/cancel"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelOrderLinesRequest | CancelOrderLinesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelOrderLinesResponse],
            error_mapper=cancel_order_lines_error_mapper,
            request_options=request_options,
        )

    async def deliver_order_lines(
        self,
        purchase_order_id: str,
        body: DeliverOrderLinesRequest | DeliverOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeliverOrderLinesResponse, DeliverOrderLinesErrorBody]:
        """Records delivery of the specified order lines. For each line, you can provide the delivered quantity,
        tracking number, package number, and delivery timestamp. Recording delivery begins the associated invoicing and
        return windows.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/deliver"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeliverOrderLinesRequest | DeliverOrderLinesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[DeliverOrderLinesResponse],
            error_mapper=deliver_order_lines_error_mapper,
            request_options=request_options,
        )

    async def get_order(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderResponse, GetOrderErrorBody]:
        """Retrieves a Walmart Marketplace order, including order status, fulfillment information, and order line
        details.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrderResponse],
            error_mapper=get_order_error_mapper,
            request_options=request_options,
        )

    async def get_order_address(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderAddressResponse, GetOrderAddressErrorBody]:
        """Retrieves the shipping address associated with a Walmart Marketplace order, including the recipient's name
        and postal address.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/address"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrderAddressResponse],
            error_mapper=get_order_address_error_mapper,
            request_options=request_options,
        )

    async def get_order_buyer_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderBuyerInfoResponse, GetOrderBuyerInfoErrorBody]:
        """Retrieves buyer contact information for a Walmart Marketplace order, including the buyer's name, email
        address, and a masked phone number showing only the last four digits.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/buyer-info"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrderBuyerInfoResponse],
            error_mapper=get_order_buyer_info_error_mapper,
            request_options=request_options,
        )

    async def get_order_items(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderItemsResponse, GetOrderItemsErrorBody]:
        """Retrieves the order lines for a Walmart Marketplace order, including item identifiers, quantities, prices,
        order line statuses, and fulfillment information.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/items"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrderItemsResponse],
            error_mapper=get_order_items_error_mapper,
            request_options=request_options,
        )

    async def get_order_regulated_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderRegulatedInfoResponse, GetOrderRegulatedInfoErrorBody]:
        """Retrieves regulated-item verification information for a Walmart Marketplace order, including applicable age
        and identity verification requirements.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/regulated-info"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrderRegulatedInfoResponse],
            error_mapper=get_order_regulated_info_error_mapper,
            request_options=request_options,
        )

    async def get_orders(
        self,
        *,
        created_after: RFC3339DateTime | None = None,
        created_before: RFC3339DateTime | None = None,
        last_updated_after: RFC3339DateTime | None = None,
        order_statuses: list[OrderStatus1OrStr] | None = None,
        fulfillment_types: list[FulfillmentType1OrStr] | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOrdersResponse, GetOrdersErrorBody]:
        """Retrieves Walmart Marketplace orders, including order status, fulfillment information, and order line
        details. You can filter results by a single order status and use pagination to retrieve additional orders. Use
        ``pageSize`` to control the number of orders returned per page and ``nextToken`` to retrieve subsequent pages.

        ## Current limitations (roadmap) ## The underlying the Orders service backend does not yet support ## every
        filter declared below. Calls using any of the following will ## return ``400 Bad Request`` with
        ``code=FILTER_NOT_SUPPORTED`` and a ## human-readable ``message`` explaining the specific rejection. Phase ## 2
        will lift these one-by-one as the underlying service adds capability.

        Args:
            created_after: Filters orders created after the specified date and time (ISO 8601). This parameter is not
                currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            created_before: Filters orders created before the specified date and time (ISO 8601). This parameter is not
                currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            last_updated_after: Filters orders updated after the specified date and time (ISO 8601). This parameter is
                not currently supported. If provided, the API returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            order_statuses: Filters orders by status. Only one status is supported per request. Providing multiple
                statuses returns ``400`` with ``FILTER_NOT_SUPPORTED``.
            fulfillment_types: Filters orders by fulfillment type. Not currently supported: Providing this parameter
                returns ``400`` with ``FILTER_NOT_SUPPORTED``
            page_size: Maximum number of orders to return per page.
            next_token: Pagination token returned in ``payload.nextToken`` from the previous response. Use this token to
                retrieve the next page of orders.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/orders"),
            query_params=[
                param[RFC3339DateTime | None]("createdAfter", created_after),
                param[RFC3339DateTime | None]("createdBefore", created_before),
                param[RFC3339DateTime | None]("lastUpdatedAfter", last_updated_after),
                param[list[OrderStatus1OrStr] | None]("orderStatuses", order_statuses),
                param[list[FulfillmentType1OrStr] | None]("fulfillmentTypes", fulfillment_types),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrdersResponse],
            error_mapper=get_orders_error_mapper,
            request_options=request_options,
        )

    async def refund_order_lines(
        self,
        purchase_order_id: str,
        body: RefundOrderLinesRequest | RefundOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RefundOrderLinesResponse, RefundOrderLinesErrorBody]:
        """Issues a seller-initiated refund for one or more order lines. Provide ``refundAmount`` and ``refundType`` for
        each line, and optionally include ``reason``.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/refund"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundOrderLinesRequest | RefundOrderLinesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[RefundOrderLinesResponse],
            error_mapper=refund_order_lines_error_mapper,
            request_options=request_options,
        )

    async def ship_order_lines(
        self,
        purchase_order_id: str,
        body: ShipOrderLinesRequest | ShipOrderLinesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ShipOrderLinesResponse, ShipOrderLinesErrorBody]:
        """Confirms shipment of the specified order lines in a Walmart Marketplace order, including carrier, tracking
        number, and shipment date. Returns the purchase order ID and the timestamp when the shipment was recorded.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/shipping"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ShipOrderLinesRequest | ShipOrderLinesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ShipOrderLinesResponse],
            error_mapper=ship_order_lines_error_mapper,
            request_options=request_options,
        )

    async def ship_order_multi_package(
        self,
        purchase_order_id: str,
        body: MultiPackageShipRequest | MultiPackageShipRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[MultiPackageShipResponse, ShipOrderMultiPackageErrorBody]:
        """Confirms shipment of a Walmart Marketplace order across multiple packages and returns the shipment
        confirmation, including the number of packages accepted.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/multi-package-shipping"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MultiPackageShipRequest | MultiPackageShipRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[MultiPackageShipResponse],
            error_mapper=ship_order_multi_package_error_mapper,
            request_options=request_options,
        )

    async def update_shipment_status(
        self,
        purchase_order_id: str,
        body: UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateShipmentStatusResponse, UpdateShipmentStatusErrorBody]:
        """Updates the shipment status of specified order lines in a Walmart
          Marketplace order, including pickup and in-transit milestones.
          Use the delivery operation to record completed deliveries.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/shipment-status"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateShipmentStatusRequest | UpdateShipmentStatusRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[UpdateShipmentStatusResponse],
            error_mapper=update_shipment_status_error_mapper,
            request_options=request_options,
        )

    async def update_verification_status(
        self,
        purchase_order_id: str,
        body: UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateVerificationStatusResponse, UpdateVerificationStatusErrorBody]:
        """Records the outcome of buyer identity or age verification at delivery for a regulated Walmart Marketplace
        order. The verification status indicates whether the buyer's identity was successfully verified or rejected.

        Args:
            purchase_order_id: Purchase order identifier assigned by Walmart.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default_catalog_items("/v4/orders/{purchase-order-id}/regulated-info"),
            path_params=[param[str]("purchase-order-id", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[UpdateVerificationStatusResponse],
            error_mapper=update_verification_status_error_mapper,
            request_options=request_options,
        )
