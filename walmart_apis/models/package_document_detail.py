from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .package_document import PackageDocument, PackageDocumentDict


class PackageDocumentDetail(SdkBaseModel):
    package_client_reference_id: str = Field(alias="packageClientReferenceId")
    package_documents: list[PackageDocument] = Field(alias="packageDocuments")
    tracking_id: Optional[str] = Field(default=UNSET, alias="trackingId")


class PackageDocumentDetailDict(TypedDict):
    package_client_reference_id: str
    package_documents: list[PackageDocumentDict]
    tracking_id: NotRequired[str]
