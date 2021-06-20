from abc import ABCMeta, abstractmethod
from typing import Optional, List, Dict, Union
from antd_admin.utils import YamlOption, Register


class BaseParser(metaclass=ABCMeta):

    def __init__(self, data, parent=None):
        self._data = data
        self._parent = parent

    @property
    def data(self):
        return self.get_data()

    @abstractmethod
    def get_data(self) -> Optional[Union[List, Dict]]:
        pass
