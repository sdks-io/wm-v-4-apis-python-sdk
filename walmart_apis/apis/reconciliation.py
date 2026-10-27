from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncFileResponse,
    AsyncRawClient,
    Date,
    FileResponse,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_file_decoder,
    async_json_decoder,
    file_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.check_download_report_by_period_error import (
    CheckDownloadReportByPeriodErrorBody,
    check_download_report_by_period_error_mapper,
)
from ..errors.download_reconciliation_report_error import (
    DownloadReconciliationReportErrorBody,
    download_reconciliation_report_error_mapper,
)
from ..errors.list_reconciliation_dates_error import (
    ListReconciliationDatesErrorBody,
    list_reconciliation_dates_error_mapper,
)
from ..models.report_availability_response import ReportAvailabilityResponse
from ..server.server import Server


class Reconciliation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReconciliationWithRawResponse(client, server, auth)

    def check_download_report_by_period(
        self, partner_id: str, date: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReportAvailabilityResponse:
        """Checks which reconciliation report versions (legacy, v1/WFS) are available for a given partner and date.
        Delegates to mp-payment-reporting GET /v3/report/reconreport/reconReportAvailability. Note: the upstream date
        param is named ``date`` (not ``reportDate``).

        Args:
            partner_id: Numeric partner/seller ID
            date: Report date in yyyy-MM-dd format
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.check_download_report_by_period(partner_id, date, request_options=request_options)
        )

    def download_reconciliation_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FileResponse:
        """Downloads a reconciliation report ZIP for the given partner and date. Delegates to mp-payment-reporting GET
        /v1/mt/report/reconreport/reconFile (Azure MT storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            ZIP file stream

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Not Found Internal Server
                Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.download_reconciliation_report(
                partner_id, report_date, request_options=request_options
            ),
        )

    def list_reconciliation_dates(
        self, partner_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReportAvailabilityResponse:
        """Returns the set of available reconciliation report dates for a partner. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/availableReconFiles.

        Args:
            partner_id: Numeric partner/seller ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.list_reconciliation_dates(partner_id, request_options=request_options))

    @property
    def with_raw_response(self) -> ReconciliationWithRawResponse:
        return self._with_raw_response


class AsyncReconciliation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReconciliationWithRawResponse(client, server, auth)

    async def check_download_report_by_period(
        self, partner_id: str, date: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReportAvailabilityResponse:
        """Checks which reconciliation report versions (legacy, v1/WFS) are available for a given partner and date.
        Delegates to mp-payment-reporting GET /v3/report/reconreport/reconReportAvailability. Note: the upstream date
        param is named ``date`` (not ``reportDate``).

        Args:
            partner_id: Numeric partner/seller ID
            date: Report date in yyyy-MM-dd format
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.check_download_report_by_period(
                partner_id, date, request_options=request_options
            ),
        )

    async def download_reconciliation_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AsyncFileResponse:
        """Downloads a reconciliation report ZIP for the given partner and date. Delegates to mp-payment-reporting GET
        /v1/mt/report/reconreport/reconFile (Azure MT storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            ZIP file stream

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Not Found Internal Server
                Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.download_reconciliation_report(
                partner_id, report_date, request_options=request_options
            ),
        )

    async def list_reconciliation_dates(
        self, partner_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReportAvailabilityResponse:
        """Returns the set of available reconciliation report dates for a partner. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/availableReconFiles.

        Args:
            partner_id: Numeric partner/seller ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_reconciliation_dates(partner_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncReconciliationWithRawResponse:
        return self._with_raw_response


class ReconciliationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_download_report_by_period(
        self, partner_id: str, date: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReportAvailabilityResponse, CheckDownloadReportByPeriodErrorBody]:
        """Checks which reconciliation report versions (legacy, v1/WFS) are available for a given partner and date.
        Delegates to mp-payment-reporting GET /v3/report/reconreport/reconReportAvailability. Note: the upstream date
        param is named ``date`` (not ``reportDate``).

        Args:
            partner_id: Numeric partner/seller ID
            date: Report date in yyyy-MM-dd format
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/checkDownloadReportByPeriod"),
            query_params=[param[str]("partnerId", partner_id), param[Date]("date", date)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ReportAvailabilityResponse],
            error_mapper=check_download_report_by_period_error_mapper,
            request_options=request_options,
        )

    def download_reconciliation_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FileResponse, DownloadReconciliationReportErrorBody]:
        """Downloads a reconciliation report ZIP for the given partner and date. Delegates to mp-payment-reporting GET
        /v1/mt/report/reconreport/reconFile (Azure MT storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/reconciliation/download"),
            query_params=[param[str]("partnerId", partner_id), param[str]("reportDate", report_date)],
            auth_scheme=self._auth.wallet_auth,
            decoder=file_decoder,
            error_mapper=download_reconciliation_report_error_mapper,
            request_options=request_options,
        )

    def list_reconciliation_dates(
        self, partner_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReportAvailabilityResponse, ListReconciliationDatesErrorBody]:
        """Returns the set of available reconciliation report dates for a partner. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/availableReconFiles.

        Args:
            partner_id: Numeric partner/seller ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/reconciliation/dateList"),
            query_params=[param[str]("partnerId", partner_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ReportAvailabilityResponse],
            error_mapper=list_reconciliation_dates_error_mapper,
            request_options=request_options,
        )


class AsyncReconciliationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_download_report_by_period(
        self, partner_id: str, date: Date, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReportAvailabilityResponse, CheckDownloadReportByPeriodErrorBody]:
        """Checks which reconciliation report versions (legacy, v1/WFS) are available for a given partner and date.
        Delegates to mp-payment-reporting GET /v3/report/reconreport/reconReportAvailability. Note: the upstream date
        param is named ``date`` (not ``reportDate``).

        Args:
            partner_id: Numeric partner/seller ID
            date: Report date in yyyy-MM-dd format
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/checkDownloadReportByPeriod"),
            query_params=[param[str]("partnerId", partner_id), param[Date]("date", date)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ReportAvailabilityResponse],
            error_mapper=check_download_report_by_period_error_mapper,
            request_options=request_options,
        )

    async def download_reconciliation_report(
        self, partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AsyncFileResponse, DownloadReconciliationReportErrorBody]:
        """Downloads a reconciliation report ZIP for the given partner and date. Delegates to mp-payment-reporting GET
        /v1/mt/report/reconreport/reconFile (Azure MT storage).

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the body unread or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/reconciliation/download"),
            query_params=[param[str]("partnerId", partner_id), param[str]("reportDate", report_date)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_file_decoder,
            error_mapper=download_reconciliation_report_error_mapper,
            request_options=request_options,
        )

    async def list_reconciliation_dates(
        self, partner_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReportAvailabilityResponse, ListReconciliationDatesErrorBody]:
        """Returns the set of available reconciliation report dates for a partner. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/availableReconFiles.

        Args:
            partner_id: Numeric partner/seller ID
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/reconciliation/dateList"),
            query_params=[param[str]("partnerId", partner_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ReportAvailabilityResponse],
            error_mapper=list_reconciliation_dates_error_mapper,
            request_options=request_options,
        )
