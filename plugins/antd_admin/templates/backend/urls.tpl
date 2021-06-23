from django.urls import path
{% for app in apps.values() -%}
{% for model in app.models.values() -%}
from .viewsets.{[ model.name ]} import {[ model.classname ]}ViewSet
{% endfor %}
{% endfor -%}

urlpatterns = [
    {% for app in apps.values() %}
    {% for model in app.models.values() -%}
    # {[ model.label ]}
    path('{[ app.name ]}/{[ model.name ]}/', {[ model.classname ]}ViewSet.as_view({'get':'list', 'post': 'create'})),
    path('{[ app.name ]}/{[ model.name ]}/<int:pk>/', {[ model.classname ]}ViewSet.as_view({'delete':'destroy', 'put':'update', 'get':'retrieve'})),

    {% endfor %}
    {% endfor %}
]