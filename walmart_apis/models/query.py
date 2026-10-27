from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .document_summary import DocumentSummary, DocumentSummaryDict
from .enums.processing_status import ProcessingStatusOrStr
from .pagination3 import Pagination3, Pagination3Dict


class Query(SdkBaseModel):
    query_id: str = Field(alias="queryId")
    query: Optional[str] = UNSET
    processing_status: ProcessingStatusOrStr = Field(alias="processingStatus")
    created_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdAt")
    updated_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="updatedAt")
    data_documents: Optional[list[DocumentSummary]] = Field(default=UNSET, alias="dataDocuments")
    """Present only when processingStatus is DONE"""

    pagination: Optional[Pagination3] = UNSET


class QueryDict(TypedDict):
    query_id: str
    query: NotRequired[str]
    processing_status: ProcessingStatusOrStr
    created_at: NotRequired[RFC3339DateTime]
    updated_at: NotRequired[RFC3339DateTime]
    data_documents: NotRequired[list[DocumentSummaryDict]]
    pagination: NotRequired[Pagination3Dict]
