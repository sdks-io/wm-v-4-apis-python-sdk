from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ShipmentBoxContentsSource(str, Enum):
    """How box contents were declared for this shipment (upstream ``BoxContentsSource``). NOTE: distinct vocabulary from
    the shared ``BoxContentInformationSource`` enum used on ``Box`` -- that schema models a DIFFERENT upstream concept
    (box-level packing-plan input) with its own ``BOX_CONTENT_PROVIDED``/``MANUAL_PROCESS``/``BARCODE_2D`` values; do
    not conflate the two."""

    _2_D_BARCODE = "2D_BARCODE"
    NONE = "NONE"

    __str__ = str.__str__


ShipmentBoxContentsSourceOrStr: TypeAlias = Annotated[
    ShipmentBoxContentsSource | str, open_enum_validator(ShipmentBoxContentsSource)
]
