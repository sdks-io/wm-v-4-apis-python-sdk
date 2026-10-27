from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .package_document_detail import PackageDocumentDetail, PackageDocumentDetailDict
from .promise import Promise, PromiseDict


class Payload12(SdkBaseModel):
    shipment_id: Optional[str] = Field(default=UNSET, alias="shipmentId")
    package_document_details: Optional[list[PackageDocumentDetail]] = Field(
        default=UNSET, alias="packageDocumentDetails"
    )
    promise: Optional[Promise] = UNSET


class Payload12Dict(TypedDict):
    shipment_id: NotRequired[str]
    package_document_details: NotRequired[list[PackageDocumentDetailDict]]
    promise: NotRequired[PromiseDict]
