from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CancelQueryResponse(SdkBaseModel):
    query_id: Optional[str] = Field(default=UNSET, alias="queryId")


class CancelQueryResponseDict(TypedDict):
    query_id: NotRequired[str]
