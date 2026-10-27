from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_dimensions import CommonDimensions, CommonDimensionsDict
from .common_item import CommonItem, CommonItemDict
from .common_region import CommonRegion, CommonRegionDict
from .common_weight import CommonWeight, CommonWeightDict
from .enums.common_box_content_information_source import CommonBoxContentInformationSourceOrStr


class CommonBox(SdkBaseModel):
    """Contains information about a box used in the inbound plan."""

    box_id: Optional[str] = Field(default=UNSET, alias="boxId")
    """The ID provided by Walmart that identifies a given box."""

    content_information_source: Optional[CommonBoxContentInformationSourceOrStr] = Field(
        default=UNSET, alias="contentInformationSource"
    )
    """Indication of how box content is meant to be provided."""

    destination_region: Optional[CommonRegion] = Field(default=UNSET, alias="destinationRegion")
    """Representation of a location used within the inbounding experience."""

    dimensions: Optional[CommonDimensions] = UNSET
    """Measurement of a package's dimensions."""

    external_container_identifier: Optional[str] = Field(default=UNSET, alias="externalContainerIdentifier")
    """The external identifier for this container / box."""

    external_container_identifier_type: Optional[str] = Field(default=UNSET, alias="externalContainerIdentifierType")
    """Type of the external identifier used. Can be: ``WALMART``, ``SSCC``."""

    items: Optional[list[CommonItem]] = UNSET
    """Items contained within the box."""

    package_id: str = Field(alias="packageId")
    """Primary key to uniquely identify a Package (Box or Pallet)."""

    quantity: Optional[int] = UNSET
    """The number of containers where all other properties like weight or dimensions are identical."""

    template_name: Optional[str] = Field(default=UNSET, alias="templateName")
    """Template name of the box."""

    weight: Optional[CommonWeight] = UNSET
    """The weight of a package."""


class CommonBoxDict(TypedDict):
    box_id: NotRequired[str]
    content_information_source: NotRequired[CommonBoxContentInformationSourceOrStr]
    destination_region: NotRequired[CommonRegionDict]
    dimensions: NotRequired[CommonDimensionsDict]
    external_container_identifier: NotRequired[str]
    external_container_identifier_type: NotRequired[str]
    items: NotRequired[list[CommonItemDict]]
    package_id: str
    quantity: NotRequired[int]
    template_name: NotRequired[str]
    weight: NotRequired[CommonWeightDict]
