<!-- Generated file — do not edit; regenerated with the SDK. -->

# FinalPayout — operations

Accessor: `client.final_payout` · Source: `walmart_apis/apis/final_payout.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.final_payout.get_final_payout_case_status

- **Route**: `GET /v4/payments/final-payout-cases/status`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def get_final_payout_case_status(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `FinalPayoutCaseStatusResponse`
- **Returns (raw)**: `ApiResult[FinalPayoutCaseStatusResponse, GetFinalPayoutCaseStatusErrorBody]`
- **Error**: `GetFinalPayoutCaseStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 404, 500, 501] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FinalPayoutCaseStatusResponse` | `walmart_apis/models/final_payout_case_status_response.py` |
| `GetFinalPayoutCaseStatusErrorBody` | `walmart_apis/errors/get_final_payout_case_status_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.final_payout.update_final_payout_case_status

- **Route**: `PUT /v4/payments/final-payout-cases/status`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def update_final_payout_case_status(body: UpdateFinalPayoutCaseStatusRequest | UpdateFinalPayoutCaseStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `FinalPayoutCaseStatusResponse`
- **Returns (raw)**: `ApiResult[FinalPayoutCaseStatusResponse, UpdateFinalPayoutCaseStatusErrorBody]`
- **Error**: `UpdateFinalPayoutCaseStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 404, 500, 501] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UpdateFinalPayoutCaseStatusRequest` | `walmart_apis/models/update_final_payout_case_status_request.py` |
| `UpdateFinalPayoutCaseStatusRequestDict` | `walmart_apis/models/update_final_payout_case_status_request.py` |
| `FinalPayoutCaseStatusResponse` | `walmart_apis/models/final_payout_case_status_response.py` |
| `UpdateFinalPayoutCaseStatusErrorBody` | `walmart_apis/errors/update_final_payout_case_status_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

