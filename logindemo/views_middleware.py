# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
from django.shortcuts import render, redirect, HttpResponse, reverse


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        name = request.POST.get("email")
        pwd = request.POST.get("pwd")
        next = request.GET.get("next")
        if name == 'lq' and pwd == 'liqing':
            request.session['is_login'] = '1'
            if next:
                return redirect(next)
            return redirect(reverse("logindemo:show_book"))
        else:
            return render(request, 'login.html')


def show_book(request):
    return render(request, "author_list.html")


def logout(request):
    request.session.flush()
    return render(request, 'login.html')