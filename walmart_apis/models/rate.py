from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .carrier import Carrier, CarrierDict
from .money import Money, MoneyDict
from .promise import Promise, PromiseDict
from .service import Service, ServiceDict
from .weight import Weight, WeightDict


class Rate(SdkBaseModel):
    rate_id: str = Field(alias="rateId")
    carrier: Carrier
    service: Service
    total_charge: Money = Field(alias="totalCharge")
    billed_weight: Optional[Weight] = Field(default=UNSET, alias="billedWeight")
    expiration_time: Optional[RFC3339DateTime] = Field(default=UNSET, alias="expirationTime")
    promise: Optional[Promise] = UNSET
    supported_document_specifications: Optional[list[Any]] = Field(
        default=UNSET, alias="supportedDocumentSpecifications"
    )
    """List of label/document formats supported by this rate. Each entry shape matches industry-standard
    SupportedDocumentSpecification; tier-1 fidelity is sufficient for v4 — see TODO at top of file."""

    available_value_added_services: Optional[list[Any]] = Field(default=UNSET, alias="availableValueAddedServices")
    """Value-added services available for purchase at this rate (signature, COD, dangerous goods, etc). Compressed
    shape; full fidelity tracked in a follow-up PR."""


class RateDict(TypedDict):
    rate_id: str
    carrier: CarrierDict
    service: ServiceDict
    total_charge: MoneyDict
    billed_weight: NotRequired[WeightDict]
    expiration_time: NotRequired[RFC3339DateTime]
    promise: NotRequired[PromiseDict]
    supported_document_specifications: NotRequired[list[Any]]
    available_value_added_services: NotRequired[list[Any]]
