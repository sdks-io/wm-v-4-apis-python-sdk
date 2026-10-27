<!-- Generated file — do not edit; regenerated with the SDK. -->

# Finances — operations

Accessor: `client.finances` · Source: `walmart_apis/apis/finances.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.finances.list_financial_event_groups

- **Route**: `GET /finances/v4/financialEventGroups`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_financial_event_groups(*, max_results_per_page: int | None = None, financial_event_group_started_before: RFC3339DateTime | None = None, financial_event_group_started_after: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `max_results_per_page` — query `MaxResultsPerPage` · `financial_event_group_started_before` — query `FinancialEventGroupStartedBefore` · `financial_event_group_started_after` — query `FinancialEventGroupStartedAfter` · `next_token` — query `NextToken`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, ListFinancialEventGroupsErrorBody]`
- **Error**: `ListFinancialEventGroupsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListFinancialEventGroupsErrorBody` | `walmart_apis/errors/list_financial_event_groups_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.finances.list_financial_events

- **Route**: `GET /finances/v4/financialEvents`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_financial_events(*, max_results_per_page: int | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `max_results_per_page` — query `MaxResultsPerPage` · `posted_after` — query `PostedAfter` · `posted_before` — query `PostedBefore` · `next_token` — query `NextToken`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, ListFinancialEventsErrorBody]`
- **Error**: `ListFinancialEventsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListFinancialEventsErrorBody` | `walmart_apis/errors/list_financial_events_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.finances.list_financial_events_by_group_id

- **Route**: `GET /finances/v4/financialEventGroups/{eventGroupId}/financialEvents`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_financial_events_by_group_id(event_group_id: str, *, max_results_per_page: int | None = None, posted_after: RFC3339DateTime | None = None, posted_before: RFC3339DateTime | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `event_group_id`
- **Params**: `event_group_id` — path `eventGroupId` · `max_results_per_page` — query `MaxResultsPerPage` · `posted_after` — query `PostedAfter` · `posted_before` — query `PostedBefore` · `next_token` — query `NextToken`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, ListFinancialEventsByGroupIdErrorBody]`
- **Error**: `ListFinancialEventsByGroupIdErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListFinancialEventsByGroupIdErrorBody` | `walmart_apis/errors/list_financial_events_by_group_id_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.finances.list_financial_events_by_order_id

- **Route**: `GET /finances/v4/orders/{orderId}/financialEvents`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def list_financial_events_by_order_id(order_id: str, *, max_results_per_page: int | None = None, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`
- **Params**: `order_id` — path `orderId` · `max_results_per_page` — query `MaxResultsPerPage` · `next_token` — query `NextToken`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, ListFinancialEventsByOrderIdErrorBody]`
- **Error**: `ListFinancialEventsByOrderIdErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ListFinancialEventsByOrderIdErrorBody` | `walmart_apis/errors/list_financial_events_by_order_id_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

