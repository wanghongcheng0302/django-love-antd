import unittest
import os
import django


class JinjaTestCase(unittest.TestCase):

    def setUp(self) -> None:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
        django.setup()

    def test_jinja_loader(self):
        """
        测试自定义jinja2 loader
        :return:
        """

