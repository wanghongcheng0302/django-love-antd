__doc__ = """组件
作为上层应用，被composer调用
"""

from antd_pro.mixins.render import RenderMixin


class Component(RenderMixin):

    def __init__(self, schema):
        self.schema = schema


class CopyComponent(Component):

    def __init__(self, files: list):
        super(CopyComponent, self).__init__(schema=None)
        self.files = files

    def write(self, *args, **kwargs):
        """
        重载
        """
        print(self.files)
