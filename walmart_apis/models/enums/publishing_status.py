from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PublishingStatus(str, Enum):
    """Current listing state of the item on Walmart.com."""

    PUBLISHED = "Published"
    UNPUBLISHED = "Unpublished"
    PROCESSING = "Processing"
    STAGE = "Stage"
    ERROR = "Error"
    WFS_INELIGIBLE = "WfsIneligible"

    __str__ = str.__str__


PublishingStatusOrStr: TypeAlias = Annotated[PublishingStatus | str, open_enum_validator(PublishingStatus)]
