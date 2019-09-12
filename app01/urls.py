from app01 import views
from django.conf.urls import url

urlpatterns = [
    url(r"^login/$", views.login,),
    url(r"^index/$", views.index),
    url(r"^press_list/$", views.press_list, name='press'),
    url(r"^add_press/$", views.add_press),
    url(r"^edit_press/$", views.edit_press),
    # url(r"^delete_press/$", views.delete_press),
    url(r"^book_list/$", views.book_list, name='book'),
    url(r"^add_book/$", views.add_book),
    url(r"^edit_book/$", views.edit_book),
    # url(r"^delete_book/$", views.delete_book),
    url(r"^author_list/$", views.author_list, name='author'),
    url(r"^add_author/$", views.add_author),
    # url(r"^delete_author/$", views.delete_author),
    url(r'^delete_(press|book|author)/(\d+)$', views.delete),
    url(r"^edit_author/$", views.edit_author),
    url(r"^upload/$", views.upload),
    url(r"^filtertest/$", views.tFilter),
    url(r'^home/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.home, name='h'),  # 命名分组
    url(r'^home2/(\d+)', views.home2, name='home2')  # 分组



]
