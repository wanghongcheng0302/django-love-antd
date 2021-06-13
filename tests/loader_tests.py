import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

django.setup()

import unittest
from antd_admin.loader import Loader


class LoaderTestCase(unittest.TestCase):

    def test_loader(self):
        loader = Loader()
        loader.compile()
