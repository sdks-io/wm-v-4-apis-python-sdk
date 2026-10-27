from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .address1 import Address1, Address1Dict
from .channel_details import ChannelDetails, ChannelDetailsDict
from .package import Package, PackageDict
from .requested_document_specification import RequestedDocumentSpecification, RequestedDocumentSpecificationDict
from .requested_value_added_service import RequestedValueAddedService, RequestedValueAddedServiceDict
from .service_selection import ServiceSelection, ServiceSelectionDict


class OneClickShipmentRequest(SdkBaseModel):
    ship_to: Address1 = Field(alias="shipTo")
    ship_from: Address1 = Field(alias="shipFrom")
    return_to: Optional[Address1] = Field(default=UNSET, alias="returnTo")
    ship_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="shipDate")
    packages: list[Package]
    service_selection: ServiceSelection = Field(alias="serviceSelection")
    """Optional seller-supplied filter to restrict the rate quote to a specific carrier(s) and/or service(s)."""

    value_added_services: Optional[list[RequestedValueAddedService]] = Field(default=UNSET, alias="valueAddedServices")
    requested_document_specification: RequestedDocumentSpecification = Field(alias="requestedDocumentSpecification")
    channel_details: ChannelDetails = Field(alias="channelDetails")


class OneClickShipmentRequestDict(TypedDict):
    ship_to: Address1Dict
    ship_from: Address1Dict
    return_to: NotRequired[Address1Dict]
    ship_date: NotRequired[RFC3339DateTime]
    packages: list[PackageDict]
    service_selection: ServiceSelectionDict
    value_added_services: NotRequired[list[RequestedValueAddedServiceDict]]
    requested_document_specification: RequestedDocumentSpecificationDict
    channel_details: ChannelDetailsDict
