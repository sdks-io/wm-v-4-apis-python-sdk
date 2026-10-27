from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Channel(SdkBaseModel):
    channel_owner: str = Field(alias="channelOwner")
    channel_name: str = Field(alias="channelName")
    type_: str = Field(alias="type")
    webhook_config: Optional[Any] = Field(default=UNSET, alias="webhookConfig")
    status: Optional[str] = UNSET
    channel_id: Optional[str] = Field(default=UNSET, alias="channelId")
    created_timestamp: Optional[int] = Field(default=UNSET, alias="createdTimestamp")
    last_modified_timestamp: Optional[int] = Field(default=UNSET, alias="lastModifiedTimestamp")


class ChannelDict(TypedDict):
    channel_owner: str
    channel_name: str
    type_: str
    webhook_config: NotRequired[Any]
    status: NotRequired[str]
    channel_id: NotRequired[str]
    created_timestamp: NotRequired[int]
    last_modified_timestamp: NotRequired[int]
