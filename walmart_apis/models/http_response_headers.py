from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class HttpResponseHeaders(SdkBaseModel):
    """A mapping of additional HTTP headers to receive for the individual batch request."""

    date: Optional[str] = Field(default=UNSET, alias="Date")
    """The timestamp that the API request was received."""

    x_request_id: Optional[str] = Field(default=UNSET, alias="X-Request-Id")
    """Unique request reference identifier."""


class HttpResponseHeadersDict(TypedDict):
    date: NotRequired[str]
    x_request_id: NotRequired[str]
