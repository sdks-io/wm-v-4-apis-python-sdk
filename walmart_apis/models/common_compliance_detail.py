from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_tax_details import CommonTaxDetails, CommonTaxDetailsDict


class CommonComplianceDetail(SdkBaseModel):
    """Contains item identifiers and related tax information."""

    msku: Optional[str] = UNSET
    """The merchant SKU, a merchant-supplied identifier for a specific SKU."""

    tax_details: Optional[CommonTaxDetails] = Field(default=UNSET, alias="taxDetails")
    """Information used to determine the tax compliance."""


class CommonComplianceDetailDict(TypedDict):
    msku: NotRequired[str]
    tax_details: NotRequired[CommonTaxDetailsDict]
