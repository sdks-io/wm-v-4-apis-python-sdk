from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellerFeedbackType(SdkBaseModel):
    """Information about the seller's feedback, including the percentage of positive feedback and total ratings."""

    seller_positive_feedback_rating: Optional[float] = Field(default=UNSET, alias="SellerPositiveFeedbackRating")
    """The percentage of positive feedback for the seller in the past 365 days."""

    feedback_count: int = Field(alias="FeedbackCount")
    """The number of ratings received about the seller."""


class SellerFeedbackTypeDict(TypedDict):
    seller_positive_feedback_rating: NotRequired[float]
    feedback_count: int
