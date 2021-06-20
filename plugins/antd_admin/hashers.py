import jwt
import datetime
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, DecodeError
from rest_framework import exceptions


def make_jwt(data: dict, exp: int = 3600):
    payload = {
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=exp),
        'iat': datetime.datetime.now(),
    }
    payload.update(data)

    headers = {
        'alg': "RS256",
    }
    token = jwt.encode(payload, settings.ANTD_RSA_PRIVATE_KEY, algorithm="RS256", headers=headers)
    return token


def check_jwt(token: str):
    try:
        return jwt.decode(token, settings.ANTD_RSA_PUBLIC_KEY, algorithms=['RS256'])
    except ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('登陆过期')
    except DecodeError:
        raise exceptions.AuthenticationFailed('请登录')
