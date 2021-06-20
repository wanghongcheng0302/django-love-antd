from . import BaseParser
from typing import Optional, List, Union, Dict
from .model import ModelParser
from . import YamlOption, Register
from antd_admin.utils import search_field


class AppParser(BaseParser):
    @property
    def name(self):
        return self.get_name()

    @property
    def label(self):
        return self.get_label()

    @property
    def models(self):
        return self.get_models()

    def get_name(self) -> str:
        """
        app名称
        :return:
        """
        return search_field(self._data, ["name"])

    @YamlOption(target="label")
    def get_label(self) -> str:
        """
        app中文名
        :return:
        """
        return search_field(self._data, ["verbose_name", "name"])

    @Register()
    def get_models(self) -> dict:
        """
        app下的models
        :return:
        """
        return {
            model.__name__.lower(): ModelParser(data=model, parent=self).data
            for model in self._data.models.values()
        }

    def get_data(self) -> Optional[Union[List, Dict]]:
        """
        整合app数据
        :return:
        """
        data = dict()
        data["name"] = self.name
        data["label"] = self.label
        data["models"] = self.models
        data["_parent"] = self._parent
        return data
