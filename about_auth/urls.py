# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.conf.urls import url
from about_auth import views

urlpatterns = [
    url(r'^login_test/', view=views.login, name="login_test"),
    url(r'^index/', view=views.index, name='index'),
    url(r'^logout/', view=views.logout, name='logout'),
    url(r'^reg/', view=views.reg, name='reg'),
]