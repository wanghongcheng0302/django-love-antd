from abc import ABCMeta, abstractmethod
from typing import Optional, List, Dict, Union
from antd_admin.utils import YamlOption


class BaseParser(metaclass=ABCMeta):

    def __init__(self, data):
        self._data = data

    @property
    def data(self):
        return self.get_data()

    @abstractmethod
    def get_data(self) -> Optional[Union[List, Dict]]:
        pass
