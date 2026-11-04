from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list_shipping_management import ErrorListShippingManagement

CreateSupplySourceErrorBody: TypeAlias = ErrorListShippingManagement | RawError


@dataclass(frozen=True, slots=True)
class _CreateSupplySourceError:
    def map(self, status_code: int, content: bytes) -> CreateSupplySourceErrorBody:
        match status_code:
            case 400 | 401 | 403 | 429 | 500:
                return decode_json[ErrorListShippingManagement](content)
            case _:
                return RawError(status_code, content)


create_supply_source_error_mapper: Final[ErrorMapper[CreateSupplySourceErrorBody]] = _CreateSupplySourceError()
