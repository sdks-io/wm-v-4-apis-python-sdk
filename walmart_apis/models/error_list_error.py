from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_error import CommonError, CommonErrorDict


class ErrorListError(SdkBaseModel):
    """RFC 9457 problem details object returned by a failed request. Carries the RFC 9457 standard members plus an
    ``errors`` extension member listing each individual error. Clients must ignore members they don't recognise (RFC
    9457 section 3.2)."""

    type_: Optional[str] = Field(default=UNSET, alias="type")
    """URI reference identifying the problem type (RFC 9457 section 3.1.1). ``about:blank`` means the problem has no
    semantics beyond its HTTP status code."""

    title: Optional[str] = UNSET
    """Short, human-readable summary of the problem type (RFC 9457 section 3.1.3). For ``about:blank`` this is the HTTP
    status phrase."""

    status: Optional[int] = UNSET
    """HTTP status code for this occurrence; always equal to the response status (RFC 9457 section 3.1.2)."""

    detail: Optional[str] = UNSET
    """Human-readable explanation specific to this occurrence (RFC 9457 section 3.1.4). Use the ``errors`` member, not
    this text, to decide what to do programmatically."""

    instance: Optional[str] = UNSET
    """URI reference identifying this occurrence of the problem (RFC 9457 section 3.1.5), typically the request path."""

    errors: list[CommonError]
    """Extension member (RFC 9457 section 3.2): the list of errors that caused the request to fail."""


class ErrorListErrorDict(TypedDict):
    type_: NotRequired[str]
    title: NotRequired[str]
    status: NotRequired[int]
    detail: NotRequired[str]
    instance: NotRequired[str]
    errors: list[CommonErrorDict]
