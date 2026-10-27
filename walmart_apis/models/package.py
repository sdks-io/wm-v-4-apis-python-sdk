from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item3 import Item3, Item3Dict
from .money import Money, MoneyDict
from .package_dimensions import PackageDimensions, PackageDimensionsDict
from .weight import Weight, WeightDict


class Package(SdkBaseModel):
    dimensions: PackageDimensions
    weight: Weight
    insured_value: Optional[Money] = Field(default=UNSET, alias="insuredValue")
    is_hazmat: Optional[bool] = Field(default=UNSET, alias="isHazmat")
    seller_declared_value: Optional[Money] = Field(default=UNSET, alias="sellerDeclaredValue")
    package_client_reference_id: str = Field(alias="packageClientReferenceId")
    """Seller-supplied unique id for this package within the shipment."""

    items: Optional[list[Item3]] = UNSET


class PackageDict(TypedDict):
    dimensions: PackageDimensionsDict
    weight: WeightDict
    insured_value: NotRequired[MoneyDict]
    is_hazmat: NotRequired[bool]
    seller_declared_value: NotRequired[MoneyDict]
    package_client_reference_id: str
    items: NotRequired[list[Item3Dict]]
