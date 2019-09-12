from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View
from logindemo import models


# 装饰器避免对多个函数重复操作
def login_required(fn):
    def inner(request, *args, **kwargs):
        print(request.COOKIES, type(request.COOKIES))
        is_login = request.COOKIES.get("is_login")
        if is_login:
            ret = fn(request, *args, **kwargs)
        else:
            next = request.path_info
            ret = redirect(reverse("logindemo:login") + "?next={}".format(next))
        return ret
    return inner


# Create your views here.
class login(View):
    def dispatch(self, request, *args, **kwargs):
        ret = super().dispatch(request, *args, **kwargs)
        return ret

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get("email")
        pwd = request.POST.get("pwd")
        print(request.path_info)
        next = request.GET.get("next")
        print(username, pwd)
        ret = models.User.objects.filter(name=username, pws=pwd)
        if ret:
            if next:
            # print(reverse("logindemo:show_book"))
                print(next)
                ret = redirect(next)
            else:
                ret = redirect(reverse("logindemo:show_book"))
            # 设置cookie
            ret.set_cookie('is_login', '1', max_age=5)
            return ret
        else:
            return HttpResponse("error")


@login_required
def show_book(request):
    return render(request, 'author_list.html')


def logout(request):
    ret = redirect(reverse("logindemo:login"))

    ret.delete_cookie("is_login")

    return ret