from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonPrepType(str, Enum):
    """Preparation instructions for shipping an item to Walmart's fulfillment network."""

    ITEM_BLACK_SHRINKWRAP = "ITEM_BLACK_SHRINKWRAP"
    ITEM_BLANKSTK = "ITEM_BLANKSTK"
    ITEM_BOXING = "ITEM_BOXING"
    ITEM_BUBBLEWRAP = "ITEM_BUBBLEWRAP"
    ITEM_CAP_SEALING = "ITEM_CAP_SEALING"
    ITEM_DEBUNDLE = "ITEM_DEBUNDLE"
    ITEM_HANG_GARMENT = "ITEM_HANG_GARMENT"
    ITEM_LABELING = "ITEM_LABELING"
    ITEM_NO_PREP = "ITEM_NO_PREP"
    ITEM_POLYBAGGING = "ITEM_POLYBAGGING"
    ITEM_RMOVHANG = "ITEM_RMOVHANG"
    ITEM_SETCREAT = "ITEM_SETCREAT"
    ITEM_SETSTK = "ITEM_SETSTK"
    ITEM_SIOC = "ITEM_SIOC"
    ITEM_SUFFOSTK = "ITEM_SUFFOSTK"
    ITEM_TAPING = "ITEM_TAPING"

    __str__ = str.__str__


CommonPrepTypeOrStr: TypeAlias = Annotated[CommonPrepType | str, open_enum_validator(CommonPrepType)]
