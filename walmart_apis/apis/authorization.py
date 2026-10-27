from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    form_body,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.authorize_error import AuthorizeErrorBody, authorize_error_mapper
from ..errors.create_token_error import CreateTokenErrorBody, create_token_error_mapper
from ..errors.register_client_error import RegisterClientErrorBody, register_client_error_mapper
from ..models.client_registration_request import ClientRegistrationRequest, ClientRegistrationRequestDict
from ..models.client_registration_response import ClientRegistrationResponse
from ..models.enums.code_challenge_method import CodeChallengeMethodOrStr
from ..models.enums.grant_type import GrantTypeOrStr
from ..models.enums.response_type1 import ResponseType1OrStr
from ..models.token_response import TokenResponse
from ..server.server import Server


class Authorization:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthorizationWithRawResponse(client, server, auth)

    def authorize(
        self,
        response_type: ResponseType1OrStr,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: CodeChallengeMethodOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Browser endpoint for the authorization-code grant (RFC 6749 §3.1). The Solution Provider redirects the seller
        here; the seller authenticates and consents at Walmart IAM, and the response redirects to ``redirect_uri`` with
        a single-use ``code``.

        - **PKCE required** — ``code_challenge`` + ``code_challenge_method=S256``
          (RFC 7636). ``plain`` is not accepted.
        - **Exact** ``redirect_uri`` match against a value registered for the client.
        - ``state`` required; echoed back verbatim (CSRF).
        - The success and error redirects (performed by IAM) carry ``iss`` (RFC 9207);
          clients MUST validate it.

        **Error handling.** For a valid request, this endpoint ``302``-redirects to the Walmart IAM consent URL; IAM
        then drives consent and performs the RFC 6749 §4.1.2.1 redirect back to the client's ``redirect_uri`` (success
        or error), because IAM is the party that can verify the ``redirect_uri`` is registered. For request-level errors
        that ``the Authorization API`` itself detects (missing/invalid ``client_id``/``redirect_uri``, ``response_type``
        != ``code``, ``code_challenge_method`` != ``S256``), it returns a JSON ``400`` (``AuthorizeError``). It
        deliberately does **not** redirect these errors to the supplied ``redirect_uri``: the proxy has no client
        registry, so self-redirecting to an unverified URI would be an open redirect.

        > **Upstream status (, pending):** ``iss`` emission, exact-redirect
        > enforcement, and server-side rejection of ``code_challenge_method=plain`` are
        > IAM / app-store responsibilities not yet fully in place. the Authorization API
        > enforces the request-side invariants it can and redirects valid requests to
        > IAM; the full guarantee lands when those upstream changes ship.

        Args:
            response_type: Must be ``code``.
            client_id: The registered client identifier.
            redirect_uri: Callback URI; must exactly match a registered value.
            scope: Space-delimited scopes. Include ``offline_access`` to receive a refresh token.
            state: Opaque CSRF token; echoed back unchanged.
            code_challenge: PKCE challenge — base64url(SHA-256(code_verifier)).
            code_challenge_method: Must be ``S256``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Raises:
            ApiError: Non-redirectable request (bad ``client_id``/``redirect_uri``). Rate limit exceeded. Internal
                error. ``error`` is ``AuthorizeError | OauthErrorModel | RawError``."""
        return unwrap(
            self._with_raw_response.authorize(
                response_type,
                client_id,
                redirect_uri,
                scope,
                state,
                code_challenge,
                code_challenge_method,
                request_options=request_options,
            ),
        )

    def create_token(
        self,
        grant_type: GrantTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        code_verifier: str | None = None,
        refresh_token: str | None = None,
        redirect_uri: str | None = None,
        scope: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenResponse:
        """Exchanges a grant for an OAuth access token. Supported ``grant_type`` values:

        | grant_type | Flow | Required (besides grant_type) |
        |----------------------|------------------|---------------------------------|
        | ``client_credentials`` | seller-direct | client auth (see below) |
        | ``authorization_code`` | delegated | ``code``, ``code_verifier`` (PKCE) |
        | ``refresh_token`` | delegated | ``refresh_token`` |

        **Client authentication:** credentials in the form body (``client_secret_post``) — ``client_id`` +
        ``client_secret``. HTTP Basic is also accepted. **Public clients** (Solution-Provider apps registered
        ``token_endpoint_auth_method: none``) send no secret on the delegated grants; PKCE protects the code.

        **``client_credentials``:** issues **no** refresh token (re-mint on expiry). **``scope`` is decorative here** —
        accepted for compatibility but **not honored**; access is governed by the scopes provisioned per client in IAM ;
        there is no down-scoping and the response does not echo ``scope``. (Verified: ``/v3/token`` ignores any
        ``scope=`` value.)

        **``authorization_code``:** ``redirect_uri`` is accepted for OAuth 2.0 back-compat but not required in 2.1 (PKCE
        covers injection).

        **``refresh_token``:** the response includes a **rotated** ``refresh_token`` — the presented token is
        invalidated (OAuth 2.1 §4.3.1; IAM rotates today, ~1-year TTL). A requested ``scope`` MUST NOT exceed the
        originally granted scope.

        **Token:** ``Bearer`` (RFC 6750), sent downstream as `Authorization: Bearer <token>`` — **not**
        ``WM_SEC.ACCESS_TOKEN`.

        **Implemented by ``the Authorization API`` as a stateless proxy to Walmart IAM .**

        Args:
            grant_type: The OAuth grant type.
            client_id: Client identifier (client_secret_post / public clients). Omit if using HTTP Basic.
            client_secret: Client secret (client_secret_post). Omit for public clients or HTTP Basic.
            code: Authorization code from ``/auth/v4/authorize`` (authorization_code grant).
            code_verifier: PKCE verifier whose S256 hash equals the earlier ``code_challenge`` (authorization_code
                grant).
            refresh_token: A previously issued refresh token (refresh_token grant). Rotated on use.
            redirect_uri: Accepted for OAuth 2.0 back-compat on authorization_code; not required in 2.1 (PKCE covers
                injection).
            scope: **client_credentials:** accepted for compatibility but **not honored** — no down-scoping; not echoed.
                **refresh_token:** optional; MUST NOT exceed the originally granted scope.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Access token issued.

        Raises:
            ApiError: Invalid token request (RFC 6749 §5.2). Client authentication failed — ``invalid_client``. Rate
                limit exceeded. Internal error. ``error`` is ``OauthErrorModel | RawError``."""
        return unwrap(
            self._with_raw_response.create_token(
                grant_type,
                client_id=client_id,
                client_secret=client_secret,
                code=code,
                code_verifier=code_verifier,
                refresh_token=refresh_token,
                redirect_uri=redirect_uri,
                scope=scope,
                request_options=request_options,
            ),
        )

    def register_client(
        self,
        body: ClientRegistrationRequest | ClientRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ClientRegistrationResponse:
        """Registers a Solution Provider client and returns its ``client_id`` (RFC 7591). Lets Solution Providers
        onboard without manual registration.

        Public clients set ``token_endpoint_auth_method: none`` (no secret; PKCE required). Confidential clients receive
        a ``client_secret``. ``redirect_uris`` are validated and later enforced by exact match at
        ``/auth/v4/authorize``.

        Proxied to Walmart IAM's registration endpoint (/). RFC 7592 registration management (read/update/delete via a
        ``registration_access_token``) is not offered in this version.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Client registered.

        Raises:
            ApiError: Invalid client metadata (RFC 7591 §3.2.2). Registration requires an initial access token and
                none/invalid was supplied. Rate limit exceeded. Internal error. ``error`` is ``RegistrationError |
                OauthErrorModel | RawError``."""
        return unwrap(self._with_raw_response.register_client(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AuthorizationWithRawResponse:
        return self._with_raw_response


class AsyncAuthorization:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthorizationWithRawResponse(client, server, auth)

    async def authorize(
        self,
        response_type: ResponseType1OrStr,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: CodeChallengeMethodOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Browser endpoint for the authorization-code grant (RFC 6749 §3.1). The Solution Provider redirects the seller
        here; the seller authenticates and consents at Walmart IAM, and the response redirects to ``redirect_uri`` with
        a single-use ``code``.

        - **PKCE required** — ``code_challenge`` + ``code_challenge_method=S256``
          (RFC 7636). ``plain`` is not accepted.
        - **Exact** ``redirect_uri`` match against a value registered for the client.
        - ``state`` required; echoed back verbatim (CSRF).
        - The success and error redirects (performed by IAM) carry ``iss`` (RFC 9207);
          clients MUST validate it.

        **Error handling.** For a valid request, this endpoint ``302``-redirects to the Walmart IAM consent URL; IAM
        then drives consent and performs the RFC 6749 §4.1.2.1 redirect back to the client's ``redirect_uri`` (success
        or error), because IAM is the party that can verify the ``redirect_uri`` is registered. For request-level errors
        that ``the Authorization API`` itself detects (missing/invalid ``client_id``/``redirect_uri``, ``response_type``
        != ``code``, ``code_challenge_method`` != ``S256``), it returns a JSON ``400`` (``AuthorizeError``). It
        deliberately does **not** redirect these errors to the supplied ``redirect_uri``: the proxy has no client
        registry, so self-redirecting to an unverified URI would be an open redirect.

        > **Upstream status (, pending):** ``iss`` emission, exact-redirect
        > enforcement, and server-side rejection of ``code_challenge_method=plain`` are
        > IAM / app-store responsibilities not yet fully in place. the Authorization API
        > enforces the request-side invariants it can and redirects valid requests to
        > IAM; the full guarantee lands when those upstream changes ship.

        Args:
            response_type: Must be ``code``.
            client_id: The registered client identifier.
            redirect_uri: Callback URI; must exactly match a registered value.
            scope: Space-delimited scopes. Include ``offline_access`` to receive a refresh token.
            state: Opaque CSRF token; echoed back unchanged.
            code_challenge: PKCE challenge — base64url(SHA-256(code_verifier)).
            code_challenge_method: Must be ``S256``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Raises:
            ApiError: Non-redirectable request (bad ``client_id``/``redirect_uri``). Rate limit exceeded. Internal
                error. ``error`` is ``AuthorizeError | OauthErrorModel | RawError``."""
        return unwrap(
            await self._with_raw_response.authorize(
                response_type,
                client_id,
                redirect_uri,
                scope,
                state,
                code_challenge,
                code_challenge_method,
                request_options=request_options,
            ),
        )

    async def create_token(
        self,
        grant_type: GrantTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        code_verifier: str | None = None,
        refresh_token: str | None = None,
        redirect_uri: str | None = None,
        scope: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenResponse:
        """Exchanges a grant for an OAuth access token. Supported ``grant_type`` values:

        | grant_type | Flow | Required (besides grant_type) |
        |----------------------|------------------|---------------------------------|
        | ``client_credentials`` | seller-direct | client auth (see below) |
        | ``authorization_code`` | delegated | ``code``, ``code_verifier`` (PKCE) |
        | ``refresh_token`` | delegated | ``refresh_token`` |

        **Client authentication:** credentials in the form body (``client_secret_post``) — ``client_id`` +
        ``client_secret``. HTTP Basic is also accepted. **Public clients** (Solution-Provider apps registered
        ``token_endpoint_auth_method: none``) send no secret on the delegated grants; PKCE protects the code.

        **``client_credentials``:** issues **no** refresh token (re-mint on expiry). **``scope`` is decorative here** —
        accepted for compatibility but **not honored**; access is governed by the scopes provisioned per client in IAM ;
        there is no down-scoping and the response does not echo ``scope``. (Verified: ``/v3/token`` ignores any
        ``scope=`` value.)

        **``authorization_code``:** ``redirect_uri`` is accepted for OAuth 2.0 back-compat but not required in 2.1 (PKCE
        covers injection).

        **``refresh_token``:** the response includes a **rotated** ``refresh_token`` — the presented token is
        invalidated (OAuth 2.1 §4.3.1; IAM rotates today, ~1-year TTL). A requested ``scope`` MUST NOT exceed the
        originally granted scope.

        **Token:** ``Bearer`` (RFC 6750), sent downstream as `Authorization: Bearer <token>`` — **not**
        ``WM_SEC.ACCESS_TOKEN`.

        **Implemented by ``the Authorization API`` as a stateless proxy to Walmart IAM .**

        Args:
            grant_type: The OAuth grant type.
            client_id: Client identifier (client_secret_post / public clients). Omit if using HTTP Basic.
            client_secret: Client secret (client_secret_post). Omit for public clients or HTTP Basic.
            code: Authorization code from ``/auth/v4/authorize`` (authorization_code grant).
            code_verifier: PKCE verifier whose S256 hash equals the earlier ``code_challenge`` (authorization_code
                grant).
            refresh_token: A previously issued refresh token (refresh_token grant). Rotated on use.
            redirect_uri: Accepted for OAuth 2.0 back-compat on authorization_code; not required in 2.1 (PKCE covers
                injection).
            scope: **client_credentials:** accepted for compatibility but **not honored** — no down-scoping; not echoed.
                **refresh_token:** optional; MUST NOT exceed the originally granted scope.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Access token issued.

        Raises:
            ApiError: Invalid token request (RFC 6749 §5.2). Client authentication failed — ``invalid_client``. Rate
                limit exceeded. Internal error. ``error`` is ``OauthErrorModel | RawError``."""
        return unwrap(
            await self._with_raw_response.create_token(
                grant_type,
                client_id=client_id,
                client_secret=client_secret,
                code=code,
                code_verifier=code_verifier,
                refresh_token=refresh_token,
                redirect_uri=redirect_uri,
                scope=scope,
                request_options=request_options,
            ),
        )

    async def register_client(
        self,
        body: ClientRegistrationRequest | ClientRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ClientRegistrationResponse:
        """Registers a Solution Provider client and returns its ``client_id`` (RFC 7591). Lets Solution Providers
        onboard without manual registration.

        Public clients set ``token_endpoint_auth_method: none`` (no secret; PKCE required). Confidential clients receive
        a ``client_secret``. ``redirect_uris`` are validated and later enforced by exact match at
        ``/auth/v4/authorize``.

        Proxied to Walmart IAM's registration endpoint (/). RFC 7592 registration management (read/update/delete via a
        ``registration_access_token``) is not offered in this version.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Client registered.

        Raises:
            ApiError: Invalid client metadata (RFC 7591 §3.2.2). Registration requires an initial access token and
                none/invalid was supplied. Rate limit exceeded. Internal error. ``error`` is ``RegistrationError |
                OauthErrorModel | RawError``."""
        return unwrap(await self._with_raw_response.register_client(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncAuthorizationWithRawResponse:
        return self._with_raw_response


class AuthorizationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def authorize(
        self,
        response_type: ResponseType1OrStr,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: CodeChallengeMethodOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AuthorizeErrorBody]:
        """Browser endpoint for the authorization-code grant (RFC 6749 §3.1). The Solution Provider redirects the seller
        here; the seller authenticates and consents at Walmart IAM, and the response redirects to ``redirect_uri`` with
        a single-use ``code``.

        - **PKCE required** — ``code_challenge`` + ``code_challenge_method=S256``
          (RFC 7636). ``plain`` is not accepted.
        - **Exact** ``redirect_uri`` match against a value registered for the client.
        - ``state`` required; echoed back verbatim (CSRF).
        - The success and error redirects (performed by IAM) carry ``iss`` (RFC 9207);
          clients MUST validate it.

        **Error handling.** For a valid request, this endpoint ``302``-redirects to the Walmart IAM consent URL; IAM
        then drives consent and performs the RFC 6749 §4.1.2.1 redirect back to the client's ``redirect_uri`` (success
        or error), because IAM is the party that can verify the ``redirect_uri`` is registered. For request-level errors
        that ``the Authorization API`` itself detects (missing/invalid ``client_id``/``redirect_uri``, ``response_type``
        != ``code``, ``code_challenge_method`` != ``S256``), it returns a JSON ``400`` (``AuthorizeError``). It
        deliberately does **not** redirect these errors to the supplied ``redirect_uri``: the proxy has no client
        registry, so self-redirecting to an unverified URI would be an open redirect.

        > **Upstream status (, pending):** ``iss`` emission, exact-redirect
        > enforcement, and server-side rejection of ``code_challenge_method=plain`` are
        > IAM / app-store responsibilities not yet fully in place. the Authorization API
        > enforces the request-side invariants it can and redirects valid requests to
        > IAM; the full guarantee lands when those upstream changes ship.

        Args:
            response_type: Must be ``code``.
            client_id: The registered client identifier.
            redirect_uri: Callback URI; must exactly match a registered value.
            scope: Space-delimited scopes. Include ``offline_access`` to receive a refresh token.
            state: Opaque CSRF token; echoed back unchanged.
            code_challenge: PKCE challenge — base64url(SHA-256(code_verifier)).
            code_challenge_method: Must be ``S256``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/auth/v4/authorize"),
            query_params=[
                param[ResponseType1OrStr]("response_type", response_type),
                param[str]("client_id", client_id),
                param[str]("redirect_uri", redirect_uri),
                param[str]("scope", scope),
                param[str]("state", state),
                param[str]("code_challenge", code_challenge),
                param[CodeChallengeMethodOrStr]("code_challenge_method", code_challenge_method),
            ],
            decoder=empty_response,
            error_mapper=authorize_error_mapper,
            request_options=request_options,
        )

    def create_token(
        self,
        grant_type: GrantTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        code_verifier: str | None = None,
        refresh_token: str | None = None,
        redirect_uri: str | None = None,
        scope: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenResponse, CreateTokenErrorBody]:
        """Exchanges a grant for an OAuth access token. Supported ``grant_type`` values:

        | grant_type | Flow | Required (besides grant_type) |
        |----------------------|------------------|---------------------------------|
        | ``client_credentials`` | seller-direct | client auth (see below) |
        | ``authorization_code`` | delegated | ``code``, ``code_verifier`` (PKCE) |
        | ``refresh_token`` | delegated | ``refresh_token`` |

        **Client authentication:** credentials in the form body (``client_secret_post``) — ``client_id`` +
        ``client_secret``. HTTP Basic is also accepted. **Public clients** (Solution-Provider apps registered
        ``token_endpoint_auth_method: none``) send no secret on the delegated grants; PKCE protects the code.

        **``client_credentials``:** issues **no** refresh token (re-mint on expiry). **``scope`` is decorative here** —
        accepted for compatibility but **not honored**; access is governed by the scopes provisioned per client in IAM ;
        there is no down-scoping and the response does not echo ``scope``. (Verified: ``/v3/token`` ignores any
        ``scope=`` value.)

        **``authorization_code``:** ``redirect_uri`` is accepted for OAuth 2.0 back-compat but not required in 2.1 (PKCE
        covers injection).

        **``refresh_token``:** the response includes a **rotated** ``refresh_token`` — the presented token is
        invalidated (OAuth 2.1 §4.3.1; IAM rotates today, ~1-year TTL). A requested ``scope`` MUST NOT exceed the
        originally granted scope.

        **Token:** ``Bearer`` (RFC 6750), sent downstream as `Authorization: Bearer <token>`` — **not**
        ``WM_SEC.ACCESS_TOKEN`.

        **Implemented by ``the Authorization API`` as a stateless proxy to Walmart IAM .**

        Args:
            grant_type: The OAuth grant type.
            client_id: Client identifier (client_secret_post / public clients). Omit if using HTTP Basic.
            client_secret: Client secret (client_secret_post). Omit for public clients or HTTP Basic.
            code: Authorization code from ``/auth/v4/authorize`` (authorization_code grant).
            code_verifier: PKCE verifier whose S256 hash equals the earlier ``code_challenge`` (authorization_code
                grant).
            refresh_token: A previously issued refresh token (refresh_token grant). Rotated on use.
            redirect_uri: Accepted for OAuth 2.0 back-compat on authorization_code; not required in 2.1 (PKCE covers
                injection).
            scope: **client_credentials:** accepted for compatibility but **not honored** — no down-scoping; not echoed.
                **refresh_token:** optional; MUST NOT exceed the originally granted scope.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/auth/v4/token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[GrantTypeOrStr]("grant_type", grant_type),
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
                param[str | None]("code", code),
                param[str | None]("code_verifier", code_verifier),
                param[str | None]("refresh_token", refresh_token),
                param[str | None]("redirect_uri", redirect_uri),
                param[str | None]("scope", scope),
            ),
            auth_scheme=self._auth.basic_client_auth,
            decoder=json_decoder[TokenResponse],
            error_mapper=create_token_error_mapper,
            request_options=request_options,
        )

    def register_client(
        self,
        body: ClientRegistrationRequest | ClientRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ClientRegistrationResponse, RegisterClientErrorBody]:
        """Registers a Solution Provider client and returns its ``client_id`` (RFC 7591). Lets Solution Providers
        onboard without manual registration.

        Public clients set ``token_endpoint_auth_method: none`` (no secret; PKCE required). Confidential clients receive
        a ``client_secret``. ``redirect_uris`` are validated and later enforced by exact match at
        ``/auth/v4/authorize``.

        Proxied to Walmart IAM's registration endpoint (/). RFC 7592 registration management (read/update/delete via a
        ``registration_access_token``) is not offered in this version.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/auth/v4/register"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClientRegistrationRequest | ClientRegistrationRequestDict](body),
            decoder=json_decoder[ClientRegistrationResponse],
            error_mapper=register_client_error_mapper,
            request_options=request_options,
        )


class AsyncAuthorizationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def authorize(
        self,
        response_type: ResponseType1OrStr,
        client_id: str,
        redirect_uri: str,
        scope: str,
        state: str,
        code_challenge: str,
        code_challenge_method: CodeChallengeMethodOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, AuthorizeErrorBody]:
        """Browser endpoint for the authorization-code grant (RFC 6749 §3.1). The Solution Provider redirects the seller
        here; the seller authenticates and consents at Walmart IAM, and the response redirects to ``redirect_uri`` with
        a single-use ``code``.

        - **PKCE required** — ``code_challenge`` + ``code_challenge_method=S256``
          (RFC 7636). ``plain`` is not accepted.
        - **Exact** ``redirect_uri`` match against a value registered for the client.
        - ``state`` required; echoed back verbatim (CSRF).
        - The success and error redirects (performed by IAM) carry ``iss`` (RFC 9207);
          clients MUST validate it.

        **Error handling.** For a valid request, this endpoint ``302``-redirects to the Walmart IAM consent URL; IAM
        then drives consent and performs the RFC 6749 §4.1.2.1 redirect back to the client's ``redirect_uri`` (success
        or error), because IAM is the party that can verify the ``redirect_uri`` is registered. For request-level errors
        that ``the Authorization API`` itself detects (missing/invalid ``client_id``/``redirect_uri``, ``response_type``
        != ``code``, ``code_challenge_method`` != ``S256``), it returns a JSON ``400`` (``AuthorizeError``). It
        deliberately does **not** redirect these errors to the supplied ``redirect_uri``: the proxy has no client
        registry, so self-redirecting to an unverified URI would be an open redirect.

        > **Upstream status (, pending):** ``iss`` emission, exact-redirect
        > enforcement, and server-side rejection of ``code_challenge_method=plain`` are
        > IAM / app-store responsibilities not yet fully in place. the Authorization API
        > enforces the request-side invariants it can and redirects valid requests to
        > IAM; the full guarantee lands when those upstream changes ship.

        Args:
            response_type: Must be ``code``.
            client_id: The registered client identifier.
            redirect_uri: Callback URI; must exactly match a registered value.
            scope: Space-delimited scopes. Include ``offline_access`` to receive a refresh token.
            state: Opaque CSRF token; echoed back unchanged.
            code_challenge: PKCE challenge — base64url(SHA-256(code_verifier)).
            code_challenge_method: Must be ``S256``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/auth/v4/authorize"),
            query_params=[
                param[ResponseType1OrStr]("response_type", response_type),
                param[str]("client_id", client_id),
                param[str]("redirect_uri", redirect_uri),
                param[str]("scope", scope),
                param[str]("state", state),
                param[str]("code_challenge", code_challenge),
                param[CodeChallengeMethodOrStr]("code_challenge_method", code_challenge_method),
            ],
            decoder=async_empty_response,
            error_mapper=authorize_error_mapper,
            request_options=request_options,
        )

    async def create_token(
        self,
        grant_type: GrantTypeOrStr,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        code_verifier: str | None = None,
        refresh_token: str | None = None,
        redirect_uri: str | None = None,
        scope: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenResponse, CreateTokenErrorBody]:
        """Exchanges a grant for an OAuth access token. Supported ``grant_type`` values:

        | grant_type | Flow | Required (besides grant_type) |
        |----------------------|------------------|---------------------------------|
        | ``client_credentials`` | seller-direct | client auth (see below) |
        | ``authorization_code`` | delegated | ``code``, ``code_verifier`` (PKCE) |
        | ``refresh_token`` | delegated | ``refresh_token`` |

        **Client authentication:** credentials in the form body (``client_secret_post``) — ``client_id`` +
        ``client_secret``. HTTP Basic is also accepted. **Public clients** (Solution-Provider apps registered
        ``token_endpoint_auth_method: none``) send no secret on the delegated grants; PKCE protects the code.

        **``client_credentials``:** issues **no** refresh token (re-mint on expiry). **``scope`` is decorative here** —
        accepted for compatibility but **not honored**; access is governed by the scopes provisioned per client in IAM ;
        there is no down-scoping and the response does not echo ``scope``. (Verified: ``/v3/token`` ignores any
        ``scope=`` value.)

        **``authorization_code``:** ``redirect_uri`` is accepted for OAuth 2.0 back-compat but not required in 2.1 (PKCE
        covers injection).

        **``refresh_token``:** the response includes a **rotated** ``refresh_token`` — the presented token is
        invalidated (OAuth 2.1 §4.3.1; IAM rotates today, ~1-year TTL). A requested ``scope`` MUST NOT exceed the
        originally granted scope.

        **Token:** ``Bearer`` (RFC 6750), sent downstream as `Authorization: Bearer <token>`` — **not**
        ``WM_SEC.ACCESS_TOKEN`.

        **Implemented by ``the Authorization API`` as a stateless proxy to Walmart IAM .**

        Args:
            grant_type: The OAuth grant type.
            client_id: Client identifier (client_secret_post / public clients). Omit if using HTTP Basic.
            client_secret: Client secret (client_secret_post). Omit for public clients or HTTP Basic.
            code: Authorization code from ``/auth/v4/authorize`` (authorization_code grant).
            code_verifier: PKCE verifier whose S256 hash equals the earlier ``code_challenge`` (authorization_code
                grant).
            refresh_token: A previously issued refresh token (refresh_token grant). Rotated on use.
            redirect_uri: Accepted for OAuth 2.0 back-compat on authorization_code; not required in 2.1 (PKCE covers
                injection).
            scope: **client_credentials:** accepted for compatibility but **not honored** — no down-scoping; not echoed.
                **refresh_token:** optional; MUST NOT exceed the originally granted scope.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/auth/v4/token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=form_body(
                param[GrantTypeOrStr]("grant_type", grant_type),
                param[str | None]("client_id", client_id),
                param[str | None]("client_secret", client_secret),
                param[str | None]("code", code),
                param[str | None]("code_verifier", code_verifier),
                param[str | None]("refresh_token", refresh_token),
                param[str | None]("redirect_uri", redirect_uri),
                param[str | None]("scope", scope),
            ),
            auth_scheme=self._auth.basic_client_auth,
            decoder=async_json_decoder[TokenResponse],
            error_mapper=create_token_error_mapper,
            request_options=request_options,
        )

    async def register_client(
        self,
        body: ClientRegistrationRequest | ClientRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ClientRegistrationResponse, RegisterClientErrorBody]:
        """Registers a Solution Provider client and returns its ``client_id`` (RFC 7591). Lets Solution Providers
        onboard without manual registration.

        Public clients set ``token_endpoint_auth_method: none`` (no secret; PKCE required). Confidential clients receive
        a ``client_secret``. ``redirect_uris`` are validated and later enforced by exact match at
        ``/auth/v4/authorize``.

        Proxied to Walmart IAM's registration endpoint (/). RFC 7592 registration management (read/update/delete via a
        ``registration_access_token``) is not offered in this version.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/auth/v4/register"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClientRegistrationRequest | ClientRegistrationRequestDict](body),
            decoder=async_json_decoder[ClientRegistrationResponse],
            error_mapper=register_client_error_mapper,
            request_options=request_options,
        )
