from . import BaseTemplateTag
import os
from django.conf import settings


class SerializerTemplateTag(BaseTemplateTag):
    serializer_tpl = os.path.join('backend', 'serializers.tpl')

    def get_content(self, model):
        """

        :param model:
        :return:
        """
        template = self.render.env.get_template(self.serializer_tpl)
        content = template.render(model=model, app_name=model['_parent']._data.name)
        return content

    def write(self):
        """

        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_content(model_info)
                model_dir = os.path.join(self.render.dist_backend_path, 'serializers')
                if not os.path.exists(model_dir):
                    os.makedirs(model_dir)
                with open(os.path.join(model_dir, '{}.py'.format(model_name)), 'w') as f:
                    f.write(content)


class UrlTemplateTag(BaseTemplateTag):
    urls_tpl = os.path.join('backend', 'urls.tpl')

    def get_content(self, model):
        """

        :param model:
        :return:
        """
        template = self.render.env.get_template(self.urls_tpl)
        content = template.render(apps=self.data.get('apps'))
        return content

    def write(self):
        """

        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_content(model_info)
                with open(os.path.join(self.render.dist_backend_path, 'urls.py'), 'w') as f:
                    f.write(content)


class ViewSetTemplateTag(BaseTemplateTag):
    viewsets_tpl = os.path.join('backend', 'viewsets.tpl')

    def get_content(self, model):
        """

        :param model:
        :return:
        """
        template = self.render.env.get_template(self.viewsets_tpl)
        content = template.render(model=model, app_name=model['_parent']._data.name)
        return content

    def write(self):
        """

        :return:
        """
        apps = self.data.get('apps')
        for app_name, app_info in apps.items():
            models = app_info.get('models')
            for model_name, model_info in models.items():
                content = self.get_content(model_info)
                model_dir = os.path.join(self.render.dist_backend_path, 'viewsets')
                if not os.path.exists(model_dir):
                    os.makedirs(model_dir)
                with open(os.path.join(model_dir, '{}.py'.format(model_name)), 'w') as f:
                    f.write(content)
