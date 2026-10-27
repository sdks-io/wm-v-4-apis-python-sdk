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
from ..errors.get_competitive_pricing_error import GetCompetitivePricingErrorBody, get_competitive_pricing_error_mapper
from ..errors.get_competitive_summary_error import GetCompetitiveSummaryErrorBody, get_competitive_summary_error_mapper
from ..errors.get_featured_offer_expected_price_batch_error import (
    GetFeaturedOfferExpectedPriceBatchErrorBody,
    get_featured_offer_expected_price_batch_error_mapper,
)
from ..errors.get_item_offers_batch_error import GetItemOffersBatchErrorBody, get_item_offers_batch_error_mapper
from ..errors.get_item_offers_error import GetItemOffersErrorBody, get_item_offers_error_mapper
from ..errors.get_listing_offers_batch_error import (
    GetListingOffersBatchErrorBody,
    get_listing_offers_batch_error_mapper,
)
from ..errors.get_listing_offers_error import GetListingOffersErrorBody, get_listing_offers_error_mapper
from ..errors.get_pricing_error import GetPricingErrorBody, get_pricing_error_mapper
from ..models.competitive_summary_batch_request import (
    CompetitiveSummaryBatchRequest,
    CompetitiveSummaryBatchRequestDict,
)
from ..models.competitive_summary_batch_response import CompetitiveSummaryBatchResponse
from ..models.enums.condition_type2 import ConditionType2OrStr
from ..models.enums.customer_type import CustomerTypeOrStr
from ..models.enums.item_type import ItemType, ItemTypeOrStr
from ..models.enums.offer_type import OfferTypeOrStr
from ..models.get_featured_offer_expected_price_batch_request import (
    GetFeaturedOfferExpectedPriceBatchRequest,
    GetFeaturedOfferExpectedPriceBatchRequestDict,
)
from ..models.get_featured_offer_expected_price_batch_response import GetFeaturedOfferExpectedPriceBatchResponse
from ..models.get_item_offers_batch_request import GetItemOffersBatchRequest, GetItemOffersBatchRequestDict
from ..models.get_item_offers_batch_response import GetItemOffersBatchResponse
from ..models.get_listing_offers_batch_request import GetListingOffersBatchRequest, GetListingOffersBatchRequestDict
from ..models.get_listing_offers_batch_response import GetListingOffersBatchResponse
from ..models.get_offers_response import GetOffersResponse
from ..models.get_pricing_response import GetPricingResponse
from ..server.server import Server


class ProductPricing:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProductPricingWithRawResponse(client, server, auth)

    def get_competitive_pricing(
        self,
        marketplace_id: str,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPricingResponse:
        """Returns competitive pricing information for a seller's offer listings based on seller SKU or Walmart Item ID
        .

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify items.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            walmart_item_ids: A list of up to twenty Walmart Item ID values used to identify items in the given
                marketplace.
            customer_type: Indicates whether to request pricing information from the point of view of Consumer or
                Business buyers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            self._with_raw_response.get_competitive_pricing(
                marketplace_id,
                item_type=item_type,
                skus=skus,
                walmart_item_ids=walmart_item_ids,
                customer_type=customer_type,
                request_options=request_options,
            ),
        )

    def get_competitive_summary(
        self,
        body: CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompetitiveSummaryBatchResponse:
        """**Planned — not yet available in production.** Returns competitive summary including featured buying options
        and lowest priced offers for a batch of Walmart Item IDs .

        **Phase 1 stub** — no upstream data source identified. Returns HTTP 501 until an upstream is confirmed. Track: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(self._with_raw_response.get_competitive_summary(body, request_options=request_options))

    def get_featured_offer_expected_price_batch(
        self,
        body: GetFeaturedOfferExpectedPriceBatchRequest | GetFeaturedOfferExpectedPriceBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFeaturedOfferExpectedPriceBatchResponse:
        """**Planned — not yet available in production.** Returns the featured offer expected price (FOEP) for a batch
        of seller SKUs.

        **Phase 1 stub** — no upstream data source identified. Returns HTTP 501 until an upstream is confirmed. Track: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            self._with_raw_response.get_featured_offer_expected_price_batch(body, request_options=request_options)
        )

    def get_item_offers(
        self,
        item_id: str,
        marketplace_id: str,
        item_condition: ConditionType2OrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOffersResponse:
        """Returns the lowest priced offers for a single item based on Walmart Item ID and item condition.

        Uses Walmart Item ID as the primary identifier(ASIN not supported — no ASIN resolver exists in the Walmart
        platform; IQS queries by product.item_id).

        Backed by IQS catalog_index cross-seller query (same as getListingOffers hop-2). Returns 404 when no offers are
        found for the given itemId.

        Args:
            item_id: The Walmart Item ID of the item.
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            self._with_raw_response.get_item_offers(
                item_id, marketplace_id, item_condition, customer_type=customer_type, request_options=request_options
            ),
        )

    def get_item_offers_batch(
        self,
        body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetItemOffersBatchResponse:
        """Batch version of getItemOffers. Accepts up to 20 Walmart Item ID requests. Uses Walmart Item ID as the
        primary identifier.

        Implemented as in-process fan-out over getItemOffers. Each item gets its own per-item HTTP status code in the
        response body; the outer HTTP response is always 200. Implemented: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(self._with_raw_response.get_item_offers_batch(body, request_options=request_options))

    def get_listing_offers(
        self,
        seller_sku: str,
        marketplace_id: str,
        item_condition: ConditionType2OrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOffersResponse:
        """Returns the lowest priced offers for a single SKU listing, based on SKU and item condition.

        Args:
            seller_sku: Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId.
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            self._with_raw_response.get_listing_offers(
                seller_sku, marketplace_id, item_condition, customer_type=customer_type, request_options=request_options
            ),
        )

    def get_listing_offers_batch(
        self,
        body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetListingOffersBatchResponse:
        """Batch version of getListingOffers. Accepts up to 20 SKU requests.

        Implemented as in-process fan-out over getListingOffers (IQS-backed). Each SKU gets its own per-item HTTP status
        code in the response body; the outer HTTP response is always 200. Implemented: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(self._with_raw_response.get_listing_offers_batch(body, request_options=request_options))

    def get_pricing(
        self,
        marketplace_id: str,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        item_condition: ConditionType2OrStr | None = None,
        offer_type: OfferTypeOrStr | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPricingResponse:
        """Returns pricing information for a seller's active offer listings based on seller SKU or Walmart Item ID .

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify items.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            walmart_item_ids: A list of up to twenty Walmart Item ID values used to identify items in the given
                marketplace.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            offer_type: Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is
                B2C.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            self._with_raw_response.get_pricing(
                marketplace_id,
                item_type=item_type,
                skus=skus,
                walmart_item_ids=walmart_item_ids,
                item_condition=item_condition,
                offer_type=offer_type,
                customer_type=customer_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ProductPricingWithRawResponse:
        return self._with_raw_response


class AsyncProductPricing:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProductPricingWithRawResponse(client, server, auth)

    async def get_competitive_pricing(
        self,
        marketplace_id: str,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPricingResponse:
        """Returns competitive pricing information for a seller's offer listings based on seller SKU or Walmart Item ID
        .

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify items.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            walmart_item_ids: A list of up to twenty Walmart Item ID values used to identify items in the given
                marketplace.
            customer_type: Indicates whether to request pricing information from the point of view of Consumer or
                Business buyers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_competitive_pricing(
                marketplace_id,
                item_type=item_type,
                skus=skus,
                walmart_item_ids=walmart_item_ids,
                customer_type=customer_type,
                request_options=request_options,
            ),
        )

    async def get_competitive_summary(
        self,
        body: CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompetitiveSummaryBatchResponse:
        """**Planned — not yet available in production.** Returns competitive summary including featured buying options
        and lowest priced offers for a batch of Walmart Item IDs .

        **Phase 1 stub** — no upstream data source identified. Returns HTTP 501 until an upstream is confirmed. Track: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(await self._with_raw_response.get_competitive_summary(body, request_options=request_options))

    async def get_featured_offer_expected_price_batch(
        self,
        body: GetFeaturedOfferExpectedPriceBatchRequest | GetFeaturedOfferExpectedPriceBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFeaturedOfferExpectedPriceBatchResponse:
        """**Planned — not yet available in production.** Returns the featured offer expected price (FOEP) for a batch
        of seller SKUs.

        **Phase 1 stub** — no upstream data source identified. Returns HTTP 501 until an upstream is confirmed. Track: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_featured_offer_expected_price_batch(body, request_options=request_options)
        )

    async def get_item_offers(
        self,
        item_id: str,
        marketplace_id: str,
        item_condition: ConditionType2OrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOffersResponse:
        """Returns the lowest priced offers for a single item based on Walmart Item ID and item condition.

        Uses Walmart Item ID as the primary identifier(ASIN not supported — no ASIN resolver exists in the Walmart
        platform; IQS queries by product.item_id).

        Backed by IQS catalog_index cross-seller query (same as getListingOffers hop-2). Returns 404 when no offers are
        found for the given itemId.

        Args:
            item_id: The Walmart Item ID of the item.
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_item_offers(
                item_id, marketplace_id, item_condition, customer_type=customer_type, request_options=request_options
            ),
        )

    async def get_item_offers_batch(
        self,
        body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetItemOffersBatchResponse:
        """Batch version of getItemOffers. Accepts up to 20 Walmart Item ID requests. Uses Walmart Item ID as the
        primary identifier.

        Implemented as in-process fan-out over getItemOffers. Each item gets its own per-item HTTP status code in the
        response body; the outer HTTP response is always 200. Implemented: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(await self._with_raw_response.get_item_offers_batch(body, request_options=request_options))

    async def get_listing_offers(
        self,
        seller_sku: str,
        marketplace_id: str,
        item_condition: ConditionType2OrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOffersResponse:
        """Returns the lowest priced offers for a single SKU listing, based on SKU and item condition.

        Args:
            seller_sku: Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId.
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_listing_offers(
                seller_sku, marketplace_id, item_condition, customer_type=customer_type, request_options=request_options
            ),
        )

    async def get_listing_offers_batch(
        self,
        body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetListingOffersBatchResponse:
        """Batch version of getListingOffers. Accepts up to 20 SKU requests.

        Implemented as in-process fan-out over getListingOffers (IQS-backed). Each SKU gets its own per-item HTTP status
        code in the response body; the outer HTTP response is always 200. Implemented: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(await self._with_raw_response.get_listing_offers_batch(body, request_options=request_options))

    async def get_pricing(
        self,
        marketplace_id: str,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        item_condition: ConditionType2OrStr | None = None,
        offer_type: OfferTypeOrStr | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPricingResponse:
        """Returns pricing information for a seller's active offer listings based on seller SKU or Walmart Item ID .

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify items.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            walmart_item_ids: A list of up to twenty Walmart Item ID values used to identify items in the given
                marketplace.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            offer_type: Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is
                B2C.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[Error3] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_pricing(
                marketplace_id,
                item_type=item_type,
                skus=skus,
                walmart_item_ids=walmart_item_ids,
                item_condition=item_condition,
                offer_type=offer_type,
                customer_type=customer_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncProductPricingWithRawResponse:
        return self._with_raw_response


class ProductPricingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_competitive_pricing(
        self,
        marketplace_id: str,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPricingResponse, GetCompetitivePricingErrorBody]:
        """Returns competitive pricing information for a seller's offer listings based on seller SKU or Walmart Item ID
        .

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify items.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            walmart_item_ids: A list of up to twenty Walmart Item ID values used to identify items in the given
                marketplace.
            customer_type: Indicates whether to request pricing information from the point of view of Consumer or
                Business buyers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/products/pricing/v4/competitivePrice"),
            query_params=[
                param[str]("MarketplaceId", marketplace_id),
                param[ItemTypeOrStr]("ItemType", item_type),
                param[list[str] | None]("Skus", skus),
                param[list[str] | None]("walmartItemIds", walmart_item_ids),
                param[CustomerTypeOrStr | None]("CustomerType", customer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetPricingResponse],
            error_mapper=get_competitive_pricing_error_mapper,
            request_options=request_options,
        )

    def get_competitive_summary(
        self,
        body: CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompetitiveSummaryBatchResponse, GetCompetitiveSummaryErrorBody]:
        """**Planned — not yet available in production.** Returns competitive summary including featured buying options
        and lowest priced offers for a batch of Walmart Item IDs .

        **Phase 1 stub** — no upstream data source identified. Returns HTTP 501 until an upstream is confirmed. Track: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/batches/products/pricing/v4/items/competitiveSummary"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CompetitiveSummaryBatchResponse],
            error_mapper=get_competitive_summary_error_mapper,
            request_options=request_options,
        )

    def get_featured_offer_expected_price_batch(
        self,
        body: GetFeaturedOfferExpectedPriceBatchRequest | GetFeaturedOfferExpectedPriceBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFeaturedOfferExpectedPriceBatchResponse, GetFeaturedOfferExpectedPriceBatchErrorBody]:
        """**Planned — not yet available in production.** Returns the featured offer expected price (FOEP) for a batch
        of seller SKUs.

        **Phase 1 stub** — no upstream data source identified. Returns HTTP 501 until an upstream is confirmed. Track: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/batches/products/pricing/v4/offer/featuredOfferExpectedPrice"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetFeaturedOfferExpectedPriceBatchRequest | GetFeaturedOfferExpectedPriceBatchRequestDict](
                body
            ),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFeaturedOfferExpectedPriceBatchResponse],
            error_mapper=get_featured_offer_expected_price_batch_error_mapper,
            request_options=request_options,
        )

    def get_item_offers(
        self,
        item_id: str,
        marketplace_id: str,
        item_condition: ConditionType2OrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOffersResponse, GetItemOffersErrorBody]:
        """Returns the lowest priced offers for a single item based on Walmart Item ID and item condition.

        Uses Walmart Item ID as the primary identifier(ASIN not supported — no ASIN resolver exists in the Walmart
        platform; IQS queries by product.item_id).

        Backed by IQS catalog_index cross-seller query (same as getListingOffers hop-2). Returns 404 when no offers are
        found for the given itemId.

        Args:
            item_id: The Walmart Item ID of the item.
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/products/pricing/v4/items/{itemId}/offers"),
            path_params=[param[str]("itemId", item_id)],
            query_params=[
                param[str]("MarketplaceId", marketplace_id),
                param[ConditionType2OrStr]("ItemCondition", item_condition),
                param[CustomerTypeOrStr | None]("CustomerType", customer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOffersResponse],
            error_mapper=get_item_offers_error_mapper,
            request_options=request_options,
        )

    def get_item_offers_batch(
        self,
        body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetItemOffersBatchResponse, GetItemOffersBatchErrorBody]:
        """Batch version of getItemOffers. Accepts up to 20 Walmart Item ID requests. Uses Walmart Item ID as the
        primary identifier.

        Implemented as in-process fan-out over getItemOffers. Each item gets its own per-item HTTP status code in the
        response body; the outer HTTP response is always 200. Implemented: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/batches/products/pricing/v4/itemOffers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetItemOffersBatchRequest | GetItemOffersBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetItemOffersBatchResponse],
            error_mapper=get_item_offers_batch_error_mapper,
            request_options=request_options,
        )

    def get_listing_offers(
        self,
        seller_sku: str,
        marketplace_id: str,
        item_condition: ConditionType2OrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOffersResponse, GetListingOffersErrorBody]:
        """Returns the lowest priced offers for a single SKU listing, based on SKU and item condition.

        Args:
            seller_sku: Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId.
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/products/pricing/v4/listings/{SellerSKU}/offers"),
            path_params=[param[str]("SellerSKU", seller_sku)],
            query_params=[
                param[str]("MarketplaceId", marketplace_id),
                param[ConditionType2OrStr]("ItemCondition", item_condition),
                param[CustomerTypeOrStr | None]("CustomerType", customer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetOffersResponse],
            error_mapper=get_listing_offers_error_mapper,
            request_options=request_options,
        )

    def get_listing_offers_batch(
        self,
        body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetListingOffersBatchResponse, GetListingOffersBatchErrorBody]:
        """Batch version of getListingOffers. Accepts up to 20 SKU requests.

        Implemented as in-process fan-out over getListingOffers (IQS-backed). Each SKU gets its own per-item HTTP status
        code in the response body; the outer HTTP response is always 200. Implemented: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/batches/products/pricing/v4/listingOffers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetListingOffersBatchRequest | GetListingOffersBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetListingOffersBatchResponse],
            error_mapper=get_listing_offers_batch_error_mapper,
            request_options=request_options,
        )

    def get_pricing(
        self,
        marketplace_id: str,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        item_condition: ConditionType2OrStr | None = None,
        offer_type: OfferTypeOrStr | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPricingResponse, GetPricingErrorBody]:
        """Returns pricing information for a seller's active offer listings based on seller SKU or Walmart Item ID .

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify items.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            walmart_item_ids: A list of up to twenty Walmart Item ID values used to identify items in the given
                marketplace.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            offer_type: Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is
                B2C.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/products/pricing/v4/price"),
            query_params=[
                param[str]("MarketplaceId", marketplace_id),
                param[ItemTypeOrStr]("ItemType", item_type),
                param[list[str] | None]("Skus", skus),
                param[list[str] | None]("walmartItemIds", walmart_item_ids),
                param[ConditionType2OrStr | None]("ItemCondition", item_condition),
                param[OfferTypeOrStr | None]("OfferType", offer_type),
                param[CustomerTypeOrStr | None]("CustomerType", customer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetPricingResponse],
            error_mapper=get_pricing_error_mapper,
            request_options=request_options,
        )


class AsyncProductPricingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_competitive_pricing(
        self,
        marketplace_id: str,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPricingResponse, GetCompetitivePricingErrorBody]:
        """Returns competitive pricing information for a seller's offer listings based on seller SKU or Walmart Item ID
        .

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify items.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            walmart_item_ids: A list of up to twenty Walmart Item ID values used to identify items in the given
                marketplace.
            customer_type: Indicates whether to request pricing information from the point of view of Consumer or
                Business buyers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/products/pricing/v4/competitivePrice"),
            query_params=[
                param[str]("MarketplaceId", marketplace_id),
                param[ItemTypeOrStr]("ItemType", item_type),
                param[list[str] | None]("Skus", skus),
                param[list[str] | None]("walmartItemIds", walmart_item_ids),
                param[CustomerTypeOrStr | None]("CustomerType", customer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetPricingResponse],
            error_mapper=get_competitive_pricing_error_mapper,
            request_options=request_options,
        )

    async def get_competitive_summary(
        self,
        body: CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompetitiveSummaryBatchResponse, GetCompetitiveSummaryErrorBody]:
        """**Planned — not yet available in production.** Returns competitive summary including featured buying options
        and lowest priced offers for a batch of Walmart Item IDs .

        **Phase 1 stub** — no upstream data source identified. Returns HTTP 501 until an upstream is confirmed. Track: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/batches/products/pricing/v4/items/competitiveSummary"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CompetitiveSummaryBatchResponse],
            error_mapper=get_competitive_summary_error_mapper,
            request_options=request_options,
        )

    async def get_featured_offer_expected_price_batch(
        self,
        body: GetFeaturedOfferExpectedPriceBatchRequest | GetFeaturedOfferExpectedPriceBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFeaturedOfferExpectedPriceBatchResponse, GetFeaturedOfferExpectedPriceBatchErrorBody]:
        """**Planned — not yet available in production.** Returns the featured offer expected price (FOEP) for a batch
        of seller SKUs.

        **Phase 1 stub** — no upstream data source identified. Returns HTTP 501 until an upstream is confirmed. Track: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/batches/products/pricing/v4/offer/featuredOfferExpectedPrice"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetFeaturedOfferExpectedPriceBatchRequest | GetFeaturedOfferExpectedPriceBatchRequestDict](
                body
            ),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFeaturedOfferExpectedPriceBatchResponse],
            error_mapper=get_featured_offer_expected_price_batch_error_mapper,
            request_options=request_options,
        )

    async def get_item_offers(
        self,
        item_id: str,
        marketplace_id: str,
        item_condition: ConditionType2OrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOffersResponse, GetItemOffersErrorBody]:
        """Returns the lowest priced offers for a single item based on Walmart Item ID and item condition.

        Uses Walmart Item ID as the primary identifier(ASIN not supported — no ASIN resolver exists in the Walmart
        platform; IQS queries by product.item_id).

        Backed by IQS catalog_index cross-seller query (same as getListingOffers hop-2). Returns 404 when no offers are
        found for the given itemId.

        Args:
            item_id: The Walmart Item ID of the item.
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/products/pricing/v4/items/{itemId}/offers"),
            path_params=[param[str]("itemId", item_id)],
            query_params=[
                param[str]("MarketplaceId", marketplace_id),
                param[ConditionType2OrStr]("ItemCondition", item_condition),
                param[CustomerTypeOrStr | None]("CustomerType", customer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOffersResponse],
            error_mapper=get_item_offers_error_mapper,
            request_options=request_options,
        )

    async def get_item_offers_batch(
        self,
        body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetItemOffersBatchResponse, GetItemOffersBatchErrorBody]:
        """Batch version of getItemOffers. Accepts up to 20 Walmart Item ID requests. Uses Walmart Item ID as the
        primary identifier.

        Implemented as in-process fan-out over getItemOffers. Each item gets its own per-item HTTP status code in the
        response body; the outer HTTP response is always 200. Implemented: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/batches/products/pricing/v4/itemOffers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetItemOffersBatchRequest | GetItemOffersBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetItemOffersBatchResponse],
            error_mapper=get_item_offers_batch_error_mapper,
            request_options=request_options,
        )

    async def get_listing_offers(
        self,
        seller_sku: str,
        marketplace_id: str,
        item_condition: ConditionType2OrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOffersResponse, GetListingOffersErrorBody]:
        """Returns the lowest priced offers for a single SKU listing, based on SKU and item condition.

        Args:
            seller_sku: Identifies an item in the given marketplace. SellerSKU is qualified by the seller's SellerId.
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/products/pricing/v4/listings/{SellerSKU}/offers"),
            path_params=[param[str]("SellerSKU", seller_sku)],
            query_params=[
                param[str]("MarketplaceId", marketplace_id),
                param[ConditionType2OrStr]("ItemCondition", item_condition),
                param[CustomerTypeOrStr | None]("CustomerType", customer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetOffersResponse],
            error_mapper=get_listing_offers_error_mapper,
            request_options=request_options,
        )

    async def get_listing_offers_batch(
        self,
        body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetListingOffersBatchResponse, GetListingOffersBatchErrorBody]:
        """Batch version of getListingOffers. Accepts up to 20 SKU requests.

        Implemented as in-process fan-out over getListingOffers (IQS-backed). Each SKU gets its own per-item HTTP status
        code in the response body; the outer HTTP response is always 200. Implemented: .

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/batches/products/pricing/v4/listingOffers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetListingOffersBatchRequest | GetListingOffersBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetListingOffersBatchResponse],
            error_mapper=get_listing_offers_batch_error_mapper,
            request_options=request_options,
        )

    async def get_pricing(
        self,
        marketplace_id: str,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        item_condition: ConditionType2OrStr | None = None,
        offer_type: OfferTypeOrStr | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPricingResponse, GetPricingErrorBody]:
        """Returns pricing information for a seller's active offer listings based on seller SKU or Walmart Item ID .

        Args:
            marketplace_id: A marketplace identifier. Specifies the marketplace for which prices are returned.
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify items.
            skus: A list of up to twenty seller SKU values used to identify items in the given marketplace.
            walmart_item_ids: A list of up to twenty Walmart Item ID values used to identify items in the given
                marketplace.
            item_condition: Filters the offer listings based on item condition. Possible values: New, Used, Collectible,
                Refurbished, Club.
            offer_type: Indicates whether to request pricing information for the seller's B2C or B2B offers. Default is
                B2C.
            customer_type: Indicates whether to request Consumer or Business offers. Default is Consumer.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/products/pricing/v4/price"),
            query_params=[
                param[str]("MarketplaceId", marketplace_id),
                param[ItemTypeOrStr]("ItemType", item_type),
                param[list[str] | None]("Skus", skus),
                param[list[str] | None]("walmartItemIds", walmart_item_ids),
                param[ConditionType2OrStr | None]("ItemCondition", item_condition),
                param[OfferTypeOrStr | None]("OfferType", offer_type),
                param[CustomerTypeOrStr | None]("CustomerType", customer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetPricingResponse],
            error_mapper=get_pricing_error_mapper,
            request_options=request_options,
        )
