import importlib
import os
from antd_pro.globals import env
from jinja2 import TemplateNotFound
import os
import posixpath as path


def makepackages(name, mode=0o777, exist_ok=False):
    """
    递归创建包
    """
    head, tail = path.split(name)
    if not tail:
        head, tail = path.split(head)
    if head and tail and not path.exists(head):
        try:
            makepackages(head, exist_ok=exist_ok)
        except FileExistsError:
            pass
        cdir = os.curdir
        if isinstance(tail, bytes):
            cdir = bytes(os.curdir, 'ASCII')
        if tail == cdir:  # xxx/newdir/. exists if xxx/newdir exists
            return
    try:
        os.mkdir(name, mode)
        with open(os.path.join(name, '__init__.py'), 'w') as f:
            f.write('')
    except OSError:
        if not exist_ok or not path.isdir(name):
            raise


def get_dirname_template(path: str):
    """
    获取同级模板
    """
    dirname = os.path.dirname(path)
    filename = os.path.split(path)[-1].split('.')[0]
    template = os.path.join(dirname, '{}.tpl'.format(filename))
    if not os.path.exists(template):
        raise TemplateNotFound(template)
    return env.get_template(template)


def search_field(obj, fields: list):
    """
    字段搜索
    """
    for field in fields:
        if isinstance(obj, dict):
            if obj.get(field):
                return obj.get(field)
        else:
            if hasattr(obj, field):
                return getattr(obj, field)


def import_class(name):
    """Import class from string
    e.g. `package.module.ClassToImport` returns the `ClasToImport` class"""
    components = name.split('.')
    module_name = '.'.join(components[:-1])
    class_name = components[-1]
    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    return class_
