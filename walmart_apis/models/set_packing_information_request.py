from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_package_grouping_input import CommonPackageGroupingInput, CommonPackageGroupingInputDict


class SetPackingInformationRequest(SdkBaseModel):
    """The ``setPackingInformation`` request."""

    package_groupings: list[CommonPackageGroupingInput] = Field(alias="packageGroupings")
    """List of packing information for the inbound plan."""


class SetPackingInformationRequestDict(TypedDict):
    package_groupings: list[CommonPackageGroupingInputDict]
