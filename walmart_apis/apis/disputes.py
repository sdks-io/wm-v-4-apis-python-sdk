from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    unwrap,
)
from ..errors.check_dispute_eligibility_error import (
    CheckDisputeEligibilityErrorBody,
    check_dispute_eligibility_error_mapper,
)
from ..models.dispute_eligibility_response import DisputeEligibilityResponse
from ..server.server import Server


class Disputes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DisputesWithRawResponse(client, server, auth)

    def check_dispute_eligibility(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisputeEligibilityResponse:
        """Returns whether the authenticated seller is eligible to raise a payment dispute and, if not, the reason for
        ineligibility. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.check_dispute_eligibility(request_options=request_options))

    @property
    def with_raw_response(self) -> DisputesWithRawResponse:
        return self._with_raw_response


class AsyncDisputes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDisputesWithRawResponse(client, server, auth)

    async def check_dispute_eligibility(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisputeEligibilityResponse:
        """Returns whether the authenticated seller is eligible to raise a payment dispute and, if not, the reason for
        ineligibility. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Internal Server Error
                ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.check_dispute_eligibility(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncDisputesWithRawResponse:
        return self._with_raw_response


class DisputesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def check_dispute_eligibility(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisputeEligibilityResponse, CheckDisputeEligibilityErrorBody]:
        """Returns whether the authenticated seller is eligible to raise a payment dispute and, if not, the reason for
        ineligibility. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/disputeEligibilityCheck"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[DisputeEligibilityResponse],
            error_mapper=check_dispute_eligibility_error_mapper,
            request_options=request_options,
        )


class AsyncDisputesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def check_dispute_eligibility(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisputeEligibilityResponse, CheckDisputeEligibilityErrorBody]:
        """Returns whether the authenticated seller is eligible to raise a payment dispute and, if not, the reason for
        ineligibility. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/payment/disputeEligibilityCheck"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[DisputeEligibilityResponse],
            error_mapper=check_dispute_eligibility_error_mapper,
            request_options=request_options,
        )
