from rest_framework import serializers
from user.models import Role


class RoleListSerializer(serializers.ModelSerializer):
    # {'name': 'permissions', 'label': '权限集', 'max_length': None, 'to': 'Permission', 'is_foreignkey': False, 'is_many2many': True, 'editable': True, 'choices': None, 'type': 'ManyToManyField', 'is_primary_key': False, 'blank': True, 'help_text': '', 'unique': False, '_parent': <antd_admin.core.parse.model.ModelParser object at 0x10801db50>}
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        return [str(item) for item in obj.permissions.filter()]
    

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