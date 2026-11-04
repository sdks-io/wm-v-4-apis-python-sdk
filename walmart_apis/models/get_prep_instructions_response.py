from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .get_prep_instructions_payload import GetPrepInstructionsPayload, GetPrepInstructionsPayloadDict
from .prep_instructions_error import PrepInstructionsError, PrepInstructionsErrorDict


class GetPrepInstructionsResponse(SdkBaseModel):
    """The ``getPrepInstructions`` response."""

    payload: Optional[GetPrepInstructionsPayload] = UNSET
    """The payload of the ``getPrepInstructions`` response."""

    errors: Optional[list[PrepInstructionsError]] = UNSET
    """A list of errors encountered while processing the request."""


class GetPrepInstructionsResponseDict(TypedDict):
    payload: NotRequired[GetPrepInstructionsPayloadDict]
    errors: NotRequired[list[PrepInstructionsErrorDict]]
