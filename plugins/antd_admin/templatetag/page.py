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
    datad_tpl = os.path.join('frontend', 'pages', 'data.d.tpl')
    service_tpl = os.path.join('frontend', 'pages', 'service.tpl')
    list_tpl = os.path.join('frontend', 'pages', 'list.tpl')

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

    def get_datad(self, model):
        """
        datad
        :return:
        """
        template = self.render.env.get_template(self.datad_tpl)
        content = template.render(model=model, pageConfig=self.data.get('pageConfig'))
        return content

    def get_service(self, model):
        """
        service
        :return:
        """
        template = self.render.env.get_template(self.service_tpl)
        content = template.render(model=model, app_name=model['_parent']._data.name)
        return content

    def get_list(self, model):
        template = self.render.env.get_template(self.list_tpl)
        content = template.render(model=model, app_name=model['_parent']._data.name)
        return content

    def write(self):
        """
        写入文件
        :return:
        """
        self.write_datad()
        self.write_service()
        self.write_list()

    def write_datad(self):
        """
        datad
        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_datad(model_info)
                output = os.path.join(self.render.dist_path, 'src', 'pages',app_name,  model_name)
                if not os.path.exists(output):
                    os.makedirs(output)
                with open(os.path.join(output, 'data.d.ts'), 'w') as f:
                    f.write(content)

    def write_service(self):
        """
        service
        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_service(model_info)
                output = os.path.join(self.render.dist_path, 'src', 'pages', app_name, model_name)
                if not os.path.exists(output):
                    os.makedirs(output)
                with open(os.path.join(output, 'service.ts'), 'w') as f:
                    f.write(content)

    def write_list(self):
        """
        list
        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_list(model_info)
                output = os.path.join(self.render.dist_path, 'src', 'pages', app_name, model_name)
                if not os.path.exists(output):
                    os.makedirs(output)
                with open(os.path.join(output, 'index.tsx'), 'w') as f:
                    f.write(content)


class CreateTemplateTag(BaseTemplateTag):

    create_tpl = os.path.join('frontend', 'pages', 'create.tpl')

    def get_form(self, model) -> str:
        """
        表单
        :return:
        """
        template = self.render.env.get_template(self.create_tpl)
        content = template.render(model=model, app_name=model['_parent']._data.name)
        return content

    def write(self):
        """
        写入文件
        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_form(model_info)
                output = os.path.join(self.render.dist_path, 'src', 'pages', app_name, model_name)
                if not os.path.exists(output):
                    os.makedirs(output)
                with open(os.path.join(output, 'create.tsx'), 'w') as f:
                    f.write(content)


class UpdateTemplateTag(BaseTemplateTag):
    update_tpl = os.path.join('frontend', 'pages', 'update.tpl')

    def get_form(self, model) -> str:
        """
        表单
        :return:
        """
        template = self.render.env.get_template(self.update_tpl)
        content = template.render(model=model, app_name=model['_parent']._data.name)
        return content

    def write(self):
        """
        写入文件
        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_form(model_info)
                output = os.path.join(self.render.dist_path, 'src', 'pages', app_name, model_name)
                if not os.path.exists(output):
                    os.makedirs(output)
                with open(os.path.join(output, 'update.tsx'), 'w') as f:
                    f.write(content)


class DetailTemplateTag(BaseTemplateTag):
    detail_tpl = os.path.join('frontend', 'pages', 'detail.tpl')

    def get_profile(self, model) -> str:
        """
        详情
        :return:
        """
        template = self.render.env.get_template(self.detail_tpl)
        content = template.render(model=model, app_name=model['_parent']._data.name)
        return content

    def write(self):
        """
        写入文件
        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_profile(model_info)
                output = os.path.join(self.render.dist_path, 'src', 'pages', app_name, model_name)
                if not os.path.exists(output):
                    os.makedirs(output)
                with open(os.path.join(output, 'detail.tsx'), 'w') as f:
                    f.write(content)
