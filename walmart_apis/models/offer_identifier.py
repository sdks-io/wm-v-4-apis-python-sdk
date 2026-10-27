from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.fulfillment_type1 import FulfillmentType1OrStr


class OfferIdentifier(SdkBaseModel):
    """Identifies an offer."""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    """A marketplace identifier."""

    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    """The seller identifier."""

    sku: Optional[str] = UNSET
    """The seller stock keeping unit (SKU) of the item."""

    fulfillment_type: Optional[FulfillmentType1OrStr] = Field(default=UNSET, alias="fulfillmentType")
    """The fulfillment type for the offer. Possible values: WFS, SELLER."""


class OfferIdentifierDict(TypedDict):
    marketplace_id: NotRequired[str]
    seller_id: NotRequired[str]
    sku: NotRequired[str]
    fulfillment_type: NotRequired[FulfillmentType1OrStr]
