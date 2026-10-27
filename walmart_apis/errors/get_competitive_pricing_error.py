from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error3 import Error3

GetCompetitivePricingErrorBody: TypeAlias = list[Error3] | RawError


@dataclass(frozen=True, slots=True)
class _GetCompetitivePricingError:
    def map(self, status_code: int, content: bytes) -> GetCompetitivePricingErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[list[Error3]](content)
            case _:
                return RawError(status_code, content)


get_competitive_pricing_error_mapper: Final[ErrorMapper[GetCompetitivePricingErrorBody]] = _GetCompetitivePricingError()
