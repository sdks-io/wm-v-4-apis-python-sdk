from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .carrier_shipping import CarrierShipping, CarrierShippingDict
from .money import Money, MoneyDict
from .package_document import PackageDocument, PackageDocumentDict
from .service import Service, ServiceDict


class PackageDocumentDetail(SdkBaseModel):
    package_client_reference_id: str = Field(alias="packageClientReferenceId")
    package_documents: list[PackageDocument] = Field(alias="packageDocuments")
    tracking_id: Optional[str] = Field(default=UNSET, alias="trackingId")
    carrier: Optional[CarrierShipping] = UNSET
    service: Optional[Service] = UNSET
    tracking_url: Optional[str] = Field(default=UNSET, alias="trackingUrl")
    """Carrier-hosted tracking page URL for this package, when the carrier/upstream provides one . Absent for carriers
    or upstream responses that don't surface a tracking URL."""

    actual_charge: Optional[Money] = Field(default=UNSET, alias="actualCharge")
    """Canonical monetary amount (string value + ISO 4217 currency code)."""


class PackageDocumentDetailDict(TypedDict):
    package_client_reference_id: str
    package_documents: list[PackageDocumentDict]
    tracking_id: NotRequired[str]
    carrier: NotRequired[CarrierShippingDict]
    service: NotRequired[ServiceDict]
    tracking_url: NotRequired[str]
    actual_charge: NotRequired[MoneyDict]
