import importlib
import copy
import inspect
from functools import singledispatchmethod
from django.apps import AppConfig
from django.db.models import Model, Field
from typing import Union, List, Dict
import os
import json
import yaml
from django.conf import settings


def import_class(name):
    """Import class from string
    e.g. `package.module.ClassToImport` returns the `ClasToImport` class"""
    components = name.split('.')
    module_name = '.'.join(components[:-1])
    class_name = components[-1]
    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    return class_


def search_field(obj, fields: list):
    """
    按优先级查询对象属性
    :param obj:
    :param fields: ['name', 'label', ]
    :return:
    """
    for field in fields:
        try:
            return str(obj.get(field)) if isinstance(obj, dict) else str(getattr(obj, field))
        except AttributeError:
            pass


def get_attr_by_chain(obj, attr_link: str):
    """
    链式查询对象或字典属性
    :param obj:
    :param attr_link: 'field.__dict__.name'
    :return:
    """
    cur_obj = copy.copy(obj)
    for item in attr_link.split('.'):
        cur_obj = cur_obj.get(item) if isinstance(cur_obj, dict) else getattr(cur_obj, item)
        if not cur_obj:
            return None
    return cur_obj


class YamlOption(object):

    def __init__(self, target: str):
        self.target = target

    def __call__(self, func, *args, **kwargs):
        def wrapper(base_class, *args, **kwargs):
            self.instance = base_class._data
            if not func:
                return self.option(self.instance)
            return self.option(self.instance) or func(base_class, *args, **kwargs)

        return wrapper

    @singledispatchmethod
    def option(self, base_class):
        pass

    @option.register(list)
    def _(self, base_class: List[AppConfig]):
        config = os.path.join(settings.BASE_DIR, 'antd.yaml')
        if not os.path.exists(config):
            return None
        with open(config, 'r') as f:
            data = yaml.load(f.read())
            if data:
                return data.get(self.target)

    @option.register(AppConfig)
    def _(self, base_class: AppConfig):
        config = os.path.join(base_class.path, 'antd.yaml')
        if not os.path.exists(config):
            return None
        with open(config, 'r') as f:
            data = yaml.load(f.read())
            if data:
                return data.get(self.target)

    @option.register(Model.__class__)
    def _(self, base_class):
        app_dir = os.path.dirname(inspect.getfile(base_class))
        config = os.path.join(app_dir, 'antd.yaml')
        if not os.path.exists(config):
            return None
        with open(config, 'r') as f:
            data = yaml.load(f.read())
            if data and data.get(base_class.__name__.lower()):
                data = data.get(base_class.__name__.lower())
                return data.get(self.target)

    @option.register(Field)
    def _(self, element: Field):
        pass
