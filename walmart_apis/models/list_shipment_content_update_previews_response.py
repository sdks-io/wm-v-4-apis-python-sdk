from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_content_update_preview import CommonContentUpdatePreview, CommonContentUpdatePreviewDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListShipmentContentUpdatePreviewsResponse(SdkBaseModel):
    """The ``listShipmentContentUpdatePreviews`` response."""

    content_update_previews: list[CommonContentUpdatePreview] = Field(alias="contentUpdatePreviews")
    """A list of content update previews in a shipment."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListShipmentContentUpdatePreviewsResponseDict(TypedDict):
    content_update_previews: list[CommonContentUpdatePreviewDict]
    pagination: NotRequired[CommonPaginationDict]
