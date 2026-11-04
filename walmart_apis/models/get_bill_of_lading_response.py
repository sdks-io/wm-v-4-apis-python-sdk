from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_document_download import CommonDocumentDownload, CommonDocumentDownloadDict


class GetBillOfLadingResponse(SdkBaseModel):
    """The ``getBillOfLading`` response. Wraps the shared ``DocumentDownload`` shape (same one used by
    ``getDeliveryChallanDocument``) rather than a bespoke envelope, since upstream's payload is likewise just a single
    signed download URL."""

    document_download: CommonDocumentDownload = Field(alias="documentDownload")
    """Resource to download the requested document."""


class GetBillOfLadingResponseDict(TypedDict):
    document_download: CommonDocumentDownloadDict
