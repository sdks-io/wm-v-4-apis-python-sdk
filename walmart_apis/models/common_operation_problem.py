from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonOperationProblem(SdkBaseModel):
    """A problem with additional properties persisted to an operation."""

    code: str
    """An error code that identifies the type of error that occurred."""

    details: Optional[str] = UNSET
    """Additional details that can help the caller understand or fix the issue."""

    message: str
    """A message that describes the error condition."""

    severity: str
    """The severity of the problem. Possible values: ``WARNING``, ``ERROR``."""


class CommonOperationProblemDict(TypedDict):
    code: str
    details: NotRequired[str]
    message: str
    severity: str
