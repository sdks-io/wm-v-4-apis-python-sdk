from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class LocaleCode(str, Enum):
    """The locale code constructed from an ISO 639 language code and an ISO 3166-1 alpha-2 country code separated by an
    underscore. Optional; defaults to ``en_US``."""

    EN_US = "en_US"
    ES_MX = "es_MX"
    ES_CL = "es_CL"
    EN_CA = "en_CA"

    __str__ = str.__str__


LocaleCodeOrStr: TypeAlias = Annotated[LocaleCode | str, open_enum_validator(LocaleCode)]
