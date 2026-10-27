from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

SearchTransactionsErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _SearchTransactionsError:
    def map(self, status_code: int, content: bytes) -> SearchTransactionsErrorBody:
        match status_code:
            case 400 | 401 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


search_transactions_error_mapper: Final[ErrorMapper[SearchTransactionsErrorBody]] = _SearchTransactionsError()
