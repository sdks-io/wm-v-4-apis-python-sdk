from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class DocumentSummary(SdkBaseModel):
    document_id: Optional[str] = Field(default=UNSET, alias="documentId")


class DocumentSummaryDict(TypedDict):
    document_id: NotRequired[str]
