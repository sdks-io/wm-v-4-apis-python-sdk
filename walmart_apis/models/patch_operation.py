from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.op import OpOrStr


class PatchOperation(SdkBaseModel):
    op: OpOrStr
    """Patch operation type (JSON Patch)"""

    path: str
    """JSON Pointer path to the attribute (RFC 6901)"""

    value: Optional[list[Any]] = UNSET
    """Value to set (absent for delete operations)"""


class PatchOperationDict(TypedDict):
    op: OpOrStr
    path: str
    value: NotRequired[list[Any]]
