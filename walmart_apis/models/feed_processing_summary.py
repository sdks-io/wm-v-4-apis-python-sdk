from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class FeedProcessingSummary(SdkBaseModel):
    total_record_count: Optional[int] = Field(default=UNSET, alias="totalRecordCount")
    """Total number of records in the submitted feed"""

    processed_record_count: Optional[int] = Field(default=UNSET, alias="processedRecordCount")
    """Number of records processed so far"""

    success_count: Optional[int] = Field(default=UNSET, alias="successCount")
    """Number of records processed successfully"""

    error_count: Optional[int] = Field(default=UNSET, alias="errorCount")
    """Number of records that failed processing"""

    warning_count: Optional[int] = Field(default=UNSET, alias="warningCount")
    """Number of records processed with warnings"""


class FeedProcessingSummaryDict(TypedDict):
    total_record_count: NotRequired[int]
    processed_record_count: NotRequired[int]
    success_count: NotRequired[int]
    error_count: NotRequired[int]
    warning_count: NotRequired[int]
