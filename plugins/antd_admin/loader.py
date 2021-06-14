from django.apps import apps
from .core.parse.site import SiteParser
from . import settings
from antd_admin.templatetag.page import CommonFilesTemplateTag, ListTemplateTag, CreateTemplateTag, UpdateTemplateTag, \
    DetailTemplateTag
from antd_admin.templatetag.route import RouteTemplateTag
from antd_admin.templatetag.redux import ReduxTemplateTag
from antd_admin.templatetag.service import ServiceTemplateTag
import json


class Loader(object):

    def __init__(self):
        self.apps = [app for app in apps.get_app_configs() if app.name in settings.ANTD_APP]

    def compile(self):
        # 解析数据
        data = SiteParser(data=self.apps).data
        print(data)
        # print(json.dumps(data))

        CommonFilesTemplateTag(data=data).write()

        RouteTemplateTag(data=data).write()

        ListTemplateTag(data=data).write()

        CreateTemplateTag(data=data).write()

        UpdateTemplateTag(data=data).write()

        DetailTemplateTag(data=data).write()

        ServiceTemplateTag(data=data).write()

        ReduxTemplateTag(data=data).write()
