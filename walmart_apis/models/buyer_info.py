from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class BuyerInfo(SdkBaseModel):
    """Buyer name, email address, and anonymized phone number."""

    purchase_order_id: Optional[str] = Field(default=UNSET, alias="purchaseOrderId")
    """Purchase order identifier assigned by Walmart."""

    buyer_name: Optional[str] = Field(default=UNSET, alias="buyerName")
    """Name of the buyer associated with the order."""

    buyer_email: Optional[EmailStr] = Field(default=UNSET, alias="buyerEmail")
    """Email address of the buyer associated with the order."""

    buyer_phone_anonymized: Optional[str] = Field(default=UNSET, alias="buyerPhoneAnonymized")
    """Buyer phone number with only the last four digits visible. All other digits are hidden."""


class BuyerInfoDict(TypedDict):
    purchase_order_id: NotRequired[str]
    buyer_name: NotRequired[str]
    buyer_email: NotRequired[EmailStr]
    buyer_phone_anonymized: NotRequired[str]
