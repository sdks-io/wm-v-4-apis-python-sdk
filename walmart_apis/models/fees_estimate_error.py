from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FeesEstimateError(SdkBaseModel):
    """Error information returned when a fee estimate cannot be calculated."""

    type_: str = Field(alias="Type")
    """Type of fee estimate error."""

    code: str = Field(alias="Code")
    """Code identifying the fee estimate error."""

    message: str = Field(alias="Message")
    """Message describing the fee estimate error."""

    detail: list[str] = Field(alias="Detail")
    """Additional details about the fee estimate error."""


class FeesEstimateErrorDict(TypedDict):
    type_: str
    code: str
    message: str
    detail: list[str]
