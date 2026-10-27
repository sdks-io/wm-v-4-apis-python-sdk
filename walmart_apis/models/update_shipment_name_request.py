from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateShipmentNameRequest(SdkBaseModel):
    """The ``updateShipmentName`` request."""

    name: str
    """A human-readable name to update the shipment name to."""


class UpdateShipmentNameRequestDict(TypedDict):
    name: str
