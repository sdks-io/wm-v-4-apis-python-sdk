from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteDestinationErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteDestinationError:
    def map(self, status_code: int, content: bytes) -> DeleteDestinationErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_destination_error_mapper: Final[ErrorMapper[DeleteDestinationErrorBody]] = _DeleteDestinationError()
