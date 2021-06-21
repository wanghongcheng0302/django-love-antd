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
    path('backend/{[ app.name ]}/{[ model.name ]}/', {[ model.classname ]}ViewSet.as_view({'get':'list'})),
    path('backend/{[ app.name ]}/{[ model.name ]}/', {[ model.classname ]}ViewSet.as_view({'post':'create'})),
    path('backend/{[ app.name ]}/{[ model.name ]}/<int:pk>/', {[ model.classname ]}ViewSet.as_view({'delete':'destroy'})),
    path('backend/{[ app.name ]}/{[ model.name ]}/<int:pk>/', {[ model.classname ]}ViewSet.as_view({'put':'update'})),
    path('backend/{[ app.name ]}/{[ model.name ]}/<int:pk>', {[ model.classname ]}ViewSet.as_view({'get':'retrieve'})),

    {% endfor %}
    {% endfor %}
]