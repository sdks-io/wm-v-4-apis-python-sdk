from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class AddressOrders(SdkBaseModel):
    """Postal address associated with the order."""

    name: Optional[str] = UNSET
    """Recipient name for the shipping address."""

    address_line1: Optional[str] = Field(default=UNSET, alias="addressLine1")
    """First line of the shipping address."""

    address_line2: Optional[str] = Field(default=UNSET, alias="addressLine2")
    """Second line of the shipping address, when provided."""

    city: Optional[str] = UNSET
    """City of the shipping address."""

    state: Optional[str] = UNSET
    """State or region of the shipping address."""

    postal_code: Optional[str] = Field(default=UNSET, alias="postalCode")
    """Postal code of the shipping address."""

    country: str = "US"
    """Country of the shipping address."""


class AddressOrdersDict(TypedDict):
    name: NotRequired[str]
    address_line1: NotRequired[str]
    address_line2: NotRequired[str]
    city: NotRequired[str]
    state: NotRequired[str]
    postal_code: NotRequired[str]
    country: NotRequired[str]
