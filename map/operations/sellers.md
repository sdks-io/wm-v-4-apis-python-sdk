<!-- Generated file — do not edit; regenerated with the SDK. -->

# Sellers — operations

Accessor: `client.sellers` · Source: `walmart_apis/apis/sellers.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sellers.get_account

- **Route**: `GET /sellers/v4/account`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_account(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SellerAccount`
- **Returns (raw)**: `ApiResult[SellerAccount, GetAccountErrorBody]`
- **Error**: `GetAccountErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SellerAccount` | `walmart_apis/models/seller_account.py` |
| `GetAccountErrorBody` | `walmart_apis/errors/get_account_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.sellers.get_marketplace_participations

- **Route**: `GET /sellers/v4/marketplaceParticipations`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_marketplace_participations(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `GetMarketplaceParticipationsResponse`
- **Returns (raw)**: `ApiResult[GetMarketplaceParticipationsResponse, GetMarketplaceParticipationsErrorBody]`
- **Error**: `GetMarketplaceParticipationsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetMarketplaceParticipationsResponse` | `walmart_apis/models/get_marketplace_participations_response.py` |
| `GetMarketplaceParticipationsErrorBody` | `walmart_apis/errors/get_marketplace_participations_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

