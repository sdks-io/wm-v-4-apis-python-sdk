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
from ..errors.cancel_fulfillment_order_error import (
    CancelFulfillmentOrderErrorBody,
    cancel_fulfillment_order_error_mapper,
)
from ..errors.create_fulfillment_order_error import (
    CreateFulfillmentOrderErrorBody,
    create_fulfillment_order_error_mapper,
)
from ..errors.get_fulfillment_order_error import GetFulfillmentOrderErrorBody, get_fulfillment_order_error_mapper
from ..errors.get_fulfillment_order_shipments_error import (
    GetFulfillmentOrderShipmentsErrorBody,
    get_fulfillment_order_shipments_error_mapper,
)
from ..errors.get_fulfillment_preview_error import GetFulfillmentPreviewErrorBody, get_fulfillment_preview_error_mapper
from ..errors.list_all_fulfillment_orders_error import (
    ListAllFulfillmentOrdersErrorBody,
    list_all_fulfillment_orders_error_mapper,
)
from ..errors.update_fulfillment_order_error import (
    UpdateFulfillmentOrderErrorBody,
    update_fulfillment_order_error_mapper,
)
from ..models.cancel_fulfillment_order_response import CancelFulfillmentOrderResponse
from ..models.create_fulfillment_order_request import CreateFulfillmentOrderRequest, CreateFulfillmentOrderRequestDict
from ..models.create_fulfillment_order_response import CreateFulfillmentOrderResponse
from ..models.get_fulfillment_order_response import GetFulfillmentOrderResponse
from ..models.get_fulfillment_order_shipments_response import GetFulfillmentOrderShipmentsResponse
from ..models.get_fulfillment_preview_request import GetFulfillmentPreviewRequest, GetFulfillmentPreviewRequestDict
from ..models.get_fulfillment_preview_response import GetFulfillmentPreviewResponse
from ..models.list_all_fulfillment_orders_response import ListAllFulfillmentOrdersResponse
from ..models.update_fulfillment_order_request import UpdateFulfillmentOrderRequest, UpdateFulfillmentOrderRequestDict
from ..models.update_fulfillment_order_response import UpdateFulfillmentOrderResponse
from ..server.server import Server


class FulfillmentOutbound:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FulfillmentOutboundWithRawResponse(client, server, auth)

    def cancel_fulfillment_order(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelFulfillmentOrderResponse:
        """Send a ``PUT`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation request submitted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.cancel_fulfillment_order(
                seller_fulfillment_order_id, request_options=request_options
            ),
        )

    def create_fulfillment_order(
        self,
        body: CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateFulfillmentOrderResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Fulfillment order created

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.create_fulfillment_order(body, request_options=request_options))

    def get_fulfillment_order(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetFulfillmentOrderResponse:
        """Send a ``GET`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_fulfillment_order(seller_fulfillment_order_id, request_options=request_options)
        )

    def get_fulfillment_order_shipments(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetFulfillmentOrderShipmentsResponse:
        """Send a ``GET`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_fulfillment_order_shipments(
                seller_fulfillment_order_id, request_options=request_options
            ),
        )

    def get_fulfillment_preview(
        self,
        body: GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFulfillmentPreviewResponse:
        """Returns estimated delivery dates, shipping costs, and available ship nodes for a prospective fulfillment
        order. Use before creating the order.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.get_fulfillment_preview(body, request_options=request_options))

    def list_all_fulfillment_orders(
        self,
        *,
        query_start_date: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAllFulfillmentOrdersResponse:
        """Send a ``GET`` request.

        Args:
            query_start_date: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.list_all_fulfillment_orders(
                query_start_date=query_start_date, next_token=next_token, request_options=request_options
            ),
        )

    def update_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
        body: UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateFulfillmentOrderResponse:
        """Send a ``PUT`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Order updated

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.update_fulfillment_order(
                seller_fulfillment_order_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> FulfillmentOutboundWithRawResponse:
        return self._with_raw_response


class AsyncFulfillmentOutbound:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFulfillmentOutboundWithRawResponse(client, server, auth)

    async def cancel_fulfillment_order(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelFulfillmentOrderResponse:
        """Send a ``PUT`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation request submitted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_fulfillment_order(
                seller_fulfillment_order_id, request_options=request_options
            ),
        )

    async def create_fulfillment_order(
        self,
        body: CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateFulfillmentOrderResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Fulfillment order created

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.create_fulfillment_order(body, request_options=request_options))

    async def get_fulfillment_order(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetFulfillmentOrderResponse:
        """Send a ``GET`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_fulfillment_order(
                seller_fulfillment_order_id, request_options=request_options
            ),
        )

    async def get_fulfillment_order_shipments(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetFulfillmentOrderShipmentsResponse:
        """Send a ``GET`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_fulfillment_order_shipments(
                seller_fulfillment_order_id, request_options=request_options
            ),
        )

    async def get_fulfillment_preview(
        self,
        body: GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFulfillmentPreviewResponse:
        """Returns estimated delivery dates, shipping costs, and available ship nodes for a prospective fulfillment
        order. Use before creating the order.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.get_fulfillment_preview(body, request_options=request_options))

    async def list_all_fulfillment_orders(
        self,
        *,
        query_start_date: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListAllFulfillmentOrdersResponse:
        """Send a ``GET`` request.

        Args:
            query_start_date: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.list_all_fulfillment_orders(
                query_start_date=query_start_date, next_token=next_token, request_options=request_options
            ),
        )

    async def update_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
        body: UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateFulfillmentOrderResponse:
        """Send a ``PUT`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Order updated

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.update_fulfillment_order(
                seller_fulfillment_order_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncFulfillmentOutboundWithRawResponse:
        return self._with_raw_response


class FulfillmentOutboundWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_fulfillment_order(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelFulfillmentOrderResponse, CancelFulfillmentOrderErrorBody]:
        """Send a ``PUT`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel"),
            path_params=[param[str]("sellerFulfillmentOrderId", seller_fulfillment_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelFulfillmentOrderResponse],
            error_mapper=cancel_fulfillment_order_error_mapper,
            request_options=request_options,
        )

    def create_fulfillment_order(
        self,
        body: CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateFulfillmentOrderResponse, CreateFulfillmentOrderErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateFulfillmentOrderResponse],
            error_mapper=create_fulfillment_order_error_mapper,
            request_options=request_options,
        )

    def get_fulfillment_order(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetFulfillmentOrderResponse, GetFulfillmentOrderErrorBody]:
        """Send a ``GET`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}"),
            path_params=[param[str]("sellerFulfillmentOrderId", seller_fulfillment_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFulfillmentOrderResponse],
            error_mapper=get_fulfillment_order_error_mapper,
            request_options=request_options,
        )

    def get_fulfillment_order_shipments(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetFulfillmentOrderShipmentsResponse, GetFulfillmentOrderShipmentsErrorBody]:
        """Send a ``GET`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}/shipments"
            ),
            path_params=[param[str]("sellerFulfillmentOrderId", seller_fulfillment_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFulfillmentOrderShipmentsResponse],
            error_mapper=get_fulfillment_order_shipments_error_mapper,
            request_options=request_options,
        )

    def get_fulfillment_preview(
        self,
        body: GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFulfillmentPreviewResponse, GetFulfillmentPreviewErrorBody]:
        """Returns estimated delivery dates, shipping costs, and available ship nodes for a prospective fulfillment
        order. Use before creating the order.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders/preview"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFulfillmentPreviewResponse],
            error_mapper=get_fulfillment_preview_error_mapper,
            request_options=request_options,
        )

    def list_all_fulfillment_orders(
        self,
        *,
        query_start_date: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAllFulfillmentOrdersResponse, ListAllFulfillmentOrdersErrorBody]:
        """Send a ``GET`` request.

        Args:
            query_start_date: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders"),
            query_params=[
                param[RFC3339DateTime | None]("queryStartDate", query_start_date),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListAllFulfillmentOrdersResponse],
            error_mapper=list_all_fulfillment_orders_error_mapper,
            request_options=request_options,
        )

    def update_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
        body: UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateFulfillmentOrderResponse, UpdateFulfillmentOrderErrorBody]:
        """Send a ``PUT`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}"),
            path_params=[param[str]("sellerFulfillmentOrderId", seller_fulfillment_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[UpdateFulfillmentOrderResponse],
            error_mapper=update_fulfillment_order_error_mapper,
            request_options=request_options,
        )


class AsyncFulfillmentOutboundWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_fulfillment_order(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelFulfillmentOrderResponse, CancelFulfillmentOrderErrorBody]:
        """Send a ``PUT`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}/cancel"),
            path_params=[param[str]("sellerFulfillmentOrderId", seller_fulfillment_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelFulfillmentOrderResponse],
            error_mapper=cancel_fulfillment_order_error_mapper,
            request_options=request_options,
        )

    async def create_fulfillment_order(
        self,
        body: CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateFulfillmentOrderResponse, CreateFulfillmentOrderErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateFulfillmentOrderRequest | CreateFulfillmentOrderRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateFulfillmentOrderResponse],
            error_mapper=create_fulfillment_order_error_mapper,
            request_options=request_options,
        )

    async def get_fulfillment_order(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetFulfillmentOrderResponse, GetFulfillmentOrderErrorBody]:
        """Send a ``GET`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}"),
            path_params=[param[str]("sellerFulfillmentOrderId", seller_fulfillment_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFulfillmentOrderResponse],
            error_mapper=get_fulfillment_order_error_mapper,
            request_options=request_options,
        )

    async def get_fulfillment_order_shipments(
        self, seller_fulfillment_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetFulfillmentOrderShipmentsResponse, GetFulfillmentOrderShipmentsErrorBody]:
        """Send a ``GET`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1(
                "/wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}/shipments"
            ),
            path_params=[param[str]("sellerFulfillmentOrderId", seller_fulfillment_order_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFulfillmentOrderShipmentsResponse],
            error_mapper=get_fulfillment_order_shipments_error_mapper,
            request_options=request_options,
        )

    async def get_fulfillment_preview(
        self,
        body: GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFulfillmentPreviewResponse, GetFulfillmentPreviewErrorBody]:
        """Returns estimated delivery dates, shipping costs, and available ship nodes for a prospective fulfillment
        order. Use before creating the order.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders/preview"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetFulfillmentPreviewRequest | GetFulfillmentPreviewRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFulfillmentPreviewResponse],
            error_mapper=get_fulfillment_preview_error_mapper,
            request_options=request_options,
        )

    async def list_all_fulfillment_orders(
        self,
        *,
        query_start_date: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListAllFulfillmentOrdersResponse, ListAllFulfillmentOrdersErrorBody]:
        """Send a ``GET`` request.

        Args:
            query_start_date: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders"),
            query_params=[
                param[RFC3339DateTime | None]("queryStartDate", query_start_date),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListAllFulfillmentOrdersResponse],
            error_mapper=list_all_fulfillment_orders_error_mapper,
            request_options=request_options,
        )

    async def update_fulfillment_order(
        self,
        seller_fulfillment_order_id: str,
        body: UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateFulfillmentOrderResponse, UpdateFulfillmentOrderErrorBody]:
        """Send a ``PUT`` request.

        Args:
            seller_fulfillment_order_id: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/wfs/outbound/v4/fulfillmentOrders/{sellerFulfillmentOrderId}"),
            path_params=[param[str]("sellerFulfillmentOrderId", seller_fulfillment_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateFulfillmentOrderRequest | UpdateFulfillmentOrderRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[UpdateFulfillmentOrderResponse],
            error_mapper=update_fulfillment_order_error_mapper,
            request_options=request_options,
        )
