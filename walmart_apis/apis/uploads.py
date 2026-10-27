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
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_upload_destination_for_resource_error import (
    CreateUploadDestinationForResourceErrorBody,
    create_upload_destination_for_resource_error_mapper,
)
from ..models.create_upload_destination_response import CreateUploadDestinationResponse
from ..models.enums.content_type1 import ContentType1OrStr
from ..models.enums.resource import ResourceOrStr
from ..server.server import Server


class Uploads:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UploadsWithRawResponse(client, server, auth)

    def create_upload_destination_for_resource(
        self,
        resource: ResourceOrStr,
        content_type: ContentType1OrStr,
        marketplace_ids: list[str],
        content_md5: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateUploadDestinationResponse:
        """Returns a pre-signed URL and upload destination ID for uploading a document for the given resource (e.g.
        feeds, reports). **Do not log the pre-signed URL — it contains temporary credentials.**

        Args:
            resource: The resource type for the upload destination (e.g. feeds)
            content_type: MIME type of the content to be uploaded
            marketplace_ids: Value sent with the request.
            content_md5: MD5 hash of the content to be uploaded, encoded as base64
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Upload destination created

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.create_upload_destination_for_resource(
                resource, content_type, marketplace_ids, content_md5, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> UploadsWithRawResponse:
        return self._with_raw_response


class AsyncUploads:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUploadsWithRawResponse(client, server, auth)

    async def create_upload_destination_for_resource(
        self,
        resource: ResourceOrStr,
        content_type: ContentType1OrStr,
        marketplace_ids: list[str],
        content_md5: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateUploadDestinationResponse:
        """Returns a pre-signed URL and upload destination ID for uploading a document for the given resource (e.g.
        feeds, reports). **Do not log the pre-signed URL — it contains temporary credentials.**

        Args:
            resource: The resource type for the upload destination (e.g. feeds)
            content_type: MIME type of the content to be uploaded
            marketplace_ids: Value sent with the request.
            content_md5: MD5 hash of the content to be uploaded, encoded as base64
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Upload destination created

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.create_upload_destination_for_resource(
                resource, content_type, marketplace_ids, content_md5, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncUploadsWithRawResponse:
        return self._with_raw_response


class UploadsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_upload_destination_for_resource(
        self,
        resource: ResourceOrStr,
        content_type: ContentType1OrStr,
        marketplace_ids: list[str],
        content_md5: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateUploadDestinationResponse, CreateUploadDestinationForResourceErrorBody]:
        """Returns a pre-signed URL and upload destination ID for uploading a document for the given resource (e.g.
        feeds, reports). **Do not log the pre-signed URL — it contains temporary credentials.**

        Args:
            resource: The resource type for the upload destination (e.g. feeds)
            content_type: MIME type of the content to be uploaded
            marketplace_ids: Value sent with the request.
            content_md5: MD5 hash of the content to be uploaded, encoded as base64
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/uploads/v4/uploadDestinations/{resource}"),
            path_params=[param[ResourceOrStr]("resource", resource)],
            query_params=[
                param[ContentType1OrStr]("contentType", content_type),
                param[list[str]]("marketplaceIds", marketplace_ids),
            ],
            headers=[param[str]("contentMD5", content_md5), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateUploadDestinationResponse],
            error_mapper=create_upload_destination_for_resource_error_mapper,
            request_options=request_options,
        )


class AsyncUploadsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_upload_destination_for_resource(
        self,
        resource: ResourceOrStr,
        content_type: ContentType1OrStr,
        marketplace_ids: list[str],
        content_md5: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateUploadDestinationResponse, CreateUploadDestinationForResourceErrorBody]:
        """Returns a pre-signed URL and upload destination ID for uploading a document for the given resource (e.g.
        feeds, reports). **Do not log the pre-signed URL — it contains temporary credentials.**

        Args:
            resource: The resource type for the upload destination (e.g. feeds)
            content_type: MIME type of the content to be uploaded
            marketplace_ids: Value sent with the request.
            content_md5: MD5 hash of the content to be uploaded, encoded as base64
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/uploads/v4/uploadDestinations/{resource}"),
            path_params=[param[ResourceOrStr]("resource", resource)],
            query_params=[
                param[ContentType1OrStr]("contentType", content_type),
                param[list[str]]("marketplaceIds", marketplace_ids),
            ],
            headers=[param[str]("contentMD5", content_md5), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateUploadDestinationResponse],
            error_mapper=create_upload_destination_for_resource_error_mapper,
            request_options=request_options,
        )
