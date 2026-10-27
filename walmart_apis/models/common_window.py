from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CommonWindow(SdkBaseModel):
    """Contains a start and end DateTime representing a time range."""

    editable_until: Optional[RFC3339DateTime] = Field(default=UNSET, alias="editableUntil")
    """The timestamp at which this window can no longer be edited."""

    end: RFC3339DateTime
    """The end timestamp of the window."""

    start: RFC3339DateTime
    """The start timestamp of the window."""


class CommonWindowDict(TypedDict):
    editable_until: NotRequired[RFC3339DateTime]
    end: RFC3339DateTime
    start: RFC3339DateTime
