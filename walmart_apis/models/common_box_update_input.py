from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_dimensions import CommonDimensions, CommonDimensionsDict
from .common_item_input import CommonItemInput, CommonItemInputDict
from .common_weight import CommonWeight, CommonWeightDict
from .enums.common_box_content_information_source import CommonBoxContentInformationSourceOrStr


class CommonBoxUpdateInput(SdkBaseModel):
    """Input information for updating a box."""

    content_information_source: CommonBoxContentInformationSourceOrStr = Field(alias="contentInformationSource")
    """Indication of how box content is meant to be provided."""

    dimensions: CommonDimensions
    """Measurement of a package's dimensions."""

    items: Optional[list[CommonItemInput]] = UNSET
    """The items and their quantity in the box. This must be empty if the box ``contentInformationSource`` is
    ``BARCODE_2D`` or ``MANUAL_PROCESS``."""

    package_id: Optional[str] = Field(default=UNSET, alias="packageId")
    """Primary key to uniquely identify a Box Package. Provide to update an existing box; omit to add a new box. Any
    existing packageIds not provided will be treated as to-be-removed."""

    quantity: int
    """The number of containers where all other properties like weight or dimensions are identical."""

    weight: CommonWeight
    """The weight of a package."""


class CommonBoxUpdateInputDict(TypedDict):
    content_information_source: CommonBoxContentInformationSourceOrStr
    dimensions: CommonDimensionsDict
    items: NotRequired[list[CommonItemInputDict]]
    package_id: NotRequired[str]
    quantity: int
    weight: CommonWeightDict
