import os
import django
import unittest


class DjangoTestCase(unittest.TestCase):
    def setUp(self) -> None:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
        django.setup()

    def test_(self):
        from antd_admin.loader import Compiler
        # from user.models import Role
        # print(Role.__dict__)
        # return
        loader = Compiler()
        loader.compile()
