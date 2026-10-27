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
from ..errors.get_account_error import GetAccountErrorBody, get_account_error_mapper
from ..errors.get_marketplace_participations_error import (
    GetMarketplaceParticipationsErrorBody,
    get_marketplace_participations_error_mapper,
)
from ..models.get_marketplace_participations_response import GetMarketplaceParticipationsResponse
from ..models.seller_account import SellerAccount
from ..server.server import Server


class Sellers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SellersWithRawResponse(client, server, auth)

    def get_account(self, *, request_options: RequestOptionsOrDict | None = None) -> SellerAccount:
        """Returns the authenticated seller's account information including business name, email, account status, and
        seller type.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.get_account(request_options=request_options))

    def get_marketplace_participations(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetMarketplaceParticipationsResponse:
        """Returns the list of marketplaces the authenticated seller participates in (e.g. Walmart US, Walmart Canada,
        Walmart Mexico).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(self._with_raw_response.get_marketplace_participations(request_options=request_options))

    @property
    def with_raw_response(self) -> SellersWithRawResponse:
        return self._with_raw_response


class AsyncSellers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSellersWithRawResponse(client, server, auth)

    async def get_account(self, *, request_options: RequestOptionsOrDict | None = None) -> SellerAccount:
        """Returns the authenticated seller's account information including business name, email, account status, and
        seller type.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.get_account(request_options=request_options))

    async def get_marketplace_participations(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetMarketplaceParticipationsResponse:
        """Returns the list of marketplaces the authenticated seller participates in (e.g. Walmart US, Walmart Canada,
        Walmart Mexico).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: Bad Request Forbidden Rate limit exceeded Internal Server Error ``error`` is ``ErrorList |
                RawError``."""
        return unwrap(await self._with_raw_response.get_marketplace_participations(request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncSellersWithRawResponse:
        return self._with_raw_response


class SellersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SellerAccount, GetAccountErrorBody]:
        """Returns the authenticated seller's account information including business name, email, account status, and
        seller type.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/sellers/v4/account"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[SellerAccount],
            error_mapper=get_account_error_mapper,
            request_options=request_options,
        )

    def get_marketplace_participations(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetMarketplaceParticipationsResponse, GetMarketplaceParticipationsErrorBody]:
        """Returns the list of marketplaces the authenticated seller participates in (e.g. Walmart US, Walmart Canada,
        Walmart Mexico).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/sellers/v4/marketplaceParticipations"),
            auth_scheme=self._auth.wallet_auth,
            decoder=json_decoder[GetMarketplaceParticipationsResponse],
            error_mapper=get_marketplace_participations_error_mapper,
            request_options=request_options,
        )


class AsyncSellersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SellerAccount, GetAccountErrorBody]:
        """Returns the authenticated seller's account information including business name, email, account status, and
        seller type.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/sellers/v4/account"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[SellerAccount],
            error_mapper=get_account_error_mapper,
            request_options=request_options,
        )

    async def get_marketplace_participations(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetMarketplaceParticipationsResponse, GetMarketplaceParticipationsErrorBody]:
        """Returns the list of marketplaces the authenticated seller participates in (e.g. Walmart US, Walmart Canada,
        Walmart Mexico).

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default1("/sellers/v4/marketplaceParticipations"),
            auth_scheme=self._auth.wallet_auth,
            decoder=async_json_decoder[GetMarketplaceParticipationsResponse],
            error_mapper=get_marketplace_participations_error_mapper,
            request_options=request_options,
        )
