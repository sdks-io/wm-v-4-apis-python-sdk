<!-- Generated file — do not edit; regenerated with the SDK. -->

# ReportSchedules — operations

Accessor: `client.report_schedules` · Source: `walmart_apis/apis/report_schedules.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.report_schedules.cancel_report_schedule

- **Route**: `DELETE /reports/v4/schedules/{reportScheduleId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_report_schedule(report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_schedule_id`
- **Params**: `report_schedule_id` — path `reportScheduleId`
- **Returns (parsed)**: `CancelReportScheduleResponse`
- **Returns (raw)**: `ApiResult[CancelReportScheduleResponse, CancelReportScheduleErrorBody]`
- **Error**: `CancelReportScheduleErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelReportScheduleResponse` | `walmart_apis/models/cancel_report_schedule_response.py` |
| `CancelReportScheduleErrorBody` | `walmart_apis/errors/cancel_report_schedule_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.report_schedules.create_report_schedule

- **Route**: `POST /reports/v4/schedules`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_report_schedule(body: CreateReportScheduleSpecification | CreateReportScheduleSpecificationDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateReportScheduleResponse`
- **Returns (raw)**: `ApiResult[CreateReportScheduleResponse, CreateReportScheduleErrorBody]`
- **Error**: `CreateReportScheduleErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateReportScheduleSpecification` | `walmart_apis/models/create_report_schedule_specification.py` |
| `CreateReportScheduleSpecificationDict` | `walmart_apis/models/create_report_schedule_specification.py` |
| `CreateReportScheduleResponse` | `walmart_apis/models/create_report_schedule_response.py` |
| `CreateReportScheduleErrorBody` | `walmart_apis/errors/create_report_schedule_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.report_schedules.get_report_schedule

- **Route**: `GET /reports/v4/schedules/{reportScheduleId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_report_schedule(report_schedule_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `report_schedule_id`
- **Params**: `report_schedule_id` — path `reportScheduleId`
- **Returns (parsed)**: `ReportSchedule`
- **Returns (raw)**: `ApiResult[ReportSchedule, GetReportScheduleErrorBody]`
- **Error**: `GetReportScheduleErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReportSchedule` | `walmart_apis/models/report_schedule.py` |
| `GetReportScheduleErrorBody` | `walmart_apis/errors/get_report_schedule_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.report_schedules.get_report_schedules

- **Route**: `GET /reports/v4/schedules`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_report_schedules(*, report_types: list[ReportType1OrStr] | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `report_types` — query `reportTypes`
- **Returns (parsed)**: `GetReportSchedulesResponse`
- **Returns (raw)**: `ApiResult[GetReportSchedulesResponse, GetReportSchedulesErrorBody]`
- **Error**: `GetReportSchedulesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ReportType1OrStr` | `walmart_apis/models/enums/report_type1.py` |
| `GetReportSchedulesResponse` | `walmart_apis/models/get_report_schedules_response.py` |
| `GetReportSchedulesErrorBody` | `walmart_apis/errors/get_report_schedules_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

