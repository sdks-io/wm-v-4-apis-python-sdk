from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class WfsprimeDetailsType(SdkBaseModel):
    """Walmart Fulfillment Services prime eligibility information."""

    is_wfs_prime: bool = Field(alias="IsWFSPrime")
    """Indicates whether the offer is eligible for WFS Prime."""

    is_national_wfs_prime: bool = Field(alias="IsNationalWFSPrime")
    """Indicates whether the offer is eligible for WFS Prime throughout the entire marketplace."""


class WfsprimeDetailsTypeDict(TypedDict):
    is_wfs_prime: bool
    is_national_wfs_prime: bool
