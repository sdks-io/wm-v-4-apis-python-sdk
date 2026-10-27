from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list1 import ErrorList1

GetFeedsErrorBody: TypeAlias = ErrorList1 | RawError


@dataclass(frozen=True, slots=True)
class _GetFeedsError:
    def map(self, status_code: int, content: bytes) -> GetFeedsErrorBody:
        match status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList1](content)
            case _:
                return RawError(status_code, content)


get_feeds_error_mapper: Final[ErrorMapper[GetFeedsErrorBody]] = _GetFeedsError()
