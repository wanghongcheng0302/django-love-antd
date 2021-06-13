from . import BaseParser, YamlOption
from .app import AppParser
from typing import Optional, List, Union, Dict


class SiteParser(BaseParser):

    @property
    def apps(self):
        return self.get_apps()

    @property
    def title(self):
        return self.get_title()

    @property
    def copyright(self):
        return self.get_copyright()

    @property
    def icon(self):
        return self.get_icon()

    @YamlOption(target='title')
    def get_title(self) -> str:
        pass

    @YamlOption(target='copyright')
    def get_copyright(self) -> str:
        pass

    @YamlOption(target='icon')
    def get_icon(self) -> str:
        pass

    def get_apps(self) -> dict:
        return {app.name: AppParser(data=app).data for app in self._data}

    def get_data(self) -> Optional[Union[List, Dict]]:
        data = dict()
        data['title'] = self.title
        data['copyright'] = self.copyright
        data['icon'] = self.icon
        data['apps'] = self.apps
        return data
