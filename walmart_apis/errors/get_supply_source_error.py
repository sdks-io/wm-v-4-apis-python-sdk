from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_shipping_management import ErrorListShippingManagement

GetSupplySourceErrorBody: TypeAlias = ErrorListShippingManagement | RawError


@dataclass(frozen=True, slots=True)
class _GetSupplySourceError:
    def map(self, status_code: int, content: bytes) -> GetSupplySourceErrorBody:
        match status_code:
            case 400 | 401 | 403 | 404 | 429 | 500:
                return decode_json[ErrorListShippingManagement](content)
            case _:
                return RawError(status_code, content)


get_supply_source_error_mapper: Final[ErrorMapper[GetSupplySourceErrorBody]] = _GetSupplySourceError()
