from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.label_format import LabelFormatOrStr
from .enums.standard_id_for_label import StandardIdForLabelOrStr
from .file_contents import FileContents, FileContentsDict
from .label_dimensions import LabelDimensions, LabelDimensionsDict


class Label(SdkBaseModel):
    custom_text_for_label: Optional[str] = Field(default=UNSET, alias="customTextForLabel")
    dimensions: Optional[LabelDimensions] = UNSET
    file_contents: Optional[FileContents] = Field(default=UNSET, alias="fileContents")
    label_format: Optional[LabelFormatOrStr] = Field(default=UNSET, alias="labelFormat")
    standard_id_for_label: Optional[StandardIdForLabelOrStr] = Field(default=UNSET, alias="standardIdForLabel")


class LabelDict(TypedDict):
    custom_text_for_label: NotRequired[str]
    dimensions: NotRequired[LabelDimensionsDict]
    file_contents: NotRequired[FileContentsDict]
    label_format: NotRequired[LabelFormatOrStr]
    standard_id_for_label: NotRequired[StandardIdForLabelOrStr]
