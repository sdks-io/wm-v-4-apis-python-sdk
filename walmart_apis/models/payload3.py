from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .ineligible_rate import IneligibleRate, IneligibleRateDict
from .rate import Rate, RateDict


class Payload3(SdkBaseModel):
    rates: Optional[list[Rate]] = UNSET
    ineligible_rates: Optional[list[IneligibleRate]] = Field(default=UNSET, alias="ineligibleRates")
    request_token: Optional[str] = Field(default=UNSET, alias="requestToken")
    """Opaque token to be passed back on subsequent purchaseShipment or getAdditionalInputs calls to identify this rate
    quote session."""


class Payload3Dict(TypedDict):
    rates: NotRequired[list[RateDict]]
    ineligible_rates: NotRequired[list[IneligibleRateDict]]
    request_token: NotRequired[str]
