from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from ..serializers.group import GroupListSerializer, GroupCreateSerializer, GroupUpdateSerializer, GroupDeleteSerializer, \
    GroupDetailSerializer
from user.models import Group
from rest_framework import filters
from antd_admin.drf_wrapper.response.renderer import Renderer
from antd_admin.drf_wrapper.pagination import PageNumberPagination


class GroupViewSet(ModelViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    renderer_classes = (Renderer, )
    pagination_class = PageNumberPagination
    
    

    def list(self, request, *args, **kwargs):
        self.serializer_class = GroupListSerializer
        return super(GroupViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = GroupUpdateSerializer
        return super(GroupViewSet, self).update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = GroupCreateSerializer
        return super(GroupViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(GroupViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = GroupDetailSerializer
        return super(GroupViewSet, self).retrieve(request, *args, **kwargs)