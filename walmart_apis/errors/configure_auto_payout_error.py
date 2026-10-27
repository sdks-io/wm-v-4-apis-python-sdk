from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

ConfigureAutoPayoutErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ConfigureAutoPayoutError:
    def map(self, status_code: int, content: bytes) -> ConfigureAutoPayoutErrorBody:
        match status_code:
            case 400 | 401 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


configure_auto_payout_error_mapper: Final[ErrorMapper[ConfigureAutoPayoutErrorBody]] = _ConfigureAutoPayoutError()
