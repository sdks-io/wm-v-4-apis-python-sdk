from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .event import Event, EventDict
from .proof_of_delivery import ProofOfDelivery, ProofOfDeliveryDict
from .tracking_summary import TrackingSummary, TrackingSummaryDict


class Payload31(SdkBaseModel):
    tracking_id: Optional[str] = Field(default=UNSET, alias="trackingId")
    alternate_leg_tracking_id: Optional[str] = Field(default=UNSET, alias="alternateLegTrackingId")
    event_history: Optional[list[Event]] = Field(default=UNSET, alias="eventHistory")
    promised_delivery_date: Optional[RFC3339DateTime] = Field(default=UNSET, alias="promisedDeliveryDate")
    summary: Optional[TrackingSummary] = UNSET
    proof_of_delivery: Optional[ProofOfDelivery] = Field(default=UNSET, alias="proofOfDelivery")


class Payload31Dict(TypedDict):
    tracking_id: NotRequired[str]
    alternate_leg_tracking_id: NotRequired[str]
    event_history: NotRequired[list[EventDict]]
    promised_delivery_date: NotRequired[RFC3339DateTime]
    summary: NotRequired[TrackingSummaryDict]
    proof_of_delivery: NotRequired[ProofOfDeliveryDict]
