from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

PurchaseShipmentErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _PurchaseShipmentError:
    def map(self, status_code: int, content: bytes) -> PurchaseShipmentErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


purchase_shipment_error_mapper: Final[ErrorMapper[PurchaseShipmentErrorBody]] = _PurchaseShipmentError()
