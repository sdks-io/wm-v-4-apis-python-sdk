from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_box_input import CommonBoxInput, CommonBoxInputDict


class CommonPackageGroupingInput(SdkBaseModel):
    """Packing information for the inbound plan."""

    boxes: list[CommonBoxInput]
    """Box level information being provided."""

    packing_group_id: Optional[str] = Field(default=UNSET, alias="packingGroupId")
    """The ID of the ``packingGroup`` that packages are grouped according to. Provide before placement confirmation."""

    shipment_id: Optional[str] = Field(default=UNSET, alias="shipmentId")
    """The ID of the shipment that packages are grouped according to. Provide after placement confirmation."""


class CommonPackageGroupingInputDict(TypedDict):
    boxes: list[CommonBoxInputDict]
    packing_group_id: NotRequired[str]
    shipment_id: NotRequired[str]
