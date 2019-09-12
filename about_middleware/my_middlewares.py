# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, HttpResponse


class MD1(MiddlewareMixin):
    def process_request(self, request):
        print(id(request))
        print("这是md1中的process_request方法")

    def process_response(self, request, response):
        print("process_response", id(request))
        print("这是md1中的process_response方法")

        return response  # 必须返回response对象
        # return HttpResponse("okk")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(id(request), view_func, view_args, view_kwargs)
        print("这是md1中的process_view方法")

        # return HttpResponse("process_view")

    def process_exception(self, request, exception):
        print("这是md1中的process_exceptions方法")

        return HttpResponse(str(exception))

    def process_template_response(self, request, response):
        print("这是md1中的process_template_response方法")

        return response


class MD2(MiddlewareMixin):
    def process_request(self, request):
        print(id(request))
        print("这是md2中的process_request方法")

    def process_response(self, request, response):
        print("process_response", id(request))
        print("这是md2中的process_response方法")

        return response  # 必须返回response对象
        # return HttpResponse("okk")

    def process_view(self, request, view_func, view_args, view_kwargs):
        print(id(request), view_func, view_args, view_kwargs)
        print("这是md2中的process_view方法")

        # return HttpResponse("process_view")

    def process_exception(self, request, exception):
        print("这是md2中的process_exceptions方法")

        return HttpResponse(str(exception))

    def process_template_response(self, request, response):
        print("这是md2中的process_template_response方法")

        return response