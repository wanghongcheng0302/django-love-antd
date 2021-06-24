from rest_framework import serializers
from user.models import Group


class GroupListSerializer(serializers.ModelSerializer):
    # {'name': 'permissions', 'label': '权限集', 'max_length': None, 'to': <class 'user.models.Permission'>, 'is_foreignkey': False, 'is_many2many': True, 'editable': True, 'choices': None, 'type': 'ManyToManyField', 'is_primary_key': False, 'blank': True, 'help_text': '', 'unique': False, '_parent': <antd_admin.core.parse.model.ModelParser object at 0x10d23cca0>, 'auto_created': False, 'auto_now_add': False, 'auto_now': False}
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, obj):
        return [str(item) for item in obj.permissions.filter()]
        # {'name': 'users', 'label': '用户群', 'max_length': None, 'to': <class 'user.models.User'>, 'is_foreignkey': False, 'is_many2many': True, 'editable': True, 'choices': None, 'type': 'ManyToManyField', 'is_primary_key': False, 'blank': True, 'help_text': '', 'unique': False, '_parent': <antd_admin.core.parse.model.ModelParser object at 0x10d23cca0>, 'auto_created': False, 'auto_now_add': False, 'auto_now': False}
    users = serializers.SerializerMethodField()

    def get_users(self, obj):
        return [str(item) for item in obj.users.filter()]
        

    obj_ = serializers.SerializerMethodField()
    def get_obj_(self, obj):
        return str(obj)

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
    obj_ = serializers.SerializerMethodField()
    def get_obj_(self, obj):
        return str(obj)
    class Meta:
        fields = '__all__'
        model = Group


class GroupDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group