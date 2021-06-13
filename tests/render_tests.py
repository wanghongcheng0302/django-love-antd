import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

django.setup()

import unittest
from antd_admin.core.render.constant import ConstantRenderer


class RenderTestCase(unittest.TestCase):

    def test_render_constant(self):
        pass
