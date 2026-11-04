from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_supply_source_error import CreateSupplySourceErrorBody, create_supply_source_error_mapper
from ..errors.get_supply_source_error import GetSupplySourceErrorBody, get_supply_source_error_mapper
from ..errors.list_supply_sources_error import ListSupplySourcesErrorBody, list_supply_sources_error_mapper
from ..errors.update_supply_source_error import UpdateSupplySourceErrorBody, update_supply_source_error_mapper
from ..models.create_supply_source_request import CreateSupplySourceRequest, CreateSupplySourceRequestDict
from ..models.create_supply_source_response import CreateSupplySourceResponse
from ..models.supply_source import SupplySource
from ..models.update_supply_source_request import UpdateSupplySourceRequest, UpdateSupplySourceRequestDict
from ..server.server import Server


class SupplySourceApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SupplySourceApiWithRawResponse(client, server, auth)

    def create_supply_source(
        self,
        body: CreateSupplySourceRequest | CreateSupplySourceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateSupplySourceResponse:
        """Creates a new supply source (fulfillment center). Returns only the ``supplySourceId`` and
        ``supplySourceCode`` of the newly created resource.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Supply source created successfully

        Raises:
            ApiError: Bad Request Unauthorized — authentication failed or token missing/expired. Forbidden — the caller
                is not permitted to access this resource. Too Many Requests — rate limit exceeded. Internal Server Error
                ``error`` is ``ErrorListShippingManagement | RawError``."""
        return unwrap(self._with_raw_response.create_supply_source(body, request_options=request_options))

    def get_supply_source(
        self, supply_source_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SupplySource:
        """Returns the supply source (fulfillment center) identified by ``supplySourceId``.

        Args:
            supply_source_id: The unique identifier of the supply source.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Supply source returned successfully

        Raises:
            ApiError: Bad Request Unauthorized — authentication failed or token missing/expired. Forbidden — the caller
                is not permitted to access this resource. Not Found Too Many Requests — rate limit exceeded. Internal
                Server Error ``error`` is ``ErrorListShippingManagement | RawError``."""
        return unwrap(self._with_raw_response.get_supply_source(supply_source_id, request_options=request_options))

    def list_supply_sources(self, *, request_options: RequestOptionsOrDict | None = None) -> list[SupplySource]:
        """Returns every supply source (fulfillment center) registered to the seller ( Phase 2 parity gap: V3's
        ``getAllFulfillmentCenters`` had no V4 equivalent before this).

        No pagination today. Planned enhancements for this operation, including pagination, are tracked and documented
        in the `Shipping Settings APIs - V4 Integration
        <https://confluence.walmart.com/spaces/MTMKTP/pages/3700253502/Shipping+Settings+APIs+-+V4+Integration>`__
        reference doc.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Supply sources returned successfully

        Raises:
            ApiError: Bad Request Unauthorized — authentication failed or token missing/expired. Forbidden — the caller
                is not permitted to access this resource. Too Many Requests — rate limit exceeded. Internal Server Error
                ``error`` is ``ErrorListShippingManagement | RawError``."""
        return unwrap(self._with_raw_response.list_supply_sources(request_options=request_options))

    def update_supply_source(
        self,
        supply_source_id: str,
        body: UpdateSupplySourceRequest | UpdateSupplySourceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the supply source (fulfillment center) identified by ``supplySourceId``. Returns 204 on success with
        no body. On error, returns the standard error envelope.

        Args:
            supply_source_id: The unique identifier of the supply source to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Supply source updated successfully (no content)

        Raises:
            ApiError: Bad Request Unauthorized — authentication failed or token missing/expired. Forbidden — the caller
                is not permitted to access this resource. Not Found Too Many Requests — rate limit exceeded. Internal
                Server Error ``error`` is ``ErrorListShippingManagement | RawError``."""
        return unwrap(
            self._with_raw_response.update_supply_source(supply_source_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> SupplySourceApiWithRawResponse:
        return self._with_raw_response


class AsyncSupplySourceApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSupplySourceApiWithRawResponse(client, server, auth)

    async def create_supply_source(
        self,
        body: CreateSupplySourceRequest | CreateSupplySourceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateSupplySourceResponse:
        """Creates a new supply source (fulfillment center). Returns only the ``supplySourceId`` and
        ``supplySourceCode`` of the newly created resource.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Supply source created successfully

        Raises:
            ApiError: Bad Request Unauthorized — authentication failed or token missing/expired. Forbidden — the caller
                is not permitted to access this resource. Too Many Requests — rate limit exceeded. Internal Server Error
                ``error`` is ``ErrorListShippingManagement | RawError``."""
        return unwrap(await self._with_raw_response.create_supply_source(body, request_options=request_options))

    async def get_supply_source(
        self, supply_source_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SupplySource:
        """Returns the supply source (fulfillment center) identified by ``supplySourceId``.

        Args:
            supply_source_id: The unique identifier of the supply source.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Supply source returned successfully

        Raises:
            ApiError: Bad Request Unauthorized — authentication failed or token missing/expired. Forbidden — the caller
                is not permitted to access this resource. Not Found Too Many Requests — rate limit exceeded. Internal
                Server Error ``error`` is ``ErrorListShippingManagement | RawError``."""
        return unwrap(
            await self._with_raw_response.get_supply_source(supply_source_id, request_options=request_options)
        )

    async def list_supply_sources(self, *, request_options: RequestOptionsOrDict | None = None) -> list[SupplySource]:
        """Returns every supply source (fulfillment center) registered to the seller ( Phase 2 parity gap: V3's
        ``getAllFulfillmentCenters`` had no V4 equivalent before this).

        No pagination today. Planned enhancements for this operation, including pagination, are tracked and documented
        in the `Shipping Settings APIs - V4 Integration
        <https://confluence.walmart.com/spaces/MTMKTP/pages/3700253502/Shipping+Settings+APIs+-+V4+Integration>`__
        reference doc.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Supply sources returned successfully

        Raises:
            ApiError: Bad Request Unauthorized — authentication failed or token missing/expired. Forbidden — the caller
                is not permitted to access this resource. Too Many Requests — rate limit exceeded. Internal Server Error
                ``error`` is ``ErrorListShippingManagement | RawError``."""
        return unwrap(await self._with_raw_response.list_supply_sources(request_options=request_options))

    async def update_supply_source(
        self,
        supply_source_id: str,
        body: UpdateSupplySourceRequest | UpdateSupplySourceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Updates the supply source (fulfillment center) identified by ``supplySourceId``. Returns 204 on success with
        no body. On error, returns the standard error envelope.

        Args:
            supply_source_id: The unique identifier of the supply source to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Supply source updated successfully (no content)

        Raises:
            ApiError: Bad Request Unauthorized — authentication failed or token missing/expired. Forbidden — the caller
                is not permitted to access this resource. Not Found Too Many Requests — rate limit exceeded. Internal
                Server Error ``error`` is ``ErrorListShippingManagement | RawError``."""
        return unwrap(
            await self._with_raw_response.update_supply_source(supply_source_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncSupplySourceApiWithRawResponse:
        return self._with_raw_response


class SupplySourceApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_supply_source(
        self,
        body: CreateSupplySourceRequest | CreateSupplySourceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateSupplySourceResponse, CreateSupplySourceErrorBody]:
        """Creates a new supply source (fulfillment center). Returns only the ``supplySourceId`` and
        ``supplySourceCode`` of the newly created resource.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/shipping-configuration/supply-sources"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSupplySourceRequest | CreateSupplySourceRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateSupplySourceResponse],
            error_mapper=create_supply_source_error_mapper,
            request_options=request_options,
        )

    def get_supply_source(
        self, supply_source_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SupplySource, GetSupplySourceErrorBody]:
        """Returns the supply source (fulfillment center) identified by ``supplySourceId``.

        Args:
            supply_source_id: The unique identifier of the supply source.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/shipping-configuration/supply-sources/{supply-source-id}"
            ),
            path_params=[param[str]("supply-source-id", supply_source_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[SupplySource],
            error_mapper=get_supply_source_error_mapper,
            request_options=request_options,
        )

    def list_supply_sources(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SupplySource], ListSupplySourcesErrorBody]:
        """Returns every supply source (fulfillment center) registered to the seller ( Phase 2 parity gap: V3's
        ``getAllFulfillmentCenters`` had no V4 equivalent before this).

        No pagination today. Planned enhancements for this operation, including pagination, are tracked and documented
        in the `Shipping Settings APIs - V4 Integration
        <https://confluence.walmart.com/spaces/MTMKTP/pages/3700253502/Shipping+Settings+APIs+-+V4+Integration>`__
        reference doc.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/shipping-configuration/supply-sources"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[list[SupplySource]],
            error_mapper=list_supply_sources_error_mapper,
            request_options=request_options,
        )

    def update_supply_source(
        self,
        supply_source_id: str,
        body: UpdateSupplySourceRequest | UpdateSupplySourceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateSupplySourceErrorBody]:
        """Updates the supply source (fulfillment center) identified by ``supplySourceId``. Returns 204 on success with
        no body. On error, returns the standard error envelope.

        Args:
            supply_source_id: The unique identifier of the supply source to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/shipping-configuration/supply-sources/{supply-source-id}"
            ),
            path_params=[param[str]("supply-source-id", supply_source_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSupplySourceRequest | UpdateSupplySourceRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=empty_response,
            error_mapper=update_supply_source_error_mapper,
            request_options=request_options,
        )


class AsyncSupplySourceApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_supply_source(
        self,
        body: CreateSupplySourceRequest | CreateSupplySourceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateSupplySourceResponse, CreateSupplySourceErrorBody]:
        """Creates a new supply source (fulfillment center). Returns only the ``supplySourceId`` and
        ``supplySourceCode`` of the newly created resource.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default_catalog_items("/v4/fulfillment/shipping-configuration/supply-sources"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSupplySourceRequest | CreateSupplySourceRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateSupplySourceResponse],
            error_mapper=create_supply_source_error_mapper,
            request_options=request_options,
        )

    async def get_supply_source(
        self, supply_source_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SupplySource, GetSupplySourceErrorBody]:
        """Returns the supply source (fulfillment center) identified by ``supplySourceId``.

        Args:
            supply_source_id: The unique identifier of the supply source.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/shipping-configuration/supply-sources/{supply-source-id}"
            ),
            path_params=[param[str]("supply-source-id", supply_source_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[SupplySource],
            error_mapper=get_supply_source_error_mapper,
            request_options=request_options,
        )

    async def list_supply_sources(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[SupplySource], ListSupplySourcesErrorBody]:
        """Returns every supply source (fulfillment center) registered to the seller ( Phase 2 parity gap: V3's
        ``getAllFulfillmentCenters`` had no V4 equivalent before this).

        No pagination today. Planned enhancements for this operation, including pagination, are tracked and documented
        in the `Shipping Settings APIs - V4 Integration
        <https://confluence.walmart.com/spaces/MTMKTP/pages/3700253502/Shipping+Settings+APIs+-+V4+Integration>`__
        reference doc.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default_catalog_items("/v4/fulfillment/shipping-configuration/supply-sources"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[list[SupplySource]],
            error_mapper=list_supply_sources_error_mapper,
            request_options=request_options,
        )

    async def update_supply_source(
        self,
        supply_source_id: str,
        body: UpdateSupplySourceRequest | UpdateSupplySourceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateSupplySourceErrorBody]:
        """Updates the supply source (fulfillment center) identified by ``supplySourceId``. Returns 204 on success with
        no body. On error, returns the standard error envelope.

        Args:
            supply_source_id: The unique identifier of the supply source to update.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default_catalog_items(
                "/v4/fulfillment/shipping-configuration/supply-sources/{supply-source-id}"
            ),
            path_params=[param[str]("supply-source-id", supply_source_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateSupplySourceRequest | UpdateSupplySourceRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_empty_response,
            error_mapper=update_supply_source_error_mapper,
            request_options=request_options,
        )
