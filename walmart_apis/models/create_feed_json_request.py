from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateFeedJsonRequest(SdkBaseModel):
    feed_data: Any = Field(alias="feedData")
    """Feed payload as inline JSON. Structure varies by feedType."""


class CreateFeedJsonRequestDict(TypedDict):
    feed_data: Any
