from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ValueAddedService(SdkBaseModel):
    code: str
    """Short service code (e.g. ADULT_SIGNATURE)."""

    description: Optional[str] = UNSET
    """Human-readable description of the service."""


class ValueAddedServiceDict(TypedDict):
    code: str
    description: NotRequired[str]
