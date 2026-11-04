from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WfsPrimeDetailsType(SdkBaseModel):
    """Walmart Fulfillment Services (WFS) Prime eligibility information for the offer."""

    is_wfs_prime: bool = Field(alias="IsWFSPrime")
    """Indicates whether the offer is eligible for WFS Prime."""

    is_national_wfs_prime: bool = Field(alias="IsNationalWFSPrime")
    """Indicates whether the offer is eligible for WFS Prime throughout the marketplace."""


class WfsPrimeDetailsTypeDict(TypedDict):
    is_wfs_prime: bool
    is_national_wfs_prime: bool
