from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list1 import ErrorList1

GetFeedDocumentErrorBody: TypeAlias = ErrorList1 | RawError


@dataclass(frozen=True, slots=True)
class _GetFeedDocumentError:
    def map(self, status_code: int, content: bytes) -> GetFeedDocumentErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[ErrorList1](content)
            case _:
                return RawError(status_code, content)


get_feed_document_error_mapper: Final[ErrorMapper[GetFeedDocumentErrorBody]] = _GetFeedDocumentError()
