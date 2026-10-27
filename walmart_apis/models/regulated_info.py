from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.regulated_category import RegulatedCategoryOrStr
from .enums.required_verification_method import RequiredVerificationMethodOrStr
from .value_added_service import ValueAddedService, ValueAddedServiceDict


class RegulatedInfo(SdkBaseModel):
    """Verification requirements for an order containing regulated items. Mirrors Amazon SP-API Orders v0
    ``RegulatedInformation`` plus a ``regulatedCategory`` discriminator so a caller can short- circuit when the order is
    not regulated at all."""

    regulated_category: RegulatedCategoryOrStr = Field(alias="regulatedCategory")
    """Top-level category of regulation that applies. NOT_REGULATED means no verification is required and the rest of
    the fields are informational only."""

    required_verification_method: RequiredVerificationMethodOrStr = Field(alias="requiredVerificationMethod")
    """How the buyer must prove identity at delivery. NONE means no verification is required (NOT_REGULATED orders
    always return NONE)."""

    required_age_minimum: Optional[int] = Field(default=UNSET, alias="requiredAgeMinimum")
    """Minimum buyer age in years (e.g. 21 for alcohol in the US)."""

    signature_required: Optional[bool] = Field(default=UNSET, alias="signatureRequired")
    """True when the carrier must capture a signature on delivery."""

    buyer_date_of_birth_required: Optional[bool] = Field(default=UNSET, alias="buyerDateOfBirthRequired")
    """True when the buyer's date of birth must be captured / cross-checked."""

    value_added_services: Optional[list[ValueAddedService]] = Field(default=UNSET, alias="valueAddedServices")
    """Any value-added services attached to the order that are relevant to the regulated workflow (e.g. signed-delivery,
    adult-signature). Empty when none apply."""


class RegulatedInfoDict(TypedDict):
    regulated_category: RegulatedCategoryOrStr
    required_verification_method: RequiredVerificationMethodOrStr
    required_age_minimum: NotRequired[int]
    signature_required: NotRequired[bool]
    buyer_date_of_birth_required: NotRequired[bool]
    value_added_services: NotRequired[list[ValueAddedServiceDict]]
