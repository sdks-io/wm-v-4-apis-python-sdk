from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class SellerFeedbackType(SdkBaseModel):
    """Seller feedback information, including the percentage of positive feedback and total number of ratings."""

    seller_positive_feedback_rating: Optional[float] = Field(default=UNSET, alias="SellerPositiveFeedbackRating")
    """Percentage of positive feedback for the seller during the past 365 days."""

    feedback_count: int = Field(alias="FeedbackCount")
    """Number of ratings received for the seller."""


class SellerFeedbackTypeDict(TypedDict):
    seller_positive_feedback_rating: NotRequired[float]
    feedback_count: int
