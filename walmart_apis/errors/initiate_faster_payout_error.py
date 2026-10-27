from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

InitiateFasterPayoutErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _InitiateFasterPayoutError:
    def map(self, status_code: int, content: bytes) -> InitiateFasterPayoutErrorBody:
        match status_code:
            case 400 | 401 | 409 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


initiate_faster_payout_error_mapper: Final[ErrorMapper[InitiateFasterPayoutErrorBody]] = _InitiateFasterPayoutError()
