# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""

from django.conf.urls import url
from about_middleware import views

urlpatterns = [
    url(r'^test', view=views.test, name="test"),
]
