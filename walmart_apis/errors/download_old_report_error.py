from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

DownloadOldReportErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _DownloadOldReportError:
    def map(self, status_code: int, content: bytes) -> DownloadOldReportErrorBody:
        match status_code:
            case 400 | 404 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


download_old_report_error_mapper: Final[ErrorMapper[DownloadOldReportErrorBody]] = _DownloadOldReportError()
