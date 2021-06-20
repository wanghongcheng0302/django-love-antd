from typing import Optional, List, Union, Dict
from django.db.models import Model, Field, ForeignKey, ManyToManyField
from antd_admin.utils import search_field

from . import BaseParser


class RelatedField(object):

    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '({}, {})'.format(self.model._parent, self.model)


class FieldParser(BaseParser):

    @property
    def name(self):
        return self.get_name()

    @property
    def label(self):
        return self.get_label()

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

    @property
    def is_primary_key(self):
        return self.get_is_primary_key()

    def get_name(self) -> str:
        """
        字段名
        :return:
        """
        return self._data.name

    def get_label(self) -> str:
        """
        字段中文名
        :return:
        """
        return search_field(self._data, ['verbose_name', 'name'])

    def get_max_length(self) -> Optional[int]:
        """
        字段最大长度
        :return:
        """
        return self._data.max_length

    def get_to(self):
        """
        关联的外键
        :return:
        """
        if self._data.related_model:
            return self._data.related_model.__name__

    def get_is_foreignkey(self) -> bool:
        """
        是否是外键
        :return:
        """
        return isinstance(self._data, ForeignKey)

    def get_is_many2many(self) -> bool:
        """
        是否是多对多字段
        :return:
        """
        return isinstance(self._data, ManyToManyField)

    def get_validators(self) -> Optional[List]:
        """
        校验器
        :return:
        """
        return [item.__dict__ for item in self._data.validators]

    def get_editable(self) -> bool:
        """
        是否可编辑
        :return:
        """
        return self._data.editable

    def get_choices(self) -> Optional[List]:
        """
        可选项
        :return:
        """
        return [{'value': item[0], 'label': str(item[1])} for item in
                self._data.choices] if self._data.choices else None

    def get_type(self) -> str:
        """
        字段类型
        :return:
        """
        return str(self._data.__class__.__name__)

    def get_is_primary_key(self) -> bool:
        """
        是否是主键
        :return:
        """
        return self._data.primary_key

    def get_blank(self) -> bool:
        """
        是否必填
        :return:
        """
        return self._data.blank

    def get_help_text(self) -> Optional[str]:
        """
        提示信息
        :return:
        """
        return self._data.help_text

    def get_unique(self) -> bool:
        """
        是否唯一
        :return:
        """
        return getattr(self._data, '_unique', False)

    def get_data(self) -> Optional[Union[List, Dict]]:
        """
        整个字段信息
        :return:
        """
        data = dict()
        data['name'] = self.name
        data['label'] = self.label
        data['max_length'] = self.max_length
        data['to'] = self.to
        data['is_foreignkey'] = self.is_foreignkey
        data['is_many2many'] = self.is_many2many
        data['editable'] = self.editable
        data['choices'] = self.choices
        data['type'] = self.type
        data['is_primary_key'] = self.is_primary_key
        data['blank'] = self.blank
        data['help_text'] = self.help_text
        data['unique'] = self.unique
        data['_parent'] = self._parent
        return data
