from rest_framework import serializers
from user.models import User


class UserListSerializer(serializers.ModelSerializer):
    

    class Meta:
        fields = '__all__'
        model = User


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User


class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User