from django_filters import rest_framework as filters
from .models import AntdCasbinRule, AntdRole, AntdUser, AntdMenuRule


class AntdRoleFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = AntdRole
        fields = ('id', 'name', 'parent')


class AntdUserFilter(filters.FilterSet):
    phone_num = filters.CharFilter(field_name='phone_num', lookup_expr='icontains')
    profile__gender = filters.NumberFilter(field_name='user_profile__gender')
    profile__birthday = filters.DateTimeFilter(field_name='user_profile__birthday')
    profile__email = filters.CharFilter(field_name='user_profile__email', lookup_expr='icontains')

    class Meta:
        model = AntdUser
        fields = ('id', 'phone_num', 'roles', 'is_super', 'profile__gender', 'profile__birthday', 'profile__email')


class AntdCasbinFilter(filters.FilterSet):
    route = filters.CharFilter(field_name='v1')
    roles = filters.CharFilter(field_name='v0')

    class Meta:
        model = AntdCasbinRule
        fields = ('route', 'roles')


class AntdMenuRuleFilter(filters.FilterSet):
    class Meta:
        model = AntdMenuRule
        fields = ('route', 'roles', 'id')
