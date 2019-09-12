import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_pratice.settings")
    import django

    django.setup()

    from app01 import models

    from django.db.models import F, Q

    ret = models.Book.objects.filter(kucun__gt=50).values()
    # for i in ret:
    #     print(i)

    ret = models.Book.objects.filter(sale__gt=F('kucun')).values()
    # for i in ret:
    #     print(i)

    # ret = models.Book.objects.filter(id=2).update(sale=100)

    # obj = models.Book.objects.get(id=2)
    # obj.sale='1000'
    # obj.save()

    # ret = models.Book.objects.all().update(sale=F('sale') * 2)

    ret = models.Book.objects.filter(id__gt=2, id__lt=10)

    ret = models.Book.objects.filter(Q(id__lte=3) | Q(id__gte=6))

    ret = models.Book.objects.filter(~Q(price__gte=10) & Q(sale__gte=3000)).values()

    for i in ret:
        print(i)
