from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.processing_status import ProcessingStatusOrStr


class Report(SdkBaseModel):
    report_id: str = Field(alias="reportId")
    report_type: str = Field(alias="reportType")
    data_start_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dataStartTime")
    data_end_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="dataEndTime")
    report_schedule_id: Optional[str] = Field(default=UNSET, alias="reportScheduleId")
    created_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdTime")
    processing_status: ProcessingStatusOrStr = Field(alias="processingStatus")
    processing_start_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="processingStartTime")
    processing_end_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="processingEndTime")
    report_document_id: Optional[str] = Field(default=UNSET, alias="reportDocumentId")
    """Present only when processingStatus is DONE"""


class ReportDict(TypedDict):
    report_id: str
    report_type: str
    data_start_time: NotRequired[RFC3339DateTime]
    data_end_time: NotRequired[RFC3339DateTime]
    report_schedule_id: NotRequired[str]
    created_time: NotRequired[RFC3339DateTime]
    processing_status: ProcessingStatusOrStr
    processing_start_time: NotRequired[RFC3339DateTime]
    processing_end_time: NotRequired[RFC3339DateTime]
    report_document_id: NotRequired[str]
