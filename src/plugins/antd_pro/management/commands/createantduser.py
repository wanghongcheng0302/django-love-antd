__doc__ = """创建ant design pro超管用户
"""

import getpass
import os
import sys
from django.contrib.auth.management import get_default_username
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.core.management.base import BaseCommand, CommandError
from django.utils.text import capfirst
from antd_pro.models import AntdUser
from django.contrib.auth.hashers import make_password


class NotRunningInTTYException(Exception):
    pass


PASSWORD_FIELD = 'password'


class Command(BaseCommand):
    help = 'Used to create a superuser.'
    requires_migrations_checks = True
    stealth_options = ('stdin',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = AntdUser
        self.phone_num_field = self.UserModel._meta.get_field('phone_num')
        self.password_field = self.UserModel._meta.get_field('password')

    def handle(self, *args, **options):
        phone_num = None
        password = None

        while phone_num is None:
            phone_num = self.get_input_data(field=self.phone_num_field, message='请输入手机号:')
        while password is None:
            password1 = getpass.getpass('请输入密码:')
            password2 = getpass.getpass('请再次输入密码:')
            if password1 != password2:
                self.stderr.write("错误: 两次密码输入不匹配！")
            else:
                password = password1
                break
        user, created = self.UserModel.objects.get_or_create(
            phone_num=phone_num,
            defaults={
                'password': make_password(password),
                'is_super': True
            }
        )
        if not created:
            self.stderr.write("错误: 用户已存在")

    def get_input_data(self, field, message, default=None):
        """
        Override this method if you want to customize data inputs or
        validation exceptions.
        """
        raw_value = input(message)
        if default and raw_value == '':
            raw_value = default
        try:
            val = field.clean(raw_value, None)
        except exceptions.ValidationError as e:
            self.stderr.write("Error: %s" % '; '.join(e.messages))
            val = None

        return val

    def _get_input_message(self, field, default=None):
        return '%s%s%s: ' % (
            capfirst(field.verbose_name),
            " (leave blank to use '%s')" % default if default else '',
            ' (%s.%s)' % (
                field.remote_field.model._meta.object_name,
                field.m2m_target_field_name() if field.many_to_many else field.remote_field.field_name,
            ) if field.remote_field else '',
        )
