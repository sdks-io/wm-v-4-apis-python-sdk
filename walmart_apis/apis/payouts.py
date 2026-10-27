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
from ..errors.configure_auto_payout_error import ConfigureAutoPayoutErrorBody, configure_auto_payout_error_mapper
from ..errors.get_annual_statement_opts_error import (
    GetAnnualStatementOptsErrorBody,
    get_annual_statement_opts_error_mapper,
)
from ..errors.get_faster_payout_eligibility_error import (
    GetFasterPayoutEligibilityErrorBody,
    get_faster_payout_eligibility_error_mapper,
)
from ..errors.get_payment_status_error import GetPaymentStatusErrorBody, get_payment_status_error_mapper
from ..errors.initiate_faster_payout_error import InitiateFasterPayoutErrorBody, initiate_faster_payout_error_mapper
from ..models.annual_statement_opts_response import AnnualStatementOptsResponse
from ..models.disbursements_v4_payment_auto_payout_request import (
    DisbursementsV4PaymentAutoPayoutRequest,
    DisbursementsV4PaymentAutoPayoutRequestDict,
)
from ..models.faster_payout_eligibility_response import FasterPayoutEligibilityResponse
from ..models.initiate_payout_response import InitiatePayoutResponse
from ..models.payout_status_response import PayoutStatusResponse
from ..server.server import Server


class Payouts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PayoutsWithRawResponse(client, server, auth)

    def configure_auto_payout(
        self,
        body: DisbursementsV4PaymentAutoPayoutRequest | DisbursementsV4PaymentAutoPayoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutStatusResponse:
        """Enables or disables automatic scheduled payouts for the authenticated seller. When enabled, payouts are
        triggered automatically on the standard settlement cadence. Returns updated payout status. Requires
        disbursements:write scope. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.configure_auto_payout(body, request_options=request_options))

    def get_annual_statement_opts(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnnualStatementOptsResponse:
        """Returns whether the authenticated seller is opted in to annual statement generation and the current statement
        year. Delegates to GMPPaymentsPlatform GET /annualStatementOpts/{partnerId}.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_annual_statement_opts(request_options=request_options))

    def get_faster_payout_eligibility(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> FasterPayoutEligibilityResponse:
        """Returns whether the authenticated seller is eligible for an on-demand faster payout, along with the approved
        amount and any ineligibility reason. Delegates to GMPPaymentsPlatform GET /fasterPayout/eligibility/{partnerId}.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_faster_payout_eligibility(request_options=request_options))

    def get_payment_status(self, *, request_options: RequestOptionsOrDict | None = None) -> PayoutStatusResponse:
        """Returns the current payout status for the authenticated seller, including scheduled payout date, amount, and
        lifecycle state (Pending, Processing, Completed, Failed, OnHold). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_payment_status(request_options=request_options))

    def initiate_faster_payout(self, *, request_options: RequestOptionsOrDict | None = None) -> InitiatePayoutResponse:
        """Triggers an immediate on-demand payout for the authenticated seller, bypassing the standard settlement
        schedule. Returns the payout ID and initial status. Requires disbursements:write scope. Delegates to
        GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Payout initiated

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Conflict — resource state
                prevents this operation Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.initiate_faster_payout(request_options=request_options))

    @property
    def with_raw_response(self) -> PayoutsWithRawResponse:
        return self._with_raw_response


class AsyncPayouts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPayoutsWithRawResponse(client, server, auth)

    async def configure_auto_payout(
        self,
        body: DisbursementsV4PaymentAutoPayoutRequest | DisbursementsV4PaymentAutoPayoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayoutStatusResponse:
        """Enables or disables automatic scheduled payouts for the authenticated seller. When enabled, payouts are
        triggered automatically on the standard settlement cadence. Returns updated payout status. Requires
        disbursements:write scope. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.configure_auto_payout(body, request_options=request_options))

    async def get_annual_statement_opts(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> AnnualStatementOptsResponse:
        """Returns whether the authenticated seller is opted in to annual statement generation and the current statement
        year. Delegates to GMPPaymentsPlatform GET /annualStatementOpts/{partnerId}.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.get_annual_statement_opts(request_options=request_options))

    async def get_faster_payout_eligibility(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> FasterPayoutEligibilityResponse:
        """Returns whether the authenticated seller is eligible for an on-demand faster payout, along with the approved
        amount and any ineligibility reason. Delegates to GMPPaymentsPlatform GET /fasterPayout/eligibility/{partnerId}.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.get_faster_payout_eligibility(request_options=request_options))

    async def get_payment_status(self, *, request_options: RequestOptionsOrDict | None = None) -> PayoutStatusResponse:
        """Returns the current payout status for the authenticated seller, including scheduled payout date, amount, and
        lifecycle state (Pending, Processing, Completed, Failed, OnHold). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.get_payment_status(request_options=request_options))

    async def initiate_faster_payout(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> InitiatePayoutResponse:
        """Triggers an immediate on-demand payout for the authenticated seller, bypassing the standard settlement
        schedule. Returns the payout ID and initial status. Requires disbursements:write scope. Delegates to
        GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Payout initiated

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Conflict — resource state
                prevents this operation Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.initiate_faster_payout(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncPayoutsWithRawResponse:
        return self._with_raw_response


class PayoutsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def configure_auto_payout(
        self,
        body: DisbursementsV4PaymentAutoPayoutRequest | DisbursementsV4PaymentAutoPayoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutStatusResponse, ConfigureAutoPayoutErrorBody]:
        """Enables or disables automatic scheduled payouts for the authenticated seller. When enabled, payouts are
        triggered automatically on the standard settlement cadence. Returns updated payout status. Requires
        disbursements:write scope. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/disbursements/v4/payment/autoPayout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisbursementsV4PaymentAutoPayoutRequest | DisbursementsV4PaymentAutoPayoutRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[PayoutStatusResponse],
            error_mapper=configure_auto_payout_error_mapper,
            request_options=request_options,
        )

    def get_annual_statement_opts(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnnualStatementOptsResponse, GetAnnualStatementOptsErrorBody]:
        """Returns whether the authenticated seller is opted in to annual statement generation and the current statement
        year. Delegates to GMPPaymentsPlatform GET /annualStatementOpts/{partnerId}.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/annualStatementOpts"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[AnnualStatementOptsResponse],
            error_mapper=get_annual_statement_opts_error_mapper,
            request_options=request_options,
        )

    def get_faster_payout_eligibility(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FasterPayoutEligibilityResponse, GetFasterPayoutEligibilityErrorBody]:
        """Returns whether the authenticated seller is eligible for an on-demand faster payout, along with the approved
        amount and any ineligibility reason. Delegates to GMPPaymentsPlatform GET /fasterPayout/eligibility/{partnerId}.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/fasterPayoutEligibility"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[FasterPayoutEligibilityResponse],
            error_mapper=get_faster_payout_eligibility_error_mapper,
            request_options=request_options,
        )

    def get_payment_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PayoutStatusResponse, GetPaymentStatusErrorBody]:
        """Returns the current payout status for the authenticated seller, including scheduled payout date, amount, and
        lifecycle state (Pending, Processing, Completed, Failed, OnHold). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/paymentstatus"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[PayoutStatusResponse],
            error_mapper=get_payment_status_error_mapper,
            request_options=request_options,
        )

    def initiate_faster_payout(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InitiatePayoutResponse, InitiateFasterPayoutErrorBody]:
        """Triggers an immediate on-demand payout for the authenticated seller, bypassing the standard settlement
        schedule. Returns the payout ID and initial status. Requires disbursements:write scope. Delegates to
        GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/disbursements/v4/payment/fasterPayout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[InitiatePayoutResponse],
            error_mapper=initiate_faster_payout_error_mapper,
            request_options=request_options,
        )


class AsyncPayoutsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def configure_auto_payout(
        self,
        body: DisbursementsV4PaymentAutoPayoutRequest | DisbursementsV4PaymentAutoPayoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayoutStatusResponse, ConfigureAutoPayoutErrorBody]:
        """Enables or disables automatic scheduled payouts for the authenticated seller. When enabled, payouts are
        triggered automatically on the standard settlement cadence. Returns updated payout status. Requires
        disbursements:write scope. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/disbursements/v4/payment/autoPayout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DisbursementsV4PaymentAutoPayoutRequest | DisbursementsV4PaymentAutoPayoutRequestDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[PayoutStatusResponse],
            error_mapper=configure_auto_payout_error_mapper,
            request_options=request_options,
        )

    async def get_annual_statement_opts(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AnnualStatementOptsResponse, GetAnnualStatementOptsErrorBody]:
        """Returns whether the authenticated seller is opted in to annual statement generation and the current statement
        year. Delegates to GMPPaymentsPlatform GET /annualStatementOpts/{partnerId}.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/annualStatementOpts"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[AnnualStatementOptsResponse],
            error_mapper=get_annual_statement_opts_error_mapper,
            request_options=request_options,
        )

    async def get_faster_payout_eligibility(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FasterPayoutEligibilityResponse, GetFasterPayoutEligibilityErrorBody]:
        """Returns whether the authenticated seller is eligible for an on-demand faster payout, along with the approved
        amount and any ineligibility reason. Delegates to GMPPaymentsPlatform GET /fasterPayout/eligibility/{partnerId}.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/fasterPayoutEligibility"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[FasterPayoutEligibilityResponse],
            error_mapper=get_faster_payout_eligibility_error_mapper,
            request_options=request_options,
        )

    async def get_payment_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PayoutStatusResponse, GetPaymentStatusErrorBody]:
        """Returns the current payout status for the authenticated seller, including scheduled payout date, amount, and
        lifecycle state (Pending, Processing, Completed, Failed, OnHold). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/paymentstatus"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[PayoutStatusResponse],
            error_mapper=get_payment_status_error_mapper,
            request_options=request_options,
        )

    async def initiate_faster_payout(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[InitiatePayoutResponse, InitiateFasterPayoutErrorBody]:
        """Triggers an immediate on-demand payout for the authenticated seller, bypassing the standard settlement
        schedule. Returns the payout ID and initial status. Requires disbursements:write scope. Delegates to
        GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/disbursements/v4/payment/fasterPayout"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[InitiatePayoutResponse],
            error_mapper=initiate_faster_payout_error_mapper,
            request_options=request_options,
        )
