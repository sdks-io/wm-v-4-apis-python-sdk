from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class GenerateShipmentContentUpdatePreviewsResponse(SdkBaseModel):
    """The ``generateShipmentContentUpdatePreviews`` response."""

    operation_id: str = Field(alias="operationId")
    """UUID for the given operation."""


class GenerateShipmentContentUpdatePreviewsResponseDict(TypedDict):
    operation_id: str
