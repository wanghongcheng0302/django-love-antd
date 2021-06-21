from . import BaseParser, YamlOption, Register
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
        """
        网站标题
        :return:
        """

    @YamlOption(target='copyright')
    def get_copyright(self) -> str:
        """
        版权说明
        :return:
        """

    @YamlOption(target='icon')
    def get_icon(self) -> str:
        """
        icon
        :return:
        """

    @YamlOption(target='pageConfig')
    def get_pageconfig(self):
        """
        分页参数
        :return:
        """
        page_config = dict()
        page_config['totalParam'] = 'count'
        page_config['pageSizeParam'] = 'pageSize'
        page_config['pageNumParam'] = 'pageNum'
        page_config['searchParam'] = 'keyWords'

    @Register()
    def get_apps(self) -> dict:
        """
        所有app
        :return:
        """
        return {app.name: AppParser(data=app, parent=self).data for app in self._data}

    def get_data(self) -> Optional[Union[List, Dict]]:
        """
        整合网站信息
        :return:
        """
        data = dict()
        data['title'] = self.title
        data['copyright'] = self.copyright
        data['icon'] = self.icon
        data['apps'] = self.apps
        return data
