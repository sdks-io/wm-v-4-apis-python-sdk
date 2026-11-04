from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.o_auth_error_model import OAuthErrorModel

CreateTokenErrorBody: TypeAlias = OAuthErrorModel | RawError


@dataclass(frozen=True, slots=True)
class _CreateTokenError:
    def map(self, status_code: int, content: bytes) -> CreateTokenErrorBody:
        match status_code:
            case 400 | 401 | 429 | 500 | 502:
                return decode_json[OAuthErrorModel](content)
            case _:
                return RawError(status_code, content)


create_token_error_mapper: Final[ErrorMapper[CreateTokenErrorBody]] = _CreateTokenError()
