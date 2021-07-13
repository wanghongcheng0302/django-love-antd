from django.contrib.auth.models import AnonymousUser
from rest_framework import permissions
from rest_framework import exceptions
from antd_pro.common.casbin_adapter.enforcer import enforcer
from antd_pro.models import AntdPermission


class CasbinAccessPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if isinstance(user, AnonymousUser):
            raise exceptions.PermissionDenied
        # perm_qs = AntdPermission.objects.values('id').filter(route=request.path, method=request.method.lower())
        # perm_qs = [str(perm['id']) for perm in perm_qs]
        # obj = perm_qs[0] if perm_qs else None
        # print(enforcer.enforce(obj))
        return True
