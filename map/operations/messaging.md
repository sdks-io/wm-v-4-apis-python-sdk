<!-- Generated file — do not edit; regenerated with the SDK. -->

# Messaging — operations

Accessor: `client.messaging` · Source: `walmart_apis/apis/messaging.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.messaging.create_warranty

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/warranty`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_warranty(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateWarrantyErrorBody]`
- **Error**: `CreateWarrantyErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateWarrantyErrorBody` | `walmart_apis/errors/create_warranty_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.get_attributes

- **Route**: `GET /messaging/v4/orders/{sp-apiOrderId}/attributes`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_attributes(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GetAttributesErrorBody]`
- **Error**: `GetAttributesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAttributesErrorBody` | `walmart_apis/errors/get_attributes_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.confirm_customization_details

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/confirmCustomizationDetails`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def confirm_customization_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, ConfirmCustomizationDetailsErrorBody]`
- **Error**: `ConfirmCustomizationDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConfirmCustomizationDetailsErrorBody` | `walmart_apis/errors/confirm_customization_details_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.create_confirm_delivery_details

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/confirmDeliveryDetails`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_confirm_delivery_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateConfirmDeliveryDetailsErrorBody]`
- **Error**: `CreateConfirmDeliveryDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateConfirmDeliveryDetailsErrorBody` | `walmart_apis/errors/create_confirm_delivery_details_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.create_confirm_order_details

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/confirmOrderDetails`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_confirm_order_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateConfirmOrderDetailsErrorBody]`
- **Error**: `CreateConfirmOrderDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateConfirmOrderDetailsErrorBody` | `walmart_apis/errors/create_confirm_order_details_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.create_confirm_service_details

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/confirmServiceDetails`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_confirm_service_details(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateConfirmServiceDetailsErrorBody]`
- **Error**: `CreateConfirmServiceDetailsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateConfirmServiceDetailsErrorBody` | `walmart_apis/errors/create_confirm_service_details_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.create_digital_access_key

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/digitalAccessKey`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_digital_access_key(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateDigitalAccessKeyErrorBody]`
- **Error**: `CreateDigitalAccessKeyErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateDigitalAccessKeyErrorBody` | `walmart_apis/errors/create_digital_access_key_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.create_legal_disclosure

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/legalDisclosure`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_legal_disclosure(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateLegalDisclosureErrorBody]`
- **Error**: `CreateLegalDisclosureErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateLegalDisclosureErrorBody` | `walmart_apis/errors/create_legal_disclosure_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.create_unexpected_problem

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/unexpectedProblem`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_unexpected_problem(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateUnexpectedProblemErrorBody]`
- **Error**: `CreateUnexpectedProblemErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CreateUnexpectedProblemErrorBody` | `walmart_apis/errors/create_unexpected_problem_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.get_messaging_actions_for_order

- **Route**: `GET /messaging/v4/orders/{sp-apiOrderId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_messaging_actions_for_order(sp_api_order_id: str, marketplace_ids: list[str], *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GetMessagingActionsForOrderErrorBody]`
- **Error**: `GetMessagingActionsForOrderErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetMessagingActionsForOrderErrorBody` | `walmart_apis/errors/get_messaging_actions_for_order_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.messaging.send_invoice

- **Route**: `POST /messaging/v4/orders/{sp-apiOrderId}/messages/invoice`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def send_invoice(sp_api_order_id: str, marketplace_ids: list[str], body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `sp_api_order_id`, `marketplace_ids`, `body`
- **Params**: `sp_api_order_id` — path `sp-apiOrderId` · `marketplace_ids` — query `marketplaceIds` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, SendInvoiceErrorBody]`
- **Error**: `SendInvoiceErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `SendInvoiceErrorBody` | `walmart_apis/errors/send_invoice_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

