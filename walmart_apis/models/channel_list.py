from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .channel import Channel, ChannelDict


class ChannelList(SdkBaseModel):
    channels: Optional[list[Channel]] = UNSET


class ChannelListDict(TypedDict):
    channels: NotRequired[list[ChannelDict]]
