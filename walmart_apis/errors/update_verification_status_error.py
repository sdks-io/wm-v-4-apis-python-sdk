from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

UpdateVerificationStatusErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _UpdateVerificationStatusError:
    def map(self, status_code: int, content: bytes) -> UpdateVerificationStatusErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500 | 503:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


update_verification_status_error_mapper: Final[
    ErrorMapper[UpdateVerificationStatusErrorBody]
] = _UpdateVerificationStatusError()
