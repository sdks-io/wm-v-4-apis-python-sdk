from __future__ import annotations

from functools import cached_property
from types import TracebackType

from typing_extensions import Self

from .apis.authorization import Authorization
from .apis.catalog import Catalog
from .apis.data_kiosk import DataKiosk
from .apis.disputes import Disputes
from .apis.feeds import Feeds
from .apis.final_payout import FinalPayout
from .apis.finances import Finances
from .apis.fulfillment_outbound import FulfillmentOutbound
from .apis.inventory import Inventory
from .apis.listings_items import ListingsItems
from .apis.listings_restrictions import ListingsRestrictions
from .apis.merchant_fulfillment import MerchantFulfillment
from .apis.messaging import Messaging
from .apis.notifications import Notifications
from .apis.orders import Orders
from .apis.payouts import Payouts
from .apis.product_fees import ProductFees
from .apis.product_pricing import ProductPricing
from .apis.product_type_definitions import ProductTypeDefinitions
from .apis.reconciliation import Reconciliation
from .apis.report_schedules import ReportSchedules
from .apis.reports import Reports
from .apis.sales import Sales
from .apis.sellers import Sellers
from .apis.settlement import Settlement
from .apis.shipping import Shipping
from .apis.solicitations import Solicitations
from .apis.supply_source_api import SupplySourceApi
from .apis.uploads import Uploads
from .apis.wfs_inbound import WfsInbound
from .apis.wfs_inventory import WfsInventory
from .auth import AuthSchemes, SellerAuthAuthorizationCodeScope, SellerAuthClientCredentialsScope, WalletAuthScope
from .base_client import DEFAULT_TIMEOUT, BaseWalmartApisClient
from .core import (
    OPERATING_SYSTEM,
    PYTHON_RUNTIME,
    AuthorizationCodeCredentials,
    AuthorizationCodeCredentialsOrDict,
    AuthorizationCodeTokenSource,
    BasicAuthCredentials,
    BasicAuthCredentialsOrDict,
    BasicAuthScheme,
    ClientCredentials,
    ClientCredentialsOrDict,
    ClientCredentialsTokenSource,
    HttpClient,
    Httpx2Client,
    LoggingOptionsOrDict,
    OAuth2RefreshableScheme,
    OAuth2Scheme,
    RawClient,
    RefreshableTokenSource,
    RetryOptionsOrDict,
    TokenSource,
    client_secret_basic,
    no_auth,
    param,
)
from .server.environment import Environment
from .server.server_config import ServerConfigOrDict


class WalmartApisClient(BaseWalmartApisClient[RawClient]):
    def __init__(
        self,
        *,
        environment: Environment = "production",
        timeout: float = DEFAULT_TIMEOUT,
        server_config: ServerConfigOrDict | None = None,
        retry_options: int | RetryOptionsOrDict | None = None,
        logging_options: LoggingOptionsOrDict | None = None,
        custom_http_client: HttpClient | None = None,
        seller_auth_authorization_code: (
            AuthorizationCodeCredentialsOrDict[SellerAuthAuthorizationCodeScope] | None
        ) = None,
        seller_auth_authorization_code_token_source: (
            RefreshableTokenSource[AuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope]] | None
        ) = None,
        seller_auth_client_credentials: ClientCredentialsOrDict[SellerAuthClientCredentialsScope] | None = None,
        seller_auth_client_credentials_token_source: (
            TokenSource[ClientCredentials[SellerAuthClientCredentialsScope]] | None
        ) = None,
        basic_client_auth: BasicAuthCredentialsOrDict | None = None,
        wallet_auth: ClientCredentialsOrDict[WalletAuthScope] | None = None,
        wallet_auth_token_source: TokenSource[ClientCredentials[WalletAuthScope]] | None = None,
    ) -> None:
        super().__init__(
            environment=environment,
            timeout=timeout,
            server_config=server_config,
            retry_options=retry_options,
            logging_options=logging_options,
        )
        self._raw_client = RawClient(
            http_client=custom_http_client if custom_http_client is not None else Httpx2Client(timeout=timeout),
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
        self._auth = AuthSchemes(
            seller_auth_authorization_code=(
                OAuth2RefreshableScheme(
                    credentials=AuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope].coerce(
                        seller_auth_authorization_code
                    ),
                    source=(
                        seller_auth_authorization_code_token_source
                        if seller_auth_authorization_code_token_source is not None
                        else AuthorizationCodeTokenSource[SellerAuthAuthorizationCodeScope](
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
                OAuth2Scheme(
                    credentials=ClientCredentials[SellerAuthClientCredentialsScope].coerce(
                        seller_auth_client_credentials
                    ),
                    source=(
                        seller_auth_client_credentials_token_source
                        if seller_auth_client_credentials_token_source is not None
                        else ClientCredentialsTokenSource[SellerAuthClientCredentialsScope](
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
                OAuth2Scheme(
                    credentials=ClientCredentials[WalletAuthScope].coerce(wallet_auth),
                    source=(
                        wallet_auth_token_source
                        if wallet_auth_token_source is not None
                        else ClientCredentialsTokenSource[WalletAuthScope](
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
    def authorization(self) -> Authorization:
        return Authorization(self._raw_client, self._server, self._auth)

    @cached_property
    def catalog(self) -> Catalog:
        return Catalog(self._raw_client, self._server, self._auth)

    @cached_property
    def data_kiosk(self) -> DataKiosk:
        return DataKiosk(self._raw_client, self._server, self._auth)

    @cached_property
    def disputes(self) -> Disputes:
        return Disputes(self._raw_client, self._server, self._auth)

    @cached_property
    def feeds(self) -> Feeds:
        return Feeds(self._raw_client, self._server, self._auth)

    @cached_property
    def final_payout(self) -> FinalPayout:
        return FinalPayout(self._raw_client, self._server, self._auth)

    @cached_property
    def finances(self) -> Finances:
        return Finances(self._raw_client, self._server, self._auth)

    @cached_property
    def fulfillment_outbound(self) -> FulfillmentOutbound:
        return FulfillmentOutbound(self._raw_client, self._server, self._auth)

    @cached_property
    def inventory(self) -> Inventory:
        return Inventory(self._raw_client, self._server, self._auth)

    @cached_property
    def listings_items(self) -> ListingsItems:
        return ListingsItems(self._raw_client, self._server, self._auth)

    @cached_property
    def listings_restrictions(self) -> ListingsRestrictions:
        return ListingsRestrictions(self._raw_client, self._server, self._auth)

    @cached_property
    def merchant_fulfillment(self) -> MerchantFulfillment:
        return MerchantFulfillment(self._raw_client, self._server, self._auth)

    @cached_property
    def orders(self) -> Orders:
        return Orders(self._raw_client, self._server, self._auth)

    @cached_property
    def payouts(self) -> Payouts:
        return Payouts(self._raw_client, self._server, self._auth)

    @cached_property
    def product_type_definitions(self) -> ProductTypeDefinitions:
        return ProductTypeDefinitions(self._raw_client, self._server, self._auth)

    @cached_property
    def reconciliation(self) -> Reconciliation:
        return Reconciliation(self._raw_client, self._server, self._auth)

    @cached_property
    def report_schedules(self) -> ReportSchedules:
        return ReportSchedules(self._raw_client, self._server, self._auth)

    @cached_property
    def reports(self) -> Reports:
        return Reports(self._raw_client, self._server, self._auth)

    @cached_property
    def sellers(self) -> Sellers:
        return Sellers(self._raw_client, self._server, self._auth)

    @cached_property
    def settlement(self) -> Settlement:
        return Settlement(self._raw_client, self._server, self._auth)

    @cached_property
    def supply_source_api(self) -> SupplySourceApi:
        return SupplySourceApi(self._raw_client, self._server, self._auth)

    @cached_property
    def uploads(self) -> Uploads:
        return Uploads(self._raw_client, self._server, self._auth)

    @cached_property
    def wfs_inventory(self) -> WfsInventory:
        return WfsInventory(self._raw_client, self._server, self._auth)

    @cached_property
    def messaging(self) -> Messaging:
        return Messaging(self._raw_client, self._server, self._auth)

    @cached_property
    def notifications(self) -> Notifications:
        return Notifications(self._raw_client, self._server, self._auth)

    @cached_property
    def product_fees(self) -> ProductFees:
        return ProductFees(self._raw_client, self._server, self._auth)

    @cached_property
    def product_pricing(self) -> ProductPricing:
        return ProductPricing(self._raw_client, self._server, self._auth)

    @cached_property
    def sales(self) -> Sales:
        return Sales(self._raw_client, self._server, self._auth)

    @cached_property
    def shipping(self) -> Shipping:
        return Shipping(self._raw_client, self._server, self._auth)

    @cached_property
    def solicitations(self) -> Solicitations:
        return Solicitations(self._raw_client, self._server, self._auth)

    @cached_property
    def wfs_inbound(self) -> WfsInbound:
        return WfsInbound(self._raw_client, self._server, self._auth)

    def close(self) -> None:
        self._raw_client.http_client.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self, exc_type: type[BaseException] | None, exc: BaseException | None, exc_tb: TracebackType | None
    ) -> None:
        self.close()


Client = WalmartApisClient
