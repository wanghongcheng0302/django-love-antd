from rest_framework import serializers
from user.models import Role


class RoleListSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        return [str(item) for item in obj.permissions.filter()]
    roles = serializers.SerializerMethodField()

    def get_roles(self, obj):
        return [str(item) for item in obj.roles.filter()]
    

    class Meta:
        fields = '__all__'
        model = Role


class RoleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Role


class RoleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Role


class RoleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Role


class RoleDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Role