from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .regulated_info import RegulatedInfo, RegulatedInfoDict


class GetOrderRegulatedInfoResponse(SdkBaseModel):
    """Verification requirements for an order containing regulated items."""

    payload: Optional[RegulatedInfo] = UNSET
    """Age and identity verification requirements associated with an order."""


class GetOrderRegulatedInfoResponseDict(TypedDict):
    payload: NotRequired[RegulatedInfoDict]
