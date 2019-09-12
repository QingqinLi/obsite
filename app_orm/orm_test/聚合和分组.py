import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_pratice.settings")
    import django

    django.setup()

    from app01 import models

    from django.db.models import Max, Min, Sum, Avg, Count

    ret = models.Book.objects.aggregate(Max('price'), avg=Avg('price'))
    # print(ret)

    ret = models.Book.objects.annotate(Count('author')).values()

    ret = models.Publisher.objects.annotate(Min('book__price')).values()
    # print(ret)

    ret = models.Book.objects.values('publisher__name').annotate(min=Min('price'))

    # for i in ret:
    #     print(i)

    ret = models.Book.objects.annotate(count=Count('author')).filter(count__gt=1).values()
    # for i in ret:
    #     print(i)

    ret = models.Author.objects.annotate(Sum('books__price')).values()
    for i in ret:
        print(i)