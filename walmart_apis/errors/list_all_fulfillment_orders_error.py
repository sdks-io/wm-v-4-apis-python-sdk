from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

ListAllFulfillmentOrdersErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListAllFulfillmentOrdersError:
    def map(self, status_code: int, content: bytes) -> ListAllFulfillmentOrdersErrorBody:
        match status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


list_all_fulfillment_orders_error_mapper: Final[
    ErrorMapper[ListAllFulfillmentOrdersErrorBody]
] = _ListAllFulfillmentOrdersError()
