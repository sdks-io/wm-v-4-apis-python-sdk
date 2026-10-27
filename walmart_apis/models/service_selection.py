from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ServiceSelection(SdkBaseModel):
    """Optional seller-supplied filter to restrict the rate quote to a specific carrier(s) and/or service(s)."""

    service_ids: Optional[list[str]] = Field(default=UNSET, alias="serviceIds")
    carrier_ids: Optional[list[str]] = Field(default=UNSET, alias="carrierIds")


class ServiceSelectionDict(TypedDict):
    service_ids: NotRequired[list[str]]
    carrier_ids: NotRequired[list[str]]
