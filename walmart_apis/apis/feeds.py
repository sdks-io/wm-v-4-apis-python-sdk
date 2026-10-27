from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncFileInput,
    AsyncFileResponse,
    AsyncRawClient,
    FileInput,
    FileResponse,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    async_file_decoder,
    async_json_decoder,
    file_decoder,
    file_part,
    json_decoder,
    multipart_body,
    param,
    unwrap,
)
from ..errors.cancel_feed_error import CancelFeedErrorBody, cancel_feed_error_mapper
from ..errors.create_feed_error import CreateFeedErrorBody, create_feed_error_mapper
from ..errors.get_feed_document_error import GetFeedDocumentErrorBody, get_feed_document_error_mapper
from ..errors.get_feed_error import GetFeedErrorBody, get_feed_error_mapper
from ..errors.get_feeds_error import GetFeedsErrorBody, get_feeds_error_mapper
from ..models.cancel_feed_response import CancelFeedResponse
from ..models.create_feed_response import CreateFeedResponse
from ..models.enums.content_type import ContentTypeOrStr
from ..models.enums.feed_status import FeedStatusOrStr
from ..models.enums.feed_type import FeedTypeOrStr
from ..models.feed import Feed
from ..models.get_feeds_response import GetFeedsResponse
from ..server.server import Server


class Feeds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FeedsWithRawResponse(client, server, auth)

    def cancel_feed(self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CancelFeedResponse:
        """**Placeholder — not yet implemented.** Cancels the feed identified by feedId if it is still queued or in
        progress. Mirrors Amazon SP-API ``cancelFeed`` (DELETE /feeds/2021-06-30/feeds/{feedId}) so partners can
        generate a client against the final contract now. A feed that has already reached DONE or ERROR cannot be
        cancelled.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation accepted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``ErrorList1 | RawError``."""
        return unwrap(self._with_raw_response.cancel_feed(feed_id, request_options=request_options))

    def create_feed(
        self,
        feed_type: FeedTypeOrStr,
        file: FileInput,
        *,
        marketplace_id: str | None = None,
        content_type: ContentTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateFeedResponse:
        """Upload a feed file and submit it for asynchronous processing in a single call. The server handles document
        storage internally. Use the returned feedId to poll processing status via GET /feeds/v4/feeds/{feedId}.

        Args:
            feed_type: The type of feed being submitted
            file: The feed content file to upload and process
            marketplace_id: Marketplace identifier (opaque token). If omitted, the service applies WALMART_US.
            content_type: MIME type of the uploaded feed content. If omitted, the server infers from the file's
                Content-Type in the multipart header.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Feed accepted for processing

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.create_feed(
                feed_type,
                file,
                marketplace_id=marketplace_id,
                content_type=content_type,
                request_options=request_options,
            ),
        )

    def get_feed(self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Feed:
        """Send a ``GET`` request.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``ErrorList1 | RawError``."""
        return unwrap(self._with_raw_response.get_feed(feed_id, request_options=request_options))

    def get_feed_document(self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FileResponse:
        """Downloads the raw feed document file. The response is a binary stream (application/octet-stream). The
        Content-Disposition header contains the original filename when available. Content-Length header is always set to
        enable download progress tracking.

        An IDOR check is performed before the download — the authenticated seller must own the feed referenced by
        feedId.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Binary file stream

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``ErrorList1 | RawError``."""
        return unwrap(self._with_raw_response.get_feed_document(feed_id, request_options=request_options))

    def get_feeds(
        self,
        *,
        feed_types: list[FeedTypeOrStr] | None = None,
        feed_statuses: list[FeedStatusOrStr] | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFeedsResponse:
        """Send a ``GET`` request.

        Args:
            feed_types: Feed type filter
            feed_statuses: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList1 |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_feeds(
                feed_types=feed_types,
                feed_statuses=feed_statuses,
                created_since=created_since,
                created_until=created_until,
                page_size=page_size,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> FeedsWithRawResponse:
        return self._with_raw_response


class AsyncFeeds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFeedsWithRawResponse(client, server, auth)

    async def cancel_feed(
        self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelFeedResponse:
        """**Placeholder — not yet implemented.** Cancels the feed identified by feedId if it is still queued or in
        progress. Mirrors Amazon SP-API ``cancelFeed`` (DELETE /feeds/2021-06-30/feeds/{feedId}) so partners can
        generate a client against the final contract now. A feed that has already reached DONE or ERROR cannot be
        cancelled.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Cancellation accepted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``ErrorList1 | RawError``."""
        return unwrap(await self._with_raw_response.cancel_feed(feed_id, request_options=request_options))

    async def create_feed(
        self,
        feed_type: FeedTypeOrStr,
        file: AsyncFileInput,
        *,
        marketplace_id: str | None = None,
        content_type: ContentTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateFeedResponse:
        """Upload a feed file and submit it for asynchronous processing in a single call. The server handles document
        storage internally. Use the returned feedId to poll processing status via GET /feeds/v4/feeds/{feedId}.

        Args:
            feed_type: The type of feed being submitted
            file: The feed content file to upload and process
            marketplace_id: Marketplace identifier (opaque token). If omitted, the service applies WALMART_US.
            content_type: MIME type of the uploaded feed content. If omitted, the server infers from the file's
                Content-Type in the multipart header.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Feed accepted for processing

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.create_feed(
                feed_type,
                file,
                marketplace_id=marketplace_id,
                content_type=content_type,
                request_options=request_options,
            ),
        )

    async def get_feed(self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Feed:
        """Send a ``GET`` request.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``ErrorList1 | RawError``."""
        return unwrap(await self._with_raw_response.get_feed(feed_id, request_options=request_options))

    async def get_feed_document(
        self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsyncFileResponse:
        """Downloads the raw feed document file. The response is a binary stream (application/octet-stream). The
        Content-Disposition header contains the original filename when available. Content-Length header is always set to
        enable download progress tracking.

        An IDOR check is performed before the download — the authenticated seller must own the feed referenced by
        feedId.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Binary file stream

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is
                ``ErrorList1 | RawError``."""
        return unwrap(await self._with_raw_response.get_feed_document(feed_id, request_options=request_options))

    async def get_feeds(
        self,
        *,
        feed_types: list[FeedTypeOrStr] | None = None,
        feed_statuses: list[FeedStatusOrStr] | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetFeedsResponse:
        """Send a ``GET`` request.

        Args:
            feed_types: Feed type filter
            feed_statuses: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList1 |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_feeds(
                feed_types=feed_types,
                feed_statuses=feed_statuses,
                created_since=created_since,
                created_until=created_until,
                page_size=page_size,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncFeedsWithRawResponse:
        return self._with_raw_response


class FeedsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_feed(
        self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelFeedResponse, CancelFeedErrorBody]:
        """**Placeholder — not yet implemented.** Cancels the feed identified by feedId if it is still queued or in
        progress. Mirrors Amazon SP-API ``cancelFeed`` (DELETE /feeds/2021-06-30/feeds/{feedId}) so partners can
        generate a client against the final contract now. A feed that has already reached DONE or ERROR cannot be
        cancelled.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/feeds/v4/feeds/{feedId}"),
            path_params=[param[str]("feedId", feed_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelFeedResponse],
            error_mapper=cancel_feed_error_mapper,
            request_options=request_options,
        )

    def create_feed(
        self,
        feed_type: FeedTypeOrStr,
        file: FileInput,
        *,
        marketplace_id: str | None = None,
        content_type: ContentTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateFeedResponse, CreateFeedErrorBody]:
        """Upload a feed file and submit it for asynchronous processing in a single call. The server handles document
        storage internally. Use the returned feedId to poll processing status via GET /feeds/v4/feeds/{feedId}.

        Args:
            feed_type: The type of feed being submitted
            file: The feed content file to upload and process
            marketplace_id: Marketplace identifier (opaque token). If omitted, the service applies WALMART_US.
            content_type: MIME type of the uploaded feed content. If omitted, the server infers from the file's
                Content-Type in the multipart header.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/feeds/v4/feeds"),
            query_params=[
                param[FeedTypeOrStr]("feedType", feed_type), param[str | None]("marketplaceId", marketplace_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(file_part("file", file), param[ContentTypeOrStr | None]("contentType", content_type)),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateFeedResponse],
            error_mapper=create_feed_error_mapper,
            request_options=request_options,
        )

    def get_feed(
        self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Feed, GetFeedErrorBody]:
        """Send a ``GET`` request.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/feeds/v4/feeds/{feedId}"),
            path_params=[param[str]("feedId", feed_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Feed],
            error_mapper=get_feed_error_mapper,
            request_options=request_options,
        )

    def get_feed_document(
        self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponse, GetFeedDocumentErrorBody]:
        """Downloads the raw feed document file. The response is a binary stream (application/octet-stream). The
        Content-Disposition header contains the original filename when available. Content-Length header is always set to
        enable download progress tracking.

        An IDOR check is performed before the download — the authenticated seller must own the feed referenced by
        feedId.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/feeds/v4/feeds/{feedId}/document"),
            path_params=[param[str]("feedId", feed_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=file_decoder,
            error_mapper=get_feed_document_error_mapper,
            request_options=request_options,
        )

    def get_feeds(
        self,
        *,
        feed_types: list[FeedTypeOrStr] | None = None,
        feed_statuses: list[FeedStatusOrStr] | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFeedsResponse, GetFeedsErrorBody]:
        """Send a ``GET`` request.

        Args:
            feed_types: Feed type filter
            feed_statuses: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/feeds/v4/feeds"),
            query_params=[
                param[list[FeedTypeOrStr] | None]("feedTypes", feed_types),
                param[list[FeedStatusOrStr] | None]("feedStatuses", feed_statuses),
                param[RFC3339DateTime | None]("createdSince", created_since),
                param[RFC3339DateTime | None]("createdUntil", created_until),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetFeedsResponse],
            error_mapper=get_feeds_error_mapper,
            request_options=request_options,
        )


class AsyncFeedsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_feed(
        self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelFeedResponse, CancelFeedErrorBody]:
        """**Placeholder — not yet implemented.** Cancels the feed identified by feedId if it is still queued or in
        progress. Mirrors Amazon SP-API ``cancelFeed`` (DELETE /feeds/2021-06-30/feeds/{feedId}) so partners can
        generate a client against the final contract now. A feed that has already reached DONE or ERROR cannot be
        cancelled.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/feeds/v4/feeds/{feedId}"),
            path_params=[param[str]("feedId", feed_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelFeedResponse],
            error_mapper=cancel_feed_error_mapper,
            request_options=request_options,
        )

    async def create_feed(
        self,
        feed_type: FeedTypeOrStr,
        file: AsyncFileInput,
        *,
        marketplace_id: str | None = None,
        content_type: ContentTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateFeedResponse, CreateFeedErrorBody]:
        """Upload a feed file and submit it for asynchronous processing in a single call. The server handles document
        storage internally. Use the returned feedId to poll processing status via GET /feeds/v4/feeds/{feedId}.

        Args:
            feed_type: The type of feed being submitted
            file: The feed content file to upload and process
            marketplace_id: Marketplace identifier (opaque token). If omitted, the service applies WALMART_US.
            content_type: MIME type of the uploaded feed content. If omitted, the server infers from the file's
                Content-Type in the multipart header.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/feeds/v4/feeds"),
            query_params=[
                param[FeedTypeOrStr]("feedType", feed_type), param[str | None]("marketplaceId", marketplace_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=multipart_body(file_part("file", file), param[ContentTypeOrStr | None]("contentType", content_type)),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateFeedResponse],
            error_mapper=create_feed_error_mapper,
            request_options=request_options,
        )

    async def get_feed(
        self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Feed, GetFeedErrorBody]:
        """Send a ``GET`` request.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/feeds/v4/feeds/{feedId}"),
            path_params=[param[str]("feedId", feed_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Feed],
            error_mapper=get_feed_error_mapper,
            request_options=request_options,
        )

    async def get_feed_document(
        self, feed_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsyncFileResponse, GetFeedDocumentErrorBody]:
        """Downloads the raw feed document file. The response is a binary stream (application/octet-stream). The
        Content-Disposition header contains the original filename when available. Content-Length header is always set to
        enable download progress tracking.

        An IDOR check is performed before the download — the authenticated seller must own the feed referenced by
        feedId.

        Args:
            feed_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/feeds/v4/feeds/{feedId}/document"),
            path_params=[param[str]("feedId", feed_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_file_decoder,
            error_mapper=get_feed_document_error_mapper,
            request_options=request_options,
        )

    async def get_feeds(
        self,
        *,
        feed_types: list[FeedTypeOrStr] | None = None,
        feed_statuses: list[FeedStatusOrStr] | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetFeedsResponse, GetFeedsErrorBody]:
        """Send a ``GET`` request.

        Args:
            feed_types: Feed type filter
            feed_statuses: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
            page_size: Value sent with the request.
            next_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/feeds/v4/feeds"),
            query_params=[
                param[list[FeedTypeOrStr] | None]("feedTypes", feed_types),
                param[list[FeedStatusOrStr] | None]("feedStatuses", feed_statuses),
                param[RFC3339DateTime | None]("createdSince", created_since),
                param[RFC3339DateTime | None]("createdUntil", created_until),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetFeedsResponse],
            error_mapper=get_feeds_error_mapper,
            request_options=request_options,
        )
