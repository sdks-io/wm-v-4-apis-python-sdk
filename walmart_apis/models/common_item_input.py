from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.common_label_owner import CommonLabelOwnerOrStr
from .enums.common_prep_owner import CommonPrepOwnerOrStr


class CommonItemInput(SdkBaseModel):
    """Defines an item's input parameters."""

    expiration: Optional[str] = UNSET
    """The expiration date of the MSKU. In ISO 8601 date format with pattern ``YYYY-MM-DD``. Items with the same MSKU
    but different expiration dates cannot go into the same box."""

    label_owner: CommonLabelOwnerOrStr = Field(alias="labelOwner")
    """Specifies who will label the items. Options include ``SELLER`` and ``NONE``."""

    manufacturing_lot_code: Optional[str] = Field(default=UNSET, alias="manufacturingLotCode")
    """The manufacturing lot code."""

    msku: str
    """The merchant SKU, a merchant-supplied identifier of a specific SKU."""

    prep_owner: CommonPrepOwnerOrStr = Field(alias="prepOwner")
    """The owner of the preparations, if special preparations are required."""

    quantity: int
    """The number of units of the specified MSKU that will be shipped."""


class CommonItemInputDict(TypedDict):
    expiration: NotRequired[str]
    label_owner: CommonLabelOwnerOrStr
    manufacturing_lot_code: NotRequired[str]
    msku: str
    prep_owner: CommonPrepOwnerOrStr
    quantity: int
