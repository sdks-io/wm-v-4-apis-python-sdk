from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.authorization import AsyncAuthorization
from .apis.catalog import AsyncCatalog
from .apis.data_kiosk import AsyncDataKiosk
from .apis.disputes import AsyncDisputes
from .apis.feeds import AsyncFeeds
from .apis.final_payout import AsyncFinalPayout
from .apis.finances import AsyncFinances
from .apis.fulfillment_outbound import AsyncFulfillmentOutbound
from .apis.inventory import AsyncInventory
from .apis.listings_items import AsyncListingsItems
from .apis.listings_restrictions import AsyncListingsRestrictions
from .apis.merchant_fulfillment import AsyncMerchantFulfillment
from .apis.messaging import AsyncMessaging
from .apis.notifications import AsyncNotifications
from .apis.orders import AsyncOrders
from .apis.payouts import AsyncPayouts
from .apis.product_fees import AsyncProductFees
from .apis.product_pricing import AsyncProductPricing
from .apis.product_type_definitions import AsyncProductTypeDefinitions
from .apis.reconciliation import AsyncReconciliation
from .apis.report_schedules import AsyncReportSchedules
from .apis.reports import AsyncReports
from .apis.sales import AsyncSales
from .apis.sellers import AsyncSellers
from .apis.settlement import AsyncSettlement
from .apis.shipping import AsyncShipping
from .apis.solicitations import AsyncSolicitations
from .apis.supply_source_api import AsyncSupplySourceApi
from .apis.uploads import AsyncUploads
from .apis.wfs_inbound import AsyncWfsInbound
from .apis.wfs_inventory import AsyncWfsInventory
from .auth import AsyncAuthSchemes, SellerAuthAuthorizationCodeScope, SellerAuthClientCredentialsScope, WalletAuthScope
from .base_client import DEFAULT_TIMEOUT, BaseWalmartApisClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AsyncAuthorizationCodeCredentials,
    AsyncAuthorizationCodeCredentialsOrDict,
    AsyncAuthorizationCodeTokenSource,
    AsyncClientCredentialsTokenSource,
    AsyncHttpClient,
    AsyncHttpx2Client,
    AsyncOAuth2RefreshableScheme,
    AsyncOAuth2Scheme,
    AsyncRawClient,
    AsyncRefreshableTokenSource,
    AsyncTokenSource,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    ClientCredentials,
    ClientCredentialsOrDict,
    LoggingOptionsOrDict,
    RetryOptionsOrDict,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment
from .server.server_config import ServerConfigOrDict


class AsyncWalmartApisClient(BaseWalmartApisClient[AsyncRawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_async_http_client: AsyncHttpClient | None = None,
        seller_auth_authorization_code: (
            AsyncAuthorizationCodeCredentialsOrDict[SellerAuthAuthorizationCodeScope] | None
        ) = None,
        seller_auth_authorization_code_token_source: (
            AsyncRefreshableTokenSource[AsyncAuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope]] | None
        ) = None,
        seller_auth_client_credentials: ClientCredentialsOrDict[SellerAuthClientCredentialsScope] | None = None,
        seller_auth_client_credentials_token_source: (
            AsyncTokenSource[ClientCredentials[SellerAuthClientCredentialsScope]] | None
        ) = None,
        basic_client_auth: BasicAuthCredentialsOrDict | None = None,
        wallet_auth: ClientCredentialsOrDict[WalletAuthScope] | None = None,
        wallet_auth_token_source: AsyncTokenSource[ClientCredentials[WalletAuthScope]] | None = None,
    ) -> None:
        super().__init__(
            environment=environment,
            timeout=timeout,
            server_config=server_config,
            retry_options=retry_options,
            logging_options=logging_options,
        )
        self._raw_client = AsyncRawClient(
            http_client=(
                custom_async_http_client if custom_async_http_client is not None else AsyncHttpx2Client(timeout=timeout)
            ),
            retry_options=self._retry_options,
            logging_options=self._logging_options,
            global_headers=[
                param[str]("User-Agent", "WalmartApisClient/v4 Python"),
                param[str]("X-APIMatic-Lang", "Python"),
                param[str]("X-APIMatic-Package-Version", "v4"),
                param[str]("X-APIMatic-Gen-Version", "4.0.0"),
                param[str]("X-APIMatic-OS", OPERATING_SYSTEM),
                param[str]("X-APIMatic-Runtime", PYTHON_RUNTIME),
            ],
        )
        self._auth = AsyncAuthSchemes(
            seller_auth_authorization_code=(
                AsyncOAuth2RefreshableScheme(
                    credentials=AsyncAuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope].coerce(
                        seller_auth_authorization_code
                    ),
                    source=(
                        seller_auth_authorization_code_token_source
                        if seller_auth_authorization_code_token_source is not None
                        else AsyncAuthorizationCodeTokenSource[SellerAuthAuthorizationCodeScope](
                            client=self._raw_client,
                            authorization_url=self._server.auth_server("/authorize"),
                            token_url=self._server.default("/v4/auth/token"),
                            refresh_url=self._server.default("/v4/auth/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if seller_auth_authorization_code is not None
                else no_auth
            ),
            seller_auth_client_credentials=(
                AsyncOAuth2Scheme(
                    credentials=ClientCredentials[SellerAuthClientCredentialsScope].coerce(
                        seller_auth_client_credentials
                    ),
                    source=(
                        seller_auth_client_credentials_token_source
                        if seller_auth_client_credentials_token_source is not None
                        else AsyncClientCredentialsTokenSource[SellerAuthClientCredentialsScope](
                            client=self._raw_client,
                            token_url=self._server.default("/v4/auth/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if seller_auth_client_credentials is not None
                else no_auth
            ),
            basic_client_auth=(
                BasicAuthScheme(BasicAuthCredentials.coerce(basic_client_auth))
                if basic_client_auth is not None
                else no_auth
            ),
            wallet_auth=(
                AsyncOAuth2Scheme(
                    credentials=ClientCredentials[WalletAuthScope].coerce(wallet_auth),
                    source=(
                        wallet_auth_token_source
                        if wallet_auth_token_source is not None
                        else AsyncClientCredentialsTokenSource[WalletAuthScope](
                            client=self._raw_client,
                            token_url=self._server.access_token_server("/token"),
                            placement=client_secret_basic,
                        )
                    ),
                )
                if wallet_auth is not None
                else no_auth
            ),
        )

    @cached_property
    def authorization(self) -> AsyncAuthorization:
        return AsyncAuthorization(self._raw_client, self._server, self._auth)

    @cached_property
    def catalog(self) -> AsyncCatalog:
        return AsyncCatalog(self._raw_client, self._server, self._auth)

    @cached_property
    def data_kiosk(self) -> AsyncDataKiosk:
        return AsyncDataKiosk(self._raw_client, self._server, self._auth)

    @cached_property
    def disputes(self) -> AsyncDisputes:
        return AsyncDisputes(self._raw_client, self._server, self._auth)

    @cached_property
    def feeds(self) -> AsyncFeeds:
        return AsyncFeeds(self._raw_client, self._server, self._auth)

    @cached_property
    def final_payout(self) -> AsyncFinalPayout:
        return AsyncFinalPayout(self._raw_client, self._server, self._auth)

    @cached_property
    def finances(self) -> AsyncFinances:
        return AsyncFinances(self._raw_client, self._server, self._auth)

    @cached_property
    def fulfillment_outbound(self) -> AsyncFulfillmentOutbound:
        return AsyncFulfillmentOutbound(self._raw_client, self._server, self._auth)

    @cached_property
    def inventory(self) -> AsyncInventory:
        return AsyncInventory(self._raw_client, self._server, self._auth)

    @cached_property
    def listings_items(self) -> AsyncListingsItems:
        return AsyncListingsItems(self._raw_client, self._server, self._auth)

    @cached_property
    def listings_restrictions(self) -> AsyncListingsRestrictions:
        return AsyncListingsRestrictions(self._raw_client, self._server, self._auth)

    @cached_property
    def merchant_fulfillment(self) -> AsyncMerchantFulfillment:
        return AsyncMerchantFulfillment(self._raw_client, self._server, self._auth)

    @cached_property
    def orders(self) -> AsyncOrders:
        return AsyncOrders(self._raw_client, self._server, self._auth)

    @cached_property
    def payouts(self) -> AsyncPayouts:
        return AsyncPayouts(self._raw_client, self._server, self._auth)

    @cached_property
    def product_type_definitions(self) -> AsyncProductTypeDefinitions:
        return AsyncProductTypeDefinitions(self._raw_client, self._server, self._auth)

    @cached_property
    def reconciliation(self) -> AsyncReconciliation:
        return AsyncReconciliation(self._raw_client, self._server, self._auth)

    @cached_property
    def report_schedules(self) -> AsyncReportSchedules:
        return AsyncReportSchedules(self._raw_client, self._server, self._auth)

    @cached_property
    def reports(self) -> AsyncReports:
        return AsyncReports(self._raw_client, self._server, self._auth)

    @cached_property
    def sellers(self) -> AsyncSellers:
        return AsyncSellers(self._raw_client, self._server, self._auth)

    @cached_property
    def settlement(self) -> AsyncSettlement:
        return AsyncSettlement(self._raw_client, self._server, self._auth)

    @cached_property
    def supply_source_api(self) -> AsyncSupplySourceApi:
        return AsyncSupplySourceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def uploads(self) -> AsyncUploads:
        return AsyncUploads(self._raw_client, self._server, self._auth)

    @cached_property
    def wfs_inventory(self) -> AsyncWfsInventory:
        return AsyncWfsInventory(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging(self) -> AsyncMessaging:
        return AsyncMessaging(self._raw_client, self._server, self._auth)

    @cached_property
    def notifications(self) -> AsyncNotifications:
        return AsyncNotifications(self._raw_client, self._server, self._auth)

    @cached_property
    def product_fees(self) -> AsyncProductFees:
        return AsyncProductFees(self._raw_client, self._server, self._auth)

    @cached_property
    def product_pricing(self) -> AsyncProductPricing:
        return AsyncProductPricing(self._raw_client, self._server, self._auth)

    @cached_property
    def sales(self) -> AsyncSales:
        return AsyncSales(self._raw_client, self._server, self._auth)

    @cached_property
    def shipping(self) -> AsyncShipping:
        return AsyncShipping(self._raw_client, self._server, self._auth)

    @cached_property
    def solicitations(self) -> AsyncSolicitations:
        return AsyncSolicitations(self._raw_client, self._server, self._auth)

    @cached_property
    def wfs_inbound(self) -> AsyncWfsInbound:
        return AsyncWfsInbound(self._raw_client, self._server, self._auth)

    async def aclose(self) -> None:
        await self._raw_client.http_client.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        await self.aclose()


AsyncClient = AsyncWalmartApisClient
