from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .address_input import AddressInput, AddressInputDict


class UpdateShipmentSourceAddressRequest(SdkBaseModel):
    """The ``updateShipmentSourceAddress`` request."""

    address: AddressInput
    """Specific details to identify a place (input variant — phone required)."""


class UpdateShipmentSourceAddressRequestDict(TypedDict):
    address: AddressInputDict
