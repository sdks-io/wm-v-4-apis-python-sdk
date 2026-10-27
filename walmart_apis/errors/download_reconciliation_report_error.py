from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_list import ErrorList

DownloadReconciliationReportErrorBody: TypeAlias = ErrorList | RawError


@dataclass(frozen=True, slots=True)
class _DownloadReconciliationReportError:
    def map(self, status_code: int, content: bytes) -> DownloadReconciliationReportErrorBody:
        match status_code:
            case 400 | 401 | 404 | 500:
                return decode_json[ErrorList](content)
            case _:
                return RawError(status_code, content)


download_reconciliation_report_error_mapper: Final[
    ErrorMapper[DownloadReconciliationReportErrorBody]
] = _DownloadReconciliationReportError()
