import casbin
from antd_pro.settings import settings

e = casbin.Enforcer(settings.get('ANTD_CASBIN_MODEL'), settings.get('ANTD_CASBIN_RULE'))