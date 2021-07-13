from antd_pro.globals import env
import os
from jinja2 import Template
from antd_pro.settings import settings
from antd_pro.utils.utils import get_dirname_template, makepackages
import sys
import inspect


class RenderMixin:
    """
    让组件具备代码生成的能力
    """

    jinja_env = env
    dist = getattr(settings, 'ANTD_DIST')

    def get_code(self):
        schema = getattr(self, 'schema')
        if isinstance(schema, list):
            schema = [item.data for item in schema]
        return self.template.render(schema=schema)

    def get_template(self) -> Template:
        mod = sys.modules[self.__class__.__module__]
        path = inspect.getsourcefile(mod)
        return get_dirname_template(path)

    def write(self, relative_path):
        path = os.path.join(self.dist, relative_path)
        dirname = os.path.dirname(path)
        if not os.path.exists(dirname):
            makepackages(dirname)
            # os.makedirs(dirname)
        with open(path, 'w') as f:
            f.write(self.code)

    @property
    def code(self):
        return self.get_code()

    @property
    def template(self):
        return self.get_template()
