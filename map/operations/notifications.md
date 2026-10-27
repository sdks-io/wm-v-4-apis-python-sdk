<!-- Generated file — do not edit; regenerated with the SDK. -->

# Notifications — operations

Accessor: `client.notifications` · Source: `walmart_apis/apis/notifications.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.notifications.create_destination

- **Route**: `POST /notifications/v4/destinations`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_destination(body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `Channel`
- **Returns (raw)**: `ApiResult[Channel, CreateDestinationErrorBody]`
- **Error**: `CreateDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `Channel` | `walmart_apis/models/channel.py` |
| `CreateDestinationErrorBody` | `walmart_apis/errors/create_destination_error.py` |

### client.notifications.create_subscription

- **Route**: `POST /notifications/v4/subscriptions/{notificationType}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def create_subscription(notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `notification_type`, `body`
- **Params**: `notification_type` — path `notificationType` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, CreateSubscriptionErrorBody]`
- **Error**: `CreateSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `CreateSubscriptionErrorBody` | `walmart_apis/errors/create_subscription_error.py` |

### client.notifications.delete_destination

- **Route**: `DELETE /notifications/v4/destinations/{destinationId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def delete_destination(destination_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `destination_id`
- **Params**: `destination_id` — path `destinationId`
- **Returns (parsed)**: `Channel`
- **Returns (raw)**: `ApiResult[Channel, DeleteDestinationErrorBody]`
- **Error**: `DeleteDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `Channel` | `walmart_apis/models/channel.py` |
| `DeleteDestinationErrorBody` | `walmart_apis/errors/delete_destination_error.py` |

### client.notifications.delete_subscription_by_id

- **Route**: `DELETE /notifications/v4/subscriptions/{notificationType}/{subscriptionId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def delete_subscription_by_id(subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `notification_type`
- **Params**: `subscription_id` — path `subscriptionId` · `notification_type` — path `notificationType`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, DeleteSubscriptionByIdErrorBody]`
- **Error**: `DeleteSubscriptionByIdErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `DeleteSubscriptionByIdErrorBody` | `walmart_apis/errors/delete_subscription_by_id_error.py` |

### client.notifications.get_destination

- **Route**: `GET /notifications/v4/destinations/{destinationId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_destination(destination_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `destination_id`
- **Params**: `destination_id` — path `destinationId`
- **Returns (parsed)**: `Channel`
- **Returns (raw)**: `ApiResult[Channel, GetDestinationErrorBody]`
- **Error**: `GetDestinationErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `Channel` | `walmart_apis/models/channel.py` |
| `GetDestinationErrorBody` | `walmart_apis/errors/get_destination_error.py` |

### client.notifications.get_destinations

- **Route**: `GET /notifications/v4/destinations`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_destinations(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ChannelList`
- **Returns (raw)**: `ApiResult[ChannelList, GetDestinationsErrorBody]`
- **Error**: `GetDestinationsErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `ChannelList` | `walmart_apis/models/channel_list.py` |
| `GetDestinationsErrorBody` | `walmart_apis/errors/get_destinations_error.py` |

### client.notifications.get_subscription

- **Route**: `GET /notifications/v4/subscriptions/{notificationType}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_subscription(notification_type: str, *, payload_version: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `notification_type`
- **Params**: `notification_type` — path `notificationType` · `payload_version` — query `payloadVersion`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GetSubscriptionErrorBody]`
- **Error**: `GetSubscriptionErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `GetSubscriptionErrorBody` | `walmart_apis/errors/get_subscription_error.py` |

### client.notifications.get_subscription_by_id

- **Route**: `GET /notifications/v4/subscriptions/{notificationType}/{subscriptionId}`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def get_subscription_by_id(subscription_id: str, notification_type: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `notification_type`
- **Params**: `subscription_id` — path `subscriptionId` · `notification_type` — path `notificationType`
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, GetSubscriptionByIdErrorBody]`
- **Error**: `GetSubscriptionByIdErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `GetSubscriptionByIdErrorBody` | `walmart_apis/errors/get_subscription_by_id_error.py` |

### client.notifications.send_test_notification

- **Route**: `POST /notifications/v4/subscriptions/{notificationType}/testNotification`
- **Auth**: `wallet_auth`
- **Server**: `default1`
- **Signature**: `def send_test_notification(notification_type: str, body: Any, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `notification_type`, `body`
- **Params**: `notification_type` — path `notificationType` · `body` — JSON body
- **Returns (parsed)**: `Any`
- **Returns (raw)**: `ApiResult[Any, SendTestNotificationErrorBody]`
- **Error**: `SendTestNotificationErrorBody` — **Case A (typed)**
- **Error arms**: `RawError` [400, 403, 404, 429, 500, anything unmapped]

| Type | Source |
| --- | --- |
| `SendTestNotificationErrorBody` | `walmart_apis/errors/send_test_notification_error.py` |

