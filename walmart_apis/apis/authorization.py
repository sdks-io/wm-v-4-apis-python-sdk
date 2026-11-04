from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    form_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.create_token_error import CreateTokenErrorBody, create_token_error_mapper
from ..models.enums.grant_type import GrantTypeOrStr
from ..models.token_response import TokenResponse
from ..server.server import Server


class Authorization:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AuthorizationWithRawResponse(client, server, auth)

    def create_token(
        self,
        grant_type: GrantTypeOrStr,
        *,
        x_o_tenant: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        code_verifier: str | None = None,
        refresh_token: str | None = None,
        redirect_uri: str | None = None,
        scope: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenResponse:
        """The Authorization API exchanges an OAuth grant for an access token. It supports the ``client_credentials``,
        ``authorization_code``, and ``refresh_token`` grant types.

        | ``grant_type`` | Authorization flow | Additional requirements |
        |--------------|--------------------|-------------------------|
        | ``client_credentials`` | Seller-direct | Client authentication |
        | ``authorization_code`` | Delegated | ``code`` and PKCE, or confidential-client authentication and
            ``redirect_uri`` |
        | ``refresh_token`` | Delegated | ``refresh_token``; public clients also send ``client_id`` |

        **Client authentication:** Confidential clients can authenticate by sending ``client_id`` and ``client_secret``
        in the form body (``client_secret_post``) or by using HTTP Basic authentication. Use only one authentication
        method. When using HTTP Basic authentication, omit ``client_id`` and ``client_secret`` from the request body. A
        request that combines HTTP Basic authentication with body credentials returns ``400`` with ``invalid_request``.

        Public clients send no client secret. Public clients using the ``authorization_code`` grant must use PKCE.

        **``client_credentials``:** Returns an access token without a refresh token. To obtain another access token
        after expiration, submit another ``client_credentials`` request. The optional ``scope`` value is accepted but
        does not reduce the access provisioned for the client, and the response does not echo ``scope``.

        **``authorization_code``:** Public clients must send a PKCE ``code_verifier``. PKCE uses the ``S256`` challenge
        method; ``plain`` is not accepted. Confidential clients can omit ``code_verifier`` when they authenticate at the
        token operation and send ``redirect_uri``.

        **``refresh_token``:** Submit a previously issued ``refresh_token`` to request another access token. Public
        clients also send ``client_id``. If ``scope`` is provided, it must not exceed the scope originally granted.

        Send the returned access token with Marketplace V4 API requests as ``Authorization: Bearer <token>``. Do not use
        ``WM_SEC.ACCESS_TOKEN``.

        ``x-o-tenant`` selects one market when supplied. A direct client active in multiple markets must supply it; a
        delegated token's IAM market must match it. Without it, a direct client with exactly one active market uses that
        market, and a delegated token uses its IAM market. Supported values are ``WALMART_US``, ``WALMART_CA``,
        ``WALMART_MX``, and ``WALMART_CL``.

        Treat access tokens, refresh tokens, and client secrets as sensitive values and do not log them.

        Args:
            grant_type: OAuth grant type used to request the access token.
            x_o_tenant: One supported market for the issued access token. Comma-separated values are rejected.
            client_id: Client ID for the application. Provide this property when using client credentials in the request
                body or when required for a public client. Omit it from the request body when using HTTP Basic
                authentication.
            client_secret: Client secret used to authenticate a confidential client with credentials in the request
                body. Omit for public clients and when using HTTP Basic authentication. Treat as a secret and do not log
                it.
            code: Authorization code returned by Walmart Account Login. Used with the ``authorization_code`` grant.
            code_verifier: PKCE verifier associated with the ``code_challenge`` from the authorization request. Required
                for public clients using the ``authorization_code`` grant and recommended for all clients. Confidential
                clients can omit this property only when authenticating at the token operation and providing
                ``redirect_uri``.
            refresh_token: Previously issued refresh token used with the ``refresh_token`` grant. Treat as a secret and
                do not log it.
            redirect_uri: Redirect URI for the authorization flow. Required when a confidential client uses the
                ``authorization_code`` grant without ``code_verifier``.
            scope: Requested OAuth scope. For ``client_credentials``, this property is accepted but does not reduce the
                access provisioned for the client, and the response does not echo the value. For ``refresh_token``, the
                requested scope must not exceed the scope originally granted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the access token and related token information.

        Raises:
            ApiError: The token request is invalid. Client authentication failed. The request exceeded the applicable
                rate limit. The token request could not be completed because of an unexpected server error. ``error`` is
                ``server_error``. A service the token endpoint depends on is temporarily unavailable. Retry the request.
                ``error`` is ``temporarily_unavailable``. ``error`` is ``OAuthErrorModel | RawError``."""
        return unwrap(
            self._with_raw_response.create_token(
                grant_type,
                x_o_tenant=x_o_tenant,
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

    @property
    def with_raw_response(self) -> AuthorizationWithRawResponse:
        return self._with_raw_response


class AsyncAuthorization:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAuthorizationWithRawResponse(client, server, auth)

    async def create_token(
        self,
        grant_type: GrantTypeOrStr,
        *,
        x_o_tenant: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        code_verifier: str | None = None,
        refresh_token: str | None = None,
        redirect_uri: str | None = None,
        scope: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TokenResponse:
        """The Authorization API exchanges an OAuth grant for an access token. It supports the ``client_credentials``,
        ``authorization_code``, and ``refresh_token`` grant types.

        | ``grant_type`` | Authorization flow | Additional requirements |
        |--------------|--------------------|-------------------------|
        | ``client_credentials`` | Seller-direct | Client authentication |
        | ``authorization_code`` | Delegated | ``code`` and PKCE, or confidential-client authentication and
            ``redirect_uri`` |
        | ``refresh_token`` | Delegated | ``refresh_token``; public clients also send ``client_id`` |

        **Client authentication:** Confidential clients can authenticate by sending ``client_id`` and ``client_secret``
        in the form body (``client_secret_post``) or by using HTTP Basic authentication. Use only one authentication
        method. When using HTTP Basic authentication, omit ``client_id`` and ``client_secret`` from the request body. A
        request that combines HTTP Basic authentication with body credentials returns ``400`` with ``invalid_request``.

        Public clients send no client secret. Public clients using the ``authorization_code`` grant must use PKCE.

        **``client_credentials``:** Returns an access token without a refresh token. To obtain another access token
        after expiration, submit another ``client_credentials`` request. The optional ``scope`` value is accepted but
        does not reduce the access provisioned for the client, and the response does not echo ``scope``.

        **``authorization_code``:** Public clients must send a PKCE ``code_verifier``. PKCE uses the ``S256`` challenge
        method; ``plain`` is not accepted. Confidential clients can omit ``code_verifier`` when they authenticate at the
        token operation and send ``redirect_uri``.

        **``refresh_token``:** Submit a previously issued ``refresh_token`` to request another access token. Public
        clients also send ``client_id``. If ``scope`` is provided, it must not exceed the scope originally granted.

        Send the returned access token with Marketplace V4 API requests as ``Authorization: Bearer <token>``. Do not use
        ``WM_SEC.ACCESS_TOKEN``.

        ``x-o-tenant`` selects one market when supplied. A direct client active in multiple markets must supply it; a
        delegated token's IAM market must match it. Without it, a direct client with exactly one active market uses that
        market, and a delegated token uses its IAM market. Supported values are ``WALMART_US``, ``WALMART_CA``,
        ``WALMART_MX``, and ``WALMART_CL``.

        Treat access tokens, refresh tokens, and client secrets as sensitive values and do not log them.

        Args:
            grant_type: OAuth grant type used to request the access token.
            x_o_tenant: One supported market for the issued access token. Comma-separated values are rejected.
            client_id: Client ID for the application. Provide this property when using client credentials in the request
                body or when required for a public client. Omit it from the request body when using HTTP Basic
                authentication.
            client_secret: Client secret used to authenticate a confidential client with credentials in the request
                body. Omit for public clients and when using HTTP Basic authentication. Treat as a secret and do not log
                it.
            code: Authorization code returned by Walmart Account Login. Used with the ``authorization_code`` grant.
            code_verifier: PKCE verifier associated with the ``code_challenge`` from the authorization request. Required
                for public clients using the ``authorization_code`` grant and recommended for all clients. Confidential
                clients can omit this property only when authenticating at the token operation and providing
                ``redirect_uri``.
            refresh_token: Previously issued refresh token used with the ``refresh_token`` grant. Treat as a secret and
                do not log it.
            redirect_uri: Redirect URI for the authorization flow. Required when a confidential client uses the
                ``authorization_code`` grant without ``code_verifier``.
            scope: Requested OAuth scope. For ``client_credentials``, this property is accepted but does not reduce the
                access provisioned for the client, and the response does not echo the value. For ``refresh_token``, the
                requested scope must not exceed the scope originally granted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Returns the access token and related token information.

        Raises:
            ApiError: The token request is invalid. Client authentication failed. The request exceeded the applicable
                rate limit. The token request could not be completed because of an unexpected server error. ``error`` is
                ``server_error``. A service the token endpoint depends on is temporarily unavailable. Retry the request.
                ``error`` is ``temporarily_unavailable``. ``error`` is ``OAuthErrorModel | RawError``."""
        return unwrap(
            await self._with_raw_response.create_token(
                grant_type,
                x_o_tenant=x_o_tenant,
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

    @property
    def with_raw_response(self) -> AsyncAuthorizationWithRawResponse:
        return self._with_raw_response


class AuthorizationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_token(
        self,
        grant_type: GrantTypeOrStr,
        *,
        x_o_tenant: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        code_verifier: str | None = None,
        refresh_token: str | None = None,
        redirect_uri: str | None = None,
        scope: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenResponse, CreateTokenErrorBody]:
        """The Authorization API exchanges an OAuth grant for an access token. It supports the ``client_credentials``,
        ``authorization_code``, and ``refresh_token`` grant types.

        | ``grant_type`` | Authorization flow | Additional requirements |
        |--------------|--------------------|-------------------------|
        | ``client_credentials`` | Seller-direct | Client authentication |
        | ``authorization_code`` | Delegated | ``code`` and PKCE, or confidential-client authentication and
            ``redirect_uri`` |
        | ``refresh_token`` | Delegated | ``refresh_token``; public clients also send ``client_id`` |

        **Client authentication:** Confidential clients can authenticate by sending ``client_id`` and ``client_secret``
        in the form body (``client_secret_post``) or by using HTTP Basic authentication. Use only one authentication
        method. When using HTTP Basic authentication, omit ``client_id`` and ``client_secret`` from the request body. A
        request that combines HTTP Basic authentication with body credentials returns ``400`` with ``invalid_request``.

        Public clients send no client secret. Public clients using the ``authorization_code`` grant must use PKCE.

        **``client_credentials``:** Returns an access token without a refresh token. To obtain another access token
        after expiration, submit another ``client_credentials`` request. The optional ``scope`` value is accepted but
        does not reduce the access provisioned for the client, and the response does not echo ``scope``.

        **``authorization_code``:** Public clients must send a PKCE ``code_verifier``. PKCE uses the ``S256`` challenge
        method; ``plain`` is not accepted. Confidential clients can omit ``code_verifier`` when they authenticate at the
        token operation and send ``redirect_uri``.

        **``refresh_token``:** Submit a previously issued ``refresh_token`` to request another access token. Public
        clients also send ``client_id``. If ``scope`` is provided, it must not exceed the scope originally granted.

        Send the returned access token with Marketplace V4 API requests as ``Authorization: Bearer <token>``. Do not use
        ``WM_SEC.ACCESS_TOKEN``.

        ``x-o-tenant`` selects one market when supplied. A direct client active in multiple markets must supply it; a
        delegated token's IAM market must match it. Without it, a direct client with exactly one active market uses that
        market, and a delegated token uses its IAM market. Supported values are ``WALMART_US``, ``WALMART_CA``,
        ``WALMART_MX``, and ``WALMART_CL``.

        Treat access tokens, refresh tokens, and client secrets as sensitive values and do not log them.

        Args:
            grant_type: OAuth grant type used to request the access token.
            x_o_tenant: One supported market for the issued access token. Comma-separated values are rejected.
            client_id: Client ID for the application. Provide this property when using client credentials in the request
                body or when required for a public client. Omit it from the request body when using HTTP Basic
                authentication.
            client_secret: Client secret used to authenticate a confidential client with credentials in the request
                body. Omit for public clients and when using HTTP Basic authentication. Treat as a secret and do not log
                it.
            code: Authorization code returned by Walmart Account Login. Used with the ``authorization_code`` grant.
            code_verifier: PKCE verifier associated with the ``code_challenge`` from the authorization request. Required
                for public clients using the ``authorization_code`` grant and recommended for all clients. Confidential
                clients can omit this property only when authenticating at the token operation and providing
                ``redirect_uri``.
            refresh_token: Previously issued refresh token used with the ``refresh_token`` grant. Treat as a secret and
                do not log it.
            redirect_uri: Redirect URI for the authorization flow. Required when a confidential client uses the
                ``authorization_code`` grant without ``code_verifier``.
            scope: Requested OAuth scope. For ``client_credentials``, this property is accepted but does not reduce the
                access provisioned for the client, and the response does not echo the value. For ``refresh_token``, the
                requested scope must not exceed the scope originally granted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v4/auth/token"),
            headers=[param[str | None]("x-o-tenant", x_o_tenant), param[UUID]("Idempotency-Key", uuid4())],
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


class AsyncAuthorizationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_token(
        self,
        grant_type: GrantTypeOrStr,
        *,
        x_o_tenant: str | None = None,
        client_id: str | None = None,
        client_secret: str | None = None,
        code: str | None = None,
        code_verifier: str | None = None,
        refresh_token: str | None = None,
        redirect_uri: str | None = None,
        scope: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TokenResponse, CreateTokenErrorBody]:
        """The Authorization API exchanges an OAuth grant for an access token. It supports the ``client_credentials``,
        ``authorization_code``, and ``refresh_token`` grant types.

        | ``grant_type`` | Authorization flow | Additional requirements |
        |--------------|--------------------|-------------------------|
        | ``client_credentials`` | Seller-direct | Client authentication |
        | ``authorization_code`` | Delegated | ``code`` and PKCE, or confidential-client authentication and
            ``redirect_uri`` |
        | ``refresh_token`` | Delegated | ``refresh_token``; public clients also send ``client_id`` |

        **Client authentication:** Confidential clients can authenticate by sending ``client_id`` and ``client_secret``
        in the form body (``client_secret_post``) or by using HTTP Basic authentication. Use only one authentication
        method. When using HTTP Basic authentication, omit ``client_id`` and ``client_secret`` from the request body. A
        request that combines HTTP Basic authentication with body credentials returns ``400`` with ``invalid_request``.

        Public clients send no client secret. Public clients using the ``authorization_code`` grant must use PKCE.

        **``client_credentials``:** Returns an access token without a refresh token. To obtain another access token
        after expiration, submit another ``client_credentials`` request. The optional ``scope`` value is accepted but
        does not reduce the access provisioned for the client, and the response does not echo ``scope``.

        **``authorization_code``:** Public clients must send a PKCE ``code_verifier``. PKCE uses the ``S256`` challenge
        method; ``plain`` is not accepted. Confidential clients can omit ``code_verifier`` when they authenticate at the
        token operation and send ``redirect_uri``.

        **``refresh_token``:** Submit a previously issued ``refresh_token`` to request another access token. Public
        clients also send ``client_id``. If ``scope`` is provided, it must not exceed the scope originally granted.

        Send the returned access token with Marketplace V4 API requests as ``Authorization: Bearer <token>``. Do not use
        ``WM_SEC.ACCESS_TOKEN``.

        ``x-o-tenant`` selects one market when supplied. A direct client active in multiple markets must supply it; a
        delegated token's IAM market must match it. Without it, a direct client with exactly one active market uses that
        market, and a delegated token uses its IAM market. Supported values are ``WALMART_US``, ``WALMART_CA``,
        ``WALMART_MX``, and ``WALMART_CL``.

        Treat access tokens, refresh tokens, and client secrets as sensitive values and do not log them.

        Args:
            grant_type: OAuth grant type used to request the access token.
            x_o_tenant: One supported market for the issued access token. Comma-separated values are rejected.
            client_id: Client ID for the application. Provide this property when using client credentials in the request
                body or when required for a public client. Omit it from the request body when using HTTP Basic
                authentication.
            client_secret: Client secret used to authenticate a confidential client with credentials in the request
                body. Omit for public clients and when using HTTP Basic authentication. Treat as a secret and do not log
                it.
            code: Authorization code returned by Walmart Account Login. Used with the ``authorization_code`` grant.
            code_verifier: PKCE verifier associated with the ``code_challenge`` from the authorization request. Required
                for public clients using the ``authorization_code`` grant and recommended for all clients. Confidential
                clients can omit this property only when authenticating at the token operation and providing
                ``redirect_uri``.
            refresh_token: Previously issued refresh token used with the ``refresh_token`` grant. Treat as a secret and
                do not log it.
            redirect_uri: Redirect URI for the authorization flow. Required when a confidential client uses the
                ``authorization_code`` grant without ``code_verifier``.
            scope: Requested OAuth scope. For ``client_credentials``, this property is accepted but does not reduce the
                access provisioned for the client, and the response does not echo the value. For ``refresh_token``, the
                requested scope must not exceed the scope originally granted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v4/auth/token"),
            headers=[param[str | None]("x-o-tenant", x_o_tenant), param[UUID]("Idempotency-Key", uuid4())],
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
