from django.db import models


# Create your models here.
class MyCharFiled(models.Field):
    """
    自定义char类型的字段类
    """
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(MyCharFiled, self).__init__(max_length=max_length, *args, **kwargs)

    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为char， 长度为max_length指定的值
        :param connection:
        :return:
        """
        return 'char(%s)' % self.max_length


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, db_column='myname', verbose_name='姓名')
    age = models.IntegerField(null=True, blank=True)   # null数据库中字段是都可以为空，blank admin中是否允许用户输入为空
    birth = models.DateTimeField(auto_now=True)
    phone = MyCharFiled(max_length=11)
    sex = models.CharField(max_length=32, choices=(('1', '男'), ('2', '女')))

    def __str__(self):
        return '<Person %s-%s>' % (self.id, self.name)

    class Meta:
        ordering = ('id', )
        # 数据库表名
        db_table = 'person'
        # admin中显示的表名称
        verbose_name = '个人信息'
        verbose_name_plural = '所有用户信息'


class Publisher(models.Model):
    id = models.AutoField(primary_key=True)  # 一张表中不能有两个AutoFiled
    name = models.CharField(max_length=32)  # 出版社名称

    def __str__(self):
        return '<Publisher %s-%s>' % (self.id, self.name)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.IntegerField()
    publisher = models.ForeignKey(to='Publisher', null=True)
    sale = models.IntegerField()
    kucun = models.IntegerField()

    def __str__(self):
        return '<Book %s-%s>' % (self.id, self.title)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    books = models.ManyToManyField(to='Book',)  # 只是在ORM层面建立一个多对多的关系，不是作者表的一个字段

    def __str__(self):
        return self.name