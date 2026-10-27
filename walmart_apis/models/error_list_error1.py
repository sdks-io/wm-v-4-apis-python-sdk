from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .error3 import Error3, Error3Dict


class ErrorListError1(SdkBaseModel):
    errors: list[Error3]
    """One or more errors describing why the request failed"""


class ErrorListError1Dict(TypedDict):
    errors: list[Error3Dict]
