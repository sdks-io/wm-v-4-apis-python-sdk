from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.status1 import Status1OrStr
from .issue import Issue, IssueDict


class ListingsItemSubmissionResponse(SdkBaseModel):
    sku: str
    status: Status1OrStr
    submission_id: Optional[str] = Field(default=UNSET, alias="submissionId")
    issues: Optional[list[Issue]] = UNSET


class ListingsItemSubmissionResponseDict(TypedDict):
    sku: str
    status: Status1OrStr
    submission_id: NotRequired[str]
    issues: NotRequired[list[IssueDict]]
