from __future__ import annotations

from typing_extensions import TypedDict

from ..core import RFC3339DateTime, SdkBaseModel


class CommonWindowInput(SdkBaseModel):
    """Contains only a starting DateTime."""

    start: RFC3339DateTime
    """The start date of the window. In ISO 8601 datetime format with minute precision."""


class CommonWindowInputDict(TypedDict):
    start: RFC3339DateTime
