from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.file_type import FileTypeOrStr


class FileContents(SdkBaseModel):
    contents: Optional[str] = UNSET
    """Base64-encoded label file"""

    file_type: Optional[FileTypeOrStr] = Field(default=UNSET, alias="fileType")
    checksum: Optional[str] = UNSET


class FileContentsDict(TypedDict):
    contents: NotRequired[str]
    file_type: NotRequired[FileTypeOrStr]
    checksum: NotRequired[str]
