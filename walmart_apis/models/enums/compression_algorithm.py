from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CompressionAlgorithm(str, Enum):
    GZIP = "GZIP"

    __str__ = str.__str__


CompressionAlgorithmOrStr: TypeAlias = Annotated[CompressionAlgorithm | str, open_enum_validator(CompressionAlgorithm)]
