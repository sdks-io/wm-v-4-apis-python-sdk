from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error3 import Error3, Error3Dict


class ErrorList(SdkBaseModel):
    errors: list[Error3]


class ErrorListDict(TypedDict):
    errors: list[Error3Dict]
