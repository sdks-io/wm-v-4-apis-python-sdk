from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.authorize_error import AuthorizeError
from ..models.oauth_error_model import OauthErrorModel

AuthorizeErrorBody: TypeAlias = AuthorizeError | OauthErrorModel | RawError


@dataclass(frozen=True, slots=True)
class _AuthorizeError:
    def map(self, status_code: int, content: bytes) -> AuthorizeErrorBody:
        match status_code:
            case 400:
                return decode_json[AuthorizeError](content)
            case 429 | 500:
                return decode_json[OauthErrorModel](content)
            case _:
                return RawError(status_code, content)


authorize_error_mapper: Final[ErrorMapper[AuthorizeErrorBody]] = _AuthorizeError()
