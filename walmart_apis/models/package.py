from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .item_shipping import ItemShipping, ItemShippingDict
from .money import Money, MoneyDict
from .package_dimensions import PackageDimensions, PackageDimensionsDict
from .weight import Weight, WeightDict


class Package(SdkBaseModel):
    dimensions: PackageDimensions
    weight: Weight
    insured_value: Optional[Money] = Field(default=UNSET, alias="insuredValue")
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    is_hazmat: Optional[bool] = Field(default=UNSET, alias="isHazmat")
    seller_declared_value: Optional[Money] = Field(default=UNSET, alias="sellerDeclaredValue")
    """Canonical monetary amount (string value + ISO 4217 currency code)."""

    package_client_reference_id: str = Field(alias="packageClientReferenceId")
    """Seller-supplied unique id for this package within the shipment."""

    items: Optional[list[ItemShipping]] = UNSET


class PackageDict(TypedDict):
    dimensions: PackageDimensionsDict
    weight: WeightDict
    insured_value: NotRequired[MoneyDict]
    is_hazmat: NotRequired[bool]
    seller_declared_value: NotRequired[MoneyDict]
    package_client_reference_id: str
    items: NotRequired[list[ItemShippingDict]]
