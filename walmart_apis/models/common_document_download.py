from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel


class CommonDocumentDownload(SdkBaseModel):
    """Resource to download the requested document."""

    download_type: str = Field(alias="downloadType")
    """The type of download. Possible values: ``URL``."""

    expiration: Optional[RFC3339DateTime] = UNSET
    """The URI's expiration time. In ISO 8601 datetime format with pattern ``yyyy-MM-ddTHH:mm:ss.sssZ``."""

    uri: str
    """Uniform resource identifier to identify where the document is located."""


class CommonDocumentDownloadDict(TypedDict):
    download_type: str
    expiration: NotRequired[RFC3339DateTime]
    uri: str
