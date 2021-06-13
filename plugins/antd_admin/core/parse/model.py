from . import BaseParser
from typing import Optional, List, Dict, Union
from .field import FieldParser
from django.db.models import Model, Field
from . import YamlOption
from ...utils import search_field


class ModelParser(BaseParser):

    @property
    def name(self):
        return self.get_name()

    @property
    def label(self):
        return self.get_label()

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
        return self.get_list_readonly()

    @property
    def fields(self):
        return self.get_fields()

    @YamlOption(target='name')
    def get_name(self) -> str:
        return self._data.__name__.lower()

    @YamlOption(target='label')
    def get_label(self) -> str:
        _meta = getattr(self._data, '_meta').__dict__
        return search_field(_meta, ['verbose_name', 'name'])

    @YamlOption(target='list_display')
    def get_list_display(self) -> Optional[List]:
        pass

    @YamlOption(target='search_fields')
    def get_search_fields(self) -> Optional[List]:
        pass

    @YamlOption(target='list_filter')
    def get_list_filter(self) -> Optional[List]:
        pass

    @YamlOption(target='list_editable')
    def get_list_editable(self) -> Optional[List]:
        pass

    @YamlOption(target='list_readonly')
    def get_list_readonly(self) -> Optional[List]:
        pass

    def get_fields(self) -> dict:
        fields = []
        for item in self._data.__dict__.values():
            if isinstance(item, Field):
                fields.append(item)
            elif hasattr(item, 'field') and getattr(item, 'field'):
                fields.append(getattr(item, 'field'))

        return {field.name.lower(): FieldParser(data=field, parent=self).data for field in fields}

    def get_data(self) -> Optional[Union[List, Dict]]:
        data = dict()
        data['name'] = self.name
        data['label'] = self.label
        data['list_display'] = self.list_display
        data['search_fields'] = self.search_fields
        data['list_filter'] = self.list_filter
        data['list_editable'] = self.list_editable
        data['list_readonly'] = self.list_readonly
        data['fields'] = self.fields

        return data
