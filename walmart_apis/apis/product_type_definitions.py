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
from ..errors.get_definitions_product_type_error import (
    GetDefinitionsProductTypeErrorBody,
    get_definitions_product_type_error_mapper,
)
from ..errors.search_definitions_product_types_error import (
    SearchDefinitionsProductTypesErrorBody,
    search_definitions_product_types_error_mapper,
)
from ..models.product_type_definition import ProductTypeDefinition
from ..models.product_type_list import ProductTypeList
from ..server.server import Server


class ProductTypeDefinitions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ProductTypeDefinitionsWithRawResponse(client, server, auth)

    def get_definitions_product_type(
        self,
        product_type: str,
        *,
        seller_id: str | None = None,
        locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductTypeDefinition:
        """**Placeholder — not yet implemented.**

        Args:
            product_type: Value sent with the request.
            seller_id: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Product type definition schema

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_definitions_product_type(
                product_type, seller_id=seller_id, locale=locale, request_options=request_options
            ),
        )

    def search_definitions_product_types(
        self,
        *,
        keywords: str | None = None,
        item_name: str | None = None,
        locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductTypeList:
        """**Placeholder — not yet implemented.**

        Args:
            keywords: Value sent with the request.
            item_name: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Product type list

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.search_definitions_product_types(
                keywords=keywords, item_name=item_name, locale=locale, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ProductTypeDefinitionsWithRawResponse:
        return self._with_raw_response


class AsyncProductTypeDefinitions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncProductTypeDefinitionsWithRawResponse(client, server, auth)

    async def get_definitions_product_type(
        self,
        product_type: str,
        *,
        seller_id: str | None = None,
        locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductTypeDefinition:
        """**Placeholder — not yet implemented.**

        Args:
            product_type: Value sent with the request.
            seller_id: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Product type definition schema

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_definitions_product_type(
                product_type, seller_id=seller_id, locale=locale, request_options=request_options
            ),
        )

    async def search_definitions_product_types(
        self,
        *,
        keywords: str | None = None,
        item_name: str | None = None,
        locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProductTypeList:
        """**Placeholder — not yet implemented.**

        Args:
            keywords: Value sent with the request.
            item_name: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Product type list

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.search_definitions_product_types(
                keywords=keywords, item_name=item_name, locale=locale, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncProductTypeDefinitionsWithRawResponse:
        return self._with_raw_response


class ProductTypeDefinitionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_definitions_product_type(
        self,
        product_type: str,
        *,
        seller_id: str | None = None,
        locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductTypeDefinition, GetDefinitionsProductTypeErrorBody]:
        """**Placeholder — not yet implemented.**

        Args:
            product_type: Value sent with the request.
            seller_id: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/definitions/v4/productTypes/{productType}"),
            path_params=[param[str]("productType", product_type)],
            query_params=[param[str | None]("sellerId", seller_id), param[str | None]("locale", locale)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ProductTypeDefinition],
            error_mapper=get_definitions_product_type_error_mapper,
            request_options=request_options,
        )

    def search_definitions_product_types(
        self,
        *,
        keywords: str | None = None,
        item_name: str | None = None,
        locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductTypeList, SearchDefinitionsProductTypesErrorBody]:
        """**Placeholder — not yet implemented.**

        Args:
            keywords: Value sent with the request.
            item_name: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/definitions/v4/productTypes"),
            query_params=[
                param[str | None]("keywords", keywords),
                param[str | None]("itemName", item_name),
                param[str | None]("locale", locale),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ProductTypeList],
            error_mapper=search_definitions_product_types_error_mapper,
            request_options=request_options,
        )


class AsyncProductTypeDefinitionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_definitions_product_type(
        self,
        product_type: str,
        *,
        seller_id: str | None = None,
        locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductTypeDefinition, GetDefinitionsProductTypeErrorBody]:
        """**Placeholder — not yet implemented.**

        Args:
            product_type: Value sent with the request.
            seller_id: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/definitions/v4/productTypes/{productType}"),
            path_params=[param[str]("productType", product_type)],
            query_params=[param[str | None]("sellerId", seller_id), param[str | None]("locale", locale)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ProductTypeDefinition],
            error_mapper=get_definitions_product_type_error_mapper,
            request_options=request_options,
        )

    async def search_definitions_product_types(
        self,
        *,
        keywords: str | None = None,
        item_name: str | None = None,
        locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProductTypeList, SearchDefinitionsProductTypesErrorBody]:
        """**Placeholder — not yet implemented.**

        Args:
            keywords: Value sent with the request.
            item_name: Value sent with the request.
            locale: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/definitions/v4/productTypes"),
            query_params=[
                param[str | None]("keywords", keywords),
                param[str | None]("itemName", item_name),
                param[str | None]("locale", locale),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ProductTypeList],
            error_mapper=search_definitions_product_types_error_mapper,
            request_options=request_options,
        )
