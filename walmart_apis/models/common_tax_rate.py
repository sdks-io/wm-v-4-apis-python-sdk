from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonTaxRate(SdkBaseModel):
    """Contains the type and rate of tax."""

    cess_rate: Optional[float] = Field(default=UNSET, alias="cessRate")
    """Rate of cess tax."""

    gst_rate: Optional[float] = Field(default=UNSET, alias="gstRate")
    """Rate of gst tax."""

    tax_type: Optional[str] = Field(default=UNSET, alias="taxType")
    """Type of tax. Possible values: ``CGST``, ``SGST``, ``IGST``, ``TOTAL_TAX``."""


class CommonTaxRateDict(TypedDict):
    cess_rate: NotRequired[float]
    gst_rate: NotRequired[float]
    tax_type: NotRequired[str]
