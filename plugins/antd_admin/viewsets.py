import json
from .drf_wrapper.authentication import TokenAuthentication
from antd_admin.drf_wrapper.viewset import BaseModelViewSet
from antd_admin.drf_wrapper.response.renderer import Renderer
from antd_admin.serializers import LoginSerializer, UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from antd_admin.drf_wrapper.response.response import DataPackage, JsonResponse
from .hashers import make_jwt

User = get_user_model()


class LoginViewSet(BaseModelViewSet):
    renderer_classes = (Renderer,)

    def login(self, request, *args, **kwargs):
        """
        登陆
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        print(json.dumps(data))
        ser = LoginSerializer(data=data)
        ser.is_valid()
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            raise AuthenticationFailed
        ser = UserSerializer(instance=user)
        token = make_jwt(data=ser.data, exp=3600)
        _d = DataPackage().set_fields(ser.data).set_field('token', token)
        return JsonResponse(data=_d)

    def logout(self, request, *args, **kwargs):
        pass


class UserViewSet(BaseModelViewSet):
    renderer_classes = (Renderer,)

    authentication_classes = (TokenAuthentication,)

    def user_detail(self, request, *args, **kwargs):
        """
        用户详情
        :return:
        """
        user = request.user
        print('-----> 用户详情', user)
        ser = UserSerializer(instance=user)
        _d = DataPackage().set_fields(ser.data)
        return JsonResponse(data=_d)
