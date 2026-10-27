from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonContactInformation(SdkBaseModel):
    """The seller's contact information."""

    email: Optional[str] = UNSET
    """The email address."""

    name: str
    """The contact's name."""

    phone_number: str = Field(alias="phoneNumber")
    """The phone number."""


class CommonContactInformationDict(TypedDict):
    email: NotRequired[str]
    name: str
    phone_number: str
