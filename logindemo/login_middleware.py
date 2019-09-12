# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse, redirect, reverse


class loginMd(MiddlewareMixin):
    def process_request(self, request):
        print("中间件执行了吗")
        path_info = request.path_info
        print(path_info)
        if path_info == '/logindemo/login/':
            return
        is_login = request.session.get("is_login")
        if is_login:
            print("已经登录，不需要拦截")
            return
        else:
            print("中间件拦截成功", 'login.html?next={}'.format(path_info))
            return redirect(reverse("logindemo:login") + "?next={}".format(path_info))