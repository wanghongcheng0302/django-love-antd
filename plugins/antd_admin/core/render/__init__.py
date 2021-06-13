from abc import ABCMeta, abstractmethod
from antd_admin import settings
from pathlib import Path
from jinja2 import FileSystemLoader, Environment
import os


class BaseRenderer(metaclass=ABCMeta):
    dist = settings.ANTD_DIST_PATH

    loader = FileSystemLoader(settings.PRIVATE_TEMPLATE_PATH)
    env = Environment(loader=loader)
    env.variable_start_string = '{[ '
    env.variable_end_string = ' ]}'

    @abstractmethod
    def write(self, data):
        pass
