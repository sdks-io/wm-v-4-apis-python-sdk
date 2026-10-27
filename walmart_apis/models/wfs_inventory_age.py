from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class WfsInventoryAge(SdkBaseModel):
    """Units grouped by storage duration. Used for long-term storage fee assessment. 7 buckets: days365Plus,
    days365To450, and days450Plus reflect the upstream split-aged-buckets feature — days365Plus is the pre-split
    total."""

    days0_to90: Optional[int] = Field(default=UNSET, alias="days0To90")
    days91_to180: Optional[int] = Field(default=UNSET, alias="days91To180")
    days181_to270: Optional[int] = Field(default=UNSET, alias="days181To270")
    days271_to365: Optional[int] = Field(default=UNSET, alias="days271To365")
    days365_plus: Optional[int] = Field(default=UNSET, alias="days365Plus")
    days365_to450: Optional[int] = Field(default=UNSET, alias="days365To450")
    days450_plus: Optional[int] = Field(default=UNSET, alias="days450Plus")


class WfsInventoryAgeDict(TypedDict):
    days0_to90: NotRequired[int]
    days91_to180: NotRequired[int]
    days181_to270: NotRequired[int]
    days271_to365: NotRequired[int]
    days365_plus: NotRequired[int]
    days365_to450: NotRequired[int]
    days450_plus: NotRequired[int]
