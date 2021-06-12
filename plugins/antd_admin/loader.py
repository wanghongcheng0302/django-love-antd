from django.apps import apps
from .core.parse.site import SiteParser


class Loader(object):

    def __init__(self):
        self.apps = apps.get_app_configs()

    def compile(self):
        pass
