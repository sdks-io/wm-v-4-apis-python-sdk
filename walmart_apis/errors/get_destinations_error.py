from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

GetDestinationsErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _GetDestinationsError:
    def map(self, status_code: int, content: bytes) -> GetDestinationsErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


get_destinations_error_mapper: Final[ErrorMapper[GetDestinationsErrorBody]] = _GetDestinationsError()
