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
from ..errors.get_buybox_offer_expected_price_batch_error import (
    GetBuyboxOfferExpectedPriceBatchErrorBody,
    get_buybox_offer_expected_price_batch_error_mapper,
)
from ..errors.get_competitive_pricing_error import GetCompetitivePricingErrorBody, get_competitive_pricing_error_mapper
from ..errors.get_competitive_summary_error import GetCompetitiveSummaryErrorBody, get_competitive_summary_error_mapper
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
from ..models.enums.condition_type_product_pricing import ConditionTypeProductPricingOrStr
from ..models.enums.customer_type import CustomerTypeOrStr
from ..models.enums.item_type import ItemType, ItemTypeOrStr
from ..models.enums.offer_customer_type import OfferCustomerTypeOrStr
from ..models.get_buybox_offer_expected_price_batch_request import (
    GetBuyboxOfferExpectedPriceBatchRequest,
    GetBuyboxOfferExpectedPriceBatchRequestDict,
)
from ..models.get_buybox_offer_expected_price_batch_response import GetBuyboxOfferExpectedPriceBatchResponse
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

    def get_buybox_offer_expected_price_batch(
        self,
        body: GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetBuyboxOfferExpectedPriceBatchResponse:
        """**Planned — not yet available in production.** Returns the Buybox Offer Expected Price (BOEP) for a batch of
        seller SKUs.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            self._with_raw_response.get_buybox_offer_expected_price_batch(body, request_options=request_options)
        )

    def get_competitive_pricing(
        self,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPricingResponse:
        """Returns competitive pricing information for seller offer listings identified by seller SKU or Walmart Item
        ID.

        Args:
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested
                items.
            skus: Seller SKUs that identify the items to return. Supports up to 20 values.
            walmart_item_ids: Walmart Item IDs that identify the items to return. Supports up to 20 values.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns competitive pricing information for the requested seller items.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            self._with_raw_response.get_competitive_pricing(
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
        """**Planned — not yet available in production.** Returns competitive summary information, including featured
        buying options and lowest-priced offers, for a batch of Walmart Item IDs.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns competitive summary results for the requested Walmart items.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(self._with_raw_response.get_competitive_summary(body, request_options=request_options))

    def get_item_offers(
        self,
        item_id: str,
        item_condition: ConditionTypeProductPricingOrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOffersResponse:
        """Returns the lowest-priced offers for a Walmart item with the specified item condition.

        Args:
            item_id: Walmart Item ID that identifies the item.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the lowest-priced offers for the requested Walmart item.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            self._with_raw_response.get_item_offers(
                item_id, item_condition, customer_type=customer_type, request_options=request_options
            ),
        )

    def get_item_offers_batch(
        self,
        body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetItemOffersBatchResponse:
        """Returns offer information for up to 20 Walmart Item ID requests. Each response entry contains an HTTP status
        for its corresponding item request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the results for the requested Walmart items.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(self._with_raw_response.get_item_offers_batch(body, request_options=request_options))

    def get_listing_offers(
        self,
        seller_sku: str,
        item_condition: ConditionTypeProductPricingOrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOffersResponse:
        """Returns the lowest-priced offers for a single SKU listing, based on SKU and item condition.

        Args:
            seller_sku: Seller SKU that identifies the item in the specified marketplace. The ``SellerSKU`` value is
                qualified by the seller's ``SellerId``.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the lowest-priced offers for the requested seller SKU.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            self._with_raw_response.get_listing_offers(
                seller_sku, item_condition, customer_type=customer_type, request_options=request_options
            ),
        )

    def get_listing_offers_batch(
        self,
        body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetListingOffersBatchResponse:
        """Returns offer information for up to 20 seller SKU requests. Each response entry contains an HTTP status for
        its corresponding seller SKU request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the results for the requested seller SKUs.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(self._with_raw_response.get_listing_offers_batch(body, request_options=request_options))

    def get_pricing(
        self,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        item_condition: ConditionTypeProductPricingOrStr | None = None,
        offer_type: OfferCustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPricingResponse:
        """Returns pricing information for the seller's listings, identified by seller SKU or Walmart Item ID.

        Args:
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested
                items.
            skus: Seller SKUs that identify the items to return. Supports up to 20 values.
            walmart_item_ids: Walmart Item IDs that identify the items to return. Supports up to 20 values.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            offer_type: Filters pricing information by business-to-consumer (``B2C``) or business-to-business (``B2B``)
                offer type. Default is ``B2C``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns pricing information for the requested seller items.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            self._with_raw_response.get_pricing(
                item_type=item_type,
                skus=skus,
                walmart_item_ids=walmart_item_ids,
                item_condition=item_condition,
                offer_type=offer_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ProductPricingWithRawResponse:
        return self._with_raw_response


class AsyncProductPricing:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProductPricingWithRawResponse(client, server, auth)

    async def get_buybox_offer_expected_price_batch(
        self,
        body: GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetBuyboxOfferExpectedPriceBatchResponse:
        """**Planned — not yet available in production.** Returns the Buybox Offer Expected Price (BOEP) for a batch of
        seller SKUs.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_buybox_offer_expected_price_batch(body, request_options=request_options)
        )

    async def get_competitive_pricing(
        self,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPricingResponse:
        """Returns competitive pricing information for seller offer listings identified by seller SKU or Walmart Item
        ID.

        Args:
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested
                items.
            skus: Seller SKUs that identify the items to return. Supports up to 20 values.
            walmart_item_ids: Walmart Item IDs that identify the items to return. Supports up to 20 values.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns competitive pricing information for the requested seller items.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_competitive_pricing(
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
        """**Planned — not yet available in production.** Returns competitive summary information, including featured
        buying options and lowest-priced offers, for a batch of Walmart Item IDs.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns competitive summary results for the requested Walmart items.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(await self._with_raw_response.get_competitive_summary(body, request_options=request_options))

    async def get_item_offers(
        self,
        item_id: str,
        item_condition: ConditionTypeProductPricingOrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOffersResponse:
        """Returns the lowest-priced offers for a Walmart item with the specified item condition.

        Args:
            item_id: Walmart Item ID that identifies the item.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the lowest-priced offers for the requested Walmart item.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_item_offers(
                item_id, item_condition, customer_type=customer_type, request_options=request_options
            ),
        )

    async def get_item_offers_batch(
        self,
        body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetItemOffersBatchResponse:
        """Returns offer information for up to 20 Walmart Item ID requests. Each response entry contains an HTTP status
        for its corresponding item request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the results for the requested Walmart items.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(await self._with_raw_response.get_item_offers_batch(body, request_options=request_options))

    async def get_listing_offers(
        self,
        seller_sku: str,
        item_condition: ConditionTypeProductPricingOrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOffersResponse:
        """Returns the lowest-priced offers for a single SKU listing, based on SKU and item condition.

        Args:
            seller_sku: Seller SKU that identifies the item in the specified marketplace. The ``SellerSKU`` value is
                qualified by the seller's ``SellerId``.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the lowest-priced offers for the requested seller SKU.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_listing_offers(
                seller_sku, item_condition, customer_type=customer_type, request_options=request_options
            ),
        )

    async def get_listing_offers_batch(
        self,
        body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetListingOffersBatchResponse:
        """Returns offer information for up to 20 seller SKU requests. Each response entry contains an HTTP status for
        its corresponding seller SKU request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the results for the requested seller SKUs.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(await self._with_raw_response.get_listing_offers_batch(body, request_options=request_options))

    async def get_pricing(
        self,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        item_condition: ConditionTypeProductPricingOrStr | None = None,
        offer_type: OfferCustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetPricingResponse:
        """Returns pricing information for the seller's listings, identified by seller SKU or Walmart Item ID.

        Args:
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested
                items.
            skus: Seller SKUs that identify the items to return. Supports up to 20 values.
            walmart_item_ids: Walmart Item IDs that identify the items to return. Supports up to 20 values.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            offer_type: Filters pricing information by business-to-consumer (``B2C``) or business-to-business (``B2B``)
                offer type. Default is ``B2C``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns pricing information for the requested seller items.

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``list[ErrorCatalogItems] | RawError``."""
        return unwrap(
            await self._with_raw_response.get_pricing(
                item_type=item_type,
                skus=skus,
                walmart_item_ids=walmart_item_ids,
                item_condition=item_condition,
                offer_type=offer_type,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncProductPricingWithRawResponse:
        return self._with_raw_response


class ProductPricingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_buybox_offer_expected_price_batch(
        self,
        body: GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetBuyboxOfferExpectedPriceBatchResponse, GetBuyboxOfferExpectedPriceBatchErrorBody]:
        """**Planned — not yet available in production.** Returns the Buybox Offer Expected Price (BOEP) for a batch of
        seller SKUs.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/pricing/product-batches/offer/buybox-offer-expected-price"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetBuyboxOfferExpectedPriceBatchResponse],
            error_mapper=get_buybox_offer_expected_price_batch_error_mapper,
            request_options=request_options,
        )

    def get_competitive_pricing(
        self,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPricingResponse, GetCompetitivePricingErrorBody]:
        """Returns competitive pricing information for seller offer listings identified by seller SKU or Walmart Item
        ID.

        Args:
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested
                items.
            skus: Seller SKUs that identify the items to return. Supports up to 20 values.
            walmart_item_ids: Walmart Item IDs that identify the items to return. Supports up to 20 values.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/pricing/products/competitive-price"),
            query_params=[
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
        """**Planned — not yet available in production.** Returns competitive summary information, including featured
        buying options and lowest-priced offers, for a batch of Walmart Item IDs.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/pricing/product-batches/items/competitive-summary"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CompetitiveSummaryBatchResponse],
            error_mapper=get_competitive_summary_error_mapper,
            request_options=request_options,
        )

    def get_item_offers(
        self,
        item_id: str,
        item_condition: ConditionTypeProductPricingOrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOffersResponse, GetItemOffersErrorBody]:
        """Returns the lowest-priced offers for a Walmart item with the specified item condition.

        Args:
            item_id: Walmart Item ID that identifies the item.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/pricing/products/items/{item-id}/offers"),
            path_params=[param[str]("item-id", item_id)],
            query_params=[
                param[ConditionTypeProductPricingOrStr]("ItemCondition", item_condition),
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
        """Returns offer information for up to 20 Walmart Item ID requests. Each response entry contains an HTTP status
        for its corresponding item request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/pricing/product-batches/item-offers"),
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
        item_condition: ConditionTypeProductPricingOrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOffersResponse, GetListingOffersErrorBody]:
        """Returns the lowest-priced offers for a single SKU listing, based on SKU and item condition.

        Args:
            seller_sku: Seller SKU that identifies the item in the specified marketplace. The ``SellerSKU`` value is
                qualified by the seller's ``SellerId``.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/pricing/products/listings/{seller-sku}/offers"),
            path_params=[param[str]("seller-sku", seller_sku)],
            query_params=[
                param[ConditionTypeProductPricingOrStr]("ItemCondition", item_condition),
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
        """Returns offer information for up to 20 seller SKU requests. Each response entry contains an HTTP status for
        its corresponding seller SKU request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/pricing/product-batches/listing-offers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetListingOffersBatchRequest | GetListingOffersBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetListingOffersBatchResponse],
            error_mapper=get_listing_offers_batch_error_mapper,
            request_options=request_options,
        )

    def get_pricing(
        self,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        item_condition: ConditionTypeProductPricingOrStr | None = None,
        offer_type: OfferCustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPricingResponse, GetPricingErrorBody]:
        """Returns pricing information for the seller's listings, identified by seller SKU or Walmart Item ID.

        Args:
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested
                items.
            skus: Seller SKUs that identify the items to return. Supports up to 20 values.
            walmart_item_ids: Walmart Item IDs that identify the items to return. Supports up to 20 values.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            offer_type: Filters pricing information by business-to-consumer (``B2C``) or business-to-business (``B2B``)
                offer type. Default is ``B2C``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/pricing/products/price"),
            query_params=[
                param[ItemTypeOrStr]("ItemType", item_type),
                param[list[str] | None]("Skus", skus),
                param[list[str] | None]("walmartItemIds", walmart_item_ids),
                param[ConditionTypeProductPricingOrStr | None]("ItemCondition", item_condition),
                param[OfferCustomerTypeOrStr | None]("OfferType", offer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetPricingResponse],
            error_mapper=get_pricing_error_mapper,
            request_options=request_options,
        )


class AsyncProductPricingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_buybox_offer_expected_price_batch(
        self,
        body: GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetBuyboxOfferExpectedPriceBatchResponse, GetBuyboxOfferExpectedPriceBatchErrorBody]:
        """**Planned — not yet available in production.** Returns the Buybox Offer Expected Price (BOEP) for a batch of
        seller SKUs.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items(
                "/v4/pricing/product-batches/offer/buybox-offer-expected-price"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetBuyboxOfferExpectedPriceBatchResponse],
            error_mapper=get_buybox_offer_expected_price_batch_error_mapper,
            request_options=request_options,
        )

    async def get_competitive_pricing(
        self,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPricingResponse, GetCompetitivePricingErrorBody]:
        """Returns competitive pricing information for seller offer listings identified by seller SKU or Walmart Item
        ID.

        Args:
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested
                items.
            skus: Seller SKUs that identify the items to return. Supports up to 20 values.
            walmart_item_ids: Walmart Item IDs that identify the items to return. Supports up to 20 values.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/pricing/products/competitive-price"),
            query_params=[
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
        """**Planned — not yet available in production.** Returns competitive summary information, including featured
        buying options and lowest-priced offers, for a batch of Walmart Item IDs.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/pricing/product-batches/items/competitive-summary"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CompetitiveSummaryBatchResponse],
            error_mapper=get_competitive_summary_error_mapper,
            request_options=request_options,
        )

    async def get_item_offers(
        self,
        item_id: str,
        item_condition: ConditionTypeProductPricingOrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOffersResponse, GetItemOffersErrorBody]:
        """Returns the lowest-priced offers for a Walmart item with the specified item condition.

        Args:
            item_id: Walmart Item ID that identifies the item.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/pricing/products/items/{item-id}/offers"),
            path_params=[param[str]("item-id", item_id)],
            query_params=[
                param[ConditionTypeProductPricingOrStr]("ItemCondition", item_condition),
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
        """Returns offer information for up to 20 Walmart Item ID requests. Each response entry contains an HTTP status
        for its corresponding item request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/pricing/product-batches/item-offers"),
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
        item_condition: ConditionTypeProductPricingOrStr,
        *,
        customer_type: CustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOffersResponse, GetListingOffersErrorBody]:
        """Returns the lowest-priced offers for a single SKU listing, based on SKU and item condition.

        Args:
            seller_sku: Seller SKU that identifies the item in the specified marketplace. The ``SellerSKU`` value is
                qualified by the seller's ``SellerId``.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            customer_type: Indicates whether to request ``Consumer`` or ``Business`` offers. The default is
                ``Consumer``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/pricing/products/listings/{seller-sku}/offers"),
            path_params=[param[str]("seller-sku", seller_sku)],
            query_params=[
                param[ConditionTypeProductPricingOrStr]("ItemCondition", item_condition),
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
        """Returns offer information for up to 20 seller SKU requests. Each response entry contains an HTTP status for
        its corresponding seller SKU request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/pricing/product-batches/listing-offers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetListingOffersBatchRequest | GetListingOffersBatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetListingOffersBatchResponse],
            error_mapper=get_listing_offers_batch_error_mapper,
            request_options=request_options,
        )

    async def get_pricing(
        self,
        *,
        item_type: ItemTypeOrStr = ItemType.SKU,
        skus: list[str] | None = None,
        walmart_item_ids: list[str] | None = None,
        item_condition: ConditionTypeProductPricingOrStr | None = None,
        offer_type: OfferCustomerTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetPricingResponse, GetPricingErrorBody]:
        """Returns pricing information for the seller's listings, identified by seller SKU or Walmart Item ID.

        Args:
            item_type: Indicates whether Walmart Item ID values or seller SKU values are used to identify the requested
                items.
            skus: Seller SKUs that identify the items to return. Supports up to 20 values.
            walmart_item_ids: Walmart Item IDs that identify the items to return. Supports up to 20 values.
            item_condition: Filters the offer listings based on item condition. Possible values are ``New``,
                ``Restored``, and ``Pre-Owned``.
            offer_type: Filters pricing information by business-to-consumer (``B2C``) or business-to-business (``B2B``)
                offer type. Default is ``B2C``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/pricing/products/price"),
            query_params=[
                param[ItemTypeOrStr]("ItemType", item_type),
                param[list[str] | None]("Skus", skus),
                param[list[str] | None]("walmartItemIds", walmart_item_ids),
                param[ConditionTypeProductPricingOrStr | None]("ItemCondition", item_condition),
                param[OfferCustomerTypeOrStr | None]("OfferType", offer_type),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetPricingResponse],
            error_mapper=get_pricing_error_mapper,
            request_options=request_options,
        )
