from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_error import CommonError, CommonErrorDict


class CommonErrorListError(SdkBaseModel):
    """A list of error responses returned when a request is unsuccessful."""

    errors: list[CommonError]
    """List of errors."""


class CommonErrorListErrorDict(TypedDict):
    errors: list[CommonErrorDict]
