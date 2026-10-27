<!-- Generated file — do not edit; regenerated with the SDK. -->

# Feeds — operations

Accessor: `client.feeds` · Source: `walmart_apis/apis/feeds.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.feeds.cancel_feed

- **Route**: `DELETE /feeds/v4/feeds/{feedId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def cancel_feed(feed_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_id`
- **Params**: `feed_id` — path `feedId`
- **Returns (parsed)**: `CancelFeedResponse`
- **Returns (raw)**: `ApiResult[CancelFeedResponse, CancelFeedErrorBody]`
- **Error**: `CancelFeedErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList1` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CancelFeedResponse` | `walmart_apis/models/cancel_feed_response.py` |
| `CancelFeedErrorBody` | `walmart_apis/errors/cancel_feed_error.py` |
| `ErrorList1` | `walmart_apis/models/error_list1.py` |

### client.feeds.create_feed

- **Route**: `POST /feeds/v4/feeds`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_feed(feed_type: FeedTypeOrStr, file: FileInput, *, marketplace_id: str | None = None, content_type: ContentTypeOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_type`, `file`
- **Params**: `feed_type` — query `feedType` · `marketplace_id` — query `marketplaceId` · `file` — multipart file · `content_type` — multipart field `contentType`
- **Returns (parsed)**: `CreateFeedResponse`
- **Returns (raw)**: `ApiResult[CreateFeedResponse, CreateFeedErrorBody]`
- **Error**: `CreateFeedErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList1` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FeedTypeOrStr` | `walmart_apis/models/enums/feed_type.py` |
| `ContentTypeOrStr` | `walmart_apis/models/enums/content_type.py` |
| `CreateFeedResponse` | `walmart_apis/models/create_feed_response.py` |
| `CreateFeedErrorBody` | `walmart_apis/errors/create_feed_error.py` |
| `ErrorList1` | `walmart_apis/models/error_list1.py` |

### client.feeds.get_feed

- **Route**: `GET /feeds/v4/feeds/{feedId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_feed(feed_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_id`
- **Params**: `feed_id` — path `feedId`
- **Returns (parsed)**: `Feed`
- **Returns (raw)**: `ApiResult[Feed, GetFeedErrorBody]`
- **Error**: `GetFeedErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList1` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `Feed` | `walmart_apis/models/feed.py` |
| `GetFeedErrorBody` | `walmart_apis/errors/get_feed_error.py` |
| `ErrorList1` | `walmart_apis/models/error_list1.py` |

### client.feeds.get_feed_document

- **Route**: `GET /feeds/v4/feeds/{feedId}/document`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_feed_document(feed_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `feed_id`
- **Params**: `feed_id` — path `feedId`
- **Returns (parsed)**: `FileResponse`
- **Returns (raw)**: `ApiResult[FileResponse, GetFeedDocumentErrorBody]`
- **Error**: `GetFeedDocumentErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList1` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetFeedDocumentErrorBody` | `walmart_apis/errors/get_feed_document_error.py` |
| `ErrorList1` | `walmart_apis/models/error_list1.py` |

### client.feeds.get_feeds

- **Route**: `GET /feeds/v4/feeds`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_feeds(*, feed_types: list[FeedTypeOrStr] | None = None, feed_statuses: list[FeedStatusOrStr] | None = None, created_since: RFC3339DateTime | None = None, created_until: RFC3339DateTime | None = None, page_size: int | None = 10, next_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `feed_types` — query `feedTypes` · `feed_statuses` — query `feedStatuses` · `created_since` — query `createdSince` · `created_until` — query `createdUntil` · `page_size` — query `pageSize` · `next_token` — query `nextToken`
- **Returns (parsed)**: `GetFeedsResponse`
- **Returns (raw)**: `ApiResult[GetFeedsResponse, GetFeedsErrorBody]`
- **Error**: `GetFeedsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList1` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `FeedTypeOrStr` | `walmart_apis/models/enums/feed_type.py` |
| `FeedStatusOrStr` | `walmart_apis/models/enums/feed_status.py` |
| `GetFeedsResponse` | `walmart_apis/models/get_feeds_response.py` |
| `GetFeedsErrorBody` | `walmart_apis/errors/get_feeds_error.py` |
| `ErrorList1` | `walmart_apis/models/error_list1.py` |

