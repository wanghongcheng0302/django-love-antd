from django.conf import settings as _settings
import copy
import os


class DefaultSettings:
    ANTD_DIST = os.path.join(_settings.BASE_DIR, 'dist')
    ANTD_CASBIN_MODEL = os.path.join(os.path.dirname(__file__), 'resources', 'casbin.conf')


class SettingsMetaClass:
    __user_settings = DefaultSettings()

    def __call__(self, *args, **kwargs):
        if self.__user_settings is None:
            self.__user_settings = object()
            # self.__user_settings = copy.deepcopy(self.default_settings)
            for attr, value in self.default_settings.items():
                print(attr, value)
                setattr(self.__user_settings, attr, value)
        return self.__user_settings

    def __getattr__(self, attr):
        if attr not in self.user_settings:
            raise AttributeError('Invalid antd setting: %s' % attr)
        try:
            val = self.user_settings.get(attr)
        except KeyError:
            val = self.defaults.get(attr)
        return val


class Settings:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = DefaultSettings()
            config = getattr(_settings, 'ANTD', None)
            if not config or not isinstance(config, dict):
                raise AttributeError
            for k, v in config.items():
                setattr(cls.__instance, k, v)
        return cls.__instance

    def __getattr__(self, attr):
        if attr not in self.user_settings:
            raise AttributeError('Invalid antd setting: %s' % attr)
        try:
            val = self.user_settings.get(attr)
        except KeyError:
            val = self.defaults.get(attr)
        return val


settings = Settings()

s1 = Settings()
s2 = Settings()
