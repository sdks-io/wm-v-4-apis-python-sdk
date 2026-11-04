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
from ..errors.delete_listings_item_error import DeleteListingsItemErrorBody, delete_listings_item_error_mapper
from ..errors.get_listings_item_error import GetListingsItemErrorBody, get_listings_item_error_mapper
from ..errors.patch_listings_item_error import PatchListingsItemErrorBody, patch_listings_item_error_mapper
from ..errors.put_listings_item_error import PutListingsItemErrorBody, put_listings_item_error_mapper
from ..errors.search_listings_items_error import SearchListingsItemsErrorBody, search_listings_items_error_mapper
from ..models.enums.identifier_type_listings_items import IdentifierTypeListingsItemsOrStr
from ..models.enums.included_datum_listings_items import IncludedDatumListingsItemsOrStr
from ..models.enums.sort_by import SortByOrStr
from ..models.enums.sort_order import SortOrder, SortOrderOrStr
from ..models.item_listings_items import ItemListingsItems
from ..models.item_search_results_listings_items import ItemSearchResultsListingsItems
from ..models.listings_item_patch_request import ListingsItemPatchRequest, ListingsItemPatchRequestDict
from ..models.listings_item_put_request import ListingsItemPutRequest, ListingsItemPutRequestDict
from ..models.listings_item_submission_response import ListingsItemSubmissionResponse
from ..server.server import Server


class ListingsItems:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ListingsItemsWithRawResponse(client, server, auth)

    def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListingsItemSubmissionResponse:
        """Send a ``DELETE`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successfully submitted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.delete_listings_item(
                seller_id, sku, marketplace_ids, issue_locale=issue_locale, request_options=request_options
            ),
        )

    def get_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        *,
        issue_locale: str | None = "en_US",
        included_data: list[IncludedDatumListingsItemsOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemListingsItems:
        """Send a ``GET`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            issue_locale: Locale for issue messages (e.g. en_US)
            included_data: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_listings_item(
                seller_id,
                sku,
                marketplace_ids,
                issue_locale=issue_locale,
                included_data=included_data,
                request_options=request_options,
            ),
        )

    def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        body: ListingsItemPatchRequest | ListingsItemPatchRequestDict,
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListingsItemSubmissionResponse:
        """Send a ``PATCH`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            body: The request body.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successfully submitted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.patch_listings_item(
                seller_id, sku, marketplace_ids, body, issue_locale=issue_locale, request_options=request_options
            ),
        )

    def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        body: ListingsItemPutRequest | ListingsItemPutRequestDict,
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListingsItemSubmissionResponse:
        """Send a ``PUT`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            body: The request body.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successfully submitted

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.put_listings_item(
                seller_id, sku, marketplace_ids, body, issue_locale=issue_locale, request_options=request_options
            ),
        )

    def search_listings_items(
        self,
        seller_id: str,
        marketplace_ids: list[str],
        *,
        included_data: list[IncludedDatumListingsItemsOrStr] | None = None,
        identifier_type: IdentifierTypeListingsItemsOrStr | None = None,
        identifier_value: str | None = None,
        lifecycle_status: list[str] | None = None,
        published_status: list[str] | None = None,
        unpublished_reasons: list[str] | None = None,
        inventory_status: list[str] | None = None,
        fulfillment_type: list[str] | None = None,
        min_customer_rating: float | None = None,
        max_customer_rating: float | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort_by: SortByOrStr | None = None,
        sort_order: SortOrderOrStr | None = SortOrder.ASC,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemSearchResultsListingsItems:
        """Returns a paginated list of the seller's listings items. Mirrors Amazon SP-API ``searchListingsItems`` so an
        existing SP-API client can call the seller-level collection endpoint (no SKU in the path) against v4.

        Filtering and sorting are pushed down to PIQS (Partner Item Query Service) ``POST /v3/items/catalog/search`` —
        the server does the filtering; callers no longer need to page through the full seller catalog and filter
        client-side.

        Args:
            seller_id: Seller identifier
            marketplace_ids: Value sent with the request.
            included_data: Value sent with the request.
            identifier_type: Identifier field to search by (PIQS ``query.field``). Requires ``identifierValue``. PIQS
                accepts a single field/value pair per call — not a list.
            identifier_value: Value to match for ``identifierType``. Ignored if ``identifierType`` is absent.
            lifecycle_status: Filter to items with any of these lifecycle statuses (PIQS
                ``filters[].field=lifecycleStatus``, op ``equals``).
            published_status: Filter to items with any of these publication statuses (e.g. PUBLISHED, UNPUBLISHED,
                SYSTEM_PROBLEM).
            unpublished_reasons: Filter to items carrying any of these unpublished reasons.
            inventory_status: Filter to items with any of these inventory statuses.
            fulfillment_type: Filter to items with any of these fulfillment types.
            min_customer_rating: Minimum customer rating, inclusive (PIQS ``filters[].field=customerRating``, op
                ``between``/``greater_than``).
            max_customer_rating: Maximum customer rating, inclusive.
            min_price: Minimum price, inclusive (PIQS ``filters[].field=price``, op ``between``/``greater_than``).
            max_price: Maximum price, inclusive.
            sort_by: Field to sort results by (PIQS ``sort.field``).
            sort_order: Sort direction. Ignored if ``sortBy`` is absent.
            page_size: Maximum number of results per page
            page_token: Opaque cursor returned by a previous call for the next page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.search_listings_items(
                seller_id,
                marketplace_ids,
                included_data=included_data,
                identifier_type=identifier_type,
                identifier_value=identifier_value,
                lifecycle_status=lifecycle_status,
                published_status=published_status,
                unpublished_reasons=unpublished_reasons,
                inventory_status=inventory_status,
                fulfillment_type=fulfillment_type,
                min_customer_rating=min_customer_rating,
                max_customer_rating=max_customer_rating,
                min_price=min_price,
                max_price=max_price,
                sort_by=sort_by,
                sort_order=sort_order,
                page_size=page_size,
                page_token=page_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ListingsItemsWithRawResponse:
        return self._with_raw_response


class AsyncListingsItems:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncListingsItemsWithRawResponse(client, server, auth)

    async def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListingsItemSubmissionResponse:
        """Send a ``DELETE`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successfully submitted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_listings_item(
                seller_id, sku, marketplace_ids, issue_locale=issue_locale, request_options=request_options
            ),
        )

    async def get_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        *,
        issue_locale: str | None = "en_US",
        included_data: list[IncludedDatumListingsItemsOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemListingsItems:
        """Send a ``GET`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            issue_locale: Locale for issue messages (e.g. en_US)
            included_data: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_listings_item(
                seller_id,
                sku,
                marketplace_ids,
                issue_locale=issue_locale,
                included_data=included_data,
                request_options=request_options,
            ),
        )

    async def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        body: ListingsItemPatchRequest | ListingsItemPatchRequestDict,
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListingsItemSubmissionResponse:
        """Send a ``PATCH`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            body: The request body.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successfully submitted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_listings_item(
                seller_id, sku, marketplace_ids, body, issue_locale=issue_locale, request_options=request_options
            ),
        )

    async def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        body: ListingsItemPutRequest | ListingsItemPutRequestDict,
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListingsItemSubmissionResponse:
        """Send a ``PUT`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            body: The request body.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successfully submitted

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.put_listings_item(
                seller_id, sku, marketplace_ids, body, issue_locale=issue_locale, request_options=request_options
            ),
        )

    async def search_listings_items(
        self,
        seller_id: str,
        marketplace_ids: list[str],
        *,
        included_data: list[IncludedDatumListingsItemsOrStr] | None = None,
        identifier_type: IdentifierTypeListingsItemsOrStr | None = None,
        identifier_value: str | None = None,
        lifecycle_status: list[str] | None = None,
        published_status: list[str] | None = None,
        unpublished_reasons: list[str] | None = None,
        inventory_status: list[str] | None = None,
        fulfillment_type: list[str] | None = None,
        min_customer_rating: float | None = None,
        max_customer_rating: float | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort_by: SortByOrStr | None = None,
        sort_order: SortOrderOrStr | None = SortOrder.ASC,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemSearchResultsListingsItems:
        """Returns a paginated list of the seller's listings items. Mirrors Amazon SP-API ``searchListingsItems`` so an
        existing SP-API client can call the seller-level collection endpoint (no SKU in the path) against v4.

        Filtering and sorting are pushed down to PIQS (Partner Item Query Service) ``POST /v3/items/catalog/search`` —
        the server does the filtering; callers no longer need to page through the full seller catalog and filter
        client-side.

        Args:
            seller_id: Seller identifier
            marketplace_ids: Value sent with the request.
            included_data: Value sent with the request.
            identifier_type: Identifier field to search by (PIQS ``query.field``). Requires ``identifierValue``. PIQS
                accepts a single field/value pair per call — not a list.
            identifier_value: Value to match for ``identifierType``. Ignored if ``identifierType`` is absent.
            lifecycle_status: Filter to items with any of these lifecycle statuses (PIQS
                ``filters[].field=lifecycleStatus``, op ``equals``).
            published_status: Filter to items with any of these publication statuses (e.g. PUBLISHED, UNPUBLISHED,
                SYSTEM_PROBLEM).
            unpublished_reasons: Filter to items carrying any of these unpublished reasons.
            inventory_status: Filter to items with any of these inventory statuses.
            fulfillment_type: Filter to items with any of these fulfillment types.
            min_customer_rating: Minimum customer rating, inclusive (PIQS ``filters[].field=customerRating``, op
                ``between``/``greater_than``).
            max_customer_rating: Maximum customer rating, inclusive.
            min_price: Minimum price, inclusive (PIQS ``filters[].field=price``, op ``between``/``greater_than``).
            max_price: Maximum price, inclusive.
            sort_by: Field to sort results by (PIQS ``sort.field``).
            sort_order: Sort direction. Ignored if ``sortBy`` is absent.
            page_size: Maximum number of results per page
            page_token: Opaque cursor returned by a previous call for the next page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.search_listings_items(
                seller_id,
                marketplace_ids,
                included_data=included_data,
                identifier_type=identifier_type,
                identifier_value=identifier_value,
                lifecycle_status=lifecycle_status,
                published_status=published_status,
                unpublished_reasons=unpublished_reasons,
                inventory_status=inventory_status,
                fulfillment_type=fulfillment_type,
                min_customer_rating=min_customer_rating,
                max_customer_rating=max_customer_rating,
                min_price=min_price,
                max_price=max_price,
                sort_by=sort_by,
                sort_order=sort_order,
                page_size=page_size,
                page_token=page_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncListingsItemsWithRawResponse:
        return self._with_raw_response


class ListingsItemsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListingsItemSubmissionResponse, DeleteListingsItemErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}/{sku}"),
            path_params=[param[str]("seller-id", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids), param[str | None]("issueLocale", issue_locale)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListingsItemSubmissionResponse],
            error_mapper=delete_listings_item_error_mapper,
            request_options=request_options,
        )

    def get_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        *,
        issue_locale: str | None = "en_US",
        included_data: list[IncludedDatumListingsItemsOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemListingsItems, GetListingsItemErrorBody]:
        """Send a ``GET`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            issue_locale: Locale for issue messages (e.g. en_US)
            included_data: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}/{sku}"),
            path_params=[param[str]("seller-id", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str | None]("issueLocale", issue_locale),
                param[list[IncludedDatumListingsItemsOrStr] | None]("includedData", included_data),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ItemListingsItems],
            error_mapper=get_listings_item_error_mapper,
            request_options=request_options,
        )

    def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        body: ListingsItemPatchRequest | ListingsItemPatchRequestDict,
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListingsItemSubmissionResponse, PatchListingsItemErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            body: The request body.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}/{sku}"),
            path_params=[param[str]("seller-id", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids), param[str | None]("issueLocale", issue_locale)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ListingsItemPatchRequest | ListingsItemPatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListingsItemSubmissionResponse],
            error_mapper=patch_listings_item_error_mapper,
            request_options=request_options,
        )

    def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        body: ListingsItemPutRequest | ListingsItemPutRequestDict,
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListingsItemSubmissionResponse, PutListingsItemErrorBody]:
        """Send a ``PUT`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            body: The request body.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}/{sku}"),
            path_params=[param[str]("seller-id", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids), param[str | None]("issueLocale", issue_locale)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ListingsItemPutRequest | ListingsItemPutRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ListingsItemSubmissionResponse],
            error_mapper=put_listings_item_error_mapper,
            request_options=request_options,
        )

    def search_listings_items(
        self,
        seller_id: str,
        marketplace_ids: list[str],
        *,
        included_data: list[IncludedDatumListingsItemsOrStr] | None = None,
        identifier_type: IdentifierTypeListingsItemsOrStr | None = None,
        identifier_value: str | None = None,
        lifecycle_status: list[str] | None = None,
        published_status: list[str] | None = None,
        unpublished_reasons: list[str] | None = None,
        inventory_status: list[str] | None = None,
        fulfillment_type: list[str] | None = None,
        min_customer_rating: float | None = None,
        max_customer_rating: float | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort_by: SortByOrStr | None = None,
        sort_order: SortOrderOrStr | None = SortOrder.ASC,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemSearchResultsListingsItems, SearchListingsItemsErrorBody]:
        """Returns a paginated list of the seller's listings items. Mirrors Amazon SP-API ``searchListingsItems`` so an
        existing SP-API client can call the seller-level collection endpoint (no SKU in the path) against v4.

        Filtering and sorting are pushed down to PIQS (Partner Item Query Service) ``POST /v3/items/catalog/search`` —
        the server does the filtering; callers no longer need to page through the full seller catalog and filter
        client-side.

        Args:
            seller_id: Seller identifier
            marketplace_ids: Value sent with the request.
            included_data: Value sent with the request.
            identifier_type: Identifier field to search by (PIQS ``query.field``). Requires ``identifierValue``. PIQS
                accepts a single field/value pair per call — not a list.
            identifier_value: Value to match for ``identifierType``. Ignored if ``identifierType`` is absent.
            lifecycle_status: Filter to items with any of these lifecycle statuses (PIQS
                ``filters[].field=lifecycleStatus``, op ``equals``).
            published_status: Filter to items with any of these publication statuses (e.g. PUBLISHED, UNPUBLISHED,
                SYSTEM_PROBLEM).
            unpublished_reasons: Filter to items carrying any of these unpublished reasons.
            inventory_status: Filter to items with any of these inventory statuses.
            fulfillment_type: Filter to items with any of these fulfillment types.
            min_customer_rating: Minimum customer rating, inclusive (PIQS ``filters[].field=customerRating``, op
                ``between``/``greater_than``).
            max_customer_rating: Maximum customer rating, inclusive.
            min_price: Minimum price, inclusive (PIQS ``filters[].field=price``, op ``between``/``greater_than``).
            max_price: Maximum price, inclusive.
            sort_by: Field to sort results by (PIQS ``sort.field``).
            sort_order: Sort direction. Ignored if ``sortBy`` is absent.
            page_size: Maximum number of results per page
            page_token: Opaque cursor returned by a previous call for the next page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}"),
            path_params=[param[str]("seller-id", seller_id)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[list[IncludedDatumListingsItemsOrStr] | None]("includedData", included_data),
                param[IdentifierTypeListingsItemsOrStr | None]("identifierType", identifier_type),
                param[str | None]("identifierValue", identifier_value),
                param[list[str] | None]("lifecycleStatus", lifecycle_status),
                param[list[str] | None]("publishedStatus", published_status),
                param[list[str] | None]("unpublishedReasons", unpublished_reasons),
                param[list[str] | None]("inventoryStatus", inventory_status),
                param[list[str] | None]("fulfillmentType", fulfillment_type),
                param[float | None]("minCustomerRating", min_customer_rating),
                param[float | None]("maxCustomerRating", max_customer_rating),
                param[float | None]("minPrice", min_price),
                param[float | None]("maxPrice", max_price),
                param[SortByOrStr | None]("sortBy", sort_by),
                param[SortOrderOrStr | None]("sortOrder", sort_order),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ItemSearchResultsListingsItems],
            error_mapper=search_listings_items_error_mapper,
            request_options=request_options,
        )


class AsyncListingsItemsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListingsItemSubmissionResponse, DeleteListingsItemErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}/{sku}"),
            path_params=[param[str]("seller-id", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids), param[str | None]("issueLocale", issue_locale)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListingsItemSubmissionResponse],
            error_mapper=delete_listings_item_error_mapper,
            request_options=request_options,
        )

    async def get_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        *,
        issue_locale: str | None = "en_US",
        included_data: list[IncludedDatumListingsItemsOrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemListingsItems, GetListingsItemErrorBody]:
        """Send a ``GET`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            issue_locale: Locale for issue messages (e.g. en_US)
            included_data: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}/{sku}"),
            path_params=[param[str]("seller-id", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str | None]("issueLocale", issue_locale),
                param[list[IncludedDatumListingsItemsOrStr] | None]("includedData", included_data),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ItemListingsItems],
            error_mapper=get_listings_item_error_mapper,
            request_options=request_options,
        )

    async def patch_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        body: ListingsItemPatchRequest | ListingsItemPatchRequestDict,
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListingsItemSubmissionResponse, PatchListingsItemErrorBody]:
        """Send a ``PATCH`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            body: The request body.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}/{sku}"),
            path_params=[param[str]("seller-id", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids), param[str | None]("issueLocale", issue_locale)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ListingsItemPatchRequest | ListingsItemPatchRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListingsItemSubmissionResponse],
            error_mapper=patch_listings_item_error_mapper,
            request_options=request_options,
        )

    async def put_listings_item(
        self,
        seller_id: str,
        sku: str,
        marketplace_ids: list[str],
        body: ListingsItemPutRequest | ListingsItemPutRequestDict,
        *,
        issue_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListingsItemSubmissionResponse, PutListingsItemErrorBody]:
        """Send a ``PUT`` request.

        Args:
            seller_id: Seller identifier
            sku: Seller SKU identifying the listing
            marketplace_ids: Value sent with the request.
            body: The request body.
            issue_locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}/{sku}"),
            path_params=[param[str]("seller-id", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids), param[str | None]("issueLocale", issue_locale)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ListingsItemPutRequest | ListingsItemPutRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ListingsItemSubmissionResponse],
            error_mapper=put_listings_item_error_mapper,
            request_options=request_options,
        )

    async def search_listings_items(
        self,
        seller_id: str,
        marketplace_ids: list[str],
        *,
        included_data: list[IncludedDatumListingsItemsOrStr] | None = None,
        identifier_type: IdentifierTypeListingsItemsOrStr | None = None,
        identifier_value: str | None = None,
        lifecycle_status: list[str] | None = None,
        published_status: list[str] | None = None,
        unpublished_reasons: list[str] | None = None,
        inventory_status: list[str] | None = None,
        fulfillment_type: list[str] | None = None,
        min_customer_rating: float | None = None,
        max_customer_rating: float | None = None,
        min_price: float | None = None,
        max_price: float | None = None,
        sort_by: SortByOrStr | None = None,
        sort_order: SortOrderOrStr | None = SortOrder.ASC,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemSearchResultsListingsItems, SearchListingsItemsErrorBody]:
        """Returns a paginated list of the seller's listings items. Mirrors Amazon SP-API ``searchListingsItems`` so an
        existing SP-API client can call the seller-level collection endpoint (no SKU in the path) against v4.

        Filtering and sorting are pushed down to PIQS (Partner Item Query Service) ``POST /v3/items/catalog/search`` —
        the server does the filtering; callers no longer need to page through the full seller catalog and filter
        client-side.

        Args:
            seller_id: Seller identifier
            marketplace_ids: Value sent with the request.
            included_data: Value sent with the request.
            identifier_type: Identifier field to search by (PIQS ``query.field``). Requires ``identifierValue``. PIQS
                accepts a single field/value pair per call — not a list.
            identifier_value: Value to match for ``identifierType``. Ignored if ``identifierType`` is absent.
            lifecycle_status: Filter to items with any of these lifecycle statuses (PIQS
                ``filters[].field=lifecycleStatus``, op ``equals``).
            published_status: Filter to items with any of these publication statuses (e.g. PUBLISHED, UNPUBLISHED,
                SYSTEM_PROBLEM).
            unpublished_reasons: Filter to items carrying any of these unpublished reasons.
            inventory_status: Filter to items with any of these inventory statuses.
            fulfillment_type: Filter to items with any of these fulfillment types.
            min_customer_rating: Minimum customer rating, inclusive (PIQS ``filters[].field=customerRating``, op
                ``between``/``greater_than``).
            max_customer_rating: Maximum customer rating, inclusive.
            min_price: Minimum price, inclusive (PIQS ``filters[].field=price``, op ``between``/``greater_than``).
            max_price: Maximum price, inclusive.
            sort_by: Field to sort results by (PIQS ``sort.field``).
            sort_order: Sort direction. Ignored if ``sortBy`` is absent.
            page_size: Maximum number of results per page
            page_token: Opaque cursor returned by a previous call for the next page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/items/listings/{seller-id}"),
            path_params=[param[str]("seller-id", seller_id)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[list[IncludedDatumListingsItemsOrStr] | None]("includedData", included_data),
                param[IdentifierTypeListingsItemsOrStr | None]("identifierType", identifier_type),
                param[str | None]("identifierValue", identifier_value),
                param[list[str] | None]("lifecycleStatus", lifecycle_status),
                param[list[str] | None]("publishedStatus", published_status),
                param[list[str] | None]("unpublishedReasons", unpublished_reasons),
                param[list[str] | None]("inventoryStatus", inventory_status),
                param[list[str] | None]("fulfillmentType", fulfillment_type),
                param[float | None]("minCustomerRating", min_customer_rating),
                param[float | None]("maxCustomerRating", max_customer_rating),
                param[float | None]("minPrice", min_price),
                param[float | None]("maxPrice", max_price),
                param[SortByOrStr | None]("sortBy", sort_by),
                param[SortOrderOrStr | None]("sortOrder", sort_order),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ItemSearchResultsListingsItems],
            error_mapper=search_listings_items_error_mapper,
            request_options=request_options,
        )
