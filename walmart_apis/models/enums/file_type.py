from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class FileType(str, Enum):
    APPLICATION_PDF = "application/pdf"
    APPLICATION_ZPL = "application/zpl"
    IMAGE_PNG = "image/png"

    __str__ = str.__str__


FileTypeOrStr: TypeAlias = Annotated[FileType | str, open_enum_validator(FileType)]
