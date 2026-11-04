from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .ship_package import ShipPackage, ShipPackageDict


class MultiPackageShipRequest(SdkBaseModel):
    """Packages and their associated order lines for a shipment."""

    packages: list[ShipPackage]
    """Packages included in the multi-package shipment. Provide at least one package."""


class MultiPackageShipRequestDict(TypedDict):
    packages: list[ShipPackageDict]
