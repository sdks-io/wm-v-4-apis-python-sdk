from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dpi import DpiOrInt
from .enums.format1 import Format1OrStr
from .enums.page_layout import PageLayoutOrStr
from .label_dimensions import LabelDimensions, LabelDimensionsDict


class RequestedDocumentSpecification(SdkBaseModel):
    format: Format1OrStr
    size: LabelDimensions
    dpi: DpiOrInt
    page_layout: Optional[PageLayoutOrStr] = Field(default=UNSET, alias="pageLayout")
    need_file_joining: Optional[bool] = Field(default=UNSET, alias="needFileJoining")
    print_options: Optional[list[Any]] = Field(default=UNSET, alias="printOptions")
    """Optional list of additional print specs (customs forms, invoice attachments, etc). Compressed; see TODO."""


class RequestedDocumentSpecificationDict(TypedDict):
    format: Format1OrStr
    size: LabelDimensionsDict
    dpi: DpiOrInt
    page_layout: NotRequired[PageLayoutOrStr]
    need_file_joining: NotRequired[bool]
    print_options: NotRequired[list[Any]]
