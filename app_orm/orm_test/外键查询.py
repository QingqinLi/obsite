import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_pratice.settings")
    import django

    django.setup()

    from app01 import models
    # 基于对象的查询

    # book_obj = models.Book.objects.get(id=2)
    # print(book_obj.title)
    # print(book_obj.price)
    # print(book_obj.publisher_id)
    # print(book_obj.publisher)   # 出版社对象


    # obj = models.Book.objects.filter(publisher_id=models.Publisher.objects.get(name='沙河出版社').id)

    # obj = models.Book.objects.filter(publisher__name='沙河出版社')
    # print(obj)

    obj = models.Book.objects.all().values('title','publisher__name')
    # print(obj)


    # 反向查询

    obj = models.Publisher.objects.get(id=1)
    # print(obj.books.all())


    # obj = models.Publisher.objects.filter(id=models.Book.objects.get(title='跟太白学理发').publisher_id)

    # obj = models.Publisher.objects.filter(books__title='跟太白学理发')
    # print(obj)



    obj = models.Publisher.objects.get(id=1)

    # obj.books.set(models.Book.objects.filter(id__in=[2,3]))
    # obj.books.add(*models.Book.objects.filter(id__in=[4,5]))
    # obj.books.remove(*models.Book.objects.filter(id__in=[4,5]))

    obj = models.Publisher.objects.filter(xxxx__title='跟太白学理发')
    print(obj)
    print(models.Publisher.objects.get(id=1).book_set.all())



