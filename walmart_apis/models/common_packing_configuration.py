from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_box_requirements import CommonBoxRequirements, CommonBoxRequirementsDict
from .common_shipping_requirements import CommonShippingRequirements, CommonShippingRequirementsDict
from .enums.common_box_content_information_source import CommonBoxContentInformationSourceOrStr


class CommonPackingConfiguration(SdkBaseModel):
    """A way to configure this packing option."""

    box_packing_methods: Optional[list[CommonBoxContentInformationSourceOrStr]] = Field(
        default=UNSET, alias="boxPackingMethods"
    )
    """The box content information sources that are allowed."""

    box_requirements: Optional[CommonBoxRequirements] = Field(default=UNSET, alias="boxRequirements")
    """The requirements for a box in the packing option."""

    shipping_requirements: Optional[list[CommonShippingRequirements]] = Field(
        default=UNSET, alias="shippingRequirements"
    )
    """A list of supported shipping requirements for this packing configuration."""


class CommonPackingConfigurationDict(TypedDict):
    box_packing_methods: NotRequired[list[CommonBoxContentInformationSourceOrStr]]
    box_requirements: NotRequired[CommonBoxRequirementsDict]
    shipping_requirements: NotRequired[list[CommonShippingRequirementsDict]]
