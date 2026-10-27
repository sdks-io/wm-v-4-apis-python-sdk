from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.common_error_list import CommonErrorList

ListPlacementOptionsErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListPlacementOptionsError:
    def map(self, status_code: int, content: bytes) -> ListPlacementOptionsErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](content)
            case _:
                return RawError(status_code, content)


list_placement_options_error_mapper: Final[ErrorMapper[ListPlacementOptionsErrorBody]] = _ListPlacementOptionsError()
