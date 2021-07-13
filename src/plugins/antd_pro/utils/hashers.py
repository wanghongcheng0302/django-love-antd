import jwt
import datetime
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError, DecodeError
from rest_framework import exceptions

antd_conf = getattr(settings, 'ANTD')
if not antd_conf:
    raise AttributeError('未配置rsa秘钥')
if not antd_conf.get('ANTD_RSA_PRIVATE_KEY') or not antd_conf.get('ANTD_RSA_PUBLIC_KEY'):
    raise AttributeError('未配置rsa秘钥')


def make_jwt(data: dict, exp: int = 360000):
    payload = {
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=exp),
        'iat': datetime.datetime.now(),
    }
    payload.update(data)

    headers = {
        'alg': "RS256",
    }
    token = jwt.encode(payload, antd_conf.get('ANTD_RSA_PRIVATE_KEY'), algorithm="RS256", headers=headers)
    return token


def check_jwt(token: str):
    try:
        return jwt.decode(token, antd_conf.get('ANTD_RSA_PUBLIC_KEY'), algorithms=['RS256'])
    except ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('登陆过期')
    except DecodeError:
        raise exceptions.AuthenticationFailed('请登录')
