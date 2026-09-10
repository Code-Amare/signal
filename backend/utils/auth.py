from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed


class JWTCookiesAuthentication(JWTAuthentication):

    cookie_name = "access_token"

    def authenticate(self, request):

        access_token = request.COOKIES.get(self.cookie_name)

        if not access_token:
            return None

        try:
            validated_token = self.get_validated_token(access_token)

            user = self.get_user(validated_token)

        except (InvalidToken, TokenError):
            raise AuthenticationFailed("Invalid or expired token.")

        self.enforce_csrf(request)

        return user, validated_token

    def enforce_csrf(self, request):
        SessionAuthentication().enforce_csrf(request)
