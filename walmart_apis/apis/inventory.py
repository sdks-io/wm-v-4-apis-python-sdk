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
from ..errors.bulk_update_inventory_error import BulkUpdateInventoryErrorBody, bulk_update_inventory_error_mapper
from ..errors.get_inventory_for_sku_error import GetInventoryForSkuErrorBody, get_inventory_for_sku_error_mapper
from ..errors.get_inventory_summaries_error import GetInventorySummariesErrorBody, get_inventory_summaries_error_mapper
from ..errors.update_inventory_for_sku_error import (
    UpdateInventoryForSkuErrorBody,
    update_inventory_for_sku_error_mapper,
)
from ..models.bulk_update_inventory_request import BulkUpdateInventoryRequest, BulkUpdateInventoryRequestDict
from ..models.bulk_update_inventory_response import BulkUpdateInventoryResponse
from ..models.get_inventory_summaries_response import GetInventorySummariesResponse
from ..models.inventory_summary import InventorySummary
from ..models.update_inventory_request import UpdateInventoryRequest, UpdateInventoryRequestDict
from ..models.update_inventory_response import UpdateInventoryResponse
from ..server.server import Server


class Inventory:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InventoryWithRawResponse(client, server, auth)

    def bulk_update_inventory(
        self,
        body: BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpdateInventoryResponse:
        """Bulk inventory update. Max 500 items per request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Bulk update accepted

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.bulk_update_inventory(body, request_options=request_options))

    def get_inventory_for_sku(
        self, sku: str, *, ship_node: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InventorySummary:
        """Send a ``GET`` request.

        Args:
            sku: Value sent with the request.
            ship_node: Walmart Ship Node ID (for multi-node sellers)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_inventory_for_sku(sku, ship_node=ship_node, request_options=request_options)
        )

    def get_inventory_summaries(
        self,
        *,
        skus: str | None = None,
        ship_node: str | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetInventorySummariesResponse:
        """Send a ``GET`` request.

        Args:
            skus: Comma-separated seller SKUs (max 50)
            ship_node: Walmart Ship Node ID (for multi-node sellers)
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_inventory_summaries(
                skus=skus,
                ship_node=ship_node,
                page_size=page_size,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    def update_inventory_for_sku(
        self,
        sku: str,
        body: UpdateInventoryRequest | UpdateInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateInventoryResponse:
        """Send a ``PUT`` request.

        Args:
            sku: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Inventory updated successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.update_inventory_for_sku(sku, body, request_options=request_options))

    @property
    def with_raw_response(self) -> InventoryWithRawResponse:
        return self._with_raw_response


class AsyncInventory:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInventoryWithRawResponse(client, server, auth)

    async def bulk_update_inventory(
        self,
        body: BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpdateInventoryResponse:
        """Bulk inventory update. Max 500 items per request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Bulk update accepted

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.bulk_update_inventory(body, request_options=request_options))

    async def get_inventory_for_sku(
        self, sku: str, *, ship_node: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> InventorySummary:
        """Send a ``GET`` request.

        Args:
            sku: Value sent with the request.
            ship_node: Walmart Ship Node ID (for multi-node sellers)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_inventory_for_sku(
                sku, ship_node=ship_node, request_options=request_options
            ),
        )

    async def get_inventory_summaries(
        self,
        *,
        skus: str | None = None,
        ship_node: str | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetInventorySummariesResponse:
        """Send a ``GET`` request.

        Args:
            skus: Comma-separated seller SKUs (max 50)
            ship_node: Walmart Ship Node ID (for multi-node sellers)
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_inventory_summaries(
                skus=skus,
                ship_node=ship_node,
                page_size=page_size,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    async def update_inventory_for_sku(
        self,
        sku: str,
        body: UpdateInventoryRequest | UpdateInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateInventoryResponse:
        """Send a ``PUT`` request.

        Args:
            sku: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Inventory updated successfully

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.update_inventory_for_sku(sku, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncInventoryWithRawResponse:
        return self._with_raw_response


class InventoryWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_update_inventory(
        self,
        body: BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpdateInventoryResponse, BulkUpdateInventoryErrorBody]:
        """Bulk inventory update. Max 500 items per request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inventory/v4/items/bulk"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[BulkUpdateInventoryResponse],
            error_mapper=bulk_update_inventory_error_mapper,
            request_options=request_options,
        )

    def get_inventory_for_sku(
        self, sku: str, *, ship_node: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InventorySummary, GetInventoryForSkuErrorBody]:
        """Send a ``GET`` request.

        Args:
            sku: Value sent with the request.
            ship_node: Walmart Ship Node ID (for multi-node sellers)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inventory/v4/items/{sku}"),
            path_params=[param[str]("sku", sku)],
            query_params=[param[str | None]("shipNode", ship_node)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[InventorySummary],
            error_mapper=get_inventory_for_sku_error_mapper,
            request_options=request_options,
        )

    def get_inventory_summaries(
        self,
        *,
        skus: str | None = None,
        ship_node: str | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetInventorySummariesResponse, GetInventorySummariesErrorBody]:
        """Send a ``GET`` request.

        Args:
            skus: Comma-separated seller SKUs (max 50)
            ship_node: Walmart Ship Node ID (for multi-node sellers)
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inventory/v4/items"),
            query_params=[
                param[str | None]("skus", skus),
                param[str | None]("shipNode", ship_node),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetInventorySummariesResponse],
            error_mapper=get_inventory_summaries_error_mapper,
            request_options=request_options,
        )

    def update_inventory_for_sku(
        self,
        sku: str,
        body: UpdateInventoryRequest | UpdateInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateInventoryResponse, UpdateInventoryForSkuErrorBody]:
        """Send a ``PUT`` request.

        Args:
            sku: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/inventory/v4/items/{sku}"),
            path_params=[param[str]("sku", sku)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateInventoryRequest | UpdateInventoryRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[UpdateInventoryResponse],
            error_mapper=update_inventory_for_sku_error_mapper,
            request_options=request_options,
        )


class AsyncInventoryWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_update_inventory(
        self,
        body: BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpdateInventoryResponse, BulkUpdateInventoryErrorBody]:
        """Bulk inventory update. Max 500 items per request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/inventory/v4/items/bulk"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpdateInventoryRequest | BulkUpdateInventoryRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[BulkUpdateInventoryResponse],
            error_mapper=bulk_update_inventory_error_mapper,
            request_options=request_options,
        )

    async def get_inventory_for_sku(
        self, sku: str, *, ship_node: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InventorySummary, GetInventoryForSkuErrorBody]:
        """Send a ``GET`` request.

        Args:
            sku: Value sent with the request.
            ship_node: Walmart Ship Node ID (for multi-node sellers)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inventory/v4/items/{sku}"),
            path_params=[param[str]("sku", sku)],
            query_params=[param[str | None]("shipNode", ship_node)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[InventorySummary],
            error_mapper=get_inventory_for_sku_error_mapper,
            request_options=request_options,
        )

    async def get_inventory_summaries(
        self,
        *,
        skus: str | None = None,
        ship_node: str | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetInventorySummariesResponse, GetInventorySummariesErrorBody]:
        """Send a ``GET`` request.

        Args:
            skus: Comma-separated seller SKUs (max 50)
            ship_node: Walmart Ship Node ID (for multi-node sellers)
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inventory/v4/items"),
            query_params=[
                param[str | None]("skus", skus),
                param[str | None]("shipNode", ship_node),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetInventorySummariesResponse],
            error_mapper=get_inventory_summaries_error_mapper,
            request_options=request_options,
        )

    async def update_inventory_for_sku(
        self,
        sku: str,
        body: UpdateInventoryRequest | UpdateInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateInventoryResponse, UpdateInventoryForSkuErrorBody]:
        """Send a ``PUT`` request.

        Args:
            sku: Value sent with the request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/inventory/v4/items/{sku}"),
            path_params=[param[str]("sku", sku)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateInventoryRequest | UpdateInventoryRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[UpdateInventoryResponse],
            error_mapper=update_inventory_for_sku_error_mapper,
            request_options=request_options,
        )
