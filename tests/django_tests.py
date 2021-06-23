import os
import django
import unittest
from django.apps import apps


class DjangoTestCase(unittest.TestCase):
    def setUp(self) -> None:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
        django.setup()

    def test_(self):
        from antd_admin.loader import Compiler
        # apps.get_app_config()
        from user.models import Role
        # print(Role._meta.app_config)
        # print(Role.__dict__)
        # return
        loader = Compiler()
        loader.compile()
