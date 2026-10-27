from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateFeedResponse(SdkBaseModel):
    feed_id: str = Field(alias="feedId")
    """Unique identifier for the submitted feed. Use this to poll feed status."""

    feed_type: Optional[str] = Field(default=UNSET, alias="feedType")
    """The feed type that was submitted"""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    """The marketplace the feed was submitted to"""


class CreateFeedResponseDict(TypedDict):
    feed_id: str
    feed_type: NotRequired[str]
    marketplace_id: NotRequired[str]
