<!-- Generated file — do not edit; regenerated with the SDK. -->

# DataKiosk — operations

Accessor: `client.data_kiosk` · Source: `walmart_apis/apis/data_kiosk.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.data_kiosk.cancel_query

- **Route**: `DELETE /data-kiosk/v4/queries/{queryId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_query(query_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query_id`
- **Params**: `query_id` — path `queryId`
- **Returns (parsed)**: `CancelQueryResponse`
- **Returns (raw)**: `ApiResult[CancelQueryResponse, CancelQueryErrorBody]`
- **Error**: `CancelQueryErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelQueryResponse` | `walmart_apis/models/cancel_query_response.py` |
| `CancelQueryErrorBody` | `walmart_apis/errors/cancel_query_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.data_kiosk.create_query

- **Route**: `POST /data-kiosk/v4/queries`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_query(body: CreateQuerySpecification | CreateQuerySpecificationDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateQueryResponse`
- **Returns (raw)**: `ApiResult[CreateQueryResponse, CreateQueryErrorBody]`
- **Error**: `CreateQueryErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateQuerySpecification` | `walmart_apis/models/create_query_specification.py` |
| `CreateQuerySpecificationDict` | `walmart_apis/models/create_query_specification.py` |
| `CreateQueryResponse` | `walmart_apis/models/create_query_response.py` |
| `CreateQueryErrorBody` | `walmart_apis/errors/create_query_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.data_kiosk.get_document

- **Route**: `GET /data-kiosk/v4/documents/{documentId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_document(document_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `document_id`
- **Params**: `document_id` — path `documentId`
- **Returns (parsed)**: `Document`
- **Returns (raw)**: `ApiResult[Document, GetDocumentErrorBody]`
- **Error**: `GetDocumentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Document` | `walmart_apis/models/document.py` |
| `GetDocumentErrorBody` | `walmart_apis/errors/get_document_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.data_kiosk.get_queries

- **Route**: `GET /data-kiosk/v4/queries`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_queries(*, processing_statuses: list[ProcessingStatusOrStr] | None = None, page_size: int | None = 10, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, pagination_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `processing_statuses` — query `processingStatuses` · `page_size` — query `pageSize` · `created_since` — query `createdSince` · `created_until` — query `createdUntil` · `pagination_token` — query `paginationToken`
- **Returns (parsed)**: `GetQueriesResponse`
- **Returns (raw)**: `ApiResult[GetQueriesResponse, GetQueriesErrorBody]`
- **Error**: `GetQueriesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProcessingStatusOrStr` | `walmart_apis/models/enums/processing_status.py` |
| `GetQueriesResponse` | `walmart_apis/models/get_queries_response.py` |
| `GetQueriesErrorBody` | `walmart_apis/errors/get_queries_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.data_kiosk.get_query

- **Route**: `GET /data-kiosk/v4/queries/{queryId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_query(query_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `query_id`
- **Params**: `query_id` — path `queryId`
- **Returns (parsed)**: `Query`
- **Returns (raw)**: `ApiResult[Query, GetQueryErrorBody]`
- **Error**: `GetQueryErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Query` | `walmart_apis/models/query.py` |
| `GetQueryErrorBody` | `walmart_apis/errors/get_query_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

