from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.compression_algorithm import CompressionAlgorithmOrStr


class ReportDocument(SdkBaseModel):
    report_document_id: str = Field(alias="reportDocumentId")
    url: str
    """Pre-signed URL to download the report — do not log"""

    compression_algorithm: Optional[CompressionAlgorithmOrStr] = Field(default=UNSET, alias="compressionAlgorithm")


class ReportDocumentDict(TypedDict):
    report_document_id: str
    url: str
    compression_algorithm: NotRequired[CompressionAlgorithmOrStr]
