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
from ..errors.cancel_shipment_error import CancelShipmentErrorBody, cancel_shipment_error_mapper
from ..errors.create_shipment_error import CreateShipmentErrorBody, create_shipment_error_mapper
from ..errors.get_eligible_shipping_services_error import (
    GetEligibleShippingServicesErrorBody,
    get_eligible_shipping_services_error_mapper,
)
from ..errors.get_label_error import GetLabelErrorBody, get_label_error_mapper
from ..errors.get_shipment2_error import GetShipment2ErrorBody, get_shipment2_error_mapper
from ..models.cancel_shipment_response import CancelShipmentResponse
from ..models.create_shipment_request import CreateShipmentRequest, CreateShipmentRequestDict
from ..models.create_shipment_response import CreateShipmentResponse
from ..models.enums.format import Format, FormatOrStr
from ..models.get_eligible_shipping_services_request import (
    GetEligibleShippingServicesRequest,
    GetEligibleShippingServicesRequestDict,
)
from ..models.get_eligible_shipping_services_response import GetEligibleShippingServicesResponse
from ..models.get_shipment_response import GetShipmentResponse
from ..models.label import Label
from ..server.server import Server


class MerchantFulfillment:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MerchantFulfillmentWithRawResponse(client, server, auth)

    def cancel_shipment(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelShipmentResponse:
        """Send a ``DELETE`` request.

        Args:
            shipment_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Shipment cancelled

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.cancel_shipment(shipment_id, request_options=request_options))

    def create_shipment(
        self,
        body: CreateShipmentRequest | CreateShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateShipmentResponse:
        """Creates a shipment for an order, purchases a shipping label from the selected carrier, and returns the label
        for printing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.create_shipment(body, request_options=request_options))

    def get_eligible_shipping_services(
        self,
        body: GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetEligibleShippingServicesResponse:
        """Returns available carriers and rates for a shipment based on package dimensions, weight, and destination
        address.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.get_eligible_shipping_services(body, request_options=request_options))

    def get_label(
        self,
        shipment_id: str,
        *,
        format_: FormatOrStr | None = Format.PDF,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Label:
        """Returns the purchased shipping label for a shipment in the requested file format for printing.

        Args:
            shipment_id: Value sent with the request.
            format_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Label returned

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_label(shipment_id, format_=format_, request_options=request_options))

    def get_shipment2(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetShipmentResponse:
        """Send a ``GET`` request.

        Args:
            shipment_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_shipment2(shipment_id, request_options=request_options))

    @property
    def with_raw_response(self) -> MerchantFulfillmentWithRawResponse:
        return self._with_raw_response


class AsyncMerchantFulfillment:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMerchantFulfillmentWithRawResponse(client, server, auth)

    async def cancel_shipment(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelShipmentResponse:
        """Send a ``DELETE`` request.

        Args:
            shipment_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Shipment cancelled

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.cancel_shipment(shipment_id, request_options=request_options))

    async def create_shipment(
        self,
        body: CreateShipmentRequest | CreateShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateShipmentResponse:
        """Creates a shipment for an order, purchases a shipping label from the selected carrier, and returns the label
        for printing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.create_shipment(body, request_options=request_options))

    async def get_eligible_shipping_services(
        self,
        body: GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetEligibleShippingServicesResponse:
        """Returns available carriers and rates for a shipment based on package dimensions, weight, and destination
        address.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_eligible_shipping_services(body, request_options=request_options)
        )

    async def get_label(
        self,
        shipment_id: str,
        *,
        format_: FormatOrStr | None = Format.PDF,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Label:
        """Returns the purchased shipping label for a shipment in the requested file format for printing.

        Args:
            shipment_id: Value sent with the request.
            format_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Label returned

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_label(shipment_id, format_=format_, request_options=request_options)
        )

    async def get_shipment2(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetShipmentResponse:
        """Send a ``GET`` request.

        Args:
            shipment_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.get_shipment2(shipment_id, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncMerchantFulfillmentWithRawResponse:
        return self._with_raw_response


class MerchantFulfillmentWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_shipment(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelShipmentResponse, CancelShipmentErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            shipment_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/mfn/v4/shipments/{shipmentId}"),
            path_params=[param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelShipmentResponse],
            error_mapper=cancel_shipment_error_mapper,
            request_options=request_options,
        )

    def create_shipment(
        self,
        body: CreateShipmentRequest | CreateShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateShipmentResponse, CreateShipmentErrorBody]:
        """Creates a shipment for an order, purchases a shipping label from the selected carrier, and returns the label
        for printing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/mfn/v4/shipments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateShipmentRequest | CreateShipmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateShipmentResponse],
            error_mapper=create_shipment_error_mapper,
            request_options=request_options,
        )

    def get_eligible_shipping_services(
        self,
        body: GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetEligibleShippingServicesResponse, GetEligibleShippingServicesErrorBody]:
        """Returns available carriers and rates for a shipment based on package dimensions, weight, and destination
        address.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/mfn/v4/eligibleShippingServices"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetEligibleShippingServicesResponse],
            error_mapper=get_eligible_shipping_services_error_mapper,
            request_options=request_options,
        )

    def get_label(
        self,
        shipment_id: str,
        *,
        format_: FormatOrStr | None = Format.PDF,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Label, GetLabelErrorBody]:
        """Returns the purchased shipping label for a shipment in the requested file format for printing.

        Args:
            shipment_id: Value sent with the request.
            format_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/mfn/v4/shipments/{shipmentId}/label"),
            path_params=[param[str]("shipmentId", shipment_id)],
            query_params=[param[FormatOrStr | None]("format", format_)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Label],
            error_mapper=get_label_error_mapper,
            request_options=request_options,
        )

    def get_shipment2(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetShipmentResponse, GetShipment2ErrorBody]:
        """Send a ``GET`` request.

        Args:
            shipment_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/mfn/v4/shipments/{shipmentId}"),
            path_params=[param[str]("shipmentId", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetShipmentResponse],
            error_mapper=get_shipment2_error_mapper,
            request_options=request_options,
        )


class AsyncMerchantFulfillmentWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_shipment(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelShipmentResponse, CancelShipmentErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            shipment_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/mfn/v4/shipments/{shipmentId}"),
            path_params=[param[str]("shipmentId", shipment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelShipmentResponse],
            error_mapper=cancel_shipment_error_mapper,
            request_options=request_options,
        )

    async def create_shipment(
        self,
        body: CreateShipmentRequest | CreateShipmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateShipmentResponse, CreateShipmentErrorBody]:
        """Creates a shipment for an order, purchases a shipping label from the selected carrier, and returns the label
        for printing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/mfn/v4/shipments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateShipmentRequest | CreateShipmentRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateShipmentResponse],
            error_mapper=create_shipment_error_mapper,
            request_options=request_options,
        )

    async def get_eligible_shipping_services(
        self,
        body: GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetEligibleShippingServicesResponse, GetEligibleShippingServicesErrorBody]:
        """Returns available carriers and rates for a shipment based on package dimensions, weight, and destination
        address.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/mfn/v4/eligibleShippingServices"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetEligibleShippingServicesRequest | GetEligibleShippingServicesRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetEligibleShippingServicesResponse],
            error_mapper=get_eligible_shipping_services_error_mapper,
            request_options=request_options,
        )

    async def get_label(
        self,
        shipment_id: str,
        *,
        format_: FormatOrStr | None = Format.PDF,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Label, GetLabelErrorBody]:
        """Returns the purchased shipping label for a shipment in the requested file format for printing.

        Args:
            shipment_id: Value sent with the request.
            format_: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/mfn/v4/shipments/{shipmentId}/label"),
            path_params=[param[str]("shipmentId", shipment_id)],
            query_params=[param[FormatOrStr | None]("format", format_)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Label],
            error_mapper=get_label_error_mapper,
            request_options=request_options,
        )

    async def get_shipment2(
        self, shipment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetShipmentResponse, GetShipment2ErrorBody]:
        """Send a ``GET`` request.

        Args:
            shipment_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/mfn/v4/shipments/{shipmentId}"),
            path_params=[param[str]("shipmentId", shipment_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetShipmentResponse],
            error_mapper=get_shipment2_error_mapper,
            request_options=request_options,
        )
