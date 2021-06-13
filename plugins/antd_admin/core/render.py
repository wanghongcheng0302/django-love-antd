from antd_admin import settings
from jinja2 import FileSystemLoader, Environment


class Renderer:
    dist = settings.ANTD_DIST_PATH

    loader = FileSystemLoader(settings.PRIVATE_TEMPLATE_PATH)
    env = Environment(loader=loader)
    env.variable_start_string = '{[ '
    env.variable_end_string = ' ]}'
