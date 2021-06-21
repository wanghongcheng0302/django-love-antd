from django.apps import apps
from antd_admin.templatetag.page import (
    CommonFilesTemplateTag,
    ListTemplateTag,
    CreateTemplateTag,
    UpdateTemplateTag,
    DetailTemplateTag,
)
from antd_admin.templatetag.drf import SerializerTemplateTag, ViewSetTemplateTag, UrlTemplateTag
from antd_admin.templatetag.route import RouteTemplateTag
from antd_admin.templatetag.redux import ReduxTemplateTag
from antd_admin.templatetag.service import ServiceTemplateTag
from .core.parse.site import SiteParser
from . import settings


class Compiler:
    """
    代码生成器
    """

    def __init__(self):
        self.apps = [
            app for app in apps.get_app_configs() if app.name in settings.ANTD_APP
        ]

    def compile(self):
        """
        编译model，生成前后端代码
        :return:
        """
        data = SiteParser(data=self.apps).data
        print(data)

        CommonFilesTemplateTag(data=data).write()

        RouteTemplateTag(data=data).write()

        ListTemplateTag(data=data).write()

        CreateTemplateTag(data=data).write()

        UpdateTemplateTag(data=data).write()

        DetailTemplateTag(data=data).write()

        ServiceTemplateTag(data=data).write()

        ReduxTemplateTag(data=data).write()

        SerializerTemplateTag(data=data).write()

        ViewSetTemplateTag(data=data).write()

        UrlTemplateTag(data=data).write()
