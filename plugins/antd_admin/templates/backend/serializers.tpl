from rest_framework import serializers
from {[ app_name ]}.models import {[ model.classname ]}


class {[ model.classname ]}ListSerializer(serializers.ModelSerializer):
    {% for field in model.fields.values() -%}
    {% if field.type == 'ManyToManyField' -%}
    {[ field.name ]} = serializers.SerializerMethodField()

    def get_{[ field.name ]}(self, obj):
        return [str(item) for item in obj.{[ field.name ]}.filter()]
    {% endif %}
    {%- endfor %}

    class Meta:
        fields = '__all__'
        model = {[ model.classname ]}


class {[ model.classname ]}CreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = {[ model.classname ]}


class {[ model.classname ]}UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = {[ model.classname ]}


class {[ model.classname ]}DetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = {[ model.classname ]}


class {[ model.classname ]}DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = {[ model.classname ]}
