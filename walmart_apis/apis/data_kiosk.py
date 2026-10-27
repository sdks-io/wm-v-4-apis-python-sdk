from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.cancel_query_error import CancelQueryErrorBody, cancel_query_error_mapper
from ..errors.create_query_error import CreateQueryErrorBody, create_query_error_mapper
from ..errors.get_document_error import GetDocumentErrorBody, get_document_error_mapper
from ..errors.get_queries_error import GetQueriesErrorBody, get_queries_error_mapper
from ..errors.get_query_error import GetQueryErrorBody, get_query_error_mapper
from ..models.cancel_query_response import CancelQueryResponse
from ..models.create_query_response import CreateQueryResponse
from ..models.create_query_specification import CreateQuerySpecification, CreateQuerySpecificationDict
from ..models.document import Document
from ..models.enums.processing_status import ProcessingStatusOrStr
from ..models.get_queries_response import GetQueriesResponse
from ..models.query import Query
from ..server.server import Server


class DataKiosk:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DataKioskWithRawResponse(client, server, auth)

    def cancel_query(
        self, query_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelQueryResponse:
        """Send a ``DELETE`` request.

        Args:
            query_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Query cancellation accepted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.cancel_query(query_id, request_options=request_options))

    def create_query(
        self,
        body: CreateQuerySpecification | CreateQuerySpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateQueryResponse:
        """Submits a structured query for async processing. Query language TBD pending ADR (GraphQL vs REST hybrid — Pod
        4).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Query request accepted for processing

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.create_query(body, request_options=request_options))

    def get_document(self, document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Document:
        """Returns a pre-signed URL for downloading query result data. Do not log the pre-signed URL.

        Args:
            document_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_document(document_id, request_options=request_options))

    def get_queries(
        self,
        *,
        processing_statuses: list[ProcessingStatusOrStr] | None = None,
        page_size: int | None = 10,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetQueriesResponse:
        """Returns a paginated list of Data Kiosk queries submitted by the seller, optionally filtered by processing
        status and creation date range.

        Args:
            processing_statuses: Value sent with the request.
            page_size: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
            pagination_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_queries(
                processing_statuses=processing_statuses,
                page_size=page_size,
                created_since=created_since,
                created_until=created_until,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    def get_query(self, query_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Query:
        """Send a ``GET`` request.

        Args:
            query_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_query(query_id, request_options=request_options))

    @property
    def with_raw_response(self) -> DataKioskWithRawResponse:
        return self._with_raw_response


class AsyncDataKiosk:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDataKioskWithRawResponse(client, server, auth)

    async def cancel_query(
        self, query_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelQueryResponse:
        """Send a ``DELETE`` request.

        Args:
            query_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Query cancellation accepted

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.cancel_query(query_id, request_options=request_options))

    async def create_query(
        self,
        body: CreateQuerySpecification | CreateQuerySpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateQueryResponse:
        """Submits a structured query for async processing. Query language TBD pending ADR (GraphQL vs REST hybrid — Pod
        4).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Query request accepted for processing

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.create_query(body, request_options=request_options))

    async def get_document(self, document_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Document:
        """Returns a pre-signed URL for downloading query result data. Do not log the pre-signed URL.

        Args:
            document_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.get_document(document_id, request_options=request_options))

    async def get_queries(
        self,
        *,
        processing_statuses: list[ProcessingStatusOrStr] | None = None,
        page_size: int | None = 10,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetQueriesResponse:
        """Returns a paginated list of Data Kiosk queries submitted by the seller, optionally filtered by processing
        status and creation date range.

        Args:
            processing_statuses: Value sent with the request.
            page_size: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
            pagination_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_queries(
                processing_statuses=processing_statuses,
                page_size=page_size,
                created_since=created_since,
                created_until=created_until,
                pagination_token=pagination_token,
                request_options=request_options,
            ),
        )

    async def get_query(self, query_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Query:
        """Send a ``GET`` request.

        Args:
            query_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.get_query(query_id, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncDataKioskWithRawResponse:
        return self._with_raw_response


class DataKioskWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_query(
        self, query_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelQueryResponse, CancelQueryErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            query_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/data-kiosk/v4/queries/{queryId}"),
            path_params=[param[str]("queryId", query_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelQueryResponse],
            error_mapper=cancel_query_error_mapper,
            request_options=request_options,
        )

    def create_query(
        self,
        body: CreateQuerySpecification | CreateQuerySpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateQueryResponse, CreateQueryErrorBody]:
        """Submits a structured query for async processing. Query language TBD pending ADR (GraphQL vs REST hybrid — Pod
        4).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/data-kiosk/v4/queries"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateQuerySpecification | CreateQuerySpecificationDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateQueryResponse],
            error_mapper=create_query_error_mapper,
            request_options=request_options,
        )

    def get_document(
        self, document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Document, GetDocumentErrorBody]:
        """Returns a pre-signed URL for downloading query result data. Do not log the pre-signed URL.

        Args:
            document_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/data-kiosk/v4/documents/{documentId}"),
            path_params=[param[str]("documentId", document_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Document],
            error_mapper=get_document_error_mapper,
            request_options=request_options,
        )

    def get_queries(
        self,
        *,
        processing_statuses: list[ProcessingStatusOrStr] | None = None,
        page_size: int | None = 10,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetQueriesResponse, GetQueriesErrorBody]:
        """Returns a paginated list of Data Kiosk queries submitted by the seller, optionally filtered by processing
        status and creation date range.

        Args:
            processing_statuses: Value sent with the request.
            page_size: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
            pagination_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/data-kiosk/v4/queries"),
            query_params=[
                param[list[ProcessingStatusOrStr] | None]("processingStatuses", processing_statuses),
                param[int | None]("pageSize", page_size),
                param[RFC3339DateTime | None]("createdSince", created_since),
                param[RFC3339DateTime | None]("createdUntil", created_until),
                param[str | None]("paginationToken", pagination_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetQueriesResponse],
            error_mapper=get_queries_error_mapper,
            request_options=request_options,
        )

    def get_query(
        self, query_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Query, GetQueryErrorBody]:
        """Send a ``GET`` request.

        Args:
            query_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/data-kiosk/v4/queries/{queryId}"),
            path_params=[param[str]("queryId", query_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Query],
            error_mapper=get_query_error_mapper,
            request_options=request_options,
        )


class AsyncDataKioskWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_query(
        self, query_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelQueryResponse, CancelQueryErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            query_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/data-kiosk/v4/queries/{queryId}"),
            path_params=[param[str]("queryId", query_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelQueryResponse],
            error_mapper=cancel_query_error_mapper,
            request_options=request_options,
        )

    async def create_query(
        self,
        body: CreateQuerySpecification | CreateQuerySpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateQueryResponse, CreateQueryErrorBody]:
        """Submits a structured query for async processing. Query language TBD pending ADR (GraphQL vs REST hybrid — Pod
        4).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/data-kiosk/v4/queries"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateQuerySpecification | CreateQuerySpecificationDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateQueryResponse],
            error_mapper=create_query_error_mapper,
            request_options=request_options,
        )

    async def get_document(
        self, document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Document, GetDocumentErrorBody]:
        """Returns a pre-signed URL for downloading query result data. Do not log the pre-signed URL.

        Args:
            document_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/data-kiosk/v4/documents/{documentId}"),
            path_params=[param[str]("documentId", document_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Document],
            error_mapper=get_document_error_mapper,
            request_options=request_options,
        )

    async def get_queries(
        self,
        *,
        processing_statuses: list[ProcessingStatusOrStr] | None = None,
        page_size: int | None = 10,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        pagination_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetQueriesResponse, GetQueriesErrorBody]:
        """Returns a paginated list of Data Kiosk queries submitted by the seller, optionally filtered by processing
        status and creation date range.

        Args:
            processing_statuses: Value sent with the request.
            page_size: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
            pagination_token: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/data-kiosk/v4/queries"),
            query_params=[
                param[list[ProcessingStatusOrStr] | None]("processingStatuses", processing_statuses),
                param[int | None]("pageSize", page_size),
                param[RFC3339DateTime | None]("createdSince", created_since),
                param[RFC3339DateTime | None]("createdUntil", created_until),
                param[str | None]("paginationToken", pagination_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetQueriesResponse],
            error_mapper=get_queries_error_mapper,
            request_options=request_options,
        )

    async def get_query(
        self, query_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Query, GetQueryErrorBody]:
        """Send a ``GET`` request.

        Args:
            query_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/data-kiosk/v4/queries/{queryId}"),
            path_params=[param[str]("queryId", query_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Query],
            error_mapper=get_query_error_mapper,
            request_options=request_options,
        )
