from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonShippingConfiguration(SdkBaseModel):
    """The shipping configurations supported for the packing option."""

    shipping_mode: Optional[str] = Field(default=UNSET, alias="shippingMode")
    """Mode of shipment transportation. Possible values: ``GROUND_SMALL_PARCEL``, ``FREIGHT_LTL``,
    ``FREIGHT_FTL_PALLET``, ``FREIGHT_FTL_NONPALLET``, ``OCEAN_LCL``, ``OCEAN_FCL``, ``AIR_SMALL_PARCEL``,
    ``AIR_SMALL_PARCEL_EXPRESS``."""

    shipping_solution: Optional[str] = Field(default=UNSET, alias="shippingSolution")
    """Shipping program for the option. Possible values: ``WALMART_PARTNERED_CARRIER``, ``USE_YOUR_OWN_CARRIER``."""


class CommonShippingConfigurationDict(TypedDict):
    shipping_mode: NotRequired[str]
    shipping_solution: NotRequired[str]
