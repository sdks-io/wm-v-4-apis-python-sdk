from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.id_type1 import IdType1OrStr
from .price_to_estimate_fees import PriceToEstimateFees, PriceToEstimateFeesDict


class FeesEstimateIdentifier(SdkBaseModel):
    """Echoes back the item identifier and request parameters that produced this result. Mirrors SP-API
    FeesEstimateIdentifier."""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="MarketplaceId")
    id_type: Optional[IdType1OrStr] = Field(default=UNSET, alias="IdType")
    id_value: Optional[str] = Field(default=UNSET, alias="IdValue")
    is_walmart_fulfilled: Optional[bool] = Field(default=UNSET, alias="IsWalmartFulfilled")
    price_to_estimate_fees: Optional[PriceToEstimateFees] = Field(default=UNSET, alias="PriceToEstimateFees")
    """Price information used to estimate fees."""

    seller_id: Optional[str] = Field(default=UNSET, alias="SellerId")
    seller_input_identifier: Optional[str] = Field(default=UNSET, alias="SellerInputIdentifier")
    """Echoed from the request Identifier field."""

    optional_fulfillment_program: Optional[str] = Field(default=UNSET, alias="OptionalFulfillmentProgram")


class FeesEstimateIdentifierDict(TypedDict):
    marketplace_id: NotRequired[str]
    id_type: NotRequired[IdType1OrStr]
    id_value: NotRequired[str]
    is_walmart_fulfilled: NotRequired[bool]
    price_to_estimate_fees: NotRequired[PriceToEstimateFeesDict]
    seller_id: NotRequired[str]
    seller_input_identifier: NotRequired[str]
    optional_fulfillment_program: NotRequired[str]
