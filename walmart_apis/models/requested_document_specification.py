from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.dpi import DpiOrInt
from .enums.format_shipping import FormatShippingOrStr
from .enums.page_layout import PageLayoutOrStr
from .size import Size, SizeDict


class RequestedDocumentSpecification(SdkBaseModel):
    format: FormatShippingOrStr
    size: Size
    dpi: DpiOrInt
    page_layout: Optional[PageLayoutOrStr] = Field(default=UNSET, alias="pageLayout")
    need_file_joining: Optional[bool] = Field(default=UNSET, alias="needFileJoining")
    print_options: Optional[list[Any]] = Field(default=UNSET, alias="printOptions")
    """Optional list of additional print specs (customs forms, invoice attachments, etc). Compressed shape; full
    fidelity tracked in a follow-up PR."""


class RequestedDocumentSpecificationDict(TypedDict):
    format: FormatShippingOrStr
    size: SizeDict
    dpi: DpiOrInt
    page_layout: NotRequired[PageLayoutOrStr]
    need_file_joining: NotRequired[bool]
    print_options: NotRequired[list[Any]]
