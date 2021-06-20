import os
import shutil
from typing import Optional, List
from . import BaseTemplateTag


class CommonFilesTemplateTag(BaseTemplateTag):

    def clear(self):
        """
        移除当前目录
        :return:
        """
        shutil.rmtree(os.path.join(self.render.dist_path, 'ant-design-pro'))

    def write(self):
        """
        拷贝公共文件到指定目录
        :return:
        """
        for root, _dirs, _files in os.walk(self.render.resource_path):
            for file in _files:
                src = os.path.join(root, file)
                dst = src.replace(self.render.resource_path, self.render.dist_path)
                _dir = os.path.dirname(dst)
                if not os.path.exists(_dir):
                    os.makedirs(_dir)
                shutil.copyfile(src, dst)


class ListTemplateTag(BaseTemplateTag):
    tpl_path = os.path.join('frontend', 'pages', 'list.tpl')

    def get_search_input(self):
        """
        搜索组件
        :return:
        """

    def get_filter_inputs(self):
        """
        过滤组件
        :return:
        """

    def get_content(self):
        """
        渲染页面
        :return:
        """

    def get_table(self):
        """
        表格
        :return:
        """

    def get_pagination(self):
        """
        分页器
        :return:
        """

    def write(self):
        """
        写入文件
        :return:
        """


class CreateTemplateTag(BaseTemplateTag):

    def get_form(self) -> str:
        """
        表单
        :return:
        """

    def write(self):
        """
        写入文件
        :return:
        """


class UpdateTemplateTag(BaseTemplateTag):

    def get_form(self) -> str:
        """
        表单
        :return:
        """

    def write(self):
        """
        写入文件
        :return:
        """


class DetailTemplateTag(BaseTemplateTag):

    def get_profile(self) -> str:
        """
        详情
        :return:
        """

    def write(self):
        """
        写入文件
        :return:
        """
