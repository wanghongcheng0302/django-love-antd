from django.apps import AppConfig
from .enforcer import initialize_enforcer
from . import settings
from django.conf import settings as django_settings


class AntdAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'antd_admin'

    def ready(self):
        initialize_enforcer()

        antd_attrs = [attr for attr in dir(settings) if 'ANTD' in attr]
        for attr in antd_attrs:
            if hasattr(django_settings, attr) and getattr(django_settings, attr):
                setattr(settings, attr, getattr(django_settings, attr))

