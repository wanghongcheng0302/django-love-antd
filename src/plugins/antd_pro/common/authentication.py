from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import AnonymousUser
from antd_pro.utils.hashers import check_jwt
from rest_framework.exceptions import AuthenticationFailed
from antd_pro.models import AntdUser


class TokenAuthentication(BaseAuthentication):

    def authenticate(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            raise AuthenticationFailed
        userinfo = check_jwt(token)
        if not userinfo:
            return AnonymousUser, False
        user = AntdUser.objects.filter(id=userinfo['id']).first()
        if not user:
            return AnonymousUser, False
        return user, True
