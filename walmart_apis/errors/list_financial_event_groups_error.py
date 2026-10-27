from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

ListFinancialEventGroupsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _ListFinancialEventGroupsError:
    def map(self, status_code: int, content: bytes) -> ListFinancialEventGroupsErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


list_financial_event_groups_error_mapper: Final[
    ErrorMapper[ListFinancialEventGroupsErrorBody]
] = _ListFinancialEventGroupsError()
