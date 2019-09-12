# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "obsite.settings")
    import django
    django.setup()

    from app_orm import models

    ret = models.Person.objects.all()

    # get 获取的是对象，查询不到会报错，获取多个也会报错
    ret1 = models.Person.objects.get(id=1)

    ret2 = models.Person.objects.filter(sex=1)

    ret3 = models.Person.objects.exclude(sex=2)

    ret4 = models.Person.objects.all().values()  # 以字典的形式显示结果

    ret5 = models.Person.objects.all().values_list()  # 以元组的形式显示结果，每条结果一个元组，不包括字典名称，只包括字段的值
    # for i in ret5:
    #     print(i)

    ret6 = models.Person.objects.all().order_by("age", "-id")  # 先按照age排序，age一样的情况下按照id逆序排序
    # for i in ret6:
    #     print(i.age)

    ret7 = models.Person.objects.all().reverse()
    for i in ret7:
        print(i.id)

    ret8 = models.Person.objects.all().count()
    print(ret8)

    ret9 = models.Person.objects.all().first()
    print(ret9)

    ret10 = models.Person.objects.all().exists()
    print(ret10)
