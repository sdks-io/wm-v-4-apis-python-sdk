from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_msku_prep_detail_input import CommonMskuPrepDetailInput, CommonMskuPrepDetailInputDict


class SetPrepDetailsRequest(SdkBaseModel):
    """The ``setPrepDetails`` request."""

    marketplace_id: str = Field(alias="marketplaceId")
    """The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
    <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__."""

    msku_prep_details: list[CommonMskuPrepDetailInput] = Field(alias="mskuPrepDetails")
    """A list of MSKUs and related prep details."""


class SetPrepDetailsRequestDict(TypedDict):
    marketplace_id: str
    msku_prep_details: list[CommonMskuPrepDetailInputDict]
