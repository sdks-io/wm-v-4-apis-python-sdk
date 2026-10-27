from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_shipment_transportation_configuration import (
    CommonShipmentTransportationConfiguration,
    CommonShipmentTransportationConfigurationDict,
)


class GenerateTransportationOptionsRequest(SdkBaseModel):
    """The ``generateTransportationOptions`` request."""

    placement_option_id: str = Field(alias="placementOptionId")
    """The placement option to generate transportation options for."""

    shipment_transportation_configurations: list[CommonShipmentTransportationConfiguration] = Field(
        alias="shipmentTransportationConfigurations"
    )
    """List of shipment transportation configurations."""


class GenerateTransportationOptionsRequestDict(TypedDict):
    placement_option_id: str
    shipment_transportation_configurations: list[CommonShipmentTransportationConfigurationDict]
