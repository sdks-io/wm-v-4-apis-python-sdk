from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_tax_details import CommonTaxDetails, CommonTaxDetailsDict


class UpdateItemComplianceDetailsRequest(SdkBaseModel):
    """The ``updateItemComplianceDetails`` request."""

    msku: str
    """The merchant SKU, a merchant-supplied identifier for a specific SKU."""

    tax_details: CommonTaxDetails = Field(alias="taxDetails")
    """Information used to determine the tax compliance."""


class UpdateItemComplianceDetailsRequestDict(TypedDict):
    msku: str
    tax_details: CommonTaxDetailsDict
