<!-- Generated file — do not edit; regenerated with the SDK. -->

# Solicitations — operations

Accessor: `client.solicitations` · Source: `walmart_apis/apis/solicitations.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.solicitations.create_product_review_and_seller_feedback_solicitation

- **Route**: `POST /solicitations/v4/orders/{sp-apiOrderId}/solicitations/productReviewAndSellerFeedback`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_product_review_and_seller_feedback_solicitation(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateProductReviewAndSellerFeedbackSolicitationErrorBody]`
- **Error**: `CreateProductReviewAndSellerFeedbackSolicitationErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateProductReviewAndSellerFeedbackSolicitationErrorBody` | `walmart_apis/errors/create_product_review_and_seller_feedback_solicitation_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.solicitations.get_solicitation_actions_for_order

- **Route**: `GET /solicitations/v4/orders/{sp-apiOrderId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_solicitation_actions_for_order(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GetSolicitationActionsForOrderErrorBody]`
- **Error**: `GetSolicitationActionsForOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetSolicitationActionsForOrderErrorBody` | `walmart_apis/errors/get_solicitation_actions_for_order_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

