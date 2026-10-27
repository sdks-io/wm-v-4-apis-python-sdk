from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

GetMarketplaceParticipationsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _GetMarketplaceParticipationsError:
    def map(self, status_code: int, content: bytes) -> GetMarketplaceParticipationsErrorBody:
        match status_code:
            case 400 | 403 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


get_marketplace_participations_error_mapper: Final[
    ErrorMapper[GetMarketplaceParticipationsErrorBody]
] = _GetMarketplaceParticipationsError()
