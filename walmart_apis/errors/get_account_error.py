from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

GetAccountErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetAccountError:
    def map(self, status_code: int, content: bytes) -> GetAccountErrorBody:
        match status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


get_account_error_mapper: Final[ErrorMapper[GetAccountErrorBody]] = _GetAccountError()
