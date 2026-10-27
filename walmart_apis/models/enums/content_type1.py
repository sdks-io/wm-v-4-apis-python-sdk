from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ContentType1(str, Enum):
    TEXT_XML_CHARSET_UTF_8 = "text/xml; charset=UTF-8"
    TEXT_TAB_SEPARATED_VALUES_CHARSET_UTF_8 = "text/tab-separated-values; charset=UTF-8"
    APPLICATION_JSON_CHARSET_UTF_8 = "application/json; charset=UTF-8"
    APPLICATION_OCTET_STREAM = "application/octet-stream"

    __str__ = str.__str__


ContentType1OrStr: TypeAlias = Annotated[ContentType1 | str, open_enum_validator(ContentType1)]
