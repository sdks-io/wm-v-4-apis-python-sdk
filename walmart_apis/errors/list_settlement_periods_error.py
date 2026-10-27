from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

ListSettlementPeriodsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListSettlementPeriodsError:
    def map(self, status_code: int, content: bytes) -> ListSettlementPeriodsErrorBody:
        match status_code:
            case 400 | 401 | 403 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


list_settlement_periods_error_mapper: Final[ErrorMapper[ListSettlementPeriodsErrorBody]] = _ListSettlementPeriodsError()
