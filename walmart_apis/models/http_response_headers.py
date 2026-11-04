from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HttpResponseHeaders(SdkBaseModel):
    """Additional HTTP headers returned for an individual batch request."""

    date: Optional[str] = Field(default=UNSET, alias="Date")
    """Timestamp when the API received the request."""

    x_request_id: Optional[str] = Field(default=UNSET, alias="X-Request-Id")
    """Unique identifier for the API request."""


class HttpResponseHeadersDict(TypedDict):
    date: NotRequired[str]
    x_request_id: NotRequired[str]
