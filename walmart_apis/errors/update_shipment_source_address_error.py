from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.common_error_list import CommonErrorList

UpdateShipmentSourceAddressErrorBody: TypeAlias = CommonErrorList | RawError


@dataclass(frozen=True, slots=True)
class _UpdateShipmentSourceAddressError:
    def map(self, status_code: int, content: bytes) -> UpdateShipmentSourceAddressErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[CommonErrorList](content)
            case _:
                return RawError(status_code, content)


update_shipment_source_address_error_mapper: Final[
    ErrorMapper[UpdateShipmentSourceAddressErrorBody]
] = _UpdateShipmentSourceAddressError()
