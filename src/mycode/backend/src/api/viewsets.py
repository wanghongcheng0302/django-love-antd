from rest_framework.viewsets import ModelViewSet
from user.models import Permission
from user.models import Role
from user.models import User
from user.models import Group
from .serializers import PermissionSerializer, PermissionFormSerializer
from .serializers import RoleSerializer, RoleFormSerializer
from .serializers import UserSerializer, UserFormSerializer
from .serializers import GroupSerializer, GroupFormSerializer


class PermissionViewSet(ModelViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.filter()

    def list(self, request, *args, **kwargs):
        return super(PermissionViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = PermissionFormSerializer
        return super(PermissionViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = PermissionFormSerializer
        return super(PermissionViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PermissionViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(PermissionViewSet, self).retrieve(request, *args, **kwargs)


class RoleViewSet(ModelViewSet):
    serializer_class = RoleSerializer
    queryset = Role.objects.filter()

    def list(self, request, *args, **kwargs):
        return super(RoleViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = RoleFormSerializer
        return super(RoleViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = RoleFormSerializer
        return super(RoleViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(RoleViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(RoleViewSet, self).retrieve(request, *args, **kwargs)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.filter()

    def list(self, request, *args, **kwargs):
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = UserFormSerializer
        return super(UserViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = UserFormSerializer
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(UserViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)


class GroupViewSet(ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.filter()

    def list(self, request, *args, **kwargs):
        return super(GroupViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = GroupFormSerializer
        return super(GroupViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = GroupFormSerializer
        return super(GroupViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(GroupViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super(GroupViewSet, self).retrieve(request, *args, **kwargs)



