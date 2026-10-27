from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncFileResponse,
    AsyncRawClient,
    FileResponse,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    async_file_decoder,
    async_json_decoder,
    file_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.cancel_report_error import CancelReportErrorBody, cancel_report_error_mapper
from ..errors.create_report_error import CreateReportErrorBody, create_report_error_mapper
from ..errors.download_new_report_error import DownloadNewReportErrorBody, download_new_report_error_mapper
from ..errors.download_old_report_error import DownloadOldReportErrorBody, download_old_report_error_mapper
from ..errors.get_report_document_error import GetReportDocumentErrorBody, get_report_document_error_mapper
from ..errors.get_report_error import GetReportErrorBody, get_report_error_mapper
from ..errors.get_reports_error import GetReportsErrorBody, get_reports_error_mapper
from ..models.cancel_report_response import CancelReportResponse
from ..models.create_report_response import CreateReportResponse
from ..models.create_report_specification import CreateReportSpecification, CreateReportSpecificationDict
from ..models.enums.processing_status import ProcessingStatusOrStr
from ..models.enums.report_type1 import ReportType1OrStr
from ..models.get_reports_response import GetReportsResponse
from ..models.report import Report
from ..models.report_document import ReportDocument
from ..server.server import Server


class Reports:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReportsWithRawResponse(client, server, auth)

    def cancel_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelReportResponse:
        """Send a ``DELETE`` request.

        Args:
            report_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Report cancelled

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.cancel_report(report_id, request_options=request_options))

    def create_report(
        self,
        body: CreateReportSpecification | CreateReportSpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateReportResponse:
        """Submits a report request. Poll ``GET /reports/{reportId}`` for status. Report type taxonomy TBD — coordinate
        with Pod 5 for financial reports.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Report request accepted

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.create_report(body, request_options=request_options))

    def download_new_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponse:
        """Downloads the current-format settlement summary report ZIP. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/v1/reconFile (Swift v1 storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            ZIP file stream

        Raises:
            ApiError: Bad Request Not Found Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.download_new_report(partner_id, report_date, request_options=request_options)
        )

    def download_old_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponse:
        """Downloads the legacy-format settlement summary report ZIP. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/reconFile (legacy Swift storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            ZIP file stream

        Raises:
            ApiError: Bad Request Not Found Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.download_old_report(partner_id, report_date, request_options=request_options)
        )

    def get_report(self, report_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Report:
        """Send a ``GET`` request.

        Args:
            report_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_report(report_id, request_options=request_options))

    def get_report_document(
        self, report_document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReportDocument:
        """Returns a pre-signed URL for downloading the completed report. Do not log the pre-signed URL.

        Args:
            report_document_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_report_document(report_document_id, request_options=request_options))

    def get_reports(
        self,
        *,
        report_types: list[ReportType1OrStr] | None = None,
        processing_statuses: list[ProcessingStatusOrStr] | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetReportsResponse:
        """Send a ``GET`` request.

        Args:
            report_types: Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime
                availability is CCM-controlled; consult PRP docs for current PROD-enabled types.
            processing_statuses: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
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
            self._with_raw_response.get_reports(
                report_types=report_types,
                processing_statuses=processing_statuses,
                created_since=created_since,
                created_until=created_until,
                page_size=page_size,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ReportsWithRawResponse:
        return self._with_raw_response


class AsyncReports:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReportsWithRawResponse(client, server, auth)

    async def cancel_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelReportResponse:
        """Send a ``DELETE`` request.

        Args:
            report_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Report cancelled

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.cancel_report(report_id, request_options=request_options))

    async def create_report(
        self,
        body: CreateReportSpecification | CreateReportSpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateReportResponse:
        """Submits a report request. Poll ``GET /reports/{reportId}`` for status. Report type taxonomy TBD — coordinate
        with Pod 5 for financial reports.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Report request accepted

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.create_report(body, request_options=request_options))

    async def download_new_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsyncFileResponse:
        """Downloads the current-format settlement summary report ZIP. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/v1/reconFile (Swift v1 storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            ZIP file stream

        Raises:
            ApiError: Bad Request Not Found Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.download_new_report(partner_id, report_date, request_options=request_options)
        )

    async def download_old_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsyncFileResponse:
        """Downloads the legacy-format settlement summary report ZIP. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/reconFile (legacy Swift storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            ZIP file stream

        Raises:
            ApiError: Bad Request Not Found Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.download_old_report(partner_id, report_date, request_options=request_options)
        )

    async def get_report(self, report_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Report:
        """Send a ``GET`` request.

        Args:
            report_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(await self._with_raw_response.get_report(report_id, request_options=request_options))

    async def get_report_document(
        self, report_document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReportDocument:
        """Returns a pre-signed URL for downloading the completed report. Do not log the pre-signed URL.

        Args:
            report_document_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_report_document(report_document_id, request_options=request_options)
        )

    async def get_reports(
        self,
        *,
        report_types: list[ReportType1OrStr] | None = None,
        processing_statuses: list[ProcessingStatusOrStr] | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetReportsResponse:
        """Send a ``GET`` request.

        Args:
            report_types: Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime
                availability is CCM-controlled; consult PRP docs for current PROD-enabled types.
            processing_statuses: Value sent with the request.
            created_since: Value sent with the request.
            created_until: Value sent with the request.
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
            await self._with_raw_response.get_reports(
                report_types=report_types,
                processing_statuses=processing_statuses,
                created_since=created_since,
                created_until=created_until,
                page_size=page_size,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncReportsWithRawResponse:
        return self._with_raw_response


class ReportsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelReportResponse, CancelReportErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            report_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/reports/v4/reports/{reportId}"),
            path_params=[param[str]("reportId", report_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelReportResponse],
            error_mapper=cancel_report_error_mapper,
            request_options=request_options,
        )

    def create_report(
        self,
        body: CreateReportSpecification | CreateReportSpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateReportResponse, CreateReportErrorBody]:
        """Submits a report request. Poll ``GET /reports/{reportId}`` for status. Report type taxonomy TBD — coordinate
        with Pod 5 for financial reports.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/reports/v4/reports"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateReportSpecification | CreateReportSpecificationDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateReportResponse],
            error_mapper=create_report_error_mapper,
            request_options=request_options,
        )

    def download_new_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponse, DownloadNewReportErrorBody]:
        """Downloads the current-format settlement summary report ZIP. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/v1/reconFile (Swift v1 storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/summary/newReportDownload"),
            query_params=[param[str]("partnerId", partner_id), param[str]("reportDate", report_date)],
            auth_scheme=self._auth.wallet_auth,
            decoder=file_decoder,
            error_mapper=download_new_report_error_mapper,
            request_options=request_options,
        )

    def download_old_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponse, DownloadOldReportErrorBody]:
        """Downloads the legacy-format settlement summary report ZIP. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/reconFile (legacy Swift storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/summary/oldReportDownload"),
            query_params=[param[str]("partnerId", partner_id), param[str]("reportDate", report_date)],
            auth_scheme=self._auth.wallet_auth,
            decoder=file_decoder,
            error_mapper=download_old_report_error_mapper,
            request_options=request_options,
        )

    def get_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Report, GetReportErrorBody]:
        """Send a ``GET`` request.

        Args:
            report_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/reports/v4/reports/{reportId}"),
            path_params=[param[str]("reportId", report_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Report],
            error_mapper=get_report_error_mapper,
            request_options=request_options,
        )

    def get_report_document(
        self, report_document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReportDocument, GetReportDocumentErrorBody]:
        """Returns a pre-signed URL for downloading the completed report. Do not log the pre-signed URL.

        Args:
            report_document_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/reports/v4/documents/{reportDocumentId}"),
            path_params=[param[str]("reportDocumentId", report_document_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ReportDocument],
            error_mapper=get_report_document_error_mapper,
            request_options=request_options,
        )

    def get_reports(
        self,
        *,
        report_types: list[ReportType1OrStr] | None = None,
        processing_statuses: list[ProcessingStatusOrStr] | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetReportsResponse, GetReportsErrorBody]:
        """Send a ``GET`` request.

        Args:
            report_types: Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime
                availability is CCM-controlled; consult PRP docs for current PROD-enabled types.
            processing_statuses: Value sent with the request.
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
            url_template=self._server.default1("/reports/v4/reports"),
            query_params=[
                param[list[ReportType1OrStr] | None]("reportTypes", report_types),
                param[list[ProcessingStatusOrStr] | None]("processingStatuses", processing_statuses),
                param[RFC3339DateTime | None]("createdSince", created_since),
                param[RFC3339DateTime | None]("createdUntil", created_until),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetReportsResponse],
            error_mapper=get_reports_error_mapper,
            request_options=request_options,
        )


class AsyncReportsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelReportResponse, CancelReportErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            report_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/reports/v4/reports/{reportId}"),
            path_params=[param[str]("reportId", report_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelReportResponse],
            error_mapper=cancel_report_error_mapper,
            request_options=request_options,
        )

    async def create_report(
        self,
        body: CreateReportSpecification | CreateReportSpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateReportResponse, CreateReportErrorBody]:
        """Submits a report request. Poll ``GET /reports/{reportId}`` for status. Report type taxonomy TBD — coordinate
        with Pod 5 for financial reports.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/reports/v4/reports"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateReportSpecification | CreateReportSpecificationDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateReportResponse],
            error_mapper=create_report_error_mapper,
            request_options=request_options,
        )

    async def download_new_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsyncFileResponse, DownloadNewReportErrorBody]:
        """Downloads the current-format settlement summary report ZIP. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/v1/reconFile (Swift v1 storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/summary/newReportDownload"),
            query_params=[param[str]("partnerId", partner_id), param[str]("reportDate", report_date)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_file_decoder,
            error_mapper=download_new_report_error_mapper,
            request_options=request_options,
        )

    async def download_old_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsyncFileResponse, DownloadOldReportErrorBody]:
        """Downloads the legacy-format settlement summary report ZIP. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/reconFile (legacy Swift storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/summary/oldReportDownload"),
            query_params=[param[str]("partnerId", partner_id), param[str]("reportDate", report_date)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_file_decoder,
            error_mapper=download_old_report_error_mapper,
            request_options=request_options,
        )

    async def get_report(
        self, report_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Report, GetReportErrorBody]:
        """Send a ``GET`` request.

        Args:
            report_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/reports/v4/reports/{reportId}"),
            path_params=[param[str]("reportId", report_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Report],
            error_mapper=get_report_error_mapper,
            request_options=request_options,
        )

    async def get_report_document(
        self, report_document_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReportDocument, GetReportDocumentErrorBody]:
        """Returns a pre-signed URL for downloading the completed report. Do not log the pre-signed URL.

        Args:
            report_document_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/reports/v4/documents/{reportDocumentId}"),
            path_params=[param[str]("reportDocumentId", report_document_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ReportDocument],
            error_mapper=get_report_document_error_mapper,
            request_options=request_options,
        )

    async def get_reports(
        self,
        *,
        report_types: list[ReportType1OrStr] | None = None,
        processing_statuses: list[ProcessingStatusOrStr] | None = None,
        created_since: RFC3339DateTime | None = None,
        created_until: RFC3339DateTime | None = None,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetReportsResponse, GetReportsErrorBody]:
        """Send a ``GET`` request.

        Args:
            report_types: Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime
                availability is CCM-controlled; consult PRP docs for current PROD-enabled types.
            processing_statuses: Value sent with the request.
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
            url_template=self._server.default1("/reports/v4/reports"),
            query_params=[
                param[list[ReportType1OrStr] | None]("reportTypes", report_types),
                param[list[ProcessingStatusOrStr] | None]("processingStatuses", processing_statuses),
                param[RFC3339DateTime | None]("createdSince", created_since),
                param[RFC3339DateTime | None]("createdUntil", created_until),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetReportsResponse],
            error_mapper=get_reports_error_mapper,
            request_options=request_options,
        )
