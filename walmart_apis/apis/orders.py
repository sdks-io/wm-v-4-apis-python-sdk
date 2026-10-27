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
from ..models.enums.fulfillment_type import FulfillmentTypeOrStr
from ..models.enums.order_status import OrderStatusOrStr
from ..models.get_fulfillment_order_response import GetFulfillmentOrderResponse
from ..models.get_fulfillment_order_shipments_response import GetFulfillmentOrderShipmentsResponse
from ..models.get_order_address_response import GetOrderAddressResponse
from ..models.get_order_buyer_info_response import GetOrderBuyerInfoResponse
from ..models.get_order_regulated_info_response import GetOrderRegulatedInfoResponse
from ..models.get_order_response import GetOrderResponse
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Records the terminal ``Delivered`` event for one or more order lines, optionally with package-level
        proof-of-delivery (tracking number, package number, delivery timestamp). This is separated from
        ``/shipment-status`` because delivery is a terminal state and carries different downstream semantics (invoicing
        windows open, return windows start).

        Walmart parity from gmp-orders-mono ``deliverOrder``.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Send a ``GET`` request.

        Args:
            purchase_order_id: Walmart Purchase Order ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Returns the ship-to postal address for a single purchase order. Mirrors Amazon SP-API ``getOrderAddress``.
        PII-restricted endpoint: handlers are marked ``@RestrictedData`` server-side and the response body must NOT be
        logged.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Returns the buyer's display name, email address, and an anonymized phone (last 4 digits only). Mirrors Amazon
        SP-API ``getOrderBuyerInfo``. PII-restricted endpoint: handlers are marked ``@RestrictedData`` server-side and
        request/response bodies must NOT be logged.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
    ) -> GetFulfillmentOrderShipmentsResponse:
        """Returns the SKU / quantity / item-price projection of a single purchase order. Mirrors Amazon SP-API
        ``getOrderItems``. Not PII-restricted: only product, quantity, and price are returned.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Parity with Amazon SP-API Orders v0 ``getOrderRegulatedInfo``. Returns the verification requirements that
        apply to an order containing regulated items (alcohol, tobacco, age-restricted goods): the required
        ID-verification method, the minimum buyer age, the regulated category, and any value-added services the order
        ships with.

        **Walmart OMS coverage gap .** The the underlying service Order Lookup response does not currently surface
        regulated-item metadata. Until upstream support lands (tracked separately as a follow-up to this PR), every
        order returns the safe default ``regulatedCategory=NOT_REGULATED`` with ``requiredVerificationMethod=NONE``. The
        endpoint shape and contract are stable; only the projected values will become richer once OMS exposes the
        fields.

        Args:
            purchase_order_id: Walmart Purchase Order ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        order_statuses: list[OrderStatusOrStr] | None = None,
        fulfillment_types: list[FulfillmentTypeOrStr] | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFulfillmentOrderResponse:
        """Returns orders matching the given filters. Orders are fulfilled by sellers (WFS or seller-fulfilled). Maps to
        Walmart OMS order queries.

        ### Current limitations (roadmap)

        The underlying the Orders service backend does not yet support every filter declared below. Calls using any of
        the following will return ``400 Bad Request`` with ``code=FILTER_NOT_SUPPORTED`` and a human-readable
        ``message`` explaining the specific rejection. Phase 2 will lift these one-by-one as the underlying service adds
        capability.

        | Filter | Status today | Reason |
        |---|---|---|
        | ``createdAfter``, ``createdBefore`` | Rejected (400) | the Orders service does not accept date-range filters
            at the order level. |
        | ``lastUpdatedAfter`` | Rejected (400) | the underlying service has no order-level update-date index. |
        | ``orderStatuses`` with >1 value | Rejected (400) | the underlying service accepts one status per call; pass a
            single value or omit to match all. |
        | ``fulfillmentTypes`` | Rejected (400) | the underlying service accepts one shipNodeType per call; multi-type
            fan-out is Phase 2. |

        These parameters remain in the contract (rather than being removed) so that SDKs generated today stay
        forward-compatible with the the roadmap surface — your code keeps compiling, only the runtime behaviour changes
        when Phase 2 ships. Until then, omit them or handle the documented 400 gracefully. The ``tools/loadgen-orders.sh
        --contract`` smoke sweep exercises the rejection contract on every run.

        Args:
            created_after: Filter orders created after this date-time (ISO 8601). **the roadmap — not yet supported.**
                Sending this parameter today returns ``400 FILTER_NOT_SUPPORTED``; the Orders service does not accept
                date-range filters at the order level. Tracked by . Retained in the contract so SDKs generated today
                stay forward-compatible.
            created_before: Filter orders created before this date-time (ISO 8601). **the roadmap — not yet supported.**
                See ``createdAfter`` for the rationale and the tracking ticket.
            last_updated_after: Filter orders updated after this date-time (ISO 8601). **the roadmap — not yet
                supported.** Sending this parameter today returns ``400 FILTER_NOT_SUPPORTED``; the Orders service has
                no order-level update-date index. Tracked by .
            order_statuses: Filter by order status. **the roadmap limitation:** the Orders service accepts AT MOST ONE
                status per call. Passing multiple values today returns `400 FILTER_NOT_SUPPORTED`; pass a single value
                or omit to match all. Multi-status fan-out tracked by .
            fulfillment_types: Filter by fulfillment type. **the roadmap — not yet supported.** Sending this parameter
                today returns ``400 FILTER_NOT_SUPPORTED``; the underlying service accepts one shipNodeType per call and
                multi-type fan-out is Phase 2. Tracked by .
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Walmart-specific write — no Amazon SP-API Orders v0 equivalent (Amazon refunds live in the Finance API).
        Mirrors gmp-orders-mono's legacy ``/partner-api/{market}/v3/orders/{po}/refund`` contract, simplified for the v4
        surface: a flat ``orderLines[]`` with per-line refund amount + reason instead of the legacy three-level nesting
        (``orderLines → refunds → refundCharges``).

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Walmart-specific extension of ``/shipping``. Each package carries its own tracking number, carrier,
        dimensions, and the order lines it covers. Maps onto FMS's existing ``shipments[]`` envelope (one FMS shipment
        per v4 package). Inspired by gmp-orders-mono's ``shipOrderV2`` (multiPackageShipping) operation; we hoist
        ``packages[]`` to the top level rather than nesting it under each line so the request stays self-evidently
        package-oriented.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Records a non-terminal shipment-lifecycle event for an order (ready for pickup, picked up, in transit, out
        for delivery). Use the dedicated ``/deliver`` endpoint for terminal delivery — it carries proof-of-delivery
        semantics this endpoint does not.

        Amazon SP-API Orders v0 ``updateShipmentStatus`` parity.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Parity with Amazon SP-API Orders v0 ``updateVerificationStatus``. The seller calls this after delivering a
        regulated-item order to record whether the buyer's identity / age was verified at the doorstep. An APPROVED
        status releases the order for settlement; REJECTED requires a ``rejectionReason`` and triggers downstream
        return-processing.

        Gated by the CCM-managed ``orders.features.regulatedInfoEnabled`` kill-switch (live-refreshable, parity with the
        cancel kill-switch).

        Args:
            purchase_order_id: Walmart Purchase Order ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Records the terminal ``Delivered`` event for one or more order lines, optionally with package-level
        proof-of-delivery (tracking number, package number, delivery timestamp). This is separated from
        ``/shipment-status`` because delivery is a terminal state and carries different downstream semantics (invoicing
        windows open, return windows start).

        Walmart parity from gmp-orders-mono ``deliverOrder``.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Send a ``GET`` request.

        Args:
            purchase_order_id: Walmart Purchase Order ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Returns the ship-to postal address for a single purchase order. Mirrors Amazon SP-API ``getOrderAddress``.
        PII-restricted endpoint: handlers are marked ``@RestrictedData`` server-side and the response body must NOT be
        logged.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Returns the buyer's display name, email address, and an anonymized phone (last 4 digits only). Mirrors Amazon
        SP-API ``getOrderBuyerInfo``. PII-restricted endpoint: handlers are marked ``@RestrictedData`` server-side and
        request/response bodies must NOT be logged.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
    ) -> GetFulfillmentOrderShipmentsResponse:
        """Returns the SKU / quantity / item-price projection of a single purchase order. Mirrors Amazon SP-API
        ``getOrderItems``. Not PII-restricted: only product, quantity, and price are returned.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Parity with Amazon SP-API Orders v0 ``getOrderRegulatedInfo``. Returns the verification requirements that
        apply to an order containing regulated items (alcohol, tobacco, age-restricted goods): the required
        ID-verification method, the minimum buyer age, the regulated category, and any value-added services the order
        ships with.

        **Walmart OMS coverage gap .** The the underlying service Order Lookup response does not currently surface
        regulated-item metadata. Until upstream support lands (tracked separately as a follow-up to this PR), every
        order returns the safe default ``regulatedCategory=NOT_REGULATED`` with ``requiredVerificationMethod=NONE``. The
        endpoint shape and contract are stable; only the projected values will become richer once OMS exposes the
        fields.

        Args:
            purchase_order_id: Walmart Purchase Order ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        order_statuses: list[OrderStatusOrStr] | None = None,
        fulfillment_types: list[FulfillmentTypeOrStr] | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFulfillmentOrderResponse:
        """Returns orders matching the given filters. Orders are fulfilled by sellers (WFS or seller-fulfilled). Maps to
        Walmart OMS order queries.

        ### Current limitations (roadmap)

        The underlying the Orders service backend does not yet support every filter declared below. Calls using any of
        the following will return ``400 Bad Request`` with ``code=FILTER_NOT_SUPPORTED`` and a human-readable
        ``message`` explaining the specific rejection. Phase 2 will lift these one-by-one as the underlying service adds
        capability.

        | Filter | Status today | Reason |
        |---|---|---|
        | ``createdAfter``, ``createdBefore`` | Rejected (400) | the Orders service does not accept date-range filters
            at the order level. |
        | ``lastUpdatedAfter`` | Rejected (400) | the underlying service has no order-level update-date index. |
        | ``orderStatuses`` with >1 value | Rejected (400) | the underlying service accepts one status per call; pass a
            single value or omit to match all. |
        | ``fulfillmentTypes`` | Rejected (400) | the underlying service accepts one shipNodeType per call; multi-type
            fan-out is Phase 2. |

        These parameters remain in the contract (rather than being removed) so that SDKs generated today stay
        forward-compatible with the the roadmap surface — your code keeps compiling, only the runtime behaviour changes
        when Phase 2 ships. Until then, omit them or handle the documented 400 gracefully. The ``tools/loadgen-orders.sh
        --contract`` smoke sweep exercises the rejection contract on every run.

        Args:
            created_after: Filter orders created after this date-time (ISO 8601). **the roadmap — not yet supported.**
                Sending this parameter today returns ``400 FILTER_NOT_SUPPORTED``; the Orders service does not accept
                date-range filters at the order level. Tracked by . Retained in the contract so SDKs generated today
                stay forward-compatible.
            created_before: Filter orders created before this date-time (ISO 8601). **the roadmap — not yet supported.**
                See ``createdAfter`` for the rationale and the tracking ticket.
            last_updated_after: Filter orders updated after this date-time (ISO 8601). **the roadmap — not yet
                supported.** Sending this parameter today returns ``400 FILTER_NOT_SUPPORTED``; the Orders service has
                no order-level update-date index. Tracked by .
            order_statuses: Filter by order status. **the roadmap limitation:** the Orders service accepts AT MOST ONE
                status per call. Passing multiple values today returns `400 FILTER_NOT_SUPPORTED`; pass a single value
                or omit to match all. Multi-status fan-out tracked by .
            fulfillment_types: Filter by fulfillment type. **the roadmap — not yet supported.** Sending this parameter
                today returns ``400 FILTER_NOT_SUPPORTED``; the underlying service accepts one shipNodeType per call and
                multi-type fan-out is Phase 2. Tracked by .
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Walmart-specific write — no Amazon SP-API Orders v0 equivalent (Amazon refunds live in the Finance API).
        Mirrors gmp-orders-mono's legacy ``/partner-api/{market}/v3/orders/{po}/refund`` contract, simplified for the v4
        surface: a flat ``orderLines[]`` with per-line refund amount + reason instead of the legacy three-level nesting
        (``orderLines → refunds → refundCharges``).

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Walmart-specific extension of ``/shipping``. Each package carries its own tracking number, carrier,
        dimensions, and the order lines it covers. Maps onto FMS's existing ``shipments[]`` envelope (one FMS shipment
        per v4 package). Inspired by gmp-orders-mono's ``shipOrderV2`` (multiPackageShipping) operation; we hoist
        ``packages[]`` to the top level rather than nesting it under each line so the request stays self-evidently
        package-oriented.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Records a non-terminal shipment-lifecycle event for an order (ready for pickup, picked up, in transit, out
        for delivery). Use the dedicated ``/deliver`` endpoint for terminal delivery — it carries proof-of-delivery
        semantics this endpoint does not.

        Amazon SP-API Orders v0 ``updateShipmentStatus`` parity.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Parity with Amazon SP-API Orders v0 ``updateVerificationStatus``. The seller calls this after delivering a
        regulated-item order to record whether the buyer's identity / age was verified at the doorstep. An APPROVED
        status releases the order for settlement; REJECTED requires a ``rejectionReason`` and triggers downstream
        return-processing.

        Gated by the CCM-managed ``orders.features.regulatedInfoEnabled`` kill-switch (live-refreshable, parity with the
        cancel kill-switch).

        Args:
            purchase_order_id: Walmart Purchase Order ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request. The the roadmap limitations described on ``GET /orders/v4/orders`` surface here with
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/acknowledge"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/cancel"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Records the terminal ``Delivered`` event for one or more order lines, optionally with package-level
        proof-of-delivery (tracking number, package number, delivery timestamp). This is separated from
        ``/shipment-status`` because delivery is a terminal state and carries different downstream semantics (invoicing
        windows open, return windows start).

        Walmart parity from gmp-orders-mono ``deliverOrder``.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/deliver"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Send a ``GET`` request.

        Args:
            purchase_order_id: Walmart Purchase Order ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrderResponse],
            error_mapper=get_order_error_mapper,
            request_options=request_options,
        )

    def get_order_address(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderAddressResponse, GetOrderAddressErrorBody]:
        """Returns the ship-to postal address for a single purchase order. Mirrors Amazon SP-API ``getOrderAddress``.
        PII-restricted endpoint: handlers are marked ``@RestrictedData`` server-side and the response body must NOT be
        logged.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/address"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrderAddressResponse],
            error_mapper=get_order_address_error_mapper,
            request_options=request_options,
        )

    def get_order_buyer_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderBuyerInfoResponse, GetOrderBuyerInfoErrorBody]:
        """Returns the buyer's display name, email address, and an anonymized phone (last 4 digits only). Mirrors Amazon
        SP-API ``getOrderBuyerInfo``. PII-restricted endpoint: handlers are marked ``@RestrictedData`` server-side and
        request/response bodies must NOT be logged.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/buyerInfo"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOrderBuyerInfoResponse],
            error_mapper=get_order_buyer_info_error_mapper,
            request_options=request_options,
        )

    def get_order_items(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetFulfillmentOrderShipmentsResponse, GetOrderItemsErrorBody]:
        """Returns the SKU / quantity / item-price projection of a single purchase order. Mirrors Amazon SP-API
        ``getOrderItems``. Not PII-restricted: only product, quantity, and price are returned.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/items"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFulfillmentOrderShipmentsResponse],
            error_mapper=get_order_items_error_mapper,
            request_options=request_options,
        )

    def get_order_regulated_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderRegulatedInfoResponse, GetOrderRegulatedInfoErrorBody]:
        """Parity with Amazon SP-API Orders v0 ``getOrderRegulatedInfo``. Returns the verification requirements that
        apply to an order containing regulated items (alcohol, tobacco, age-restricted goods): the required
        ID-verification method, the minimum buyer age, the regulated category, and any value-added services the order
        ships with.

        **Walmart OMS coverage gap .** The the underlying service Order Lookup response does not currently surface
        regulated-item metadata. Until upstream support lands (tracked separately as a follow-up to this PR), every
        order returns the safe default ``regulatedCategory=NOT_REGULATED`` with ``requiredVerificationMethod=NONE``. The
        endpoint shape and contract are stable; only the projected values will become richer once OMS exposes the
        fields.

        Args:
            purchase_order_id: Walmart Purchase Order ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/regulatedInfo"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        order_statuses: list[OrderStatusOrStr] | None = None,
        fulfillment_types: list[FulfillmentTypeOrStr] | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFulfillmentOrderResponse, GetOrdersErrorBody]:
        """Returns orders matching the given filters. Orders are fulfilled by sellers (WFS or seller-fulfilled). Maps to
        Walmart OMS order queries.

        ### Current limitations (roadmap)

        The underlying the Orders service backend does not yet support every filter declared below. Calls using any of
        the following will return ``400 Bad Request`` with ``code=FILTER_NOT_SUPPORTED`` and a human-readable
        ``message`` explaining the specific rejection. Phase 2 will lift these one-by-one as the underlying service adds
        capability.

        | Filter | Status today | Reason |
        |---|---|---|
        | ``createdAfter``, ``createdBefore`` | Rejected (400) | the Orders service does not accept date-range filters
            at the order level. |
        | ``lastUpdatedAfter`` | Rejected (400) | the underlying service has no order-level update-date index. |
        | ``orderStatuses`` with >1 value | Rejected (400) | the underlying service accepts one status per call; pass a
            single value or omit to match all. |
        | ``fulfillmentTypes`` | Rejected (400) | the underlying service accepts one shipNodeType per call; multi-type
            fan-out is Phase 2. |

        These parameters remain in the contract (rather than being removed) so that SDKs generated today stay
        forward-compatible with the the roadmap surface — your code keeps compiling, only the runtime behaviour changes
        when Phase 2 ships. Until then, omit them or handle the documented 400 gracefully. The ``tools/loadgen-orders.sh
        --contract`` smoke sweep exercises the rejection contract on every run.

        Args:
            created_after: Filter orders created after this date-time (ISO 8601). **the roadmap — not yet supported.**
                Sending this parameter today returns ``400 FILTER_NOT_SUPPORTED``; the Orders service does not accept
                date-range filters at the order level. Tracked by . Retained in the contract so SDKs generated today
                stay forward-compatible.
            created_before: Filter orders created before this date-time (ISO 8601). **the roadmap — not yet supported.**
                See ``createdAfter`` for the rationale and the tracking ticket.
            last_updated_after: Filter orders updated after this date-time (ISO 8601). **the roadmap — not yet
                supported.** Sending this parameter today returns ``400 FILTER_NOT_SUPPORTED``; the Orders service has
                no order-level update-date index. Tracked by .
            order_statuses: Filter by order status. **the roadmap limitation:** the Orders service accepts AT MOST ONE
                status per call. Passing multiple values today returns `400 FILTER_NOT_SUPPORTED`; pass a single value
                or omit to match all. Multi-status fan-out tracked by .
            fulfillment_types: Filter by fulfillment type. **the roadmap — not yet supported.** Sending this parameter
                today returns ``400 FILTER_NOT_SUPPORTED``; the underlying service accepts one shipNodeType per call and
                multi-type fan-out is Phase 2. Tracked by .
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders"),
            query_params=[
                param[RFC3339DateTime | None]("createdAfter", created_after),
                param[RFC3339DateTime | None]("createdBefore", created_before),
                param[RFC3339DateTime | None]("lastUpdatedAfter", last_updated_after),
                param[list[OrderStatusOrStr] | None]("orderStatuses", order_statuses),
                param[list[FulfillmentTypeOrStr] | None]("fulfillmentTypes", fulfillment_types),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFulfillmentOrderResponse],
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
        """Walmart-specific write — no Amazon SP-API Orders v0 equivalent (Amazon refunds live in the Finance API).
        Mirrors gmp-orders-mono's legacy ``/partner-api/{market}/v3/orders/{po}/refund`` contract, simplified for the v4
        surface: a flat ``orderLines[]`` with per-line refund amount + reason instead of the legacy three-level nesting
        (``orderLines → refunds → refundCharges``).

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/refund"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/shipping"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Walmart-specific extension of ``/shipping``. Each package carries its own tracking number, carrier,
        dimensions, and the order lines it covers. Maps onto FMS's existing ``shipments[]`` envelope (one FMS shipment
        per v4 package). Inspired by gmp-orders-mono's ``shipOrderV2`` (multiPackageShipping) operation; we hoist
        ``packages[]`` to the top level rather than nesting it under each line so the request stays self-evidently
        package-oriented.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/multi-package-shipping"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Records a non-terminal shipment-lifecycle event for an order (ready for pickup, picked up, in transit, out
        for delivery). Use the dedicated ``/deliver`` endpoint for terminal delivery — it carries proof-of-delivery
        semantics this endpoint does not.

        Amazon SP-API Orders v0 ``updateShipmentStatus`` parity.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/shipment-status"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Parity with Amazon SP-API Orders v0 ``updateVerificationStatus``. The seller calls this after delivering a
        regulated-item order to record whether the buyer's identity / age was verified at the doorstep. An APPROVED
        status releases the order for settlement; REJECTED requires a ``rejectionReason`` and triggers downstream
        return-processing.

        Gated by the CCM-managed ``orders.features.regulatedInfoEnabled`` kill-switch (live-refreshable, parity with the
        cancel kill-switch).

        Args:
            purchase_order_id: Walmart Purchase Order ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/regulatedInfo"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/acknowledge"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/cancel"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Records the terminal ``Delivered`` event for one or more order lines, optionally with package-level
        proof-of-delivery (tracking number, package number, delivery timestamp). This is separated from
        ``/shipment-status`` because delivery is a terminal state and carries different downstream semantics (invoicing
        windows open, return windows start).

        Walmart parity from gmp-orders-mono ``deliverOrder``.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/deliver"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Send a ``GET`` request.

        Args:
            purchase_order_id: Walmart Purchase Order ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrderResponse],
            error_mapper=get_order_error_mapper,
            request_options=request_options,
        )

    async def get_order_address(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderAddressResponse, GetOrderAddressErrorBody]:
        """Returns the ship-to postal address for a single purchase order. Mirrors Amazon SP-API ``getOrderAddress``.
        PII-restricted endpoint: handlers are marked ``@RestrictedData`` server-side and the response body must NOT be
        logged.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/address"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrderAddressResponse],
            error_mapper=get_order_address_error_mapper,
            request_options=request_options,
        )

    async def get_order_buyer_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderBuyerInfoResponse, GetOrderBuyerInfoErrorBody]:
        """Returns the buyer's display name, email address, and an anonymized phone (last 4 digits only). Mirrors Amazon
        SP-API ``getOrderBuyerInfo``. PII-restricted endpoint: handlers are marked ``@RestrictedData`` server-side and
        request/response bodies must NOT be logged.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/buyerInfo"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOrderBuyerInfoResponse],
            error_mapper=get_order_buyer_info_error_mapper,
            request_options=request_options,
        )

    async def get_order_items(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetFulfillmentOrderShipmentsResponse, GetOrderItemsErrorBody]:
        """Returns the SKU / quantity / item-price projection of a single purchase order. Mirrors Amazon SP-API
        ``getOrderItems``. Not PII-restricted: only product, quantity, and price are returned.

        Args:
            purchase_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/items"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFulfillmentOrderShipmentsResponse],
            error_mapper=get_order_items_error_mapper,
            request_options=request_options,
        )

    async def get_order_regulated_info(
        self, purchase_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetOrderRegulatedInfoResponse, GetOrderRegulatedInfoErrorBody]:
        """Parity with Amazon SP-API Orders v0 ``getOrderRegulatedInfo``. Returns the verification requirements that
        apply to an order containing regulated items (alcohol, tobacco, age-restricted goods): the required
        ID-verification method, the minimum buyer age, the regulated category, and any value-added services the order
        ships with.

        **Walmart OMS coverage gap .** The the underlying service Order Lookup response does not currently surface
        regulated-item metadata. Until upstream support lands (tracked separately as a follow-up to this PR), every
        order returns the safe default ``regulatedCategory=NOT_REGULATED`` with ``requiredVerificationMethod=NONE``. The
        endpoint shape and contract are stable; only the projected values will become richer once OMS exposes the
        fields.

        Args:
            purchase_order_id: Walmart Purchase Order ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/regulatedInfo"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        order_statuses: list[OrderStatusOrStr] | None = None,
        fulfillment_types: list[FulfillmentTypeOrStr] | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFulfillmentOrderResponse, GetOrdersErrorBody]:
        """Returns orders matching the given filters. Orders are fulfilled by sellers (WFS or seller-fulfilled). Maps to
        Walmart OMS order queries.

        ### Current limitations (roadmap)

        The underlying the Orders service backend does not yet support every filter declared below. Calls using any of
        the following will return ``400 Bad Request`` with ``code=FILTER_NOT_SUPPORTED`` and a human-readable
        ``message`` explaining the specific rejection. Phase 2 will lift these one-by-one as the underlying service adds
        capability.

        | Filter | Status today | Reason |
        |---|---|---|
        | ``createdAfter``, ``createdBefore`` | Rejected (400) | the Orders service does not accept date-range filters
            at the order level. |
        | ``lastUpdatedAfter`` | Rejected (400) | the underlying service has no order-level update-date index. |
        | ``orderStatuses`` with >1 value | Rejected (400) | the underlying service accepts one status per call; pass a
            single value or omit to match all. |
        | ``fulfillmentTypes`` | Rejected (400) | the underlying service accepts one shipNodeType per call; multi-type
            fan-out is Phase 2. |

        These parameters remain in the contract (rather than being removed) so that SDKs generated today stay
        forward-compatible with the the roadmap surface — your code keeps compiling, only the runtime behaviour changes
        when Phase 2 ships. Until then, omit them or handle the documented 400 gracefully. The ``tools/loadgen-orders.sh
        --contract`` smoke sweep exercises the rejection contract on every run.

        Args:
            created_after: Filter orders created after this date-time (ISO 8601). **the roadmap — not yet supported.**
                Sending this parameter today returns ``400 FILTER_NOT_SUPPORTED``; the Orders service does not accept
                date-range filters at the order level. Tracked by . Retained in the contract so SDKs generated today
                stay forward-compatible.
            created_before: Filter orders created before this date-time (ISO 8601). **the roadmap — not yet supported.**
                See ``createdAfter`` for the rationale and the tracking ticket.
            last_updated_after: Filter orders updated after this date-time (ISO 8601). **the roadmap — not yet
                supported.** Sending this parameter today returns ``400 FILTER_NOT_SUPPORTED``; the Orders service has
                no order-level update-date index. Tracked by .
            order_statuses: Filter by order status. **the roadmap limitation:** the Orders service accepts AT MOST ONE
                status per call. Passing multiple values today returns `400 FILTER_NOT_SUPPORTED`; pass a single value
                or omit to match all. Multi-status fan-out tracked by .
            fulfillment_types: Filter by fulfillment type. **the roadmap — not yet supported.** Sending this parameter
                today returns ``400 FILTER_NOT_SUPPORTED``; the underlying service accepts one shipNodeType per call and
                multi-type fan-out is Phase 2. Tracked by .
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/orders/v4/orders"),
            query_params=[
                param[RFC3339DateTime | None]("createdAfter", created_after),
                param[RFC3339DateTime | None]("createdBefore", created_before),
                param[RFC3339DateTime | None]("lastUpdatedAfter", last_updated_after),
                param[list[OrderStatusOrStr] | None]("orderStatuses", order_statuses),
                param[list[FulfillmentTypeOrStr] | None]("fulfillmentTypes", fulfillment_types),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFulfillmentOrderResponse],
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
        """Walmart-specific write — no Amazon SP-API Orders v0 equivalent (Amazon refunds live in the Finance API).
        Mirrors gmp-orders-mono's legacy ``/partner-api/{market}/v3/orders/{po}/refund`` contract, simplified for the v4
        surface: a flat ``orderLines[]`` with per-line refund amount + reason instead of the legacy three-level nesting
        (``orderLines → refunds → refundCharges``).

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/refund"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Send a ``POST`` request.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/shipping"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Walmart-specific extension of ``/shipping``. Each package carries its own tracking number, carrier,
        dimensions, and the order lines it covers. Maps onto FMS's existing ``shipments[]`` envelope (one FMS shipment
        per v4 package). Inspired by gmp-orders-mono's ``shipOrderV2`` (multiPackageShipping) operation; we hoist
        ``packages[]`` to the top level rather than nesting it under each line so the request stays self-evidently
        package-oriented.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/multi-package-shipping"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Records a non-terminal shipment-lifecycle event for an order (ready for pickup, picked up, in transit, out
        for delivery). Use the dedicated ``/deliver`` endpoint for terminal delivery — it carries proof-of-delivery
        semantics this endpoint does not.

        Amazon SP-API Orders v0 ``updateShipmentStatus`` parity.

        Args:
            purchase_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/shipment-status"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
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
        """Parity with Amazon SP-API Orders v0 ``updateVerificationStatus``. The seller calls this after delivering a
        regulated-item order to record whether the buyer's identity / age was verified at the doorstep. An APPROVED
        status releases the order for settlement; REJECTED requires a ``rejectionReason`` and triggers downstream
        return-processing.

        Gated by the CCM-managed ``orders.features.regulatedInfoEnabled`` kill-switch (live-refreshable, parity with the
        cancel kill-switch).

        Args:
            purchase_order_id: Walmart Purchase Order ID
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default1("/orders/v4/orders/{purchaseOrderId}/regulatedInfo"),
            path_params=[param[str]("purchaseOrderId", purchase_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateVerificationStatusRequest | UpdateVerificationStatusRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[UpdateVerificationStatusResponse],
            error_mapper=update_verification_status_error_mapper,
            request_options=request_options,
        )
