import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_pratice.settings")
    import django

    django.setup()

    from app01 import models

    # obj = models.Author.objects.get(id=1)

    # obj.books.set([])
    # obj.books.add(*models.Book.objects.all())
    # obj.books.add(2,3,4,5)
    # obj.books.remove(*models.Book.objects.all())
    # obj.books.remove(2,3)
    # obj.books.clear()
    # obj.books.create(title='跟景女神学茶道',price=25,publisher_id='1')

    obj = models.Book.objects.get(id=6)

    # print(obj.authors.all())


