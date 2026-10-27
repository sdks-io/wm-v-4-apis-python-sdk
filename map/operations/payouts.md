<!-- Generated file — do not edit; regenerated with the SDK. -->

# Payouts — operations

Accessor: `client.payouts` · Source: `walmart_apis/apis/payouts.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payouts.configure_auto_payout

- **Route**: `PUT /disbursements/v4/payment/autoPayout`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def configure_auto_payout(body: DisbursementsV4PaymentAutoPayoutRequest | DisbursementsV4PaymentAutoPayoutRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `PayoutStatusResponse`
- **Returns (raw)**: `ApiResult[PayoutStatusResponse, ConfigureAutoPayoutErrorBody]`
- **Error**: `ConfigureAutoPayoutErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DisbursementsV4PaymentAutoPayoutRequest` | `walmart_apis/models/disbursements_v4_payment_auto_payout_request.py` |
| `DisbursementsV4PaymentAutoPayoutRequestDict` | `walmart_apis/models/disbursements_v4_payment_auto_payout_request.py` |
| `PayoutStatusResponse` | `walmart_apis/models/payout_status_response.py` |
| `ConfigureAutoPayoutErrorBody` | `walmart_apis/errors/configure_auto_payout_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.payouts.get_annual_statement_opts

- **Route**: `GET /disbursements/v4/payment/annualStatementOpts`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_annual_statement_opts(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `AnnualStatementOptsResponse`
- **Returns (raw)**: `ApiResult[AnnualStatementOptsResponse, GetAnnualStatementOptsErrorBody]`
- **Error**: `GetAnnualStatementOptsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `AnnualStatementOptsResponse` | `walmart_apis/models/annual_statement_opts_response.py` |
| `GetAnnualStatementOptsErrorBody` | `walmart_apis/errors/get_annual_statement_opts_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.payouts.get_faster_payout_eligibility

- **Route**: `GET /disbursements/v4/payment/fasterPayoutEligibility`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_faster_payout_eligibility(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `FasterPayoutEligibilityResponse`
- **Returns (raw)**: `ApiResult[FasterPayoutEligibilityResponse, GetFasterPayoutEligibilityErrorBody]`
- **Error**: `GetFasterPayoutEligibilityErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FasterPayoutEligibilityResponse` | `walmart_apis/models/faster_payout_eligibility_response.py` |
| `GetFasterPayoutEligibilityErrorBody` | `walmart_apis/errors/get_faster_payout_eligibility_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.payouts.get_payment_status

- **Route**: `GET /disbursements/v4/payment/paymentstatus`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_payment_status(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `PayoutStatusResponse`
- **Returns (raw)**: `ApiResult[PayoutStatusResponse, GetPaymentStatusErrorBody]`
- **Error**: `GetPaymentStatusErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `PayoutStatusResponse` | `walmart_apis/models/payout_status_response.py` |
| `GetPaymentStatusErrorBody` | `walmart_apis/errors/get_payment_status_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.payouts.initiate_faster_payout

- **Route**: `POST /disbursements/v4/payment/fasterPayout`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def initiate_faster_payout(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `InitiatePayoutResponse`
- **Returns (raw)**: `ApiResult[InitiatePayoutResponse, InitiateFasterPayoutErrorBody]`
- **Error**: `InitiateFasterPayoutErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 409, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `InitiatePayoutResponse` | `walmart_apis/models/initiate_payout_response.py` |
| `InitiateFasterPayoutErrorBody` | `walmart_apis/errors/initiate_faster_payout_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

