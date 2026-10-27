from __future__ import annotations

from typing import Any
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
from ..errors.confirm_customization_details_error import (
    ConfirmCustomizationDetailsErrorBody,
    confirm_customization_details_error_mapper,
)
from ..errors.create_confirm_delivery_details_error import (
    CreateConfirmDeliveryDetailsErrorBody,
    create_confirm_delivery_details_error_mapper,
)
from ..errors.create_confirm_order_details_error import (
    CreateConfirmOrderDetailsErrorBody,
    create_confirm_order_details_error_mapper,
)
from ..errors.create_confirm_service_details_error import (
    CreateConfirmServiceDetailsErrorBody,
    create_confirm_service_details_error_mapper,
)
from ..errors.create_digital_access_key_error import (
    CreateDigitalAccessKeyErrorBody,
    create_digital_access_key_error_mapper,
)
from ..errors.create_legal_disclosure_error import CreateLegalDisclosureErrorBody, create_legal_disclosure_error_mapper
from ..errors.create_unexpected_problem_error import (
    CreateUnexpectedProblemErrorBody,
    create_unexpected_problem_error_mapper,
)
from ..errors.create_warranty_error import CreateWarrantyErrorBody, create_warranty_error_mapper
from ..errors.get_attributes_error import GetAttributesErrorBody, get_attributes_error_mapper
from ..errors.get_messaging_actions_for_order_error import (
    GetMessagingActionsForOrderErrorBody,
    get_messaging_actions_for_order_error_mapper,
)
from ..errors.send_invoice_error import SendInvoiceErrorBody, send_invoice_error_mapper
from ..server.server import Server


class Messaging:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MessagingWithRawResponse(client, server, auth)

    def create_warranty(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.create_warranty(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    def get_attributes(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_attributes(sp_api_order_id, marketplace_ids, request_options=request_options)
        )

    def confirm_customization_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.confirm_customization_details(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    def create_confirm_delivery_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.create_confirm_delivery_details(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    def create_confirm_order_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.create_confirm_order_details(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    def create_confirm_service_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.create_confirm_service_details(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    def create_digital_access_key(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.create_digital_access_key(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    def create_legal_disclosure(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.create_legal_disclosure(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    def create_unexpected_problem(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.create_unexpected_problem(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    def get_messaging_actions_for_order(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This specifies the order for which you want a list of
                available message types.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_messaging_actions_for_order(
                sp_api_order_id, marketplace_ids, request_options=request_options
            ),
        )

    def send_invoice(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.send_invoice(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> MessagingWithRawResponse:
        return self._with_raw_response


class AsyncMessaging:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMessagingWithRawResponse(client, server, auth)

    async def create_warranty(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.create_warranty(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    async def get_attributes(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_attributes(
                sp_api_order_id, marketplace_ids, request_options=request_options
            ),
        )

    async def confirm_customization_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.confirm_customization_details(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    async def create_confirm_delivery_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.create_confirm_delivery_details(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    async def create_confirm_order_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.create_confirm_order_details(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    async def create_confirm_service_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.create_confirm_service_details(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    async def create_digital_access_key(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.create_digital_access_key(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    async def create_legal_disclosure(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.create_legal_disclosure(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    async def create_unexpected_problem(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.create_unexpected_problem(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    async def get_messaging_actions_for_order(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This specifies the order for which you want a list of
                available message types.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_messaging_actions_for_order(
                sp_api_order_id, marketplace_ids, request_options=request_options
            ),
        )

    async def send_invoice(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.send_invoice(
                sp_api_order_id, marketplace_ids, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncMessagingWithRawResponse:
        return self._with_raw_response


class MessagingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_warranty(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateWarrantyErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/warranty"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_warranty_error_mapper,
            request_options=request_options,
        )

    def get_attributes(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetAttributesErrorBody]:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/attributes"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=get_attributes_error_mapper,
            request_options=request_options,
        )

    def confirm_customization_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ConfirmCustomizationDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/messaging/v4/orders/{sp-apiOrderId}/messages/confirmCustomizationDetails"
            ),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=confirm_customization_details_error_mapper,
            request_options=request_options,
        )

    def create_confirm_delivery_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateConfirmDeliveryDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/confirmDeliveryDetails"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_confirm_delivery_details_error_mapper,
            request_options=request_options,
        )

    def create_confirm_order_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateConfirmOrderDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/confirmOrderDetails"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_confirm_order_details_error_mapper,
            request_options=request_options,
        )

    def create_confirm_service_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateConfirmServiceDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/confirmServiceDetails"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_confirm_service_details_error_mapper,
            request_options=request_options,
        )

    def create_digital_access_key(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateDigitalAccessKeyErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/digitalAccessKey"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_digital_access_key_error_mapper,
            request_options=request_options,
        )

    def create_legal_disclosure(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateLegalDisclosureErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/legalDisclosure"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_legal_disclosure_error_mapper,
            request_options=request_options,
        )

    def create_unexpected_problem(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateUnexpectedProblemErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/unexpectedProblem"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_unexpected_problem_error_mapper,
            request_options=request_options,
        )

    def get_messaging_actions_for_order(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetMessagingActionsForOrderErrorBody]:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This specifies the order for which you want a list of
                available message types.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=get_messaging_actions_for_order_error_mapper,
            request_options=request_options,
        )

    def send_invoice(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, SendInvoiceErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/invoice"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=send_invoice_error_mapper,
            request_options=request_options,
        )


class AsyncMessagingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_warranty(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateWarrantyErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/warranty"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_warranty_error_mapper,
            request_options=request_options,
        )

    async def get_attributes(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetAttributesErrorBody]:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/attributes"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=get_attributes_error_mapper,
            request_options=request_options,
        )

    async def confirm_customization_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ConfirmCustomizationDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1(
                "/messaging/v4/orders/{sp-apiOrderId}/messages/confirmCustomizationDetails"
            ),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=confirm_customization_details_error_mapper,
            request_options=request_options,
        )

    async def create_confirm_delivery_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateConfirmDeliveryDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/confirmDeliveryDetails"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_confirm_delivery_details_error_mapper,
            request_options=request_options,
        )

    async def create_confirm_order_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateConfirmOrderDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/confirmOrderDetails"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_confirm_order_details_error_mapper,
            request_options=request_options,
        )

    async def create_confirm_service_details(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateConfirmServiceDetailsErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/confirmServiceDetails"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_confirm_service_details_error_mapper,
            request_options=request_options,
        )

    async def create_digital_access_key(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateDigitalAccessKeyErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/digitalAccessKey"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_digital_access_key_error_mapper,
            request_options=request_options,
        )

    async def create_legal_disclosure(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateLegalDisclosureErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/legalDisclosure"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_legal_disclosure_error_mapper,
            request_options=request_options,
        )

    async def create_unexpected_problem(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, CreateUnexpectedProblemErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/unexpectedProblem"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_unexpected_problem_error_mapper,
            request_options=request_options,
        )

    async def get_messaging_actions_for_order(
        self, sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetMessagingActionsForOrderErrorBody]:
        """Send a ``GET`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This specifies the order for which you want a list of
                available message types.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=get_messaging_actions_for_order_error_mapper,
            request_options=request_options,
        )

    async def send_invoice(
        self,
        sp_api_order_id: str,
        marketplace_ids: list[str],
        body: Any,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, SendInvoiceErrorBody]:
        """Send a ``POST`` request.

        Args:
            sp_api_order_id: A marketplace order identifier. This identifies the order for which a message is sent.
            marketplace_ids: A marketplace identifier. This identifies the marketplace in which the order was placed.
                You can only specify one market
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/messaging/v4/orders/{sp-apiOrderId}/messages/invoice"),
            path_params=[param[str]("sp-apiOrderId", sp_api_order_id)],
            query_params=[param[list[str]]("marketplaceIds", marketplace_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=send_invoice_error_mapper,
            request_options=request_options,
        )
