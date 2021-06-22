from rest_framework import serializers
from user.models import User


class UserListSerializer(serializers.ModelSerializer):
    # {'name': 'roles', 'label': '角色集', 'max_length': None, 'to': <class 'user.models.Role'>, 'is_foreignkey': False, 'is_many2many': True, 'editable': True, 'choices': None, 'type': 'ManyToManyField', 'is_primary_key': False, 'blank': True, 'help_text': '', 'unique': False, '_parent': <antd_admin.core.parse.model.ModelParser object at 0x10e469760>, 'auto_created': False, 'auto_now_add': False, 'auto_now': False}
    roles = serializers.SerializerMethodField()

    def get_roles(self, obj):
        return [str(item) for item in obj.roles.filter()]
    

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