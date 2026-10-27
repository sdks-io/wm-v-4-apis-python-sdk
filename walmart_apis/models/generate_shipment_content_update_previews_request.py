from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_box_update_input import CommonBoxUpdateInput, CommonBoxUpdateInputDict
from .common_item_input import CommonItemInput, CommonItemInputDict


class GenerateShipmentContentUpdatePreviewsRequest(SdkBaseModel):
    """The ``generateShipmentContentUpdatePreviews`` request."""

    boxes: list[CommonBoxUpdateInput]
    """A list of boxes that will be present in the shipment after the update."""

    items: list[CommonItemInput]
    """A list of all items that will be present in the shipment after the update."""


class GenerateShipmentContentUpdatePreviewsRequestDict(TypedDict):
    boxes: list[CommonBoxUpdateInputDict]
    items: list[CommonItemInputDict]
