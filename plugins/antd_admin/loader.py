from django.apps import apps
from .core.parse.site import SiteParser
from .core.render.page import ListPageRenderer, UpdatePageRenderer, CreatePageRenderer, DetailPageRenderer
from . import settings
import json


class Loader(object):

    def __init__(self):
        self.apps = [app for app in apps.get_app_configs() if app.name in settings.ANTD_APP]

    def compile(self):
        # 解析数据
        data = SiteParser(data=self.apps).data
        print(data)
        print(json.dumps(data))

        # 动态创建list page，使用元类

        # 动态创建create page

        #  动态创建update page

        # 动态创建detail page
