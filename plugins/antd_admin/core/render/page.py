from . import BaseRenderer
from antd_admin import settings
import os


class ListPageRenderer(BaseRenderer):
    list_page_tpl = os.path.join('frontend', 'pages', 'list.tpl')

    @property
    def template(self):
        return self.env.get_template(self.list_page_tpl)

    def get_content(self, data):
        pass

    def write(self, data):
        conetnt = self.get_content(data)

        print('ListPageRenderer 输出列表渲染后的内容')


class CreatePageRenderer(BaseRenderer):
    pass


class UpdatePageRenderer(BaseRenderer):
    pass


class DetailPageRenderer(BaseRenderer):
    pass


class ConstantPageRenderer(BaseRenderer):
    pass
