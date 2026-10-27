from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_ltl_tracking_detail_input import CommonLtlTrackingDetailInput, CommonLtlTrackingDetailInputDict
from .common_spd_tracking_detail_input import CommonSpdTrackingDetailInput, CommonSpdTrackingDetailInputDict


class CommonTrackingDetailsInput(SdkBaseModel):
    """Tracking information input for LTL and SPD shipments."""

    ltl_tracking_detail: Optional[CommonLtlTrackingDetailInput] = Field(default=UNSET, alias="ltlTrackingDetail")
    """Contains input information to update LTL tracking information."""

    spd_tracking_detail: Optional[CommonSpdTrackingDetailInput] = Field(default=UNSET, alias="spdTrackingDetail")
    """Contains input information to update SPD tracking information."""


class CommonTrackingDetailsInputDict(TypedDict):
    ltl_tracking_detail: NotRequired[CommonLtlTrackingDetailInputDict]
    spd_tracking_detail: NotRequired[CommonSpdTrackingDetailInputDict]
