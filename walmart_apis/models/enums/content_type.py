from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentType(str, Enum):
    """MIME type of the uploaded feed content. If omitted, the server infers from the file's Content-Type in the
    multipart header."""

    TEXT_XML_CHARSET_UTF_8 = "text/xml; charset=UTF-8"
    TEXT_TAB_SEPARATED_VALUES_CHARSET_UTF_8 = "text/tab-separated-values; charset=UTF-8"
    APPLICATION_JSON_CHARSET_UTF_8 = "application/json; charset=UTF-8"

    __str__ = str.__str__


ContentTypeOrStr: TypeAlias = Annotated[ContentType | str, open_enum_validator(ContentType)]
