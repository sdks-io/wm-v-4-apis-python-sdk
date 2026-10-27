from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .rejected_shipping_service import RejectedShippingService, RejectedShippingServiceDict
from .shipping_service import ShippingService, ShippingServiceDict


class GetEligibleShippingServicesResponse(SdkBaseModel):
    shipping_service_list: Optional[list[ShippingService]] = Field(default=UNSET, alias="shippingServiceList")
    rejected_shipping_service_list: Optional[list[RejectedShippingService]] = Field(
        default=UNSET, alias="rejectedShippingServiceList"
    )


class GetEligibleShippingServicesResponseDict(TypedDict):
    shipping_service_list: NotRequired[list[ShippingServiceDict]]
    rejected_shipping_service_list: NotRequired[list[RejectedShippingServiceDict]]
