from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CommonError(SdkBaseModel):
    """Error information returned when the request is unsuccessful."""

    code: str
    """Machine-readable error code that identifies the type of error that occurred."""

    message: str
    """Human-readable message that describes the error condition."""

    details: Optional[str] = UNSET
    """Additional context or field-level detail to help the caller understand or resolve the error."""

    pointer: Optional[str] = UNSET
    """RFC 6901 JSON Pointer, as a URI fragment, to the request-body member this error is about (e.g.
    ``#/orderLines/0/quantity``). Present only for request-body validation errors, as in RFC 9457 section 3."""


class CommonErrorDict(TypedDict):
    code: str
    message: str
    details: NotRequired[str]
    pointer: NotRequired[str]
