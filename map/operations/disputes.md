<!-- Generated file — do not edit; regenerated with the SDK. -->

# Disputes — operations

Accessor: `client.disputes` · Source: `walmart_apis/apis/disputes.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.disputes.check_dispute_eligibility

- **Route**: `GET /disbursements/v4/payment/disputeEligibilityCheck`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def check_dispute_eligibility(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `DisputeEligibilityResponse`
- **Returns (raw)**: `ApiResult[DisputeEligibilityResponse, CheckDisputeEligibilityErrorBody]`
- **Error**: `CheckDisputeEligibilityErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisputeEligibilityResponse` | `walmart_apis/models/dispute_eligibility_response.py` |
| `CheckDisputeEligibilityErrorBody` | `walmart_apis/errors/check_dispute_eligibility_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

