# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.conf.urls import url
from logindemo import views_middleware

urlpatterns = [
    # path('login/', admin.site.urls),
    # url(r"^login/$", views.login),
    url(r'^login/', view=views_middleware.login, name='login'),
    url(r'^show_book/', view=views_middleware.show_book, name="show_book"),
    url(r'^logout/', view=views_middleware.logout, name='logout'),

    ]