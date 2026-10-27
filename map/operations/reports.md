<!-- Generated file — do not edit; regenerated with the SDK. -->

# Reports — operations

Accessor: `client.reports` · Source: `walmart_apis/apis/reports.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.reports.cancel_report

- **Route**: `DELETE /reports/v4/reports/{reportId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_report(report_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_id`
- **Params**: `report_id` — path `reportId`
- **Returns (parsed)**: `CancelReportResponse`
- **Returns (raw)**: `ApiResult[CancelReportResponse, CancelReportErrorBody]`
- **Error**: `CancelReportErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelReportResponse` | `walmart_apis/models/cancel_report_response.py` |
| `CancelReportErrorBody` | `walmart_apis/errors/cancel_report_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reports.create_report

- **Route**: `POST /reports/v4/reports`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_report(body: CreateReportSpecification | CreateReportSpecificationDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateReportResponse`
- **Returns (raw)**: `ApiResult[CreateReportResponse, CreateReportErrorBody]`
- **Error**: `CreateReportErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateReportSpecification` | `walmart_apis/models/create_report_specification.py` |
| `CreateReportSpecificationDict` | `walmart_apis/models/create_report_specification.py` |
| `CreateReportResponse` | `walmart_apis/models/create_report_response.py` |
| `CreateReportErrorBody` | `walmart_apis/errors/create_report_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reports.download_new_report

- **Route**: `GET /disbursements/v4/payment/summary/newReportDownload`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def download_new_report(partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `partner_id`, `report_date`
- **Params**: `partner_id` — query `partnerId` · `report_date` — query `reportDate`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, DownloadNewReportErrorBody]`
- **Error**: `DownloadNewReportErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DownloadNewReportErrorBody` | `walmart_apis/errors/download_new_report_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reports.download_old_report

- **Route**: `GET /disbursements/v4/payment/summary/oldReportDownload`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def download_old_report(partner_id: str, report_date: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `partner_id`, `report_date`
- **Params**: `partner_id` — query `partnerId` · `report_date` — query `reportDate`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, DownloadOldReportErrorBody]`
- **Error**: `DownloadOldReportErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 404, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DownloadOldReportErrorBody` | `walmart_apis/errors/download_old_report_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reports.get_report

- **Route**: `GET /reports/v4/reports/{reportId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_report(report_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_id`
- **Params**: `report_id` — path `reportId`
- **Returns (parsed)**: `Report`
- **Returns (raw)**: `ApiResult[Report, GetReportErrorBody]`
- **Error**: `GetReportErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Report` | `walmart_apis/models/report.py` |
| `GetReportErrorBody` | `walmart_apis/errors/get_report_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reports.get_report_document

- **Route**: `GET /reports/v4/documents/{reportDocumentId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_report_document(report_document_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_document_id`
- **Params**: `report_document_id` — path `reportDocumentId`
- **Returns (parsed)**: `ReportDocument`
- **Returns (raw)**: `ApiResult[ReportDocument, GetReportDocumentErrorBody]`
- **Error**: `GetReportDocumentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReportDocument` | `walmart_apis/models/report_document.py` |
| `GetReportDocumentErrorBody` | `walmart_apis/errors/get_report_document_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.reports.get_reports

- **Route**: `GET /reports/v4/reports`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_reports(*, report_types: list[ReportType1OrStr] | None = None, processing_statuses: list[ProcessingStatusOrStr] | None = None, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `report_types` — query `reportTypes` · `processing_statuses` — query `processingStatuses` · `created_since` — query `createdSince` · `created_until` — query `createdUntil` · `page_size` — query `pageSize` · `next_token` — query `nextToken`
- **Returns (parsed)**: `GetReportsResponse`
- **Returns (raw)**: `ApiResult[GetReportsResponse, GetReportsErrorBody]`
- **Error**: `GetReportsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReportType1OrStr` | `walmart_apis/models/enums/report_type1.py` |
| `ProcessingStatusOrStr` | `walmart_apis/models/enums/processing_status.py` |
| `GetReportsResponse` | `walmart_apis/models/get_reports_response.py` |
| `GetReportsErrorBody` | `walmart_apis/errors/get_reports_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

