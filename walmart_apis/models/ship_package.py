from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .package_dimensions1 import PackageDimensions1, PackageDimensions1Dict
from .ship_package_line import ShipPackageLine, ShipPackageLineDict
from .tracking_info import TrackingInfo, TrackingInfoDict


class ShipPackage(SdkBaseModel):
    package_id: Optional[str] = Field(default=UNSET, alias="packageId")
    """Caller-supplied stable identifier for this physical package. Optional — server falls back to the package's
    tracking number when echoed in the response."""

    tracking_info: TrackingInfo = Field(alias="trackingInfo")
    dimensions: Optional[PackageDimensions1] = UNSET
    """Physical dimensions of a shipped package. All numeric values are non-negative; unit enums avoid the
    unit-ambiguity bug that bit gmp-orders-mono PayloadUtil pre-2024."""

    lines: list[ShipPackageLine]


class ShipPackageDict(TypedDict):
    package_id: NotRequired[str]
    tracking_info: TrackingInfoDict
    dimensions: NotRequired[PackageDimensions1Dict]
    lines: list[ShipPackageLineDict]
