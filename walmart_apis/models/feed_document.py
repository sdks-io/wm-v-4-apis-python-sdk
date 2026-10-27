from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.compression_algorithm import CompressionAlgorithmOrStr


class FeedDocument(SdkBaseModel):
    feed_document_id: str = Field(alias="feedDocumentId")
    """Unique identifier for this feed result document"""

    url: str
    """Pre-signed URL to download the document (valid 15 minutes) — do not log"""

    compression_algorithm: Optional[CompressionAlgorithmOrStr] = Field(default=UNSET, alias="compressionAlgorithm")
    """Compression applied to the document; decompress before parsing if present"""


class FeedDocumentDict(TypedDict):
    feed_document_id: str
    url: str
    compression_algorithm: NotRequired[CompressionAlgorithmOrStr]
