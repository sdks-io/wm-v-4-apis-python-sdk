from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_my_fees_estimate_for_item_error import (
    GetMyFeesEstimateForItemErrorBody,
    get_my_fees_estimate_for_item_error_mapper,
)
from ..errors.get_my_fees_estimate_for_sku_error import (
    GetMyFeesEstimateForSkuErrorBody,
    get_my_fees_estimate_for_sku_error_mapper,
)
from ..errors.get_my_fees_estimates_error import GetMyFeesEstimatesErrorBody, get_my_fees_estimates_error_mapper
from ..models.fees_estimate_by_id_request import FeesEstimateByIdRequest, FeesEstimateByIdRequestDict
from ..models.fees_estimate_result import FeesEstimateResult
from ..models.get_my_fees_estimate_request import GetMyFeesEstimateRequest, GetMyFeesEstimateRequestDict
from ..models.get_my_fees_estimate_response import GetMyFeesEstimateResponse
from ..server.server import Server


class ProductFees:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProductFeesWithRawResponse(client, server, auth)

    def get_my_fees_estimate_for_item(
        self,
        walmart_item_id: str,
        body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetMyFeesEstimateResponse:
        """Returns an estimated fee for a single item identified by Walmart Item ID. Walmart Item ID replaces the SP-API
        ASIN path parameter.

        SP-API equivalent: ``getMyFeesEstimateForASIN`` (identifier changed from ASIN to Walmart Item ID;
        request/response shape is otherwise 1:1).

        Args:
            walmart_item_id: The Walmart Item ID of the item. Replaces SP-API ASIN.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_my_fees_estimate_for_item(
                walmart_item_id, body, request_options=request_options
            ),
        )

    def get_my_fees_estimate_for_sku(
        self,
        seller_sku: str,
        marketplace_id: str,
        body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetMyFeesEstimateResponse:
        """Returns an estimated fee for a seller listing identified by Seller SKU.

        Args:
            seller_sku: The seller's SKU for the listing. Scoped to the authenticated seller.
            marketplace_id: Marketplace identifier.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_my_fees_estimate_for_sku(
                seller_sku, marketplace_id, body, request_options=request_options
            ),
        )

    def get_my_fees_estimates(
        self,
        body: list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FeesEstimateResult]:
        """Returns estimated Walmart fees for a list of items identified by Walmart Item ID or Seller SKU.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_my_fees_estimates(body, request_options=request_options))

    @property
    def with_raw_response(self) -> ProductFeesWithRawResponse:
        return self._with_raw_response


class AsyncProductFees:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProductFeesWithRawResponse(client, server, auth)

    async def get_my_fees_estimate_for_item(
        self,
        walmart_item_id: str,
        body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetMyFeesEstimateResponse:
        """Returns an estimated fee for a single item identified by Walmart Item ID. Walmart Item ID replaces the SP-API
        ASIN path parameter.

        SP-API equivalent: ``getMyFeesEstimateForASIN`` (identifier changed from ASIN to Walmart Item ID;
        request/response shape is otherwise 1:1).

        Args:
            walmart_item_id: The Walmart Item ID of the item. Replaces SP-API ASIN.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_my_fees_estimate_for_item(
                walmart_item_id, body, request_options=request_options
            ),
        )

    async def get_my_fees_estimate_for_sku(
        self,
        seller_sku: str,
        marketplace_id: str,
        body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetMyFeesEstimateResponse:
        """Returns an estimated fee for a seller listing identified by Seller SKU.

        Args:
            seller_sku: The seller's SKU for the listing. Scoped to the authenticated seller.
            marketplace_id: Marketplace identifier.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_my_fees_estimate_for_sku(
                seller_sku, marketplace_id, body, request_options=request_options
            ),
        )

    async def get_my_fees_estimates(
        self,
        body: list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[FeesEstimateResult]:
        """Returns estimated Walmart fees for a list of items identified by Walmart Item ID or Seller SKU.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.get_my_fees_estimates(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncProductFeesWithRawResponse:
        return self._with_raw_response


class ProductFeesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_my_fees_estimate_for_item(
        self,
        walmart_item_id: str,
        body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetMyFeesEstimateResponse, GetMyFeesEstimateForItemErrorBody]:
        """Returns an estimated fee for a single item identified by Walmart Item ID. Walmart Item ID replaces the SP-API
        ASIN path parameter.

        SP-API equivalent: ``getMyFeesEstimateForASIN`` (identifier changed from ASIN to Walmart Item ID;
        request/response shape is otherwise 1:1).

        Args:
            walmart_item_id: The Walmart Item ID of the item. Replaces SP-API ASIN.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/products/fees/v4/items/{WalmartItemId}/feesEstimate"),
            path_params=[param[str]("WalmartItemId", walmart_item_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetMyFeesEstimateResponse],
            error_mapper=get_my_fees_estimate_for_item_error_mapper,
            request_options=request_options,
        )

    def get_my_fees_estimate_for_sku(
        self,
        seller_sku: str,
        marketplace_id: str,
        body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetMyFeesEstimateResponse, GetMyFeesEstimateForSkuErrorBody]:
        """Returns an estimated fee for a seller listing identified by Seller SKU.

        Args:
            seller_sku: The seller's SKU for the listing. Scoped to the authenticated seller.
            marketplace_id: Marketplace identifier.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/products/fees/v4/listings/{SellerSKU}/feesEstimate"),
            path_params=[param[str]("SellerSKU", seller_sku)],
            query_params=[param[str]("MarketplaceId", marketplace_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetMyFeesEstimateResponse],
            error_mapper=get_my_fees_estimate_for_sku_error_mapper,
            request_options=request_options,
        )

    def get_my_fees_estimates(
        self,
        body: list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[FeesEstimateResult], GetMyFeesEstimatesErrorBody]:
        """Returns estimated Walmart fees for a list of items identified by Walmart Item ID or Seller SKU.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/products/fees/v4/feesEstimate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict]](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[list[FeesEstimateResult]],
            error_mapper=get_my_fees_estimates_error_mapper,
            request_options=request_options,
        )


class AsyncProductFeesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_my_fees_estimate_for_item(
        self,
        walmart_item_id: str,
        body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetMyFeesEstimateResponse, GetMyFeesEstimateForItemErrorBody]:
        """Returns an estimated fee for a single item identified by Walmart Item ID. Walmart Item ID replaces the SP-API
        ASIN path parameter.

        SP-API equivalent: ``getMyFeesEstimateForASIN`` (identifier changed from ASIN to Walmart Item ID;
        request/response shape is otherwise 1:1).

        Args:
            walmart_item_id: The Walmart Item ID of the item. Replaces SP-API ASIN.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/products/fees/v4/items/{WalmartItemId}/feesEstimate"),
            path_params=[param[str]("WalmartItemId", walmart_item_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetMyFeesEstimateResponse],
            error_mapper=get_my_fees_estimate_for_item_error_mapper,
            request_options=request_options,
        )

    async def get_my_fees_estimate_for_sku(
        self,
        seller_sku: str,
        marketplace_id: str,
        body: GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetMyFeesEstimateResponse, GetMyFeesEstimateForSkuErrorBody]:
        """Returns an estimated fee for a seller listing identified by Seller SKU.

        Args:
            seller_sku: The seller's SKU for the listing. Scoped to the authenticated seller.
            marketplace_id: Marketplace identifier.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/products/fees/v4/listings/{SellerSKU}/feesEstimate"),
            path_params=[param[str]("SellerSKU", seller_sku)],
            query_params=[param[str]("MarketplaceId", marketplace_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetMyFeesEstimateRequest | GetMyFeesEstimateRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetMyFeesEstimateResponse],
            error_mapper=get_my_fees_estimate_for_sku_error_mapper,
            request_options=request_options,
        )

    async def get_my_fees_estimates(
        self,
        body: list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict],
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[FeesEstimateResult], GetMyFeesEstimatesErrorBody]:
        """Returns estimated Walmart fees for a list of items identified by Walmart Item ID or Seller SKU.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/products/fees/v4/feesEstimate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[list[FeesEstimateByIdRequest | FeesEstimateByIdRequestDict]](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[list[FeesEstimateResult]],
            error_mapper=get_my_fees_estimates_error_mapper,
            request_options=request_options,
        )
