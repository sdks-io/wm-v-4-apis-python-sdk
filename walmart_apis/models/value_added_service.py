from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ValueAddedService(SdkBaseModel):
    """Additional service associated with an order’s regulated delivery requirements."""

    code: str
    """Identifier for the value-added service, such as ``ADULT_SIGNATURE``."""

    description: Optional[str] = UNSET
    """Human-readable description of the service."""


class ValueAddedServiceDict(TypedDict):
    code: str
    description: NotRequired[str]
