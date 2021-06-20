from django.contrib.auth import get_user_model
from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import AnonymousUser
from ..hashers import check_jwt
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
            raise AuthenticationFailed
        userinfo = check_jwt(token)
        if not userinfo:
            return AnonymousUser, False
        user = User.objects.filter(id=userinfo['id']).first()
        if not user:
            return AnonymousUser, False
        return user, True
