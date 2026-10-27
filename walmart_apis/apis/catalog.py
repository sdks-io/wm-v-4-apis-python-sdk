from __future__ import annotations

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
from ..errors.get_catalog_item_error import GetCatalogItemErrorBody, get_catalog_item_error_mapper
from ..errors.search_catalog_items_error import SearchCatalogItemsErrorBody, search_catalog_items_error_mapper
from ..models.enums.included_datum import IncludedDatumOrStr
from ..models.item import Item
from ..models.item_search_results import ItemSearchResults
from ..server.server import Server


class Catalog:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CatalogWithRawResponse(client, server, auth)

    def get_catalog_item(
        self,
        walmart_item_id: str,
        marketplace_ids: list[str],
        *,
        included_data: list[IncludedDatumOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Item:
        """Send a ``GET`` request.

        Args:
            walmart_item_id: Walmart Item ID (14-digit numeric identifier)
            marketplace_ids: Walmart marketplace identifiers. Use WALMART_US for the US marketplace.
            included_data: Data sections to include in the response
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden — insufficient permissions Resource not found Rate limit exceeded Internal
                Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.get_catalog_item(
                walmart_item_id, marketplace_ids, included_data=included_data, request_options=request_options
            ),
        )

    def search_catalog_items(
        self,
        marketplace_ids: list[str],
        *,
        keywords: str | None = None,
        walmart_item_ids: str | None = None,
        seller_sku: str | None = None,
        gtin: str | None = None,
        upc: str | None = None,
        included_data: list[IncludedDatumOrStr] | None = None,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemSearchResults:
        """Search the Walmart Marketplace catalog using keywords, WalmartItemId, GTIN, UPC, or seller SKU. Returns
        matching catalog items.

        Args:
            marketplace_ids: Walmart marketplace identifiers. Use WALMART_US for the US marketplace.
            keywords: Keyword search terms
            walmart_item_ids: Comma-separated Walmart Item IDs (14-digit). Max 20.
            seller_sku: Seller-defined SKU
            gtin: Global Trade Item Number (14-digit)
            upc: Universal Product Code (12-digit)
            included_data: Data sections to include in the response
            page_size: Number of results per page (1–20). **Known limitation:** The PIQS keyword search backend
                hard-caps results at 40 items per call regardless of this value.
            page_token: Token for the next page of results, obtained from ``pagination.nextToken`` in a previous
                response. **Known limitation:** Cursor-based pagination is not currently supported for keyword search.
                The PIQS search backend (``/v3/items/walmart/search``) does not return a ``nextCursor`` and does not
                honour this parameter. Results are capped at 40 items per call. Reserved for future use once PIQS
                exposes pagination support.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden — insufficient permissions Resource not found Rate limit exceeded Internal
                Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.search_catalog_items(
                marketplace_ids,
                keywords=keywords,
                walmart_item_ids=walmart_item_ids,
                seller_sku=seller_sku,
                gtin=gtin,
                upc=upc,
                included_data=included_data,
                page_size=page_size,
                page_token=page_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> CatalogWithRawResponse:
        return self._with_raw_response


class AsyncCatalog:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCatalogWithRawResponse(client, server, auth)

    async def get_catalog_item(
        self,
        walmart_item_id: str,
        marketplace_ids: list[str],
        *,
        included_data: list[IncludedDatumOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Item:
        """Send a ``GET`` request.

        Args:
            walmart_item_id: Walmart Item ID (14-digit numeric identifier)
            marketplace_ids: Walmart marketplace identifiers. Use WALMART_US for the US marketplace.
            included_data: Data sections to include in the response
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden — insufficient permissions Resource not found Rate limit exceeded Internal
                Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.get_catalog_item(
                walmart_item_id, marketplace_ids, included_data=included_data, request_options=request_options
            ),
        )

    async def search_catalog_items(
        self,
        marketplace_ids: list[str],
        *,
        keywords: str | None = None,
        walmart_item_ids: str | None = None,
        seller_sku: str | None = None,
        gtin: str | None = None,
        upc: str | None = None,
        included_data: list[IncludedDatumOrStr] | None = None,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemSearchResults:
        """Search the Walmart Marketplace catalog using keywords, WalmartItemId, GTIN, UPC, or seller SKU. Returns
        matching catalog items.

        Args:
            marketplace_ids: Walmart marketplace identifiers. Use WALMART_US for the US marketplace.
            keywords: Keyword search terms
            walmart_item_ids: Comma-separated Walmart Item IDs (14-digit). Max 20.
            seller_sku: Seller-defined SKU
            gtin: Global Trade Item Number (14-digit)
            upc: Universal Product Code (12-digit)
            included_data: Data sections to include in the response
            page_size: Number of results per page (1–20). **Known limitation:** The PIQS keyword search backend
                hard-caps results at 40 items per call regardless of this value.
            page_token: Token for the next page of results, obtained from ``pagination.nextToken`` in a previous
                response. **Known limitation:** Cursor-based pagination is not currently supported for keyword search.
                The PIQS search backend (``/v3/items/walmart/search``) does not return a ``nextCursor`` and does not
                honour this parameter. Results are capped at 40 items per call. Reserved for future use once PIQS
                exposes pagination support.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden — insufficient permissions Resource not found Rate limit exceeded Internal
                Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.search_catalog_items(
                marketplace_ids,
                keywords=keywords,
                walmart_item_ids=walmart_item_ids,
                seller_sku=seller_sku,
                gtin=gtin,
                upc=upc,
                included_data=included_data,
                page_size=page_size,
                page_token=page_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncCatalogWithRawResponse:
        return self._with_raw_response


class CatalogWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_catalog_item(
        self,
        walmart_item_id: str,
        marketplace_ids: list[str],
        *,
        included_data: list[IncludedDatumOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Item, GetCatalogItemErrorBody]:
        """Send a ``GET`` request.

        Args:
            walmart_item_id: Walmart Item ID (14-digit numeric identifier)
            marketplace_ids: Walmart marketplace identifiers. Use WALMART_US for the US marketplace.
            included_data: Data sections to include in the response
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/catalog/v4/items/{walmartItemId}"),
            path_params=[param[str]("walmartItemId", walmart_item_id)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[list[IncludedDatumOrStr] | None]("includedData", included_data),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Item],
            error_mapper=get_catalog_item_error_mapper,
            request_options=request_options,
        )

    def search_catalog_items(
        self,
        marketplace_ids: list[str],
        *,
        keywords: str | None = None,
        walmart_item_ids: str | None = None,
        seller_sku: str | None = None,
        gtin: str | None = None,
        upc: str | None = None,
        included_data: list[IncludedDatumOrStr] | None = None,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemSearchResults, SearchCatalogItemsErrorBody]:
        """Search the Walmart Marketplace catalog using keywords, WalmartItemId, GTIN, UPC, or seller SKU. Returns
        matching catalog items.

        Args:
            marketplace_ids: Walmart marketplace identifiers. Use WALMART_US for the US marketplace.
            keywords: Keyword search terms
            walmart_item_ids: Comma-separated Walmart Item IDs (14-digit). Max 20.
            seller_sku: Seller-defined SKU
            gtin: Global Trade Item Number (14-digit)
            upc: Universal Product Code (12-digit)
            included_data: Data sections to include in the response
            page_size: Number of results per page (1–20). **Known limitation:** The PIQS keyword search backend
                hard-caps results at 40 items per call regardless of this value.
            page_token: Token for the next page of results, obtained from ``pagination.nextToken`` in a previous
                response. **Known limitation:** Cursor-based pagination is not currently supported for keyword search.
                The PIQS search backend (``/v3/items/walmart/search``) does not return a ``nextCursor`` and does not
                honour this parameter. Results are capped at 40 items per call. Reserved for future use once PIQS
                exposes pagination support.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/catalog/v4/items"),
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str | None]("keywords", keywords),
                param[str | None]("walmartItemIds", walmart_item_ids),
                param[str | None]("sellerSku", seller_sku),
                param[str | None]("gtin", gtin),
                param[str | None]("upc", upc),
                param[list[IncludedDatumOrStr] | None]("includedData", included_data),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ItemSearchResults],
            error_mapper=search_catalog_items_error_mapper,
            request_options=request_options,
        )


class AsyncCatalogWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_catalog_item(
        self,
        walmart_item_id: str,
        marketplace_ids: list[str],
        *,
        included_data: list[IncludedDatumOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Item, GetCatalogItemErrorBody]:
        """Send a ``GET`` request.

        Args:
            walmart_item_id: Walmart Item ID (14-digit numeric identifier)
            marketplace_ids: Walmart marketplace identifiers. Use WALMART_US for the US marketplace.
            included_data: Data sections to include in the response
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/catalog/v4/items/{walmartItemId}"),
            path_params=[param[str]("walmartItemId", walmart_item_id)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[list[IncludedDatumOrStr] | None]("includedData", included_data),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Item],
            error_mapper=get_catalog_item_error_mapper,
            request_options=request_options,
        )

    async def search_catalog_items(
        self,
        marketplace_ids: list[str],
        *,
        keywords: str | None = None,
        walmart_item_ids: str | None = None,
        seller_sku: str | None = None,
        gtin: str | None = None,
        upc: str | None = None,
        included_data: list[IncludedDatumOrStr] | None = None,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemSearchResults, SearchCatalogItemsErrorBody]:
        """Search the Walmart Marketplace catalog using keywords, WalmartItemId, GTIN, UPC, or seller SKU. Returns
        matching catalog items.

        Args:
            marketplace_ids: Walmart marketplace identifiers. Use WALMART_US for the US marketplace.
            keywords: Keyword search terms
            walmart_item_ids: Comma-separated Walmart Item IDs (14-digit). Max 20.
            seller_sku: Seller-defined SKU
            gtin: Global Trade Item Number (14-digit)
            upc: Universal Product Code (12-digit)
            included_data: Data sections to include in the response
            page_size: Number of results per page (1–20). **Known limitation:** The PIQS keyword search backend
                hard-caps results at 40 items per call regardless of this value.
            page_token: Token for the next page of results, obtained from ``pagination.nextToken`` in a previous
                response. **Known limitation:** Cursor-based pagination is not currently supported for keyword search.
                The PIQS search backend (``/v3/items/walmart/search``) does not return a ``nextCursor`` and does not
                honour this parameter. Results are capped at 40 items per call. Reserved for future use once PIQS
                exposes pagination support.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/catalog/v4/items"),
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str | None]("keywords", keywords),
                param[str | None]("walmartItemIds", walmart_item_ids),
                param[str | None]("sellerSku", seller_sku),
                param[str | None]("gtin", gtin),
                param[str | None]("upc", upc),
                param[list[IncludedDatumOrStr] | None]("includedData", included_data),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ItemSearchResults],
            error_mapper=search_catalog_items_error_mapper,
            request_options=request_options,
        )
