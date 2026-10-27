from __future__ import annotations

from typing import Any

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
from ..errors.get_order_metrics_error import GetOrderMetricsErrorBody, get_order_metrics_error_mapper
from ..models.enums.buyer_type import BuyerTypeOrStr
from ..models.enums.first_day_of_week import FirstDayOfWeekOrStr
from ..models.enums.granularity import GranularityOrStr
from ..server.server import Server


class Sales:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SalesWithRawResponse(client, server, auth)

    def get_order_metrics(
        self,
        marketplace_ids: list[str],
        interval: str,
        granularity: GranularityOrStr,
        *,
        granularity_time_zone: str | None = None,
        buyer_type: BuyerTypeOrStr | None = None,
        fulfillment_network: str | None = None,
        first_day_of_week: FirstDayOfWeekOrStr | None = None,
        asin: str | None = None,
        sku: str | None = None,
        sp_api_program: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be specified
            interval: A time interval used for selecting order metrics. This takes the form of two dates separated by
                two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must
                represent absolute time (either Z notation or offset notation). Example:
                2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in
                the -07:00 zone.
            granularity: The granularity of the grouping of order metrics, based on a unit of time. Specifying
                granularity=Hour results in a successful request only if the interval specified is less than or equal to
                30 days from now. For all other granularities, the interval specified must be less or equal to 2 years
                from now. Specifying granularity=Total results in order metrics that are aggregated over the entire
                interval that you specify. If the interval start and end date don’t align with the specified
                granularity, the head and tail end of the response interval will contain partial data. Example: Day to
                get a daily breakdown of the request interval, where the day boundary is defined by the
                granularityTimeZone.
            granularity_time_zone: An IANA-compatible time zone for determining the day boundary. Required when
                specifying a granularity value greater than Hour. The granularityTimeZone value must align with the
                offset of the specified interval value. For example, if the interval value uses Z notation, then
                granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be
                an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries,
                accounting for daylight time savings, for US/Pacific zone.
            buyer_type: Filters the results by the buyer type that you specify, B2B (business to business) or B2C
                (business to customer). Example: B2B, if you want the response to include order metrics for only B2B
                buyers.
            fulfillment_network: Filters the results by the fulfillment network that you specify, MFN (merchant
                fulfillment network) or AFN (marketplace fulfillment network). Do not include this filter if you want
                the response to include order metrics for all fulfillment networks. Example: AFN, if you want the
                response to include order metrics for only the marketplace fulfillment network.
            first_day_of_week: Specifies the day that the week starts on when granularity=Week, either Monday or Sunday.
                Default: Monday. Example: Sund
            asin: Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do
                not include this filter if you want the response to include order metrics for all ASINs. Example:
                B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.
            sku: Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not
                include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if
                you want the response to include order metrics for only SKU TestSKU.
            sp_api_program: Filters the results by the program that you specify. Do not include this filter if you want
                the response to inclu
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            self._with_raw_response.get_order_metrics(
                marketplace_ids,
                interval,
                granularity,
                granularity_time_zone=granularity_time_zone,
                buyer_type=buyer_type,
                fulfillment_network=fulfillment_network,
                first_day_of_week=first_day_of_week,
                asin=asin,
                sku=sku,
                sp_api_program=sp_api_program,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> SalesWithRawResponse:
        return self._with_raw_response


class AsyncSales:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSalesWithRawResponse(client, server, auth)

    async def get_order_metrics(
        self,
        marketplace_ids: list[str],
        interval: str,
        granularity: GranularityOrStr,
        *,
        granularity_time_zone: str | None = None,
        buyer_type: BuyerTypeOrStr | None = None,
        fulfillment_network: str | None = None,
        first_day_of_week: FirstDayOfWeekOrStr | None = None,
        asin: str | None = None,
        sku: str | None = None,
        sp_api_program: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Any:
        """Send a ``GET`` request.

        Args:
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be specified
            interval: A time interval used for selecting order metrics. This takes the form of two dates separated by
                two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must
                represent absolute time (either Z notation or offset notation). Example:
                2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in
                the -07:00 zone.
            granularity: The granularity of the grouping of order metrics, based on a unit of time. Specifying
                granularity=Hour results in a successful request only if the interval specified is less than or equal to
                30 days from now. For all other granularities, the interval specified must be less or equal to 2 years
                from now. Specifying granularity=Total results in order metrics that are aggregated over the entire
                interval that you specify. If the interval start and end date don’t align with the specified
                granularity, the head and tail end of the response interval will contain partial data. Example: Day to
                get a daily breakdown of the request interval, where the day boundary is defined by the
                granularityTimeZone.
            granularity_time_zone: An IANA-compatible time zone for determining the day boundary. Required when
                specifying a granularity value greater than Hour. The granularityTimeZone value must align with the
                offset of the specified interval value. For example, if the interval value uses Z notation, then
                granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be
                an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries,
                accounting for daylight time savings, for US/Pacific zone.
            buyer_type: Filters the results by the buyer type that you specify, B2B (business to business) or B2C
                (business to customer). Example: B2B, if you want the response to include order metrics for only B2B
                buyers.
            fulfillment_network: Filters the results by the fulfillment network that you specify, MFN (merchant
                fulfillment network) or AFN (marketplace fulfillment network). Do not include this filter if you want
                the response to include order metrics for all fulfillment networks. Example: AFN, if you want the
                response to include order metrics for only the marketplace fulfillment network.
            first_day_of_week: Specifies the day that the week starts on when granularity=Week, either Monday or Sunday.
                Default: Monday. Example: Sund
            asin: Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do
                not include this filter if you want the response to include order metrics for all ASINs. Example:
                B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.
            sku: Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not
                include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if
                you want the response to include order metrics for only SKU TestSKU.
            sp_api_program: Filters the results by the program that you specify. Do not include this filter if you want
                the response to inclu
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Not Found Rate limit exceeded Internal Server Error ``error`` is ``ErrorList
                | RawError``."""
        return unwrap(
            await self._with_raw_response.get_order_metrics(
                marketplace_ids,
                interval,
                granularity,
                granularity_time_zone=granularity_time_zone,
                buyer_type=buyer_type,
                fulfillment_network=fulfillment_network,
                first_day_of_week=first_day_of_week,
                asin=asin,
                sku=sku,
                sp_api_program=sp_api_program,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncSalesWithRawResponse:
        return self._with_raw_response


class SalesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_order_metrics(
        self,
        marketplace_ids: list[str],
        interval: str,
        granularity: GranularityOrStr,
        *,
        granularity_time_zone: str | None = None,
        buyer_type: BuyerTypeOrStr | None = None,
        fulfillment_network: str | None = None,
        first_day_of_week: FirstDayOfWeekOrStr | None = None,
        asin: str | None = None,
        sku: str | None = None,
        sp_api_program: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GetOrderMetricsErrorBody]:
        """Send a ``GET`` request.

        Args:
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be specified
            interval: A time interval used for selecting order metrics. This takes the form of two dates separated by
                two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must
                represent absolute time (either Z notation or offset notation). Example:
                2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in
                the -07:00 zone.
            granularity: The granularity of the grouping of order metrics, based on a unit of time. Specifying
                granularity=Hour results in a successful request only if the interval specified is less than or equal to
                30 days from now. For all other granularities, the interval specified must be less or equal to 2 years
                from now. Specifying granularity=Total results in order metrics that are aggregated over the entire
                interval that you specify. If the interval start and end date don’t align with the specified
                granularity, the head and tail end of the response interval will contain partial data. Example: Day to
                get a daily breakdown of the request interval, where the day boundary is defined by the
                granularityTimeZone.
            granularity_time_zone: An IANA-compatible time zone for determining the day boundary. Required when
                specifying a granularity value greater than Hour. The granularityTimeZone value must align with the
                offset of the specified interval value. For example, if the interval value uses Z notation, then
                granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be
                an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries,
                accounting for daylight time savings, for US/Pacific zone.
            buyer_type: Filters the results by the buyer type that you specify, B2B (business to business) or B2C
                (business to customer). Example: B2B, if you want the response to include order metrics for only B2B
                buyers.
            fulfillment_network: Filters the results by the fulfillment network that you specify, MFN (merchant
                fulfillment network) or AFN (marketplace fulfillment network). Do not include this filter if you want
                the response to include order metrics for all fulfillment networks. Example: AFN, if you want the
                response to include order metrics for only the marketplace fulfillment network.
            first_day_of_week: Specifies the day that the week starts on when granularity=Week, either Monday or Sunday.
                Default: Monday. Example: Sund
            asin: Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do
                not include this filter if you want the response to include order metrics for all ASINs. Example:
                B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.
            sku: Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not
                include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if
                you want the response to include order metrics for only SKU TestSKU.
            sp_api_program: Filters the results by the program that you specify. Do not include this filter if you want
                the response to inclu
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/sales/v4/orderMetrics"),
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str]("interval", interval),
                param[GranularityOrStr]("granularity", granularity),
                param[str | None]("granularityTimeZone", granularity_time_zone),
                param[BuyerTypeOrStr | None]("buyerType", buyer_type),
                param[str | None]("fulfillmentNetwork", fulfillment_network),
                param[FirstDayOfWeekOrStr | None]("firstDayOfWeek", first_day_of_week),
                param[str | None]("asin", asin),
                param[str | None]("sku", sku),
                param[str | None]("sp-apiProgram", sp_api_program),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[Any],
            error_mapper=get_order_metrics_error_mapper,
            request_options=request_options,
        )


class AsyncSalesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_order_metrics(
        self,
        marketplace_ids: list[str],
        interval: str,
        granularity: GranularityOrStr,
        *,
        granularity_time_zone: str | None = None,
        buyer_type: BuyerTypeOrStr | None = None,
        fulfillment_network: str | None = None,
        first_day_of_week: FirstDayOfWeekOrStr | None = None,
        asin: str | None = None,
        sku: str | None = None,
        sp_api_program: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Any, GetOrderMetricsErrorBody]:
        """Send a ``GET`` request.

        Args:
            marketplace_ids: A marketplace identifier. This specifies the marketplace in which the order was placed.
                Only one marketplace can be specified
            interval: A time interval used for selecting order metrics. This takes the form of two dates separated by
                two hyphens (first date is inclusive; second date is exclusive). Dates are in ISO8601 format and must
                represent absolute time (either Z notation or offset notation). Example:
                2018-09-01T00:00:00-07:00--2018-09-04T00:00:00-07:00 requests order metrics for Sept 1st, 2nd and 3rd in
                the -07:00 zone.
            granularity: The granularity of the grouping of order metrics, based on a unit of time. Specifying
                granularity=Hour results in a successful request only if the interval specified is less than or equal to
                30 days from now. For all other granularities, the interval specified must be less or equal to 2 years
                from now. Specifying granularity=Total results in order metrics that are aggregated over the entire
                interval that you specify. If the interval start and end date don’t align with the specified
                granularity, the head and tail end of the response interval will contain partial data. Example: Day to
                get a daily breakdown of the request interval, where the day boundary is defined by the
                granularityTimeZone.
            granularity_time_zone: An IANA-compatible time zone for determining the day boundary. Required when
                specifying a granularity value greater than Hour. The granularityTimeZone value must align with the
                offset of the specified interval value. For example, if the interval value uses Z notation, then
                granularityTimeZone must be UTC. If the interval value uses an offset, then granularityTimeZone must be
                an IANA-compatible time zone that matches the offset. Example: US/Pacific to compute day boundaries,
                accounting for daylight time savings, for US/Pacific zone.
            buyer_type: Filters the results by the buyer type that you specify, B2B (business to business) or B2C
                (business to customer). Example: B2B, if you want the response to include order metrics for only B2B
                buyers.
            fulfillment_network: Filters the results by the fulfillment network that you specify, MFN (merchant
                fulfillment network) or AFN (marketplace fulfillment network). Do not include this filter if you want
                the response to include order metrics for all fulfillment networks. Example: AFN, if you want the
                response to include order metrics for only the marketplace fulfillment network.
            first_day_of_week: Specifies the day that the week starts on when granularity=Week, either Monday or Sunday.
                Default: Monday. Example: Sund
            asin: Filters the results by the ASIN that you specify. Specifying both ASIN and SKU returns an error. Do
                not include this filter if you want the response to include order metrics for all ASINs. Example:
                B0792R1RSN, if you want the response to include order metrics for only ASIN B0792R1RSN.
            sku: Filters the results by the SKU that you specify. Specifying both ASIN and SKU returns an error. Do not
                include this filter if you want the response to include order metrics for all SKUs. Example: TestSKU, if
                you want the response to include order metrics for only SKU TestSKU.
            sp_api_program: Filters the results by the program that you specify. Do not include this filter if you want
                the response to inclu
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/sales/v4/orderMetrics"),
            query_params=[
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str]("interval", interval),
                param[GranularityOrStr]("granularity", granularity),
                param[str | None]("granularityTimeZone", granularity_time_zone),
                param[BuyerTypeOrStr | None]("buyerType", buyer_type),
                param[str | None]("fulfillmentNetwork", fulfillment_network),
                param[FirstDayOfWeekOrStr | None]("firstDayOfWeek", first_day_of_week),
                param[str | None]("asin", asin),
                param[str | None]("sku", sku),
                param[str | None]("sp-apiProgram", sp_api_program),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[Any],
            error_mapper=get_order_metrics_error_mapper,
            request_options=request_options,
        )
