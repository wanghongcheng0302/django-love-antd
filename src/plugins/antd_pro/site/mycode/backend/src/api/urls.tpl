from django.urls import path
{% for model in schema %}
from .viewsets import {[ model.classname ]}ViewSet
{% endfor %}


urlpatterns = [
    {% for model in schema %}
    # {[ model.label ]}管理
    path('{[ model.namespace | namespace_to_blueprint ]}/{[ model.name ]}/', {[ model.classname ]}ViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('{[ model.namespace | namespace_to_blueprint ]}/{[ model.name ]}/<int:pk>/', {[ model.classname ]}ViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    {% endfor %}
]