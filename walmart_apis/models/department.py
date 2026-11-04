from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class Department(SdkBaseModel):
    """Department identifier and display name."""

    department_id: Optional[str] = Field(default=UNSET, alias="departmentId")
    """Identifier of the department."""

    display_name: Optional[str] = Field(default=UNSET, alias="displayName")
    """Display name of the department."""


class DepartmentDict(TypedDict):
    department_id: NotRequired[str]
    display_name: NotRequired[str]
