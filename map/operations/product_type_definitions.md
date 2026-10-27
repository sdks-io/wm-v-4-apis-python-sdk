<!-- Generated file — do not edit; regenerated with the SDK. -->

# ProductTypeDefinitions — operations

Accessor: `client.product_type_definitions` · Source: `walmart_apis/apis/product_type_definitions.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.product_type_definitions.get_definitions_product_type

- **Route**: `GET /definitions/v4/productTypes/{productType}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_definitions_product_type(product_type: str, *, seller_id: str | None = None, locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `product_type`
- **Params**: `product_type` — path `productType` · `seller_id` — query `sellerId` · `locale` — query
- **Returns (parsed)**: `ProductTypeDefinition`
- **Returns (raw)**: `ApiResult[ProductTypeDefinition, GetDefinitionsProductTypeErrorBody]`
- **Error**: `GetDefinitionsProductTypeErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProductTypeDefinition` | `walmart_apis/models/product_type_definition.py` |
| `GetDefinitionsProductTypeErrorBody` | `walmart_apis/errors/get_definitions_product_type_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

### client.product_type_definitions.search_definitions_product_types

- **Route**: `GET /definitions/v4/productTypes`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def search_definitions_product_types(*, keywords: str | None = None, item_name: str | None = None, locale: str | None = "en_US", request_options: RequestOptionsOrDict | None = None)`
- **Params**: `keywords` — query · `item_name` — query `itemName` · `locale` — query
- **Returns (parsed)**: `ProductTypeList`
- **Returns (raw)**: `ApiResult[ProductTypeList, SearchDefinitionsProductTypesErrorBody]`
- **Error**: `SearchDefinitionsProductTypesErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorList` [400, 403, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ProductTypeList` | `walmart_apis/models/product_type_list.py` |
| `SearchDefinitionsProductTypesErrorBody` | `walmart_apis/errors/search_definitions_product_types_error.py` |
| `ErrorList` | `walmart_apis/models/error_list.py` |

