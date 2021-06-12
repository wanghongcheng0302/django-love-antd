from . import BaseParser
from django.apps import AppConfig
from typing import Optional, List
from .model import ModelParser


class AppParser(BaseParser):

    def __init__(self, app: AppConfig):
        self.app = app

    @property
    def name(self):
        return self.get_name()

    @property
    def label(self):
        return self.label

    @property
    def models(self):
        return self.models

    def get_name(self) -> str:
        pass

    def get_label(self) -> str:
        pass

    def get_models(self) -> Optional[List[ModelParser]]:
        pass
