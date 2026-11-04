from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ClassificationRefinement(SdkBaseModel):
    """Category information and matching result count."""

    category_id: Optional[str] = Field(default=UNSET, alias="categoryId")
    """Identifier of the classification category."""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """Display name of the classification category."""

    number_of_results: Optional[int] = Field(default=UNSET, alias="numberOfResults")
    """Number of search results associated with the classification category."""


class ClassificationRefinementDict(TypedDict):
    category_id: NotRequired[str]
    display_name: NotRequired[str]
    number_of_results: NotRequired[int]
