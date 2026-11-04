from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrepInstruction(str, Enum):
    """A single preparation action applicable to an item."""

    POLYBAGGING = "Polybagging"
    BUBBLE_WRAPPING = "BubbleWrapping"
    TAPING = "Taping"
    NO_PREP = "NoPrep"
    LABELING = "Labeling"

    __str__ = str.__str__


PrepInstructionOrStr: TypeAlias = Annotated[PrepInstruction | str, open_enum_validator(PrepInstruction)]
