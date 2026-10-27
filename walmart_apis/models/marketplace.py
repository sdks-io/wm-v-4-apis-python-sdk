from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Marketplace(SdkBaseModel):
    id: Optional[str] = UNSET
    """Marketplace tenant token (see docs/marketplace-ids.md)."""

    name: Optional[str] = UNSET
    country_code: Optional[str] = Field(default=UNSET, alias="countryCode")
    currency_code: Optional[str] = Field(default=UNSET, alias="currencyCode")
    default_language_code: Optional[str] = Field(default=UNSET, alias="defaultLanguageCode")


class MarketplaceDict(TypedDict):
    id: NotRequired[str]
    name: NotRequired[str]
    country_code: NotRequired[str]
    currency_code: NotRequired[str]
    default_language_code: NotRequired[str]
