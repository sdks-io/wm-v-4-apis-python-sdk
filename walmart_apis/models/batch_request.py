from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.http_method_model import HttpMethodModelOrStr


class BatchRequest(SdkBaseModel):
    """Common properties of batch requests against individual APIs."""

    uri: str
    """The resource path of the operation being called in batch, without query parameters."""

    method: HttpMethodModelOrStr
    """The HTTP method associated with the individual APIs being called as part of the batch request."""

    headers: Optional[Any] = UNSET
    """A mapping of additional HTTP headers to send for the individual batch request."""


class BatchRequestDict(TypedDict):
    uri: str
    method: HttpMethodModelOrStr
    headers: NotRequired[Any]
