from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ship_package import ShipPackage, ShipPackageDict


class MultiPackageShipRequest(SdkBaseModel):
    packages: list[ShipPackage]


class MultiPackageShipRequestDict(TypedDict):
    packages: list[ShipPackageDict]
