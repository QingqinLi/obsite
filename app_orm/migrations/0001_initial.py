# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-11 03:13
from __future__ import unicode_literals

import app_orm.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('sale', models.IntegerField()),
                ('kucun', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='myname', max_length=32, verbose_name='姓名')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('birth', models.DateTimeField(auto_now=True)),
                ('phone', app_orm.models.MyCharFiled(max_length=11)),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], max_length=32)),
            ],
            options={
                'verbose_name': '个人信息',
                'verbose_name_plural': '所有用户信息',
                'db_table': 'person',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_orm.Publisher'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='app_orm.Book'),
        ),
    ]
