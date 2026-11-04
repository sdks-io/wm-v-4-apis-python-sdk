from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CompressionAlgorithmFeeds(str, Enum):
    """Compression applied to the document; decompress before parsing if present"""

    GZIP = "GZIP"

    __str__ = str.__str__


CompressionAlgorithmFeedsOrStr: TypeAlias = Annotated[
    CompressionAlgorithmFeeds | str, open_enum_validator(CompressionAlgorithmFeeds)
]
