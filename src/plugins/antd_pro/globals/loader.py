from jinja2 import BaseLoader, TemplateNotFound
from jinja2 import Environment as _Environment
import os
from antd_pro.utils.filters import namespace_to_blueprint


class Loader(BaseLoader):

    def get_source(self, environment, template: str):
        """
        按文件路径加载模板
        """
        if not os.path.exists(template):
            raise TemplateNotFound(template)
        mtime = os.path.getmtime(template)
        with open(template) as f:
            source = f.read()
        return source, template, lambda: mtime == os.path.getmtime(template)


class Environment(_Environment):

    def __init__(self, *args, **kwargs):
        super(Environment, self).__init__(*args, **kwargs)
        self.variable_start_string = '{[ '
        self.variable_end_string = ' ]}'
        self.add_extension('jinja2.ext.loopcontrols')
        self.add_extension('jinja2.ext.autoescape')
        self.lstrip_blocks = True
        self.trim_blocks = True
        self.filters['namespace_to_blueprint'] = namespace_to_blueprint
