<!-- Generated file — do not edit; regenerated with the SDK. -->

# Authorization — operations

Accessor: `client.authorization` · Source: `walmart_apis/apis/authorization.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.authorization.authorize

- **Route**: `GET /auth/v4/authorize`
- **Server**: `default`
- **Signature**: `def authorize(response_type: ResponseType1OrStr, client_id: str, redirect_uri: str, scope: str, state: str, code_challenge: str, code_challenge_method: CodeChallengeMethodOrStr, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `response_type`, `client_id`, `redirect_uri`, `scope`, `state`, `code_challenge`, `code_challenge_method`
- **Params**: `response_type` — query · `client_id` — query · `redirect_uri` — query · `scope` — query · `state` — query · `code_challenge` — query · `code_challenge_method` — query
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, AuthorizeErrorBody]`
- **Error**: `AuthorizeErrorBody` — **Case A (typed)**
- **Error arms**: `AuthorizeError` [400] · `OauthErrorModel` [429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ResponseType1OrStr` | `walmart_apis/models/enums/response_type1.py` |
| `CodeChallengeMethodOrStr` | `walmart_apis/models/enums/code_challenge_method.py` |
| `AuthorizeErrorBody` | `walmart_apis/errors/authorize_error.py` |
| `AuthorizeError` | `walmart_apis/models/authorize_error.py` |
| `OauthErrorModel` | `walmart_apis/models/oauth_error_model.py` |

### client.authorization.create_token

- **Route**: `POST /auth/v4/token`
- **Auth**: `basic_client_auth`
- **Server**: `default`
- **Signature**: `def create_token(grant_type: GrantTypeOrStr, *, client_id: str | None = None, client_secret: str | None = None, code: str | None = None, code_verifier: str | None = None, refresh_token: str | None = None, redirect_uri: str | None = None, scope: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `grant_type`
- **Params**: `grant_type` — form field · `client_id` — form field · `client_secret` — form field · `code` — form field · `code_verifier` — form field · `refresh_token` — form field · `redirect_uri` — form field · `scope` — form field
- **Returns (parsed)**: `TokenResponse`
- **Returns (raw)**: `ApiResult[TokenResponse, CreateTokenErrorBody]`
- **Error**: `CreateTokenErrorBody` — **Case A (typed)**
- **Error arms**: `OauthErrorModel` [400, 401, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GrantTypeOrStr` | `walmart_apis/models/enums/grant_type.py` |
| `TokenResponse` | `walmart_apis/models/token_response.py` |
| `CreateTokenErrorBody` | `walmart_apis/errors/create_token_error.py` |
| `OauthErrorModel` | `walmart_apis/models/oauth_error_model.py` |

### client.authorization.register_client

- **Route**: `POST /auth/v4/register`
- **Server**: `default`
- **Signature**: `def register_client(body: ClientRegistrationRequest | ClientRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ClientRegistrationResponse`
- **Returns (raw)**: `ApiResult[ClientRegistrationResponse, RegisterClientErrorBody]`
- **Error**: `RegisterClientErrorBody` — **Case A (typed)**
- **Error arms**: `RegistrationError` [400, 401] · `OauthErrorModel` [429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClientRegistrationRequest` | `walmart_apis/models/client_registration_request.py` |
| `ClientRegistrationRequestDict` | `walmart_apis/models/client_registration_request.py` |
| `ClientRegistrationResponse` | `walmart_apis/models/client_registration_response.py` |
| `RegisterClientErrorBody` | `walmart_apis/errors/register_client_error.py` |
| `RegistrationError` | `walmart_apis/models/registration_error.py` |
| `OauthErrorModel` | `walmart_apis/models/oauth_error_model.py` |

