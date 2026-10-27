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
from ..errors.get_wfs_inventory_items_error import GetWfsInventoryItemsErrorBody, get_wfs_inventory_items_error_mapper
from ..models.get_wfs_inventory_response import GetWfsInventoryResponse
from ..server.server import Server


class WfsInventory:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WfsInventoryWithRawResponse(client, server, auth)

    def get_wfs_inventory_items(
        self,
        *,
        skus: str | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetWfsInventoryResponse:
        """Returns inventory for items managed by Walmart Fulfillment Services (WFS). Includes stock health, age
        buckets, and demand-intelligence fields not available on seller-fulfilled inventory.

        **Rate limit:** 300 items per page maximum. Requests retrieving more than 100 items per page will receive
        ``X-RateLimit-Limit`` and ``X-RateLimit-Remaining`` headers in the response.

        Args:
            skus: Comma-separated seller SKUs to filter (max 50). Omit to return all WFS items.
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
            self._with_raw_response.get_wfs_inventory_items(
                skus=skus, page_size=page_size, next_token=next_token, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> WfsInventoryWithRawResponse:
        return self._with_raw_response


class AsyncWfsInventory:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWfsInventoryWithRawResponse(client, server, auth)

    async def get_wfs_inventory_items(
        self,
        *,
        skus: str | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetWfsInventoryResponse:
        """Returns inventory for items managed by Walmart Fulfillment Services (WFS). Includes stock health, age
        buckets, and demand-intelligence fields not available on seller-fulfilled inventory.

        **Rate limit:** 300 items per page maximum. Requests retrieving more than 100 items per page will receive
        ``X-RateLimit-Limit`` and ``X-RateLimit-Remaining`` headers in the response.

        Args:
            skus: Comma-separated seller SKUs to filter (max 50). Omit to return all WFS items.
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
            await self._with_raw_response.get_wfs_inventory_items(
                skus=skus, page_size=page_size, next_token=next_token, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWfsInventoryWithRawResponse:
        return self._with_raw_response


class WfsInventoryWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_wfs_inventory_items(
        self,
        *,
        skus: str | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetWfsInventoryResponse, GetWfsInventoryItemsErrorBody]:
        """Returns inventory for items managed by Walmart Fulfillment Services (WFS). Includes stock health, age
        buckets, and demand-intelligence fields not available on seller-fulfilled inventory.

        **Rate limit:** 300 items per page maximum. Requests retrieving more than 100 items per page will receive
        ``X-RateLimit-Limit`` and ``X-RateLimit-Remaining`` headers in the response.

        Args:
            skus: Comma-separated seller SKUs to filter (max 50). Omit to return all WFS items.
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inventory/v4/wfs/items"),
            query_params=[
                param[str | None]("skus", skus),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetWfsInventoryResponse],
            error_mapper=get_wfs_inventory_items_error_mapper,
            request_options=request_options,
        )


class AsyncWfsInventoryWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_wfs_inventory_items(
        self,
        *,
        skus: str | None = None,
        page_size: int | None = 100,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetWfsInventoryResponse, GetWfsInventoryItemsErrorBody]:
        """Returns inventory for items managed by Walmart Fulfillment Services (WFS). Includes stock health, age
        buckets, and demand-intelligence fields not available on seller-fulfilled inventory.

        **Rate limit:** 300 items per page maximum. Requests retrieving more than 100 items per page will receive
        ``X-RateLimit-Limit`` and ``X-RateLimit-Remaining`` headers in the response.

        Args:
            skus: Comma-separated seller SKUs to filter (max 50). Omit to return all WFS items.
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/inventory/v4/wfs/items"),
            query_params=[
                param[str | None]("skus", skus),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetWfsInventoryResponse],
            error_mapper=get_wfs_inventory_items_error_mapper,
            request_options=request_options,
        )
