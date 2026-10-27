from __future__ import annotations

from typing import Any
from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_product_review_and_seller_feedback_solicitation_error import (
    CreateProductReviewAndSellerFeedbackSolicitationErrorBody,
    create_product_review_and_seller_feedback_solicitation_error_mapper,
)
from ..errors.get_solicitation_actions_for_order_error import (
    GetSolicitationActionsForOrderErrorBody,
    get_solicitation_actions_for_order_error_mapper,
)
from ..server.server import Server


class Solicitations:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SolicitationsWithRawResponse(client, server, auth)

    def create_product_review_and_seller_feedback_solicitation(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: An SP-API order identifier. This specifies the order for which a solicitation is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be spec
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.create_product_review_and_seller_feedback_solicitation(
                sp_api_order_id, marketplace_ids, request_options=request_options
            ),
        )

    def get_solicitation_actions_for_order(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: An SP-API order identifier. This specifies the order for which you want a list of available
                solicitation types.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be spec
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_solicitation_actions_for_order(
                sp_api_order_id, marketplace_ids, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> SolicitationsWithRawResponse:
        return self._with_raw_response


class AsyncSolicitations:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSolicitationsWithRawResponse(client, server, auth)

    async def create_product_review_and_seller_feedback_solicitation(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: An SP-API order identifier. This specifies the order for which a solicitation is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be spec
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.create_product_review_and_seller_feedback_solicitation(
                sp_api_order_id, marketplace_ids, request_options=request_options
            ),
        )

    async def get_solicitation_actions_for_order(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: An SP-API order identifier. This specifies the order for which you want a list of available
                solicitation types.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be spec
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_solicitation_actions_for_order(
                sp_api_order_id, marketplace_ids, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSolicitationsWithRawResponse:
        return self._with_raw_response


class SolicitationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_product_review_and_seller_feedback_solicitation(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, CreateProductReviewAndSellerFeedbackSolicitationErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: An SP-API order identifier. This specifies the order for which a solicitation is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be spec
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/solicitations/v4/orders/{sp-apiOrderId}/solicitations/productReviewAndSellerFeedback"
            ),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_product_review_and_seller_feedback_solicitation_error_mapper,
            request_options=request_options,
        )

    def get_solicitation_actions_for_order(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetSolicitationActionsForOrderErrorBody]:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: An SP-API order identifier. This specifies the order for which you want a list of available
                solicitation types.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be spec
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/solicitations/v4/orders/{sp-apiOrderId}"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=get_solicitation_actions_for_order_error_mapper,
            request_options=request_options,
        )


class AsyncSolicitationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_product_review_and_seller_feedback_solicitation(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, CreateProductReviewAndSellerFeedbackSolicitationErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: An SP-API order identifier. This specifies the order for which a solicitation is sent.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be spec
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/solicitations/v4/orders/{sp-apiOrderId}/solicitations/productReviewAndSellerFeedback"
            ),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_product_review_and_seller_feedback_solicitation_error_mapper,
            request_options=request_options,
        )

    async def get_solicitation_actions_for_order(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetSolicitationActionsForOrderErrorBody]:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: An SP-API order identifier. This specifies the order for which you want a list of available
                solicitation types.
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be spec
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/solicitations/v4/orders/{sp-apiOrderId}"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=get_solicitation_actions_for_order_error_mapper,
            request_options=request_options,
        )
