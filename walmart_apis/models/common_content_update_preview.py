from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel
from .common_requested_updates import CommonRequestedUpdates, CommonRequestedUpdatesDict
from .common_transportation_option import CommonTransportationOption, CommonTransportationOptionDict


class CommonContentUpdatePreview(SdkBaseModel):
    """Preview of the changes that will be applied to the shipment."""

    content_update_preview_id: str = Field(alias="contentUpdatePreviewId")
    """Identifier of a content update preview."""

    expiration: RFC3339DateTime
    """The time at which the content update expires. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mm:ss.sssZ``."""

    requested_updates: CommonRequestedUpdates = Field(alias="requestedUpdates")
    """Objects that were included in the update request."""

    transportation_option: CommonTransportationOption = Field(alias="transportationOption")
    """Contains information pertaining to a transportation option and the related carrier."""


class CommonContentUpdatePreviewDict(TypedDict):
    content_update_preview_id: str
    expiration: RFC3339DateTime
    requested_updates: CommonRequestedUpdatesDict
    transportation_option: CommonTransportationOptionDict
