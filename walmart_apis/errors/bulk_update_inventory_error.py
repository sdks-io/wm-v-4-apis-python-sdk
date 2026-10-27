from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

BulkUpdateInventoryErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _BulkUpdateInventoryError:
    def map(self, status_code: int, content: bytes) -> BulkUpdateInventoryErrorBody:
        match status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


bulk_update_inventory_error_mapper: Final[ErrorMapper[BulkUpdateInventoryErrorBody]] = _BulkUpdateInventoryError()
