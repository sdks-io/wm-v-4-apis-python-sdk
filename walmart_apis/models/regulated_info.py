from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.regulated_category import RegulatedCategoryOrStr
from .enums.required_verification_method import RequiredVerificationMethodOrStr
from .value_added_service import ValueAddedService, ValueAddedServiceDict


class RegulatedInfo(SdkBaseModel):
    """Age and identity verification requirements associated with an order."""

    regulated_category: RegulatedCategoryOrStr = Field(alias="regulatedCategory")
    """Category of regulation associated with the order. ``NOT_REGULATED`` indicates that no regulated category has been
    identified."""

    required_verification_method: RequiredVerificationMethodOrStr = Field(alias="requiredVerificationMethod")
    """Identification method required at delivery. ``NONE`` indicates no verification method."""

    required_age_minimum: Optional[int] = Field(default=UNSET, alias="requiredAgeMinimum")
    """Minimum buyer age, in years, required for the order. For example, 21 for alcohol. Zero indicates no age
    requirement."""

    signature_required: Optional[bool] = Field(default=UNSET, alias="signatureRequired")
    """Indicates whether a signature is required at delivery."""

    buyer_date_of_birth_required: Optional[bool] = Field(default=UNSET, alias="buyerDateOfBirthRequired")
    """Indicates whether the buyer’s date of birth must be collected or verified."""

    value_added_services: Optional[list[ValueAddedService]] = Field(default=UNSET, alias="valueAddedServices")
    """Value-added services associated with an order containing regulated items, such as adult-signature delivery. Empty
    when no additional services apply."""


class RegulatedInfoDict(TypedDict):
    regulated_category: RegulatedCategoryOrStr
    required_verification_method: RequiredVerificationMethodOrStr
    required_age_minimum: NotRequired[int]
    signature_required: NotRequired[bool]
    buyer_date_of_birth_required: NotRequired[bool]
    value_added_services: NotRequired[list[ValueAddedServiceDict]]
