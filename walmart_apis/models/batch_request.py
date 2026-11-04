from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.http_method_model import HttpMethodModelOrStr


class BatchRequest(SdkBaseModel):
    """Common properties for individual API requests submitted as part of a batch."""

    uri: str
    """Resource path of the operation being called in the batch, without query parameters."""

    method: HttpMethodModelOrStr
    """HTTP method used for the individual API request in the batch."""

    headers: Optional[Any] = UNSET
    """Additional HTTP headers to send with an individual batch request."""


class BatchRequestDict(TypedDict):
    uri: str
    method: HttpMethodModelOrStr
    headers: NotRequired[Any]
