import json

from rest_framework import serializers
from .models import AntdPermission, AntdRole, AntdUser, AntdUserProfile, AntdCasbinRule, AntdMenuRule
from django.core import validators
from rest_framework import exceptions
from django.contrib.auth.hashers import check_password
from antd_pro.common.serializers import ModelSerializer
from antd_pro.utils.fields import get_field_by_entity


class AntdPermissionSerializer(ModelSerializer):
    _str_parent = serializers.SerializerMethodField()

    def get__str_parent(self, obj):
        return str(obj.parent) if obj.parent else None

    class Meta:
        fields = '__all__'
        model = AntdPermission


class AntdPermissionFormSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AntdPermission


class AntdPermissionBatchDeleteSerializer(ModelSerializer):
    ids = serializers.ListField(write_only=True)

    class Meta:
        model = AntdPermission
        fields = ('ids',)


class AntdRoleSerializer(ModelSerializer):
    _str_parent = serializers.SerializerMethodField()

    # _str_permissions = serializers.SerializerMethodField()

    def get__str_parent(self, obj):
        return str(obj.parent) if obj.parent else None

    # def get__str_permissions(self, obj):
    #     return [str(perm) for perm in obj.permissions.filter()]

    class Meta:
        fields = '__all__'
        model = AntdRole


class AntdRoleFormSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = AntdRole


class AntdRoleBatchDeleteSerializer(ModelSerializer):
    ids = serializers.ListField(write_only=True)

    class Meta:
        model = AntdRole
        fields = ('ids',)


class AntdUserProfileSerializer(ModelSerializer):
    birthday = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    _str_gender = serializers.SerializerMethodField(read_only=True)

    def get__str_gender(self, obj):
        gender_field = get_field_by_entity(obj, 'gender')
        choices = getattr(gender_field, 'choices')
        display = [item[1] for item in choices if item[0] == obj.gender]
        return display[0] if display else None

    class Meta:
        fields = '__all__'
        model = AntdUserProfile


class AntdUserSerializer(ModelSerializer):
    profile = serializers.SerializerMethodField()
    _str_roles = serializers.SerializerMethodField()

    def get__str_roles(self, obj):
        return [str(role) for role in obj.roles.filter()]

    def get_profile(self, obj):
        profile = AntdUserProfile.objects.filter(user=obj).first()
        ser = AntdUserProfileSerializer(instance=profile)
        return ser.data

    class Meta:
        exclude = ('password',)
        model = AntdUser


class AntdUserFormSerializer(ModelSerializer):
    phoneNum = serializers.CharField(write_only=True,
                                     validators=[validators.RegexValidator('1[345678]\d{9}', message='请输入正确的手机号')])
    profile__birthday = serializers.DateTimeField(write_only=True)
    profile__email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    # profile__avatar = serializers.ImageField(write_only=True)
    profile__gender = serializers.ChoiceField(choices=AntdUserProfile.GENDER_CHOICES, write_only=True)

    class Meta:
        fields = ('phoneNum', 'is_super', 'roles', 'profile__birthday', 'profile__email', 'password', 'profile__gender')
        model = AntdUser


class AntdUserBatchDeleteSerializer(ModelSerializer):
    ids = serializers.ListField(write_only=True)

    class Meta:
        model = AntdUser
        fields = ('ids',)


class LoginSerializer(ModelSerializer):
    phoneNum = serializers.CharField(write_only=True,
                                     validators=[validators.RegexValidator('1[345678]\d{9}', message='请输入正确的手机号')])

    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        phone_num = self.initial_data.get('phoneNum')
        password = value
        user = AntdUser.objects.filter(phone_num=phone_num).first()
        if not check_password(value, user.password):
            raise exceptions.AuthenticationFailed('密码错误')
        return password

    def validate_phoneNum(self, value):
        user = AntdUser.objects.filter(phone_num=value).first()
        if not user:
            raise exceptions.AuthenticationFailed('手机号未注册')
        return value

    class Meta:
        model = AntdUser
        fields = ('phoneNum', 'password')


class AntdCasbinRuleSerializer(ModelSerializer):
    route = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()
    method = serializers.SerializerMethodField()
    _str_roles = serializers.SerializerMethodField()

    def get_route(self, obj):
        return obj.v1

    def get_method(self, obj):
        return obj.v2

    def get_roles(self, obj):
        try:
            return json.loads(obj.v0) if obj.v0 else []
        except Exception:
            return []

    def get__str_roles(self, obj):
        try:
            role_ids = json.loads(obj.v0) if obj.v0 else []
            return [str(role) for role in AntdRole.objects.filter(id__in=role_ids)]
        except Exception:
            return []

    class Meta:
        model = AntdCasbinRule
        fields = ('id', 'route', 'roles', 'method', '_str_roles')


class AntdCasbinRuleFormSerializer(ModelSerializer):
    route = serializers.CharField(write_only=True)
    roles = serializers.ListField(write_only=True)
    method = serializers.ChoiceField(write_only=True, choices=('get', 'post', 'put', 'delete'))

    class Meta:
        model = AntdCasbinRule
        fields = ('route', 'roles', 'method')


class AntdCasbinBatchDeleteSerializer(ModelSerializer):
    ids = serializers.ListField(write_only=True)

    class Meta:
        model = AntdCasbinRule
        fields = ('ids',)


class AntdMenuSerializer(ModelSerializer):
    _str_roles = serializers.SerializerMethodField()

    def get__str_roles(self, obj):
        return [str(role) for role in obj.roles.filter()]

    class Meta:
        model = AntdMenuRule
        fields = '__all__'


class AntdMenuFormSerializer(ModelSerializer):
    class Meta:
        model = AntdMenuRule
        fields = ('route', 'roles',)


class AntdMenuBatchDeleteSerializer(ModelSerializer):
    ids = serializers.ListField(write_only=True)

    class Meta:
        model = AntdCasbinRule
        fields = ('ids',)
