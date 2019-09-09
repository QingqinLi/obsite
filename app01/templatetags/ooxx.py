# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django import template

# 固定写法，生成一个注册实例对象
register = template.Library()


@register.filter()  # 告诉django的模版语言我现在注册一个自定义的filter
def add_sb(value):
    """
    给任意指定的变量增加sb
    :param value: 被装饰的变量
    :return: 装饰后的变量内容
    """
    return value + 'sb'


@register.filter()
def add_str(value, s):
    return value + s