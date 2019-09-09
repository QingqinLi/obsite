from django.db import models
# Create your models here.


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

    def __str__(self):  # 打印对象的时候打印出的内容
        return self.email


class Press(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    # Django 1.11 默认就是级联删除， Django 2.0之后必须指定on_delete
    # to=关联的表名
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to='Book')

    def __str__(self):
        return self.name

