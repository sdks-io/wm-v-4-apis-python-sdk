from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_document_download import CommonDocumentDownload, CommonDocumentDownloadDict


class GetDeliveryChallanDocumentResponse(SdkBaseModel):
    """The ``getDeliveryChallanDocument`` response."""

    document_download: CommonDocumentDownload = Field(alias="documentDownload")
    """Resource to download the requested document."""


class GetDeliveryChallanDocumentResponseDict(TypedDict):
    document_download: CommonDocumentDownloadDict
