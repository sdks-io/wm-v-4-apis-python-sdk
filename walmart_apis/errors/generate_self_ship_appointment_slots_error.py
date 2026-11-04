from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.common_error_list_fulfillment_inbound_plans import CommonErrorListFulfillmentInboundPlans

GenerateSelfShipAppointmentSlotsErrorBody: TypeAlias = CommonErrorListFulfillmentInboundPlans | RawError


@dataclass(frozen=True, slots=True)
class _GenerateSelfShipAppointmentSlotsError:
    def map(self, status_code: int, content: bytes) -> GenerateSelfShipAppointmentSlotsErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorListFulfillmentInboundPlans](content)
            case _:
                return RawError(status_code, content)


generate_self_ship_appointment_slots_error_mapper: Final[
    ErrorMapper[GenerateSelfShipAppointmentSlotsErrorBody]
] = _GenerateSelfShipAppointmentSlotsError()
