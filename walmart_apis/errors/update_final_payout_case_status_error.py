from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

UpdateFinalPayoutCaseStatusErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _UpdateFinalPayoutCaseStatusError:
    def map(self, status_code: int, content: bytes) -> UpdateFinalPayoutCaseStatusErrorBody:
        match status_code:
            case 400 | 404 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


update_final_payout_case_status_error_mapper: Final[
    ErrorMapper[UpdateFinalPayoutCaseStatusErrorBody]
] = _UpdateFinalPayoutCaseStatusError()
