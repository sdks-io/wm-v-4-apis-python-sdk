from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonShippingRequirements(SdkBaseModel):
    """The possible shipping modes for the packing option for a given shipping solution."""

    modes: list[str]
    """Available shipment modes for this shipping program."""

    solution: str
    """Shipping program for the option. Can be: ``WALMART_PARTNERED_CARRIER``, ``USE_YOUR_OWN_CARRIER``."""


class CommonShippingRequirementsDict(TypedDict):
    modes: list[str]
    solution: str
