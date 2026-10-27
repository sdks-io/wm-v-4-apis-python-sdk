from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_msku_prep_detail import CommonMskuPrepDetail, CommonMskuPrepDetailDict


class ListPrepDetailsResponse(SdkBaseModel):
    """The ``listPrepDetails`` response."""

    msku_prep_details: list[CommonMskuPrepDetail] = Field(alias="mskuPrepDetails")
    """A list of MSKUs and related prep details."""


class ListPrepDetailsResponseDict(TypedDict):
    msku_prep_details: list[CommonMskuPrepDetailDict]
