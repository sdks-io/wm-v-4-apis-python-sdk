from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_box_update_input import CommonBoxUpdateInput, CommonBoxUpdateInputDict
from .common_item_input import CommonItemInput, CommonItemInputDict


class CommonRequestedUpdates(SdkBaseModel):
    """Objects that were included in the update request."""

    boxes: Optional[list[CommonBoxUpdateInput]] = UNSET
    """A list of boxes that will be present in the shipment after the update."""

    items: Optional[list[CommonItemInput]] = UNSET
    """A list of all items that will be present in the shipment after the update."""


class CommonRequestedUpdatesDict(TypedDict):
    boxes: NotRequired[list[CommonBoxUpdateInputDict]]
    items: NotRequired[list[CommonItemInputDict]]
