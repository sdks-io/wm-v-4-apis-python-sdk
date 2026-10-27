from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .classification_refinement import ClassificationRefinement, ClassificationRefinementDict
from .department import Department, DepartmentDict


class Refinements(SdkBaseModel):
    departments: Optional[list[Department]] = UNSET
    classification_refinements: Optional[list[ClassificationRefinement]] = Field(
        default=UNSET, alias="classificationRefinements"
    )


class RefinementsDict(TypedDict):
    departments: NotRequired[list[DepartmentDict]]
    classification_refinements: NotRequired[list[ClassificationRefinementDict]]
