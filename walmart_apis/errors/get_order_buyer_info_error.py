from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

GetOrderBuyerInfoErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetOrderBuyerInfoError:
    def map(self, status_code: int, content: bytes) -> GetOrderBuyerInfoErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500 | 503:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


get_order_buyer_info_error_mapper: Final[ErrorMapper[GetOrderBuyerInfoErrorBody]] = _GetOrderBuyerInfoError()
