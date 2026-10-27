from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .common_incentive import CommonIncentive, CommonIncentiveDict


class CommonPlacementOption(SdkBaseModel):
    """Contains information pertaining to the placement of the contents of an inbound plan and the related costs."""

    discounts: list[CommonIncentive]
    """Discount for the offered option."""

    expiration: Optional[RFC3339DateTime] = UNSET
    """The expiration date of the placement option. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mm:ss.sssZ``."""

    fees: list[CommonIncentive]
    """The fee for the offered option."""

    placement_option_id: str = Field(alias="placementOptionId")
    """The identifier of a placement option. A placement option represents the shipment splits and destinations of
    SKUs."""

    shipment_ids: list[str] = Field(alias="shipmentIds")
    """Shipment IDs."""

    status: str
    """The status of a placement option. Possible values: ``OFFERED``, ``ACCEPTED``, ``EXPIRED``."""


class CommonPlacementOptionDict(TypedDict):
    discounts: list[CommonIncentiveDict]
    expiration: NotRequired[RFC3339DateTime]
    fees: list[CommonIncentiveDict]
    placement_option_id: str
    shipment_ids: list[str]
    status: str
