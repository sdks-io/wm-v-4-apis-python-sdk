from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_address import CommonAddress, CommonAddressDict


class CommonShipmentSource(SdkBaseModel):
    """Specifies the 'ship from' address for the shipment."""

    address: Optional[CommonAddress] = UNSET
    """Specific details to identify a place."""

    source_type: str = Field(alias="sourceType")
    """The type of source for this shipment. Possible values: ``SELLER_FACILITY``."""


class CommonShipmentSourceDict(TypedDict):
    address: NotRequired[CommonAddressDict]
    source_type: str
