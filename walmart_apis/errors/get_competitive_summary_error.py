from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_catalog_items import ErrorCatalogItems

GetCompetitiveSummaryErrorBody: TypeAlias = list[ErrorCatalogItems] | RawError


@dataclass(frozen=True, slots=True)
class _GetCompetitiveSummaryError:
    def map(self, status_code: int, content: bytes) -> GetCompetitiveSummaryErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[list[ErrorCatalogItems]](content)
            case _:
                return RawError(status_code, content)


get_competitive_summary_error_mapper: Final[ErrorMapper[GetCompetitiveSummaryErrorBody]] = _GetCompetitiveSummaryError()
