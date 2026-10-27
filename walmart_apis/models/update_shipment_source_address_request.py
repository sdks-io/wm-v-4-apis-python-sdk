from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_address_input import CommonAddressInput, CommonAddressInputDict


class UpdateShipmentSourceAddressRequest(SdkBaseModel):
    """The ``updateShipmentSourceAddress`` request."""

    address: CommonAddressInput
    """Specific details to identify a place (input variant — phone required)."""


class UpdateShipmentSourceAddressRequestDict(TypedDict):
    address: CommonAddressInputDict
