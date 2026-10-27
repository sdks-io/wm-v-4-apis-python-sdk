from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_contact_information import CommonContactInformation, CommonContactInformationDict
from .common_freight_information import CommonFreightInformation, CommonFreightInformationDict
from .common_pallet_input import CommonPalletInput, CommonPalletInputDict
from .common_window_input import CommonWindowInput, CommonWindowInputDict


class CommonShipmentTransportationConfiguration(SdkBaseModel):
    """Details needed to generate the transportation options."""

    contact_information: Optional[CommonContactInformation] = Field(default=UNSET, alias="contactInformation")
    """The seller's contact information."""

    freight_information: Optional[CommonFreightInformation] = Field(default=UNSET, alias="freightInformation")
    """Freight information describes the SKUs that are in transit."""

    pallets: Optional[list[CommonPalletInput]] = UNSET
    """List of pallet configuration inputs."""

    ready_to_ship_window: CommonWindowInput = Field(alias="readyToShipWindow")
    """Contains only a starting DateTime."""

    shipment_id: str = Field(alias="shipmentId")
    """Identifier of a shipment."""


class CommonShipmentTransportationConfigurationDict(TypedDict):
    contact_information: NotRequired[CommonContactInformationDict]
    freight_information: NotRequired[CommonFreightInformationDict]
    pallets: NotRequired[list[CommonPalletInputDict]]
    ready_to_ship_window: CommonWindowInputDict
    shipment_id: str
