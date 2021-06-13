from rest_framework import serializers


class BaseSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    def is_valid(self, raise_exception=True):
        return super(BaseSerializer, self).is_valid(raise_exception=raise_exception)
