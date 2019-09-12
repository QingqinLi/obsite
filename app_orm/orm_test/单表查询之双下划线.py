# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
__author__ = 'qing.li'
"""
import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_orm.settings")
    import django

    django.setup()

    from app_orm import models

    ret = models.Person.objects.filter(id__gt=1)  # greater than  大于
    ret1 = models.Person.objects.filter(id__lt=4)  # less than   小于
    ret2 = models.Person.objects.filter(id__gte=1)  # greater than equal  大于等于
    ret3 = models.Person.objects.filter(id__lte=1)  # less than equal  小于等于

    ret4 = models.Person.objects.filter(id__in=[1, 3])

    ret5 = models.Person.objects.filter(id__gte=1, id__lte=3)
    ret6 = models.Person.objects.filter(id__range=[1, 3])  # 前后都包括

    ret7 = models.Person.objects.filter(name__contains='e')
    ret8 = models.Person.objects.filter(name__icontains='e')

    ret9 = models.Person.objects.filter(name__startswith='e')
    ret00 = models.Person.objects.filter(name__istartswith='e')

    ret11 = models.Person.objects.filter(name__endswith='x')
    ret12 = models.Person.objects.filter(name__iendswith='x')

    # ret = models.Person.objects.filter(birth__year=2018)
    ret13 = models.Person.objects.filter(birth__day=11)

    print(ret)