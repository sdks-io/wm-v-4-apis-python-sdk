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
from ..models.enums.included_datum1 import IncludedDatum1OrStr
from ..models.item1 import Item1
from ..models.item_search_results1 import ItemSearchResults1
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
        included_data: list[IncludedDatum1OrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Item1:
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
        included_data: list[IncludedDatum1OrStr] | None = None,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemSearchResults1:
        """Returns a paginated list of the seller's listings items. Mirrors Amazon SP-API ``searchListingsItems`` so an
        existing SP-API client can call the seller-level collection endpoint (no SKU in the path) against v4.

        Args:
            seller_id: Seller identifier
            marketplace_ids: Value sent with the request.
            included_data: Value sent with the request.
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
        included_data: list[IncludedDatum1OrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Item1:
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
        included_data: list[IncludedDatum1OrStr] | None = None,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ItemSearchResults1:
        """Returns a paginated list of the seller's listings items. Mirrors Amazon SP-API ``searchListingsItems`` so an
        existing SP-API client can call the seller-level collection endpoint (no SKU in the path) against v4.

        Args:
            seller_id: Seller identifier
            marketplace_ids: Value sent with the request.
            included_data: Value sent with the request.
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
            url_template=self._server.default1("/listings/v4/items/{sellerId}/{sku}"),
            path_params=[param[str]("sellerId", seller_id), param[str]("sku", sku)],
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
        included_data: list[IncludedDatum1OrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Item1, GetListingsItemErrorBody]:
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
            url_template=self._server.default1("/listings/v4/items/{sellerId}/{sku}"),
            path_params=[param[str]("sellerId", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str | None]("issueLocale", issue_locale),
                param[list[IncludedDatum1OrStr] | None]("includedData", included_data),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Item1],
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
            url_template=self._server.default1("/listings/v4/items/{sellerId}/{sku}"),
            path_params=[param[str]("sellerId", seller_id), param[str]("sku", sku)],
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
            url_template=self._server.default1("/listings/v4/items/{sellerId}/{sku}"),
            path_params=[param[str]("sellerId", seller_id), param[str]("sku", sku)],
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
        included_data: list[IncludedDatum1OrStr] | None = None,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemSearchResults1, SearchListingsItemsErrorBody]:
        """Returns a paginated list of the seller's listings items. Mirrors Amazon SP-API ``searchListingsItems`` so an
        existing SP-API client can call the seller-level collection endpoint (no SKU in the path) against v4.

        Args:
            seller_id: Seller identifier
            marketplace_ids: Value sent with the request.
            included_data: Value sent with the request.
            page_size: Maximum number of results per page
            page_token: Opaque cursor returned by a previous call for the next page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/listings/v4/items/{sellerId}"),
            path_params=[param[str]("sellerId", seller_id)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[list[IncludedDatum1OrStr] | None]("includedData", included_data),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ItemSearchResults1],
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
            url_template=self._server.default1("/listings/v4/items/{sellerId}/{sku}"),
            path_params=[param[str]("sellerId", seller_id), param[str]("sku", sku)],
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
        included_data: list[IncludedDatum1OrStr] | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Item1, GetListingsItemErrorBody]:
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
            url_template=self._server.default1("/listings/v4/items/{sellerId}/{sku}"),
            path_params=[param[str]("sellerId", seller_id), param[str]("sku", sku)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str | None]("issueLocale", issue_locale),
                param[list[IncludedDatum1OrStr] | None]("includedData", included_data),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Item1],
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
            url_template=self._server.default1("/listings/v4/items/{sellerId}/{sku}"),
            path_params=[param[str]("sellerId", seller_id), param[str]("sku", sku)],
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
            url_template=self._server.default1("/listings/v4/items/{sellerId}/{sku}"),
            path_params=[param[str]("sellerId", seller_id), param[str]("sku", sku)],
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
        included_data: list[IncludedDatum1OrStr] | None = None,
        page_size: int | None = 10,
        page_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ItemSearchResults1, SearchListingsItemsErrorBody]:
        """Returns a paginated list of the seller's listings items. Mirrors Amazon SP-API ``searchListingsItems`` so an
        existing SP-API client can call the seller-level collection endpoint (no SKU in the path) against v4.

        Args:
            seller_id: Seller identifier
            marketplace_ids: Value sent with the request.
            included_data: Value sent with the request.
            page_size: Maximum number of results per page
            page_token: Opaque cursor returned by a previous call for the next page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/listings/v4/items/{sellerId}"),
            path_params=[param[str]("sellerId", seller_id)],
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[list[IncludedDatum1OrStr] | None]("includedData", included_data),
                param[int | None]("pageSize", page_size),
                param[str | None]("pageToken", page_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ItemSearchResults1],
            error_mapper=search_listings_items_error_mapper,
            request_options=request_options,
        )
