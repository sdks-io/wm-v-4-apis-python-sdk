from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.common_error_list_fulfillment_inbound_plans import CommonErrorListFulfillmentInboundPlans

GetShipmentItemsByShipmentIdErrorBody: TypeAlias = CommonErrorListFulfillmentInboundPlans | RawError


@dataclass(frozen=True, slots=True)
class _GetShipmentItemsByShipmentIdError:
    def map(self, status_code: int, content: bytes) -> GetShipmentItemsByShipmentIdErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorListFulfillmentInboundPlans](content)
            case _:
                return RawError(status_code, content)


get_shipment_items_by_shipment_id_error_mapper: Final[
    ErrorMapper[GetShipmentItemsByShipmentIdErrorBody]
] = _GetShipmentItemsByShipmentIdError()
