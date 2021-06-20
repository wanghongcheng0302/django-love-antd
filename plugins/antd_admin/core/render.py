from antd_admin import settings
from jinja2 import FileSystemLoader, Environment


class Renderer:
    """
    渲染器，输出路径，模板路径、前端源码路径
    """
    dist_path = settings.ANTD_DIST_PATH
    tpl_path = settings.PRIVATE_TEMPLATE_PATH
    resource_path = settings.PRIVATE_RESOURCE_PATH

    loader = FileSystemLoader(settings.PRIVATE_TEMPLATE_PATH)
    env = Environment(loader=loader)
    env.variable_start_string = '{[ '
    env.variable_end_string = ' ]}'
