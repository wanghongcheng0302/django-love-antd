__doc__ = """抽象数据层
"""

from antd_pro.utils.utils import search_field
from abc import abstractmethod
from django.db.models import Field, ForeignKey, ManyToManyField


class Schema:
    schemas = []

    @property
    def data(self):
        return self.get_data()

    @abstractmethod
    def get_data(self):
        pass


class FieldSchema(Schema):

    def __init__(self, field, model):
        self._field = field
        self._model = model

    def get_name(self) -> str:
        """
        字段名
        """
        return self._field.name

    def get_label(self) -> str:
        """
        字段中文名
        """
        return search_field(self._field, ['verbose_name', 'name'])

    def get_max_length(self):
        """
        字段最大长度
        """
        return self._field.max_length

    def get_to(self):
        """
        关联外键
        todo: 采用装饰器可能无法获取
        """
        return self._field.related_model

    def get_is_foreignkey(self) -> bool:
        """
        是否外键
        """
        return isinstance(self._field, ForeignKey)

    def get_is_many2many(self) -> bool:
        """
        是否是多对多字段
        """
        return isinstance(self._field, ManyToManyField)

    def get_validators(self):
        """
        校验器
        """
        return [item.__dict__ for item in self._field.validators]

    def get_editable(self) -> bool:
        """
        是否可编辑
        """
        return self._field.editable

    def get_choices(self):
        """
        选项
        """
        return [{'value': item[0], 'label': str(item[1])} for item in
                self._field.choices] if self._field.choices else None

    def get_type(self) -> str:
        """
        字段类型
        """
        return str(self._field.__class__.__name__)

    def get_is_primary_key(self) -> bool:
        """
        是否主键
        """
        return self._field.primary_key

    def get_blank(self) -> bool:
        """
        是否必填
        """
        return self._field.blank

    def get_help_text(self):
        """
        提示信息
        """
        return self._field.help_text

    def get_unique(self) -> bool:
        """
        是否唯一
        """
        return getattr(self._field, '_unique', False)

    def get_auto_now(self) -> bool:
        """
        更新时更新
        """
        return getattr(self._field, 'auto_now', False)

    def get_auto_now_add(self) -> bool:
        """
        创建时更新
        """
        return getattr(self._field, 'auto_now_add', False)

    def get_auto_created(self) -> bool:
        """
        自动创建
        """
        return getattr(self._field, 'auto_created', False)

    def get_data(self):
        data = dict()
        data['name'] = self.get_name()
        data['label'] = self.get_label()
        data['max_length'] = self.get_max_length()
        data['to'] = self.get_to()
        data['is_foreignkey'] = self.get_is_foreignkey()
        data['is_many2many'] = self.get_is_many2many()
        data['editable'] = self.get_editable()
        data['choices'] = self.get_choices()
        data['type'] = self.get_type()
        data['is_primary_key'] = self.get_is_primary_key()
        data['blank'] = self.get_blank()
        data['help_text'] = self.get_help_text()
        data['unique'] = self.get_unique()
        data['auto_created'] = self.get_auto_created()
        data['auto_now_add'] = self.get_auto_now_add()
        data['auto_now'] = self.get_auto_now()
        return data

    def __str__(self):
        return '{}'.format(self.data)


class ModelSchema(Schema):
    def __init__(self, **kwargs):
        self.options = kwargs

    def __call__(self, model, *args, **kwargs):
        self._model = model
        # 惰性加载数据，等待app注册
        self.schemas.append(self)
        return model(*args, **kwargs)

    def get_module(self):
        """
        模块
        """
        return self._model.__module__

    def get_name(self) -> str:
        """
        表名称
        """
        return self._model.__name__.lower()

    def get_label(self) -> str:
        """
        表中文名称
        """
        _meta = getattr(self._model, '_meta').__dict__
        return search_field(_meta, ['verbose_name', 'name'])

    def get_list_display(self):
        """
        列表显示字段
        """
        return getattr(self.options, 'list_display', None)

    def get_classname(self):
        """
        类名
        """
        return self._model.__name__

    def get_search_fields(self):
        """
        支持查询的字段
        """
        return getattr(self.options, 'search_fields', None)

    def get_list_filter(self):
        """
        支持过滤的字段
        """
        return getattr(self.options, 'list_filter', None)

    def get_list_editable(self):
        """
        可编辑的字段
        """
        return getattr(self.options, 'list_editable', None)

    def get_list_readonly(self):
        """
        只读字段
        """
        return getattr(self.options, 'list_readonly', None)

    def get_fields(self) -> dict:
        """
        所有字段
        """
        fields = set()
        for field_name in dir(self._model):
            try:
                field = getattr(self._model, field_name).field
                if not isinstance(field, Field):
                    continue
                if field in fields:
                    continue
                if field.model is not self._model and field.remote_field:
                    continue
                fields.add(field)
            except AttributeError:
                pass
        return {field.name.lower(): FieldSchema(field=field, model=self._model).data for field in fields}

    def get_data(self):
        data = dict()
        data.update(self.options)
        data['name'] = self.get_name()
        data['label'] = self.get_label()
        data['list_display'] = self.get_list_display()
        data['search_fields'] = self.get_search_fields()
        data['list_filter'] = self.get_list_filter()
        data['list_editable'] = self.get_list_editable()
        data['list_readonly'] = self.get_list_readonly()
        data['classname'] = self.get_classname()
        data['fields'] = self.get_fields()
        data['module'] = self.get_module()

        return data

    def __str__(self):

        return '{}'.format(self.data)
