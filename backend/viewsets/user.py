from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from ..serializers.user import UserListSerializer, UserCreateSerializer, UserUpdateSerializer, UserDeleteSerializer, \
    UserDetailSerializer
from user.models import User
from rest_framework import filters
from antd_admin.drf_wrapper.response.renderer import Renderer
from antd_admin.drf_wrapper.pagination import PageNumberPagination


class UserViewSet(ModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    renderer_classes = (Renderer, )
    pagination_class = PageNumberPagination
    
    

    def list(self, request, *args, **kwargs):
        self.serializer_class = UserListSerializer
        return super(UserViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = UserUpdateSerializer
        return super(UserViewSet, self).update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = UserCreateSerializer
        return super(UserViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(UserViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = UserDetailSerializer
        return super(UserViewSet, self).retrieve(request, *args, **kwargs)