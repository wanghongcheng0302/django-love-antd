from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from ..serializers.role import RoleListSerializer, RoleCreateSerializer, RoleUpdateSerializer, RoleDeleteSerializer, \
    RoleDetailSerializer
from user.models import Role
from rest_framework import filters
from antd_admin.drf_wrapper.response.renderer import Renderer
from antd_admin.drf_wrapper.pagination import PageNumberPagination


class RoleViewSet(ModelViewSet):
    serializer_class = RoleListSerializer
    queryset = Role.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    renderer_classes = (Renderer, )
    pagination_class = PageNumberPagination
    
    

    def list(self, request, *args, **kwargs):
        self.serializer_class = RoleListSerializer
        return super(RoleViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        return super(RoleViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(RoleViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = RoleDetailSerializer
        return super(RoleViewSet, self).retrieve(request, *args, **kwargs)