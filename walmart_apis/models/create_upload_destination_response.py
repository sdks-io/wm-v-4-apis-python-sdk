from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CreateUploadDestinationResponse(SdkBaseModel):
    upload_destination_id: Optional[str] = Field(default=UNSET, alias="uploadDestinationId")
    """The upload destination ID to pass when creating a feed or report"""

    url: Optional[str] = UNSET
    """Pre-signed URL for a PUT upload (valid 15 minutes) — do not log"""

    headers: Optional[dict[str, str]] = UNSET
    """HTTP headers to include with the upload PUT request"""


class CreateUploadDestinationResponseDict(TypedDict):
    upload_destination_id: NotRequired[str]
    url: NotRequired[str]
    headers: NotRequired[dict[str, str]]
