from rest_framework.viewsets import ModelViewSet
{% for model in schema %}
from {[ model.module ]} import {[ model.classname ]}
{% endfor %}
{% for model in schema %}
from .serializers import {[ model.classname ]}Serializer, {[ model.classname ]}FormSerializer
{% endfor %}


{% for model in schema %}
class {[ model.classname ]}ViewSet(ModelViewSet):
    serializer_class = {[ model.classname ]}Serializer
    queryset = {[ model.classname ]}.objects.filter()

    def list(self, request, *args, **kwargs):
        return super({[ model.classname ]}ViewSet, self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.serializer_class = {[ model.classname ]}FormSerializer
        return super({[ model.classname ]}ViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = {[ model.classname ]}FormSerializer
        return super({[ model.classname ]}ViewSet, self).update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super({[ model.classname ]}ViewSet, self).destroy(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super({[ model.classname ]}ViewSet, self).retrieve(request, *args, **kwargs)


{% endfor %}


