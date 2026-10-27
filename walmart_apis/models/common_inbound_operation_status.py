from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_operation_problem import CommonOperationProblem, CommonOperationProblemDict
from .enums.common_operation_status import CommonOperationStatusOrStr


class CommonInboundOperationStatus(SdkBaseModel):
    """GetInboundOperationStatus response."""

    operation: str
    """The name of the operation in the asynchronous API call."""

    operation_id: str = Field(alias="operationId")
    """The operation ID returned by the asynchronous API call."""

    operation_problems: list[CommonOperationProblem] = Field(alias="operationProblems")
    """The problems in the processing of the asynchronous operation."""

    operation_status: CommonOperationStatusOrStr = Field(alias="operationStatus")
    """The status of an operation."""


class CommonInboundOperationStatusDict(TypedDict):
    operation: str
    operation_id: str
    operation_problems: list[CommonOperationProblemDict]
    operation_status: CommonOperationStatusOrStr
