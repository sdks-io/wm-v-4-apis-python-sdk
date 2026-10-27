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
from ..errors.get_final_payout_case_status_error import (
    GetFinalPayoutCaseStatusErrorBody,
    get_final_payout_case_status_error_mapper,
)
from ..errors.update_final_payout_case_status_error import (
    UpdateFinalPayoutCaseStatusErrorBody,
    update_final_payout_case_status_error_mapper,
)
from ..models.disbursements_v4_final_payout_case_update_status_request import (
    DisbursementsV4FinalPayoutCaseUpdateStatusRequest,
    DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict,
)
from ..models.final_payout_case_status_response import FinalPayoutCaseStatusResponse
from ..server.server import Server


class FinalPayout:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FinalPayoutWithRawResponse(client, server, auth)

    def get_final_payout_case_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> FinalPayoutCaseStatusResponse:
        """Returns the current state, case ID, and payable amount for the authenticated seller's final payout case (used
        when a seller account is being offboarded). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Not Found Internal Server
                Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.get_final_payout_case_status(request_options=request_options))

    def update_final_payout_case_status(
        self,
        body: DisbursementsV4FinalPayoutCaseUpdateStatusRequest | DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FinalPayoutCaseStatusResponse:
        """Transitions the authenticated seller's final payout case to Resolved or Closed, optionally including
        resolution notes. Requires disbursements:write scope. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Not Found Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(self._with_raw_response.update_final_payout_case_status(body, request_options=request_options))

    @property
    def with_raw_response(self) -> FinalPayoutWithRawResponse:
        return self._with_raw_response


class AsyncFinalPayout:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFinalPayoutWithRawResponse(client, server, auth)

    async def get_final_payout_case_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> FinalPayoutCaseStatusResponse:
        """Returns the current state, case ID, and payable amount for the authenticated seller's final payout case (used
        when a seller account is being offboarded). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Unauthorized — missing, expired, or invalid OAuth2 token Not Found Internal Server
                Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(await self._with_raw_response.get_final_payout_case_status(request_options=request_options))

    async def update_final_payout_case_status(
        self,
        body: DisbursementsV4FinalPayoutCaseUpdateStatusRequest | DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FinalPayoutCaseStatusResponse:
        """Transitions the authenticated seller's final payout case to Resolved or Closed, optionally including
        resolution notes. Requires disbursements:write scope. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Not Found Internal Server Error ``error`` is ``ErrorList | RawError``."""
        return unwrap(
            await self._with_raw_response.update_final_payout_case_status(body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncFinalPayoutWithRawResponse:
        return self._with_raw_response


class FinalPayoutWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_final_payout_case_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FinalPayoutCaseStatusResponse, GetFinalPayoutCaseStatusErrorBody]:
        """Returns the current state, case ID, and payable amount for the authenticated seller's final payout case (used
        when a seller account is being offboarded). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/finalPayout/case/status"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[FinalPayoutCaseStatusResponse],
            error_mapper=get_final_payout_case_status_error_mapper,
            request_options=request_options,
        )

    def update_final_payout_case_status(
        self,
        body: DisbursementsV4FinalPayoutCaseUpdateStatusRequest | DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FinalPayoutCaseStatusResponse, UpdateFinalPayoutCaseStatusErrorBody]:
        """Transitions the authenticated seller's final payout case to Resolved or Closed, optionally including
        resolution notes. Requires disbursements:write scope. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/disbursements/v4/finalPayout/case/updateStatus"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                (
                    DisbursementsV4FinalPayoutCaseUpdateStatusRequest
                    | DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict
                )
            ](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[FinalPayoutCaseStatusResponse],
            error_mapper=update_final_payout_case_status_error_mapper,
            request_options=request_options,
        )


class AsyncFinalPayoutWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_final_payout_case_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FinalPayoutCaseStatusResponse, GetFinalPayoutCaseStatusErrorBody]:
        """Returns the current state, case ID, and payable amount for the authenticated seller's final payout case (used
        when a seller account is being offboarded). Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/disbursements/v4/finalPayout/case/status"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[FinalPayoutCaseStatusResponse],
            error_mapper=get_final_payout_case_status_error_mapper,
            request_options=request_options,
        )

    async def update_final_payout_case_status(
        self,
        body: DisbursementsV4FinalPayoutCaseUpdateStatusRequest | DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FinalPayoutCaseStatusResponse, UpdateFinalPayoutCaseStatusErrorBody]:
        """Transitions the authenticated seller's final payout case to Resolved or Closed, optionally including
        resolution notes. Requires disbursements:write scope. Delegates to GMPPaymentsPlatform (Phase 5).

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default1("/disbursements/v4/finalPayout/case/updateStatus"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                (
                    DisbursementsV4FinalPayoutCaseUpdateStatusRequest
                    | DisbursementsV4FinalPayoutCaseUpdateStatusRequestDict
                )
            ](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[FinalPayoutCaseStatusResponse],
            error_mapper=update_final_payout_case_status_error_mapper,
            request_options=request_options,
        )
