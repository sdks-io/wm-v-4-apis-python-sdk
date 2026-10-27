from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.common_error_list import CommonErrorList

CancelSelfShipAppointmentErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _CancelSelfShipAppointmentError:
    def map(self, status_code: int, content: bytes) -> CancelSelfShipAppointmentErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](content)
            case _:
                return RawError(status_code, content)


cancel_self_ship_appointment_error_mapper: Final[
    ErrorMapper[CancelSelfShipAppointmentErrorBody]
] = _CancelSelfShipAppointmentError()
