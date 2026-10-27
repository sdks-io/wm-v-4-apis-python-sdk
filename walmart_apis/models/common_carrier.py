from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonCarrier(SdkBaseModel):
    """The carrier for the inbound shipment."""

    alpha_code: Optional[str] = Field(default=UNSET, alias="alphaCode")
    """The carrier code. For example, USPS or DHLEX."""

    name: Optional[str] = UNSET
    """The name of the carrier."""


class CommonCarrierDict(TypedDict):
    alpha_code: NotRequired[str]
    name: NotRequired[str]
