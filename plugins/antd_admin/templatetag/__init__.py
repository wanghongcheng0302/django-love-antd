from abc import ABCMeta, abstractmethod
from antd_admin.core.render import Renderer


class _BaseTemplateTag(type):

    def __new__(cls, *args, **kwargs):
        return type(*args, **kwargs)


class BaseTemplateTag(metaclass=_BaseTemplateTag):
    render = Renderer()

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def write(self):
        pass
