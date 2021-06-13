from abc import abstractmethod


class _FormItemMetaClass(type):
    pass


class FormItem(metaclass=_FormItemMetaClass):

    def __init__(self, data, renderer):
        self._data = data
        self._renderer = renderer

    @abstractmethod
    def write(self):
        pass
