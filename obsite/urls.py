"""obsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from app01 import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'login/', admin.site.urls),
    # url(r"^login/$", views.login),
    url(r'app01/', include("app01.urls", namespace='app01')),
    url(r'logindemo/', include("logindemo.urls", namespace="logindemo")),
    url(r'about_middleware/', include("about_middleware.urls", namespace="about_middleware")),
    url(r'about_form/', include("about_form.urls", namespace="about_form")),
    url(r'about_auth/', include("about_auth.urls", namespace="about_auth")),
    url(r'about_ajax/', include("about_ajax.urls", namespace="about_ajax")),
    # url(r"^index/$", views.index),
    # url(r"^press_list/$", views.press_list),
    # url(r"^add_press/$", views.add_press),
    # url(r"^edit_press/$", views.edit_press),
    # url(r"^delete_press/$", views.delete_press),
    # url(r"^book_list/$", views.book_list),
    # url(r"^add_book/$", views.add_book),
    # url(r"^edit_book/$", views.edit_book),
    # url(r"^delete_book/$", views.delete_book),
    # url(r"^author_list/$", views.author_list),
    # url(r"^add_author/$", views.add_author),
    # url(r"^delete_author/$", views.delete_author),
    # url(r"^edit_author/$", views.edit_author),
    # url(r"^upload/$", views.upload),
    # url(r"^filtertest/$", views.tFilter),


]
