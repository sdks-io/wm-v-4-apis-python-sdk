<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductPricing — operations

Accessor: `client.product_pricing` · Source: `walmart_apis/apis/product_pricing.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.product_pricing.get_buybox_offer_expected_price_batch

- **Route**: `POST /v4/pricing/product-batches/offer/buybox-offer-expected-price`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_buybox_offer_expected_price_batch(body: GetBuyboxOfferExpectedPriceBatchRequest | GetBuyboxOfferExpectedPriceBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetBuyboxOfferExpectedPriceBatchResponse`
- **Returns (raw)**: `ApiResult[GetBuyboxOfferExpectedPriceBatchResponse, GetBuyboxOfferExpectedPriceBatchErrorBody]`
- **Error**: `GetBuyboxOfferExpectedPriceBatchErrorBody` — **Case A (typed)**
- **Error arms**: `list[ErrorCatalogItems]` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetBuyboxOfferExpectedPriceBatchRequest` | `walmart_apis/models/get_buybox_offer_expected_price_batch_request.py` |
| `GetBuyboxOfferExpectedPriceBatchRequestDict` | `walmart_apis/models/get_buybox_offer_expected_price_batch_request.py` |
| `GetBuyboxOfferExpectedPriceBatchResponse` | `walmart_apis/models/get_buybox_offer_expected_price_batch_response.py` |
| `GetBuyboxOfferExpectedPriceBatchErrorBody` | `walmart_apis/errors/get_buybox_offer_expected_price_batch_error.py` |
| `ErrorCatalogItems` | `walmart_apis/models/error_catalog_items.py` |

### client.product_pricing.get_competitive_pricing

- **Route**: `GET /v4/pricing/products/competitive-price`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_competitive_pricing(*, item_type: ItemTypeOrStr = ItemType.SKU, skus: list[str] | None = None, walmart_item_ids: list[str] | None = None, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `item_type` — query `ItemType` · `skus` — query `Skus` · `walmart_item_ids` — query `walmartItemIds` · `customer_type` — query `CustomerType`
- **Returns (parsed)**: `GetPricingResponse`
- **Returns (raw)**: `ApiResult[GetPricingResponse, GetCompetitivePricingErrorBody]`
- **Error**: `GetCompetitivePricingErrorBody` — **Case A (typed)**
- **Error arms**: `list[ErrorCatalogItems]` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ItemTypeOrStr` | `walmart_apis/models/enums/item_type.py` |
| `CustomerTypeOrStr` | `walmart_apis/models/enums/customer_type.py` |
| `GetPricingResponse` | `walmart_apis/models/get_pricing_response.py` |
| `GetCompetitivePricingErrorBody` | `walmart_apis/errors/get_competitive_pricing_error.py` |
| `ErrorCatalogItems` | `walmart_apis/models/error_catalog_items.py` |

### client.product_pricing.get_competitive_summary

- **Route**: `POST /v4/pricing/product-batches/items/competitive-summary`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_competitive_summary(body: CompetitiveSummaryBatchRequest | CompetitiveSummaryBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CompetitiveSummaryBatchResponse`
- **Returns (raw)**: `ApiResult[CompetitiveSummaryBatchResponse, GetCompetitiveSummaryErrorBody]`
- **Error**: `GetCompetitiveSummaryErrorBody` — **Case A (typed)**
- **Error arms**: `list[ErrorCatalogItems]` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CompetitiveSummaryBatchRequest` | `walmart_apis/models/competitive_summary_batch_request.py` |
| `CompetitiveSummaryBatchRequestDict` | `walmart_apis/models/competitive_summary_batch_request.py` |
| `CompetitiveSummaryBatchResponse` | `walmart_apis/models/competitive_summary_batch_response.py` |
| `GetCompetitiveSummaryErrorBody` | `walmart_apis/errors/get_competitive_summary_error.py` |
| `ErrorCatalogItems` | `walmart_apis/models/error_catalog_items.py` |

### client.product_pricing.get_item_offers

- **Route**: `GET /v4/pricing/products/items/{item-id}/offers`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_item_offers(item_id: str, item_condition: ConditionTypeProductPricingOrStr, *, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `item_id`, `item_condition`
- **Params**: `item_id` — path `item-id` · `item_condition` — query `ItemCondition` · `customer_type` — query `CustomerType`
- **Returns (parsed)**: `GetOffersResponse`
- **Returns (raw)**: `ApiResult[GetOffersResponse, GetItemOffersErrorBody]`
- **Error**: `GetItemOffersErrorBody` — **Case A (typed)**
- **Error arms**: `list[ErrorCatalogItems]` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConditionTypeProductPricingOrStr` | `walmart_apis/models/enums/condition_type_product_pricing.py` |
| `CustomerTypeOrStr` | `walmart_apis/models/enums/customer_type.py` |
| `GetOffersResponse` | `walmart_apis/models/get_offers_response.py` |
| `GetItemOffersErrorBody` | `walmart_apis/errors/get_item_offers_error.py` |
| `ErrorCatalogItems` | `walmart_apis/models/error_catalog_items.py` |

### client.product_pricing.get_item_offers_batch

- **Route**: `POST /v4/pricing/product-batches/item-offers`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_item_offers_batch(body: GetItemOffersBatchRequest | GetItemOffersBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetItemOffersBatchResponse`
- **Returns (raw)**: `ApiResult[GetItemOffersBatchResponse, GetItemOffersBatchErrorBody]`
- **Error**: `GetItemOffersBatchErrorBody` — **Case A (typed)**
- **Error arms**: `list[ErrorCatalogItems]` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetItemOffersBatchRequest` | `walmart_apis/models/get_item_offers_batch_request.py` |
| `GetItemOffersBatchRequestDict` | `walmart_apis/models/get_item_offers_batch_request.py` |
| `GetItemOffersBatchResponse` | `walmart_apis/models/get_item_offers_batch_response.py` |
| `GetItemOffersBatchErrorBody` | `walmart_apis/errors/get_item_offers_batch_error.py` |
| `ErrorCatalogItems` | `walmart_apis/models/error_catalog_items.py` |

### client.product_pricing.get_listing_offers

- **Route**: `GET /v4/pricing/products/listings/{seller-sku}/offers`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_listing_offers(seller_sku: str, item_condition: ConditionTypeProductPricingOrStr, *, customer_type: CustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `seller_sku`, `item_condition`
- **Params**: `seller_sku` — path `seller-sku` · `item_condition` — query `ItemCondition` · `customer_type` — query `CustomerType`
- **Returns (parsed)**: `GetOffersResponse`
- **Returns (raw)**: `ApiResult[GetOffersResponse, GetListingOffersErrorBody]`
- **Error**: `GetListingOffersErrorBody` — **Case A (typed)**
- **Error arms**: `list[ErrorCatalogItems]` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConditionTypeProductPricingOrStr` | `walmart_apis/models/enums/condition_type_product_pricing.py` |
| `CustomerTypeOrStr` | `walmart_apis/models/enums/customer_type.py` |
| `GetOffersResponse` | `walmart_apis/models/get_offers_response.py` |
| `GetListingOffersErrorBody` | `walmart_apis/errors/get_listing_offers_error.py` |
| `ErrorCatalogItems` | `walmart_apis/models/error_catalog_items.py` |

### client.product_pricing.get_listing_offers_batch

- **Route**: `POST /v4/pricing/product-batches/listing-offers`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_listing_offers_batch(body: GetListingOffersBatchRequest | GetListingOffersBatchRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GetListingOffersBatchResponse`
- **Returns (raw)**: `ApiResult[GetListingOffersBatchResponse, GetListingOffersBatchErrorBody]`
- **Error**: `GetListingOffersBatchErrorBody` — **Case A (typed)**
- **Error arms**: `list[ErrorCatalogItems]` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetListingOffersBatchRequest` | `walmart_apis/models/get_listing_offers_batch_request.py` |
| `GetListingOffersBatchRequestDict` | `walmart_apis/models/get_listing_offers_batch_request.py` |
| `GetListingOffersBatchResponse` | `walmart_apis/models/get_listing_offers_batch_response.py` |
| `GetListingOffersBatchErrorBody` | `walmart_apis/errors/get_listing_offers_batch_error.py` |
| `ErrorCatalogItems` | `walmart_apis/models/error_catalog_items.py` |

### client.product_pricing.get_pricing

- **Route**: `GET /v4/pricing/products/price`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_pricing(*, item_type: ItemTypeOrStr = ItemType.SKU, skus: list[str] | None = None, walmart_item_ids: list[str] | None = None, item_condition: ConditionTypeProductPricingOrStr | None = None, offer_type: OfferCustomerTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `item_type` — query `ItemType` · `skus` — query `Skus` · `walmart_item_ids` — query `walmartItemIds` · `item_condition` — query `ItemCondition` · `offer_type` — query `OfferType`
- **Returns (parsed)**: `GetPricingResponse`
- **Returns (raw)**: `ApiResult[GetPricingResponse, GetPricingErrorBody]`
- **Error**: `GetPricingErrorBody` — **Case A (typed)**
- **Error arms**: `list[ErrorCatalogItems]` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ItemTypeOrStr` | `walmart_apis/models/enums/item_type.py` |
| `ConditionTypeProductPricingOrStr` | `walmart_apis/models/enums/condition_type_product_pricing.py` |
| `OfferCustomerTypeOrStr` | `walmart_apis/models/enums/offer_customer_type.py` |
| `GetPricingResponse` | `walmart_apis/models/get_pricing_response.py` |
| `GetPricingErrorBody` | `walmart_apis/errors/get_pricing_error.py` |
| `ErrorCatalogItems` | `walmart_apis/models/error_catalog_items.py` |

