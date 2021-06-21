from rest_framework import serializers
from user.models import Group


class GroupListSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    def get_users(self, obj):
        return [str(item) for item in obj.users.filter()]
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        return [str(item) for item in obj.permissions.filter()]
    

    class Meta:
        fields = '__all__'
        model = Group


class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class GroupUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class GroupDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group