from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_contact_information import CommonContactInformation, CommonContactInformationDict


class CommonTransportationSelection(SdkBaseModel):
    """The transportation option selected to confirm."""

    contact_information: Optional[CommonContactInformation] = Field(default=UNSET, alias="contactInformation")
    """The seller's contact information."""

    shipment_id: str = Field(alias="shipmentId")
    """Shipment ID that the transportation option is for."""

    transportation_option_id: str = Field(alias="transportationOptionId")
    """Transportation option being selected for the provided shipment."""


class CommonTransportationSelectionDict(TypedDict):
    contact_information: NotRequired[CommonContactInformationDict]
    shipment_id: str
    transportation_option_id: str
