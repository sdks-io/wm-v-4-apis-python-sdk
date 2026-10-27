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
from ..errors.cancel_report_schedule_error import CancelReportScheduleErrorBody, cancel_report_schedule_error_mapper
from ..errors.create_report_schedule_error import CreateReportScheduleErrorBody, create_report_schedule_error_mapper
from ..errors.get_report_schedule_error import GetReportScheduleErrorBody, get_report_schedule_error_mapper
from ..errors.get_report_schedules_error import GetReportSchedulesErrorBody, get_report_schedules_error_mapper
from ..models.cancel_report_schedule_response import CancelReportScheduleResponse
from ..models.create_report_schedule_response import CreateReportScheduleResponse
from ..models.create_report_schedule_specification import (
    CreateReportScheduleSpecification,
    CreateReportScheduleSpecificationDict,
)
from ..models.enums.report_type1 import ReportType1OrStr
from ..models.get_report_schedules_response import GetReportSchedulesResponse
from ..models.report_schedule import ReportSchedule
from ..server.server import Server


class ReportSchedules:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ReportSchedulesWithRawResponse(client, server, auth)

    def cancel_report_schedule(
        self, report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelReportScheduleResponse:
        """Send a ``DELETE`` request.

        Args:
            report_schedule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Schedule cancelled

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.cancel_report_schedule(report_schedule_id, request_options=request_options)
        )

    def create_report_schedule(
        self,
        body: CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateReportScheduleResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Schedule created

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.create_report_schedule(body, request_options=request_options))

    def get_report_schedule(
        self, report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReportSchedule:
        """Send a ``GET`` request.

        Args:
            report_schedule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(self._with_raw_response.get_report_schedule(report_schedule_id, request_options=request_options))

    def get_report_schedules(
        self, *, report_types: list[ReportType1OrStr] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GetReportSchedulesResponse:
        """Send a ``GET`` request.

        Args:
            report_types: Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime
                availability is CCM-controlled; consult PRP docs for current PROD-enabled types.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_report_schedules(report_types=report_types, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> ReportSchedulesWithRawResponse:
        return self._with_raw_response


class AsyncReportSchedules:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncReportSchedulesWithRawResponse(client, server, auth)

    async def cancel_report_schedule(
        self, report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelReportScheduleResponse:
        """Send a ``DELETE`` request.

        Args:
            report_schedule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Schedule cancelled

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_report_schedule(report_schedule_id, request_options=request_options)
        )

    async def create_report_schedule(
        self,
        body: CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateReportScheduleResponse:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Schedule created

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.create_report_schedule(body, request_options=request_options))

    async def get_report_schedule(
        self, report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ReportSchedule:
        """Send a ``GET`` request.

        Args:
            report_schedule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_report_schedule(report_schedule_id, request_options=request_options)
        )

    async def get_report_schedules(
        self, *, report_types: list[ReportType1OrStr] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> GetReportSchedulesResponse:
        """Send a ``GET`` request.

        Args:
            report_types: Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime
                availability is CCM-controlled; consult PRP docs for current PROD-enabled types.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_report_schedules(
                report_types=report_types, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncReportSchedulesWithRawResponse:
        return self._with_raw_response


class ReportSchedulesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_report_schedule(
        self, report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelReportScheduleResponse, CancelReportScheduleErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            report_schedule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/reports/v4/schedules/{reportScheduleId}"),
            path_params=[param[str]("reportScheduleId", report_schedule_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CancelReportScheduleResponse],
            error_mapper=cancel_report_schedule_error_mapper,
            request_options=request_options,
        )

    def create_report_schedule(
        self,
        body: CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateReportScheduleResponse, CreateReportScheduleErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/reports/v4/schedules"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[CreateReportScheduleResponse],
            error_mapper=create_report_schedule_error_mapper,
            request_options=request_options,
        )

    def get_report_schedule(
        self, report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReportSchedule, GetReportScheduleErrorBody]:
        """Send a ``GET`` request.

        Args:
            report_schedule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/reports/v4/schedules/{reportScheduleId}"),
            path_params=[param[str]("reportScheduleId", report_schedule_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[ReportSchedule],
            error_mapper=get_report_schedule_error_mapper,
            request_options=request_options,
        )

    def get_report_schedules(
        self, *, report_types: list[ReportType1OrStr] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetReportSchedulesResponse, GetReportSchedulesErrorBody]:
        """Send a ``GET`` request.

        Args:
            report_types: Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime
                availability is CCM-controlled; consult PRP docs for current PROD-enabled types.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/reports/v4/schedules"),
            query_params=[param[list[ReportType1OrStr] | None]("reportTypes", report_types)],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetReportSchedulesResponse],
            error_mapper=get_report_schedules_error_mapper,
            request_options=request_options,
        )


class AsyncReportSchedulesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_report_schedule(
        self, report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelReportScheduleResponse, CancelReportScheduleErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            report_schedule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default1("/reports/v4/schedules/{reportScheduleId}"),
            path_params=[param[str]("reportScheduleId", report_schedule_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CancelReportScheduleResponse],
            error_mapper=cancel_report_schedule_error_mapper,
            request_options=request_options,
        )

    async def create_report_schedule(
        self,
        body: CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateReportScheduleResponse, CreateReportScheduleErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default1("/reports/v4/schedules"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict](body),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[CreateReportScheduleResponse],
            error_mapper=create_report_schedule_error_mapper,
            request_options=request_options,
        )

    async def get_report_schedule(
        self, report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ReportSchedule, GetReportScheduleErrorBody]:
        """Send a ``GET`` request.

        Args:
            report_schedule_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/reports/v4/schedules/{reportScheduleId}"),
            path_params=[param[str]("reportScheduleId", report_schedule_id)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[ReportSchedule],
            error_mapper=get_report_schedule_error_mapper,
            request_options=request_options,
        )

    async def get_report_schedules(
        self, *, report_types: list[ReportType1OrStr] | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetReportSchedulesResponse, GetReportSchedulesErrorBody]:
        """Send a ``GET`` request.

        Args:
            report_types: Filter by report type. Values are Walmart Partner Reporting Platform enum names. Runtime
                availability is CCM-controlled; consult PRP docs for current PROD-enabled types.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/reports/v4/schedules"),
            query_params=[param[list[ReportType1OrStr] | None]("reportTypes", report_types)],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetReportSchedulesResponse],
            error_mapper=get_report_schedules_error_mapper,
            request_options=request_options,
        )
