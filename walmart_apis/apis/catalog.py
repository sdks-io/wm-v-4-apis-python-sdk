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
        """Retrieves information about an item in the Walmart Marketplace catalog using its Walmart Item ID. Returns
        available product information for the specified marketplace. Use ``includedData`` to select specific data
        sections, such as attributes, identifiers, images, and product types.

        Args:
            walmart_item_id: Specifies the 14-digit Walmart Item ID of the catalog item to retrieve.
            marketplace_ids: Walmart Marketplace identifiers that scope the request. Use ``WALMART_US`` for the US
                marketplace.
            included_data: Product information sections to include in the response.
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
        """Searches the Walmart Marketplace catalog using keywords or item identifiers, including Walmart Item IDs,
        Global Trade Item Numbers (GTINs), Universal Product Codes (UPCs), and seller SKUs. Returns matching catalog
        items and requested product information for the specified marketplace.

        Args:
            marketplace_ids: Walmart Marketplace identifiers that scope the request. Use ``WALMART_US`` for the US
                marketplace.
            keywords: Keywords used to search for matching catalog items.
            walmart_item_ids: Comma-separated Walmart Item IDs to search for, with a maximum of 20 IDs.
            seller_sku: Seller-defined stock keeping unit (SKU) used to search for catalog items.
            gtin: Global Trade Item Number (GTIN) used to search for catalog items. Must contain 14 digits.
            upc: Universal Product Code (UPC) used to search for catalog items. Must contain 12 digits.
            included_data: Product information sections to include in the response.
            page_size: Maximum number of results requested per page (1–20). Defaults to 10.
            page_token: Token for requesting another page, when cursor-based pagination is supported.
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
        """Retrieves information about an item in the Walmart Marketplace catalog using its Walmart Item ID. Returns
        available product information for the specified marketplace. Use ``includedData`` to select specific data
        sections, such as attributes, identifiers, images, and product types.

        Args:
            walmart_item_id: Specifies the 14-digit Walmart Item ID of the catalog item to retrieve.
            marketplace_ids: Walmart Marketplace identifiers that scope the request. Use ``WALMART_US`` for the US
                marketplace.
            included_data: Product information sections to include in the response.
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
        """Searches the Walmart Marketplace catalog using keywords or item identifiers, including Walmart Item IDs,
        Global Trade Item Numbers (GTINs), Universal Product Codes (UPCs), and seller SKUs. Returns matching catalog
        items and requested product information for the specified marketplace.

        Args:
            marketplace_ids: Walmart Marketplace identifiers that scope the request. Use ``WALMART_US`` for the US
                marketplace.
            keywords: Keywords used to search for matching catalog items.
            walmart_item_ids: Comma-separated Walmart Item IDs to search for, with a maximum of 20 IDs.
            seller_sku: Seller-defined stock keeping unit (SKU) used to search for catalog items.
            gtin: Global Trade Item Number (GTIN) used to search for catalog items. Must contain 14 digits.
            upc: Universal Product Code (UPC) used to search for catalog items. Must contain 12 digits.
            included_data: Product information sections to include in the response.
            page_size: Maximum number of results requested per page (1–20). Defaults to 10.
            page_token: Token for requesting another page, when cursor-based pagination is supported.
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
        """Retrieves information about an item in the Walmart Marketplace catalog using its Walmart Item ID. Returns
        available product information for the specified marketplace. Use ``includedData`` to select specific data
        sections, such as attributes, identifiers, images, and product types.

        Args:
            walmart_item_id: Specifies the 14-digit Walmart Item ID of the catalog item to retrieve.
            marketplace_ids: Walmart Marketplace identifiers that scope the request. Use ``WALMART_US`` for the US
                marketplace.
            included_data: Product information sections to include in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/catalog/items/{walmart-item-id}"),
            path_params=[param[str]("walmart-item-id", walmart_item_id)],
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
        """Searches the Walmart Marketplace catalog using keywords or item identifiers, including Walmart Item IDs,
        Global Trade Item Numbers (GTINs), Universal Product Codes (UPCs), and seller SKUs. Returns matching catalog
        items and requested product information for the specified marketplace.

        Args:
            marketplace_ids: Walmart Marketplace identifiers that scope the request. Use ``WALMART_US`` for the US
                marketplace.
            keywords: Keywords used to search for matching catalog items.
            walmart_item_ids: Comma-separated Walmart Item IDs to search for, with a maximum of 20 IDs.
            seller_sku: Seller-defined stock keeping unit (SKU) used to search for catalog items.
            gtin: Global Trade Item Number (GTIN) used to search for catalog items. Must contain 14 digits.
            upc: Universal Product Code (UPC) used to search for catalog items. Must contain 12 digits.
            included_data: Product information sections to include in the response.
            page_size: Maximum number of results requested per page (1–20). Defaults to 10.
            page_token: Token for requesting another page, when cursor-based pagination is supported.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/catalog/items"),
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
        """Retrieves information about an item in the Walmart Marketplace catalog using its Walmart Item ID. Returns
        available product information for the specified marketplace. Use ``includedData`` to select specific data
        sections, such as attributes, identifiers, images, and product types.

        Args:
            walmart_item_id: Specifies the 14-digit Walmart Item ID of the catalog item to retrieve.
            marketplace_ids: Walmart Marketplace identifiers that scope the request. Use ``WALMART_US`` for the US
                marketplace.
            included_data: Product information sections to include in the response.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/catalog/items/{walmart-item-id}"),
            path_params=[param[str]("walmart-item-id", walmart_item_id)],
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
        """Searches the Walmart Marketplace catalog using keywords or item identifiers, including Walmart Item IDs,
        Global Trade Item Numbers (GTINs), Universal Product Codes (UPCs), and seller SKUs. Returns matching catalog
        items and requested product information for the specified marketplace.

        Args:
            marketplace_ids: Walmart Marketplace identifiers that scope the request. Use ``WALMART_US`` for the US
                marketplace.
            keywords: Keywords used to search for matching catalog items.
            walmart_item_ids: Comma-separated Walmart Item IDs to search for, with a maximum of 20 IDs.
            seller_sku: Seller-defined stock keeping unit (SKU) used to search for catalog items.
            gtin: Global Trade Item Number (GTIN) used to search for catalog items. Must contain 14 digits.
            upc: Universal Product Code (UPC) used to search for catalog items. Must contain 12 digits.
            included_data: Product information sections to include in the response.
            page_size: Maximum number of results requested per page (1–20). Defaults to 10.
            page_token: Token for requesting another page, when cursor-based pagination is supported.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/catalog/items"),
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
