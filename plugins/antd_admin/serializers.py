from rest_framework import serializers
from antd_admin.drf_wrapper.serializer import BaseSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializer(BaseSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        exclude = ('password',)
