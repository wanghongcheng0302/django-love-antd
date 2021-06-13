import os

from typing import Optional, List
from . import BaseTemplateTag


class CommonFilesTemplateTag(BaseTemplateTag):

    def write(self):
        """
        拷贝公共文件到指定目录
        :return:
        """
        pass


class ListTemplateTag(BaseTemplateTag):
    tpl_path = os.path.join('frontend', 'pages', 'list.tpl')

    @property
    def search_input(self) -> Optional[str]:
        """
        搜索，根据keywords
        :return:
        """
        return self.get_search_input()

    @property
    def filter_inputs(self) -> Optional[List[str]]:
        """
        过滤器，choices\many2many\bool
        :return:
        """
        return self.get_filter_inputs()

    @property
    def content(self):
        """
        整页渲染结果
        :return:
        """
        return self.get_content()

    def get_search_input(self):
        pass

    def get_filter_inputs(self):
        pass

    def get_content(self):
        pass

    def write(self):
        pass


class CreateTemplateTag(BaseTemplateTag):

    @property
    def form(self):
        return self.get_form()

    def get_form(self) -> str:
        pass

    def write(self):
        pass


class UpdateTemplateTag(BaseTemplateTag):

    @property
    def form(self):
        return self

    def get_form(self) -> str:
        pass

    def write(self):
        pass


class DetailTemplateTag(BaseTemplateTag):

    @property
    def profile(self):
        return self.get_profile()

    def get_profile(self) -> str:
        pass

    def write(self):
        pass
