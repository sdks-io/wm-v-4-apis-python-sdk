from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClassificationRefinement(SdkBaseModel):
    category_id: Optional[str] = Field(default=UNSET, alias="categoryId")
    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    number_of_results: Optional[int] = Field(default=UNSET, alias="numberOfResults")


class ClassificationRefinementDict(TypedDict):
    category_id: NotRequired[str]
    display_name: NotRequired[str]
    number_of_results: NotRequired[int]
