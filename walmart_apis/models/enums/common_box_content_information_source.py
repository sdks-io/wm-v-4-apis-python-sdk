from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CommonBoxContentInformationSource(str, Enum):
    """Indication of how box content is meant to be provided."""

    BOX_CONTENT_PROVIDED = "BOX_CONTENT_PROVIDED"
    MANUAL_PROCESS = "MANUAL_PROCESS"
    BARCODE_2_D = "BARCODE_2D"

    __str__ = str.__str__


CommonBoxContentInformationSourceOrStr: TypeAlias = Annotated[
    CommonBoxContentInformationSource | str, open_enum_validator(CommonBoxContentInformationSource)
]
