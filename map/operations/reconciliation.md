<!-- Generated file — do not edit; regenerated with the SDK. -->

# Reconciliation — operations

Accessor: `client.reconciliation` · Source: `walmart_apis/apis/reconciliation.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.reconciliation.check_download_report_by_period

- **Route**: `GET /disbursements/v4/payment/checkDownloadReportByPeriod`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def check_download_report_by_period(partner_id: str, date: Date, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `partner_id`, `date`
- **Params**: `partner_id` — query `partnerId` · `date` — query
- **Returns (parsed)**: `ReportAvailabilityResponse`
- **Returns (raw)**: `ApiResult[ReportAvailabilityResponse, CheckDownloadReportByPeriodErrorBody]`
- **Error**: `CheckDownloadReportByPeriodErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReportAvailabilityResponse` | `walmart_apis/models/report_availability_response.py` |
| `CheckDownloadReportByPeriodErrorBody` | `walmart_apis/errors/check_download_report_by_period_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reconciliation.download_reconciliation_report

- **Route**: `GET /disbursements/v4/payment/reconciliation/download`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def download_reconciliation_report(partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `partner_id`, `report_date`
- **Params**: `partner_id` — query `partnerId` · `report_date` — query `reportDate`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, DownloadReconciliationReportErrorBody]`
- **Error**: `DownloadReconciliationReportErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DownloadReconciliationReportErrorBody` | `walmart_apis/errors/download_reconciliation_report_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reconciliation.list_reconciliation_dates

- **Route**: `GET /disbursements/v4/payment/reconciliation/dateList`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_reconciliation_dates(partner_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `partner_id`
- **Params**: `partner_id` — query `partnerId`
- **Returns (parsed)**: `ReportAvailabilityResponse`
- **Returns (raw)**: `ApiResult[ReportAvailabilityResponse, ListReconciliationDatesErrorBody]`
- **Error**: `ListReconciliationDatesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReportAvailabilityResponse` | `walmart_apis/models/report_availability_response.py` |
| `ListReconciliationDatesErrorBody` | `walmart_apis/errors/list_reconciliation_dates_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

