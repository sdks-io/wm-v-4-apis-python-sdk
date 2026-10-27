<!-- Generated file — do not edit; regenerated with the SDK. -->

# Settlement — operations

Accessor: `client.settlement` · Source: `walmart_apis/apis/settlement.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.settlement.list_settlement_details

- **Route**: `GET /disbursements/v4/payment/settlementDetails`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_settlement_details(partner_id: str, report_date: str, *, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `partner_id`, `report_date`
- **Params**: `partner_id` — query `partnerId` · `report_date` — query `reportDate` · `page_size` — query `pageSize` · `next_token` — query `nextToken`
- **Returns (parsed)**: `SettlementDetailsResponse`
- **Returns (raw)**: `ApiResult[SettlementDetailsResponse, ListSettlementDetailsErrorBody]`
- **Error**: `ListSettlementDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SettlementDetailsResponse` | `walmart_apis/models/settlement_details_response.py` |
| `ListSettlementDetailsErrorBody` | `walmart_apis/errors/list_settlement_details_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.settlement.list_settlement_periods

- **Route**: `GET /disbursements/v4/payment/settlementPeriods`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_settlement_periods(*, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `pageSize` · `next_token` — query `nextToken`
- **Returns (parsed)**: `SettlementPeriodsResponse`
- **Returns (raw)**: `ApiResult[SettlementPeriodsResponse, ListSettlementPeriodsErrorBody]`
- **Error**: `ListSettlementPeriodsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SettlementPeriodsResponse` | `walmart_apis/models/settlement_periods_response.py` |
| `ListSettlementPeriodsErrorBody` | `walmart_apis/errors/list_settlement_periods_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.settlement.search_transactions

- **Route**: `GET /disbursements/v4/payment/search/transactions`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def search_transactions(*, page_size: int | None = 10, next_token: str | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `page_size` — query `pageSize` · `next_token` — query `nextToken` · `posted_after` — query `postedAfter` · `posted_before` — query `postedBefore`
- **Returns (parsed)**: `TransactionSearchResponse`
- **Returns (raw)**: `ApiResult[TransactionSearchResponse, SearchTransactionsErrorBody]`
- **Error**: `SearchTransactionsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `TransactionSearchResponse` | `walmart_apis/models/transaction_search_response.py` |
| `SearchTransactionsErrorBody` | `walmart_apis/errors/search_transactions_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

