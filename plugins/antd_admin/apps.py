from django.apps import AppConfig


class AntdAdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'antd_admin'

    def ready(self):
        from .enforcer import initialize_enforcer
        initialize_enforcer()
