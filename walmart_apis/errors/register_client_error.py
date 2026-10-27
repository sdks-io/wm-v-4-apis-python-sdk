from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.oauth_error_model import OauthErrorModel
from ..models.registration_error import RegistrationError

RegisterClientErrorBody: TypeAlias = RegistrationError | OauthErrorModel | RawError


@dataclass(frozen=True, slots=True)
class _RegisterClientError:
    def map(self, status_code: int, content: bytes) -> RegisterClientErrorBody:
        match status_code:
            case 400 | 401:
                return decode_json[RegistrationError](content)
            case 429 | 500:
                return decode_json[OauthErrorModel](content)
            case _:
                return RawError(status_code, content)


register_client_error_mapper: Final[ErrorMapper[RegisterClientErrorBody]] = _RegisterClientError()
