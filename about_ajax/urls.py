# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.conf.urls import url
from about_ajax import views

urlpatterns = [
    url('^index/', view=views.index, name='index'),
    url('^ajax_test', view=views.ajax_test, name='ajax_test')
]