from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class FeesEstimateError(SdkBaseModel):
    """Error detail when a fee estimate could not be computed."""

    type_: str = Field(alias="Type")
    code: str = Field(alias="Code")
    message: str = Field(alias="Message")
    detail: list[str] = Field(alias="Detail")


class FeesEstimateErrorDict(TypedDict):
    type_: str
    code: str
    message: str
    detail: list[str]
