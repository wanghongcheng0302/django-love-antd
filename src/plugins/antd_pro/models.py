from django.db import models
from antd_pro.globals.models import BaseModel
from django.core import validators


class AntdPermission(BaseModel):
    METHOD_CHOICES = (('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'))

    name = models.CharField(verbose_name="名称", max_length=50, unique=True)
    parent = models.ForeignKey(
        verbose_name="上级权限", to="self", on_delete=models.CASCADE, null=True, blank=True
    )
    method = models.CharField(verbose_name='请求方法', choices=METHOD_CHOICES, max_length=10)
    route = models.CharField(verbose_name='路由，支持正则', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = verbose_name


class AntdRole(BaseModel):
    name = models.CharField(verbose_name="名称", max_length=50, unique=True)
    parent = models.ForeignKey(
        verbose_name="上级角色", to="self", on_delete=models.SET_NULL, null=True, blank=True
    )
    # permissions = models.ManyToManyField(verbose_name="权限集", to=AntdPermission, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = verbose_name


class AntdUser(BaseModel):
    is_super = models.BooleanField(verbose_name='是否超管', default=False)
    roles = models.ManyToManyField(verbose_name='角色集', to=AntdRole, blank=True)
    phone_num = models.CharField(verbose_name='手机号', max_length=11, unique=True,
                                 validators=[validators.RegexValidator('1[345678]\d{9}', message='请输入正确的手机号')])
    password = models.CharField(verbose_name='密码', max_length=250)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class AntdUserProfile(BaseModel):
    GENDER_CHOICES = ((0, '女'), (1, '男'), (2, '其他'))
    user = models.OneToOneField(verbose_name='用户', to=AntdUser, on_delete=models.CASCADE, related_query_name='user_profile')
    avatar = models.ImageField(verbose_name='头像', upload_to='images', null=True, blank=True)
    birthday = models.DateTimeField(verbose_name='生日', null=True, blank=True)
    gender = models.PositiveSmallIntegerField(verbose_name='性别', null=True, choices=GENDER_CHOICES, blank=True)
    email = models.EmailField(verbose_name='邮箱', null=True, blank=True)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class AntdCasbinRule(BaseModel):
    PTYPE_CHOICES = (('p', '策略',), ('g', '角色',),)
    ptype = models.CharField(max_length=10, choices=PTYPE_CHOICES)
    v0 = models.CharField(max_length=255, null=True, blank=True)
    v1 = models.CharField(max_length=255, null=True, blank=True)
    v2 = models.CharField(max_length=255, null=True, blank=True)
    v3 = models.CharField(max_length=255, null=True, blank=True)
    v4 = models.CharField(max_length=255, null=True, blank=True)
    v5 = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'casbin_rule'
        verbose_name = 'casbin规则'
        verbose_name_plural = verbose_name

    def __str__(self):
        text = self.ptype

        if self.v0:
            text = text + ', ' + self.v0
        if self.v1:
            text = text + ', ' + self.v1
        if self.v2:
            text = text + ', ' + self.v2
        if self.v3:
            text = text + ', ' + self.v3
        if self.v4:
            text = text + ', ' + self.v4
        if self.v5:
            text = text + ', ' + self.v5
        return text


class AntdMenuRule(BaseModel):
    route = models.CharField(verbose_name='路由', max_length=255)
    roles = models.ManyToManyField(verbose_name='角色', blank=True, to=AntdRole)

    class Meta:
        verbose_name = '菜单配置'
        verbose_name_plural = verbose_name
