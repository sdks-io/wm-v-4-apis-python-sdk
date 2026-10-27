from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    RFC3339DateTime,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.list_settlement_details_error import ListSettlementDetailsErrorBody, list_settlement_details_error_mapper
from ..errors.list_settlement_periods_error import ListSettlementPeriodsErrorBody, list_settlement_periods_error_mapper
from ..errors.search_transactions_error import SearchTransactionsErrorBody, search_transactions_error_mapper
from ..models.settlement_details_response import SettlementDetailsResponse
from ..models.settlement_periods_response import SettlementPeriodsResponse
from ..models.transaction_search_response import TransactionSearchResponse
from ..server.server import Server


class Settlement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SettlementWithRawResponse(client, server, auth)

    def list_settlement_details(
        self,
        partner_id: str,
        report_date: str,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SettlementDetailsResponse:
        """Returns paginated settlement transaction detail for the given partner and report date. Contains PII (purchase
        order IDs). Delegates to mp-payment-reporting GET /v3/report/reconreport/v1/getJson with offset-based
        pagination. nextToken is a Base64-encoded offset into the report file.

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Forbidden Rate limit exceeded
                Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_settlement_details(
                partner_id, report_date, page_size=page_size, next_token=next_token, request_options=request_options
            ),
        )

    def list_settlement_periods(
        self,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SettlementPeriodsResponse:
        """Returns available settlement period dates for the authenticated seller. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/v1/availableReconFiles.

        Args:
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Forbidden Rate limit exceeded
                Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.list_settlement_periods(
                page_size=page_size, next_token=next_token, request_options=request_options
            ),
        )

    def search_transactions(
        self,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionSearchResponse:
        """Returns a paginated list of payment transactions for the authenticated seller filtered by optional date
        range. Contains PII (purchase order IDs). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            posted_after: Value sent with the request.
            posted_before: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            self._with_raw_response.search_transactions(
                page_size=page_size,
                next_token=next_token,
                posted_after=posted_after,
                posted_before=posted_before,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SettlementWithRawResponse:
        return self._with_raw_response


class AsyncSettlement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSettlementWithRawResponse(client, server, auth)

    async def list_settlement_details(
        self,
        partner_id: str,
        report_date: str,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SettlementDetailsResponse:
        """Returns paginated settlement transaction detail for the given partner and report date. Contains PII (purchase
        order IDs). Delegates to mp-payment-reporting GET /v3/report/reconreport/v1/getJson with offset-based
        pagination. nextToken is a Base64-encoded offset into the report file.

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Forbidden Rate limit exceeded
                Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_settlement_details(
                partner_id, report_date, page_size=page_size, next_token=next_token, request_options=request_options
            ),
        )

    async def list_settlement_periods(
        self,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SettlementPeriodsResponse:
        """Returns available settlement period dates for the authenticated seller. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/v1/availableReconFiles.

        Args:
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Forbidden Rate limit exceeded
                Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.list_settlement_periods(
                page_size=page_size, next_token=next_token, request_options=request_options
            ),
        )

    async def search_transactions(
        self,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TransactionSearchResponse:
        """Returns a paginated list of payment transactions for the authenticated seller filtered by optional date
        range. Contains PII (purchase order IDs). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            posted_after: Value sent with the request.
            posted_before: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.search_transactions(
                page_size=page_size,
                next_token=next_token,
                posted_after=posted_after,
                posted_before=posted_before,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSettlementWithRawResponse:
        return self._with_raw_response


class SettlementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_settlement_details(
        self,
        partner_id: str,
        report_date: str,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SettlementDetailsResponse, ListSettlementDetailsErrorBody]:
        """Returns paginated settlement transaction detail for the given partner and report date. Contains PII (purchase
        order IDs). Delegates to mp-payment-reporting GET /v3/report/reconreport/v1/getJson with offset-based
        pagination. nextToken is a Base64-encoded offset into the report file.

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/settlementDetails"),
            query_params=[
                param[str]("partnerId", partner_id),
                param[str]("reportDate", report_date),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[SettlementDetailsResponse],
            error_mapper=list_settlement_details_error_mapper,
            request_options=request_options,
        )

    def list_settlement_periods(
        self,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SettlementPeriodsResponse, ListSettlementPeriodsErrorBody]:
        """Returns available settlement period dates for the authenticated seller. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/v1/availableReconFiles.

        Args:
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/settlementPeriods"),
            query_params=[param[int | None]("pageSize", page_size), param[str | None]("nextToken", next_token)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[SettlementPeriodsResponse],
            error_mapper=list_settlement_periods_error_mapper,
            request_options=request_options,
        )

    def search_transactions(
        self,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionSearchResponse, SearchTransactionsErrorBody]:
        """Returns a paginated list of payment transactions for the authenticated seller filtered by optional date
        range. Contains PII (purchase order IDs). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            posted_after: Value sent with the request.
            posted_before: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/search/transactions"),
            query_params=[
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
                param[RFC3339DateTime | None]("postedAfter", posted_after),
                param[RFC3339DateTime | None]("postedBefore", posted_before),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[TransactionSearchResponse],
            error_mapper=search_transactions_error_mapper,
            request_options=request_options,
        )


class AsyncSettlementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_settlement_details(
        self,
        partner_id: str,
        report_date: str,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SettlementDetailsResponse, ListSettlementDetailsErrorBody]:
        """Returns paginated settlement transaction detail for the given partner and report date. Contains PII (purchase
        order IDs). Delegates to mp-payment-reporting GET /v3/report/reconreport/v1/getJson with offset-based
        pagination. nextToken is a Base64-encoded offset into the report file.

        Args:
            partner_id: Numeric partner/seller ID
            report_date: Report date in MMddyyyy format (e.g. 06172026)
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/settlementDetails"),
            query_params=[
                param[str]("partnerId", partner_id),
                param[str]("reportDate", report_date),
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[SettlementDetailsResponse],
            error_mapper=list_settlement_details_error_mapper,
            request_options=request_options,
        )

    async def list_settlement_periods(
        self,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SettlementPeriodsResponse, ListSettlementPeriodsErrorBody]:
        """Returns available settlement period dates for the authenticated seller. Delegates to mp-payment-reporting GET
        /v3/report/reconreport/v1/availableReconFiles.

        Args:
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/settlementPeriods"),
            query_params=[param[int | None]("pageSize", page_size), param[str | None]("nextToken", next_token)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[SettlementPeriodsResponse],
            error_mapper=list_settlement_periods_error_mapper,
            request_options=request_options,
        )

    async def search_transactions(
        self,
        *,
        page_size: int | None = 10,
        next_token: str | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TransactionSearchResponse, SearchTransactionsErrorBody]:
        """Returns a paginated list of payment transactions for the authenticated seller filtered by optional date
        range. Contains PII (purchase order IDs). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            page_size: Value sent with the request.
            next_token: Opaque cursor from a prior response; omit for first page
            posted_after: Value sent with the request.
            posted_before: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/search/transactions"),
            query_params=[
                param[int | None]("pageSize", page_size),
                param[str | None]("nextToken", next_token),
                param[RFC3339DateTime | None]("postedAfter", posted_after),
                param[RFC3339DateTime | None]("postedBefore", posted_before),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[TransactionSearchResponse],
            error_mapper=search_transactions_error_mapper,
            request_options=request_options,
        )
