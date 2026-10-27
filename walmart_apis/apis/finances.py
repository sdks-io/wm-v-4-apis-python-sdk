from __future__ import annotations

from typing import Any

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
from ..errors.list_financial_event_groups_error import (
    ListFinancialEventGroupsErrorBody,
    list_financial_event_groups_error_mapper,
)
from ..errors.list_financial_events_by_group_id_error import (
    ListFinancialEventsByGroupIdErrorBody,
    list_financial_events_by_group_id_error_mapper,
)
from ..errors.list_financial_events_by_order_id_error import (
    ListFinancialEventsByOrderIdErrorBody,
    list_financial_events_by_order_id_error_mapper,
)
from ..errors.list_financial_events_error import ListFinancialEventsErrorBody, list_financial_events_error_mapper
from ..server.server import Server


class Finances:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FinancesWithRawResponse(client, server, auth)

    def list_financial_event_groups(
        self,
        *,
        max_results_per_page: int | None = None,
        financial_event_group_started_before: RFC3339DateTime | None = None,
        financial_event_group_started_after: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns financial event groups for the seller.

        **Status: stub** — no upstream endpoint found that models the SP-API FinancialEventGroup (requires eventGroupId
        keying, date-range filter, and cursor pagination). Returns empty response pending Phase 5.

        Args:
            max_results_per_page: The maximum number of results per page.
            financial_event_group_started_before: Financial event groups that opened before this date/time (ISO 8601).
            financial_event_group_started_after: Financial event groups that opened after this date/time (ISO 8601).
            next_token: Cursor token for the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.list_financial_event_groups(
                max_results_per_page=max_results_per_page,
                financial_event_group_started_before=financial_event_group_started_before,
                financial_event_group_started_after=financial_event_group_started_after,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    def list_financial_events(
        self,
        *,
        max_results_per_page: int | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns financial events for the authenticated seller via GMP partnerTxnSearch.

        **Best-effort implementation** — backed by GMP partnerTxnSearch. Returns transaction records for the seller
        keyed by partnerId.

        **Unsupported parameters:** PostedAfter, PostedBefore, and NextToken are not supported by the upstream.
        Supplying any of these parameters returns 400 Bad Request.

        Args:
            max_results_per_page: Ignored — GMP returns all results in a single page.
            posted_after: Not supported — returns 400 Bad Request if supplied.
            posted_before: Not supported — returns 400 Bad Request if supplied.
            next_token: Not supported — returns 400 Bad Request if supplied.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.list_financial_events(
                max_results_per_page=max_results_per_page,
                posted_after=posted_after,
                posted_before=posted_before,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    def list_financial_events_by_group_id(
        self,
        event_group_id: str,
        *,
        max_results_per_page: int | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns financial events for a specific financial event group.

        **Status: stub** — no upstream maps eventGroupId to a financial event set. Returns empty response pending Phase
        5.

        Args:
            event_group_id: The identifier of the financial event group.
            max_results_per_page: The maximum number of results to return per page.
            posted_after: Financial events posted after (or on) this date (ISO 8601).
            posted_before: Financial events posted before (but not on) this date (ISO 8601).
            next_token: Cursor token for the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.list_financial_events_by_group_id(
                event_group_id,
                max_results_per_page=max_results_per_page,
                posted_after=posted_after,
                posted_before=posted_before,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    def list_financial_events_by_order_id(
        self,
        order_id: str,
        *,
        max_results_per_page: int | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns financial events for a specific order via GMP commission endpoint.

        **Best-effort implementation** — returns commission charges only; refunds, fees, and adjustments are absent.
        IDOR ownership gate enforced.

        Args:
            order_id: Walmart order number — must be numeric (1–50 digits).
            max_results_per_page: Ignored — GMP returns all commission entries in one page.
            next_token: Not supported — returns 400 Bad Request if supplied.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.list_financial_events_by_order_id(
                order_id,
                max_results_per_page=max_results_per_page,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> FinancesWithRawResponse:
        return self._with_raw_response


class AsyncFinances:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFinancesWithRawResponse(client, server, auth)

    async def list_financial_event_groups(
        self,
        *,
        max_results_per_page: int | None = None,
        financial_event_group_started_before: RFC3339DateTime | None = None,
        financial_event_group_started_after: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns financial event groups for the seller.

        **Status: stub** — no upstream endpoint found that models the SP-API FinancialEventGroup (requires eventGroupId
        keying, date-range filter, and cursor pagination). Returns empty response pending Phase 5.

        Args:
            max_results_per_page: The maximum number of results per page.
            financial_event_group_started_before: Financial event groups that opened before this date/time (ISO 8601).
            financial_event_group_started_after: Financial event groups that opened after this date/time (ISO 8601).
            next_token: Cursor token for the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.list_financial_event_groups(
                max_results_per_page=max_results_per_page,
                financial_event_group_started_before=financial_event_group_started_before,
                financial_event_group_started_after=financial_event_group_started_after,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    async def list_financial_events(
        self,
        *,
        max_results_per_page: int | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns financial events for the authenticated seller via GMP partnerTxnSearch.

        **Best-effort implementation** — backed by GMP partnerTxnSearch. Returns transaction records for the seller
        keyed by partnerId.

        **Unsupported parameters:** PostedAfter, PostedBefore, and NextToken are not supported by the upstream.
        Supplying any of these parameters returns 400 Bad Request.

        Args:
            max_results_per_page: Ignored — GMP returns all results in a single page.
            posted_after: Not supported — returns 400 Bad Request if supplied.
            posted_before: Not supported — returns 400 Bad Request if supplied.
            next_token: Not supported — returns 400 Bad Request if supplied.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.list_financial_events(
                max_results_per_page=max_results_per_page,
                posted_after=posted_after,
                posted_before=posted_before,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    async def list_financial_events_by_group_id(
        self,
        event_group_id: str,
        *,
        max_results_per_page: int | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns financial events for a specific financial event group.

        **Status: stub** — no upstream maps eventGroupId to a financial event set. Returns empty response pending Phase
        5.

        Args:
            event_group_id: The identifier of the financial event group.
            max_results_per_page: The maximum number of results to return per page.
            posted_after: Financial events posted after (or on) this date (ISO 8601).
            posted_before: Financial events posted before (but not on) this date (ISO 8601).
            next_token: Cursor token for the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.list_financial_events_by_group_id(
                event_group_id,
                max_results_per_page=max_results_per_page,
                posted_after=posted_after,
                posted_before=posted_before,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    async def list_financial_events_by_order_id(
        self,
        order_id: str,
        *,
        max_results_per_page: int | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Returns financial events for a specific order via GMP commission endpoint.

        **Best-effort implementation** — returns commission charges only; refunds, fees, and adjustments are absent.
        IDOR ownership gate enforced.

        Args:
            order_id: Walmart order number — must be numeric (1–50 digits).
            max_results_per_page: Ignored — GMP returns all commission entries in one page.
            next_token: Not supported — returns 400 Bad Request if supplied.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.list_financial_events_by_order_id(
                order_id,
                max_results_per_page=max_results_per_page,
                next_token=next_token,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncFinancesWithRawResponse:
        return self._with_raw_response


class FinancesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_financial_event_groups(
        self,
        *,
        max_results_per_page: int | None = None,
        financial_event_group_started_before: RFC3339DateTime | None = None,
        financial_event_group_started_after: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListFinancialEventGroupsErrorBody]:
        """Returns financial event groups for the seller.

        **Status: stub** — no upstream endpoint found that models the SP-API FinancialEventGroup (requires eventGroupId
        keying, date-range filter, and cursor pagination). Returns empty response pending Phase 5.

        Args:
            max_results_per_page: The maximum number of results per page.
            financial_event_group_started_before: Financial event groups that opened before this date/time (ISO 8601).
            financial_event_group_started_after: Financial event groups that opened after this date/time (ISO 8601).
            next_token: Cursor token for the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/finances/v4/financialEventGroups"),
            query_params=[
                param[int | None]("MaxResultsPerPage", max_results_per_page),
                param[RFC3339DateTime | None]("FinancialEventGroupStartedBefore", financial_event_group_started_before),
                param[RFC3339DateTime | None]("FinancialEventGroupStartedAfter", financial_event_group_started_after),
                param[str | None]("NextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=list_financial_event_groups_error_mapper,
            request_options=request_options,
        )

    def list_financial_events(
        self,
        *,
        max_results_per_page: int | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListFinancialEventsErrorBody]:
        """Returns financial events for the authenticated seller via GMP partnerTxnSearch.

        **Best-effort implementation** — backed by GMP partnerTxnSearch. Returns transaction records for the seller
        keyed by partnerId.

        **Unsupported parameters:** PostedAfter, PostedBefore, and NextToken are not supported by the upstream.
        Supplying any of these parameters returns 400 Bad Request.

        Args:
            max_results_per_page: Ignored — GMP returns all results in a single page.
            posted_after: Not supported — returns 400 Bad Request if supplied.
            posted_before: Not supported — returns 400 Bad Request if supplied.
            next_token: Not supported — returns 400 Bad Request if supplied.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/finances/v4/financialEvents"),
            query_params=[
                param[int | None]("MaxResultsPerPage", max_results_per_page),
                param[RFC3339DateTime | None]("PostedAfter", posted_after),
                param[RFC3339DateTime | None]("PostedBefore", posted_before),
                param[str | None]("NextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=list_financial_events_error_mapper,
            request_options=request_options,
        )

    def list_financial_events_by_group_id(
        self,
        event_group_id: str,
        *,
        max_results_per_page: int | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListFinancialEventsByGroupIdErrorBody]:
        """Returns financial events for a specific financial event group.

        **Status: stub** — no upstream maps eventGroupId to a financial event set. Returns empty response pending Phase
        5.

        Args:
            event_group_id: The identifier of the financial event group.
            max_results_per_page: The maximum number of results to return per page.
            posted_after: Financial events posted after (or on) this date (ISO 8601).
            posted_before: Financial events posted before (but not on) this date (ISO 8601).
            next_token: Cursor token for the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/finances/v4/financialEventGroups/{eventGroupId}/financialEvents"),
            path_params=[param[str]("eventGroupId", event_group_id)],
            query_params=[
                param[int | None]("MaxResultsPerPage", max_results_per_page),
                param[RFC3339DateTime | None]("PostedAfter", posted_after),
                param[RFC3339DateTime | None]("PostedBefore", posted_before),
                param[str | None]("NextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=list_financial_events_by_group_id_error_mapper,
            request_options=request_options,
        )

    def list_financial_events_by_order_id(
        self,
        order_id: str,
        *,
        max_results_per_page: int | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListFinancialEventsByOrderIdErrorBody]:
        """Returns financial events for a specific order via GMP commission endpoint.

        **Best-effort implementation** — returns commission charges only; refunds, fees, and adjustments are absent.
        IDOR ownership gate enforced.

        Args:
            order_id: Walmart order number — must be numeric (1–50 digits).
            max_results_per_page: Ignored — GMP returns all commission entries in one page.
            next_token: Not supported — returns 400 Bad Request if supplied.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/finances/v4/orders/{orderId}/financialEvents"),
            path_params=[param[str]("orderId", order_id)],
            query_params=[
                param[int | None]("MaxResultsPerPage", max_results_per_page), param[str | None]("NextToken", next_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=list_financial_events_by_order_id_error_mapper,
            request_options=request_options,
        )


class AsyncFinancesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_financial_event_groups(
        self,
        *,
        max_results_per_page: int | None = None,
        financial_event_group_started_before: RFC3339DateTime | None = None,
        financial_event_group_started_after: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListFinancialEventGroupsErrorBody]:
        """Returns financial event groups for the seller.

        **Status: stub** — no upstream endpoint found that models the SP-API FinancialEventGroup (requires eventGroupId
        keying, date-range filter, and cursor pagination). Returns empty response pending Phase 5.

        Args:
            max_results_per_page: The maximum number of results per page.
            financial_event_group_started_before: Financial event groups that opened before this date/time (ISO 8601).
            financial_event_group_started_after: Financial event groups that opened after this date/time (ISO 8601).
            next_token: Cursor token for the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/finances/v4/financialEventGroups"),
            query_params=[
                param[int | None]("MaxResultsPerPage", max_results_per_page),
                param[RFC3339DateTime | None]("FinancialEventGroupStartedBefore", financial_event_group_started_before),
                param[RFC3339DateTime | None]("FinancialEventGroupStartedAfter", financial_event_group_started_after),
                param[str | None]("NextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=list_financial_event_groups_error_mapper,
            request_options=request_options,
        )

    async def list_financial_events(
        self,
        *,
        max_results_per_page: int | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListFinancialEventsErrorBody]:
        """Returns financial events for the authenticated seller via GMP partnerTxnSearch.

        **Best-effort implementation** — backed by GMP partnerTxnSearch. Returns transaction records for the seller
        keyed by partnerId.

        **Unsupported parameters:** PostedAfter, PostedBefore, and NextToken are not supported by the upstream.
        Supplying any of these parameters returns 400 Bad Request.

        Args:
            max_results_per_page: Ignored — GMP returns all results in a single page.
            posted_after: Not supported — returns 400 Bad Request if supplied.
            posted_before: Not supported — returns 400 Bad Request if supplied.
            next_token: Not supported — returns 400 Bad Request if supplied.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/finances/v4/financialEvents"),
            query_params=[
                param[int | None]("MaxResultsPerPage", max_results_per_page),
                param[RFC3339DateTime | None]("PostedAfter", posted_after),
                param[RFC3339DateTime | None]("PostedBefore", posted_before),
                param[str | None]("NextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=list_financial_events_error_mapper,
            request_options=request_options,
        )

    async def list_financial_events_by_group_id(
        self,
        event_group_id: str,
        *,
        max_results_per_page: int | None = None,
        posted_after: RFC3339DateTime | None = None,
        posted_before: RFC3339DateTime | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListFinancialEventsByGroupIdErrorBody]:
        """Returns financial events for a specific financial event group.

        **Status: stub** — no upstream maps eventGroupId to a financial event set. Returns empty response pending Phase
        5.

        Args:
            event_group_id: The identifier of the financial event group.
            max_results_per_page: The maximum number of results to return per page.
            posted_after: Financial events posted after (or on) this date (ISO 8601).
            posted_before: Financial events posted before (but not on) this date (ISO 8601).
            next_token: Cursor token for the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/finances/v4/financialEventGroups/{eventGroupId}/financialEvents"),
            path_params=[param[str]("eventGroupId", event_group_id)],
            query_params=[
                param[int | None]("MaxResultsPerPage", max_results_per_page),
                param[RFC3339DateTime | None]("PostedAfter", posted_after),
                param[RFC3339DateTime | None]("PostedBefore", posted_before),
                param[str | None]("NextToken", next_token),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=list_financial_events_by_group_id_error_mapper,
            request_options=request_options,
        )

    async def list_financial_events_by_order_id(
        self,
        order_id: str,
        *,
        max_results_per_page: int | None = None,
        next_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, ListFinancialEventsByOrderIdErrorBody]:
        """Returns financial events for a specific order via GMP commission endpoint.

        **Best-effort implementation** — returns commission charges only; refunds, fees, and adjustments are absent.
        IDOR ownership gate enforced.

        Args:
            order_id: Walmart order number — must be numeric (1–50 digits).
            max_results_per_page: Ignored — GMP returns all commission entries in one page.
            next_token: Not supported — returns 400 Bad Request if supplied.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/finances/v4/orders/{orderId}/financialEvents"),
            path_params=[param[str]("orderId", order_id)],
            query_params=[
                param[int | None]("MaxResultsPerPage", max_results_per_page), param[str | None]("NextToken", next_token)
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=list_financial_events_by_order_id_error_mapper,
            request_options=request_options,
        )
