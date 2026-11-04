<!-- Generated file — do not edit; regenerated with the SDK. -->

# Authorization — operations

Accessor: `client.authorization` · Source: `walmart_apis/apis/authorization.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.authorization.create_token

- **Route**: `POST /v4/auth/token`
- **Auth**: `basic_client_auth`
- **Server**: `default`
- **Signature**: `def create_token(grant_type: GrantTypeOrStr, *, x_o_tenant: str | None = None, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, code_verifier: str | None = None, refresh_token: str | None = None, redirect_uri: str | None = None, scope: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `grant_type`
- **Params**: `x_o_tenant` — header `x-o-tenant` · `grant_type` — form field · `client_id` — form field · `client_secret` — form field · `code` — form field · `code_verifier` — form field · `refresh_token` — form field · `redirect_uri` — form field · `scope` — form field
- **Returns (parsed)**: `TokenResponse`
- **Returns (raw)**: `ApiResult[TokenResponse, CreateTokenErrorBody]`
- **Error**: `CreateTokenErrorBody` — **Case A (typed)**
- **Error arms**: `OAuthErrorModel` [400, 401, 429, 500, 502] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantTypeOrStr` | `walmart_apis/models/enums/grant_type.py` |
| `TokenResponse` | `walmart_apis/models/token_response.py` |
| `CreateTokenErrorBody` | `walmart_apis/errors/create_token_error.py` |
| `OAuthErrorModel` | `walmart_apis/models/o_auth_error_model.py` |

