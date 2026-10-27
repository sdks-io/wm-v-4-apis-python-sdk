from __future__ import annotations

from pydantic import EmailStr, Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.account_status import AccountStatusOrStr
from .enums.seller_type import SellerTypeOrStr


class SellerAccount(SdkBaseModel):
    seller_id: Optional[str] = Field(default=UNSET, alias="sellerId")
    business_name: Optional[str] = Field(default=UNSET, alias="businessName")
    email: Optional[EmailStr] = UNSET
    account_status: Optional[AccountStatusOrStr] = Field(default=UNSET, alias="accountStatus")
    seller_type: Optional[SellerTypeOrStr] = Field(default=UNSET, alias="sellerType")
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")


class SellerAccountDict(TypedDict):
    seller_id: NotRequired[str]
    business_name: NotRequired[str]
    email: NotRequired[EmailStr]
    account_status: NotRequired[AccountStatusOrStr]
    seller_type: NotRequired[SellerTypeOrStr]
    created_at: NotRequired[RFC3339DateTime]
