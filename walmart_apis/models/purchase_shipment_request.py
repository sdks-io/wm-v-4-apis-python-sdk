from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .requested_document_specification import RequestedDocumentSpecification, RequestedDocumentSpecificationDict
from .requested_value_added_service import RequestedValueAddedService, RequestedValueAddedServiceDict


class PurchaseShipmentRequest(SdkBaseModel):
    request_token: str = Field(alias="requestToken")
    """requestToken returned by the prior getRates response."""

    rate_id: str = Field(alias="rateId")
    """The chosen rateId from the getRates response."""

    requested_document_specification: RequestedDocumentSpecification = Field(alias="requestedDocumentSpecification")
    requested_value_added_services: Optional[list[RequestedValueAddedService]] = Field(
        default=UNSET, alias="requestedValueAddedServices"
    )
    additional_inputs: Optional[Any] = Field(default=UNSET, alias="additionalInputs")
    """Carrier/service-specific inputs validated against the schema returned by getAdditionalInputs."""


class PurchaseShipmentRequestDict(TypedDict):
    request_token: str
    rate_id: str
    requested_document_specification: RequestedDocumentSpecificationDict
    requested_value_added_services: NotRequired[list[RequestedValueAddedServiceDict]]
    additional_inputs: NotRequired[Any]
