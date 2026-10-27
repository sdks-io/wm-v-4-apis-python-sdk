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
from ..errors.create_destination_error import CreateDestinationErrorBody, create_destination_error_mapper
from ..errors.create_subscription_error import CreateSubscriptionErrorBody, create_subscription_error_mapper
from ..errors.delete_destination_error import DeleteDestinationErrorBody, delete_destination_error_mapper
from ..errors.delete_subscription_by_id_error import (
    DeleteSubscriptionByIdErrorBody,
    delete_subscription_by_id_error_mapper,
)
from ..errors.get_destination_error import GetDestinationErrorBody, get_destination_error_mapper
from ..errors.get_destinations_error import GetDestinationsErrorBody, get_destinations_error_mapper
from ..errors.get_subscription_by_id_error import GetSubscriptionByIdErrorBody, get_subscription_by_id_error_mapper
from ..errors.get_subscription_error import GetSubscriptionErrorBody, get_subscription_error_mapper
from ..errors.send_test_notification_error import SendTestNotificationErrorBody, send_test_notification_error_mapper
from ..models.channel import Channel
from ..models.channel_list import ChannelList
from ..server.server import Server


class Notifications:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = NotificationsWithRawResponse(client, server, auth)

    def create_destination(self, body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Channel:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(self._with_raw_response.create_destination(body, request_options=request_options))

    def create_subscription(
        self, notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            self._with_raw_response.create_subscription(notification_type, body, request_options=request_options)
        )

    def delete_destination(
        self, destination_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Channel:
        """Send a ``DELETE`` request.

        Args:
            destination_id: The identifier for the destination that you want to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(self._with_raw_response.delete_destination(destination_id, request_options=request_options))

    def delete_subscription_by_id(
        self, subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``DELETE`` request.

        Args:
            subscription_id: The identifier for the subscription that you want to delete.
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_subscription_by_id(
                subscription_id, notification_type, request_options=request_options
            ),
        )

    def get_destination(self, destination_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Channel:
        """Send a ``GET`` request.

        Args:
            destination_id: The identifier generated when you created the destination.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(self._with_raw_response.get_destination(destination_id, request_options=request_options))

    def get_destinations(self, *, request_options: RequestOptionsOrDict | None = None) -> ChannelList:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(self._with_raw_response.get_destinations(request_options=request_options))

    def get_subscription(
        self,
        notification_type: str,
        *,
        payload_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            payload_version: The version of the payload object to be used in the notification.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            self._with_raw_response.get_subscription(
                notification_type, payload_version=payload_version, request_options=request_options
            ),
        )

    def get_subscription_by_id(
        self, subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            subscription_id: The identifier for the subscription that you want to get.
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            self._with_raw_response.get_subscription_by_id(
                subscription_id, notification_type, request_options=request_options
            ),
        )

    def send_test_notification(
        self, notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            self._with_raw_response.send_test_notification(notification_type, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> NotificationsWithRawResponse:
        return self._with_raw_response


class AsyncNotifications:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncNotificationsWithRawResponse(client, server, auth)

    async def create_destination(self, body: Any, *, request_options: RequestOptionsOrDict | None = None) -> Channel:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(await self._with_raw_response.create_destination(body, request_options=request_options))

    async def create_subscription(
        self, notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            await self._with_raw_response.create_subscription(notification_type, body, request_options=request_options)
        )

    async def delete_destination(
        self, destination_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Channel:
        """Send a ``DELETE`` request.

        Args:
            destination_id: The identifier for the destination that you want to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(await self._with_raw_response.delete_destination(destination_id, request_options=request_options))

    async def delete_subscription_by_id(
        self, subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``DELETE`` request.

        Args:
            subscription_id: The identifier for the subscription that you want to delete.
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_subscription_by_id(
                subscription_id, notification_type, request_options=request_options
            ),
        )

    async def get_destination(
        self, destination_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Channel:
        """Send a ``GET`` request.

        Args:
            destination_id: The identifier generated when you created the destination.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(await self._with_raw_response.get_destination(destination_id, request_options=request_options))

    async def get_destinations(self, *, request_options: RequestOptionsOrDict | None = None) -> ChannelList:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(await self._with_raw_response.get_destinations(request_options=request_options))

    async def get_subscription(
        self,
        notification_type: str,
        *,
        payload_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            payload_version: The version of the payload object to be used in the notification.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_subscription(
                notification_type, payload_version=payload_version, request_options=request_options
            ),
        )

    async def get_subscription_by_id(
        self, subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            subscription_id: The identifier for the subscription that you want to get.
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            await self._with_raw_response.get_subscription_by_id(
                subscription_id, notification_type, request_options=request_options
            ),
        )

    async def send_test_notification(
        self, notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> Any:
        """Send a ``POST`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Too Many Requests Internal Server Error ``error`` is
                ``RawError``."""
        return unwrap(
            await self._with_raw_response.send_test_notification(
                notification_type, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncNotificationsWithRawResponse:
        return self._with_raw_response


class NotificationsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_destination(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, CreateDestinationErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/notifications/v4/destinations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Channel],
            error_mapper=create_destination_error_mapper,
            request_options=request_options,
        )

    def create_subscription(
        self, notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, CreateSubscriptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}"),
            path_params=[param[str]("notificationType", notification_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=create_subscription_error_mapper,
            request_options=request_options,
        )

    def delete_destination(
        self, destination_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, DeleteDestinationErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            destination_id: The identifier for the destination that you want to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/notifications/v4/destinations/{destinationId}"),
            path_params=[param[str]("destinationId", destination_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Channel],
            error_mapper=delete_destination_error_mapper,
            request_options=request_options,
        )

    def delete_subscription_by_id(
        self, subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, DeleteSubscriptionByIdErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            subscription_id: The identifier for the subscription that you want to delete.
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}/{subscriptionId}"),
            path_params=[
                param[str]("subscriptionId", subscription_id), param[str]("notificationType", notification_type)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=delete_subscription_by_id_error_mapper,
            request_options=request_options,
        )

    def get_destination(
        self, destination_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, GetDestinationErrorBody]:
        """Send a ``GET`` request.

        Args:
            destination_id: The identifier generated when you created the destination.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/notifications/v4/destinations/{destinationId}"),
            path_params=[param[str]("destinationId", destination_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Channel],
            error_mapper=get_destination_error_mapper,
            request_options=request_options,
        )

    def get_destinations(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChannelList, GetDestinationsErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/notifications/v4/destinations"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ChannelList],
            error_mapper=get_destinations_error_mapper,
            request_options=request_options,
        )

    def get_subscription(
        self,
        notification_type: str,
        *,
        payload_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GetSubscriptionErrorBody]:
        """Send a ``GET`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            payload_version: The version of the payload object to be used in the notification.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}"),
            path_params=[param[str]("notificationType", notification_type)],
            query_params=[param[str | None]("payloadVersion", payload_version)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=get_subscription_error_mapper,
            request_options=request_options,
        )

    def get_subscription_by_id(
        self, subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetSubscriptionByIdErrorBody]:
        """Send a ``GET`` request.

        Args:
            subscription_id: The identifier for the subscription that you want to get.
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}/{subscriptionId}"),
            path_params=[
                param[str]("subscriptionId", subscription_id), param[str]("notificationType", notification_type)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=get_subscription_by_id_error_mapper,
            request_options=request_options,
        )

    def send_test_notification(
        self, notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, SendTestNotificationErrorBody]:
        """Send a ``POST`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}/testNotification"),
            path_params=[param[str]("notificationType", notification_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=send_test_notification_error_mapper,
            request_options=request_options,
        )


class AsyncNotificationsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_destination(
        self, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, CreateDestinationErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/notifications/v4/destinations"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Channel],
            error_mapper=create_destination_error_mapper,
            request_options=request_options,
        )

    async def create_subscription(
        self, notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, CreateSubscriptionErrorBody]:
        """Send a ``POST`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}"),
            path_params=[param[str]("notificationType", notification_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=create_subscription_error_mapper,
            request_options=request_options,
        )

    async def delete_destination(
        self, destination_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, DeleteDestinationErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            destination_id: The identifier for the destination that you want to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/notifications/v4/destinations/{destinationId}"),
            path_params=[param[str]("destinationId", destination_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Channel],
            error_mapper=delete_destination_error_mapper,
            request_options=request_options,
        )

    async def delete_subscription_by_id(
        self, subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, DeleteSubscriptionByIdErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            subscription_id: The identifier for the subscription that you want to delete.
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}/{subscriptionId}"),
            path_params=[
                param[str]("subscriptionId", subscription_id), param[str]("notificationType", notification_type)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=delete_subscription_by_id_error_mapper,
            request_options=request_options,
        )

    async def get_destination(
        self, destination_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Channel, GetDestinationErrorBody]:
        """Send a ``GET`` request.

        Args:
            destination_id: The identifier generated when you created the destination.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/notifications/v4/destinations/{destinationId}"),
            path_params=[param[str]("destinationId", destination_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Channel],
            error_mapper=get_destination_error_mapper,
            request_options=request_options,
        )

    async def get_destinations(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ChannelList, GetDestinationsErrorBody]:
        """Send a ``GET`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/notifications/v4/destinations"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ChannelList],
            error_mapper=get_destinations_error_mapper,
            request_options=request_options,
        )

    async def get_subscription(
        self,
        notification_type: str,
        *,
        payload_version: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GetSubscriptionErrorBody]:
        """Send a ``GET`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            payload_version: The version of the payload object to be used in the notification.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}"),
            path_params=[param[str]("notificationType", notification_type)],
            query_params=[param[str | None]("payloadVersion", payload_version)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=get_subscription_error_mapper,
            request_options=request_options,
        )

    async def get_subscription_by_id(
        self, subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetSubscriptionByIdErrorBody]:
        """Send a ``GET`` request.

        Args:
            subscription_id: The identifier for the subscription that you want to get.
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}/{subscriptionId}"),
            path_params=[
                param[str]("subscriptionId", subscription_id), param[str]("notificationType", notification_type)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=get_subscription_by_id_error_mapper,
            request_options=request_options,
        )

    async def send_test_notification(
        self, notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, SendTestNotificationErrorBody]:
        """Send a ``POST`` request.

        Args:
            notification_type: The type of notification. Must be one of: EMAIL, WEBHOOKS, SMS, PULL, MOBILE_PUSH.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/notifications/v4/subscriptions/{notificationType}/testNotification"),
            path_params=[param[str]("notificationType", notification_type)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[Any](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=send_test_notification_error_mapper,
            request_options=request_options,
        )
