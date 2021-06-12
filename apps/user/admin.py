from django.contrib import admin
from django.apps import apps
from django.db.models import Model
models = apps.get_models()

for model in models:
    try:
        if issubclass(model, (Model, )):
            search_fields = getattr(model, 'search_fields', None)
            list_display = getattr(model, 'list_display', None)
            list_filter = getattr(model, 'list_filter', None)
            model_name = str(model._meta.model_name).capitalize()
            _m = [field.name for field in model._meta.fields if field.name != 'url']

            options = dict()
            if search_fields:
                options['search_fields'] = search_fields
            if list_filter:
                options['list_filter'] = list_filter
            if list_display:
                options['list_display'] = list_display
            else:
                options['list_display'] = _m
            _q = type('{}Admin'.format(model_name), (admin.ModelAdmin,), options)
            admin.site.register(model, _q)
    except Exception as e:
        # print(e)
        pass
