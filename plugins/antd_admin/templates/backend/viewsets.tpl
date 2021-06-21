from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from ..serializers.{[ model.name ]} import {[ model.classname ]}ListSerializer, {[ model.classname ]}CreateSerializer, {[ model.classname ]}UpdateSerializer, {[ model.classname ]}DeleteSerializer, \
    {[ model.classname ]}DetailSerializer
from {[ app_name ]}.models import {[ model.classname ]}
from rest_framework import filters
from antd_admin.drf_wrapper.response.renderer import Renderer
from antd_admin.drf_wrapper.pagination import PageNumberPagination


class {[ model.classname ]}ViewSet(ModelViewSet):
    serializer_class = {[ model.classname ]}ListSerializer
    queryset = {[ model.classname ]}.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    renderer_classes = (Renderer, )
    pagination_class = PageNumberPagination
    {% if list_filter %}
    filter_fields = ({% for field in list_filter -%}'{[ field ]}',{%- endfor %})
    {%- endif %}
    {% if search_fields %}
    search_fields = ({% for field in search_fields -%}'{[ field ]}',{%- endfor %})
    {%- endif %}

    def list(self, request, *args, **kwargs):
        self.serializer_class = {[ model.classname ]}ListSerializer
        return super({[ model.classname ]}ViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        return super({[ model.classname ]}ViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = {[ model.classname ]}DetailSerializer
        return super({[ model.classname ]}ViewSet, self).retrieve(request, *args, **kwargs)
