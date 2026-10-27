from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetOffersHttpStatusLine(SdkBaseModel):
    """The HTTP status line associated with the response."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """The HTTP response Status Code."""

    reason_phrase: Optional[str] = Field(default=UNSET, alias="reasonPhrase")
    """The HTTP response Reason-Phrase."""


class GetOffersHttpStatusLineDict(TypedDict):
    status_code: NotRequired[int]
    reason_phrase: NotRequired[str]
