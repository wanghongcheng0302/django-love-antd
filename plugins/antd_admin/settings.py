from django.conf import settings
import os

ANTD_DIST_PATH = os.path.join(settings.BASE_DIR, 'dist', 'ant-design-pro')

ANTD_APP = []

PRIVATE_APP_PATH = os.path.dirname(__file__)

PRIVATE_TEMPLATE_PATH = os.path.join(PRIVATE_APP_PATH, 'templates')

PRIVATE_RESOURCE_PATH = os.path.join(PRIVATE_APP_PATH, 'resources', 'ant-design-pro')
