from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, TypeAlias

from .core import AsyncAuthScheme, AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AuthSchemes:
    seller_auth_authorization_code: AuthScheme
    seller_auth_client_credentials: AuthScheme
    basic_client_auth: AuthScheme
    wallet_auth: AuthScheme


@dataclass(frozen=True, slots=True, kw_only=True)
class AsyncAuthSchemes:
    seller_auth_authorization_code: AsyncAuthScheme
    seller_auth_client_credentials: AsyncAuthScheme
    basic_client_auth: AsyncAuthScheme
    wallet_auth: AsyncAuthScheme


SellerAuthAuthorizationCodeScope: TypeAlias = Literal[
    "seller-api:catalog:read",
    "seller-api:catalog:write",
    "seller-api:listings:read",
    "seller-api:listings:write",
    "seller-api:orders:read",
    "seller-api:orders:write",
    "seller-api:fulfillment:read",
    "seller-api:fulfillment:write",
    "seller-api:merchant-fulfillment:read",
    "seller-api:merchant-fulfillment:write",
    "seller-api:inventory:read",
    "seller-api:inventory:write",
    "seller-api:pricing:read",
    "seller-api:pricing:write",
    "seller-api:feeds:read",
    "seller-api:feeds:write",
    "seller-api:uploads:write",
    "seller-api:reports:read",
    "seller-api:analytics:read",
    "seller-api:sellers:read",
    "seller-api:finances:read",
    "seller-api:notifications:read",
    "seller-api:notifications:write",
    "offline_access",
]
"""``seller-api:catalog:read``: Read product catalog items, attributes, and metadata. ``seller-api:catalog:write``:
Create and update catalog items. ``seller-api:listings:read``: Read listing items and listing restrictions.
``seller-api:listings:write``: Create and update listing items. ``seller-api:orders:read``: Read seller orders, order
lines, and order status. ``seller-api:orders:write``: Acknowledge, ship, and cancel order lines.
``seller-api:fulfillment:read``: Read WFS fulfillment orders and shipment status. ``seller-api:fulfillment:write``:
Create, update, and cancel WFS fulfillment orders. ``seller-api:merchant-fulfillment:read``: Read merchant-fulfilled
shipment rates and labels. ``seller-api:merchant-fulfillment:write``: Create merchant-fulfilled shipment labels.
``seller-api:inventory:read``: Read inventory levels and supply detail. ``seller-api:inventory:write``: Update inventory
quantities and fulfillment center feeds. ``seller-api:pricing:read``: Read product pricing and competitive price data.
``seller-api:pricing:write``: Update product pricing rules. ``seller-api:feeds:read``: Read feed processing status and
feed document metadata. ``seller-api:feeds:write``: Submit bulk feeds for catalog, inventory, and pricing updates.
``seller-api:uploads:write``: Create upload destinations (pre-signed URLs) for feed documents.
``seller-api:reports:read``: Request and download seller performance and analytics reports.
``seller-api:analytics:read``: Submit and retrieve Data Kiosk analytics queries and documents.
``seller-api:sellers:read``: Read seller account information and marketplace participation.
``seller-api:finances:read``: Read financial events, settlements, and transaction history.
``seller-api:notifications:read``: Read notification subscriptions and delivery status.
``seller-api:notifications:write``: Create, update, and delete notification subscriptions. ``offline_access``: Issue a
refresh token (OIDC-standard; enables long-lived delegated access)."""

SellerAuthClientCredentialsScope: TypeAlias = Literal[
    "seller-api:catalog:read",
    "seller-api:catalog:write",
    "seller-api:listings:read",
    "seller-api:listings:write",
    "seller-api:orders:read",
    "seller-api:orders:write",
    "seller-api:fulfillment:read",
    "seller-api:fulfillment:write",
    "seller-api:merchant-fulfillment:read",
    "seller-api:merchant-fulfillment:write",
    "seller-api:inventory:read",
    "seller-api:inventory:write",
    "seller-api:pricing:read",
    "seller-api:pricing:write",
    "seller-api:feeds:read",
    "seller-api:feeds:write",
    "seller-api:uploads:write",
    "seller-api:reports:read",
    "seller-api:analytics:read",
    "seller-api:sellers:read",
    "seller-api:finances:read",
    "seller-api:notifications:read",
    "seller-api:notifications:write",
]
"""``seller-api:catalog:read``: Read product catalog items, attributes, and metadata. ``seller-api:catalog:write``:
Create and update catalog items. ``seller-api:listings:read``: Read listing items and listing restrictions.
``seller-api:listings:write``: Create and update listing items. ``seller-api:orders:read``: Read seller orders, order
lines, and order status. ``seller-api:orders:write``: Acknowledge, ship, and cancel order lines.
``seller-api:fulfillment:read``: Read WFS fulfillment orders and shipment status. ``seller-api:fulfillment:write``:
Create, update, and cancel WFS fulfillment orders. ``seller-api:merchant-fulfillment:read``: Read merchant-fulfilled
shipment rates and labels. ``seller-api:merchant-fulfillment:write``: Create merchant-fulfilled shipment labels.
``seller-api:inventory:read``: Read inventory levels and supply detail. ``seller-api:inventory:write``: Update inventory
quantities and fulfillment center feeds. ``seller-api:pricing:read``: Read product pricing and competitive price data.
``seller-api:pricing:write``: Update product pricing rules. ``seller-api:feeds:read``: Read feed processing status and
feed document metadata. ``seller-api:feeds:write``: Submit bulk feeds for catalog, inventory, and pricing updates.
``seller-api:uploads:write``: Create upload destinations (pre-signed URLs) for feed documents.
``seller-api:reports:read``: Request and download seller performance and analytics reports.
``seller-api:analytics:read``: Submit and retrieve Data Kiosk analytics queries and documents.
``seller-api:sellers:read``: Read seller account information and marketplace participation.
``seller-api:finances:read``: Read financial events, settlements, and transaction history.
``seller-api:notifications:read``: Read notification subscriptions and delivery status.
``seller-api:notifications:write``: Create, update, and delete notification subscriptions."""

WalletAuthScope: TypeAlias = Literal[
    "catalog:read",
    "analytics:read",
    "feeds:read",
    "feeds:write",
    "read",
    "write",
    "fulfillment:read",
    "fulfillment:write",
    "inventory:read",
    "inventory:write",
    "listings:read",
    "listings:write",
    "orders:read",
    "orders:write",
    "disbursements:read",
    "disbursements:write",
    "finances:read",
    "pricing:read",
    "definitions:read",
    "reports:read",
    "reports:write",
    "sellers:read",
    "shipping:read",
    "shipping:write",
    "uploads:write",
]
"""``catalog:read``: Read catalog data. ``analytics:read``: Submit and retrieve Data Kiosk analytics queries and
documents. ``feeds:read``: Read feed status. ``feeds:write``: Submit feeds. ``read``: Read access. ``write``: Write
access. ``fulfillment:read``: Read WFS fulfillment orders and shipments, Read eligible shipping services.
``fulfillment:write``: Create, update, and cancel WFS fulfillment orders, Purchase and cancel shipping labels.
``inventory:read``: Read inventory data. ``inventory:write``: Update inventory quantities. ``listings:read``: Read
listings items, Read listing restrictions for items. ``listings:write``: Create, update, patch, and delete listings
items. ``orders:read``: Read orders. ``orders:write``: Acknowledge, ship, cancel orders. ``disbursements:read``: Read
settlement, reconciliation, and payout data. ``disbursements:write``: Initiate and configure payout operations.
``finances:read``: Read financial event groups and financial events. ``pricing:read``: Read seller pricing and
competitive pricing data. ``definitions:read``: Read product type definitions. ``reports:read``: Read and download
seller reports and schedules. ``reports:write``: Create and cancel reports and schedules. ``sellers:read``: Read seller
account and marketplace participation info. ``shipping:read``: Read shipping rates, tracking, documents, and access
points. ``shipping:write``: Purchase, cancel, and submit NDR feedback on shipments. ``uploads:write``: Create upload
destinations for feed and report documents."""
