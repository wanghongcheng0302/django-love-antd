import jwt
import datetime
from django.conf import settings


def make_jwt(data: dict, exp: int = 3600):
    payload = {
        'exp': datetime.datetime.now() + datetime.timedelta(seconds=exp),
        'iat': datetime.datetime.now(),
    }
    payload.update(data)

    headers = {
        'alg': "HS256",
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256", headers=headers)
    return token


def check_jwt(token: str):
    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    except Exception as _:
        return None
    return data
