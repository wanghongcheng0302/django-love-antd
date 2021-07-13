from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    def __init__(self, *args, **kwargs):
        keys = list(self.fields.keys())
        fields = kwargs.get('fields')
        exclude = kwargs.get('exclude')

        if fields:
            for key in keys:
                if key not in fields:
                    try:
                        del self.fields[key]
                    except KeyError:
                        pass
        if exclude:
            for field in exclude:
                try:
                    del self.fields[field]
                except KeyError:
                    pass

        try:
            del kwargs['exclude']
        except KeyError:
            pass
        try:
            del kwargs['fields']
        except KeyError:
            pass
        super(ModelSerializer, self).__init__(*args, **kwargs)

    def is_valid(self, raise_exception=True, fields: tuple = None, exclude: tuple = None):
        keys = list(self.fields.keys())
        if fields:
            for key in keys:
                if key not in fields:
                    del self.fields[key]

        if exclude:
            for field in exclude:
                del self.fields[field]
        super(ModelSerializer, self).is_valid(raise_exception)

    def data_wrap(self, fields: tuple = None, exclude: tuple = None):
        keys = list(self.fields.keys())
        try:
            if fields:
                for key in keys:
                    if key not in fields:
                        del self.fields[key]

            if exclude:
                for field in exclude:
                    del self.fields[field]
        except KeyError:
            pass
        return self.data
