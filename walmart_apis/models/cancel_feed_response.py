from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CancelFeedResponse(SdkBaseModel):
    feed_id: str = Field(alias="feedId")
    """The feed that was requested to be cancelled"""

    status: str
    """Result of the cancellation request"""


class CancelFeedResponseDict(TypedDict):
    feed_id: str
    status: str
