from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_document_download import CommonDocumentDownload, CommonDocumentDownloadDict


class GetLabelsResponse(SdkBaseModel):
    """The ``getLabels`` response . Wraps the shared ``DocumentDownload`` shape (same one used by
    ``getBillOfLading``/``getDeliveryChallanDocument``), since upstream's payload is likewise just a single signed
    download URL."""

    document_download: CommonDocumentDownload = Field(alias="documentDownload")
    """Resource to download the requested document."""


class GetLabelsResponseDict(TypedDict):
    document_download: CommonDocumentDownloadDict
