from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

ListSettlementDetailsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListSettlementDetailsError:
    def map(self, status_code: int, content: bytes) -> ListSettlementDetailsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


list_settlement_details_error_mapper: Final[ErrorMapper[ListSettlementDetailsErrorBody]] = _ListSettlementDetailsError()
