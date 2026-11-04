from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .package_dimensions_orders import PackageDimensionsOrders, PackageDimensionsOrdersDict
from .ship_package_line import ShipPackageLine, ShipPackageLineDict
from .tracking_info import TrackingInfo, TrackingInfoDict


class ShipPackage(SdkBaseModel):
    """Tracking, dimensions, and order lines associated with a package."""

    package_id: Optional[str] = Field(default=UNSET, alias="packageId")
    """Optional identifier supplied for the physical package."""

    tracking_info: TrackingInfo = Field(alias="trackingInfo")
    """Carrier, tracking number, and shipment details."""

    dimensions: Optional[PackageDimensionsOrders] = UNSET
    """Physical dimensions and weight of a package."""

    lines: list[ShipPackageLine]
    """Order lines included in this package. Provide at least one line."""


class ShipPackageDict(TypedDict):
    package_id: NotRequired[str]
    tracking_info: TrackingInfoDict
    dimensions: NotRequired[PackageDimensionsOrdersDict]
    lines: list[ShipPackageLineDict]
