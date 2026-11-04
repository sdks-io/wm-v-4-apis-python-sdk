from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class PaginationDataKiosk(SdkBaseModel):
    pagination_token: Optional[str] = Field(default=UNSET, alias="paginationToken")


class PaginationDataKioskDict(TypedDict):
    pagination_token: NotRequired[str]
