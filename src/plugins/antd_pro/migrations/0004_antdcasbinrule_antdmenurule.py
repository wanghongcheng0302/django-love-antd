# Generated by Django 3.2.4 on 2021-07-08 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antd_pro', '0003_delete_antdcasbinrule'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntdCasbinRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否软删除')),
                ('ptype', models.CharField(choices=[('p', '策略'), ('g', '角色')], max_length=10)),
                ('v0', models.CharField(blank=True, max_length=255, null=True)),
                ('v1', models.CharField(blank=True, max_length=255, null=True)),
                ('v2', models.CharField(blank=True, max_length=255, null=True)),
                ('v3', models.CharField(blank=True, max_length=255, null=True)),
                ('v4', models.CharField(blank=True, max_length=255, null=True)),
                ('v5', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'casbin规则',
                'verbose_name_plural': 'casbin规则',
                'db_table': 'casbin_rule',
            },
        ),
        migrations.CreateModel(
            name='AntdMenuRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否软删除')),
                ('route', models.CharField(max_length=255, verbose_name='路由')),
                ('roles', models.ManyToManyField(blank=True, to='antd_pro.AntdRole', verbose_name='角色')),
            ],
            options={
                'verbose_name': '菜单配置',
                'verbose_name_plural': '菜单配置',
            },
        ),
    ]
