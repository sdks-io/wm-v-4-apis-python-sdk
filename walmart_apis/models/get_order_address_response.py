from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .payload2 import Payload2, Payload2Dict


class GetOrderAddressResponse(SdkBaseModel):
    """Order identifier and shipping address."""

    payload: Optional[Payload2] = UNSET
    """Shipping address for the purchase order. Do not log response bodies containing shipping addresses."""


class GetOrderAddressResponseDict(TypedDict):
    payload: NotRequired[Payload2Dict]
