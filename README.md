# Walmart APIs SDK

[![Built with APIMatic][apimatic-badge]][apimatic-url] [![License: MIT][license-badge]][license-url] [![Python 3.10+][python-badge]][python-url]

The Walmart APIs SDK for Python provides access to the Walmart APIs REST APIs from Python applications.

> [!TIP]
> **Looking for a specific signature, model, enum, or error type?** This SDK ships a generated
> **[SDK map](sdk-map.md)** -- a lookup index of the SDK's entire Python surface. Consult it before
> scanning the source tree; details under [SDK map](#sdk-map).

Use the Authorization API to obtain OAuth access tokens for Walmart Marketplace V4 APIs.

Seller applications can use the `client_credentials` grant to obtain an access token.
Solution Provider applications can use the `authorization_code` grant for delegated
access and the `refresh_token` grant when a refresh token is available.

`POST /v4/auth/token` supports the following grant types:

- `client_credentials` for seller-direct authorization.
- `authorization_code` for delegated Solution Provider authorization.
- `refresh_token` for delegated authorization using a previously issued refresh token.

Public clients using the `authorization_code` grant must use Proof Key for Code
Exchange (PKCE) with the `S256` challenge method. Confidential clients can
authenticate at the token operation as described in the operation requirements.

Access tokens use the `Bearer` token type. Send the access token with Marketplace
V4 API requests as `Authorization: Bearer <token>`. Do not use
`WM_SEC.ACCESS_TOKEN` for V4 requests.

Treat access tokens, refresh tokens, and client secrets as sensitive values and
do not log them.
, The Catalog Items API lets you search for products in the Walmart Marketplace
catalog and retrieve detailed catalog item information. Search by keywords,
Walmart Item IDs, GTINs, UPCs, or seller SKUs, and retrieve product attributes,
identifiers, images, product types, and other available catalog information., Submit analytics queries and retrieve structured data from Walmart's
data platform. Modeled after Walmart Seller API Data Kiosk API.

ADR pending: GraphQL vs REST query language — see docs/adr/ once filed.
Until the ADR resolves, the query body is treated as an opaque string.

**Pod Owner:** Pod 4 — Feeds & Reports
**Implementation target:** Walmart Analytics / Data Platform, Submit bulk data to Walmart Marketplace via asynchronous feed processing.
Sellers submit a feed file in a single API call; the server handles
document storage and initiates async processing. Poll feed status
with the feedId returned in the submission response.

**Pod Owner:** Pod 4 — Feeds & Reports
**Implementation target:** Walmart Feed Service / Bulk Operations, Use the Walmart Fulfillment Services (WFS) Inbound Plans API to create and manage inbound plans for shipments
to Walmart fulfillment centers., WFS Inbound Delivery Windows, Self-Ship Appointments & Operation Status API. Walmart Seller API — Fulfillment Inbound contract.
Terminology: WFS = Walmart Fulfillment Services, Ship Node = fulfillment center., WFS Inbound Packing. Walmart Seller API — Fulfillment Inbound contract.
Terminology: WFS = Walmart Fulfillment Services, Ship Node = fulfillment center., WFS Inbound Packing & Placement API. Walmart Seller API — Fulfillment Inbound contract.
Terminology: WFS = Walmart Fulfillment Services, Ship Node = fulfillment center., WFS Inbound Items, Compliance, Labels & Prep API. Walmart Seller API — Fulfillment Inbound contract.
Terminology: WFS = Walmart Fulfillment Services, Ship Node = fulfillment center., WFS Inbound Shipments API. Walmart Seller API — Fulfillment Inbound contract.
Terminology: WFS = Walmart Fulfillment Services, Ship Node = fulfillment center., Create and manage WFS (Walmart Fulfillment Services) outbound fulfillment orders.
Sellers ship inventory to Walmart ship nodes; Walmart picks, packs, and ships
to end customers.


**Pod Owner:** Pod 2 — Orders & Fulfillment
**Implementation target:** WFS Outbound / Ship Node Service


**Delivery priority:** Phase 2 — Pod 2 is prioritizing `fulfillment-inbound`
first. See `PHASE-2.md` in this service's directory for what that does and
doesn't mean (bug/honesty fixes still welcome; new endpoints on hold)., Manage seller inventory on the Walmart Marketplace.


**Pod Owner:** Pod 3 — Inventory & Pricing
**Implementation target:** Walmart Inventory Service, Create, fully update, patch, and delete listings items for sellers on the
Walmart Marketplace. Modeled after Walmart Seller API Listings Items API.

**Pod Owner:** Pod 1 — Items & Catalog
**Implementation target:** Walmart Item Setup Service, Get information about listing restrictions on items in the Walmart Marketplace.
Identifies compliance blocks, category restrictions, and approval requirements.


**Pod Owner:** Pod 3 — Inventory & Pricing
**Implementation target:** Walmart Item Compliance / Restriction Service, SUPERSEDED — NOT SCHEDULED FOR IMPLEMENTATION.
the Merchant Fulfillment API is obsolete: its operations are covered by
the Shipping API, and both front the same upstream (Ship With Walmart).
Per Suresh's SWW-consolidation analysis, every operation below is marked
counts toward Pod 2 implementation scope. This spec is retained for
reference only (tombstone) — no code is being built against it. New
seller-fulfilled shipping work goes to the Shipping API.

Tracking: (this deprecation). The one partial-coverage gap
(MFN full-record `getShipment` has no single the Shipping API equivalent)
is owned by Suresh for decision in .

---
Get eligible shipping services and purchase shipping labels for seller-fulfilled
orders. Modeled after Walmart Seller API Merchant Fulfillment API.

**Pod Owner:** Pod 2 — Orders & Fulfillment
**Implementation target:** Ship With Walmart (SWW) — SWW-LABEL-SERVICE
(internal `/v3/sww/labels/*` synchronous REST; see
docs/mapper/mfn-mapper-feasibility.md), Use the Orders API to retrieve and manage Walmart Marketplace orders, including order details, order lines, fulfillment
updates, cancellations, refunds, and delivery information., Unified Payments domain API for Walmart Marketplace sellers.
Consolidates Pod 5 (Finances / financial event reporting) and Pod 6
(Outbound Payments — settlement, reconciliation, payout execution) into a
single service under the Payments domain .

**Category A (7 routes):** Reporting — delegated to mp-payment-reporting upstream.
**Category B (9 routes):** Execution — delegated to GMPPayments upstream.
**Finances (4 routes):** Financial event reporting — delegated to GMP partnerTxnSearch
and commission endpoints (, ).

Routes with x-walmart-pii: true contain order/seller PII and require an RDT
issued by the Tokens service (Pod 0, ) in production.

**Domain Owner:** Payments Domain (consolidated Pod 5 + Pod 6)
**Tech Lead:** @cssehga
**Replaces:** the payments settlement backend (v3 BFF); the Payments API (Pod 5), The Product Pricing API retrieves pricing and offer information for seller items, compares competitive pricing, and returns the lowest-priced offers for Walmart items. Batch operations retrieve offer information for multiple items or seller SKUs in a single request., The Product Fees API returns estimated fees for seller items based on item, pricing, and fulfillment information., Retrieve Walmart product type definitions, attribute schemas, and
item classification rules used when setting up seller listings.

**Pod Owner:** Pod 1 — Items & Catalog
**Implementation target:** Walmart Item Classification Service, Create, cancel, and retrieve seller reports.
Supports scheduled and on-demand reports with async processing.


**Pod Owner:** Pod 4 — Feeds & Reports
**Implementation target:** Walmart Seller Reporting Service, Walmart Seller API contract for sales metrics., Walmart Seller API contract for messaging., Walmart Seller API contract for notifications., Walmart Seller API contract for solicitations., Retrieve information about a seller's Walmart Marketplace account
and marketplace participations.


**Pod Owner:** Pod 5 — Seller & Finances
**Implementation target:** Walmart Seller Account Service / Seller Center, Shipping API for sellers to request rates, purchase shipping labels,
track shipments, and manage delivery exceptions across Walmart
Marketplace and WFS channels.

Surface aligned with industry SP-API Shipping v2. Pod 2 — Orders &
Fulfillment owns this service. Common types (Address, Money, Weight,
PackageDimensions) are inlined per Pod 2 convention, byte-identical to
the canonical copies in the Merchant Fulfillment API; (proposed)
defines the future promotion path to models/_shared/ once the Rule of
Three triggers a coordinated extraction PR., Shipping Management API for sellers to manage supply sources
(fulfillment centers / ship nodes). This service acts as a facade over
Aurora Fulfilment Services (AFS), applying field renaming and response
shaping for the WSA v4 contract., Create upload destinations (pre-signed URLs) for feed documents and
retrieve previously uploaded documents. Used in conjunction with the
Feeds service for async bulk operations.


Pre-signed URLs must not appear in logs — treat as secrets.

**Pod Owner:** Pod 4 — Feeds & Reports
**Implementation target:** Walmart Document Store / S3 pre-signed URLs

---

## Installation

To install the Python SDK from PyPI, with whichever package manager your project uses:

```bash
pip install wm-v-4-apis-sdk
```

```bash
uv add wm-v-4-apis-sdk
```

```bash
poetry add wm-v-4-apis-sdk
```

To install from the SDK source instead, give the tool a path containing a slash — a bare folder name is looked up on PyPI, and resolves to whatever project holds that name there:

```bash
pip install <path-to-sdk>
```

---

## Quick Start

### Synchronous client

Construct `WalmartApisClient` with keyword arguments, and call `close()` when you are done. Every argument is optional; the full list is in the [SDK map](sdk-map.md).

```python
from walmart_apis import WalmartApisClient
from walmart_apis.auth import SellerAuthAuthorizationCodeScope, SellerAuthClientCredentialsScope, WalletAuthScope
from walmart_apis.core import AuthorizationCodeCredentials, BasicAuthCredentials, ClientCredentials


def prompt(url: str) -> str:
    return input(f"Open {url}, then paste the code: ")


client = WalmartApisClient(
    seller_auth_authorization_code=AuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope](
        client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
    ),
    seller_auth_client_credentials=ClientCredentials[SellerAuthClientCredentialsScope](
        client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
    ),
    basic_client_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
    wallet_auth=ClientCredentials[WalletAuthScope](client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it -- `with WalmartApisClient(...) as client:` closes the pool on exit; see [Best Practices](#best-practices).

`Client` is exported as an alias of `WalmartApisClient`, so `from walmart_apis import Client` also works.

The SDK accepts every model-typed input in two interchangeable spellings, both type-checked: the typed model, or a plain dict with the same keys -- the `OrDict` and `Model | ModelDict` unions in the [SDK map](sdk-map.md). Pick whichever suits the call site: the dict form needs no import, while the model form adds a keyword-checked constructor and editor completion.

### Asynchronous client

`AsyncWalmartApisClient` mirrors `WalmartApisClient` with **identical method names**, and every endpoint method is a coroutine. It takes the same arguments, with some differences -- for example, the transport argument is `custom_async_http_client`.

```python
from asyncio import run, to_thread

from walmart_apis import AsyncWalmartApisClient
from walmart_apis.auth import SellerAuthAuthorizationCodeScope, SellerAuthClientCredentialsScope, WalletAuthScope
from walmart_apis.core import AsyncAuthorizationCodeCredentials, BasicAuthCredentials, ClientCredentials


async def prompt(url: str) -> str:
    print(f"Open {url}")
    return await to_thread(input, "Paste the code: ")


async def main() -> None:
    client = AsyncWalmartApisClient(
        seller_auth_authorization_code=AsyncAuthorizationCodeCredentials[SellerAuthAuthorizationCodeScope](
            client_id="YOUR_CLIENT_ID", redirect_uri="YOUR_REDIRECT_URI", prompt_for_authorization_code=prompt
        ),
        seller_auth_client_credentials=ClientCredentials[SellerAuthClientCredentialsScope](
            client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"
        ),
        basic_client_auth=BasicAuthCredentials(username="YOUR_USERNAME", password="YOUR_PASSWORD"),
        wallet_auth=ClientCredentials[WalletAuthScope](client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
        environment="production",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it -- `async with AsyncWalmartApisClient(...) as client:` closes the pool on exit. Only the async spelling is `aclose`, matching httpx2; see [Best Practices](#best-practices).

`AsyncClient` is the exported alias. Each client accepts **only** its own transport argument and its own prompt flavour; passing the other's is a `TypeError` at runtime and an error under mypy.

---

## Usage

Two generated references cover the SDK; each answers a different question:

| Reference | For |
| --- | --- |
| **[API Reference](api-reference.md)** | Usage guidance for a single **parsed** operation: `client.<group>.<operation>(...)` returns the typed payload and raises `ApiError` on any non-2xx, with `.error` the typed error body, or `RawError` for a status the operation does not document. |
| **[Raw API Reference](raw-api-reference.md)** | The same for the **raw** variant: `client.<group>.with_raw_response.<operation>(...)` returns `ApiResult[T, E]` and never raises for an API error. |

Both API references carry every one of the 184 operations, with a sync and an async sample and a parameter table each.

## SDK map

This SDK ships a generated **SDK map** -- [`sdk-map.md`](sdk-map.md) -- a deterministic, lookup-oriented table of contents of the SDK's Python surface, generated by APIMatic alongside this SDK.

Consult the map before scanning or grepping the source: it answers call-level contract questions by lookup, and for anything it does not carry -- model shapes, enum values, an endpoint's route or behavioural prose -- it names the one source file to read. How to read the map itself, including the SDK-wide defaults its rows rely on, is stated at the top of [`sdk-map.md`](sdk-map.md).

## Logging

The SDK logs every HTTP exchange through Python's standard `logging` module, under the `walmart_apis` logger, and configures nothing itself: with no logging set up, nothing is printed unless `WALMART_APIS_LOG` is set. Turn it on as for any library:

```python
import logging

logging.basicConfig()  # your application's handler; the root stays at WARNING
logging.getLogger("walmart_apis").setLevel(logging.INFO)  # the SDK's lines; DEBUG adds the dumps that logging_options turns on
```

Or set one environment variable before the process starts, for a run you cannot edit: `WALMART_APIS_LOG=info` writes the request and response lines, `WALMART_APIS_LOG=debug` adds the request headers, the request body and the response headers. If your application has configured logging, its handlers and format are used; otherwise the SDK writes to stderr.

Choose the detail with `logging_options`, a `LoggingOptions` from `walmart_apis.core`:

```python
from walmart_apis import WalmartApisClient
from walmart_apis.core import LoggingOptions

client = WalmartApisClient(
    logging_options=LoggingOptions(log_request_headers=True, log_response_headers=True, log_request_body=True)
)
```

A plain dict with the same keys is accepted too, as for every model-typed argument (see [Quick Start](#quick-start)): `logging_options={"log_request_headers": True}`.

| Option | Default | Effect |
| --- | --- | --- |
| `log_request_headers` | `False` | Log the sent headers at DEBUG, masked. |
| `log_response_headers` | `False` | Log the received headers at DEBUG, masked. |
| `log_request_body` | `False` | Log the request body at DEBUG: its text when in memory, a description when streamed. |
| `body_size_limit` | `32768` | Bytes of a logged body kept before it is cut. |
| `redaction_placeholder` | `"REDACTED"` | What a hidden value prints as. |
| `unmask_headers` | none | Header names to show although they are not on the safe list. |
| `mask_headers` | none | Header names to hide although they are on the safe list. |
| `mask_keys` | 11 credential names | Query and form keys whose values are always hidden; naming a set replaces the default. |

A single call can be quietened with `request_options={"log_level": logging.WARNING}`: records below that level are not written for that call. It never turns on a record the client's options leave off. Header, query and form values print `REDACTED` unless known safe; a JSON body is printed as sent, so enable `log_request_body` only where its content may be logged; a response body is never logged. The levels and every field are under **Logging** in the SDK map.

## Best Practices

> [!TIP]
> Use a **single `WalmartApisClient` instance** for the lifetime of your application and reuse it across
> all requests. Each instance owns its own connection pool, so an instance per request forfeits
> connection reuse and leaks pools that are never closed.

Match the disposal to the client's lifetime: an application-lifetime client is closed once at shutdown with `close()` / `aclose()`; where the lifetime fits a block, `with WalmartApisClient() as client:` / `async with AsyncWalmartApisClient() as client:` releases it automatically. Both are idempotent, but a closed client is not reusable: the next call raises. The client closes **whatever transport it holds**, including one you supplied via `custom_http_client` / `custom_async_http_client`; if you intend to reuse your own transport across clients, don't hand its lifetime to a `with` block.

**Retries are on by default**: a failed idempotent request — a retryable status or no response at all — is sent again up to three times before the call gives up. Pass `retry_options=0` to turn it off, for instance in a test that stubs an error response; the policy and its defaults are under **Retries** in the SDK map.

## License

This SDK is distributed under the [MIT License][license-url].

---

## Support

Refer to the [API reference](api-reference.md) for detailed information on available operations with code samples.

For further assistance, please contact support at pod-0@sellers.walmart.com.

---

[license-url]: LICENSE
[license-badge]: https://img.shields.io/badge/License-MIT-blue.svg
[apimatic-url]: https://www.apimatic.io
[apimatic-badge]: https://www.apimatic.io/hubfs/Built-with-APIMatic-badge.svg
[python-url]: https://www.python.org/downloads/
[python-badge]: https://img.shields.io/badge/python-3.10%2B-blue.svg
