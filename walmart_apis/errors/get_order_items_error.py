from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

GetOrderItemsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetOrderItemsError:
    def map(self, status_code: int, content: bytes) -> GetOrderItemsErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500 | 503:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


get_order_items_error_mapper: Final[ErrorMapper[GetOrderItemsErrorBody]] = _GetOrderItemsError()
