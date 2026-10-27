from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.identifier_type import IdentifierTypeOrStr


class ItemIdentifier(SdkBaseModel):
    identifier_type: Optional[IdentifierTypeOrStr] = Field(default=UNSET, alias="identifierType")
    identifier: Optional[str] = UNSET
    marketplace_id: Optional[str] = Field(default=UNSET, alias="marketplaceId")


class ItemIdentifierDict(TypedDict):
    identifier_type: NotRequired[IdentifierTypeOrStr]
    identifier: NotRequired[str]
    marketplace_id: NotRequired[str]
