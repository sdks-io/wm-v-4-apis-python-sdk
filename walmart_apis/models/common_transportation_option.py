from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_appointment_slot_time import CommonAppointmentSlotTime, CommonAppointmentSlotTimeDict
from .common_carrier import CommonCarrier, CommonCarrierDict
from .common_quote import CommonQuote, CommonQuoteDict


class CommonTransportationOption(SdkBaseModel):
    """Contains information pertaining to a transportation option and the related carrier."""

    carrier: CommonCarrier
    """The carrier for the inbound shipment."""

    carrier_appointment: Optional[CommonAppointmentSlotTime] = Field(default=UNSET, alias="carrierAppointment")
    """Contains details for a transportation carrier appointment."""

    preconditions: list[str]
    """Identifies a list of preconditions for confirming the transportation option."""

    quote: Optional[CommonQuote] = UNSET
    """The estimated shipping cost associated with the transportation option."""

    shipment_id: str = Field(alias="shipmentId")
    """Identifier of a shipment."""

    shipping_mode: str = Field(alias="shippingMode")
    """Mode of shipment transportation. Possible values: ``GROUND_SMALL_PARCEL``, ``FREIGHT_LTL``,
    ``FREIGHT_FTL_PALLET``, ``FREIGHT_FTL_NONPALLET``, ``OCEAN_LCL``, ``OCEAN_FCL``, ``AIR_SMALL_PARCEL``,
    ``AIR_SMALL_PARCEL_EXPRESS``."""

    shipping_solution: str = Field(alias="shippingSolution")
    """Shipping program for the option. Possible values: ``WALMART_PARTNERED_CARRIER``, ``USE_YOUR_OWN_CARRIER``."""

    transportation_option_id: str = Field(alias="transportationOptionId")
    """Identifier of a transportation option."""


class CommonTransportationOptionDict(TypedDict):
    carrier: CommonCarrierDict
    carrier_appointment: NotRequired[CommonAppointmentSlotTimeDict]
    preconditions: list[str]
    quote: NotRequired[CommonQuoteDict]
    shipment_id: str
    shipping_mode: str
    shipping_solution: str
    transportation_option_id: str
