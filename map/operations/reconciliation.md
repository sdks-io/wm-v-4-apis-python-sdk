<!-- Generated file — do not edit; regenerated with the SDK. -->

# Reconciliation — operations

Accessor: `client.reconciliation` · Source: `walmart_apis/apis/reconciliation.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.reconciliation.check_download_report_by_period

- **Route**: `GET /v4/payments/reports`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
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

- **Route**: `GET /v4/payments/reports/reconciliation-reports/{reconciliation-report-id}`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
- **Signature**: `def download_reconciliation_report(reconciliation_report_id: str, partner_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `reconciliation_report_id`, `partner_id`
- **Params**: `reconciliation_report_id` — path `reconciliation-report-id` · `partner_id` — query `partnerId`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, DownloadReconciliationReportErrorBody]`
- **Error**: `DownloadReconciliationReportErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 401, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DownloadReconciliationReportErrorBody` | `walmart_apis/errors/download_reconciliation_report_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reconciliation.list_reconciliation_dates

- **Route**: `GET /v4/payments/reports/reconciliation/date-list`
- **Auth**: `wallet_auth`
- **Server**: `default_catalog_items`
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

