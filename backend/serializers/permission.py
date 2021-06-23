from rest_framework import serializers
from user.models import Permission


class PermissionListSerializer(serializers.ModelSerializer):
    
    parent = serializers.SerializerMethodField()
    def get_parent(self, obj):
        return str(obj.parent) if  obj.parent else ''
    

    obj_ = serializers.SerializerMethodField()
    def get_obj_(self, obj):
        return str(obj)

    class Meta:
        fields = '__all__'
        model = Permission


class PermissionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission


class PermissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission


class PermissionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission


class PermissionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Permission