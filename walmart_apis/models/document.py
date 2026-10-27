from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.compression_algorithm import CompressionAlgorithmOrStr


class Document(SdkBaseModel):
    document_id: str = Field(alias="documentId")
    url: str
    """Pre-signed URL to download query result data — do not log"""

    compression_algorithm: Optional[CompressionAlgorithmOrStr] = Field(default=UNSET, alias="compressionAlgorithm")


class DocumentDict(TypedDict):
    document_id: str
    url: str
    compression_algorithm: NotRequired[CompressionAlgorithmOrStr]
