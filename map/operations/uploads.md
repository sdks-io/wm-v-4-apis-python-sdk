<!-- Generated file — do not edit; regenerated with the SDK. -->

# Uploads — operations

Accessor: `client.uploads` · Source: `walmart_apis/apis/uploads.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.uploads.create_upload_destination_for_resource

- **Route**: `POST /uploads/v4/uploadDestinations/{resource}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_upload_destination_for_resource(resource: ResourceOrStr, content_type: ContentType1OrStr, marketplace_ids: list[str], content_md5: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `resource`, `content_type`, `marketplace_ids`, `content_md5`
- **Params**: `resource` — path · `content_type` — query `contentType` · `marketplace_ids` — query `marketplaceIds` · `content_md5` — header `contentMD5`
- **Returns (parsed)**: `CreateUploadDestinationResponse`
- **Returns (raw)**: `ApiResult[CreateUploadDestinationResponse, CreateUploadDestinationForResourceErrorBody]`
- **Error**: `CreateUploadDestinationForResourceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ResourceOrStr` | `walmart_apis/models/enums/resource.py` |
| `ContentType1OrStr` | `walmart_apis/models/enums/content_type1.py` |
| `CreateUploadDestinationResponse` | `walmart_apis/models/create_upload_destination_response.py` |
| `CreateUploadDestinationForResourceErrorBody` | `walmart_apis/errors/create_upload_destination_for_resource_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

