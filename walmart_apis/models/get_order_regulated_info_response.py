from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .regulated_info import RegulatedInfo, RegulatedInfoDict


class GetOrderRegulatedInfoResponse(SdkBaseModel):
    payload: Optional[RegulatedInfo] = UNSET
    """Verification requirements for an order containing regulated items. Mirrors Amazon SP-API Orders v0
    ``RegulatedInformation`` plus a ``regulatedCategory`` discriminator so a caller can short- circuit when the order is
    not regulated at all."""


class GetOrderRegulatedInfoResponseDict(TypedDict):
    payload: NotRequired[RegulatedInfoDict]
