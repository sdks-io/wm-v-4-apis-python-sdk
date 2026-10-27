from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

DeliverOrderLinesErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _DeliverOrderLinesError:
    def map(self, status_code: int, content: bytes) -> DeliverOrderLinesErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500 | 503:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


deliver_order_lines_error_mapper: Final[ErrorMapper[DeliverOrderLinesErrorBody]] = _DeliverOrderLinesError()
