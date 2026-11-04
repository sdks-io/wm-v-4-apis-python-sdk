from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BarcodeInstruction(str, Enum):
    """Guidance on which barcode a seller should use when labeling an item."""

    REQUIRES_FNSKU_LABEL = "RequiresFNSKULabel"
    CAN_USE_ORIGINAL_BARCODE = "CanUseOriginalBarcode"
    MUST_PROVIDE_SELLER_SKU = "MustProvideSellerSKU"

    __str__ = str.__str__


BarcodeInstructionOrStr: TypeAlias = Annotated[BarcodeInstruction | str, open_enum_validator(BarcodeInstruction)]
