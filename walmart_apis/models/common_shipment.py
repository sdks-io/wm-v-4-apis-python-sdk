from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_contact_information import CommonContactInformation, CommonContactInformationDict
from .common_dates import CommonDates, CommonDatesDict
from .common_freight_information import CommonFreightInformation, CommonFreightInformationDict
from .common_selected_delivery_window import CommonSelectedDeliveryWindow, CommonSelectedDeliveryWindowDict
from .common_self_ship_appointment_details import CommonSelfShipAppointmentDetails, CommonSelfShipAppointmentDetailsDict
from .common_shipment_destination import CommonShipmentDestination, CommonShipmentDestinationDict
from .common_shipment_source import CommonShipmentSource, CommonShipmentSourceDict
from .common_tracking_details import CommonTrackingDetails, CommonTrackingDetailsDict


class CommonShipment(SdkBaseModel):
    """Contains information pertaining to a shipment in an inbound plan."""

    contact_information: Optional[CommonContactInformation] = Field(default=UNSET, alias="contactInformation")
    """The seller's contact information."""

    dates: Optional[CommonDates] = UNSET
    """Specifies the date that the seller expects their shipment will be shipped."""

    destination: CommonShipmentDestination
    """The Walmart Ship Node address and warehouse ID."""

    freight_information: Optional[CommonFreightInformation] = Field(default=UNSET, alias="freightInformation")
    """Freight information describes the SKUs that are in transit."""

    name: Optional[str] = UNSET
    """The name of the shipment."""

    placement_option_id: str = Field(alias="placementOptionId")
    """The identifier of a placement option."""

    selected_delivery_window: Optional[CommonSelectedDeliveryWindow] = Field(
        default=UNSET, alias="selectedDeliveryWindow"
    )
    """Selected delivery window attributes."""

    selected_transportation_option_id: Optional[str] = Field(default=UNSET, alias="selectedTransportationOptionId")
    """Identifier of a transportation option."""

    self_ship_appointment_details: Optional[list[CommonSelfShipAppointmentDetails]] = Field(
        default=UNSET, alias="selfShipAppointmentDetails"
    )
    """List of self ship appointment details."""

    shipment_confirmation_id: Optional[str] = Field(default=UNSET, alias="shipmentConfirmationId")
    """The confirmed shipment ID which shows up on labels."""

    shipment_id: str = Field(alias="shipmentId")
    """Identifier of a shipment."""

    source: CommonShipmentSource
    """Specifies the 'ship from' address for the shipment."""

    status: Optional[str] = UNSET
    """The status of a shipment. Possible values: ``ABANDONED``, ``CANCELLED``, ``CHECKED_IN``, ``CLOSED``, ``DELETED``,
    ``DELIVERED``, ``IN_TRANSIT``, ``MIXED``, ``READY_TO_SHIP``, ``RECEIVING``, ``SHIPPED``, ``UNCONFIRMED``,
    ``WORKING``."""

    tracking_details: Optional[CommonTrackingDetails] = Field(default=UNSET, alias="trackingDetails")
    """Tracking information for LTL and SPD shipments."""


class CommonShipmentDict(TypedDict):
    contact_information: NotRequired[CommonContactInformationDict]
    dates: NotRequired[CommonDatesDict]
    destination: CommonShipmentDestinationDict
    freight_information: NotRequired[CommonFreightInformationDict]
    name: NotRequired[str]
    placement_option_id: str
    selected_delivery_window: NotRequired[CommonSelectedDeliveryWindowDict]
    selected_transportation_option_id: NotRequired[str]
    self_ship_appointment_details: NotRequired[list[CommonSelfShipAppointmentDetailsDict]]
    shipment_confirmation_id: NotRequired[str]
    shipment_id: str
    source: CommonShipmentSourceDict
    status: NotRequired[str]
    tracking_details: NotRequired[CommonTrackingDetailsDict]
