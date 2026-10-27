<!-- Generated file — do not edit; regenerated with the SDK. -->

# ListingsRestrictions — operations

Accessor: `client.listings_restrictions` · Source: `walmart_apis/apis/listings_restrictions.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.listings_restrictions.get_listings_restrictions

- **Route**: `GET /listings/v4/restrictions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_listings_restrictions(asin: str, condition_type: ConditionType1OrStr, seller_id: str, marketplace_ids: list[str], *, reason_locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `asin`, `condition_type`, `seller_id`, `marketplace_ids`
- **Params**: `asin` — query · `condition_type` — query `conditionType` · `seller_id` — query `sellerId` · `marketplace_ids` — query `marketplaceIds` · `reason_locale` — query `reasonLocale`
- **Returns (parsed)**: `RestrictionList`
- **Returns (raw)**: `ApiResult[RestrictionList, GetListingsRestrictionsErrorBody]`
- **Error**: `GetListingsRestrictionsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConditionType1OrStr` | `walmart_apis/models/enums/condition_type1.py` |
| `RestrictionList` | `walmart_apis/models/restriction_list.py` |
| `GetListingsRestrictionsErrorBody` | `walmart_apis/errors/get_listings_restrictions_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

