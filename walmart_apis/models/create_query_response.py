from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CreateQueryResponse(SdkBaseModel):
    query_id: str = Field(alias="queryId")


class CreateQueryResponseDict(TypedDict):
    query_id: str
