from antd_admin import settings
from jinja2 import FileSystemLoader, Environment
from django.conf import settings as django_settings
from .convert.filter import django_convert_typescript, django_to_protable, capitalize
import os


class Renderer:
    """
    渲染器，输出路径，模板路径、前端源码路径
    """
    dist_path = settings.ANTD_DIST_PATH
    tpl_path = settings.PRIVATE_TEMPLATE_PATH
    resource_path = settings.PRIVATE_RESOURCE_PATH
    dist_backend_path = os.path.join(django_settings.BASE_DIR, 'backend')

    if not os.path.exists(dist_backend_path):
        os.makedirs(dist_backend_path)

    loader = FileSystemLoader(settings.PRIVATE_TEMPLATE_PATH)
    env = Environment(loader=loader)
    env.variable_start_string = '{[ '
    env.variable_end_string = ' ]}'
    env.filters['django_convert_typescript'] = django_convert_typescript
    env.filters['django_to_protable'] = django_to_protable
    env.filters['capitalize'] = capitalize
