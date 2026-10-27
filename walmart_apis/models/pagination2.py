from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Pagination2(SdkBaseModel):
    size: Optional[int] = UNSET
    """Maximum number of results per document"""


class Pagination2Dict(TypedDict):
    size: NotRequired[int]
