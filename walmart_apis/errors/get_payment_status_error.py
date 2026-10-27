from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

GetPaymentStatusErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetPaymentStatusError:
    def map(self, status_code: int, content: bytes) -> GetPaymentStatusErrorBody:
        match status_code:
            case 400 | 401 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


get_payment_status_error_mapper: Final[ErrorMapper[GetPaymentStatusErrorBody]] = _GetPaymentStatusError()
