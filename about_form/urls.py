# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.conf.urls import url
from about_form import views

urlpatterns = [
    url(r'^reg/', view=views.register, name="register")
]