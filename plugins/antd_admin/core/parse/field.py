from typing import Optional, List
from django.apps import AppConfig
from django.db.models import Model, Field

from . import BaseParser


class RelatedField(object):

    def __init__(self, app: AppConfig, model: Model):
        self.app = app
        self.model = model

    def __str__(self):
        return '({}, {})'.format(self.app.name, self.model.__name__)


class FieldParser(BaseParser):

    def __init__(self, app: AppConfig, model: Model, field: Field):
        self.app = app
        self.model = model
        self.field = Field

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
    def max_length(self):
        return self.get_max_length()

    @property
    def to(self):
        return self.get_to()

    @property
    def is_foreignkey(self):
        return self.get_is_foreignkey()

    @property
    def is_many2many(self):
        return self.get_is_many2many()

    @property
    def validators(self):
        return self.get_validators()

    @property
    def editable(self):
        return self.get_editable()

    @property
    def choices(self):
        return self.get_choices()

    @property
    def type(self):
        return self.get_type()

    @property
    def primary_key(self):
        return self.get_is_primary_key()

    @property
    def unique(self):
        return self.get_unique()

    @property
    def blank(self):
        return self.get_blank()

    @property
    def help_text(self):
        return self.get_help_text()

    def get_name(self) -> str:
        pass

    def get_label(self) -> str:
        pass

    def get_max_length(self) -> Optional[int]:
        pass

    def get_to(self) -> Optional[RelatedField]:
        pass

    def get_is_foreignkey(self) -> bool:
        pass

    def get_is_many2many(self) -> bool:
        pass

    def get_validators(self) -> Optional[List]:
        pass

    def get_editable(self) -> bool:
        pass

    def get_choices(self) -> Optional[List]:
        pass

    def get_type(self) -> str:
        pass

    def get_is_primary_key(self) -> bool:
        pass

    def get_blank(self) -> bool:
        pass

    def get_help_text(self) -> Optional[str]:
        pass

    def get_unique(self) -> bool:
        pass

    def get_meta(self) -> dict:
        pass