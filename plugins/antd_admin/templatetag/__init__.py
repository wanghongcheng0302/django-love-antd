from abc import ABCMeta, abstractmethod
from antd_admin.core.render import Renderer


class BaseTemplateTag(metaclass=ABCMeta):
    render = Renderer()

    def __init__(self, data):
        self.data = data

    @abstractmethod
    def write(self):
        pass
