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
    param,
    unwrap,
)
from ..errors.get_listings_restrictions_error import (
    GetListingsRestrictionsErrorBody,
    get_listings_restrictions_error_mapper,
)
from ..models.enums.condition_type1 import ConditionType1OrStr
from ..models.restriction_list import RestrictionList
from ..server.server import Server


class ListingsRestrictions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ListingsRestrictionsWithRawResponse(client, server, auth)

    def get_listings_restrictions(
        self,
        asin: str,
        condition_type: ConditionType1OrStr,
        seller_id: str,
        marketplace_ids: list[str],
        *,
        reason_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> RestrictionList:
        """Returns restrictions on listing an item for a given ASIN and seller. A successful response does not guarantee
        the seller can list — check the restrictions array.

        Args:
            asin: Walmart Item ID (maps to ASIN in Walmart Seller API)
            condition_type: Value sent with the request.
            seller_id: Value sent with the request.
            marketplace_ids: Value sent with the request.
            reason_locale: Locale for localized restriction reason messages
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            self._with_raw_response.get_listings_restrictions(
                asin,
                condition_type,
                seller_id,
                marketplace_ids,
                reason_locale=reason_locale,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> ListingsRestrictionsWithRawResponse:
        return self._with_raw_response


class AsyncListingsRestrictions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncListingsRestrictionsWithRawResponse(client, server, auth)

    async def get_listings_restrictions(
        self,
        asin: str,
        condition_type: ConditionType1OrStr,
        seller_id: str,
        marketplace_ids: list[str],
        *,
        reason_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> RestrictionList:
        """Returns restrictions on listing an item for a given ASIN and seller. A successful response does not guarantee
        the seller can list — check the restrictions array.

        Args:
            asin: Walmart Item ID (maps to ASIN in Walmart Seller API)
            condition_type: Value sent with the request.
            seller_id: Value sent with the request.
            marketplace_ids: Value sent with the request.
            reason_locale: Locale for localized restriction reason messages
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(
            await self._with_raw_response.get_listings_restrictions(
                asin,
                condition_type,
                seller_id,
                marketplace_ids,
                reason_locale=reason_locale,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncListingsRestrictionsWithRawResponse:
        return self._with_raw_response


class ListingsRestrictionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_listings_restrictions(
        self,
        asin: str,
        condition_type: ConditionType1OrStr,
        seller_id: str,
        marketplace_ids: list[str],
        *,
        reason_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RestrictionList, GetListingsRestrictionsErrorBody]:
        """Returns restrictions on listing an item for a given ASIN and seller. A successful response does not guarantee
        the seller can list — check the restrictions array.

        Args:
            asin: Walmart Item ID (maps to ASIN in Walmart Seller API)
            condition_type: Value sent with the request.
            seller_id: Value sent with the request.
            marketplace_ids: Value sent with the request.
            reason_locale: Locale for localized restriction reason messages
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/listings/v4/restrictions"),
            query_params=[
                param[str]("asin", asin),
                param[ConditionType1OrStr]("conditionType", condition_type),
                param[str]("sellerId", seller_id),
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str | None]("reasonLocale", reason_locale),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[RestrictionList],
            error_mapper=get_listings_restrictions_error_mapper,
            request_options=request_options,
        )


class AsyncListingsRestrictionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_listings_restrictions(
        self,
        asin: str,
        condition_type: ConditionType1OrStr,
        seller_id: str,
        marketplace_ids: list[str],
        *,
        reason_locale: str | None = "en_US",
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RestrictionList, GetListingsRestrictionsErrorBody]:
        """Returns restrictions on listing an item for a given ASIN and seller. A successful response does not guarantee
        the seller can list — check the restrictions array.

        Args:
            asin: Walmart Item ID (maps to ASIN in Walmart Seller API)
            condition_type: Value sent with the request.
            seller_id: Value sent with the request.
            marketplace_ids: Value sent with the request.
            reason_locale: Locale for localized restriction reason messages
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/listings/v4/restrictions"),
            query_params=[
                param[str]("asin", asin),
                param[ConditionType1OrStr]("conditionType", condition_type),
                param[str]("sellerId", seller_id),
                param[list[str]]("marketplaceIds", marketplace_ids),
                param[str | None]("reasonLocale", reason_locale),
            ],
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[RestrictionList],
            error_mapper=get_listings_restrictions_error_mapper,
            request_options=request_options,
        )
