from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.common_all_owners_constraint import CommonAllOwnersConstraintOrStr
from .enums.common_owner_constraint import CommonOwnerConstraintOrStr
from .enums.common_prep_category import CommonPrepCategoryOrStr
from .enums.common_prep_type import CommonPrepTypeOrStr


class CommonMskuPrepDetail(SdkBaseModel):
    """An MSKU and its related prep details."""

    all_owners_constraint: Optional[CommonAllOwnersConstraintOrStr] = Field(default=UNSET, alias="allOwnersConstraint")
    """A constraint that applies to all owners. If no constraint is specified, defer to any individual owner
    constraints."""

    label_owner_constraint: Optional[CommonOwnerConstraintOrStr] = Field(default=UNSET, alias="labelOwnerConstraint")
    """A constraint that can apply to an individual owner."""

    msku: str
    """The merchant SKU, a merchant-supplied identifier for a specific SKU."""

    prep_category: CommonPrepCategoryOrStr = Field(alias="prepCategory")
    """The preparation category for shipping an item to Walmart's fulfillment network."""

    prep_owner_constraint: Optional[CommonOwnerConstraintOrStr] = Field(default=UNSET, alias="prepOwnerConstraint")
    """A constraint that can apply to an individual owner."""

    prep_types: list[CommonPrepTypeOrStr] = Field(alias="prepTypes")
    """A list of preparation types associated with a preparation category."""


class CommonMskuPrepDetailDict(TypedDict):
    all_owners_constraint: NotRequired[CommonAllOwnersConstraintOrStr]
    label_owner_constraint: NotRequired[CommonOwnerConstraintOrStr]
    msku: str
    prep_category: CommonPrepCategoryOrStr
    prep_owner_constraint: NotRequired[CommonOwnerConstraintOrStr]
    prep_types: list[CommonPrepTypeOrStr]
