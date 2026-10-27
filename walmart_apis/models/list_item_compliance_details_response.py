from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_compliance_detail import CommonComplianceDetail, CommonComplianceDetailDict


class ListItemComplianceDetailsResponse(SdkBaseModel):
    """The ``listItemComplianceDetails`` response."""

    compliance_details: Optional[list[CommonComplianceDetail]] = Field(default=UNSET, alias="complianceDetails")
    """List of compliance details."""


class ListItemComplianceDetailsResponseDict(TypedDict):
    compliance_details: NotRequired[list[CommonComplianceDetailDict]]
