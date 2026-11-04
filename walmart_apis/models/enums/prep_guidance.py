from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class PrepGuidance(str, Enum):
    """High-level guidance on whether/how an item needs to be prepped."""

    CONSULT_HELP_DOCUMENTS = "ConsultHelpDocuments"
    NO_ADDITIONAL_PREP_REQUIRED = "NoAdditionalPrepRequired"
    SEE_PREP_INSTRUCTIONS_LIST = "SeePrepInstructionsList"

    __str__ = str.__str__


PrepGuidanceOrStr: TypeAlias = Annotated[PrepGuidance | str, open_enum_validator(PrepGuidance)]
