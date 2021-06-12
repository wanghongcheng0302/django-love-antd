from django.db import models
from globals.models import BaseModel


class Permission(BaseModel):
    name = models.CharField(verbose_name='名称', max_length=50, unique=True)
    parent = models.ForeignKey(verbose_name='上级权限', to='self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = verbose_name


class Role(BaseModel):
    name = models.CharField(verbose_name='名称', max_length=50, unique=True)
    parent = models.ForeignKey(verbose_name='上级角色', to='self', on_delete=models.CASCADE, null=True, blank=True)
    permissions = models.ManyToManyField(verbose_name='权限集', to=Permission, blank=True)

    class Meta:
        verbose_name = '角色'
        verbose_name_plural = verbose_name


class User(BaseModel):
    GENDER_CHOICES = ((0, '女',), (1, '男',), (2, '其他'))
    openid = models.CharField(verbose_name='openid', max_length=255, unique=True)
    roles = models.ManyToManyField(verbose_name='角色集', to=Role, blank=True)
    nickname = models.CharField(verbose_name='昵称', max_length=50, unique=True)
    birthday = models.DateField(verbose_name='生日', blank=True, null=True)
    last = models.DateTimeField(verbose_name='上次登陆', blank=True, null=True)
    email = models.EmailField(verbose_name='邮箱', null=True, blank=True)
    phone = models.CharField(verbose_name='手机', max_length=13, null=True, blank=True)
    gender = models.PositiveSmallIntegerField(verbose_name='性别', choices=GENDER_CHOICES)
    brief = models.TextField(verbose_name='简介', null=True, blank=True)
    avatar = models.ImageField(verbose_name='头像', null=True, blank=True, upload_to='images')
    resume = models.FileField(verbose_name='简历', null=True, blank=True, upload_to='files')
    height = models.FloatField(verbose_name='身高', default=1.8)
    wallet = models.DecimalField(verbose_name='钱包', default=0, max_digits=10, decimal_places=2)
    married = models.BooleanField(verbose_name='是否结婚', default=False)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Group(BaseModel):
    users = models.ManyToManyField(verbose_name='用户群', to=User, blank=True)
    permissions = models.ManyToManyField(verbose_name='权限集', to=Permission, blank=True)

    class Meta:
        verbose_name = '组'
        verbose_name_plural = verbose_name
