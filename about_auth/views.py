from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, redirect, render, reverse
from about_auth.form import LoginForm, RegForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AbstractBaseUser


def login(request):
    form_obj = LoginForm()
    if request.method == 'POST':
        form_obj = LoginForm(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data.get('username')
            password = form_obj.cleaned_data.get("password")
            obj = auth.authenticate(request, username=username, password=password)
            if obj:
                # 认证成功，记录登录状态
                auth.login(request, obj)
                next = request.GET.get("next")
                if next:
                    return redirect(next)
                return redirect(reverse("about_auth:index"))
            else:
                return HttpResponse("no this user")
        else:
            return HttpResponse("param is wrong")

    return render(request, 'login1.html', {'form_obj': form_obj})


# 装饰器 判断登录状态
@login_required()
def index(request):
    print(request.user.password)
    result = request.user.check_password("liqing123456")
    if result:
        request.user.set_password("liqing123")
        request.user.save()
    print("result", result)
    return render(request, 'author_list.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse("about_auth:login_test"))


def reg(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            username = form_obj.cleaned_data.get("username")
            password = form_obj.cleaned_data.get("password")
            User.objects.create_user(is_staff=1, username=username, password=password)
            return redirect(reverse("about_auth:login_test"))
    return render(request, 'reg.html', {'form_obj': form_obj})