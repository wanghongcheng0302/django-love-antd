from rest_framework import serializers
from user.models import User


class UserListSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    def get_roles(self, obj):
        return [str(item) for item in obj.roles.filter()]
    users = serializers.SerializerMethodField()

    def get_users(self, obj):
        return [str(item) for item in obj.users.filter()]
    

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