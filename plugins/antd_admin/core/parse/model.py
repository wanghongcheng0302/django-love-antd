from . import BaseParser
from typing import Optional, List, Dict
from .field import FieldParser
from django.apps import AppConfig
from django.db.models import Model


class ModelParser(BaseParser):

    def __init__(self, app: AppConfig, model: Model):
        self.app = app
        self.model = model

    @property
    def name(self):
        return self.get_name()

    @property
    def label(self):
        return self.get_label()

    @property
    def meta(self):
        return self.get_meta()

    @property
    def list_display(self):
        return self.get_list_display()

    @property
    def search_fields(self):
        return self.get_search_fields()

    @property
    def list_filter(self):
        return self.get_list_filter()

    @property
    def list_editable(self):
        return self.get_list_editable()

    @property
    def list_readonly(self):
        return self.list_readonly()

    @property
    def fields(self):
        return self.get_fields()

    def get_meta(self) -> dict:
        pass

    def get_name(self) -> str:
        pass

    def get_label(self) -> str:
        pass

    def get_list_display(self) -> Optional[List]:
        pass

    def get_search_fields(self) -> Optional[List]:
        pass

    def get_list_filter(self) -> Optional[List]:
        pass

    def get_list_editable(self) -> Optional[List]:
        pass

    def get_list_readonly(self) -> Optional[List]:
        pass

    def get_fields(self) -> Optional[List[FieldParser]]:
        pass
