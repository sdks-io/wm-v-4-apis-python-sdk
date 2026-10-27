from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_document_download import CommonDocumentDownload, CommonDocumentDownloadDict


class CreateMarketplaceItemLabelsResponse(SdkBaseModel):
    """The ``createMarketplaceItemLabels`` response."""

    document_downloads: list[CommonDocumentDownload] = Field(alias="documentDownloads")
    """Resources to download the requested document."""


class CreateMarketplaceItemLabelsResponseDict(TypedDict):
    document_downloads: list[CommonDocumentDownloadDict]
