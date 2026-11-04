from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .pagination_data_kiosk import PaginationDataKiosk, PaginationDataKioskDict
from .query import Query, QueryDict


class GetQueriesResponse(SdkBaseModel):
    queries: Optional[list[Query]] = UNSET
    pagination: Optional[PaginationDataKiosk] = UNSET


class GetQueriesResponseDict(TypedDict):
    queries: NotRequired[list[QueryDict]]
    pagination: NotRequired[PaginationDataKioskDict]
