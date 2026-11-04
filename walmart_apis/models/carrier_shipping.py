from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CarrierShipping(SdkBaseModel):
    id: str
    name: str
    """Carrier display name. Walmart-specific enum-widening for internally-fulfilled carriers (e.g. WALMART_GROUND) is
    captured by leaving this as a free string rather than a closed enum."""


class CarrierShippingDict(TypedDict):
    id: str
    name: str
