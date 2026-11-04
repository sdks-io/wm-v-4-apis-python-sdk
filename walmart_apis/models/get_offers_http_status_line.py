from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetOffersHttpStatusLine(SdkBaseModel):
    """HTTP status information associated with the response."""

    status_code: Optional[int] = Field(default=UNSET, alias="statusCode")
    """HTTP status code returned for the response."""

    reason_phrase: Optional[str] = Field(default=UNSET, alias="reasonPhrase")
    """HTTP reason phrase returned for the response."""


class GetOffersHttpStatusLineDict(TypedDict):
    status_code: NotRequired[int]
    reason_phrase: NotRequired[str]
