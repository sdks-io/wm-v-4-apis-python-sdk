from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

CreateDigitalAccessKeyErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CreateDigitalAccessKeyError:
    def map(self, status_code: int, content: bytes) -> CreateDigitalAccessKeyErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


create_digital_access_key_error_mapper: Final[
    ErrorMapper[CreateDigitalAccessKeyErrorBody]
] = _CreateDigitalAccessKeyError()
