from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class RequestedValueAddedService(SdkBaseModel):
    id: str
    """Identifier of the value-added service being requested."""

    details: Optional[Any] = UNSET
    """Service-specific input payload. Validated against the schema published in availableValueAddedServices on the
    corresponding Rate. Compressed shape; see TODO."""


class RequestedValueAddedServiceDict(TypedDict):
    id: str
    details: NotRequired[Any]
