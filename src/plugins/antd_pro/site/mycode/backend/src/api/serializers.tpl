from rest_framework import serializers
{% for model in schema %}
from {[ model.module ]} import {[ model.classname ]}
{% endfor %}


{% for model in schema %}
class {[ model.classname ]}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {[ model.classname ]}
        fields = '__all__'


class {[ model.classname ]}FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = {[ model.classname ]}
        fields = '__all__'


{% endfor %}