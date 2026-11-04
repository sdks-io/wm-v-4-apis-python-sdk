from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.id_type1 import IdType1OrStr
from .price_to_estimate_fees import PriceToEstimateFees, PriceToEstimateFeesDict


class FeesEstimateIdentifier(SdkBaseModel):
    """Item identifier and request information associated with the fee estimate result."""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="MarketplaceId")
    """Marketplace identifier associated with the fee estimate result."""

    id_type: Optional[IdType1OrStr] = Field(default=UNSET, alias="IdType")
    """Type of item identifier associated with the fee estimate result."""

    id_value: Optional[str] = Field(default=UNSET, alias="IdValue")
    """Item identifier associated with the fee estimate result."""

    is_walmart_fulfilled: Optional[bool] = Field(default=UNSET, alias="IsWalmartFulfilled")
    """Indicates whether Walmart Fulfillment Services (WFS) fulfills the item."""

    price_to_estimate_fees: Optional[PriceToEstimateFees] = Field(default=UNSET, alias="PriceToEstimateFees")
    """Price information used to estimate fees."""

    seller_id: Optional[str] = Field(default=UNSET, alias="SellerId")
    """Seller identifier associated with the fee estimate result."""

    seller_input_identifier: Optional[str] = Field(default=UNSET, alias="SellerInputIdentifier")
    """Identifier provided in the request and returned with the fee estimate result."""

    optional_fulfillment_program: Optional[str] = Field(default=UNSET, alias="OptionalFulfillmentProgram")
    """Fulfillment program information associated with the fee estimate request."""


class FeesEstimateIdentifierDict(TypedDict):
    marketplace_id: NotRequired[str]
    id_type: NotRequired[IdType1OrStr]
    id_value: NotRequired[str]
    is_walmart_fulfilled: NotRequired[bool]
    price_to_estimate_fees: NotRequired[PriceToEstimateFeesDict]
    seller_id: NotRequired[str]
    seller_input_identifier: NotRequired[str]
    optional_fulfillment_program: NotRequired[str]
