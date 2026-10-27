from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonMskuQuantity(SdkBaseModel):
    """Represents an MSKU and the related quantity."""

    msku: str
    """The merchant SKU, a merchant-supplied identifier for a specific SKU."""

    quantity: int
    """A positive integer."""


class CommonMskuQuantityDict(TypedDict):
    msku: str
    quantity: int
