from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AnnualStatementOptsResponse(SdkBaseModel):
    is_opted_in: Optional[bool] = Field(default=UNSET, alias="isOptedIn")
    statement_year: Optional[int] = Field(default=UNSET, alias="statementYear")


class AnnualStatementOptsResponseDict(TypedDict):
    is_opted_in: NotRequired[bool]
    statement_year: NotRequired[int]
