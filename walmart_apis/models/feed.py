from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.processing_status1 import ProcessingStatus1OrStr
from .feed_processing_summary import FeedProcessingSummary, FeedProcessingSummaryDict


class Feed(SdkBaseModel):
    feed_id: str = Field(alias="feedId")
    """Unique identifier for this feed"""

    feed_type: str = Field(alias="feedType")
    """The type of feed submitted (e.g. LISTINGS_FEED, INVENTORY_FEED)"""

    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")
    """Marketplace the feed was submitted to (e.g. WALMART_US)"""

    created_at: RFC3339DateTime = Field(alias="createdAt")
    """Timestamp when the feed was received by the server"""

    processing_started_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="processingStartedAt")
    """Timestamp when feed processing began; absent until processing starts"""

    processing_completed_at: Optional[RFC3339DateTime] = Field(default=UNSET, alias="processingCompletedAt")
    """Timestamp when feed processing finished; absent until complete"""

    processing_status: ProcessingStatus1OrStr = Field(alias="processingStatus")
    """Current processing status of the feed"""

    result_feed_document_id: Optional[str] = Field(default=UNSET, alias="resultFeedDocumentId")
    """ID of the result document; present only when processingStatus is DONE. Use with GET
    /feeds/v4/feeds/{feedId}/document."""

    feed_processing_summary: Optional[FeedProcessingSummary] = Field(default=UNSET, alias="feedProcessingSummary")
    """Record-level processing counts; present only when processingStatus is DONE"""


class FeedDict(TypedDict):
    feed_id: str
    feed_type: str
    marketplace_id: NotRequired[str]
    created_at: RFC3339DateTime
    processing_started_at: NotRequired[RFC3339DateTime]
    processing_completed_at: NotRequired[RFC3339DateTime]
    processing_status: ProcessingStatus1OrStr
    result_feed_document_id: NotRequired[str]
    feed_processing_summary: NotRequired[FeedProcessingSummaryDict]
