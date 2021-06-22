from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from ..serializers.permission import PermissionListSerializer, PermissionCreateSerializer, PermissionUpdateSerializer, PermissionDeleteSerializer, \
    PermissionDetailSerializer
from user.models import Permission
from rest_framework import filters
from antd_admin.drf_wrapper.response.renderer import Renderer
from antd_admin.drf_wrapper.pagination import PageNumberPagination


class PermissionViewSet(ModelViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    renderer_classes = (Renderer, )
    pagination_class = PageNumberPagination
    
    

    def list(self, request, *args, **kwargs):
        self.serializer_class = PermissionListSerializer
        return super(PermissionViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        return super(PermissionViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PermissionDetailSerializer
        return super(PermissionViewSet, self).retrieve(request, *args, **kwargs)